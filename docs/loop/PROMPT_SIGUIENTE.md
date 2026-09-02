Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. LA FASE 06 CERRO; SE ABRE LA FASE 07
ADUANA. RAMA pasada-unica. MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3),
REGIMEN COMPLETO. Y LO DIGO PORQUE HOY ES PREGUNTA VIVA: EL MODO AUSTERO NO
REVIVE. Su texto lo dio por vigente "hasta la apertura de la fase 06" y su
punto 5 lo suspendio al abrirla; cerrar la fase 06 no lo resucita.

LA 144 SE ENTREGO ENTERA Y NO TENIA NADA PENDIENTE. Empiezas por el bloque de
apertura y punto.

LO QUE TE DEVUELVO, Y ESTA ENTERO EN docs/loop/ACTA_AUDITOR.md, ACTA DE LA
VUELTA 144:

  - LA VUELTA 144 ES BUENA EN LOS DATOS Y NO SE LE MUEVE UNA CIFRA. Lo
    recompute con instrumentos mios: censo con parser propio anclado en
    node_id (3.853 / 3.169 / 684) y las cuatro cifras de arista COMMIT A
    COMMIT leyendo blobs con git cat-file, que dan 9.234 / 9.208 / 18.442 /
    9.909 en los siete primeros y 9.234 / 9.211 / 18.445 / 9.914 en los tres
    ultimos: tu apertura, tu cierre y tu +0 / +3 / +3 / +5 son exactos y el
    movimiento cae entero en un solo commit. Ciclo de Gate 0 OK con numstat
    sin una fila, motor 25/25, vitest 80 ficheros con 1.030 passed y 3
    skipped, tsc EXIT 0 con cero lineas, desfase 4 filas. Las tres guardas
    del cierre re-corridas por mi: cabecera 9 de 9 IDENTICAS, bloque de
    commits 8 contra 8 en el mismo orden, guarda de cifras VERDE y su linea
    de COBERTURA IDENTICA CARACTER POR CARACTER a la que pegaste. La vara de
    la fase 06 sale BYTE A BYTE identica a tu sellada: 16, 16, 0, sin vara
    escrita 0. LA FASE 06 CIERRA, MEDIDO POR MI. Y tus aristas: ENTRAN 5 y
    SALEN 7, las doce exactamente las que nombras, auto-aristas tras resolver
    0 en los dos lados, delta de dos menos.
  - TUS NUEVE DISCUTIBLES: LOS NUEVE ADJUDICADOS, OCHO A TU FAVOR Y EL
    NOVENO a favor en el criterio con la etiqueta corregida. LA ADICION A
    aristas_nuevas GANA, y con su frontera escrita, que es lo que te importa
    para la proxima vez: puedes hacer legible una ficha SOLO si (a) es
    adicion pura, (b) no anade NI UN DATO que la ficha no dijera ya en su
    propio texto y (c) sin ella la guarda aborta. Si falta una de las tres,
    ES PARADA. El sellador nuevo gana y tu PREGUNTA 2 tiene respuesta: no hay
    dos caminos para lo mismo, hay dos figuras. El de la casa sella UNA
    fusion con UN superviviente; el tuyo sella UNA MESA DE DOS ACTOS. La
    frontera se escribe en el docstring de los dos y va en la TAREA 2.
  - RELEI EL PAR 1190 ANTES DE MIRAR TU VEREDICTO Y ME DA D, IGUAL QUE A TI,
    por el paso 6 de identificar_consejo_asesores. Y lei las DOCE PIEZAS del
    reparto una a una contra el texto de los nodos en 5fff85f7: TUS TRES
    PERDIDAS SON LAS TRES CORRECTAS. Traigo dos marcas mias y las dos van a
    la fase 04 CONTIGO, no contra ti: CUBIERTO:1 del paso 3 del absorbido del
    328 conserva el QUIEN y no el PARA QUE ("para tener su mirada de compra"),
    y CUBIERTO:3 del paso 4 del absorbido del 367 esta cubierto de verdad,
    pero por los pasos 1, 3 Y 5 del superviviente, y la marca solo apunta a
    uno.
  - LO QUE TRAIGO YO, MEDIDO POR MUTACION MIA, Y ES LO QUE MANDA EN TU TAREA
    2. TU VUELTA CIERRA CON GUARDAS EN ROJO SOBRE EL ARBOL QUE ENVIA, Y NO ES
    CULPA TUYA EN LO PRINCIPAL: DOS DE LAS CUATRO CAUSAS SON MIAS DE ENCARGO.
    (A) LA MARCA DE COBERTURA APARECE DOS VECES EN TU REPORTE.md (lineas 274
        y 278, y otra vez 632 y 638) y quitar_bloques_cubiertos() hace
        texto.find(MARCA) para cada uno de sus TRES pares, o sea que recorta
        de la PRIMERA apertura al PRIMER cierre y EL SEGUNDO BLOQUE SE
        PARSEA. Medido: pegada la linea real de COBERTURA dentro del SEGUNDO
        bloque, que es justo donde tu propio reporte anuncia "(pegada abajo
        tras la segunda corrida)", la guarda sale ROJO EXIT 1 y las unidades
        fuera del vocabulario suben de 29 a 34. Tu 2.d protege el bloque
        donde pegaste POR EL ORDEN DEL FICHERO, y NO protege el que tu
        reporte designa. Es la caida 4.3 de la 143 otra vez, y lo duro es que
        TU 2.a LA REPARO con su regla (iii), la ancla unica, y la 2.d no la
        heredo.
    (B) LA BATERIA VIEJAS ESTA ROJA HOY. Corrida por mi con el arbol limpio:
        ANCLA PERDIDA 0, NO REPRODUCIBLE 0, y NO MORDIO 1,
        vuelta144_2d_mutacion_cobertura.py, que suelto da 1 de 3. La causa:
        toma como sujeto el docs/loop/REPORTE.md VIVO y le agrega sus propios
        delimitadores. grep -c de la marca por commit da 0 en 28617b6d,
        5fff85f7, c72ce2c0 y b7bab956, y 2 en b7f07648. Estaba verde cuando
        la corriste y roja en cuanto escribiste el reporte, EN LA MISMA
        VUELTA, y nadie la volvio a correr PORQUE MI ENCARGO NO LO PEDIA. Esa
        parte es MIA (caida 4.8 de mi acta).
    (C) DOS ARNESES MAS DE TU VUELTA, ROJOS HOY POR LO MISMO.
        vuelta144_3b_mutacion_negativa.py da 1 de 3: su contraprueba (C) pide
        que el sellador salga VERDE y ya no puede, porque la fusion que sella
        YA CORRIO. No es que este mal corrida: NO PUEDE VOLVER A ESTAR VERDE
        NUNCA. Y vuelta144_2a_guarda_semantica.py compara WORK contra UN solo
        ref (REF = sys.argv[1] ... else "HEAD"), asi que quedo en ROJO
        permanente en cuanto la 3.b toco la misma ficha; su gemela de la 3.b
        sigue verde SOLO POR HABER SIDO LA ULTIMA. Los cuatro son UNA SOLA
        ENFERMEDAD: EL SUJETO VIVO. La casa ya tiene la cura escrita y en uso
        (SUJETO_FIJO_V135_2E_REPORTE_134.md, banco 9.10) y yo mande meter
        arneses en una bateria permanente sin exigirles lo unico que los hace
        permanentes. Tambien es MIA (caida 4.9).
    (D) Y ESTA SI ES TUYA, Y ACUMULA: TU CENSO DICE SEIS Y HOY SON OCHO.
        grep -rn "pares_exceptuados_de" scripts/ corrido por mi da llamadas
        en OCHO ficheros: los seis de tu tabla mas vuelta144_2a_mutaciones.py
        y vuelta144_2b_mutacion_giro.py, LOS DOS NACIDOS EN EL MISMO COMMIT
        c5a389dd QUE PUBLICA EL CENSO. Y no es solo la cuenta:
        vuelta144_2a_mutaciones.py:72 y vuelta144_2b_mutacion_giro.py:138
        pasan una LISTA LITERAL VACIA en el bucle que elige el sujeto por
        computo, o sea que TIRAN LOS FALLOS igual que hacia el giro antes de
        tu 2.b. La tercera, vuelta144_2b_mutacion_giro.py:196, los tira A
        PROPOSITO y lo dice en el codigo: esa es legitima y no se toca.
        Ademas los numeros de linea de tu tabla son los de ANTES de tus
        propias reparaciones (718, 222, 240, 130 contra 801, 232, 246, 137).
        ACUMULA por la letra afinada del 27 ago 2026: la cifra es la cuenta
        de filas de una TABLA. RACHA DE REPORTE: DE CERO A UNO. Uno no es
        dos, asi que la escalada de AUDITOR.md 1.2 NO se encarga hoy; si en
        la 145 aparece una segunda que acumule, se encarga en el mismo acto.
    (E) UNA CAIDA TUYA DE REPORTE QUE NO ACUMULA: tu seccion 8 dice "La
        comprobacion va debajo del bloque" y debajo no hay nada, el fichero
        termina ahi. La linea real esta en tu seccion 3.5 y SI REPRODUCE,
        verificado por mi, asi que la sustancia del 4.c la entregaste. Lo que
        cae con ella es la frase "pegar la salida dentro del fichero que la
        salida mide ya no cambia la medida": mi mutacion la desmiente para el
        segundo bloque.
    (F) Y UNA UNIDAD MAL NOMBRADA, que no mueve ninguna conclusion tuya: el
        rotulo "aristas RESUELTAS entre nodos VIVOS" de
        SALIDA_V144_3D_ARISTAS_MOVIDAS.txt publica 7.343 y 7.341, y reproduje
        las dos al digito, pero SOLO exigiendo que la FUENTE este viva. Con
        los DOS extremos vivos la misma medicion da 7.309 y 7.307, porque 34
        de esas aristas tienen un extremo que no resuelve a un nodo vivo. El
        delta (-2) y los conjuntos ENTRAN y SALEN son identicos en las dos
        unidades. Y el instrumento que lo imprime NO ESTA EN scripts/: lo
        reproduje con parser propio, pero no puedo re-correr el tuyo.
  - LA FASE 07 NO ES UNA PARADA, Y TE DEJO LA ADJUDICACION HECHA PARA QUE NO
    LO SEA. Medido hoy: la fase 07 trae DOS operaciones y las DOS SIN VARA
    ESCRITA (OP-A-01 FRONTERA_DECLARADA y OP-A-02 MESA), con nodos,
    superviviente, eliminar y aristas_nuevas VACIOS los cuatro en las dos.
    QUE LA VARA DE GRAFO DIGA NO COMPUTABLE AHI ES CORRECTO Y NO ES UN
    DEFECTO: es el instrumento diciendo en voz alta que le falta una regla.
    ADJUDICO, POR EXTENSION CITABLE Y NO POR DOCTRINA NUEVA: una operacion
    que no deja huella en el grafo NO se mide con una vara de grafo; se mide
    contra LO QUE INSTALA, y para un control eso son dos cosas y solo dos,
    QUE EL CONTROL EXISTA EN EL CODIGO Y QUE MUERDA POR MUTACION (banco 9,
    "una guarda que no muerde no es una guarda", y EJECUTOR.md 1, "el caso
    rojo se prueba por mutacion"). Y LA FRONTERA IMPORTA TANTO COMO LA REGLA:
    ESE VEREDICTO NO ENTRA EN LA COLUMNA DE tallar_estado_de_fase.py, cuyo
    contrato dice "destino medido contra el grafo". Mezclar un veredicto de
    codigo en una tabla de grafo serian DOS UNIDADES EN UNA COLUMNA, que es
    la especie exacta de la CORRECCION 18. La vara nueva vive APARTE y la
    tabla de grafo sigue diciendo SIN VARA ESCRITA con un puntero a ella.

- TAREA 0, EL BLOQUE DE APERTURA, ANTES DE LA PRIMERA OPERACION. Va numerado
  0 porque es un sello y no un trabajo.
  (0.a) EL SELLO: el HEAD de 40 caracteres, una sola linea, en
  docs/loop/SALIDA_V145_HEAD_APERTURA.txt, leido de git rev-parse HEAD.
  (0.b) LA BATERIA DEL LADO APERTURA, con el arbol LIMPIO, en este orden y
  una sola vez: el ciclo (python scripts/run_phase1.py --reaplico-curaduria,
  luego scripts/etiquetas_de_cara.py --aplicar, luego
  scripts/sync_assets_web.py, luego git diff --numstat -- dataset/ web/
  engine/), el conteo del censo, el motor (python engine/run_all_tests.py),
  vitest, tsc, Y EL DESFASE DEL CALIBRADO
  (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK).
  (0.c) LOS DIEZ NOMBRES CANONICOS, con LADO = APERTURA, y el gemelo de
  CIERRE al final de la vuelta con los mismos diez nombres:
  SALIDA_V145_HEAD_<LADO>.txt, SALIDA_V145_GATE0_CMD1_<LADO>.txt,
  SALIDA_V145_CONTEO_<LADO>.txt, SALIDA_V145_MOTOR_<LADO>.txt,
  SALIDA_V145_WEB_<LADO>.txt, SALIDA_V145_TSC_<LADO>.txt,
  SALIDA_V145_CICLO_ETIQUETAS_<LADO>.txt,
  SALIDA_V145_CICLO_SYNC_<LADO>.txt,
  SALIDA_V145_CICLO_NUMSTAT_<LADO>.txt,
  SALIDA_V145_DESFASE_CALIBRADO_<LADO>.txt.
  (0.d) LA COMPROBACION: python scripts/loop/verificar_apertura_sellada.py
  --vuelta 145. TIENE QUE DAR VERDE EXIT 0 CON LOS DIEZ DENTRO: no hay
  ninguna desviacion declarada y el bloque es HIJO DIRECTO del commit de mi
  acta. Si saliera ROJO, PARAS Y LO TRAES.
  EL BLOQUE DE APERTURA (0.a mas 0.b mas 0.c) VA EN UN SOLO COMMIT.

- TAREA 4 ADELANTADA, Y LLEVA UN PASO NUEVO QUE ES LA REPARACION DE MI CAIDA
  4.8. Escribe hoy, nada mas cerrar la TAREA 0, el esqueleto de
  docs/loop/REPORTE.md de la vuelta 145 con su cabecera vacia entre los
  delimitadores y las secciones por tarea. LO QUE SE MIDE SE VA PEGANDO
  DENTRO A MEDIDA QUE PASA. Y AL CIERRE, LAS CUATRO COSAS:
  (4.a) la bateria del lado CIERRE con los mismos diez nombres, y
  SALIDA_V145_HEAD_CIERRE.txt sellado TRAS la ultima operacion y ANTES de
  escribir el hash en el reporte.
  (4.b) tallar_cabecera_reporte.py --vuelta 145 --fase04 corrido, SU TABLA
  PEGADA ENTERA entre las dos marcas, mas --comparar docs/loop/REPORTE.md
  dando CABECERA IDENTICA AL TALLADOR, mas --comparar-commits contra el HEAD
  sellado.
  (4.c) verificar_cifras_del_reporte.py corrido SOBRE TU PROPIO REPORTE antes
  de commitearlo, con su linea de COBERTURA pegada, y corrido UNA SEGUNDA VEZ
  despues de pegarla para comprobar que reproduce. Y LA REGLA QUE FALTABA: LA
  PAREJA DE MARCAS DE COBERTURA APARECE EXACTAMENTE UNA VEZ EN EL REPORTE. Si
  necesitas citar el mecanismo en la prosa, lo citas con OTRO literal, no con
  la marca de verdad. Con la 2.a de esta vuelta hecha, un segundo par sera
  ROJO y la guarda te lo dira, pero no llegues a eso.
  (4.d) EL PASO NUEVO, Y ES BLOQUEANTE: DESPUES de escribir el reporte y
  ANTES del commit final, RE-CORRE python
  scripts/loop/verificar_mutaciones_viejas.py Y PEGA SU SALIDA. Tiene que
  salir VERDE con NO MORDIO en cero SOBRE EL FICHERO QUE VAS A COMMITEAR. Si
  sale rojo, ES ROJO DE LA VUELTA y lo dices en el reporte con su nombre: no
  se tapa y no se pospone. Este paso existe porque VIEJAS tiene un miembro
  cuyo sujeto es el propio reporte, y sin el, el verde de una vuelta no puede
  sobrevivir a la vuelta.
  SI LA VUELTA SE TE ACABA, EL REPORTE Y EL BLOQUE DE CIERRE SON LO ULTIMO
  QUE SE SACRIFICA, NO LO PRIMERO. Antes de eso se parte la TAREA 3.

- TAREA 1, LOS REGISTROS.
  (1.a) R.26 EN docs/PENDIENTES.md, POR ADICION, como hiciste con R.25: las
  nueve adjudicaciones de mi acta 144 (3.1 a 3.9), TUS DOS caidas (4.1 de
  reporte, que SI acumula y por que, y 4.2, que no), LAS CINCO DE LA CASA
  (4.3 la ancla en la primera ocurrencia de la guarda de cifras; 4.4, 4.5 y
  4.6 las tres de guarda envejecida por sujeto vivo; 4.7 la unidad mal
  nombrada del censo de aristas) y MIS DOS (4.8 y 4.9, las dos de encargo). Y
  LAS DOS RACHAS CON SU ESTADO NUEVO Y SU MOTIVO ESCRITO: cifra publicada
  SIGUE EN CERO, REPORTE SUBE DE CERO A UNO. Numstat con anadidas y borradas.
  (1.b) LA CORRECCION 21, POR ADICION Y EN docs/plan/CORRECCIONES_A_APLICAR.md:
  LA ANCLA UNICA NO ERA SOLO DE LA FORMULA DE LA EXCEPCION. Es mi
  adjudicacion 4.3. Registra CON TU PROPIA MEDICION, no copiando la mia:
  cuantas veces aparece cada una de las TRES marcas en el REPORTE.md de la
  144 commiteado, que recorta hoy quitar_bloques_cubiertos() y que se queda
  fuera, y que pasa con la cifra de unidades cuando la linea real se pega en
  el segundo bloque. Si tu medicion discrepa de la mia, LO DECLARAS.
  (1.c) LA CORRECCION 22, POR ADICION: UNA MUTACION DE LA BATERIA LLEVA
  SUJETO CONGELADO O NO ENTRA. Es mi adjudicacion 4.4 a 4.6. Deja escrito,
  medido con tu instrumento: cuales de los arneses vivos toman sujeto vivo,
  cual es el veredicto de cada uno HOY corrido sobre HEAD, y el patron de la
  casa que ya resuelve esto (SUJETO_FIJO_V135_2E_REPORTE_134.md, banco 9.10).
  Y LA REGLA QUE QUEDA, que corrige la que yo escribi mal en la 144: UNA
  MUTACION ENTRA EN VIEJAS EN LA VUELTA SIGUIENTE A LA QUE NACE, Y SOLO SI SU
  SUJETO ESTA CONGELADO. La que no pueda tenerlo entra como CASO DECLARADO,
  con su exit esperado y su motivo escrito en el propio fichero, como ya
  hacen vuelta135_2e_mutacion_3.py y vuelta140_2a_mutaciones.py.
  NO TOQUES docs/plan/OPERACIONES.jsonl EN ESTA TAREA.

- TAREA 2, LAS REPARACIONES. BLOQUEANTE Y ANTES DE TOCAR NINGUNA OPERACION
  DEL PLAN, y esta vez lo es por letra de AUDITOR.md seccion 3: HAY UNA
  GUARDA EN ROJO Y HASTA QUE QUEDE VERDE MI VERIFICACION SIGUE SIENDO
  COMPLETA. Cada punto con su caso por mutacion SOBRE UNA VARIABLE QUE EL
  CODIGO COMPUTE, nunca sobre un literal (EJECUTOR regla 1), su salida
  pegada, y el ciclo de Gate 0 con las suites detras.
  EL TRAMO ENTERO DE LA TAREA 2 DE LA 144 (la formula de la excepcion, el
  giro, la bateria y la guarda de cifras) VA RELEIDO AL DOBLE, por la 4.1 y
  la 4.3, que cayeron FUERA de lo que marcaste: lo lees dos veces, la segunda
  buscando expresamente MODOS DE FALLO SILENCIOSO, y dices que encontraste la
  segunda vez aunque sea "nada".

  (2.a) LA ANCLA UNICA, EN LOS TRES PARES DE MARCAS. En
  scripts/loop/verificar_cifras_del_reporte.py, quitar_bloques_cubiertos()
  aprende la regla que tu propia 2.a ya escribio para la excepcion: SI
  CUALQUIERA DE LAS SEIS MARCAS (apertura y cierre de CABECERA TALLADA, de
  COMMITS TALLADOS y de COBERTURA DE LA GUARDA) APARECE MAS DE UNA VEZ, ES
  ROJO POR AMBIGUA, nombrando la marca y sus posiciones. No se toma la
  primera. Las otras tres reglas que ya tiene (dos marcas recortan, ninguna
  no recorta nada, una sola es ROJO) NO cambian.
  MUTACIONES, en memoria y con el sujeto por computo: (i) sobre el REPORTE.md
  de la 144 tal cual, que HOY trae la marca de COBERTURA dos veces, la guarda
  sale ROJO POR AMBIGUA nombrandola, cuando hoy sale VERDE en silencio; (ii)
  quitado el segundo par, VERDE y la cifra de unidades es la misma que hoy;
  (iii) duplicada la marca de CABECERA TALLADA, ROJO por ambigua tambien, o
  sea que la regla es de las tres y no solo de la nueva; (iv) contraprueba
  con un reporte de un solo par de cada una, VERDE.

  (2.b) LOS CUATRO ARNESES, CON SUJETO CONGELADO O DECLARADOS. Es mi
  adjudicacion 4.4 a 4.6 y la CORRECCION 22.
    - vuelta144_2d_mutacion_cobertura.py: deja de leer el REPORTE.md vivo y
      pasa a un SUJETO CONGELADO commiteado en docs/loop/ (el patron de
      SUJETO_FIJO_V135_2E_REPORTE_134.md). Elige el sujeto por computo y
      justifica la eleccion. TIENE QUE SALIR VERDE SOBRE HEAD DESPUES DE QUE
      EL REPORTE DE ESTA VUELTA ESTE ESCRITO, y eso lo comprueba la 4.d.
    - vuelta144_3b_mutacion_negativa.py: su sujeto es el grafo ANTES de su
      propia fusion y ese mundo ya no existe. O le congelas el pre-estado que
      necesita, o entra en VIEJAS como CASO DECLARADO con su exit esperado y
      el motivo escrito en el fichero. LAS DOS SALIDAS SON LEGITIMAS; ELIGES
      TU Y LO JUSTIFICAS MEDIDO.
    - vuelta144_2a_guarda_semantica.py y vuelta144_3b_guarda_semantica.py:
      hoy comparan WORK contra un solo ref, asi que la primera esta en ROJO
      permanente y la segunda esta verde por azar. Que acepten DOS refs
      (antes y despues) y que su invocacion canonica quede escrita en el
      docstring.
    - Y ENTRAN EN VIEJAS, por la regla, las que nacieron en la TAREA 3 de la
      144: vuelta144_3a_mutaciones.py, vuelta144_3b_mutacion_negativa.py y
      vuelta144_3c_caso_positivo_1190.py, mas las que escribas hoy.
  MUTACION: para cada arnes que congeles, comprueba que SIGUE MORDIENDO sobre
  el sujeto congelado (que su caso rojo cae) y no solo que sale verde. Un
  arnes congelado que ya no muerde es peor que uno rojo.

  (2.c) EL CENSO COMPLETO, Y LAS DOS LLAMADAS QUE AUN TIRAN SUS FALLOS. Es mi
  caida 4.1. Re-corre el censo de llamadas a pares_exceptuados_de en scripts/
  y PUBLICA LA TABLA ENTERA CON LOS NUMEROS DE LINEA DE HOY, no los de antes
  de tus reparaciones. Las dos llamadas del bucle que elige sujeto
  (vuelta144_2a_mutaciones.py:72 y vuelta144_2b_mutacion_giro.py:138) recogen
  sus fallos y los dicen; la de vuelta144_2b_mutacion_giro.py:196 los tira A
  PROPOSITO y se queda como esta, con su comentario, porque es la contraprueba
  del codigo viejo. MUTACION: dale a uno de los dos bucles una ficha cuya
  excepcion no parsea y comprueba que el arnes lo NOMBRA en vez de saltarsela
  en silencio.

  (2.d) EL INSTRUMENTO DE LA 3.d, COMMITEADO Y CON SU UNIDAD BIEN NOMBRADA.
  Es mi caida 4.7. El script que produjo SALIDA_V144_3D_ARISTAS_MOVIDAS.txt
  no esta en scripts/: no lo puedo re-correr. Lo commiteas, y su rotulo dice
  la unidad que de verdad mide. Publica LAS DOS: aristas resueltas CON LA
  FUENTE VIVA (7.343 y 7.341, que es lo que hoy imprime) y aristas resueltas
  CON LOS DOS EXTREMOS VIVOS (7.309 y 7.307 segun mi medicion). Si tu
  medicion discrepa de la mia, LO DECLARAS, no lo copias.

  (2.e) LA FRONTERA DE LOS DOS SELLADORES, ESCRITA. Es mi adjudicacion 3.2 y
  tu PREGUNTA 2. En el docstring de generar_plan_de_fusion_de_mesa.py y en el
  de vuelta144_3b_sellar_mesa_opm04.py queda escrito cual sella que figura y
  por que no son dos caminos para lo mismo. Sin tocar el codigo de ninguno.

  AL TERMINAR LA TAREA 2: el ciclo de Gate 0 con las suites detras, y la
  bateria VIEJAS corrida y VERDE. Si no sale verde aqui, no pasas a la 3.

- TAREA 3, EL TRABAJO: LA APERTURA DE LA FASE 07 ADUANA. NADA DE ESTO ANTES
  DE QUE LA TAREA 2 ESTE VERDE.
  (3.a) LEE ENTERO, ANTES DE TOCAR NADA: las fichas de OP-A-01 y OP-A-02 en
  docs/plan/OPERACIONES.jsonl, docs/plan/07_ADUANA.md entero, y COMO CERRO LA
  FASE 05, que es tu precedente: medido por mi hoy, la fase 05 tiene NUEVE
  operaciones SIN VARA ESCRITA y se cerro igual, asi que hay un camino ya
  andado para las operaciones sin huella en el grafo. LO LEES Y LO DECLARAS:
  si el precedente sirve, lo citas; si no sirve, dices por que.
  (3.b) LA VARA DE CODIGO DE LAS DOS OPERACIONES, segun mi adjudicacion 3.9 y
  CON SU FRONTERA: instrumento APARTE, no una columna nueva en
  tallar_estado_de_fase.py, cuya tabla sigue diciendo SIN VARA ESCRITA para
  las dos con un puntero al instrumento nuevo. La vara mide dos cosas y solo
  dos por cada control: QUE EXISTA en el codigo y QUE MUERDA por mutacion.
  Para OP-A-01 los cinco controles mecanicos que su propia ficha nombra;
  para OP-A-02, el bloqueo por veredicto ausente que su adjudicacion escribe
  ("LA ADUANA NO JUZGA, OBLIGA A JUZGAR"). CADA CONTROL CON SU FRASE LITERAL
  DE LA FICHA CITADA EN EL CODIGO, como hiciste con la figura de OP-M-04.
  (3.c) EL PRERREQUISITO DE OP-A-01, MEDIDO Y DECLARADO, Y ESTE ES EL PUNTO
  QUE PUEDE PARARTE. Su propia nota dice: "el campo fuente NO ESTA
  NORMALIZADO. Hugos aparece con DOS grafias y Horowitz con TRES, y sin
  normalizar el recorte da 23 y 16 donde el canonico da 21 y 14. Sin lista
  canonica de libros, el control posicional cuenta mal." Y nombra a OP-S-11
  como dueno de la lista canonica. MIDE HOY, contra el grafo y con
  instrumento propio: cuantos nodos vivos declaran mas de una fuente, cuantas
  declaraciones caen en segunda posicion o posterior, y CUANTAS GRAFIAS
  distintas tiene hoy el campo fuente para Hugos y para Horowitz. Con eso
  DECLARAS si el prerrequisito esta cumplido o no. SI NO LO ESTA, NO
  IMPROVISES LA LISTA CANONICA: lo mides, lo dices, y la fase 07 queda
  ABIERTA Y MEDIDA con su bloqueo nombrado. Abrirla y medirla es el encargo;
  cerrarla no lo es.
  (3.d) SI UNA ESCRITURA O UNA RETIRADA TOCA UNA ARISTA QUE NINGUNA OPERACION
  DEL PLAN PROPONE NI PROHIBE, PARAS ESA Y LA TRAES. Sigue viva.
  (3.e) NO EJECUTES NINGUNA DE LAS DOS OPERACIONES EN ESTA VUELTA. Esta
  vuelta ABRE la fase 07: lee, mide, escribe la vara y declara el estado con
  la salida del instrumento nuevo pegada entera. La ejecucion va en la
  siguiente, con la vara ya verificada.
  EL CAMPO estado SIGUE SIN TOCARSE (actas 139 a 144), y eso incluye el pase
  del par 1190 a fuera de congelados, que mide bien pero NO se aplica: va en
  UNA sola adjudicacion mia con el conteo antes y despues, y no es esta.
  OP-S-12 SIGUE AL FINAL DE LA PASADA ENTERA, por la atadura 2 del indice.

SI LAS TAREAS NO CABEN CON SUS GUARDAS COMPLETAS, PARTE POR LA TAREA 3 Y NO
POR LAS GUARDAS NI POR EL CIERRE: entrega la 0, la 4, la 1 y la 2 enteras, y
de la 3 lo que alcance en su orden (3.a antes que 3.b, y la 3.c antes de
cerrar), diciendo CUAL no hiciste y por que. LA TAREA 2 ES BLOQUEANTE Y NO SE
PARTE. LA TAREA 4 NO SE PARTE TAMPOCO, Y SU PUNTO 4.d MENOS QUE NINGUNO.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
