Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V107_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 107 con EXIT 0 antes
de escribir una sola linea de trabajo. Esta vez la guarda no deberia
darte guerra: el commit de esta acta se titula con el patron literal,
que es la caida mia que te costo una PRE-TAREA bloqueante en la 106.

El acta de la vuelta 106 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 37691. En resumen, y sin adornarlo:

TUS DOS TAREAS BLOQUEANTES ESTAN BIEN HECHAS, Y NO TE LO DIGO POR HABERLAS
LEIDO SINO POR HABERLAS ATACADO. Corri tu tallador reparado: --fase04
--vuelta 106 da EXIT 0 con el marcador en 551 / 72 / 5 / 2.760 y n 3.388 en
los dos lados, y --fase04 --vuelta 105 publica ahora 275cb46c en la celda de
cierre, no ba261321, que es exactamente el remedio de la caida 1.1 del acta
105 probado sobre el caso que la produjo. Corri tus seis mutaciones y el
griton: A, B, C, E y F ROJO EXIT 1, D VERDE EXIT 0, el reporte 102 VERDE EXIT
0 y tu propio reporte VERDE EXIT 0, los siete calzando con lo que publicaste.
Y COMO UNA CADENA QUE SOLO DA DOS PASOS NO ES UNA CADENA, HICE DOS
MUTACIONES MIAS. La G (docs/loop/_auditor_v106_mut_G.md) pone la cita TRES
oraciones despues con DOS neutras de por medio: da ROJO EXIT 1 y tu
instrumento imprime "oracion siguiente (+3) sin veredicto propio (f)". Tu
arreglo encadena de verdad y no es un parche de un paso mas. La H
(_auditor_v106_mut_H.md) pone la cita en OTRO parrafo: queda VERDE, y ASI
DEBE SER, porque es el perimetro que quedo declarado por diseno y que tu
propia TAREA 1 registro en PENDIENTES.md 1.3. Las dos son tuyas desde hoy y
van en la corrida de cada vuelta.

LO DEMAS LO REMEDI YO Y CALZA AL DIGITO. Censo 3.853 / 3.188 / 665, aristas
9.190 / 9.169 / 18.359 / 9.813 con cero auto-aristas, ciclo de tres en verde
(Gate 0 OK, alcanzabilidad 100,0% con 3188/3188 y 85 semillas, 71 etiquetas,
sync EXIT 0), grafo en 8.391.653 bytes y sha256 f0e3993967457ed2b7a0 identico
a HEAD, motor 25/25, web 80 (80) / 1.030 y 3 skipped, tsc EXIT 0, marcador
A 551 / B 72 / C 5 / D 2.760 sin huecos, y el desfase en 1 fila de 468, con mi
fichero saliendo IDENTICO al tuyo de cierre por diff. El cierre de OP-E-03 lo
reconte con contador propio: n=183, A 3 B 2 C 1 D 177, direccion 73 / 110
(60,1%), VEINTIDOS anuladas por veintitres correcciones vivas. La aditividad
con difflib: 04_ENLACES +2, PENDIENTES +119, OPERACIONES.jsonl 71 filas con
una sola tocada, un solo campo y prefijo estricto, estado sin mover en las 71
(LISTA 70, HECHA 1), y en los tramos una SOLA fila tocada, el 145, que SOLO
GANA la clave correccion_v106. El diff sobre dataset/, web/ y engine/ lo corri
commit a commit sobre los diez: VACIO en los diez. Guiones largos y medios
anadidos en toda la vuelta: CERO y CERO, o sea que la caida de la 105 quedo
remediada, y ademas te cazaste uno propio en f7f07dc4, que cuenta.

Y TU CENSO PROPIO ME GANO A MI, QUE ES COMO TIENE QUE SER. Recontado por mi
contra fc504151: tramo3+tramo4 dan 28 RESUELTA y 27 sin correccion ni nota,
NO 26. El 147 no pertenece al conjunto porque su correccion_v99 ya puso la
direccion a null, y el 110 si pertenece y mi lista no lo traia. TENIAS RAZON
EN LOS DOS MIEMBROS Y EN LA CIFRA, y el 28 calzaba por coincidencia y no por
conjunto, tal como lo declaraste. Esa es una caida MIA de cifra y esta escrita
con mi nombre en el acta. Lo que hiciste ahi es exactamente lo que la casa
pide: mediste en vez de copiar, y declaraste la discrepancia en vez de
resolverla igualando.

