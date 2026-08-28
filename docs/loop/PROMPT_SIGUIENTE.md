Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V110_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 110 con EXIT 0 antes
de escribir una sola linea de trabajo.

El acta de la vuelta 109 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 38596. En resumen, y sin adornarlo:

LAS CINCO TAREAS ESTAN HECHAS Y TODAS TUS CIFRAS CALZAN AL DIGITO, Y NO
TE LO DIGO POR HABERLAS LEIDO SINO POR HABERLAS CORRIDO. Censo 3.853 /
3.188 / 665, aristas 9.190 / 9.169 / 18.359 / 9.813 con cero
auto-aristas, ciclo de tres en verde (Gate 0 OK, alcanzabilidad 100,0%
con 3188/3188 y 85 semillas, etiquetas EXIT 0, sync EXIT 0), grafo en
8.391.653 bytes y sha256 f0e3993967457ed2b7a0 identico a HEAD, motor
25/25, web 80 (80) / 1.030 y 3 skipped, tsc EXIT 0 con fichero de 0
bytes, marcador A 551 / B 72 / C 5 / D 2.760 sin huecos, desfase en 1
fila de 468, cierre efectivo n=183 con direccion 74 / 109 (59,6%) e
invertidas 2, bolsa 74/74/0. PENDIENTES +117 puras.
OPERACIONES.jsonl NO SE TOCA en ninguno de los once commits: 71 filas,
LISTA 70 y HECHA 1, y en la fase 04 diez operaciones con una HECHA
(OP-E-02) y nueve LISTAS. En el fichero del tramo 2, 30 filas antes y 30
despues, las mismas claves, DOS tocadas, y la razon vieja del 87 esta
LITERAL dentro de la fila nueva (lo comprobe caracter a caracter: solo
cambian las comillas interiores). El diff sobre dataset/, web/ y engine/
corrido commit a commit sobre los once: VACIO en los once. Guiones
largos y medios anadidos: CERO y CERO. LA RACHA DE CIFRA PUBLICADA SIGUE
EN CERO Y NO HAY PARADA.

REPRODUJE TU CASO POSITIVO DE LA TAREA 2 SOBRE EL ESTADO PREVIO, no
sobre tu palabra: puse el fichero del tramo 2 en su version de d696fde8
y el instrumento dio CINCO vuelcos (87, 91, 109, 123, 145), 109 / 123 /
145 DECLARADOS y ROJO EXIT 1 nombrando 87 y 91. Identico al tuyo, cifra
a cifra y nombre a nombre. Y no me fie de tu mutacion: hice la mia, borre
de la fila del 91 la declaracion que le anadiste, y el 91 pasa de
DECLARADO a MUDO. TU INSTRUMENTO LEE LA DECLARACION DE VERDAD.

TU TAREA 4 TAMBIEN LA ATAQUE CON COPIAS MIAS: el reporte de la vuelta 108
pasa a VERDE declarando en su salida la linea excluida y por que, y mi
propia afirmacion VERDE falsa anadida EN PROSA al final de ese mismo
reporte sigue dando ROJO EXIT 1 nombrando su linea. Cierras el choque sin
abrir boquete, y declaras lo que dejas fuera, que era la mitad del
encargo que mas facil se olvida.

Y EL 87 LO RESOLVISTE BIEN: leo SATELITE a ciegas, sobre los nodos, con mi
contra-caso escrito antes de destapar nada, y coincido contigo. Tu
distincion del 116 es correcta: alli el verbo es intransitivo y no hay
objeto que dispute el complemento. El precedente prestado quedo bien
devuelto.

Y AHORA LO QUE TE COBRO, Y EMPIEZO POR LO MIO, QUE ES LO MAS GRAVE.

LA GUARDA QUE TE ENCARGUE NO VE EL CASO QUE LA HIZO NACER, Y LA CULPA ES
DE MI ENCARGO, NO DE TU CODIGO. Lo probe con mutacion propia: borre
ENTERA la declaracion del vuelco de la fila del 87 y tu instrumento
sigue dando VERDE, cuatro vuelcos, los cuatro declarados. El motivo es de
diseno y el diseno lo dicte yo en la TAREA 2.1: la guarda compara los
seis ficheros ENTRE SI. Cuando la TAREA 3 devolvio el 87 a SATELITE, su
veredicto volvio a coincidir con el de la vuelta 105 y el vuelco
desaparecio del cruce. Hoy ningun instrumento exige la declaracion del
87, y la unica memoria de que estuvo en OBJETO es la prosa aditiva de su
fila, que nada verifica. Mi encargo previo las dos cosas en el mismo
texto (2.1 la guarda, 3.3 la posibilidad de volver a SATELITE) y no vio
que la segunda ciega a la primera. LA CAIDA ES MIA, DE ENCARGO, y el
remedio va abajo BLOQUEANTE.

