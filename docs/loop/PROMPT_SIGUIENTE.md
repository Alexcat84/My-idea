Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V113_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 113 con EXIT 0 antes
de escribir una sola linea de trabajo.

El acta de la vuelta 112 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 39323. En resumen, y sin adornarlo:

TUS CIFRAS CALZAN TODAS AL DIGITO Y LAS CORRI YO. Censo 3.853 / 3.188 /
665, aristas 9.190 / 9.169 / 18.359 / 9.813 con cero auto-aristas y cero
duplicadas, ciclo de tres en verde (Gate 0 OK, alcanzabilidad 100,0% con
3188/3188 y 85 semillas, etiquetas EXIT 0, sync EXIT 0), grafo en
8.391.653 bytes y sha256 f0e3993967457ed2b7a0 MEDIDO DESPUES del ciclo
entero, motor 25/25, web 80 (80) / 1.030 y 3 skipped, tsc EXIT 0, marcador
A 551 / B 72 / C 5 / D 2.760 sin huecos, desfase en 1 fila de 468, cierre
efectivo 74 / 109 (59,6%) e invertidas 2, bolsa 74/74/0.
OPERACIONES.jsonl no se toca: 71 filas, LISTA 70 y HECHA 1, fase 04 con
una HECHA y nueve LISTAS. Diff sobre dataset/, web/ y engine/ corrido
commit a commit sobre los OCHO: CERO lineas en los ocho, y docs/plan/
intacto en todo el tramo, que es la prueba dura de que tu retracto no
dejo rastro. PENDIENTES mas 109 puras. Guiones largos y medios: CERO y
CERO. wc -l del reporte, 34. Cabecera identica byte a byte a la que talla
el tallador, y PEGADA ENTERA.

TU TAREA 2 LA VERIFIQUE POR DENTRO Y NO POR SU EXIT, y esta bien hecha:
resolver_cita() de tallar_cifras_de_antes.py (linea 172) y la de
tallar_veredictos_reporte.py (linea 314) son hoy la misma logica linea por
linea, o sea que tu promesa de que los dos resuelven igual es cierta; el
instrumento sobre tu propio reporte ya NO da verde vacuo (marca 2
oraciones con citas resueltas con prefijo, 3/2 y 2/2, y excluye 4 por
orden); la S pasa la linea 4 de "0/1 citas ()" a 1/1 con el mismo fichero;
la T pasa el reporte 111 de 0 oraciones a marcar la de la 2.5; y la U me
da 72/2 y 70/4, las dos cifras que mi antecesor midio por su cuenta.

Y TU TAREA 3 LA CONTRASTE DONDE MAS DOLIA. Rehice tu censo del techo con
codigo mio y me salen tus 88 y tu reparto al digito, y tus 80 y tus 8
puesto a puesto. Medi ademas la descomposicion que nadie habia medido:
las 109 NO RESUELTA son 88 nunca reabiertas mas 21 con la direccion
ANULADA a None por correccion declarada (6, 8, 20, 21, 24, 25, 28, 29, 31,
38, 40, 52, 62, 66, 80, 93, 147, 161, 172, 174, 175), y otras 3 traen
correccion que no anula (46 y 148 sobre la vara, 145 sobre la direccion).
109 igual a 88 mas 21, cuadrado. Y lei a ciegas OCHO pares: los dos que
marcaste (12 y 104, retractos CORRECTOS los dos) y SEIS mas fuera del
marcado, elegidos donde mas dolia: medi primero cuantos de tus 80 traen la
palabra DISCUTIBLE en su propia razon, son TRES (26, 120, 124), y los tres
entraron en mi muestra con 11, 44 y 69. COINCIDO EN LOS OCHO. En el 26 y
en el 120 mi primera adjudicacion se inclinaba a RESUELTA y me corregi a
mi mismo con el texto delante (en el 26 el hijo anota CINCO salidas y la
linea de la madre nombra DOS; en el 120 la linea nombra DOS lienzos y el
hijo cubre UNO): mi escoria, declarada. Tu cosecha cero es correcta.

Y AHORA LO QUE COBRO, QUE SON DOS TUYAS Y UNA MIA, Y LAS TRES FUERA DEL
MARCADO. Empiezo por la mia, que es la mas vieja.

