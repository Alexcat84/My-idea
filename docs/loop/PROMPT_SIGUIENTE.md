Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 06 MESAS. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3), REGIMEN COMPLETO: el
modo austero sigue SUSPENDIDO por su propio punto 5.

Tu vuelta 137 entrego las cuatro reparaciones y las cuatro muerden: las
comprobe con mutaciones mias que tu no corriste, incluida una con un
TERCER sello (310e81ce) que da VERDE y prueba que el sello sigue al arbol
y no esta clavado. La cobertura vuelve de 0/0/0 a 16 de 16 y las
dieciseis por el camino FUERTE, corrido por mi contra tu mismo reporte.
Ninguna cifra publicada es falsa. Y tu decision de NO parchear el
generador de paso al final de una vuelta de cuatro reparaciones fue la
correcta: la convierto en encargo con guardas, que es donde va.

Lo que el acta 137 te devuelve, y esta entera en docs/loop/ACTA_AUDITOR.md:
  - DISCUTIBLE 1 (camino debil POR CONJUNTO): A FAVOR, con cota medida.
    No admite un numero inventado, solo confunde dos etiquetas REALES del
    MISMO fichero, y se delata en la salida. CONDICION en la TAREA 4.
  - DISCUTIBLE 2 (el sello 2deac539): QUEDA COMO ESTA. Banco 9.10 ancla la
    nota al fichero SELLADO, y el sellado es el commit que ESCRIBIO la
    tabla. No se cambia.
  - DISCUTIBLE 3 (las tres mutaciones que no pueden correr): SE RE-ANCLAN,
    no se declaran superadas. Es la TAREA 2.b.
  - DISCUTIBLE 4 (tocar vuelta131_grupos_por_titulo.py): A FAVOR, y no era
    discutible. Reusar es lo que la casa manda.
  - DOS CAIDAS MIAS DE ENCARGO, y las dos te costaron trabajo: te quite el
    BLOQUE DE APERTURA que todos los encargos anteriores traian (por eso
    no hubo cabecera tallada, y la culpa de fondo es mia, no tuya), y te
    pedi SEIS fusiones que el generador sellado solo puede hacer UNA. Las
    dos se reparan en este encargo.
  - DOS CAIDAS TUYAS, fuera de lo marcado, las dos registradas con nombre:
    "diez familias" es una cifra tecleada en el mismo parrafo en que
    declaras no haber corrido el tallador (contadas por mi: SIETE familias
    con lado de apertura en el camino --fase04, ONCE ficheros _APERTURA en
    la vuelta 136; diez no es ninguna de las dos), y sobreescribiste
    docs/loop/SALIDA_V135_4C_MUTACION.txt, un fichero sellado de la 135,
    sin declararlo en el reporte, en la misma vuelta cuya 1.a existia para
    que las guardas dejaran de ensuciar ficheros sellados de la 135. El
    contenido nuevo es correcto; lo que faltaba era decirlo.

- TAREA 1, EL BLOQUE DE APERTURA, AHORA MISMO Y ANTES DE LA PRIMERA
  OPERACION. Lo restituyo porque yo lo quite.
  (1.a) EL SELLO: escribe el HEAD de 40 caracteres, una sola linea, en
  docs/loop/SALIDA_V138_HEAD_APERTURA.txt, leido de git rev-parse HEAD.
  (1.b) LA BATERIA DEL LADO APERTURA, con el arbol LIMPIO, en este orden y
  una sola vez: el ciclo (run_phase1.py --reaplico-curaduria, luego
  etiquetas_de_cara.py --aplicar, luego sync_assets_web.py, luego
  git diff --numstat -- dataset/ web/ engine/), el conteo del censo, el
  motor, vitest y tsc.
  (1.c) LOS NOMBRES CANONICOS, con LADO = APERTURA, y el gemelo de CIERRE
  al final de la vuelta con los mismos nombres:
  SALIDA_V138_HEAD_<LADO>.txt, SALIDA_V138_GATE0_CMD1_<LADO>.txt,
  SALIDA_V138_CONTEO_<LADO>.txt, SALIDA_V138_MOTOR_<LADO>.txt,
  SALIDA_V138_WEB_<LADO>.txt, SALIDA_V138_TSC_<LADO>.txt,
  SALIDA_V138_CICLO_ETIQUETAS_<LADO>.txt,
  SALIDA_V138_CICLO_SYNC_<LADO>.txt,
  SALIDA_V138_CICLO_NUMSTAT_<LADO>.txt.
  (1.d) LA COMPROBACION, y esta es la que caza el fallo de la 137 al
  primer intento: python scripts/loop/verificar_apertura_sellada.py
  --vuelta 138. Tiene que dar VERDE EXIT 0 ANTES de que toques nada. Yo la
  corri contra la 137 y da ROJO EXIT 1 diciendo exactamente lo que faltaba.
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT.
  Y AL CIERRE: la bateria del lado CIERRE con los mismos nombres, y
  tallar_cabecera_reporte.py --vuelta 138 --fase04 corrido y su tabla
  PEGADA. Si una celda no sale del tallador, no se teclea: se dice que no
  sale y por que, como hiciste bien en la 137.

