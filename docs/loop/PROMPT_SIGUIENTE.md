Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V106_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 106 con EXIT 0 antes
de escribir una sola linea de trabajo. La 105 lo hizo bien y sin que
hubiera que recordarselo: se mantiene igual.

El acta de la vuelta 105 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 37405. En resumen, y sin adornarlo:

ESTA ES LA TANDA MAS LIMPIA DE JUICIO DE TODA LA CAMPANA, Y TE LO DIGO
HABIENDOLA BUSCADO POR DOS SITIOS. Lei a ciegas los SIETE discutibles que
marcaste (instrumento propio, docs/loop/_auditor_v105_ciega.py, los cuatro
nodos enteros de cada par sin tu direccion, sin tu razon, sin tu correccion
y sin el veredicto del re-barrido) y COINCIDO EN LOS SIETE, sin reserva: los
cinco que mueves (20, 21, 38, 66, 93) y los dos que sostienes (87, 91). Y
MIS DOS CONTRA-CASOS, los que yo mismo escribi fuertes, PERDIERON LOS DOS,
con razon: alinear dos procesos no exige ejecutar los pasos internos del
ajeno, y "medibles" no arrastra por si sola un acuerdo bilateral con cartas
compartidas sin cesar. Cediste bien donde tenias que ceder y sostuviste bien
donde tenias que sostener: SATELITE nunca fue sinonimo de que se mueva, y tu
resultado de 5 y 2 es exactamente lo que la 4.4 pedia.

