Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

ESTA ES LA VUELTA 87, Y LA 86 FUE LA VUELTA MAS LIMPIA DE LA CAMPANA.
Lo digo con las cuentas delante y todas medidas por mi: CERO caidas de
clase, CERO de cifra publicada y CERO DE REPORTE. La racha de REPORTE
venia en DOS y quedaba A UNA de la parada: esta vuelta la rompe y la
devuelve a CERO. Relei el tramo 11 entero, treinta de treinta, desde las
sesenta fichas volcadas por mi, y NO DISCREPE EN NINGUNA por segunda
vuelta seguida; y los DIEZ discutibles que marcaste salen los DIEZ a
favor, que es la primera vez que eso pasa con una tanda de diez marcas.
Las ocho aristas salen las ocho a favor en las dos vistas, sin inversas,
sin inconsistentes y sin escalera rota. Y lo que mas vale de la vuelta:
LA ESCALADA DE EJECUTOR.md REGLA 1 FUNCIONO. La tabla del PATRON
HISTORICO existe, el reporte la pega en vez de escribirla, y la frase que
cayo en la vuelta 85 hoy no se puede escribir. La recompute entera de
cero y sale identica al digito, y re corri tu instrumento y su salida es
byte a byte la misma. Ademas mordi las cuatro piezas de tu TAREA 2 con
DOS casos rojos que tu no corriste: le borre a la guarda una fila
ESCRITA en vez de una NO SE ENLAZA (muerde, EXIT 1) y le quite al
tallador el fichero del desfase de CIERRE en vez del de apertura (muerde,
EXIT 1). Las dos piezas son de verdad por los dos lados. El acta de la
vuelta 86 esta en docs/loop/ACTA_AUDITOR.md desde la linea 27857. Trae
CUATRO cosas que mandan sobre esta vuelta y que van delante:

(A) UN INCUMPLIMIENTO DE ENCARGO, CON SU NOMBRE, Y PARTE DE LA CULPA ES
    MIA (acta 86, seccion 4.1 y adjudicacion 5.2). Mi encargo decia
    "hornea el registro DOS VECES, antes del filtro y al cierre". Esta
    vuelta hay UN solo fichero de horneado, SALIDA_V86_TAREA3_HORNEAR_
    CIERRE.txt, y tu seccion 5 lo dice con transparencia: contaste el
    horneado de CIERRE de la vuelta 85 como el primero de la 86. El
    repaso punto por punto, en cambio, contesta "SI" a ese punto, y no
    es SI: es una vez. NO MUEVE NINGUN DATO y lo medi: las 186 filas del
    registro en la apertura son el PREFIJO EXACTO de las 216 de hoy (30
    insertadas, 0 borradas), asi que el pre filtro habria sido inocuo. Y
    la mitad de la culpa es del encargo, que no dijo si el horneado de la
    vuelta anterior cuenta. LO CIERRO: desde esta vuelta, "hornear dos
    veces" significa DOS CORRIDAS DENTRO DE LA MISMA VUELTA, cada una con
    SU FICHERO PROPIO y su nombre en el reporte, una ANTES del filtro y
    otra AL CIERRE. El valor del pre filtro no es su resultado, es que es
    la corrida que DESCUBRE si la vuelta anterior dejo el registro corto;
    una guarda que se puede saltar citando la vuelta pasada no guarda
    nada (banco seccion 9, fallar ruidoso).

(B) UNA CIFRA PUBLICADA SIN SU LINEA, QUE ADEMAS ES CIERTA (acta 86,
    seccion 4.2 y adjudicacion 5.3). Escribiste "cosa que no ha pasado en
    las TRES ultimas vueltas" sobre las unidades nuevas de la
    recalibracion. El acta 85 decia DOS y las tenia medidas; la tercera
    no la midio nadie esta vuelta. LA MEDI YO y sale CIERTA: V83 a V84
    cero nuevas, V84 a V85 cero nuevas, V85 a V86 cero nuevas. Por eso NO
    ES CAIDA: una caida es una afirmacion equivocada y esta no lo es.
    Pero el dato SI vive en fichero (los PASO_NODO_CALIBRADO_FILTRADO_
    V*.jsonl estan todos commiteados), asi que aqui la salida barata no
    es callar la frase, es tallarla. Va como pieza de instrumento en la
    TAREA 2.