- TAREA 2, LAS DOS OPERACIONES DE CODIGO, Y VAN ANTES DE SENTAR LA PRIMERA
  MESA. Cada una con su caso por mutacion sobre una variable QUE EL CODIGO
  COMPUTE, nunca sobre un literal (EJECUTOR regla 1), y su salida pegada.
  (2.a) EL REPARTO POR ABSORBIDO EN
  scripts/loop/generar_plan_de_fusion_de_mesa.py. ADJUDICADO COMO
  OPERACION DE CODIGO BLOQUEANTE (acta 137, 3.4): no es doctrina nueva, es
  el carril de la fase 0 de codigo del 00_INDICE y el mismo por el que
  corrieron tus cuatro reparaciones. El defecto esta probado por los dos,
  tu corriendolo y yo leyendolo: marcar(spec["pasos"], ...) se llama
  dentro de `for ab in absorbidos` con el MISMO spec, y spec_marcas se
  indexa por NUMERO DE PASO, no por el par (absorbido, paso), asi que el
  paso 1 de dos absorbidos distintos lee la misma marca. Y lo que anado
  yo, medido y que cierra el caso: los TRES usos historicos del generador
  (OP-M-02-PROG, OP-M-03-I, OP-M-03-II, vueltas 63 y 64) tienen
  EXACTAMENTE UN absorbido cada uno, o sea que el camino de dos o mas NO
  HA CORRIDO NUNCA. No estas arreglando una regresion: estas estrenando
  un camino, y por eso las guardas van completas.
  LAS GUARDAS, y son de la casa, no inventadas:
    (i) el reparto se indexa por el par (absorbido, numero de paso). EL
    FORMATO VIEJO SIGUE VALIENDO para las de un solo absorbido, y eso no
    se promete, se PRUEBA: regenera los tres planes de las vueltas 63 y 64
    y compara byte a byte contra docs/loop/PLAN_V63_OPM02PROG.json,
    PLAN_V63_OPM03I.json y PLAN_V64_OPM03II.json. IDENTICOS. Ese es el
    caso positivo y ya existe: no hay que fabricarlo.
    (ii) MUTACION 1: dos absorbidos con marcas DISTINTAS para el MISMO
    numero de paso tienen que salir DISTINTAS en el plan. Contra el codigo
    viejo esta mutacion no puede pasar; contra el nuevo, si.
    (iii) MUTACION 2: una marca que falte para un par (absorbido, paso)
    cae ROJO NOMBRANDO EL PAR, no solo el numero.
    (iv) EL FALLO VIEJO QUEDA EXHIBIBLE, como tu 1.a lo dejo con
    --arbol-vivo: una bandera que corra el reparto viejo y enseñe las dos
    marcas iguales. Una reparacion que no puede enseñar el defecto que
    repara no se puede auditar.
    (v) cero escritura si hay fallos (ya lo hace) y el ciclo de Gate 0 con
    las suites detras.
  (2.b) EL RE-ANCLAJE DE LAS TRES MUTACIONES SELLADAS
  (vuelta135_2e_mutacion_1.py, _2.py y _3.py). ADJUDICADO: se re-anclan,
  NO se declaran superadas (acta 137, 3.3). Lo cubre el ramal (xxi)
  literal ("un EXIT 1 que no mide nada no es una prueba, es un plato
  vacio") y EJECUTOR regla 1. CONTRA QUE: contra un sujeto PROPIO Y
  CONGELADO, nunca contra docs/loop/REPORTE.md, que se sobreescribe cada
  vuelta. Congela el texto que las tres necesitan en un fichero propio de
  docs/loop/ con nombre que diga que es sujeto fijo, y que las tres muten
  ESA copia. Es la misma figura de tu guarda envejecida de 1.a, solo que
  del lado del SUJETO en vez del lado del ARBOL, y se resuelve con la
  misma regla, banco 9.10.
  Y LA GUARDA PARA QUE NO VUELVA A PASAR: las cuatro mutaciones viejas
  entran en el ciclo de cierre de cada vuelta, y a partir de que esten
  re-ancladas, ANCLA PERDIDA cuenta como ROJO. Hoy no: hoy tu mutacion D
  hace bien en distinguirla.

- TAREA 3, LA FASE 06. OP-M-01 A OP-M-05 POR SU ORDEN ESCRITO, y al
  sentarse cada mesa sus fusiones diferidas. MODO CONTINUO ENTRE FICHAS.
  LA LECTURA DE ACTO POR P.5 ES TRABAJO PROPIO Y OBLIGATORIO ANTES DE
  FUNDIR, y lo es POR LA LETRA de P.5 y no por extension: "CADA ACTO SE
  LEE ENTERO DESPUES DE SU DESTEJIDO Y ANTES DE SU FUSION", porque "una
  vez fundido, el acto es un nodo y la pregunta de si eran una familia o
  dos se vuelve irrespondible". Su alcance esta acotado por la correccion
  declarada del 15 ago 2026: EL ACTO EN OPERACION Y NADA MAS. No abre
  re-cribado, y si te sale un par de fuera del acto, no lo lees: lo
  anotas.
  EL ORDEN, fijado por el acta 137, 3.5, y dentro de cada una la lectura
  ANTES de la fusion:
    1. OP-M-01-FUSION (4 absorbidos). Declara P.5 SATISFECHA POR
       CONSTRUCCION: VERIFICA esa declaracion contra la ficha y dilo, no
       repitas la lectura.
    2. OP-M-02-ACCLIMATE (1 absorbido). Es la unica que el generador
       sellado podia hacer sin la 2.a.
    3. OP-M-03-III (2 absorbidos). AVISO MEDIDO PARA QUE NO SE DESCUBRA A
       MITAD: su propia ficha dice que el par interno pivote_estrategico
       contra pivotes_e_iteraciones NO SE HA LEIDO NUNCA y esta FUERA DE
       COLA. Es el caso exacto para el que P.5 existe, asi que esa lectura
       es la que decide si el acto es una familia o dos.
    4. OP-M-05-INDICE (2 absorbidos).
    5. OP-M-05-EDIFICIO (2 absorbidos). Su ficha avisa de que el margen de
       cableado es corto, 6 contra 5, y de que la lectura de P.5 no es
       formalidad ahi.
    6. OP-M-05-APERTURA (2 absorbidos).
  Cada fusion con SIMULACION PREVIA sobre copia en memoria, CASO POSITIVO,
  P.16 (QUIEN FABRICA, LIMPIA), la tabla de seis motivos de perdida con su
  perdida sellada en campo propio si no viaja, y EL CICLO DE GATE 0 CON
  LAS SUITES detras de cada ficha, mas cero duplicadas y cero auto-aristas
  tras resolver.
  EL TERRENO YA MEDIDO, RECOMPUTADO POR MI CONTRA EL GRAFO Y NO CONTRA EL
  CAMPO estado, para que no lo vuelvas a medir a ciegas: las seis estan
  SIN FUNDIR (13 absorbidos, los 13 VIVOS), las cinco mesas estan LISTA
  con pregunta_pendiente en None, las fronteras 4 y 5 de
  FRONTERAS_DECLARADAS.md ya estan escritas (12 ago 2026), y las seis
  fichas traen `eliminar` calzando con `nodos` menos superviviente, o sea
  que las guardas de ficha del generador pasaran. Recomputa al cierre lo
  que publiques, pero el terreno de partida es este.
  LO QUE SIGUE VIGENTE DEL ENCARGO ANTERIOR Y NO SE DEDUCE DEL CAMPO
  estado: LAS DIECISEIS fichas con fase=03_FUSIONES leen LISTA, las diez
  que el cierre de la fase 03 declaro RESUELTAS incluidas. LAS SEIS SON
  LAS SEIS NOMBRADAS ARRIBA Y NINGUNA OTRA se ejecuta por parecerlo. Y
  OP-M-02-MEDIOS no se toca: su nota la declara CONSUMIDA por el tramo 3
  de OP-U-01, con la divergencia de superviviente declarada como contraste
  y no resuelta copiando. Lo verifique leyendo la nota entera. Acertaste.
  Recordatorio del terreno: OP-S-12 va AL FINAL de la pasada entera,
  despues de la ultima fusion, por la atadura 2 del indice y porque las
  cinco mesas la nombran en su bloquea_a.

- TAREA 4, LOS REGISTROS Y LA CONDICION DE LA COBERTURA.
  (4.a) EL REGISTRO de las adjudicaciones del acta 137 donde corresponda
  en docs/PENDIENTES.md, POR ADICION, como hiciste con R.18: los cuatro
  discutibles adjudicados (3.1 a 3.6), las dos caidas mias de encargo
  (4.4 y 4.5) y la mia de acta (4.6) con su nombre, y tus dos de fuera del
  marcado (4.1 y 4.2). Las mias se escriben igual que las tuyas.
  (4.b) LA CONDICION DEL DISCUTIBLE 1, que es lo que lo hace auditable: el
  reporte publica, junto a la linea COBERTURA, EL REPARTO entre POR
  ETIQUETA y POR CONJUNTO, y si alguna cifra va POR CONJUNTO la NOMBRA.
  Esta vuelta salieron 16 y 0; la proxima puede no salir asi, y una
  cobertura tiene que decir de que esta llena. Es el ramal (xxi) aplicado.
  (4.c) EL FICHERO SELLADO: si una corrida tuya va a cambiar un fichero
  sellado de otra vuelta, se DECLARA EN EL REPORTE con su nombre y su
  diff, aunque el contenido nuevo sea mejor. La 137 lo hizo bien con
  SALIDA_V135_4B_PELDANOS.txt y lo hizo mal con SALIDA_V135_4C_MUTACION.txt.

SI LAS CUATRO TAREAS NO CABEN CON SUS GUARDAS COMPLETAS, PARTE POR LA
TAREA 3 Y NO POR LAS GUARDAS: entrega la 1, la 2 y la 4 enteras y las
fusiones que alcancen en su orden, y di CUALES no hiciste y por que, como
hiciste en la 137. Recortar guardas para llegar al final de la lista es
la caida que ninguna vuelta ha cometido todavia.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