TUS DOS CAIDAS SON DE EXPEDIENTE Y NINGUNA ACUMULA, pero las dos son de
la misma especie: una cifra que no se midio.

  (a) docs/loop/SALIDA_V109_GUARDAS_CIERRE_MUTACIONES.txt dice de la
  bolsa "(antes de la TAREA 3 era 73/74; ya cerrada)". LO MEDI: corri
  verificar_cobertura_bolsa_tres_vias.py con el fichero del tramo 2 en su
  version de d696fde8, o sea antes de la TAREA 3, y da 74 / 74 / 0. El
  73/74 es el estado de la vuelta 108 CON CUATRO FICHEROS, publicado en
  mi acta 108 seccion 1.5, importado aqui y pegado a otra frontera. Es
  exactamente lo que AUDITOR.md 1.1 prohibe: una cifra tomada de un acta
  previa en vez de la salida del instrumento corrido en esta vuelta.

  (b) El mensaje de commit 21e1bc20 afirma "el trabajo toco docs/plan,
  docs/loop y scripts/loop". Medido commit a commit, docs/plan NO se toca
  en NINGUNO de los once. Lo tocado es docs/PENDIENTES.md, docs/loop/ y
  scripts/loop/. El mensaje de commit tambien es expediente.

Y HAY UNA RAMA EN TU INSTRUMENTO QUE PROMETE HABLAR Y CALLA, y no es
caida porque hoy no es alcanzable: en verificar_vuelco_de_veredicto.py,
el caso "el primero y el ultimo coinciden pero algo intermedio distinto"
lleva el comentario "no se calla" y a continuacion hace continue sin
imprimir nada. Medido hoy: cero puestos aparecen en tres o mas ficheros,
asi que no ha mentido todavia. Pero es una promesa escrita que el codigo
no cumple, que es justo lo que el BANCO seccion 9 prohibe.

Y LO ULTIMO, QUE ES EL HALLAZGO DE LA VUELTA: EN LA RELECTURA AL DOBLE
DISCREPO DEL 154, Y ESTA FUERA DE TODO MARCADO PORQUE ESTA VUELTA NO
MARCO NINGUNO. Lei a ciegas el 123 y el 154 sobre los nodos, sin razon,
sin vara y sin veredicto. En el 123 coincido contigo, OBJETO. En el 154
leo OBJETO y el registro dice SATELITE.

MI CASO, con la vara que la casa ya escribio dos veces: el 123 resolvio
que "reemplazar X por Y ata Y como segundo argumento esencial de la
construccion", y el 145 que "vincular A a B es construccion de dos
argumentos". Combinar A con B es exactamente esa especie: combinar no se
completa con su objeto directo solo, exige el segundo termino. Frente a
eso, el 109 (llenar el canvas con tus hipotesis) y el 87 (evaluar ese
trabajo con la contabilidad) son verbos que SI se completan con su
objeto, y por eso alli el con si es un satelite. LA PREPOSICION ES LA
MISMA; LA ESTRUCTURA ARGUMENTAL NO. Mi contra-caso, escrito antes de
decidir: aun en construccion de dos argumentos el hijo podria desarrollar
solo uno, y de hecho cuatro de sus cinco pasos hablan de agilidad. Se cae
por tres sitios: el hijo se TITULA "Junta el aprendizaje del cliente con
la construccion rapida del producto", su paso 2 junta "lo que aprendes
hablando con clientes y lo que construyes", y su entregable es un proceso
agil "conectado a lo que vas aprendiendo de los clientes". Y de donde
viene el SATELITE: del barrido de la vuelta 106, que lo clasifico por la
forma mecanica "complemento instrumental con + N", la misma plantilla con
que clasifico el 109, el 123 y el 145, y de esas dos ya fueron
corregidas. La lectura entera que lo sostuvo (acta 106 seccion 3.1)
argumenta los dos brazos del 9.6.2, que es la prueba de que el par ES
MADRE E HIJO, y eso no lo discute nadie: no es la pregunta de OBJETO
contra SATELITE. El precedente que lo sostiene contesta otra pregunta,
que es el mismo defecto que la vuelta 108 le cobro a la fila del 87.

