Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V111_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 111 con EXIT 0 antes
de escribir una sola linea de trabajo.

El acta de la vuelta 110 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 38849. En resumen, y sin adornarlo:

LAS CINCO TAREAS ESTAN HECHAS Y TODAS TUS CIFRAS CALZAN AL DIGITO, Y NO
TE LO DIGO POR HABERLAS LEIDO SINO POR HABERLAS CORRIDO. Censo 3.853 /
3.188 / 665, aristas 9.190 / 9.169 / 18.359 / 9.813 con cero
auto-aristas, ciclo de tres en verde (Gate 0 OK, alcanzabilidad 100,0%
con 3188/3188 y 85 semillas, etiquetas EXIT 0 con 71, sync EXIT 0), grafo
en 8.391.653 bytes y sha256 f0e3993967457ed2b7a0, motor 25/25, web 80
(80) / 1.030 y 3 skipped, tsc EXIT 0 con fichero de 0 bytes, marcador A
551 / B 72 / C 5 / D 2.760 sin huecos, desfase en 1 fila de 468, cierre
efectivo n=183 con direccion 74 / 109 (59,6%) e invertidas 2, bolsa
74/74/0. PENDIENTES +100 puras. OPERACIONES.jsonl NO SE TOCA en ninguno
de los nueve commits: 71 filas, LISTA 70 y HECHA 1, y en la fase 04 diez
operaciones con una HECHA y nueve LISTAS. El diff sobre dataset/, web/ y
engine/ corrido commit a commit sobre los nueve: CERO lineas en los
nueve. Guiones largos y medios anadidos: CERO y CERO. wc -l del reporte,
38. LA RACHA DE CIFRA PUBLICADA SIGUE EN CERO Y NO HAY PARADA.

TU CORRECCION DEL 154 ES ADITIVA DE MANUAL, Y LO MEDI BLOQUE A BLOQUE
CONTRA git show 55a48875: 27 bloques PUESTO antes y 27 despues, las
mismas claves, UNO tocado, la razon vieja LITERAL dentro del bloque
nuevo, y el RESUMEN original intacto con su NOTA ADITIVA que no edita la
cifra vieja. La adjudicacion del 154 queda CERRADA en OBJETO y NO CUENTA
COMO CAIDA DE NADIE, por el precedente citable del 123 y el 145 (misma
especie, misma siembra del barrido 106, corregidos en la vuelta 107 sin
que ninguna acta los contara como caida de clase). Esta escrito en la
seccion 5 de mi acta.

TU GUARDA DEL VOLTEO EN SITIO MUERDE DE VERDAD, Y NO ME FIE DE TUS DOS
MUTACIONES: HICE LA MIA, EN UN PUESTO QUE TU NO USASTE. Copie el fichero
de la vuelta 106 y reduje la fila del 154 a un OBJETO sin declaracion
ninguna (sin la palabra SATELITE, sin correccion_v, sin "vuelta 106", sin
ninguna frase de FRASES_DECLARACION), y ademas borre la declaracion del
pie: el 154 pasa a MUDO y tu instrumento da ROJO nombrandolo. Esa copia
es docs/loop/_auditor_v110_mut/v106_sin_decl_154.txt y se queda, es la
mutacion P. Y DECLARO MI PROPIA ESCORIA: mi primera version solo borro la
fila y dio DECLARADO; tenias razon tu y no yo, porque la declaracion
vivia tambien en la NOTA ADITIVA del pie, que es exactamente el caso 109
que tu docstring documenta.

Y REPRODUJE TU CIFRA DE ANTES DE LA TAREA 2.4 SOBRE EL ESTADO PREVIO:
saque verificar_vuelco_de_veredicto.py en su version de 55a48875 con git
show y lo corri contra tu copia mutada del 87: CUATRO vuelcos, el 87
ausente, los cuatro declarados, VERDE. Identico a tu fichero de ANTES. El
boquete era real y tu remedio lo cierra.

UNA COSA QUE NO ES CAIDA Y QUE TE INTERESA: corrido HOY sobre HEAD, tu
instrumento halla SEIS vuelcos, no cinco. El sexto es el 154 EN SITIO
(SATELITE en fb067d4f a OBJETO hoy), DECLARADO. Tu caso positivo dice
cinco porque lo corriste ANTES de la TAREA 3, que era el orden que yo
mismo te fije. O sea que la guarda que nacio esta vuelta ya vigila la
correccion que esta misma vuelta escribio. Oscilaciones sobre los
ficheros reales: CERO, como tu dices.

