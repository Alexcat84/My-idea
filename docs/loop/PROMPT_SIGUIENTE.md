Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ESTA ES LA VUELTA 118. El numero 117 quedo gastado por mi acta
(precedente del acta 81 seccion 5.3). Tus ficheros se llaman
SALIDA_V118_*, y los SALIDA_V117_* que ya estan en el arbol son pieza
historica: NO se tocan, NO se reusan, NO se borran.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V118_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 118 con EXIT 0 y SU
SALIDA COMMITEADA en docs/loop/SALIDA_V118_APERTURA_SELLADA.txt. La 117
lo hizo bien y lo verifique: sigue igual.

LA VUELTA 117 ENTREGO SUS CUATRO TAREAS Y TODAS SUS CIFRAS SON CIERTAS
AL DIGITO. Las recompute con codigo mio: censo 3.853 / 3.188 / 665,
aristas 9.190 / 9.169 / 18.359 / 9.813 con cero auto-aristas y cero
duplicadas, Gate 0 OK con alcanzabilidad 100,0% (3188/3188) y 85
semillas, grafo en 8.391.653 bytes y sha256 f0e399396745, motor 25/25,
web 80 (80) / 1.030 y 3 skipped, tsc EXIT 0 y cero lineas, marcador
A 551 / B 72 / C 5 / D 2.760 sin huecos y con las diez tasas, desfase 1
de 468, cierre efectivo 74 / 109 (59,6%) e invertidas 2, bolsa 74/74/0.
Diff sobre dataset/, web/ y engine/ commit a commit sobre los CATORCE:
CERO lineas. 04_ENLACES.md 94 insertadas y 0 borradas, y su diff no trae
UNA SOLA linea que empiece por menos: aditivo MEDIDO. Guiones: CERO.
wc -l del reporte: 34, y su fichero dice 34. Y lo mas importante: TU
CAIDA BLOQUEANTE DE LA 116 QUEDA CERRADA Y LO PROBE MUTANDO YO MISMO.
Contee INSTRUMENTOS con ast (NUEVE entradas, el INSTRUMENTO 1 dentro y
corrido), verifique que las lineas 240 y 327 imprimen len(INSTRUMENTOS)
y total_casos con %d, y en vez de repetir tu mutacion BB hice la mia
quitando OTRA entrada: la copia dice 8 en la apertura y 8 en el cierre.
La cifra se mueve con la lista. Y la 4.2 tambien queda cerrada: los
absolutos de la Y ESTAN en tu reporte, los recorri yo con y sin
exclusion y dan crudo 16 / 5 / 59 union 73 y neto 15 / 4 / 58 union 72,
identico, ningun absoluto baja. CERO caidas de clase, CERO de cifra
publicada, y esta vuelta CERO DE REPORTE: barri todas las citas de tu
REPORTE.md una por una y todas resuelven, incluida la mas fina, que es
_resolver en run_phase1.py lineas 989 a 1009, verificada linea a linea.

LO QUE COBRO SON DOS COSAS, LAS DOS DE LA MISMA ESPECIE, Y LA MITAD DE
LA CULPA ES MIA. VA PRIMERO LA MIA.

MI PRIMERA CAIDA, DE ENCARGO: MI CONTRASTE SE CONVIRTIO EN TU CRITERIO.
En la TAREA 3.2 te di "mi contraste de hoy" con siete citas y cerre con
"Si tu censo no es el mio, PARAS Y LO TRAES". Mis siete citas usan todas
CERRADA, SELLADA o EJECUTADA ENTERA, y NINGUNA usa la forma CIERRE
MEDIDO. Asi que la unica lista de palabras que reproduce mi contraste
sin dispararte una parada es justo la que no ve la palabra CIERRE. Y en
la 3.3 fui peor: te pedi "si trae registro de cierre en la pagina" sin
darte lista ninguna ni contraste ninguno. Tu instrumento heredo mi punto
ciego, y que tu censo y el mio coincidieran al digito no probaba nada.

