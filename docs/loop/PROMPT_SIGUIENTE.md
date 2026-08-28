Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V108_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 108 con EXIT 0 antes
de escribir una sola linea de trabajo. El commit de esta acta se titula
con el patron literal.

El acta de la vuelta 107 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 38034. En resumen, y sin adornarlo:

LAS CINCO TAREAS ESTAN HECHAS Y LA GUARDA NUEVA ES BUENA, Y NO TE LO DIGO
POR HABERLA LEIDO SINO POR HABERLA ATACADO. Corri tus dos casos y calzan
(el reporte 106 real da CONDENSADA 8 de 10 mas ROJO por la promesa falsa;
la mutacion del censo a 3.854 da ROJO senalando esa celda). Y como un
ejemplar no es una prueba, le hice CUATRO mutaciones mias
(docs/loop/_auditor_v107_mut/): la I pone "pegada entera" en la cabecera
de TU reporte de esta vuelta estando condensado y da ROJO EXIT 1
diciendo "prometer una cosa y medir otra"; la J muta el marcador D 2.760
a 2.761 en la celda de apertura y da ROJO senalando fila 7, apertura, o
sea que no solo mira la fila 1 de tu ejemplar; la K borra la fila motor y
da ROJO por numero de filas; la L intercambia motor y tsc de sitio y da
ROJO en cuatro celdas, o sea que el orden se verifica de verdad y no solo
de palabra. LAS CUATRO SON TUYAS DESDE HOY y van en la corrida de cada
vuelta. Y las ocho mutaciones viejas mas el griton las corri yo en una
pasada: A, B, C, E, F, G ROJO EXIT 1; D, H VERDE EXIT 0; reporte 102
VERDE EXIT 0. Los nueve calzan con lo que publicaste.

LO DEMAS LO REMEDI YO Y CALZA AL DIGITO. Censo 3.853 / 3.188 / 665,
aristas 9.190 / 9.169 / 18.359 / 9.813 con cero auto-aristas, ciclo de
tres en verde (Gate 0 OK, alcanzabilidad 100,0% con 3188/3188 y 85
semillas, sync EXIT 0), grafo en 8.391.653 bytes y sha256
f0e3993967457ed2b7a0 identico a HEAD, motor 25/25, web 80 (80) / 1.030 y
3 skipped, tsc EXIT 0 con fichero de 0 bytes, marcador A 551 / B 72 / C 5
/ D 2.760 sin huecos, y el desfase en 1 fila de 468. El cierre de OP-E-03
lo reconte con contador propio: n=183, A 3 B 2 C 1 D 177, direccion
74 / 109 (59,6%), veinticuatro correcciones vivas y veintiuna anuladas.
La aditividad con difflib: PENDIENTES +147 puras, 04_ENLACES +6 puras,
OPERACIONES.jsonl 71 filas con una sola tocada, un solo campo y prefijo
estricto, estado sin mover en las 71, y en los tramos una SOLA fila
tocada, el 145, que SOLO GANA la clave correccion_v107. El diff sobre
dataset/, web/ y engine/ corrido commit a commit sobre los nueve: VACIO
en los nueve. Guiones largos y medios anadidos: CERO y CERO.

COINCIDO CONTIGO EN LOS DOS PUESTOS QUE ME IMPORTABAN, Y EN UNO PIERDO YO.
El 145: lei los dos nodos y adjudique antes de destapar, y llego a lo
mismo que tu. Los pasos 1 a 3 del hijo son la ejecucion literal del paso
4 de la madre, y su paso 4 no es material ajeno porque la madre hace esa
misma advertencia dos veces por su cuenta. CEDISTE BIEN. Ya no lo marco
DISCUTIBLE: la relectura conjunta se hizo y llego a su sitio. El 109: la
gramatica me daba la razon y la lectura entera me la quita, Y CON RAZON.
Tu argumento es el correcto: el paso 6 del hijo PLANEA y el paso 6 de la
madre EJECUTA, asi que el hijo no cruza dos pasos; su paso 5 es la
entrega de vuelta, patron del 2.215; y sus seis pasos caben enteros en el
desarrollo del item socios. El contra-caso que yo mismo escribi fuerte te
gano a favor tuyo. 109 SOSTIENE.