MI LISTA DE MARCAS SIGUE PARCHEANDOSE POR ENUMERACION Y SIGUE DEJANDO
FUERA LA PALABRA QUE TU REPORTE USA, Y ES LA TERCERA VEZ DE LA MISMA
ESPECIE. La 110 la cerro sin "pasa de"; la 111 lo cobro y volvio a
arreglarlo enumerando ("pasa de", "queda en", "quedo en", "daba", "dio").
Tu reporte 112 escribe DOS afirmaciones de estado anterior con el verbo
"sigue": "contar_cierre_efectivo.py sigue 74/109 (59,6%)" y
"verificar_cobertura_bolsa_tres_vias.py sigue 74/74/0". Las dos pasan
invisibles. Lo probe cambiando UNA palabra en
docs/loop/_auditor_v112_mut/reporte_112_sigue.md ("sigue" por "quedaba
en") y la oracion pasa de no marcada a marcada con 2/1 citas. Tus cifras
son correctas y tus citas existen: la caida es mia, de encargo. Y por eso
el remedio de esta vuelta NO es otra enumeracion.

TU CAIDA GRANDE ES DE GUARDA CEGADA, Y ES GRANDE PORQUE LA GUARDA
FUNCIONABA Y LA MATASTE CON UNA LINEA. tallar_cabecera_reporte.py dice en
su codigo, linea 600, "El tsc vacio ES la senal de exito (tsc sin salida
igual a exitcode 0)": fichero vacio da la celda "EXITCODE 0, cero lineas",
fichero con lineas da "N linea(s) de salida (revisar)". Esta vuelta
empezaste a apendar EXIT=0 a TODOS tus ficheros de salida. Para Gate 0,
motor y web es inocuo porque el tallador los parsea. Para el tsc mata la
guarda entera: SALIDA_V112_TSC_APERTURA.txt y SALIDA_V112_TSC_CIERRE.txt
pesan 7 bytes y son solo ese marcador, y tu cabecera publica en SUS DOS
COLUMNAS "1 linea(s) de salida (revisar)". Lo medi contra la historia: los
ficheros de las vueltas 110 y 111 pesan 0 bytes (git show 27ecfe43: y git
show 9aea9f43:) y las dos cabeceras publican "EXITCODE 0, cero lineas". Y
corri el tsc yo: exit 0, cero lineas reales. O sea que el tsc esta VERDE,
la celda dice "revisar", nadie lo declaro, y desde ahora un tsc con UNA
linea de error verdadera daria una celda IDENTICA a la de hoy. Es guarda
cegada, no acumula para la racha por el precedente del acta 111 (4.2), y
el remedio va BLOQUEANTE.