Y NO ME QUEDE AHI, PORQUE TU RE-BARRIDO ENCONTRO EXACTAMENTE MIS OCHO Y NI
UNO MAS, y eso podia ser confirmacion o podia ser eco de mi lista. Asi que
volque los 33 que dejaste en OBJETO con su paso_casado leido hoy y busque la
especie del satelite yo mismo. Levante TRES candidatos: el 4, el 47 y el 77.
Y SE ME CAYERON LOS TRES al leerlos enteros. El 4, porque el titulo del hijo
es literalmente el acto del paso. El 47, porque el paso 3 del hijo ES el
acto de la madre. Y el 77, porque "en el desempeno de los proyectos" vive
DENTRO del objeto directo ("el impacto de la capacitacion en el desempeno
de..."), que es complemento del nombre y no complemento del verbo: la misma
distincion que tu aplicas, escrita en tus propios motivos, en el 4, en el 74
y en el 77. CERO satelites perdidos entre los 33. Y tu censo del paso mal
casado lo recorri con red mas ancha que la tuya, nueve formulas en vez de
una, sobre las 183 filas: los dos damos DOS, el 46 y el 147. Anado lo que tu
censo no dice y conviene que este escrito: el 147 ya tenia la direccion
anulada desde la correccion_v99, asi que su paso mal casado no toca ninguna
cifra viva.

LO DEMAS TAMBIEN LO REMEDI YO Y CALZA AL DIGITO. Censo 3.853 / 3.188 / 665,
aristas 9.190 / 9.169 / 18.359 / 9.813 con cero auto-aristas, ciclo de tres
en verde (Gate 0 OK, alcanzabilidad 100,0% con 3188/3188 y 85 semillas, 71
etiquetas, sync EXIT 0), grafo en 8.391.653 bytes y sha256
f0e3993967457ed2b7a0 identico a HEAD, motor 25/25, web 80 (80) / 1.030 y 3
skipped, tsc EXIT 0, marcador A 551 / B 72 / C 5 / D 2.760 sin huecos, y el
desfase en 1 fila de 468. Tu salida del marcador y la mia difieren en UNA
linea, el EXIT=0 que tu anades. Las nueve mediciones de apertura y cierre las
cotoje fichero a fichero: siete pares byte a byte identicos y los dos que
difieren (motor, web) solo en los segundos del cronometro. Y el sha256 que
publicas SI tiene fichero, y fui a buscarlo: SALIDA_V105_SYNC_APERTURA.txt y
_CIERRE.txt lo imprimen identico en los dos lados. El cierre de OP-E-03 lo
reconte con contador propio aplicando yo las correcciones por
campo_corregido: n=183, A 3 B 2 C 1 D 177, direccion 74 / 109 (59,6%),
invertidas 2 (16 y 114), VEINTIUNA anuladas por veintidos correcciones vivas.
La aditividad la medi con difflib: 04_ENLACES 0 borradas / +6, PENDIENTES 0
borradas / +110, OPERACIONES.jsonl 71 filas antes y despues con una sola
tocada, un solo campo y prefijo estricto, estado sin mover en las 71, y los
cinco puestos de los tramos SOLO GANAN la clave correccion_v105. Y el diff
sobre dataset/, web/ y engine/ lo corri commit a commit sobre los ocho:
VACIO en los ocho.

Y TU TAREA 1 FUNCIONA, PERO NO ME FIE DE QUE FUNCIONARA SOLO EN MI EJEMPLAR.
Mis tres mutaciones de la 104 contra tu codigo nuevo: A ROJO EXIT 1, B ROJO
EXIT 1, y la C, que era la que pasaba, ahora ROJO EXIT 1. El reporte 102
sigue VERDE EXIT 0 y tus cuatro coberturas calzan con mi corrida (102 3/17,
103 1/4, 104 2/6, 105 3/8). Despues hice TRES nuevas mias. La F es la misma
forma que la C pero con otra frase, otro fichero y otro parrafo: ROJO EXIT 1,
o sea que TU ARREGLO ES GENERAL Y NO UN PARCHE AL EJEMPLAR, que era lo que
yo queria saber. La D (cita en la oracion siguiente, pero esa oracion trae su
propia palabra de veredicto) queda VERDE, y ASI DEBE SER: es la condicion que
impide que vuelva el emparejamiento por parrafo de los seis falsos.

PERO LA E PASA, Y ESO SI ES UN AGUJERO, Y ES MIO DE ENCARGO OTRA VEZ. La E es
la cita DOS oraciones despues, sin palabra de veredicto propia en ninguna de
las dos ("...salio VERDE y no hubo nada que declarar. La corrida fue de
rutina y no llevo mas de un segundo. La evidencia esta en `...`."): misma
unidad de argumentacion, solo que con una oracion neutra en medio, y tu cerco
no la ve. Mi 1.4 dijo "la oracion siguiente" y tu implementaste exactamente
eso, lo mediste y publicaste la cobertura: el perimetro que quedo abierto lo
deje yo, esta escrito con mi nombre en el acta y va encargado abajo.

Y AHORA LO QUE SI TE COBRO, Y SON DOS COSAS CHICAS. LA PRIMERA: el hash de
HEAD de tu cabecera contradice tu propio fichero. Abres el bloque "CABECERA,
cada celda con su fichero" con (rama pasada-unica, apertura 1b76e800, HEAD
ba261321), y docs/loop/SALIDA_V105_HEAD_CIERRE.txt, que es el fichero de esa
misma cabecera, dice 275cb46c, que es donde corriste el ciclo de cierre;
ba261321 es el HEAD de tu TAREA 4.4, dos commits antes. Es CAIDA DE REPORTE
por AUDITOR.md 1.1 ("toda cifra o nombre propio que publiques se lee de la
salida del instrumento corrido EN ESTA VUELTA"), y ACUMULA por la letra
afinada del 27 ago, porque vive en una CABECERA y no en una lista de rutas ni
en prosa. La racha de reporte pasa de CERO a UNO tras tres vueltas limpias;
tres seguidas serian parada. Y lo digo entero para que no lo arrastres mas de
lo que pesa: NO MUEVE NI UN DATO, remedi las nueve mediciones y calzan todas,
y el remedio es codigo y va abajo, porque esa celda es exactamente la que el
tallador de cabecera tallaria si no estuviera roto.

LA SEGUNDA: cinco guiones largos. git diff 9cf7a06a..HEAD | grep '^+'
filtrado a U+2013 y U+2014 da cinco, los cinco U+2014, todos en las cabeceras
de docs/loop/SALIDA_V105_TAREA4_4_LECTURA_ENTERA.md. El encargo cierra, como
todos, con "Cero guiones largos y cero guiones medios", sin excepcion para
los ficheros de salida. Caida de INCUMPLIMIENTO DE ENCARGO. En la 104 esa
misma medicion daba cero. Usa dos puntos o parentesis y ya esta.

Y TU "PENDIENTE DE DOCTRINA" LO ADJUDICO YO, Y NO ES DOCTRINA NUEVA. Fui al
codigo. Tu diagnostico es correcto pero incompleto, y lo completo: el mismo
fichero lleva DOS regex distintos para el mismo marcador. lado(), linea 447,
usa \n  A\s+(\d+), que SI casa con la salida de hoy; lado_fase04(), linea
617, usa 'A': (\d+), que NO casa. Lo corri contra tu fichero de esta vuelta:
Match='\n  A 551' en el primero, None en el segundo. Eso no es un choque de
doctrina: es una GUARDA ENVEJECIDA, y el leer_opcional() la mantuvo muda
hasta que tu produjiste el fichero por primera vez, que es justo la
degradacion silenciosa que el banco 9 prohibe. La cubren por extension la
letra del fundador del 29 ago y la adjudicacion 5.4 del acta 85, que ya
convirtio el desfase de opcional a fallo declarado por este mismo motivo. NO
PARO EL BUCLE POR ESTO. Va como tarea bloqueante, y ademas por AUDITOR.md 3,
modo continuo: una guarda en rojo convoca al auditor y la verificacion sigue
siendo completa hasta que quede verde.

- TAREA 1, LOS REGISTROS DEL ACTA 105, en docs/PENDIENTES.md, seccion propia,
  con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado con
  su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (1.1) EL HASH DE HEAD EN LA CABECERA, como caida TUYA de reporte, con las
  dos cadenas literales (ba261321 en el reporte, 275cb46c en
  SALIDA_V105_HEAD_CIERRE.txt), la racha en UNO y la constancia de que no
  mueve ningun dato.
  (1.2) LOS CINCO GUIONES LARGOS, como caida TUYA de incumplimiento de
  encargo, con el fichero y la medicion.
  (1.3) EL PERIMETRO DE LAS DOS ORACIONES, como caida MIA de encargo, con mis
  mutaciones D, E y F citadas por fichero y con el perimetro que quedara
  DESPUES del arreglo escrito explicitamente (la cita en OTRO parrafo y la
  cita detras de una oracion con veredicto propio siguen invisibles POR
  DISENO, y la defensa real es la cobertura publicada cada vuelta).
  (1.4) EL TALLADOR DE CABECERA, como GUARDA ENVEJECIDA, con los dos regex y
  sus numeros de linea, y con mi adjudicacion de que no es doctrina nueva.
  (1.5) LO QUE HICISTE BIEN Y NO QUIERO QUE SE PIERDA: siete de siete a
  ciegas conmigo, mis dos contra-casos examinados y vencidos por escrito, los
  33 que barri yo mismo sin encontrar un solo satelite perdido, el censo del
  paso mal casado que aguanta una red mas ancha, la aditividad con estado sin
  mover en las 71 filas, y el sellado de apertura hecho a la primera.
  (1.6) MIS TRES FALSAS ALARMAS (4, 47 y 77), corregidas antes de publicar, y
  la razon por la que se cayeron: el 77 se cayo por la MISMA regla que
  sostuvo al 87 y al 91, o sea que tu linea es internamente consistente.
  (1.7) EL 147, con la nota de que su direccion ya estaba anulada desde la
  correccion_v99 y su paso mal casado no toca ninguna cifra viva.

- TAREA 2, BLOQUEANTE, EL TALLADOR DE CABECERA Y LA CELDA DE HEAD. Es el
  arreglo de una guarda envejecida, adjudicado arriba, y decide si la vuelta
  cierra.
  (2.1) EN lado_fase04(), los cinco regex del marcador se ponen al formato
  VIGENTE de scripts/recomputar_marcador.py, que es el que imprime desde la
  vuelta 53. El de lado() ya lo tiene bien y te sirve de ejemplar. La celda n
  no sale del fichero de marcador (que imprime la LISTA de huecos, no la
  cifra): decide de donde la lees, y escribe en el docstring por que.
  (2.2) CASO POSITIVO: correr --fase04 --vuelta 105 sobre los ficheros que ya
  estan commiteados tiene que dar VERDE y tallar las diez celdas del marcador
  con A 551 / B 72 / C 5 / D 2.760 en los dos lados. Pega la salida antes y
  despues.
  (2.3) CASO ROJO POR MUTACION, y no vale una que no muerda: copia
  SALIDA_V105_MARCADOR_CIERRE.txt cambiando A 551 por otra cifra y comprueba
  que la celda tallada CAMBIA con ella (o que la comparacion contra el
  reporte salta). Una guarda que da lo mismo con el fichero adulterado no
  esta contando.
  (2.4) LA CELDA DE HEAD SE TALLA, NO SE TECLEA. El tallador ya lee
  SALIDA_V<N>_HEAD_APERTURA.txt; que lea tambien SALIDA_V<N>_HEAD_CIERRE.txt
  y publique el HEAD del cierre desde ahi, con fallo declarado si el fichero
  falta. Ese es el remedio de la caida 1.1 y por eso va aqui y no en la
  TAREA 1.
  (2.5) Y LA CABECERA DE TU REPORTE DE ESTA VUELTA SALE DE ESTE TALLADOR. Si
  al cierre sigue en rojo, NO CIERRES LA VUELTA.

- TAREA 3, BLOQUEANTE, EL ENSANCHE A LAS ORACIONES SIGUIENTES. Es el cuarto
  tramo del mismo arreglo y lo cubre la misma letra del 29 ago que cubrio el
  griton y el agujero de la oracion.
  (3.1) LA REGLA QUE PIDO, y es la extension natural de la que ya
  implementaste: si la oracion de la palabra no trae cita, se sigue
  avanzando por las oraciones del parrafo HASTA LA PRIMERA QUE TRAIGA PALABRA
  DE VEREDICTO PROPIA, y se para ahi. Eso deja la D intacta (su oracion
  siguiente trae veredicto propio, asi que el avance se detiene antes de
  llegar a la cita) y hace saltar la E. Si eliges otro patron, escribe en el
  docstring por que, y mide.
  (3.2) EL CASO A BATIR TE LO DEJO MEDIDO Y NO HAY QUE INVENTARLO:
  docs/loop/_auditor_v105_mut_E.md, tal cual esta, DESPUES DEL ARREGLO TIENE
  QUE DAR ROJO EXIT 1. Pega la salida antes y despues.
  (3.3) Y LAS QUE NO PUEDEN MOVERSE, las cinco: _auditor_v104_mut_A.md,
  _B.md y _C.md siguen dando ROJO EXIT 1; _auditor_v105_mut_F.md sigue dando
  ROJO EXIT 1; y _auditor_v105_mut_D.md SIGUE DANDO VERDE EXIT 0, que no es
  un descuido sino la condicion que impide que vuelvan los seis falsos.
  Correlas las cinco y pegalas.
  (3.4) Y EL GRITON NO PUEDE VOLVER: el REPORTE.md de la vuelta 102
  (git show f253842b:docs/loop/REPORTE.md) TIENE QUE SEGUIR DANDO VERDE EXIT
  0. Los siete casos van en la misma corrida.
  (3.5) LA COBERTURA SE VUELVE A PUBLICAR CON EL PATRON NUEVO, sobre el 102,
  el 104, el 105 y el tuyo. Si sube, dilo con la cifra; si baja, tambien.
  (3.6) CORRELA AL CIERRE DE LA VUELTA junto con las otras guardas, despues
  de tu ultima edicion.

- TAREA 4, LA PREGUNTA DE TRES VIAS SOBRE LOS TRAMOS 3 Y 4, QUE CIERRA LA
  BOLSA ENTERA. Es la relectura al doble que dispara la caida de reporte por
  la letra afinada del 27 ago, y por quinta vez seguida no puede ir por donde
  ya se fue: ni extremos (102), ni centro (103), ni la especie del 28 (104),
  ni los 41 de los tramos 1 y 2 (105).
  (4.1) EL LOTE, contado por mi hoy y no de memoria
  (docs/loop/_auditor_v105_censo_relecturas.txt): de las 74 RESUELTA vivas,
  28 estan en los tramos 3 y 4 (19 en el 3, 9 en el 4), y 26 de esas 28 no
  tienen ni correccion ni nota de relectura. Los 19 del tramo 3 son 101, 102,
  106, 107, 108, 109, 111, 114, 116, 123, 127, 128, 129, 130, 132, 134, 145,
  mas el 147 y el 148, que ya traen correccion_v99; los 9 del tramo 4 son
  153, 154, 156, 158, 169, 177, 179, 180 y 182. RECUENTA TU EL LOTE ANTES DE
  CORRERLO y declara la cifra que te salga a ti: si difiere de la mia, la
  discrepancia se declara, no se resuelve copiando.
  (4.2) LA GUARDA DEL PASO MAL CASADO CORRE PRIMERO, la misma de tu 4.1 de la
  105, sobre los cuatro tramos. El 147 tiene que saltar por ella igual que
  salto el 46, y su salto tiene que quedar escrito.
  (4.3) DESPUES LA PREGUNTA DE TRES RESPUESTAS, la misma que ya usaste:
  OBJETO (objeto del imperativo), SATELITE (nombrado en complemento
  preposicional de origen, destino o instrumental) y NO_OBJETO (ejemplo,
  condicion o subordinada). Una linea por par con el verbo y el objeto
  citados literalmente, como en la 105, que es lo que me deja cotejarlos sin
  abrir el nodo. Y ANOTA LA DISTINCION QUE TU MISMO APLICASTE Y QUE ME TIRO
  ABAJO TRES CANDIDATOS: un complemento que vive DENTRO del objeto directo
  (complemento del nombre) no es un satelite; solo lo es el que gobierna al
  hijo desde FUERA del objeto.
  (4.4) Y LAS QUE SALGAN SATELITE VAN A LECTURA ENTERA, a ciegas, con las dos
  patas del 9.6.2 mas el 9.6.3. Y SATELITE SIGUE SIN SER SINONIMO DE QUE SE
  MUEVA: el 87 y el 91 de la vuelta pasada lo demuestran. Lo que exijo es que
  cada satelite pase por la lectura, no que se mueva. Las que se muevan van
  con correccion_v106 declarada, sin borrar el texto viejo, y RECOMPUTAS con
  scripts/loop/contar_cierre_efectivo.py en los tres sitios aditivos. Si no
  se mueve ninguna, lo dices con la cifra y ya esta: no fuerces hallazgos.
  (4.5) Y CUANDO ACABES, DILO CON LA CIFRA QUE LO CIERRA: cuantas de las
  RESUELTA vivas de OP-E-03 han pasado ya por la pregunta de tres vias. Si mi
  cuenta es buena, al terminar esta tarea son TODAS, y eso es un cierre de
  verdad y no otra muestra. Si no lo son, di cuantas faltan y donde.
  (4.6) EL LOTE ENTERO CABE BAJO EL DOBLE DEL AUSTERO. Si no cabe con sus
  guardas completas, lo unico que puedes partir es la lectura entera de la
  4.4: haz las del tramo 3 y deja las del tramo 4 para la vuelta siguiente,
  diciendolo con la cifra de lo que si hiciste.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Lo unico que va fijo
  es el sellado de la apertura, que es antes de todo, y las TAREAS 2 y 3, que
  son bloqueantes y deciden si la vuelta cierra.

- LO QUE NO SE TOCA. La deriva de contenido (26 nodos de 140, 32 pares de 87,
  acta 92 seccion 4.4), los siete nodos con guion, el bloque repetido de
  formalizar_un_proceso_ad_hoc y los titulos gemelos por mayuscula
  (sistema_responsabilidad_gerencial y su _2) siguen ANOTADOS PARA ALEXIS Y
  SIN ENCARGAR, porque rozan el ALCANCE de la campana. Y sigue constando que
  Gate 0 tiene razon al dar 0 en duplicadas: su guarda dice "titulo_concepto
  EXACTO duplicado" y esos dos titulos no son exactos.

- LO QUE NO SE ABRE. No se toca el campo estado, que sigue sin voto por el
  acta 100 seccion 4.2 (lo volvi a medir hoy: LISTA 70, HECHA 1, y en la fase
  04 una HECHA y seis LISTAS). No se abre la fase 05 ni la 06. No se mueve
  ninguna operacion de fase. No se escribe ni se retira una sola arista: la
  TAREA 4 es juicio y registro, no cirugia, igual que OP-E-03.

- LA NOTA DE HIGIENE DE SIEMPRE, y sigue midiendose igual: git status trae M
  en dataset/metadata/master_graph.json desde antes de que nadie toque nada, y
  NO es un cambio (8.391.653 bytes y sha256 f0e3993967457ed2b7a0, identico a
  HEAD; lo volvi a medir hoy, despues de correr el ciclo entero). No lo
  commitees y no lo "arregles". Y si corres SOLO run_phase1.py el fichero
  cambia de tamano y parece que has movido algo: es el CICLO DE TRES ENTERO el
  que lo devuelve identico byte a byte.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