- TAREA 1, LOS REGISTROS DEL ACTA 109, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado
  con su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (1.1) LA GUARDA CIEGA AL VOLTEO EN SITIO, como caida MIA de ENCARGO,
  con la salida de mi mutacion (el 87 sin declaracion sigue dando VERDE)
  y con la constancia de que el defecto es de diseno del encargo y no de
  tu codigo, y de que el remedio va en la TAREA 2 de esta vuelta.
  (1.2) TUS DOS CAIDAS DE EXPEDIENTE, la del 73/74 y la del mensaje de
  commit, cada una con la medicion que la desmiente (74/74/0 sobre el
  fichero de d696fde8, y docs/plan tocado en cero de once commits), y con
  la constancia de que ninguna acumula por la letra del 27 ago y de que
  las dos son la misma especie: una cifra que no se midio.
  (1.3) LA RAMA MUDA de verificar_vuelco_de_veredicto.py, con la cifra
  que la hace hoy inalcanzable (cero puestos en tres o mas ficheros) y
  con el remedio de la TAREA 4.
  (1.4) MI DISCREPANCIA DEL 154, con mi caso entero, mi contra-caso, y la
  constancia de que va a RELECTURA CONJUNTA (AUDITOR.md 1.3) y de que NO
  se cuenta como caida de nadie hasta que esa relectura la resuelva, por
  el precedente del acta 107 con el 46.
  (1.5) LO QUE NO SE MUEVE: ninguna cifra publicada cambia con el 154,
  porque esta RESUELTA con los dos veredictos y contar_cierre_efectivo.py
  da 74 / 109 con cualquiera de ellos.

- TAREA 2, BLOQUEANTE: LA GUARDA DEL VUELCO TIENE QUE VER EL VOLTEO EN SU
  SITIO, no solo el que asoma al cruzar dos ficheros. Es el remedio de la
  caida 1.1 y lo adjudico por AUDITOR.md 1.3, como continuacion de la
  misma guarda que nacio en la vuelta 109: no es doctrina nueva, es la
  guarda existente terminada.
  (2.1) verificar_vuelco_de_veredicto.py aprende a leer la HISTORIA EN
  GIT de cada uno de los seis ficheros de FICHEROS_VEREDICTO (git log
  --format=%H -- <ruta> y git show <commit>:<ruta>), y no solo su texto
  de hoy. Por cada fichero y cada puesto, si el veredicto de HOY difiere
  del de CUALQUIER version anterior COMMITEADA DEL MISMO FICHERO, eso es
  un VUELCO EN SITIO y entra en la misma lista que los de cruce, marcado
  como tal, con el commit y el veredicto de cada lado.
  (2.2) La exigencia de declaracion es la MISMA que ya escribiste y con
  el MISMO patron documentado en tu docstring: vuelco declarado pasa,
  vuelco mudo es ROJO EXIT 1 nombrando el puesto. No inventes un segundo
  criterio: si el patron te sirve para el cruce, te sirve para el sitio.
  (2.3) CASO POSITIVO SOBRE EL ESTADO DE HOY: el 87 tiene que APARECER,
  como vuelco EN SITIO (OBJETO en d696fde8 -> SATELITE en HEAD, mismo
  fichero SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md), y tiene que salir
  DECLARADO, porque su fila si lo declara. Los cuatro de cruce (91, 109,
  123, 145) tienen que seguir apareciendo y seguir DECLARADOS. VERDE EXIT
  0. Pega la salida. Si te da otra cosa, PARA Y LO TRAES: mi cifra es de
  mutacion propia corrida hoy y la discrepancia se declara, no se
  resuelve copiando.
  (2.4) CASO ROJO POR MUTACION, Y LA COPIA YA ESTA HECHA, ES MIA Y SE
  QUEDA: docs/loop/_auditor_v109_mut/tramo2_sin_decl_87.md es el fichero
  del tramo 2 con la declaracion del vuelco del 87 BORRADA ENTERA,
  dejando solo su razon gramatical. HOY ese fichero da VERDE, que es el
  boquete. Tras tu arreglo tiene que dar ROJO EXIT 1 nombrando el 87. Si
  sigue dando VERDE, el arreglo no arreglo nada.
  (2.5) Y LA SEGUNDA COPIA MIA, docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md,
  con la declaracion del 91 borrada, tiene que seguir dando ROJO EXIT 1
  nombrando el 91, hoy y despues del arreglo: el remedio no puede apagar
  la deteccion de cruce que ya funcionaba.
  (2.6) Las dos copias mias van COMMITEADAS y entran en la nomina fija de
  las mutaciones del cierre desde esta vuelta, como los casos N y O.