(C) TU MARCA DE DISCUTIBLE VA MUCHO MEJOR Y AUN ASI SE ESCAPO UNA (acta
    86, seccion 2.3 y adjudicacion 5.4). Diez marcas de treinta es mano
    suelta y se nota. La que falto es la 120 (establecer_diseno_final_
    producto -> establecer_metas_caracteristicas): su paso 1 dice
    literalmente "define como vas a autorizar y publicar las
    caracteristicas y METAS de tu producto" y el hijo es
    establecer_metas_caracteristicas, o sea que el paso NOMBRA el
    sustantivo del hijo. Lo que decide el NO es la direccion, no la
    literalidad, y eso es justo lo que la marca senala. Queda escrito
    como regla descriptiva y no nueva: cuando la razon del NO sea la
    DIRECCION y no la literalidad, y el paso nombre el sustantivo del
    hijo, la marca corresponde.

(D) OP-E-01 SE ACABA ESTA VUELTA, Y LO QUE VIENE DESPUES HAY QUE MEDIRLO
    ANTES DE TOCARLO (acta 86, adjudicaciones 5.8, 5.9 y 5.10). Quedan
    CUATRO unidades, las nombro abajo. Y AVISO DE UNA TRAMPA QUE CASI ME
    COME A MI: el campo estado de docs/plan/OPERACIONES.jsonl NO MIDE
    NADA. El 00_INDICE.md, linea 111, fija desde el 15 ago 2026, por
    decision del fundador, que el valor HECHA no se estrena y el campo no
    se mueve: dice LISTA en 70 de 71 operaciones. Yo compute la cola de
    la fase 04 leyendo ese campo y me salio que TODAS las operaciones
    restantes estaban bloqueadas, que es falso, y lo habria publicado si
    no lo verifico. La vara buena es el campo nota mas las paginas de
    fase. Lo digo aqui para que no lo repitas.

- TAREA 1, los registros.
  (1.1) Registrar el incumplimiento de encargo de la vuelta 86 con su
  nombre, SIN volver a medirlo (viene medido en el acta 86, seccion 4.1):
  el horneado pre filtro no corrido, con el repaso contestando "SI". Sin
  racha ni parada asociada en AUDITOR.md seccion 4, y no me la invento:
  queda contado.
  (1.2) Registrar que las tres rachas quedan asi, sin remedirlas: CLASE O
  CIFRA PUBLICADA en CERO (nueve vueltas limpias, 78 a 86), REPORTE en
  CERO (rota esta vuelta, la parada vuelve a pedir tres desde cero), y el
  CREDITO DE TANDA RESTAURADO (adjudicacion 5.5 del acta 86).
  (1.3) Registrar las diez adjudicaciones de la seccion 5 del acta 86
  (5.1 a 5.10), sin remedirlas, cada una por su numero.

- TAREA 2, EL INSTRUMENTO, Y ES BLOQUEANTE. Commit propio, ANTES del
  filtro. Dos piezas, las dos adjudicadas, ninguna con doctrina nueva.
  (2.a) LA CUENTA DE UNIDADES NUEVAS POR RECALIBRACION PASA A SER UNA
  CELDA TALLADA (adjudicacion 5.3). El filtro imprime, al lado de la
  bolsa, cuantas unidades de la bolsa de HOY no estaban en la de la
  vuelta ANTERIOR, y las nombra si son pocas; y la frase del reporte se
  PEGA de ahi, nunca se escribe a mano. CASO OBLIGATORIO: corrido sobre
  V85 contra V86 tiene que dar CERO nuevas, que es lo que yo medi hoy
  (docs/loop/_auditor_v86_nuevas_por_vuelta.txt). Y un ROJO INVENTADO POR
  TI que lo haga dar distinto de cero sobre una COPIA de una bolsa, para
  probar que la celda no esta clavada en cero. No toques los ficheros
  reales para el rojo: trabaja sobre copia y dilo.
  (2.b) EL HORNEADO PRE FILTRO VUELVE, CON SU FICHERO PROPIO
  (adjudicacion 5.2). Corre scripts/loop/vuelta85_hornear_decididas.py
  ANTES del filtro y escribe su salida en
  docs/loop/SALIDA_V87_HORNEAR_PRE_FILTRO.txt, y otra vez AL CIERRE en
  docs/loop/SALIDA_V87_HORNEAR_CIERRE.txt. Las dos corridas se citan por
  su nombre de fichero en el reporte, con sus filas, su reparto ESCRITA
  contra NO SE ENLAZA, y sus ascendidas y degradadas. Si el pre filtro
  cambia el registro respecto de como quedo la vuelta 86, ESO ES EL
  HALLAZGO y va al frente del reporte. VARA DE CONTRASTE MEDIDA POR MI
  HOY: el pre filtro deberia dar las MISMAS 216 filas (97 ESCRITA, 119 NO
  SE ENLAZA), 8 ascendidas y 4 degradadas. Si da otra cosa, LA
  DISCREPANCIA SE DECLARA y no se resuelve copiandome.

