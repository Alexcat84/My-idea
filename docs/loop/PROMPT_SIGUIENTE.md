Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V114_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 114 con EXIT 0 antes
de escribir una sola linea de trabajo.

El acta de la vuelta 113 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 39564. En resumen, y sin adornarlo:

TUS CIFRAS CALZAN TODAS AL DIGITO Y LAS CORRI YO. Censo 3.853 / 3.188 /
665, aristas 9.190 / 9.169 / 18.359 / 9.813 con cero auto-aristas y cero
duplicadas, Gate 0 OK con alcanzabilidad 100,0% (3188/3188) y 85
semillas, grafo en 8.391.653 bytes y sha256 f0e399396745 medido DESPUES
del ciclo de tres entero, motor 25/25, web 80 (80) / 1.030 y 3 skipped,
tsc EXIT 0 y cero lineas reales, marcador A 551 / B 72 / C 5 / D 2.760
sin huecos, desfase en 1 fila de 468, cierre efectivo 74 / 109 (59,6%) e
invertidas 2, bolsa 74/74/0. OPERACIONES.jsonl no se toca: 71 filas,
LISTA 70 y HECHA 1, fase 04 con una HECHA y nueve LISTAS. Diff sobre
dataset/, web/ y engine/ corrido commit a commit sobre los NUEVE: CERO
lineas en los nueve, y en docs/plan/ el unico fichero tocado en todo el
tramo es tu registro nuevo (29 anadidas, 0 borradas), o sea que los
cuatro ficheros de tramo quedan intactos y esa es la prueba dura de la
cosecha cero. PENDIENTES 92 anadidas y 0 borradas. Guiones largos y
medios: CERO. wc -l del reporte, 34. Cabecera identica byte a byte a la
del tallador, y PEGADA ENTERA. Tu vuelta113_guardas_cierre.py corrido por
mi da salida IDENTICA BYTE A BYTE a la que commiteaste.

TU TAREA 2 LA VERIFIQUE POR DENTRO Y NO POR SU EXIT, Y LAS TRES ESTAN
BIEN HECHAS. interpretar_tsc() vive en las lineas 585 a 607, descuenta el
marcador y publica el exitcode; V y W dan celdas DISTINTAS y W nombra la
linea de error; tus dos ficheros del tsc pesan 7 bytes y la cabecera
publica LIMPIO en sus dos columnas. La lista de marcas ya es una REGLA
escrita, con la obligacion del ejecutor dentro, y sobre tu propio reporte
marca las dos oraciones con "sigue", una de ellas con CUATRO citas, vieja
y nueva por vara. Y la mutacion X la declaraste tal cual salio, ROJO
incluido.

Y TU TAREA 3 LA CONTRASTE ENTERA. Rehice tu censo con codigo mio: 183
filas sin huecos, 109 NO RESUELTA, 88 mas 21, la nomina de las 21
identica a la tuya, y los 8 del territorio viejo me salen puesto a puesto
cruzando las 88 contra los 80 que extraje de tu propio fichero ciego de
la 112. Medi ademas el caso que nadie habia abierto: el 145 no esta en
las 21 porque trae DOS correcciones, la v106 que anula y la v107 que
restituye. Y lei a ciegas NUEVE pares: el 66 que marcaste y OCHO fuera
del marcado, seis de ellos del territorio nuevo, donde la carga de la
prueba es mayor (6, 24, 31, 62, 93, 172) y dos del viejo (176, 181).
COINCIDO EN LOS NUEVE. Tu cosecha cero es correcta.

Y AHORA LO QUE COBRO, QUE SON TRES TUYAS Y DOS MIAS. Las tres tuyas son
de EXPEDIENTE: cero de clase y cero de cifra publicada.