TU SEGUNDA ES DE EXPEDIENTE: EL BARRIDO 2.7 DICE "NINGUNO OMITIDO DE LA
LISTA" Y OMITE. El fichero declara su busqueda (grep de RE_CITA, del
patron de extension entre backticks, y de LOOP = os.path.join( en
scripts/loop/*.py) y encabeza "Ninguno omitido de la lista". Corri esa
misma busqueda: el tercer grep devuelve 57 ficheros. Tu lista publica
NUEVE instrumentos vivos mas dos fuera de alcance. De los que la propia
busqueda devuelve y tu lista no nombra ni descarta con su motivo hay TRES
VIVOS: abrir_tramo_de_opu01.py, caso_positivo_del_contrato_de_perdidas.py
y registrar_cierre_de_tramo.py, mas los 45 historicos, despachados sin
nombrarlos como grupo. TU CONCLUSION AGUANTA Y LA VERIFIQUE YO: abri los
tres y ninguno parsea una cita de prosa (rutas fijas o listdir), asi que
el unico boquete de la especie si vivia en el instrumento que corregiste.
No mueve ninguna cifra. Pero la letra del encargo era "un tallador
omitido de esa lista es un boquete callado", y "ninguno omitido" es una
promesa de completitud que tu propia busqueda desmiente.

Y LO QUE NO TE COBRO, DICHO CON LA MEDICION DELANTE. (a) El 3.5 pedia la
cifra vieja y la nueva cada una con SU fichero y citaste uno por vara; no
lo cobro porque el mismo 3.5 dice "si no se mueve ninguno, DILO CON LA
CIFRA" y eso es lo que hiciste, con docs/plan/ intacto como prueba. (b) El
doble sello de HEAD_CIERRE (1d8deba4, el renombre en 03827ad0, el re-sello
en 961fb18c) es escoria declarada en los mensajes de commit y corregida
dentro de la vuelta: no se publico nada equivocado. (c) Anoto a tu favor
que tu reporte escribe "entre los pasos 1 Y 2 de su madre" donde el acta
97 y la razon del 42 dicen "1, 2 y 4 de su madre" siendo esa madre de solo
TRES pasos: corregiste un desliz heredado, y es a lo que llegue yo a
ciegas. La proxima vez dilo cuando lo corrijas.

EL CREDITO DE LA TANDA BAJA, Y BAJA OTRA VEZ SOLO EN LA MITAD DE
INSTRUMENTOS. AUDITOR.md 1.2 manda relectura al doble del tramo donde sale
la discrepancia. Las dos tuyas estan en guardas y expediente, ninguna en
una lectura de nodos, y la lectura salio 8 de 8 buscando yo adrede donde
tu propio registro decia DISCUTIBLE. Asi que el doble va sobre los
instrumentos: dos casos de mutacion para la guarda del tsc, la lista de
marcas convertida en regla con su caso, y el barrido 2.7 rehecho ENTERO.
La lectura dirigida va en tramo normal.

- TAREA 1, LOS REGISTROS DEL ACTA 112, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su fichero de salida
  commiteado, y con la extraccion del bloque hecha DESPUES de la ultima
  edicion, con su diff de fidelidad como la vuelta pasada. Numera los
  subapartados COMO ESTAN AQUI.
  (1.1) TU CAIDA DE GUARDA CEGADA: el EXIT=0 apendado a los ficheros del
  tsc, con las tres mediciones que la prueban (7 bytes en la 112 contra 0
  bytes en la 110 y la 111; las celdas "1 linea(s) de salida (revisar)"
  contra "EXITCODE 0, cero lineas"; y el tsc real en exit 0 y cero lineas)
  y con la constancia de que el remedio es la TAREA 2 de esta vuelta.
  (1.2) TU CAIDA DE EXPEDIENTE del barrido 2.7 que promete "ninguno
  omitido" y omite, con los 57 ficheros que devuelve su propia busqueda,
  los TRES vivos no nombrados y los 45 historicos no agrupados, y con la
  constancia de que la CONCLUSION aguanta y la verifico el auditor.
  (1.3) MI CAIDA DE ENCARGO, la lista de marcas parcheada por enumeracion
  por tercera vez, con "sigue" como la palabra que se cuela y con la
  constancia de que el remedio ya no es enumerar.
  (1.4) LO QUE NO ES CAIDA: el 3.5 con un fichero por vara, el doble sello
  de HEAD_CIERRE como escoria declarada, y tu correccion silenciosa del
  desliz heredado del acta 97, esta ultima anotada A TU FAVOR.

- TAREA 2, BLOQUEANTE: LA GUARDA DEL TSC DEVUELTA A LA VIDA, LA LISTA DE
  MARCAS CONVERTIDA EN REGLA, Y EL BARRIDO REHECHO ENTERO.
  (2.1) LA CONVENCION DEL TSC, Y LA DECIDES TU CON UNA SOLA CONDICION:
  que la celda de la cabecera vuelva a distinguir un tsc limpio de un tsc
  con UNA linea de error. Tienes dos caminos y los dos valen: o vuelves al
  fichero vacio de las vueltas 110 y 111 (y entonces el EXIT del tsc va a
  OTRO fichero, no al suyo), o ensenas a tallar_cabecera_reporte.py a
  descontar una linea final de la forma EXIT=<n> antes de contar, y a
  publicar el exitcode que lea. Elijas el que elijas, ESCRIBELO EN EL
  DOCSTRING del tallador con su motivo, porque la cabecera de un
  instrumento es expediente y se mide como el reporte.
  (2.2) MUTACION V, del lado verde: un fichero de tsc que contenga SOLO el
  marcador EXIT=0. Tras tu arreglo, la celda de la cabecera tiene que
  decir que el tsc esta LIMPIO, no "revisar". Pega la salida de antes y la
  de despues, cada una en su fichero.
  (2.3) MUTACION W, del lado rojo, y es la que prueba que la guarda vive:
  un fichero de tsc con UNA linea de error verdadera (inventala, del tipo
  "web/lib/x.ts(3,5): error TS2304: Cannot find name 'foo'.") mas su
  EXIT=1. La celda tiene que salir DISTINTA de la de la mutacion V y
  nombrar la linea. Si V y W producen la misma celda, tu arreglo no
  arreglo nada y PARAS Y LO TRAES.
  (2.4) LA LISTA DE MARCAS DEJA DE SER UNA ENUMERACION. Anade como minimo
  "sigue", "sigue en", "continua", "se mantiene", "sin cambio", "identico
  a" e "igual que", y ESCRIBE EN EL DOCSTRING la regla que las gobierna, no
  solo la lista: TODA construccion que afirme un estado ANTERIOR o su
  permanencia entra en la lista, la amplia el AUDITOR por encargo, y EL
  EJECUTOR ESTA OBLIGADO a anadir cualquier verbo que su propio reporte use
  para una afirmacion de estado anterior y que la lista no traiga. Esa
  ultima frase es la que impide la cuarta vez.
  (2.5) MUTACION X, la que cierra mi caida 4.3: tu propio reporte de la
  vuelta 112 tal como quedo commiteado (git show 87397be1:docs/loop/
  REPORTE.md a un fichero). ANTES del arreglo NO marca ninguna de las dos
  oraciones con "sigue"; DESPUES tiene que MARCAR LAS DOS y evaluarlas con
  sus citas. NO REESCRIBAS EL REPORTE DE LA 112: es historia. Se pide la
  MEDICION sobre el, y su resultado se declara tal cual salga, incluso si
  sale ROJO. Pega las dos salidas.
  (2.6) EL BARRIDO 2.7 REHECHO ENTERO, y esta vez la lista es la lista.
  Corre las tres busquedas que el propio fichero declara, PUBLICA EL
  RECUENTO DE CADA UNA (la de LOOP = os.path.join( devuelve 57, cuentalo
  tu), y clasifica TODOS los ficheros que devuelven, sin excepcion, en
  grupos con su motivo escrito: los que parsean citas de prosa, los que
  resuelven nombres fijos construidos por codigo, los historicos de un
  solo uso, y los fuera de familia. Los que hoy no aparecen ni nombrados
  ni descartados son abrir_tramo_de_opu01.py,
  caso_positivo_del_contrato_de_perdidas.py y registrar_cierre_de_tramo.py:
  esos van con su linea, como los demas. Un fichero que la busqueda
  devuelve y la lista no menciona es un boquete callado, y la frase
  "ninguno omitido" solo se escribe si es verdad.

- TAREA 3, EL TRABAJO DE LECTURA, CON SU TECHO DECLARADO Y SELLADO ANTES
  DE LEER. Territorio: SE AGOTA EL VIEJO Y SE ABRE EL NUEVO, y van los dos
  en el mismo lote porque caben de sobra en el tramo austero.
  (3.1) RECUENTALO TU PRIMERO con codigo y declara las cifras antes de
  leer ninguno. Mi medicion, PARA CONTRASTAR Y NO PARA COPIAR: quedan 8
  del territorio viejo (168, 170, 171, 173, 176, 178, 181, 183, las NO
  RESUELTA nunca reabiertas que no cupieron en la 112) y el territorio
  nuevo son las 21 filas cuya direccion en base fue ANULADA a None por una
  correccion declarada (6, 8, 20, 21, 24, 25, 28, 29, 31, 38, 40, 52, 62,
  66, 80, 93, 147, 161, 172, 174, 175). Y ademas hay 3 filas con
  correccion que NO anula (46 y 148 sobre la vara, 145 sobre la direccion)
  que NO son de este territorio y que nombro para que no las cuentes de
  mas. Si tu nomina no es la mia, PARAS Y LO TRAES.
  (3.2) EL TECHO, ESCRITO ANTES DE CORRER: 29. Si las 29 se resolvieran,
  el 74 / 109 pasaria a 103 / 80. Y EL SELLADO ES NUEVO Y ES OBLIGATORIO:
  el fichero del censo y del techo va en SU PROPIO COMMIT, ANTES del
  commit que traiga una sola lectura. En la 111 y en la 112 el techo y la
  lectura nacieron en el mismo commit y el "declarado antes de leer" no se
  podia verificar por git; desde hoy si.
  (3.3) LEE LOS 29 contra el grafo, HOY, los dos nodos de cada par, con la
  vara escrita: banco 9.6.1 (la rama de contenido manda), la DIRECCION por
  9.6.2 (test de reconocimiento y senal de entregables), y 9.6.3 (el
  tamano del solape no decide). No copies de la razon vieja: la razon
  vieja se lee DESPUES de adjudicar, igual que en la ciega. Y OJO CON ESTE
  TERRITORIO, que no es el de la 112: estas 21 YA fueron reabiertas una
  vez y anuladas a proposito, asi que la carga de la prueba para
  reabrirlas otra vez es MAYOR, no menor.
  (3.4) CINCO DE ESAS 21 (20, 21, 38, 66, 93) SE RELEYERON EN LA VUELTA
  111, pero por la PREGUNTA DE TRES VIAS y no por la direccion, y el
  auditor de aquella vuelta las confirmo SATELITE cinco de cinco. Se
  releen igual, por la direccion, y en el registro se dice que son esas
  cinco y que la relectura de la 111 era de otra pregunta. No confundas
  una cosa con la otra ni la uses como coartada para no leerlas.
  (3.5) POR CADA PAR QUE MUEVAS, contra-caso fuerte ESCRITO ANTES DE
  DECIDIR, y correccion_v113 DECLARADA Y ADITIVA sobre direccion_leida,
  con el valor anterior, la vuelta que lo dio y la cita del banco. Sin
  borrar una letra. Por cada par que NO se mueva basta la linea del
  registro: la decision vive en el JSONL, no en la prosa del reporte.
  (3.6) MARCA LOS DISCUTIBLES EN EL REPORTE, Y ESTA VEZ CON UNA REGLA
  EXPLICITA: si al destapar la razon vieja esa razon contiene la palabra
  DISCUTIBLE, el par va NOMBRADO en la lista de discutibles marcados de tu
  reporte, aunque coincidas con ella. En la 112 habia tres asi (26, 120,
  124) y tu lista decia UNO: no lo cobre porque coincidi en los tres, pero
  el punto de entrada de mi relectura ciega no puede depender de que yo
  haga el grep.
  (3.7) RECOMPUTO OBLIGATORIO al terminar, con contar_cierre_efectivo.py y
  verificar_cobertura_bolsa_tres_vias.py, diciendo la cifra VIEJA y la
  NUEVA cada una con SU fichero de salida. Si no se mueve ninguno, DILO
  CON LA CIFRA: cosecha cero con techo declarado es una salida legitima y
  no se fuerzan hallazgos.
  (3.8) Y SI NO TE DA LA VUELTA PARA LOS 29 CON ESTA DISCIPLINA ENTERA,
  PARA DONDE ESTES Y DILO CON EL PUESTO EXACTO: cuantos leiste, cuales, y
  cuales quedan. Lo que NO se admite es un recorte callado.

- LO QUE NO SE TOCA EN LA TAREA 3: esto es JUICIO Y REGISTRO, como lo ha
  sido OP-E-03 desde el principio. NO se escribe ni se retira una sola
  arista del grafo, no se toca el campo estado, no se mueve ninguna
  operacion de fase, no se abre la fase 05 ni la 06. El diff sobre
  dataset/, web/ y engine/ tiene que seguir dando CERO lineas al cierre, y
  lo vas a medir commit a commit como siempre.

- LAS GUARDAS DEL CIERRE, y desde hoy son NUEVE instrumentos y VEINTISEIS
  casos. Contados uno por uno.
  INSTRUMENTOS (9): los mismos nueve de la vuelta 112
  (tallar_veredictos_reporte.py sobre tu propio reporte;
  tallar_nombre_de_operacion.py OP-E-03; verificar_apertura_sellada.py
  --vuelta 113; verificar_cabecera_pegada_o_condensada.py --vuelta 113;
  verificar_cobertura_bolsa_tres_vias.py; contar_cierre_efectivo.py;
  verificar_vuelco_de_veredicto.py; tallar_cabecera_reporte.py --fase04
  --vuelta 113; tallar_cifras_de_antes.py sobre tu propio reporte, YA CON
  LA LISTA CONVERTIDA EN REGLA).
  CASOS DE MUTACION (26): los VEINTITRES de la vuelta 112 (A, B, C, D, E,
  F, G, H, el reporte 102 por git show f253842b, mI.md, mJ.md, mK.md,
  mL.md, mM.md, la de la TAREA 2.4 de la vuelta 109, N, O, P, Q, R, S, T y
  U) MAS las TRES que nacen en la TAREA 2: V (el tsc con solo el marcador,
  celda LIMPIA), W (el tsc con una linea de error verdadera, celda
  DISTINTA de la de V) y X (tu reporte 112 por git show 87397be1, que
  despues del arreglo MARCA las dos oraciones con "sigue").
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F, G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I ROJO por la
  promesa falsa; J ROJO senalando fila 7 apertura; K ROJO por numero de
  filas; L ROJO EXIT 1 con 0 DISTINTA y 3 AUSENTE; M ROJO EXIT 1 con
  CUATRO celdas; la de la TAREA 2.4 con el 123 pasando de DECLARADO a
  MUDO; N ROJO nombrando el 87 en_sitio; O ROJO nombrando el 91 cruce; P
  ROJO nombrando el 154 en_sitio; Q y R en ROJO con la linea que les toca;
  S, T y U en VERDE EXIT 0. La H sigue siendo la frontera declarada por
  diseno: si algun dia da ROJO, eso no es una mejora, es que se movio el
  perimetro sin decidirlo, y paras.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Va fijo el sellado
  de la apertura, que es antes de todo; el sellado del techo de la TAREA 3
  en su propio commit ANTES de la primera lectura; y que la TAREA 2 quede
  cerrada con sus mutaciones V, W y X ANTES de que escribas una sola cifra
  de "antes" en el reporte de esta vuelta: primero la guarda reparada,
  despues el dictado que ella vigila.

- LO QUE NO SE ABRE Y LO QUE SIGUE ANOTADO. La deriva de contenido (26
  nodos de 140, 32 pares de 87, acta 92 seccion 4.4), los siete nodos con
  guion, el bloque repetido de formalizar_un_proceso_ad_hoc y los titulos
  gemelos por mayuscula (sistema_responsabilidad_gerencial y su _2) siguen
  ANOTADOS PARA ALEXIS Y SIN ENCARGAR, porque rozan el ALCANCE de la
  campana. Y sigue constando que Gate 0 tiene razon al dar 0 en
  duplicadas: su guarda dice "titulo_concepto EXACTO duplicado" y esos dos
  titulos no son exactos.

- LA NOTA DE HIGIENE DE SIEMPRE, remedida hoy por mi: git status trae M en
  dataset/metadata/master_graph.json desde antes de que nadie toque nada,
  y NO es un cambio (git diff sobre ese fichero da CERO lineas; es final de
  linea). Corri el ciclo de tres entero y despues medi: 8.391.653 bytes,
  sha256 f0e3993967457ed2b7a0. No lo commitees y no lo "arregles". Y si
  corres SOLO run_phase1.py el fichero cambia de tamano y parece que has
  movido algo: es el CICLO DE TRES ENTERO el que lo devuelve identico. El
  validador vive en scripts/run_phase1.py, y etiquetas_de_cara.py y
  sync_assets_web.py viven en scripts/, NO en scripts/loop/; el
  recomputador del marcador, en scripts/recomputar_marcador.py.

- Y LAS CUATRO DEL DICTADO. La primera: toda cifra que publiques sobre un
  estado ANTERIOR se mide corriendo el instrumento sobre ese estado y se
  cita el fichero de salida; si la frase habla del antes Y del despues, son
  DOS ficheros, uno por lado. La segunda: toda vara que corras declara SU
  TECHO medido antes de correrse, y desde esta vuelta SELLADO en su propio
  commit; una cosecha 0 sin techo declarado no cuenta como prueba de salud.
  La tercera: EL DOCSTRING DE UN INSTRUMENTO ES EXPEDIENTE Y SE MIDE COMO
  EL REPORTE, y el mensaje de commit igual. Y LA CUARTA ES NUEVA Y SALE DE
  TU 4.1: NO SE LE CAMBIA LA CONVENCION DE ENTRADA A UNA GUARDA SIN CORRER
  LA GUARDA DESPUES Y MIRAR SU SALIDA. Anadir una linea a un fichero de
  salida parece higiene y puede ser una guarda muerta; si la cambias, lo
  declaras en el reporte y ensenas la celda de antes y la de despues.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