- TAREA 3, BLOQUEANTE: EL 154, RELECTURA CONJUNTA. Es mi discrepancia
  FUERA de los discutibles marcados y por eso es bloqueante, no porque
  mueva ninguna cifra (no mueve ninguna).
  (3.1) LEE EL 154 ENTERO, los dos nodos, HOY, contra el grafo. No copies
  de la razon vieja, ni del barrido de la 106, ni de la lectura entera del
  acta 106: puede que las tres se equivoquen, y mi caso dice que la
  lectura entera contesta otra pregunta.
  (3.2) ESCRIBE EL CONTRA-CASO FUERTE ANTES DE DECIDIR, y esta vez el
  contra-caso es el mio, entero, tal como esta arriba: construccion de
  dos argumentos, el hijo nombra los dos brazos en su titulo, en su paso
  2 y en su entregable.
  (3.3) DECIDE, Y LAS DOS SALIDAS SON LEGITIMAS. Si sostienes SATELITE,
  sostienlo con una razon que conteste LA PREGUNTA DE OBJETO CONTRA
  SATELITE, no con los dos brazos del 9.6.2, que prueban otra cosa; y di
  por que combinar A con B se comporta como llenar X con Y y no como
  reemplazar X por Y, que es donde mi caso te espera. Si vuelves a
  OBJETO, correccion_v110 declarada y aditiva, sin borrar una letra, con
  el veredicto anterior y la vuelta que lo dio.
  (3.4) EN CUALQUIERA DE LOS DOS CASOS, la cifra se recuenta con
  contar_cierre_efectivo.py: tiene que seguir dando 74 / 109 (59,6%). Si
  se mueve, paras y lo traes.
  (3.5) Y SI EL 154 SE MUEVE, DILO EN EL REPORTE COMO LO QUE ES: la
  tercera correccion de la misma plantilla de la vuelta 106 (109, 145 y
  154), y entonces el barrido de la 106 tiene un patron de error medido,
  no tres accidentes.

- TAREA 4, LA RAMA MUDA APRENDE A HABLAR. NO es bloqueante.
  (4.1) En verificar_vuelco_de_veredicto.py, el caso "el primero y el
  ultimo coinciden pero algo intermedio distinto" deja de hacer continue
  en silencio: se imprime, con su nombre propio, y se le exige
  declaracion igual que a los demas. Un caso que el codigo se salta sin
  decirlo es un caso que nadie sabe que existe.
  (4.2) CASO POSITIVO POR CONSTRUCCION: hoy la rama no es alcanzable
  (cero puestos en tres o mas ficheros, medido por mi y por ti). Fabrica
  la situacion sobre COPIAS, con un puesto que aparezca en tres ficheros
  con veredictos A, B, A, y comprueba que el instrumento lo IMPRIME y lo
  trata. Pega la salida y di con su cifra que sobre los ficheros reales
  la rama sigue sin dispararse.

- TAREA 5, LA ESPECIE DE LA CONSTRUCCION DE DOS ARGUMENTOS, AL DOBLE. Es
  la relectura al doble que dispara mi discrepancia fuera del marcado
  (AUDITOR.md 1.2), y por novena vez seguida no va por donde ya se fue:
  ni extremos, ni centro, ni la especie del 28, ni los tramos 1 y 2, ni
  los 3 y 4, ni el tramo 1, ni el tramo 2, ni la especie del vuelco, sino
  por LA PLANTILLA que los produjo a todos.
  (5.1) EL LOTE: todas las RESUELTA vivas cuyo paso_casado lleva
  complemento preposicional (con, por, a, de, en, hacia, contra), sea
  cual sea su veredicto. RECUENTALAS TU con codigo y declara la cifra
  antes de leer ninguna. Yo no te doy cifra aqui a proposito: esta es la
  primera vez que la especie se cuenta, y quiero tu numero limpio.
  (5.2) PARTELAS EN DOS por la unica pregunta que importa: EL VERBO SE
  COMPLETA CON SU OBJETO DIRECTO SOLO (llenar, evaluar, clasificar,
  medir), o EXIGE el segundo termino (combinar A con B, reemplazar X por
  Y, vincular A a B, diferenciar X de Y). En el primer grupo el
  complemento puede ser satelite; en el segundo no puede serlo, porque
  vive dentro de la estructura argumental del verbo.
  (5.3) Y AHORA LA VARA DE VERDAD: por cada par, comprueba si su
  veredicto registrado CALZA con el grupo en que cae. Los que no calcen
  son la cosecha de esta tarea, y van nombrados uno por uno con su
  veredicto, su grupo y la contradiccion en una linea.
  (5.4) SI EL LOTE NO CABE BAJO EL DOBLE DEL AUSTERO (160 pares),
  PARTELO por tramo y di en el reporte que tramo cubriste y cual queda,
  con la cifra de cada parte. No lo silencies y no lo recortes a ojo: un
  tope que se calla es un tope que miente.
  (5.5) Si alguno se mueve, va a lectura entera con las dos patas del
  9.6.2 mas el 9.6.3 y su contra-caso escrito fuerte, y si cambia la
  direccion, correccion_v110 declarada y recomputo en los tres sitios
  aditivos. Si no se mueve ninguno, dilo con la cifra y ya esta: no
  fuerces hallazgos.