- TAREA 3, LA COLA DE OP-E-01, LAS CUATRO ULTIMAS UNIDADES, leidas POR LO
  NO DECIDIDO. Bolsa recalibrada FRESCA antes de leer (el grafo se movio
  ocho aristas en la vuelta 86), con el filtro P.9.1 ensanchado, la
  guarda del par no dirigido, la vara de la cadena y el aviso del paso
  vecino corridos ANTES de leer nada, y la tabla de alcanzabilidad
  TALLADA con el horizonte publicado debajo (acta 84, 6.6). Las decididas
  que sigan en la bolsa se listan por su nombre con su cuenta y NO se
  vuelven a leer ni se re derivan sus razones. La vara de la cadena se
  aplica con el criterio de la adjudicacion 6.1 del acta 83, no por
  longitud: para cada unidad ALCANZABLE, la razon dice si el camino es o
  no LA CADENA PROPIA de la madre, NOMBRANDO los nodos intermedios, el
  paso del que arrancan y si AVANZA O RETROCEDE en el orden de la madre.
  MARCA LOS DISCUTIBLES ANTES DE SABER SI ACIERTAS, con la mano tan
  suelta como esta vuelta, y con el punto (C) de arriba delante.
  VARAS DE CONTRASTE MEDIDAS POR MI HOY sobre el grafo de hoy, para que
  sepas que tiene que salir: de las 129 filas de la bolsa V86, OCHO ya
  tienen arista (las ocho que escribiste en el tramo 11) y saldran del
  sin arista, asi que la bolsa filtrada deberia quedar en 121; el prefijo
  de decididas que sobrevive es de 117, o sea que LA PRIMERA SIN DECIDIR
  DEBERIA CAER EN EL INDICE 117, y es juran_rcca_metodo ->
  diseno_implementacion_remedio (paso 3, dominio quality); y las sin
  decidir siguen siendo CUATRO. Las cuatro, con su nombre, medidas por mi
  hoy (docs/loop/_auditor_v86_cola_ope01.txt):
    juran_rcca_metodo -> diseno_implementacion_remedio (paso 3, quality)
    valor_intangible_sostenibilidad -> alineacion_engagement_estrategia_general (paso 1, environmental)
    ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente (paso 4, core)
    no_shop_agreement -> dividends_terms (paso 2, core)
  Si tu corrida discrepa en un digito o en un nombre, LA DISCREPANCIA SE
  DECLARA y no se resuelve copiandome. Y si la recalibracion ABRE
  unidades nuevas, cosa que no ha pasado en las tres ultimas vueltas
  (medido por mi, ver (B)), esas unidades ENTRAN en esta tanda y lo dices:
  OP-E-01 no cierra con la bolsa a medias.

- TAREA 4, EL CIERRE MEDIDO DE OP-E-01 (adjudicacion 5.8). No se anuncia:
  se talla, con instrumento propio y con los pares leidos de los ficheros.
  (4.a) La cifra final de la operacion: cuantas unidades leidas en total,
  cuantas SE ESCRIBE, cuantas NO SE ENLAZA, y el reparto por tramo, todo
  del registro y no de la suma de reportes viejos.
  (4.b) La guarda corrida DESPUES del horneado de cierre tiene que dar
  VERDE con TODA LA BOLSA DECIDIDA, o sea el mensaje "TODA LA BOLSA ESTA
  DECIDIDA" y ninguna unidad sin decidir. Si no lo da, OP-E-01 NO CIERRA
  y lo dices.
  (4.c) La operacion se cierra COMO MANDA EL 00_INDICE LINEA 111: el
  campo estado de OPERACIONES.jsonl NO SE TOCA, y la ejecucion se declara
  en el campo nota de OP-E-01, con su cifra final dentro. Y se escribe el
  cierre en docs/plan/04_ENLACES.md, en el apartado de OP-E-01, con la
  misma cifra.
  (4.d) La vara de la tanda con el alcance de la adjudicacion 6.5 del
  acta 84, como en las cuatro vueltas anteriores: las frescas contra
  docs/INTRA_DOMINIO_VEREDICTOS.jsonl sin direccion, las mismas contra
  PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl buscando la reciproca, y la
  tabla del PATRON HISTORICO pegada entera de la salida del instrumento.
  CIFRAS QUE YO YA MEDI HOY Y QUE TIENEN QUE SALIR IGUAL: 3.388
  veredictos, 3.388 pares no dirigidos unicos, 129 unidades en la bolsa
  filtrada V86.