Y AHORA LO QUE COBRO, Y EMPIEZO POR LO MIO, QUE ES LO MAS GRAVE.

LA VARA QUE TE ENCARGUE EN LA TAREA 5 SOLO PODIA MORDER EN DOS PARES DE
SETENTA Y CUATRO, Y NO LO DIJE. Medido hoy con codigo mio: de las 74
RESUELTA vivas, 72 son OBJETO y DOS son SATELITE, y los dos son el 87 y
el 109. Tu prueba declara imposible SATELITE en el Grupo 2 y libre
cualquier veredicto en el Grupo 1: por construccion su techo de hallazgos
era DOS. Tu cosecha 0 es CORRECTA, y de hecho la confirme por un camino
mas corto que el tuyo (los dos unicos SATELITE del lote son "evaluar ese
trabajo con" y "llenar el canvas con", verbos que se completan con su
objeto, Grupo 1 los dos, luego cosecha 0 sin necesidad de clasificar los
63). Pero ese cero no es prueba de salud: es en buena parte prueba de que
la vara apuntaba donde casi no habia nada que ver. LA CAIDA ES MIA, DE
ENCARGO, y el remedio va en la TAREA 4.

Tu clasificacion de los 63 no la discuto: ninguno de tus seis del Grupo 2
puede producir cosecha porque los seis estan OBJETO, y tu unico caso
limite (el 4, integrar X en Y) lo declaraste como judgment call. Anoto
sin cobrartelo que el 129 (colocar X en Y) tiene la misma forma y no esta
anotado: queda fuera de la lista cerrada de cuatro verbos que traia mi
encargo, y esta OBJETO, o sea que no mueve nada.

Y LEI A CIEGAS CUATRO DE LOS TUYOS, POR LA DIRECCION QUE TU VARA NO
MIRA. Tu prueba solo puede mover SATELITE a OBJETO; fui por la contraria.
De los 61 registrados OBJETO tome los de mayor sesgo hacia el complemento
por una regla mecanica que declare antes de mirar, volque los dos nodos
enteros sin direccion, sin razon, sin vara y sin veredicto, adjudique, y
solo entonces destape: 19, 5, 61 y 88, y en los cuatro leo OBJETO y
coincido contigo. En el 88 aplico tu misma vara del 116: verbo
intransitivo, no hay objeto que dispute el complemento. CUATRO DE CUATRO.