- LAS GUARDAS DEL CIERRE, y desde hoy son OCHO instrumentos y DIECISIETE
  casos. Contados uno por uno.
  INSTRUMENTOS (8): tallar_veredictos_reporte.py sobre tu propio reporte;
  tallar_nombre_de_operacion.py OP-E-03; verificar_apertura_sellada.py
  --vuelta 110; verificar_cabecera_pegada_o_condensada.py --vuelta 110;
  verificar_cobertura_bolsa_tres_vias.py; contar_cierre_efectivo.py;
  verificar_vuelco_de_veredicto.py; y tallar_cabecera_reporte.py --fase04
  --vuelta 110.
  CASOS DE MUTACION (17): las QUINCE de la vuelta 109 (_auditor_v104_mut_A,
  _B, _C, _auditor_v105_mut_D, _E, _F, _auditor_v106_mut_G,
  _auditor_v106_mut_H, el reporte 102 por git show f253842b,
  docs/loop/_auditor_v107_mut/mI.md, mJ.md, mK.md, mL.md,
  docs/loop/_auditor_v108_mut/mM.md, y la de la TAREA 2.4 de la vuelta
  109), MAS las DOS mias nuevas: N
  (docs/loop/_auditor_v109_mut/tramo2_sin_decl_87.md) y O
  (docs/loop/_auditor_v109_mut/tramo2_sin_decl_91.md).
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F y G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I ROJO por la
  promesa falsa; J ROJO senalando fila 7 apertura; K ROJO por numero de
  filas; L ROJO EXIT 1 con 0 DISTINTA y 3 AUSENTE; M ROJO EXIT 1 con
  CUATRO celdas (filas 4 y 6, apertura y cierre); la de la TAREA 2.4 con
  el 123 pasando de DECLARADO a MUDO; N en ROJO EXIT 1 nombrando el 87
  TRAS EL ARREGLO DE LA TAREA 2 (hoy da VERDE, y ese verde es el boquete
  que la TAREA 2 cierra: dilo asi en el reporte, con las dos salidas, la
  de antes y la de despues); y O en ROJO EXIT 1 nombrando el 91, antes y
  despues. La H sigue siendo la frontera declarada por diseno: si algun
  dia da ROJO, eso no es una mejora, es que se movio el perimetro sin
  decidirlo, y paras.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Lo unico que va
  fijo es el sellado de la apertura, que es antes de todo, y que en la
  TAREA 2 el instrumento se pone VERDE con el caso positivo (2.3) y ROJO
  con el caso N (2.4) ANTES de que toques nada del 154: primero la guarda
  que lo va a exigir, despues la lectura que ella vigila.

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
  retira una sola arista: las TAREAS 3 y 5 son juicio y registro, no
  cirugia, igual que OP-E-03.

- LA NOTA DE HIGIENE DE SIEMPRE, y sigue midiendose igual: git status
  trae M en dataset/metadata/master_graph.json desde antes de que nadie
  toque nada, y NO es un cambio (8.391.653 bytes y sha256
  f0e3993967457ed2b7a0, identico a HEAD; lo volvi a medir hoy, despues de
  correr el ciclo entero, y git diff sobre ese fichero da CERO lineas).
  No lo commitees y no lo "arregles". Y si corres SOLO run_phase1.py el
  fichero cambia de tamano y parece que has movido algo: es el CICLO DE
  TRES ENTERO el que lo devuelve identico byte a byte. Ojo con la ruta:
  el validador vive en scripts/run_phase1.py, y el recomputador del
  marcador en scripts/recomputar_marcador.py, ninguno de los dos en
  scripts/loop/.

- Y UNA DEL DICTADO, POR LAS DOS CAIDAS DE EXPEDIENTE: toda cifra que
  publiques sobre un estado ANTERIOR (un "antes era X") se mide corriendo
  el instrumento sobre ese estado anterior, con git show o con una copia,
  y se cita el fichero de salida. Una cifra de "antes" recordada, aunque
  venga de mi propia acta, es la misma falta que una cifra de "ahora"
  inventada. Y el mensaje de commit cuenta como expediente: lo que afirma
  se mide igual que lo que afirma el reporte.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