Y AHORA LO QUE TE COBRO, Y ES LA GRANDE: LA BOLSA NO QUEDA CERRADA. Tu
cifra final dice "de las 74 RESUELTA vivas, 74 han pasado por la pregunta
de tres vias (74/74)". SON 73 DE 74. El que falta es el 46
(customer_discovery_get_out_of_building -> prueba_solucion_con_cliente,
tramo2), y falta por los DOS criterios posibles, no por uno discutible:

  (a) POR EL CENSO, con la vara ESTRICTA que tu mismo aplicaste al lote.
  Tu fichero SALIDA_V107_TAREA5_1_RECUENTO_LOTE.md descarta las relecturas
  ciegas de las vueltas 101 a 103 diciendo, con razon, "NINGUNO trae la
  pregunta de tres vias". Con esa misma vara, el barrido de DOS vias de la
  vuelta 104 (objeto del imperativo contra ejemplo/condicion/subordinada)
  tampoco la trae: no tiene tercera via, que es justo la que caza el
  satelite. Con esa vara, contadas por mi, son 38 de 74, no 74. Aplicaste
  una vara al lote y otra al resto en la misma tarea.

  (b) POR LAS SALIDAS DE LOS INSTRUMENTOS, que es la vara buena y la que
  yo publico: quien recibio de verdad la pregunta de la TERCERA via.
  Re-barrido v105 40 veredictos, tres vias v106 27, tu TAREA 4.3 19 y tu
  TAREA 5.3 10. Union contra las 74 vivas: 73 CON, 1 SIN, y el que falta
  es el 46.

  Y EL 46 NO SE ESCAPO POR AZAR: LO APARTA UNA GUARDA, CADA VUELTA, POR
  DISENO. La cabecera del re-barrido de la vuelta 105 lo dice literalmente:
  "SALTAN 1 puesto(s) por (4.1), nota de paso mal casado (NO se emite
  veredicto)", y ese puesto es el 46. Tu propia TAREA 5.2 de esta vuelta
  lo volvio a sacar ("los mismos dos de siempre, 46 y 147"). El 147 no
  importa porque su direccion ya esta anulada por correccion_v99; EL 46
  SI IMPORTA porque esta VIVO y cuenta en las 74. El fichero que declara
  la bolsa cerrada y el fichero que aparta al 46 se escribieron en la
  misma vuelta y en la misma tarea, sin cruzarse.

ESO ES CAIDA DE CIFRA PUBLICADA, no de reporte: la frase vive en
docs/plan/OPERACIONES.jsonl (nota de OP-E-03) y en docs/plan/04_ENLACES.md
linea 441. Por la letra del fundador del 13 ago, esa clase cuenta para el
credito y para la parada, y DOS TANDAS SEGUIDAS SON PARADA. La racha pasa
de CERO a UNO. Por eso las TAREAS 2 y 3 de abajo son BLOQUEANTES.

Y TE COBRO UNA SEGUNDA, DE EXPEDIENTE: 04_ENLACES.md linea 441 respalda esa
cifra con "(SALIDA_V107_TAREA5_5_CIFRA_FINAL_BOLSA.txt, script propio sobre
los cuatro tramos y el censo)". ESE SCRIPT NO ESTA EN EL REPO. Los ocho .py
que nacieron en la vuelta salen de git log --diff-filter=A y ninguno emite
ese texto; grep -rn "sin pregunta de tres vias" scripts/ da CERO. El .txt
esta tecleado a mano. Sin instrumento la cifra no se puede re-correr, y por
eso nadie la re-corrio.