MI SEGUNDA CAIDA, DE CIFRA: MI ACTA 116 PUBLICO "297 ARISTAS QUE LA FASE
ESCRIBIO DE VERDAD (98 + 113 + 86)". La cifra vigente, medida hoy con mi
propio codigo sobre las tres nominas de verdad, es 296 (98 + 114 + 84),
y el reparto real es 293 ESCRITA y 3 YA_ESTABA. Sume el "86 ESCRITAS"
del addendum de la vuelta 91, que es una cosecha SUPERADA TRES VECES por
las correcciones declaradas de las vueltas 92, 93 y 94, escritas debajo
en la propia nota de OP-E-07 hasta "84 con direccion, 82 ESCRITA, 2
YA_ESTABA". Lei la nota y no baje hasta el final. Tu mediste 296 y
publicaste 296: la falsa es la mia.

TU PRIMERA, DE INSTRUMENTO CEGADO: EL CENSO DE LA TAREA 3.2 CUENTA UNA
NEGACION COMO UN SI. Tu tabla publica OP-D-07 con la superficie (C),
frase REGISTRO DE OPERACION HECHA, en SI, citando 02_DESTEJIDOS.md:4461.
Fui a leer la linea: dice, literal, "Por eso este registro NO dice
REGISTRO DE OPERACION HECHA". El tallador casa la subcadena y no ve la
negacion que la precede, y la celda afirma lo contrario de lo que la
pagina declara. La misma afirmacion viaja al asunto del commit aa45b6ed
("y tambien la nota y la frase en :4461"), que por la tercera del
dictado es expediente y se mide como el reporte. NINGUN DATO SE DANO Y
NINGUNA CONCLUSION SE MUEVE: OP-D-07 ya trae registro por (A) y por (B),
y el 9 de 9 se sostiene entero, lo verifique aparte. Lo que lo hizo
posible es que mi encargo pedia "la CITA LITERAL con su fichero y SU
LINEA" para cada SI, y tu instrumento imprime el ENCABEZADO, no la linea
casada. Si hubieras pegado la linea, la negacion habria saltado sola.
NO ACUMULA en ninguna racha (es de expediente, la categoria del acta
116 4.3), pero dispara la relectura al doble del tramo.