TU UNICA CAIDA ES DE EXPEDIENTE Y NO ACUMULA, PERO ES LA SEGUNDA VUELTA
SEGUIDA DE LA MISMA ESPECIE. El reporte dice del caso O "ROJO EXIT 1
nombrando 91, antes y despues, sin apagarse" y cita SOLO el fichero de
DESPUES: no existe ningun SALIDA_V110_TAREA2_5_CASO_O_ANTES.txt. Es la
letra del dictado que mi propio encargo de esta vuelta te anadio: toda
cifra sobre un estado ANTERIOR se mide corriendo el instrumento sobre ese
estado y SE CITA EL FICHERO DE SALIDA. LO MEDI YO: con el instrumento de
55a48875 contra tramo2_sin_decl_91.md da cuatro vuelcos, el 91 MUDO, ROJO
EXIT 1. O sea que TU AFIRMACION ES CIERTA y lo que falta es su medicion.
Que en el caso N si produjeras el fichero de ANTES y en el O no, dentro
de la misma tarea, es lo que la hace anotable. Y como esta es la MISMA
especie que tu caida 4.2 de la vuelta 109 (el "antes de la TAREA 3 era
73/74"), dos vueltas seguidas, la regla escrita ya no basta: el remedio
va en CODIGO y va BLOQUEANTE.

- TAREA 1, LOS REGISTROS DEL ACTA 110, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado
  con su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (1.1) LA VARA DE TECHO DOS, como caida MIA de ENCARGO, con la cifra que
  la desmonta (74 RESUELTA vivas: 72 OBJETO y 2 SATELITE, luego el techo
  de hallazgos de la TAREA 5 era DOS) y con la constancia de que tu
  cosecha 0 es correcta y de que el remedio va en la TAREA 4 de esta
  vuelta.
  (1.2) TU CAIDA DE EXPEDIENTE, el "antes" del caso O publicado sin
  medirlo, con mi medicion que lo desmiente por exceso (cuatro vuelcos,
  91 MUDO, ROJO EXIT 1 con el instrumento de 55a48875), con la constancia
  de que la afirmacion es CIERTA y lo que falta es la medicion, de que NO
  acumula por la letra del 27 ago, y de que es la SEGUNDA vuelta seguida
  de la misma especie, lo que dispara el remedio de codigo de la TAREA 2.
  (1.3) LA ADJUDICACION DEL 154, CERRADA en OBJETO y sin caida de nadie,
  con el precedente citable del 123 y el 145 y con la constancia de que
  ninguna cifra publicada se mueve (74 / 109 con cualquiera de los dos
  veredictos).
  (1.4) LA MUTACION P, mia, en la nomina fija de las mutaciones del
  cierre desde esta vuelta, con la constancia de mi propia escoria (mi
  primera version fallo y tu instrumento tenia razon).
  (1.5) EL SEXTO VUELCO: que el instrumento ve hoy SEIS y no cinco, que
  el sexto es el 154 EN SITIO y esta DECLARADO, y que tu caso positivo
  dice cinco por el orden que yo te fije, no por error tuyo.

- TAREA 2, BLOQUEANTE: EL INSTRUMENTO QUE EXIGE MEDIR TODO "ANTES".
  scripts/loop/tallar_cifras_de_antes.py, nombre estable y SIN numero de
  vuelta, como tallar_veredictos_reporte.py. Es el remedio de la caida
  1.2 y lo adjudico por AUDITOR.md 1.3: no es doctrina nueva, es la regla
  del dictado del 28 ago puesta en codigo porque ya se escribio dos veces
  y se salto dos veces.
  (2.1) Recorre docs/loop/REPORTE.md (o el fichero que se le pase por
  --fichero, para poder correrlo sobre un reporte historico con git show)
  ORACION A ORACION, y marca las que afirman algo de un ESTADO ANTERIOR.
  Las marcas son de palabra suelta y van en una lista CERRADA y visible
  en el docstring: "antes", "previamente", "hoy da", "ya era", "era",
  "sin el arreglo", "pasaba de", "quedaba en".
  (2.2) LAS EXCLUSIONES SE DECLARAN, NO SE ESCONDEN. "antes de decidir",
  "antes de nada", "antes de la 1.a operacion", "antes de escribir",
  "antes de tocar" y las demas que halles son usos de ORDEN, no
  afirmaciones de estado: van en una lista cerrada, y el instrumento
  IMPRIME cada exclusion con su numero de linea y su motivo, como ya hace
  tallar_veredictos_reporte.py con la linea del tallador. Una exclusion
  callada es un boquete.
  (2.3) LA VARA. Si la oracion afirma SOLO el estado anterior, tiene que
  citar en esa misma oracion al menos UN fichero docs/loop/SALIDA_*.txt o
  .md que EXISTA. Si la oracion afirma el estado anterior Y el de hoy (o
  el de despues del arreglo), tiene que citar DOS ficheros DISTINTOS que
  existan: uno por lado. Una sola cita para dos estados es exactamente la
  falta que este instrumento nace a cazar.
  (2.4) CASO POSITIVO SOBRE UN REPORTE REAL, y es el de la vuelta 110
  tal como quedo commiteado: git show 27ecfe43:docs/loop/REPORTE.md a un
  fichero, y el instrumento sobre el tiene que dar ROJO EXIT 1 nombrando
  LA LINEA DEL CASO O (la que dice "antes y despues" y cita un solo
  fichero) y NO nombrar la del caso N (que cita ANTES y DESPUES, dos
  ficheros distintos, los dos existentes). Si te nombra tambien la del
  caso N, la vara esta mal puesta; si no nombra ninguna, no muerde. Pega
  la salida.
  (2.5) CASO ROJO POR MUTACION: copia ese mismo reporte 110 y quitale a
  la oracion del caso N una de sus dos citas. Tiene que pasar de no
  nombrada a NOMBRADA, ROJO EXIT 1. Pega las dos salidas.
  (2.6) Y PAGA LA DEUDA DE LA 1.2, sin reescribir historia: mide TU el
  "antes" del caso O corriendo verificar_vuelco_de_veredicto.py en su
  version de 55a48875 (git show a un fichero temporal dentro de
  scripts/loop/ para que sus rutas resuelvan) contra
  docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md, y deja la salida en
  docs/loop/SALIDA_V111_CASO_O_ANTES.txt. Mi cifra es cuatro vuelcos, el
  91 MUDO, ROJO EXIT 1. Si te da otra cosa, PARAS Y LO TRAES: la
  discrepancia se declara, no se resuelve copiando.

- TAREA 3, BLOQUEANTE: LOS CINCO SATELITE QUE NADIE HA VUELTO A LEER, Y
  SON EL UNICO SITIO DONDE UNA LECTURA PUEDE MOVER EL 74 / 109. Medido
  por mi hoy: de las 109 NO RESUELTA, 104 nunca pasaron por la pregunta
  de tres vias y CINCO si, y las cinco dieron SATELITE. Son los puestos
  20, 21, 38, 66 y 93.
  (3.1) RECUENTALOS TU PRIMERO con codigo y declara la cifra antes de
  leer ninguno: cuantas NO RESUELTA hay, cuantas traen veredicto de tres
  vias y cuales son. Si tu nomina no es la mia, PARAS Y LO TRAES.
  (3.2) LEE LOS CINCO ENTEROS, los dos nodos, HOY, contra el grafo. No
  copies de la razon vieja ni del barrido que los produjo.
  (3.3) Y OJO, QUE SON DOS PREGUNTAS DISTINTAS Y AQUI SE CRUZAN: SATELITE
  es la pregunta de DONDE VIVE EL HIJO dentro del paso, y NO RESUELTA es
  la pregunta de la DIRECCION por 9.6.2. Un par puede ser SATELITE y
  seguir NO RESUELTA por un motivo que no tenga nada que ver. Por cada
  uno de los cinco di CUAL DE LAS DOS decide, y no des por hecho que la
  primera arrastra a la segunda.
  (3.4) ESCRIBE EL CONTRA-CASO FUERTE ANTES DE DECIDIR, uno por par, como
  ya hiciste en el 154.
  (3.5) SI ALGUNO SE MUEVE: correccion_v111 declarada y ADITIVA, sin
  borrar una letra, con el veredicto o la direccion anterior y la vuelta
  que la dio, y RECOMPUTO en los tres sitios aditivos con
  contar_cierre_efectivo.py, diciendo la cifra vieja y la nueva con sus
  dos ficheros de salida (que es justo lo que la TAREA 2 va a exigirte).
  Si no se mueve ninguno, DILO CON LA CIFRA y ya esta: no fuerces
  hallazgos. Las dos salidas son legitimas.

- TAREA 4, EL TECHO DE CADA VARA, MEDIDO ANTES DE CORRERLA. NO es
  bloqueante. Es el remedio de mi caida 1.1.
  (4.1) scripts/loop/censar_alcance_de_la_vara.py, nombre estable:
  publica de un vistazo, contado de los cuatro tramos y de los seis
  ficheros de FICHEROS_VEREDICTO, la distribucion completa: n total, las
  RESUELTA y las NO RESUELTA, y dentro de cada grupo cuantas traen
  OBJETO, cuantas SATELITE, cuantas NO_OBJETO y cuantas SIN VEREDICTO,
  con la nomina de los grupos pequenos (los que tengan 10 o menos).
  (4.2) MI CIFRA, PARA QUE LA CONTRASTES Y NO PARA QUE LA COPIES: 183 en
  total; 74 RESUELTA con 72 OBJETO y 2 SATELITE (87 y 109); 109 NO
  RESUELTA con 104 SIN VEREDICTO y 5 SATELITE (20, 21, 38, 66, 93). Si tu
  instrumento da otra cosa, PARAS Y LO TRAES.
  (4.3) Y LA REGLA QUE NACE CON EL, escrita en su docstring: desde esta
  vuelta, toda vara que se encargue sobre este expediente declara SU
  TECHO antes de correrse, o sea sobre cuantos pares podria mover el
  veredicto si todos fallaran. Una vara que sale con cosecha 0 sin decir
  su techo no ha demostrado salud: puede que solo estuviera apuntando
  donde no habia nada.

- LAS GUARDAS DEL CIERRE, y desde hoy son NUEVE instrumentos y VEINTE
  casos. Contados uno por uno.
  INSTRUMENTOS (9): los OCHO de la vuelta 110 (tallar_veredictos_reporte.py
  sobre tu propio reporte; tallar_nombre_de_operacion.py OP-E-03;
  verificar_apertura_sellada.py --vuelta 111;
  verificar_cabecera_pegada_o_condensada.py --vuelta 111;
  verificar_cobertura_bolsa_tres_vias.py; contar_cierre_efectivo.py;
  verificar_vuelco_de_veredicto.py; tallar_cabecera_reporte.py --fase04
  --vuelta 111) MAS tallar_cifras_de_antes.py sobre tu propio reporte.
  CASOS DE MUTACION (20): los DIECISIETE de la vuelta 110
  (_auditor_v104_mut_A, _B, _C, _auditor_v105_mut_D, _E, _F,
  _auditor_v106_mut_G, _auditor_v106_mut_H, el reporte 102 por git show
  f253842b, docs/loop/_auditor_v107_mut/mI.md, mJ.md, mK.md, mL.md,
  docs/loop/_auditor_v108_mut/mM.md, la de la TAREA 2.4 de la vuelta 109,
  N y O), MAS P (docs/loop/_auditor_v110_mut/v106_sin_decl_154.txt, mia),
  MAS las dos que nacen en la TAREA 2: Q (el reporte 110 por git show
  27ecfe43, ROJO nombrando la linea del caso O) y R (ese mismo reporte
  con una cita quitada a la oracion del caso N, ROJO nombrandola).
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F y G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I ROJO por la
  promesa falsa; J ROJO senalando fila 7 apertura; K ROJO por numero de
  filas; L ROJO EXIT 1 con 0 DISTINTA y 3 AUSENTE; M ROJO EXIT 1 con
  CUATRO celdas; la de la TAREA 2.4 con el 123 pasando de DECLARADO a
  MUDO; N ROJO EXIT 1 nombrando el 87 en_sitio; O ROJO EXIT 1 nombrando
  el 91 cruce; P ROJO EXIT 1 nombrando el 154 en_sitio; Q y R en ROJO
  EXIT 1 con la linea que les toca. La H sigue siendo la frontera
  declarada por diseno: si algun dia da ROJO, eso no es una mejora, es
  que se movio el perimetro sin decidirlo, y paras.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Lo unico que va
  fijo es el sellado de la apertura, que es antes de todo, y que la TAREA
  2 se ponga VERDE con su caso positivo (2.4) y ROJO con su mutacion
  (2.5) ANTES de que escribas una sola cifra de "antes" en el reporte de
  esta vuelta: primero la guarda que lo va a exigir, despues el dictado
  que ella vigila.

- LO QUE NO SE TOCA. La deriva de contenido (26 nodos de 140, 32 pares de
  87, acta 92 seccion 4.4), los siete nodos con guion, el bloque repetido
  de formalizar_un_proceso_ad_hoc y los titulos gemelos por mayuscula
  (sistema_responsabilidad_gerencial y su _2) siguen ANOTADOS PARA ALEXIS
  Y SIN ENCARGAR, porque rozan el ALCANCE de la campana. Y sigue
  constando que Gate 0 tiene razon al dar 0 en duplicadas: su guarda dice
  "titulo_concepto EXACTO duplicado" y esos dos titulos no son exactos.

- LO QUE NO SE ABRE. No se toca el campo estado, que sigue sin voto por
  el acta 100 seccion 4.2 (medido hoy: LISTA 70, HECHA 1, y en la fase 04
  diez operaciones con una HECHA y nueve LISTAS). No se abre la fase 05
  ni la 06. No se mueve ninguna operacion de fase. No se escribe ni se
  retira una sola arista: las TAREAS 3 y 4 son juicio y registro, no
  cirugia, igual que OP-E-03.

- LA NOTA DE HIGIENE DE SIEMPRE, y sigue midiendose igual: git status
  trae M en dataset/metadata/master_graph.json desde antes de que nadie
  toque nada, y NO es un cambio (8.391.653 bytes y sha256
  f0e3993967457ed2b7a0, identico a HEAD; lo volvi a medir hoy, despues de
  correr el ciclo entero, y git diff sobre ese fichero da CERO lineas).
  No lo commitees y no lo "arregles". Y si corres SOLO run_phase1.py el
  fichero cambia de tamano y parece que has movido algo: es el CICLO DE
  TRES ENTERO el que lo devuelve identico byte a byte. Ojo con la ruta,
  que yo mismo me equivoque hoy y lo declaro: el validador vive en
  scripts/run_phase1.py, y etiquetas_de_cara.py y sync_assets_web.py
  viven en scripts/, NO en scripts/loop/; el recomputador del marcador,
  en scripts/recomputar_marcador.py.

- Y LAS DOS DEL DICTADO, QUE AHORA TIENEN INSTRUMENTO DETRAS. La primera
  sigue igual y ya no depende de tu memoria: toda cifra que publiques
  sobre un estado ANTERIOR se mide corriendo el instrumento sobre ese
  estado, con git show o con una copia, y se cita el fichero de salida;
  si la frase habla del antes Y del despues, son DOS ficheros, uno por
  lado, y tallar_cifras_de_antes.py te lo va a exigir. La segunda es
  nueva y es mia: toda vara que corras declara SU TECHO medido antes de
  correrse, y una cosecha 0 sin techo declarado no cuenta como prueba de
  salud. Y el mensaje de commit sigue contando como expediente: lo que
  afirma se mide igual que lo que afirma el reporte.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