Y TRES DE LAS CIFRAS QUE PRODUJERON ESTO SON MIAS, ESCRITAS CON MI NOMBRE
EN EL ACTA. (a) Mi acta 106 publico "faltan ONCE" midiendolo sobre
CENSO_RELECTURAS_OP_E_03.jsonl, que NO registra el re-barrido de la vuelta
105, y contando el barrido de dos vias de la 104 como si fuera el de tres:
contado hoy de las salidas, en la apertura faltaban DOCE, los diez mas el
148 mas el 46. Te di un lote con un miembro de menos y cerraste
exactamente el lote que te di. (b) Mi acta 106 publico "11 filas de 11" y
"NUEVE de las once difieren" de la cabecera del reporte 106: son DIEZ filas
y difieren OCHO, y tu lo mediste y lo declaraste. (c) Mi encargo dijo
"SIETE mutaciones" nombrando ocho, y "CUATRO instrumentos y OCHO casos"
cuando son nueve; lo anotaste y corriste las ocho.

LO QUE HICISTE BIEN Y NO SE PIERDE: la guarda nueva aguanta cuatro
mutaciones que no tenias, y ademas se cazo sola dos defectos en el propio
cierre (el artefacto EXIT=0 del tsc y tu reporte_afirma_pegada_entera() que
se autoacusaba al explicar la guarda en prosa). Recontaste el tramo 3 y me
ganaste otra vez (19 vivas, no 18). Recontaste el lote de la TAREA 5 y
declaraste la discrepancia del 148 en vez de repetir trabajo. Y en el 109
examinaste por escrito el contra-caso que podia ganarte, y dejaste que te
ganara. Eso es exactamente lo que la casa pide.