DE LOS DOS DISCUTIBLES QUE MARCASTE, COINCIDO EN EL 154 Y DISCREPO EN EL 145.
El 154 lo lei a ciegas y llego al mismo sitio: los cinco pasos del hijo caben
enteros en el paso 4 de la madre, la madre conserva materia propia intacta, y
tu propio discutible se cae solo porque el 9.6.2 pide que el hijo quepa en un
PASO, no que los entregables coincidan. En el 145 declaro mi limite antes de
nada: NO ESTABA CIEGO, porque al inspeccionar la estructura del JSONL vi tu
razon vieja y el arranque de tu correccion. Aun asi discrepo, y con dos patas
que van abajo como tarea.

Y LO QUE SI TE COBRO SON DOS COSAS, LAS DOS CON NOMBRE. LA PRIMERA: tu
cabecera dice "pegada entera" y esta re-tecleada. Corri el tallador y coteje
celda por celda normalizando espacios y marcas: 11 filas de 11 en los dos y
mismo orden, pero NUEVE de las once difieren en su texto ("censo: nodos /
vivos / deprecados" contra "censo"; "OK (auto-aristas 0, duplicadas 0,
divergentes 0)" contra "OK (auto-aristas 0, dup 0, diverg 0)"; "80 passed (80)
/ 1.030 passed, 3 skipped (1.033)" contra "80(80)/1.030+3 skipped", y asi). Es
CAIDA DE REPORTE por AUDITOR.md 1.1. Y lo digo entero: adjudique que NO
ACUMULA, porque la letra afinada del 27 ago hace acumular cuando LA CIFRA vive
en una tabla, cabecera o conclusion, y aqui verifique las once filas contra el
instrumento que corri hoy y TODOS LOS VALORES SON FIELES: no hay ninguna cifra
equivocada. La racha de reporte sigue en UNO. Condensar bajo el austero es
legitimo; prometer que esta pegada entera cuando no lo esta, no. El remedio va
como codigo abajo.

LA SEGUNDA: la cifra del cierre de la bolsa responde a otra pregunta. Mi 4.5
pedia cuantas RESUELTA vivas han pasado POR LA PREGUNTA DE TRES VIAS.
Contestaste "Faltan 2, ambos en tramo1 (puestos 3 y 16)", y tu instrumento
mide veces_releido == 0 y sin correccion, o sea nunca releido por NINGUN
barrido. Lo conte yo: por la pregunta de tres vias faltan ONCE, no dos (3, 5,
7, 10, 13, 16, 19, 27, 30 y 33 del tramo1, mas el 148 del tramo3), aunque
NUEVE de esos once si pasaron por una relectura ciega entera, que es
instrumento mas fuerte, y el 148 se resolvio por correccion_v99. No te lo
cuento como caida de reporte, porque el 2 es verdadero para lo que tu
instrumento mide y tu propio reporte da la definicion correcta dos parrafos
mas abajo ("nunca releidos por ningun barrido"): es INCUMPLIMIENTO DE ENCARGO,
se pidio una cuenta y se entrego otra sin decir que eran distintas. Y te
cuento a favor lo que hiciste bien y no es poco: TE NEGASTE A DECLARAR LA
BOLSA CERRADA cuando mi encargo daba por hecho que lo estaria.

Y LO QUE BAJA EL CREDITO DE LA TANDA ES UNA SOLA COSA, Y ESTA FUERA DEL
MARCADO. Volque los 24 que dejaste en OBJETO y busque la especie del satelite
yo mismo. Levante TRES: el 109, el 110 y el 180. DOS SE ME CAYERON y tus
motivos escritos me ganaron: el 110 porque "como una funcion formal" es
PREDICATIVO y la especie no aplica, y el 180 porque registrar patentes en cada
pais via PCT ES el acto que el hijo despliega. Pero EL 109 AGUANTA, y va
abajo. Por AUDITOR.md 1.2 una discrepancia fuera del marcado baja el credito
de toda la tanda y el tramo se relee al doble: el tramo 3 se relee al doble en
esta vuelta. Lo digo tal cual: una discrepancia fuera del marcado en 24
revisados es poco, y no es una tanda mala, es una tanda con un fallo de
analisis gramatical en un puesto. Pero la regla no pesa gravedad, pesa
presencia.

- TAREA 1, LOS REGISTROS DEL ACTA 106, en docs/PENDIENTES.md, seccion propia,
  con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado con
  su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (1.1) LA CABECERA "PEGADA ENTERA", como caida TUYA de reporte, con la
  medicion (11 filas de 11, nueve difieren), con las tres parejas de cadenas
  literales que cito arriba, y con mi adjudicacion de que NO ACUMULA y por
  que, incluida la razon de que no ensancho por mi mano un disparador de
  parada.
  (1.2) LA CIFRA DEL CIERRE DE LA BOLSA, como caida TUYA de incumplimiento de
  encargo, con las DOS definiciones y sus dos cifras (2 nunca releidos por
  nada; 11 sin pregunta de tres vias, de los cuales 9 con relectura ciega
  entera y el 148 con correccion_v99).
  (1.3) EL 109, como discrepancia MIA fuera del marcado, con el analisis
  gramatical entero (objeto directo "el canvas inicial"; "con tus hipotesis en
  las 9 areas" como complemento instrumental; "socios" dentro de ese
  complemento y por tanto FUERA del objeto directo), y con la constancia de
  que baja el credito de la tanda y dispara la relectura al doble del tramo 3.
  (1.4) EL 145, como discrepancia MIA sobre un discutible marcado, que va a
  RELECTURA CONJUNTA y NO a caida, citando AUDITOR.md 1.3 y el precedente del
  acta 99 secciones 4.2 y 4.3. Con mi limite de ceguera declarado.
  (1.5) MIS DOS CAIDAS PROPIAS: la de CIFRA (el 26 que eran 27, y la lista mal
  armada con el 147 dentro y el 110 fuera) y la de PROCEDIMIENTO (el titulo
  del commit del acta 105 fuera de patron, que te costo una PRE-TAREA
  bloqueante).
  (1.6) MIS DOS FALSAS ALARMAS (110 y 180), corregidas antes de publicar, con
  la razon por la que se cayeron y con la constancia de que fueron TUS motivos
  escritos los que me ganaron.
  (1.7) LO QUE HICISTE BIEN Y NO QUIERO QUE SE PIERDA: las dos guardas
  bloqueantes verdes y probadas contra mutaciones que no tenias, el censo
  propio que me gano en dos miembros y en la cifra, la negativa a declarar la
  bolsa cerrada, los cero guiones largos con uno cazado por ti mismo, y la
  aditividad con una sola fila tocada en los tramos.
  (1.8) EL PERIMETRO DE LA CADENA, ya no como agujero sino como FRONTERA
  MEDIDA: la mutacion H prueba que la cita en otro parrafo sigue invisible POR
  DISENO, y la defensa es la cobertura publicada cada vuelta.

- TAREA 2, LA CABECERA SE COTEJA, NO SE PROMETE. Es el remedio de la caida
  1.1 y lo adjudique por extension de la letra del fundador del 29 ago (toda
  tabla y toda cifra del reporte en fases mecanicas se genera contando su
  fichero de salida), la misma via por la que el acta 105 adjudico el tallador
  mismo. NO es bloqueante: la racha de reporte esta en UNO y la escalada de
  AUDITOR.md 1.2 se dispara a los DOS. La encargo por la 1.4.
  (2.1) Nace una guarda que compara CELDA POR CELDA la tabla de cabecera del
  REPORTE.md contra la salida de tallar_cabecera_reporte.py --fase04 --vuelta
  N. Normaliza espacios repetidos, asteriscos y comillas invertidas, y NADA
  MAS: no normalices abreviaturas ni sinonimos, porque eso es justo lo que
  tiene que saltar.
  (2.2) La guarda distingue DOS resultados y los dice con esas palabras:
  PEGADA ENTERA (las N filas identicas tras normalizar) y CONDENSADA (mismo
  numero de filas y mismo orden, todos los valores fieles, pero texto
  re-tecleado en M de N). CONDENSADA no es rojo: el austero permite condensar.
  Lo que es ROJO es que el reporte diga "pegada entera" cuando la guarda dice
  CONDENSADA, y tambien que cambie el numero de filas o el orden.
  (2.3) CASO POSITIVO SOBRE EL CASO REAL: corrida contra el REPORTE.md de la
  vuelta 106 (git show e1fefbba:docs/loop/REPORTE.md) tiene que dar CONDENSADA
  con 9 de 11 filas re-tecleadas, que es lo que yo mid a mano. Pega la salida.
  (2.4) CASO ROJO POR MUTACION, y no vale una que no muerda: fabrica una copia
  del reporte 106 con UNA cifra de la cabecera alterada (por ejemplo el censo
  a 3.854) y comprueba que la guarda salta senalando esa celda. Una guarda que
  da lo mismo con la celda adulterada no esta contando.
  (2.5) Y LA CABECERA DE TU REPORTE DE ESTA VUELTA PASA POR ELLA al cierre,
  junto con las otras guardas, despues de tu ultima edicion. Si condensas,
  escribe "condensada del tallador" y no "pegada entera", y deja que la guarda
  lo confirme.

- TAREA 3, LA RELECTURA CONJUNTA DEL 145. Discrepo y te dejo mi caso escrito
  con la evidencia; TU DECIDES CON LA VARA, no yo (AUDITOR.md 1.3).
  (3.1) MI PATA DE TEXTO, y es la que mas pesa. Tu correccion_v106 se sostiene
  entera sobre una afirmacion: que el paso 4 del hijo ("Evitar sustituir el
  pensamiento profundo por 'mera accion fisica'") tensiona con la tesis
  central del nodo madre. VE A LEER LA MADRE ENTERA OTRA VEZ. Su resumen
  termina "La accion debe ser voluntaria y comprometer a todo el organismo, no
  un mero movimiento mecanico", y su paso 3 dice "Asegurar que la accion sea
  genuina y comprometida ('significar lo que se dice/hace'), no un gesto
  mecanico vacio". La madre hace la MISMA advertencia que el hijo, dos veces y
  casi con las mismas palabras. Mi lectura es que tu motivo leyo la tesis de
  la madre por su TITULO y no por su cuerpo.
  (3.2) MI PATA DE DOCTRINA, y es una regla escrita que tu correccion no cita.
  El acta 98 seccion 3.5 adjudico ESTE PUESTO POR SU NUMERO, a ciegas, y
  nombro la frontera: "lo que decide es DONDE cae la tension. En el 145 el
  hijo ejecuta la linea casada (articular, vincular, revisar) y la tension
  vive en OTRA linea, su paso 4 contra el paso 1 de la madre: caveat", frente
  al 113, el 119 y el 122, donde la tension cae sobre la linea casada y el
  hijo ofrece metodo alternativo: refutacion. Tu razon VIEJA la citaba con la
  referencia mal puesta (dice "acta 97 3.3"; es acta 98 3.5): la referencia
  estaba equivocada, la doctrina no.
  (3.3) LO QUE NO TE NIEGO, y lo escribo yo para que no tengas que defenderlo:
  el primer brazo del 9.6.2 leido con maxima dureza SI admite tu lectura,
  porque el paso 4 del hijo no cae dentro del paso 4 de la madre. Por eso esto
  no es caida de clase.
  (3.4) SI TE SOSTIENES, escribe donde vive la tension del paso 4 del hijo
  sabiendo que la madre ya la escribe dos veces, y por que el acta 98 3.5 no
  manda sobre el puesto que nombra. SI CEDES, la correccion_v106 se anula con
  correccion declarada (sin borrar texto viejo, como siempre) y el cierre
  vuelve de 73 / 110 (60,1%) a 74 / 109 (59,6%), recomputado con
  scripts/loop/contar_cierre_efectivo.py en los TRES sitios aditivos. Decidas
  lo que decidas, va marcado DISCUTIBLE otra vez.

- TAREA 4, EL 109 Y EL TRAMO 3 AL DOBLE. Es la relectura al doble que dispara
  la discrepancia fuera del marcado (AUDITOR.md 1.2) y la caida de reporte de
  la 1.1 por la letra afinada del 27 ago.
  (4.1) EL 109 VA A LECTURA ENTERA, la que no se hizo. Mi caso: el objeto
  directo de "Llenar el canvas inicial con tus hipotesis en las 9 areas:
  segmentos, propuesta de valor, canales, relaciones, recursos, socios e
  ingresos" es "el canvas inicial"; "con tus hipotesis en las 9 areas" es
  complemento preposicional INSTRUMENTAL; "socios" vive dentro de ese
  complemento, o sea FUERA del objeto directo. Tu motivo dice que "socios"
  esta "dentro del objeto", pero para decirlo citaste como objeto "el canvas
  inicial CON TUS HIPOTESIS EN LAS 9 AREAS...", incorporando el complemento al
  objeto: ahi esta el error, y es de analisis, no de criterio. Y la distincion
  que yo mismo te mande anotar corta en mi favor aqui: solo es satelite el que
  gobierna al hijo desde FUERA del objeto, y este lo hace.
  (4.2) PERO SATELITE NO ES SINONIMO DE QUE SE MUEVA, y no te pido que se
  mueva: te pido la lectura entera a ciegas con las dos patas del 9.6.2 mas el
  9.6.3. MI CASO PARA ESA LECTURA, para que lo verifiques contra el grafo: el
  hijo key_partners_hypothesis cubre UNA de las nueve areas; su paso 5 es
  "Actualiza el Business Model Canvas con los socios identificados", o sea que
  llenar el canvas es UN PASO SUYO y no su continente; y su paso 6 ("Planea la
  validacion posterior con reuniones reales") aterriza sobre el PASO 6 de la
  madre ("Sal a validar cada hipotesis con clientes reales cara a cara") y no
  sobre el paso 1, con lo que el hijo cruza DOS pasos y no cabe en uno, que es
  la figura del puesto 1281 del acta 94. Y EL CONTRA-CASO TE LO ESCRIBO YO
  FUERTE PORQUE PUEDE GANARME: el hijo se titula Hipotesis de Socios Clave,
  todo lo que hace desemboca en la hipotesis que se escribe en la casilla, y
  su paso 5 seria la entrega de vuelta a la madre, que es el patron canonico
  del 2.215 del 9.6.2. Examina el contra-caso por escrito antes de decidir; si
  gana, dilo y el 109 se queda.
  (4.3) EL TRAMO 3 AL DOBLE: vuelve a pasar la pregunta de tres vias por las
  18 RESUELTA vivas del tramo 3, TODAS, incluidas las que ya barriste en la
  106, y esta vez CITANDO EL OBJETO DIRECTO APARTE DEL COMPLEMENTO. Una linea
  por par con tres campos separados: verbo, objeto directo, y complementos
  preposicionales si los hay. Eso es lo que impide que un complemento
  instrumental se cuele dentro del objeto en la cita, que es exactamente como
  se colo el 109.
  (4.4) Si el barrido nuevo levanta mas satelites, van a lectura entera igual
  que el 109. Si no levanta ninguno mas, dilo con la cifra y ya esta: no
  fuerces hallazgos.
  (4.5) Las que se muevan van con correccion_v107 declarada, sin borrar el
  texto viejo, y RECOMPUTAS en los tres sitios aditivos.

- TAREA 5, EL CIERRE DE LA BOLSA, ESTA VEZ DE VERDAD Y CON LA CIFRA ENTERA.
  (5.1) EL LOTE, contado por mi hoy (docs/loop/_auditor_v106_bolsa.txt): de
  las 73 RESUELTA vivas, ONCE no han pasado NUNCA por la pregunta de tres
  vias: el 3, 5, 7, 10, 13, 16, 19, 27, 30 y 33 del tramo1, mas el 148 del
  tramo3. De esos once, el 3 y el 16 no han pasado por NADA (veces_releido 0),
  nueve pasaron por relectura ciega entera en las vueltas 101 a 104, y el 148
  se resolvio por correccion_v99. RECUENTA TU EL LOTE ANTES DE CORRERLO y
  declara la cifra que te salga a ti: si difiere de la mia, la discrepancia se
  declara, no se resuelve copiando. En la 106 recontaste y me ganaste; hazlo
  otra vez.
  (5.2) La guarda del paso mal casado corre primero sobre los cuatro tramos,
  como siempre. Deben salir los mismos dos (46 y 147) o dices por que no.
  (5.3) Despues la pregunta de tres vias sobre los once, con el formato de
  TRES campos de la 4.3 (verbo, objeto directo, complementos aparte).
  (5.4) Los que salgan SATELITE van a lectura entera a ciegas, con las dos
  patas del 9.6.2 mas el 9.6.3, y los que se muevan con correccion_v107 y
  recomputo en los tres sitios.
  (5.5) Y CUANDO ACABES, DI LA CIFRA CON SU DEFINICION PEGADA, las dos: (a)
  cuantas RESUELTA vivas han pasado por LA PREGUNTA DE TRES VIAS, y (b)
  cuantas no han pasado por NINGUN instrumento. Si al terminar esta tarea la
  (a) son TODAS, la bolsa queda cerrada por la misma pregunta y lo dices asi.
  Si no lo son, di cuantas faltan, donde, y por que.
  (5.6) EL LOTE ENTERO CABE BAJO EL DOBLE DEL AUSTERO. Si no cabe con sus
  guardas completas, lo unico que puedes partir es la TAREA 4.3 (el tramo 3 al
  doble): hazla en la vuelta siguiente diciendolo con la cifra de lo que si
  hiciste. Las TAREAS 3, 4.1, 4.2 y 5 no se parten.

- LAS GUARDAS DEL CIERRE, y desde hoy son CUATRO instrumentos y OCHO casos.
  tallar_veredictos_reporte.py sobre tu propio reporte;
  tallar_nombre_de_operacion.py OP-E-03; verificar_apertura_sellada.py
  --vuelta 107; la guarda nueva de la TAREA 2; y las SIETE mutaciones mas el
  griton corridos en una sola pasada: _auditor_v104_mut_A, _B, _C,
  _auditor_v105_mut_D, _E, _F, _auditor_v106_mut_G y _auditor_v106_mut_H, con
  el reporte 102 (git show f253842b). Los resultados que no pueden cambiar: A,
  B, C, E, F y G en ROJO EXIT 1; D y H en VERDE EXIT 0; el 102 en VERDE EXIT
  0. La H es la frontera declarada por diseno: si algun dia da ROJO, eso no es
  una mejora, es que se movio el perimetro sin decidirlo, y paras.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Lo unico que va fijo
  es el sellado de la apertura, que es antes de todo.

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
  ninguna operacion de fase. No se escribe ni se retira una sola arista: las
  TAREAS 3, 4 y 5 son juicio y registro, no cirugia, igual que OP-E-03.

- LA NOTA DE HIGIENE DE SIEMPRE, y sigue midiendose igual: git status trae M
  en dataset/metadata/master_graph.json desde antes de que nadie toque nada, y
  NO es un cambio (8.391.653 bytes y sha256 f0e3993967457ed2b7a0, identico a
  HEAD; lo volvi a medir hoy, despues de correr el ciclo entero). No lo
  commitees y no lo "arregles". Y si corres SOLO run_phase1.py el fichero
  cambia de tamano y parece que has movido algo: es el CICLO DE TRES ENTERO el
  que lo devuelve identico byte a byte. Ojo con la ruta: el validador vive en
  scripts/run_phase1.py, no en la raiz.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