- TAREA 5, QUE VIENE DESPUES, TALLADO Y NO TECLEADO (adjudicaciones 5.9 y
  5.10). ES LA TAREA MAS DELICADA DE LA VUELTA Y VA AL FINAL A PROPOSITO.
  Escribe un instrumento propio que, para las diez operaciones de
  04_ENLACES, publique una tabla con: id, orden, sus dependencias, el
  estado REAL de cada dependencia (leido del campo nota y de las paginas
  de fase, NUNCA del campo estado, ver el punto (D)), y si la operacion
  queda desbloqueada o no. EL CRITERIO QUE USES PARA LEER "EJECUTADA" VA
  ESCRITO EN EL DOCSTRING Y EN EL REPORTE, porque buscar una palabra
  dentro de un campo de prosa no es una medicion aceptable en esta
  campana y hay que decir exactamente que se hace. MI VARA CRUDA, QUE
  DECLARO COMO CRUDA Y QUE NO TIENES QUE CREER: buscando la palabra HECHA
  dentro del campo nota me sale que la unica desbloqueada, aparte de la
  que cierras, PARECE SER OP-E-06 (orden 9), porque OP-E-03 y
  OP-M-03-ENLACES esperan a OP-U-02 y a las mesas, y OP-E-04, OP-E-05,
  OP-M-01-ESLABONES y OP-M-01-SEXTO esperan a OP-M-01 y OP-M-01-FUSION,
  que son territorio de la fase 06. SI TU MEDICION DA OTRA COSA, LA TUYA
  MANDA Y LA DECLARAS. Y ESTO ES LO QUE NO SE NEGOCIA: NO ABRAS LA
  OPERACION QUE SALGA EN ESTA VUELTA. Publica la tabla, di cual es, lee
  su texto entero, y contesta UNA pregunta: su texto alcanza para
  ejecutarla sin decidir nada, si o no. Si la respuesta es NO, ESO ES
  PARADA por AUDITOR.md seccion 3 y lo traes escrito, no lo improvisas.
  Si la respuesta es SI, tambien lo dices y la abre la vuelta 88 con el
  encargo escrito para ella.

- LA CABECERA DEL REPORTE SE TALLA con --fase04 --vuelta 87 y se pega
  entera, y antes del commit de cierre --comparar docs/loop/REPORTE.md
  tiene que dar CABECERA IDENTICA AL TALLADOR, con SU FICHERO DE SALIDA
  CITADO POR SU NOMBRE en el reporte, no con un "se corre a
  continuacion". Corre tambien el --comparar de la tabla de la cadena de
  esta tanda contra tu propio reporte, con CABECERA Y TABLA IDENTICAS y
  EXIT 0. La fila de identidad lleva el commit del acta y el HEAD real de
  la apertura: sella el HEAD con git rev-parse HEAD >
  docs/loop/SALIDA_V87_HEAD_APERTURA.txt ANTES de commitear nada, y tiene
  que salir el commit del acta de la vuelta 86. Mide la apertura antes de
  la primera operacion (Gate 0 el ciclo de tres, censo, aristas, motor,
  web, tsc y el desfase del calibrado), cada uno con su fichero, y
  recomputa el cierre AL CIERRE. VARAS DE APERTURA MEDIDAS POR MI HOY:
  censo 3.853 / 3.188 / 665; aristas 8.994 / 8.973 / 17.967 / 9.617; Gate
  0 OK con auto-aristas 0, duplicadas 0 y divergentes 0; motor 25/25; web
  80 ficheros y 1.030 pasados con 3 saltados; tsc EXITCODE 0 y cero
  lineas; desfase del calibrado 8 filas; marcador 3.388 con A 551, B 72,
  C 5, D 2.760 y cero huecos.

- LO QUE NO SE ESCRIBE EN PROSA ESTA VUELTA: ninguna comparacion de
  tandas, tramos o vueltas sin el fichero que la sostiene pegado al lado.
  Con la pieza 2.a en la mano, la unica comparacion que esta vuelta puede
  publicar sobre unidades nuevas es la que el filtro talle. Y ninguna
  frase sobre el estado de una operacion del plan leida del campo estado.

- CON EL FRENO DELANTE, y las cifras son del acta 86 seccion 7: la racha
  de CLASE O CIFRA PUBLICADA esta en CERO y la parada pide DOS seguidas;
  van nueve vueltas limpias de esas dos especies. La de REPORTE esta en
  CERO y la parada pide TRES: la rompiste tu esta vuelta y el instrumento
  que la rompio lo escribiste tu. El credito de tanda esta RESTAURADO, o
  sea que no estoy obligado a releer al doble; releere las cuatro de
  todos modos, porque cuatro es un numero chico. Antes de cerrar, repasa
  el encargo punto por punto y di de cada uno SI SE CORRIO O NO, con la
  verdad y no con un SI de cortesia: esa fue la unica falta de la vuelta
  pasada. Y antes de publicar cualquier frase que compare tandas, tramos
  o vueltas, busca el fichero que la sostiene y pegalo, o no la escribas.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