TU SEGUNDA, DE EXPEDIENTE: UNA CELDA FALSA POR UNA LISTA DE PALABRAS QUE
NO CONTIENE LA PALABRA CIERRE. vuelta117_tarea3_3_censo_ejecucion_
fase04.py linea 47 declara PALABRAS_CIERRE = ("CERRADA", "SELLADA",
"EJECUTADA ENTERA", "HECHO"). Corri el mismo censo con una lista ancha y
compare celda por celda: se mueven DOS, y una es FALSA.
(i) "OP-E-03 | registro en pagina | NO" es falso: 04_ENLACES.md linea
1474 lleva "## EL CIERRE DE LA LECTURA DE OP-E-03, EL TERRITORIO SE
ACABO (VUELTA 115, TAREA 3.3)", que es exactamente un registro de cierre
de los que mi acta 116 3.1 declaro validos.
(ii) OP-E-01 sale con dos citas que son encabezados de PASO ("PASO 1 DE
OP-E-01, HECHO" en la 60 y "PASO 2" en la 139), mientras que el registro
de cierre de la operacion entera, 04_ENLACES.md linea 783, "## OP-E-01,
CIERRE MEDIDO (27 ago 2026, vuelta 87)", NO SE REPORTA: la celda sale SI
por las razones equivocadas, y la que faltaba es justo la que te habria
evitado dejar OP-E-01 sin categoria.
Comprobe que ninguna otra celda se mueve: con la lista ancha, las ocho
operaciones restantes dan lo mismo. Y ninguna cifra de docs/plan/ se
contamino: tu registro de la TAREA 4 no publica esa columna, lo verifique
leyendo las 94 lineas anadidas. NO ACUMULA (expediente) y dispara el
doble.

LO QUE ADJUDICO, Y CAMBIA EL MAPA DE LA CAMPANA. Cuatro piezas, ninguna
es doctrina nueva:
(1) OP-E-01 TIENE SU DESTINO CUMPLIDO Y ESTA EJECUTADA. Tu la dejaste
"aparte sin categoria", que es lo que mi encargo te mandaba ("NO
ADJUDICAS: mides y publicas"), asi que no es caida tuya, es trabajo mio,
y lo hago con lo medido hoy: su propia nota trae CIERRE MEDIDO (27 ago
2026, vuelta 87) y dice literal "esta nota es la unica declaracion de
que quedo ejecutada"; 04_ENLACES.md linea 783 lleva su encabezado de
cierre; sus 98 de 98 estan presentes por las dos vistas; y la nota de
OP-E-06 la cita como precedente de ejecutada. Doctrina: acta 116, 3.1 y
3.2.
(2) UN CONTRASTE NO ES UN CRITERIO. La lista de casos que yo doy como
"mi contraste de hoy" es una vara de comparacion, NO la definicion de lo
que hay que buscar. Un instrumento construido para reproducir mi
contraste hereda mis puntos ciegos. Desde aqui: TODO INSTRUMENTO DE
CENSO IMPRIME SU PROPIO CRITERIO EN SU SALIDA (la lista de patrones, no
solo en el docstring), y mi contraste se coteja DESPUES. Es AUDITOR.md
1.1 ("el instrumento manda ... se citan como contraste") aplicada al
encargo del auditor.
(3) LA FASE 04 QUEDA CERRADA CON REMISION. El criterio de HECHO escrito
(00_INDICE.md, tabla EL ORDEN, fila 4) lo medi hoy clausula por clausula
sobre las tres fuentes: ids RESUELTOS, 296 de 296 resuelven (272 directo
y 24 por alias), cero rotas, las 296 presentes por las dos vistas; una
sola direccion salvo los dos mutuos, cero bidireccionales, y LD-41 y
LD-43 viven en OP-E-05, que va REMITIDA y no escrita; cero aristas por
alias nuevas, y lo medi expresamente: de los 24 que solo resuelven por
alias, CERO tienen su forma cruda escrita en el grafo. Las diez se
reparten sin que sobre ni falte una: CINCO CON DESTINO CUMPLIDO
(OP-E-01, OP-E-02 HECHA, OP-E-03 con ADDENDUM de la 94 y su encabezado
de cierre en 04_ENLACES.md:1474, OP-E-06 114/114, OP-E-07 84/84) y CINCO
REMITIDAS a las mesas de la fase 06 (OP-M-03-ENLACES a OP-M-03, y
OP-E-04, OP-E-05, OP-M-01-ESLABONES y OP-M-01-SEXTO a OP-M-01), con sus
tres criterios cumplidos. El campo estado NO SE TOCA en ninguna.
(4) LA FASE 05 SE ABRE, con el orden que mi acta 115 seccion 5.1 dejo
adjudicado: OP-S-01 primero, luego las siete en su orden declarado
(OP-S-02 2, OP-S-03 3, OP-S-04 4, OP-S-05 5, OP-S-08 7, OP-S-09 8,
OP-S-10 9, OP-S-11 11) y OP-S-12 REMITIDA al final de la campana por la
atadura 2 de 00_INDICE.md. Y CON SU GUARDA DE ENTRADA, que es bloqueante
y no se hereda del registro de la vuelta 102: OP-S-01 y OP-S-09 MUEVEN
IDS, y la atadura 1 pone la fase 0 delante de todo lo que mueve un id.

ESTA VUELTA REGISTRA, REPARA Y ABRE. Lo que se toca, y solo eso:
docs/PENDIENTES.md (TAREA 1), scripts/loop/ (ficheros nuevos), y de
forma ADITIVA docs/plan/04_ENLACES.md y docs/plan/00_INDICE.md (TAREA
3), con su diff medido y pegado. El diff sobre dataset/, web/ y engine/
tiene que dar CERO lineas al cierre, medido commit a commit, SALVO que
la TAREA 4 llegue a ejecutar y su ejecucion este autorizada por la letra
que va escrita alli, en cuyo caso el movimiento va declarado, medido y
con su caso positivo.

- TAREA 1, LOS REGISTROS DE MI ACTA 117, en docs/PENDIENTES.md, seccion
  propia y claramente nombrada, con la composicion del anadido TALLADA
  con scripts/loop/tallar_composicion_salida.py y su fichero de salida
  commiteado, y con la extraccion del bloque hecha DESPUES de la ultima
  edicion, con su diff de fidelidad. Numera los subapartados COMO ESTAN
  AQUI.
  (E.1) LA CAIDA DE INSTRUMENTO CEGADO, con la celda falsa nombrada
  (OP-D-07, superficie C, SI), la cita LITERAL de 02_DESTEJIDOS.md:4461
  re-medida por ti hoy, la constancia de que el instrumento imprime el
  encabezado y no la linea casada, la de que el asunto del commit
  aa45b6ed repite la afirmacion, la de que NINGUNA conclusion se mueve
  (OP-D-07 trae registro por A y por B, y el 9 de 9 se sostiene), la de
  que NO ACUMULA por ser de expediente, y la de que su remedio es la
  TAREA 2 de esta vuelta, BLOQUEANTE.
  (E.2) LA CAIDA DE EXPEDIENTE DE LA LISTA DE PALABRAS, con la linea 47
  del instrumento citada tal cual, las DOS celdas que se mueven con
  lista ancha, la cita literal de 04_ENLACES.md:1474 y la de
  04_ENLACES.md:783 re-medidas por ti hoy, la constancia de que ninguna
  otra celda se mueve, la de que ninguna cifra de docs/plan/ se
  contamino, y la de que NO ACUMULA.
  (E.3) MIS DOS CAIDAS, cada una con su nombre: la de encargo por
  convertir mi contraste en tu criterio, y la de cifra por publicar 297
  cuando lo medido es 296 (98 + 114 + 84, con 293 ESCRITA y 3
  YA_ESTABA). La cifra correcta va escrita al lado.
  (E.4) LA ADJUDICACION DE OP-E-01, escrita entera, con sus cuatro
  apoyos y sus dos citas de linea RE-MEDIDAS POR TI HOY (la nota y
  04_ENLACES.md:783), no copiadas de aqui.
  (E.5) LA LETRA NUEVA, UN CONTRASTE NO ES UN CRITERIO, escrita entera y
  con su cita de AUDITOR.md 1.1.
  (E.6) EL CIERRE CON REMISION DE LA FASE 04, con las tres clausulas del
  criterio de HECHO y sus cifras, y las diez repartidas en cinco y
  cinco.
  (E.7) LA APERTURA DE LA FASE 05, con su orden, su remision de OP-S-12
  y su guarda de entrada bloqueante.
  (E.8) LO QUE NO ES CAIDA EN LA 117: la TAREA 2, que cierra su caida
  bloqueante y que verifique mutando yo mismo; los absolutos de la Y, ya
  en el reporte; las cuatro mediciones de la TAREA 3, que calzan al
  digito con las mias; el registro aditivo de la TAREA 4, medido en 94 y
  0 y sin una sola linea borrada; y el REPORTE.md entero, cuyas citas
  barri una por una sin encontrar ninguna falsa.

- TAREA 2, BLOQUEANTE: LOS DOS CENSOS SE REPARAN EN CODIGO Y SE
  RE-CORREN. Ficheros nuevos, vuelta118_*; los de la 117 son historia y
  NO SE TOCAN.
  (2.1) EL CRITERIO SE IMPRIME EN LA SALIDA. Todo censo por palabra
  clave imprime, en su cabecera, la lista EXACTA de patrones con la que
  corre, sacada de la constante con %s y no tecleada. Un lector de la
  salida tiene que poder ver que se busco sin abrir el fuente.
  (2.2) LA LINEA CASADA SE PEGA ENTERA. Para cada SI de cualquier
  superficie, la salida pega la LINEA que caso, literal y con su numero
  medido hoy, ademas del encabezado al que se atribuye. No basta el
  encabezado: la caida E.1 vivio justo en ese hueco.
  (2.3) LA NEGACION NO CUENTA COMO SI. Anade una guarda de negacion: si
  la linea casada contiene la marca de negacion delante del patron (por
  ejemplo "NO dice", "no dice", "NO lleva", "sin"), la superficie NO
  cuenta como SI y la salida lo dice con la linea delante, marcada como
  DESCARTADA POR NEGACION. Declara en la salida QUE marcas de negacion
  usas, contadas del codigo. Si tu lectura de que cuenta como negacion
  es otra, la declaras y la traes, no la resuelves a ojo.
  (2.4) LA LISTA DE PALABRAS DE CIERRE SE AMPLIA Y SE DECLARA. La lista
  de la 117 no contenia la palabra CIERRE. Amplia la lista, imprimela en
  la salida por 2.1, y DI en el reporte, en una linea, CUANTAS CELDAS SE
  MUEVEN respecto de la corrida de la 117 y CUALES. Mi contraste, y esta
  vez lo digo con su etiqueta: ES CONTRASTE, NO CRITERIO, y si tu
  criterio bien construido encuentra mas que yo, eso es un hallazgo y no
  una discrepancia. Lo que yo medi con lista ancha: se mueven DOS,
  OP-E-03 de NO a SI por 04_ENLACES.md:1474, y OP-E-01 gana
  04_ENLACES.md:783; las ocho restantes no se mueven.
  (2.5) MUTACION CC, DEL LADO ROJO, SOBRE LA GUARDA DE NEGACION: en una
  copia del censo reparado, quita la guarda de negacion sin tocar nada
  mas, y la salida tiene que VOLVER A DAR SI en OP-D-07 superficie (C).
  Pega la salida de antes y la de despues, cada una en su fichero
  nombrado, con su veredicto aparte. Una guarda que nunca fallo no esta
  probada.
  (2.6) MUTACION DD, DEL LADO ROJO, SOBRE LA LISTA DECLARADA: en otra
  copia, quita UNA palabra de la lista de cierre sin tocar nada mas, y
  la salida tiene que imprimir una lista MENOR en su cabecera Y perder
  al menos una celda. Pega antes, despues y veredicto.
  (2.7) LOS VEINTINUEVE CASOS DE MUTACION DE LA 117 SIGUEN ENTEROS Y CON
  SUS RESULTADOS FIJOS, y los INSTRUMENTOS se siguen contando del codigo
  con len(INSTRUMENTOS) y %d, como los dejaste. La H sigue siendo la
  frontera declarada por diseno: si algun dia da ROJO, eso no es una
  mejora, es que se movio el perimetro sin decidirlo, y paras.
  (2.8) LOS ABSOLUTOS DE LA Y VUELVEN AL REPORTE, en una linea, diciendo
  contra que cifra mia los comparas. Las mias, medidas hoy sobre los 641
  ficheros .py de scripts/loop contados NO recursivos: crudo 16 / 5 / 59
  union 73, neto 15 / 4 / 58 union 72. Pueden SUBIR legitimamente si un
  fichero nuevo tuyo casa alguno de los tres patrones; si alguno BAJA,
  eso es rojo y PARAS.

- TAREA 3, EL REGISTRO DEL CIERRE DE LA FASE 04, ADITIVO, EN SU PROPIO
  COMMIT, MEDIDO CON difflib Y CON git diff --numstat, LOS DOS PEGADOS.
  Va DESPUES de la TAREA 2 y usa las cifras de tu censo reparado, no las
  mias.
  (3.1) EN docs/plan/04_ENLACES.md: LA FASE 04 QUEDA CERRADA CON
  REMISION, con las TRES clausulas del criterio de HECHO y su cifra cada
  una (ids resueltos, una sola direccion, cero aristas por alias
  nuevas), las diez repartidas en cinco cumplidas y cinco remitidas, y
  la adjudicacion de OP-E-01 con sus dos citas re-medidas. EL TEXTO
  VIEJO SE QUEDA ENTERO Y SIN BORRAR UNA LETRA, incluida la correccion
  declarada que escribiste en la 117: esto se anade debajo.
  (3.2) LA CORRECCION DECLARADA DE LAS DOS CELDAS FALSAS, pegada debajo
  del texto viejo y sin reescribirlo: la de OP-D-07 superficie (C) y la
  de OP-E-03 registro en pagina, cada una con la linea real y su cita
  literal re-medida hoy. Van donde vivan sus tablas, que es en las
  salidas de la 117: como esas son pieza historica y NO SE TOCAN, la
  correccion vive en este registro y en PENDIENTES, y lo dices asi.
  (3.3) EN docs/plan/00_INDICE.md: la fila de la fase 04 del mapa de
  fases y el resumen de ejecucion, actualizados de forma ADITIVA con el
  cierre con remision y su fecha, SIN borrar lo anterior y SIN tocar el
  campo estado de ninguna operacion. Si el formato de esa pagina no
  admite un anadido aditivo sin reescribir una linea viva, PARAS Y LO
  TRAES en vez de reescribirla.
  (3.4) LO QUE NO SE TOCA: cero cambios en el campo estado de las 71
  filas, cero aristas escritas o retiradas por esta tarea, y la fase 06
  no se abre.

- TAREA 4, LA APERTURA DE LA FASE 05, Y SE ABRE MIDIENDO, NO EJECUTANDO.
  (4.1) LA GUARDA DE ENTRADA, BLOQUEANTE Y PRIMERO. La atadura 1 de
  00_INDICE.md pone la fase 0 delante de TODO lo que mueve un id, y
  OP-S-01 (FUSION) y OP-S-09 (RENOMBRE_CON_ALIAS, 67 nodos) mueven ids.
  El criterio de HECHO de la fase 0, escrito en 00_INDICE.md fila 0, es
  "las cinco guardas pasan en verde y cada una fallo primero en su caso
  positivo. Una guarda que nunca fallo no esta probada". LEE
  docs/plan/FASE_0_CODIGO.md y publica, con tallador: cuales son las
  cinco guardas NOMBRADAS DE ESA PAGINA (no de mi memoria ni de la
  tuya), donde vive el codigo de cada una, si pasa hoy en verde, y si
  tiene su caso positivo con su fichero. Si no son cinco, o si alguna no
  tiene caso positivo localizable, PARAS Y LO TRAES: no la das por buena
  porque el registro de la vuelta 102 lo dijera, que es exactamente lo
  que mi acta 115 5.1(d) prohibio.
  (4.2) EL TECHO DE LA FASE 05, SELLADO EN SU PROPIO COMMIT ANTES DE
  MEDIR NADA, con su propio tallador: numero de operaciones de la fase
  05, su orden declarado una por una, cuantas traen pregunta_pendiente y
  cuantas depende_de. Mi contraste, y ES CONTRASTE: diez operaciones,
  ordenes 1, 2, 3, 4, 5, 7, 8, 9, 11 y 12, pregunta_pendiente None en
  las diez, y solo OP-S-12 declara depende_de.
  (4.3) EL CENSO DE OP-S-01 CONTRA EL GRAFO, PUNTO POR PUNTO Y ANTES DE
  TOCARLA. Lee SU PROPIA NOTA entera hasta el final (es la letra de mi
  acta 116 4.7, y yo mismo la incumpli esta vuelta), y despues mide
  contra el grafo de hoy, uno por uno, TODOS los puntos de su campo
  verificacion, publicando para cada uno CUMPLE o NO CUMPLE con el
  comando que lo mide. Mi contraste, y va CRUDO y sin adjudicar, porque
  es medicion parcial mia y no un veredicto: hoy
  nafta_free_trade_agreements ya esta DEPRECADO y
  certificado_de_origen_tratados_libre_comercio ya lleva
  nafta_free_trade_agreements en su ids_alias, o sea que los dos
  primeros puntos parecen YA CUMPLIDOS; y el punto que dice "ningun nodo
  VIVO lleva NAFTA en su id ni en su titulo" parece NO CUMPLIDO, porque
  el titulo_concepto del superviviente es "Certificado de Origen y
  Tratados de Libre Comercio (NAFTA, Rules of Origin, RVC)". Mide los
  siete y publica la tabla.
  (4.4) Y AQUI LA LETRA QUE MANDA, Y NO TIENE VUELTA: NO EJECUTES NADA
  DE OP-S-01 EN ESTA VUELTA SI SU TEXTO NO ALCANZA PARA EJECUTARSE SIN
  DECIDIR. AUDITOR.md seccion 3 lo dice con esas palabras: "Una
  operacion cuyo texto no alcance para ejecutarse sin decidir es PARADA,
  no una improvisacion". En concreto: si el punto del NAFTA en el titulo
  sale NO CUMPLE, la operacion NO dice que texto tiene que llevar el
  titulo del superviviente, y reescribir el titulo de un nodo VIVO
  inventando la redaccion es exactamente la improvisacion prohibida.
  Publica el censo, di si la operacion esta CUMPLIDA, PARCIALMENTE
  CUMPLIDA o SIN EMPEZAR con sus puntos delante, y DETENTE AHI. Yo
  adjudico en la 119 con tu censo delante. Si el censo sale con los
  siete puntos en CUMPLE, tampoco la declaras HECHA: lo dices y lo
  traes.
  (4.5) LO QUE NO SE TOCA EN LA TAREA 4: cero nodos deprecados, cero
  alias escritos, cero titulos reescritos, cero aristas, cero cambios de
  estado. Esta tarea MIDE.

- LAS GUARDAS DEL CIERRE, con lo que la TAREA 2 deje construido: los
  instrumentos que sean, CONTADOS DEL CODIGO, con --vuelta actualizado a
  118 donde toque, mas los veintinueve casos de mutacion enteros, mas
  las mutaciones CC y DD nuevas. Corre las guardas AL CIERRE, con el
  REPORTE.md ya escrito, y pega su salida en
  docs/loop/SALIDA_V118_GUARDAS_CIERRE.txt.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Va fijo el
  sellado de la apertura con su salida commiteada, que es antes de todo;
  que la TAREA 2 quede cerrada con sus mutaciones CC y DD ANTES de que
  la TAREA 3 escriba una sola cifra de censo; que la TAREA 3 vaya
  DESPUES de la TAREA 2 y con SUS cifras; que la guarda de entrada 4.1
  vaya ANTES que el resto de la TAREA 4; y que el techo de la 4.2 se
  selle en su propio commit ANTES del censo de la 4.3. Y CADA TAREA VA
  EN SU PROPIO COMMIT, con su asunto diciendo que tarea cierra, y el
  push detras.

- Y LAS LETRAS NUEVAS DE ESTA VUELTA, que son dos y son cortas. LA
  PRIMERA: UN CONTRASTE NO ES UN CRITERIO. Cuando yo escriba "mi
  contraste de hoy", eso es una vara de comparacion y NO la definicion
  de lo que hay que buscar; el instrumento define su criterio por si
  mismo, lo IMPRIME en su salida, y mi contraste se coteja despues. Si
  tu criterio bien construido encuentra MAS que mi contraste, eso es un
  hallazgo y lo publicas; no recortes el instrumento para que calce
  conmigo. LA SEGUNDA: UNA SUBCADENA NO ES UNA AFIRMACION. Un patron que
  casa dentro de una frase que lo NIEGA no vale como SI, y cualquier
  censo que publique un SI tiene que pegar la linea entera que lo
  sostiene. Y las dos de siempre siguen vivas: ANTES DE PREGUNTAR SI UNA
  OPERACION SE PUEDE EJECUTAR, SE LEE SU PROPIA NOTA HASTA EL FINAL
  (yo mismo la incumpli esta vuelta y por eso publique 297); y TODA
  CIFRA QUE PUBLIQUE UN VEREDICTO SOBRE UN CONJUNTO SE CUENTA DEL
  CODIGO, NO SE TECLEA.

- LO QUE NO SE ABRE Y LO QUE SIGUE ANOTADO. La deriva de contenido (26
  nodos de 140, 32 pares de 87, acta 92 seccion 4.4), los siete nodos
  con guion, el bloque repetido de formalizar_un_proceso_ad_hoc y los
  titulos gemelos por mayuscula (sistema_responsabilidad_gerencial y su
  _2) siguen ANOTADOS PARA ALEXIS Y SIN ENCARGAR, porque rozan el
  ALCANCE de la campana. Y sigue constando que Gate 0 tiene razon al dar
  0 en duplicadas: su guarda dice "titulo_concepto EXACTO duplicado" y
  esos dos titulos no son exactos. SE ANADE UNO NUEVO, MEDIDO POR MI HOY
  Y TAMBIEN SIN ENCARGAR: el resolvedor de alias de la casa vive
  replicado a mano en MAS DE VEINTE ficheros de scripts/loop
  (acta21_auditor_medir.py:127, auditor_v52_verifica.py:96,
  vuelta24_ops07.py:48, vuelta39_acto.py:62, vuelta64_puesto2.py:43 y
  siguientes) y ninguno importa una version compartida, porque _resolver
  de run_phase1.py es funcion anidada y no es importable. Tu replica
  declarada de la 117 fue lo correcto y la verifique escribiendo la mia.
  El refactor NO se encarga: se anota. La fase 06 NO se abre.

- LA NOTA DE HIGIENE DE SIEMPRE, remedida hoy por mi: git status trae M
  en dataset/metadata/master_graph.json desde antes de que nadie toque
  nada, y NO es un cambio (git diff --numstat sobre ese fichero da CERO
  lineas; es final de linea). Corri el ciclo de tres entero y despues
  medi: 8.391.653 bytes, sha256 f0e399396745. No lo commitees y no lo
  "arregles". El ciclo de tres es run_phase1.py, DESPUES etiquetas_de_
  cara.py CON --aplicar (sin --aplicar es dry run y el recompilado te
  deja las 71 etiquetas revertidas), y DESPUES sync_assets_web.py; el
  orden que fijaste en la 117 lo adjudique A FAVOR, porque conserva ese
  orden relativo e intercala las mediciones entre el segundo y el
  tercero. El validador vive en scripts/run_phase1.py, y
  etiquetas_de_cara.py y sync_assets_web.py viven en scripts/, NO en
  scripts/loop/; el recomputador del marcador, en
  scripts/recomputar_marcador.py. Y aviso medido: run_phase1.py termina
  con EXITCODE 2 por la alarma de las etiquetas aunque imprima GATE 0:
  OK; el verde que se publica es el de la linea "GATE 0: OK" y el ciclo
  se cierra con los otros dos pasos, no el exitcode del primero. Y un
  aviso mas, medido hoy: la clave nodos de master_graph.json es un
  DICCIONARIO de node_id a nodo, no una lista; quien la itere como lista
  obtiene cadenas y una cifra falsa.

- Y LAS CINCO DEL DICTADO, INTACTAS. La primera: toda cifra que publiques
  sobre un estado ANTERIOR se mide corriendo el instrumento sobre ese
  estado y se cita el fichero de salida; si la frase habla del antes Y
  del despues, son DOS ficheros, uno por lado. La segunda: toda vara que
  corras declara SU TECHO medido antes de correrse y SELLADO en su
  propio commit; una cosecha 0 sin techo declarado no cuenta como prueba
  de salud. La tercera: EL DOCSTRING DE UN INSTRUMENTO ES EXPEDIENTE Y
  SE MIDE COMO EL REPORTE, y el mensaje de commit igual. La cuarta: NO
  SE LE CAMBIA LA CONVENCION DE ENTRADA A UNA GUARDA SIN CORRER LA
  GUARDA DESPUES Y MIRAR SU SALIDA. La quinta: UNA CITA QUE PROMETE
  DETALLE ("declarado con el detalle completo en X", "explicado en X",
  "con su motivo en X") SOLO SE ESCRIBE SI X CONTIENE ESE DETALLE; si el
  detalle vive en el codigo o en el mensaje de commit, la cita nombra
  ESE sitio, o se mete el detalle en el fichero.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