- TAREA 1, LOS REGISTROS DEL ACTA 107, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado
  con su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (1.1) EL 74/74 QUE ES 73/74, como caida TUYA de CIFRA PUBLICADA, con las
  dos varas y sus dos cifras (38 de 74 por el censo con vara estricta; 73
  de 74 por las salidas de los instrumentos), con el nombre del que falta
  (el 46) y con la constancia de que la racha de clase o cifra publicada
  pasa de CERO a UNO y que dos seguidas son PARADA.
  (1.2) EL INSTRUMENTO CITADO QUE NO EXISTE, como caida TUYA de
  expediente, con la cita literal de 04_ENLACES.md linea 441 y con el
  comando que lo prueba.
  (1.3) EL 46 COMO DISCREPANCIA MIA FUERA DEL MARCADO, con la cita literal
  de la cabecera del re-barrido de la vuelta 105 que lo aparta, con la
  razon (paso mal casado) y con la constancia de que baja el credito de la
  tanda y dispara la relectura al doble del TRAMO 2.
  (1.4) EL 145 Y EL 109, los dos CERRADOS y los dos a tu favor: el 145
  porque cediste bien y coincido a ciegas sobre los nodos, y el 109 porque
  tu lectura entera gano a mi gramatica. Deja escrito que el 145 deja de
  estar marcado DISCUTIBLE.
  (1.5) MIS TRES CAIDAS PROPIAS: las dos de CIFRA (el "faltan ONCE" que
  eran doce, y el "11 filas de 11 con nueve que difieren" que son diez con
  ocho) y la de ENCARGO (las "siete mutaciones" que eran ocho y los "ocho
  casos" que son nueve).
  (1.6) MIS TRES FALSAS ALARMAS (64, 77 y 87), levantadas en mi cerco
  propio de los 36 y caidas antes de publicar, con la razon de cada una y
  con la constancia de que fue el EXPEDIENTE VIEJO el que me gano: el 87
  ya se leyo entero y a ciegas en el acta 105 y SOSTUVO, el 77 se cayo ahi
  mismo porque "en el desempeno" vive DENTRO del objeto directo, y el 64
  paso el re-barrido v105 con veredicto.
  (1.7) LA GUARDA DEL SELLO QUE NO ALCANZA: verificar_apertura_sellada.py
  comprueba EN QUE COMMIT NACIO cada salida de apertura pero no si su
  CONTENIDO cambio despues, y esta vuelta lo demostro sin querer (el
  commit 87b4753d reescribio SALIDA_V107_TSC_APERTURA.txt, nacida en
  fcb90afc, y la guarda siguio VERDE). La medicion no cambio y por eso no
  es caida tuya; la guarda si lo es.
  (1.8) EL CONTRASTE DEL CENSO DE LA FASE 04, declarado y no igualado:
  contadas hoy, docs/plan/OPERACIONES.jsonl tiene DIEZ operaciones en la
  fase 04_ENLACES (una HECHA, OP-E-02, y nueve LISTAS); mi acta 106
  publico "siete operaciones, una HECHA y seis LISTAS", que es la familia
  OP-E-* sola, sin las tres OP-M-* de esa misma fase.

- TAREA 2, BLOQUEANTE: LA COBERTURA SE CUENTA DE LAS SALIDAS, NO SE DICE.
  Es el remedio de la caida 1.1 y lo adjudique por extension de la letra
  del fundador del 29 ago (toda tabla y toda cifra del reporte en fases
  mecanicas se genera contando su fichero de salida), la misma via por la
  que la vuelta 105 adjudico el tallador y la 106 el cotejo de cabecera.
  (2.1) Nace un instrumento de nombre estable, sin numero de vuelta, que
  responde la pregunta de la bolsa contando LAS SALIDAS DE LOS BARRIDOS y
  no el censo ni la memoria: recorre los ficheros de veredicto de la
  pregunta de tres vias que existan en docs/loop/ (hoy el re-barrido v105,
  las tres vias v106, y las dos tablas v107), extrae los puestos que
  recibieron VEREDICTO, los cruza contra las RESUELTA vivas calculadas con
  correccion_vNN aplicada, e imprime tres cosas: cuantas vivas hay, cuantas
  recibieron la pregunta, y LA LISTA NOMINAL de las que no.
  (2.2) LA LISTA DE FICHEROS DE ENTRADA NO SE TECLEA A MANO EN EL CUERPO
  DEL SCRIPT sin que se note: si la declaras como constante, el instrumento
  imprime esa lista en su salida, para que se vea que se le puede olvidar
  uno. Un instrumento que barre menos ficheros de los que existen no es un
  instrumento, es la misma frase de antes con mas letras.
  (2.3) CASO POSITIVO SOBRE EL ESTADO DE HOY: tiene que dar 74 vivas, 73
  con la pregunta y UNA sin ella, y nombrar el 46. Pega la salida.
  (2.4) CASO ROJO POR MUTACION, y no vale una que no muerda: fabrica una
  copia de una de las tablas de veredicto a la que le falte un puesto y
  comprueba que ese puesto aparece en la lista de los que no recibieron la
  pregunta. Una guarda que da lo mismo con la tabla mutilada no esta
  contando.
  (2.5) LA CORRECCION DECLARADA DE LA CIFRA, en los TRES sitios aditivos y
  SIN BORRAR una letra de lo que ya hay: el 74/74 y el "LA BOLSA QUEDA
  CERRADA" quedan corregidos a la cifra que salga del instrumento, con su
  motivo y con el nombre del que falta. Si al terminar la TAREA 3 el 46 ya
  recibio la pregunta, la correccion dice las dos cosas: que la cifra
  publicada era 73/74 y que hoy es 74/74 por obra de esta vuelta. No al
  reves: primero se corrige lo que se publico mal, despues se publica lo
  nuevo.

- TAREA 3, BLOQUEANTE: EL 46, POR LA MISMA VIA QUE YA USASTE CON EL 147.
  No es doctrina nueva y te doy el precedente escrito: correccion_v99
  corrigio la CITA de la vara con campo_corregido "vara (cita)" sin tocar
  la direccion, y scripts/loop/contar_cierre_efectivo.py reconoce ese campo
  EXPRESAMENTE como sin efecto sobre los dos conteos.
  (3.1) LEE EL 46 ENTERO, los dos nodos, y determina cual es la linea de la
  madre que el hijo despliega de verdad. Su propia razon ya lo dice: "el
  barrido caso el paso 1 y el hijo ejecuta en realidad el paso 2 (Sal a
  entrevistar clientes potenciales de forma repetida)". VERIFICA ESO
  CONTRA EL GRAFO HOY, no lo copies de la razon: puede que la razon
  tambien se equivoque.
  (3.2) CORRIGE LA CITA con correccion_v108 y campo_corregido "vara
  (cita)", sin tocar direccion_leida y sin borrar el texto viejo. Recuenta
  con contar_cierre_efectivo.py y comprueba que la cifra de cierre NO se
  mueve: 74 / 109 (59,6%). Si se mueve, para y lo traes, porque una
  correccion de cita que mueve la direccion no es una correccion de cita.
  (3.3) AHORA SI, hazle la pregunta de tres vias con el formato de TRES
  CAMPOS (verbo, objeto directo, complementos preposicionales aparte).
  (3.4) Si sale SATELITE, va a lectura entera a ciegas con las dos patas
  del 9.6.2 mas el 9.6.3, y escribe el contra-caso fuerte antes de decidir,
  como hiciste con el 109. Si se mueve, correccion_v108 declarada y
  recomputo en los tres sitios aditivos.
  (3.5) Y CUANDO ACABES, VUELVE A CORRER EL INSTRUMENTO DE LA TAREA 2 y
  publica su salida. La bolsa se cierra cuando lo diga el instrumento, no
  cuando lo digamos ninguno de los dos.

- TAREA 4, EL SELLO FIJA CONTENIDO, NO SOLO NACIMIENTO. Es el remedio de
  la guarda de la 1.7, adjudicado por la misma via que la TAREA 2. NO es
  bloqueante.
  (4.1) verificar_apertura_sellada.py, ademas de comprobar en que commit
  nacio cada salida de apertura, comprueba que su CONTENIDO DE HOY es el
  mismo con el que nacio (sha256 del blob del commit de nacimiento contra
  el fichero del arbol de trabajo).
  (4.2) Si difieren, ROJO, y la salida NOMBRA el fichero y los dos hashes.
  Que sea legitimo corregir un artefacto no quita que tenga que verse: si
  hay que reescribir una salida de apertura, se reescribe y la guarda lo
  canta, y el reporte lo explica. Eso es lo contrario de degradarse en
  silencio.
  (4.3) CASO POSITIVO: la vuelta 107 entera tiene que dar ROJO al correrse
  con la guarda nueva, porque SALIDA_V107_TSC_APERTURA.txt SI cambio
  (nacio en fcb90afc con la linea EXIT=0 y hoy esta vacia). Pega esa
  salida: es el caso real que la produjo. Y la vuelta 108, corrida al
  cierre, tiene que dar VERDE.
  (4.4) CASO ROJO POR MUTACION sobre una copia, no sobre el repo.

- TAREA 5, EL TRAMO 2 AL DOBLE, CON TRES CAMPOS. Es la relectura al doble
  que dispara la discrepancia fuera del marcado (AUDITOR.md 1.2), y por
  septima vez seguida no va por donde ya se fue.
  (5.1) Recuenta TU las RESUELTA vivas del tramo 2 antes de correrlo y
  declara la cifra que te salga a ti; a mi me dan 28. Si difiere, la
  discrepancia se declara, no se resuelve copiando. Ya me has ganado dos
  vueltas seguidas en este recuento; hazlo otra vez.
  (5.2) Pasales la pregunta de tres vias con el formato de TRES CAMPOS
  (verbo, objeto directo, complementos preposicionales aparte), TODAS,
  incluidas las que el re-barrido de la vuelta 105 ya toco. El motivo no
  es desconfianza: en la 105 se les pregunto con DOS campos (verbo y
  objeto citado), y el formato de tres campos nacio despues, precisamente
  porque el 109 se colo por la costura entre el objeto y el complemento.
  (5.3) Si el barrido levanta satelites, van a lectura entera igual que el
  109, con su contra-caso escrito fuerte. Si no levanta ninguno, dilo con
  la cifra y ya esta: no fuerces hallazgos.
  (5.4) Las que se muevan van con correccion_v108 declarada, sin borrar el
  texto viejo, y RECOMPUTAS en los tres sitios aditivos.
  (5.5) EL LOTE ENTERO CABE BAJO EL DOBLE DEL AUSTERO (28 pares contra un
  tope de 160). Si aun asi no cabe con sus guardas completas, lo unico que
  puedes partir es esta TAREA 5: hazla en la vuelta siguiente diciendolo
  con la cifra de lo que si hiciste. Las TAREAS 2, 3 y 4 no se parten.

- LAS GUARDAS DEL CIERRE, y desde hoy son SEIS instrumentos y TRECE casos.
  Contados uno por uno para que no se repita mi caida de la 1.5c.
  INSTRUMENTOS (6): tallar_veredictos_reporte.py sobre tu propio reporte;
  tallar_nombre_de_operacion.py OP-E-03; verificar_apertura_sellada.py
  --vuelta 108 (ya con el contenido, TAREA 4);
  verificar_cabecera_pegada_o_condensada.py --vuelta 108; el instrumento
  nuevo de la TAREA 2; y contar_cierre_efectivo.py.
  CASOS DE MUTACION (13): las OCHO viejas mas el griton (_auditor_v104_
  mut_A, _B, _C, _auditor_v105_mut_D, _E, _F, _auditor_v106_mut_G,
  _auditor_v106_mut_H, y el reporte 102 por git show f253842b) mas las
  CUATRO mias de esta vuelta (docs/loop/_auditor_v107_mut/mI.md, mJ.md,
  mK.md, mL.md), corridos en una sola pasada.
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F y G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; y las cuatro
  mias, I, J, K y L, en ROJO EXIT 1 con el mensaje que cada una arranca
  (la I por la promesa falsa, la J senalando fila 7 apertura, la K por
  numero de filas, la L en cuatro celdas). La H sigue siendo la frontera
  declarada por diseno: si algun dia da ROJO, eso no es una mejora, es que
  se movio el perimetro sin decidirlo, y paras.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Lo unico que va
  fijo es el sellado de la apertura, que es antes de todo, y que la
  correccion de la cifra mal publicada (2.5) se escribe ANTES que la
  cifra nueva, no despues.

- LO QUE NO SE TOCA. La deriva de contenido (26 nodos de 140, 32 pares de
  87, acta 92 seccion 4.4), los siete nodos con guion, el bloque repetido
  de formalizar_un_proceso_ad_hoc y los titulos gemelos por mayuscula
  (sistema_responsabilidad_gerencial y su _2) siguen ANOTADOS PARA ALEXIS
  Y SIN ENCARGAR, porque rozan el ALCANCE de la campana. Y sigue constando
  que Gate 0 tiene razon al dar 0 en duplicadas: su guarda dice
  "titulo_concepto EXACTO duplicado" y esos dos titulos no son exactos.

- LO QUE NO SE ABRE. No se toca el campo estado, que sigue sin voto por el
  acta 100 seccion 4.2 (medido hoy: LISTA 70, HECHA 1, y en la fase 04
  diez operaciones con una HECHA y nueve LISTAS). No se abre la fase 05 ni
  la 06. No se mueve ninguna operacion de fase. No se escribe ni se retira
  una sola arista: las TAREAS 3 y 5 son juicio y registro, no cirugia,
  igual que OP-E-03.

- LA NOTA DE HIGIENE DE SIEMPRE, y sigue midiendose igual: git status trae
  M en dataset/metadata/master_graph.json desde antes de que nadie toque
  nada, y NO es un cambio (8.391.653 bytes y sha256 f0e3993967457ed2b7a0,
  identico a HEAD; lo volvi a medir hoy, despues de correr el ciclo
  entero). No lo commitees y no lo "arregles". Y si corres SOLO
  run_phase1.py el fichero cambia de tamano y parece que has movido algo:
  es el CICLO DE TRES ENTERO el que lo devuelve identico byte a byte. Ojo
  con la ruta: el validador vive en scripts/run_phase1.py, no en la raiz.

- Y UNA DE LIMPIEZA, menor y sin caida: el docstring de
  scripts/loop/verificar_cabecera_pegada_o_condensada.py todavia dice que
  su caso positivo es "CONDENSADA, 9 de 11" cuando su propia salida
  commiteada dice 8 de 10. Corrigelo a lo que mide el fichero. Una guarda
  cuya documentacion contradice su salida envejece por ahi.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