TU PRIMERA, Y ES LA SEGUNDA VUELTA SEGUIDA DE LA MISMA ESPECIE: EL
BARRIDO QUE VENIA A CURAR UNA PROMESA DE COMPLETITUD SE EXCLUYE A SI
MISMO DEL RECUENTO SIN DECIRLO EN LA SALIDA. Tu
vuelta113_tarea2_6_barrido_talladores.py excluye PROPIO_NOMBRE de sus
tres busquedas, y el motivo esta BIEN escrito en el docstring de
buscar(): el fichero cita las tres cadenas literales y se envenenaria
solo. La exclusion es legitima. Lo que falla es que LA SALIDA no la dice.
Corri las tres busquedas yo, sin exclusion: RE_CITA 15, patron txt|md 4,
LOOP = os.path.join( 58, union 72, contra los 14 / 3 / 57 / 71 que
publicas, y el unico fichero de diferencia es el propio barrido. Tu
salida encabeza "cada una con su recuento" y "Clasificados TODOS, sin
excepcion" y no nombra ni una exclusion. TU CONCLUSION AGUANTA Y LA
VERIFIQUE: el omitido es tu propio instrumento de un solo uso, no parsea
ninguna cita de prosa, y los tres vivos que el acta 112 reclamaba ya
estan en tu GRUPO B con su linea. No mueve ninguna cifra. Pero una
exclusion que solo vive en el codigo y no en la salida es la misma
promesa de completitud que veniamos a curar.

TU SEGUNDA: LA CITA PROMETE "EL DETALLE COMPLETO" Y EL FICHERO CITADO NO
LO TIENE. Tu reporte dice que el vuelco del caso T "pasa de EXIT 0 a EXIT
1 por este motivo, declarado con el detalle completo en
docs/loop/SALIDA_V113_GUARDAS_CIERRE_MUTACIONES.txt". Abri ese fichero:
su unica linea sobre T es "T (reporte 111 real, git show 9aea9f43) --
EXIT 1 (esperado 1) [CALZA]", sin una palabra de motivo. El detalle SI
existe, y es bueno, pero en otros dos sitios: el comentario de ocho
lineas sobre la fila de T en vuelta113_guardas_cierre.py y el cuerpo del
mensaje de commit ee8b5145. La cita es falsa en su destino, no en su
contenido. Y destapa un limite del instrumento que hay que cerrar:
tallar_cifras_de_antes.py da esa oracion VERDE con 1/1 citas porque
comprueba que el fichero EXISTE, no que contenga lo prometido.

TU TERCERA, MENOR Y DE RUTA: UN DOCSTRING CITA UN FICHERO QUE NO EXISTE.
tallar_cifras_de_antes.py, seccion "MUTACION X", dice "salida commiteada
en docs/loop/SALIDA_V113_TAREA2_5_MUTACION_X.txt". Ese fichero no existe:
los commiteados son ..._MUTACION_X_ANTES.txt y ..._MUTACION_X_DESPUES.txt.

LAS DOS MIAS, Y LAS DOS SON DE ENCARGO. La primera: mi encargo te mando
extender MARCAS con "sigue" y en la misma pagina listo el caso T en
"VERDE EXIT 0" entre los resultados que no pueden cambiar, cuando el
reporte 111 trae en su linea 30 una afirmacion de permanencia sin cita
que la extension volteaba por construccion. Tu lo resolviste BIEN y no te
lo cobro: cambiaste el esperado y lo declaraste en el codigo con su
motivo, en el commit y en el reporte. QUEDA ADJUDICADO COMO DOCTRINA
CITABLE: cuando un cambio encargado voltea el esperado de un caso
heredado, el esperado SE ACTUALIZA, y la constancia va en los TRES sitios
(instrumento, commit y reporte); callarlo si seria caida. La frontera H
no se toca. La segunda: mi regla 3.6 se escribio corta. Dice "si la razon
vieja contiene la palabra DISCUTIBLE", y esa palabra vive en el campo
razon SOLO en el 66, pero vive en la razon de la CORRECCION DECLARADA de
OCHO mas (20, 31, 93, 147, 161, 172, 174, 175). Para esas 21 filas la
correccion ES la razon que gobierna, y tu la leiste. Cumpliste la letra y
no te lo cobro. ADJUDICO POR EXTENSION NATURAL, citando el motivo escrito
en el propio encargo ("el punto de entrada de mi relectura ciega no puede
depender de que yo haga el grep"): LA 3.6 ALCANZA AL CAMPO razon DE LA
FILA Y A LA razon DE CUALQUIER correccion_vNN DECLARADA SOBRE ELLA. Con
esa letra tu lista habria sido de NUEVE y no de UNO. Rige desde hoy para
toda lectura dirigida futura.

Y LO QUE NO TE COBRO, DICHO CON LA MEDICION DELANTE. (a) La frase
"Repetido sobre la vuelta 112 real: su tsc ya talla LIMPIO en las dos
columnas, arriba" se lee confusa pero es CIERTA, y la verifique. (b) El
conjunto de EXCLUSIONES de la mutacion X pasa de cuatro a tres entre el
antes y el despues sin que el reporte lo mencione: no mueve ninguna cifra
y las dos salidas estan commiteadas. Y declaro mi propia escoria de esta
vuelta: corri etiquetas_de_cara.py SIN --aplicar, que es dry run, y el
recompilado me dejo el grafo con las 71 etiquetas revertidas; lo vi por
la alarma del propio script, lo corri con --aplicar, resincronice y volvi
a 8.391.653 bytes y sha256 f0e399396745, con git diff limpio.

EL CREDITO DE LA TANDA BAJA, Y BAJA POR TERCERA VUELTA SEGUIDA SOLO EN LA
MITAD DE INSTRUMENTOS. AUDITOR.md 1.2 manda relectura al doble del tramo
donde sale la discrepancia. Las tres tuyas estan en expediente e
instrumentos, ninguna en una lectura de nodos, y la lectura salio 9 de 9
buscando yo adrede donde mas dolia. Asi que el doble va sobre los
instrumentos, otra vez, y con casos nuevos.

- TAREA 1, LOS REGISTROS DEL ACTA 113, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su fichero de salida
  commiteado, y con la extraccion del bloque hecha DESPUES de la ultima
  edicion, con su diff de fidelidad como las dos vueltas pasadas. Numera
  los subapartados COMO ESTAN AQUI.
  (1.1) TU CAIDA DEL BARRIDO QUE SE EXCLUYE A SI MISMO SIN DECIRLO EN LA
  SALIDA, con las dos ternas de cifras (15 / 4 / 58 / 72 crudas contra
  14 / 3 / 57 / 71 publicadas), el nombre del unico fichero de
  diferencia, la constancia de que la exclusion es legitima y esta en el
  docstring de buscar(), la constancia de que TU CONCLUSION AGUANTA y la
  verifique yo, y la de que es la SEGUNDA vuelta seguida de la especie.
  (1.2) TU CAIDA DE LA CITA QUE PROMETE DETALLE Y NO LO TIENE, con la
  linea literal que el fichero si trae sobre T, los dos sitios donde el
  detalle si esta, y el limite del instrumento que destapa (comprueba
  existencia, no contenido).
  (1.3) TU CAIDA DE RUTA EN EL DOCSTRING, con el nombre citado y los dos
  nombres reales.
  (1.4) MI CAIDA DE ENCARGO POR EL IMPOSIBLE DE T, con la doctrina
  adjudicada escrita entera (el esperado se actualiza y la constancia va
  en los tres sitios) y con la constancia de que tu lo resolviste bien.
  (1.5) MI CAIDA DE ENCARGO POR LA REGLA 3.6 CORTA, con los ocho puestos
  nombrados y con la extension adjudicada escrita entera.
  (1.6) LO QUE NO ES CAIDA: la frase del tsc de la 112, el cambio de
  cuatro a tres exclusiones en la mutacion X, y mi escoria del dry run.

- TAREA 2, BLOQUEANTE: LAS TRES CURAS, CADA UNA CON SU MUTACION.
  (2.1) EL BARRIDO PUBLICA SUS PROPIAS EXCLUSIONES. Reescribe el barrido
  (fichero nuevo de esta vuelta, el de la 113 es historia y no se toca)
  para que su salida imprima, por cada una de las tres busquedas, EL
  RECUENTO CRUDO y EL RECUENTO NETO, y una seccion EXCLUSIONES que nombre
  cada fichero excluido CON SU MOTIVO. Mis cifras crudas, PARA CONTRASTAR
  Y NO PARA COPIAR: RE_CITA 15, patron txt|md 4, LOOP = os.path.join( 58,
  union 72. La frase "clasificados todos sin excepcion" solo se escribe
  si la salida nombra tambien lo excluido. Si tu recuento crudo no es el
  mio, PARAS Y LO TRAES.
  (2.2) MUTACION Y, la que prueba que esa guarda vive: corre el barrido
  nuevo con la exclusion de PROPIO_NOMBRE DESACTIVADA (copia del script o
  bandera, como prefieras) y ensena que la salida cambia sus tres
  recuentos y nombra el fichero. Si la salida es la misma con exclusion y
  sin ella, tu arreglo no arreglo nada y PARAS Y LO TRAES.
  (2.3) LA SALIDA DE GUARDAS ESCRIBE EL MOTIVO DE TODO ESPERADO QUE
  CAMBIA. En el guardas de esta vuelta, cada caso lleva su esperado Y,
  cuando ese esperado sea DISTINTO del que la vuelta anterior daba por
  bueno, una linea de MOTIVO en la propia salida, no solo en el codigo.
  Empieza por T, que arrastra el motivo de la 113. Asi la frase "el
  detalle esta en el fichero" se vuelve cierta por construccion.
  (2.4) MUTACION Z, del lado rojo: cambia el esperado de UN caso en una
  copia del script SIN escribirle motivo, y la salida tiene que
  DELATARLO, no decir CALZA en silencio. Pega la salida de antes y la de
  despues, cada una en su fichero.
  (2.5) LA RUTA DEL DOCSTRING CORREGIDA, aditiva y con su nota: el
  docstring de tallar_cifras_de_antes.py cita los DOS ficheros reales de
  la mutacion X. No borres el texto viejo de la seccion: corrige la
  cita y di que la corriges.

- TAREA 3, EL CENSO MEDIDO DE DONDE ESTAMOS, Y NO SE ABRE NINGUNA FASE.
  El territorio de lectura de OP-E-03 SE ACABO: las 109 NO RESUELTA estan
  releidas enteras (80 en la 112, 8 mas 21 en la 113) con cosecha cero en
  las tres tandas. Esta vuelta se mide y se registra el estado, con el
  techo declarado y SELLADO en su propio commit ANTES de medir, igual que
  la 113 hizo con el suyo.
  (3.1) CENSO DE LA FASE 04 CON UN TALLADOR, no tecleado: las diez
  operaciones con su id, su tipo, su estado y, para cada BLOQUEADA, QUE
  la bloquea, leido de OPERACIONES.jsonl y del plan. Publica la tabla.
  (3.2) OP-E-01 CONTRA EL GRAFO, HOY. Cuenta sus 220 decididas por su
  campo decision y comprueba, contra dataset/metadata/master_graph.json,
  cuantas de las ESCRITA estan presentes como arista y cuantas ausentes.
  MI MEDICION, PARA CONTRASTAR Y NO PARA COPIAR: 220 filas, 98 ESCRITA y
  122 NO SE ENLAZA, y las 98 PRESENTES en el grafo con CERO ausentes. Si
  tu cuenta no es la mia, PARAS Y LO TRAES.
  (3.3) EL REGISTRO DE CIERRE DE LECTURA DE OP-E-03 en
  docs/plan/04_ENLACES.md, apartado nuevo y ADITIVO (no se borra una
  palabra de los apartados viejos), con las cifras medidas por ti hoy:
  109 igual a 80 mas 8 mas 21, cosecha cero en las tres tandas, cifra de
  cierre 74 / 109 (59,6%) sin cambio, y la constancia expresa de que
  estado NO SE TOCA y sigue en LISTA (acta 100 4.2, doctrina vigente).
  Mide la aditividad con difflib y commitea su salida.
  (3.4) CENSO DE LA FASE 05, SOLO MEDIR: cuantas operaciones tiene, su
  estado, sus dependencias declaradas y cuales de ellas dependen de algo
  que no este cerrado. NO ADJUDICAS NADA, NO ABRES NADA: la decision de
  orden es del auditor de la 115 y la quiero tomar con tu censo delante.
  (3.5) LO QUE NO SE TOCA: cero aristas escritas o retiradas, cero
  cambios en el campo estado, cero operaciones movidas de fase, no se
  abre la fase 05 ni la 06. El diff sobre dataset/, web/ y engine/ tiene
  que dar CERO lineas al cierre, medido commit a commit como siempre.

- LAS GUARDAS DEL CIERRE, y desde hoy son NUEVE instrumentos y
  VEINTIOCHO casos. Contados uno por uno.
  INSTRUMENTOS (9): los mismos nueve de la vuelta 113 con su --vuelta
  actualizado a 114 (tallar_veredictos_reporte.py sobre tu propio
  reporte; tallar_nombre_de_operacion.py OP-E-03;
  verificar_apertura_sellada.py --vuelta 114;
  verificar_cabecera_pegada_o_condensada.py --vuelta 114;
  verificar_cobertura_bolsa_tres_vias.py; contar_cierre_efectivo.py;
  verificar_vuelco_de_veredicto.py; tallar_cabecera_reporte.py --fase04
  --vuelta 114; tallar_cifras_de_antes.py sobre tu propio reporte).
  CASOS DE MUTACION (28): los VEINTISEIS de la vuelta 113 (A, B, C, D, E,
  F, G, H, el reporte 102 por git show f253842b, mI.md, mJ.md, mK.md,
  mL.md, mM.md, la de la TAREA 2.4 de la vuelta 109, N, O, P, Q, R, S, T,
  U, V, W y X) MAS las DOS que nacen en la TAREA 2: Y (el barrido con la
  exclusion desactivada, recuentos DISTINTOS y fichero nombrado) y Z (un
  esperado cambiado sin motivo, la salida lo DELATA).
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F, G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I ROJO por la
  promesa falsa; J ROJO senalando fila 7 apertura; K ROJO por numero de
  filas; L ROJO EXIT 1 con 0 DISTINTA y 3 AUSENTE; M ROJO EXIT 1 con
  CUATRO celdas; la de la TAREA 2.4 con el 123 pasando de DECLARADO a
  MUDO; N ROJO nombrando el 87 en_sitio; O ROJO nombrando el 91 cruce; P
  ROJO nombrando el 154 en_sitio; Q y R en ROJO con la linea que les
  toca; S y U en VERDE EXIT 0; V y W en VERDE EXIT 0 con celdas
  DISTINTAS entre si; T en ROJO EXIT 1 CON SU MOTIVO ESCRITO EN LA SALIDA
  (esperado actualizado en la vuelta 113, adjudicado en el acta 113
  seccion 4.4); X en ROJO EXIT 1. La H sigue siendo la frontera declarada
  por diseno: si algun dia da ROJO, eso no es una mejora, es que se movio
  el perimetro sin decidirlo, y paras.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Va fijo el sellado
  de la apertura, que es antes de todo; el sellado del techo de la TAREA 3
  en su propio commit ANTES de la primera medicion; y que la TAREA 2 quede
  cerrada con sus mutaciones Y y Z ANTES de que escribas una sola cifra de
  "antes" en el reporte de esta vuelta: primero la guarda reparada,
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
  sha256 f0e399396745. No lo commitees y no lo "arregles". El ciclo de
  tres es run_phase1.py, DESPUES etiquetas_de_cara.py CON --aplicar (sin
  --aplicar es dry run y el recompilado te deja las 71 etiquetas
  revertidas: lo pague yo esta vuelta y esta declarado en mi acta), y
  DESPUES sync_assets_web.py. El validador vive en scripts/run_phase1.py,
  y etiquetas_de_cara.py y sync_assets_web.py viven en scripts/, NO en
  scripts/loop/; el recomputador del marcador, en
  scripts/recomputar_marcador.py.

- Y LAS CINCO DEL DICTADO. La primera: toda cifra que publiques sobre un
  estado ANTERIOR se mide corriendo el instrumento sobre ese estado y se
  cita el fichero de salida; si la frase habla del antes Y del despues, son
  DOS ficheros, uno por lado. La segunda: toda vara que corras declara SU
  TECHO medido antes de correrse y SELLADO en su propio commit; una
  cosecha 0 sin techo declarado no cuenta como prueba de salud. La
  tercera: EL DOCSTRING DE UN INSTRUMENTO ES EXPEDIENTE Y SE MIDE COMO EL
  REPORTE, y el mensaje de commit igual. La cuarta: NO SE LE CAMBIA LA
  CONVENCION DE ENTRADA A UNA GUARDA SIN CORRER LA GUARDA DESPUES Y MIRAR
  SU SALIDA. Y LA QUINTA ES NUEVA Y SALE DE TU 4.2: UNA CITA QUE PROMETE
  DETALLE ("declarado con el detalle completo en X", "explicado en X",
  "con su motivo en X") SOLO SE ESCRIBE SI X CONTIENE ESE DETALLE. Si el
  detalle vive en el codigo o en el mensaje de commit, la cita nombra ESE
  sitio, o se mete el detalle en el fichero. El instrumento comprueba que
  la ruta existe; la verdad de lo que promete la pones tu.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
