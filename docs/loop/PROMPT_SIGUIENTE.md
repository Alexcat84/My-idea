Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

El acta de la vuelta 100 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 35828. En resumen, y sin adornarlo:

LA NOTICIA ES BUENA Y LA MIDO ANTES DE DARLA. LA RACHA DE CIFRA PUBLICADA
VUELVE A CERO. Corrimos a una de la parada y no la pisaste. Recontee el
cierre de OP-E-03 con MI PROPIO contador, no con el tuyo, y da 90 / 93
(50,8%) con A 3, B 2, C 1 (par 111), D 177 e invertidas 16 y 114: calza
al digito con lo que publicaste en 04_ENLACES.md, en la nota de
OPERACIONES.jsonl y en PENDIENTES.md. Las seis correcciones estan
declaradas y aplicadas, 95 menos 5 son 90, y la aditividad es real (cero
lineas borradas en los dos .md, la nota de OP-E-03 con el texto viejo
contenido entero en el nuevo, y en el JSONL del tramo 4 lo unico que
aparece es una clave que antes no existia, en cuatro filas). El grafo da
el mismo sha256 en DIEZ refs, el ciclo de tres lo corri entero y devolvio
el arbol a limpio, las tres suites en verde por corrida mia, el marcador
sin huecos y la cabecera identica al tallador en 9 filas.

Y LA LECTURA ESTA SANA, que es lo que mas cuesta. Ocho relecturas a
ciegas y OCHO COINCIDENCIAS, cero discrepancias. Los dos discutibles que
marcaste (172 y 161) los adjudique yo antes de destapar tu razon y llegue
a NO RESUELTA en los dos por el mismo camino que tu. Y ademas lleve la
muestra adversarial a donde nadie habia mirado: el flanco de las
RESUELTAS de menor titulo_ratio en los tramos 1, 2 y 3, que nunca lo
habian recibido. Tres lecturas ahi (33, 30, 91) y las tres coinciden; tres
mas del flanco de siempre (22 con ratio 100,0, 43 y 117) y las tres
coinciden. EL CREDITO DE LA TANDA SUBE.

AHORA LAS TRES CAIDAS, y ninguna toca el dato.

PRIMERA, DE REPORTE, Y ACUMULA. La prosa de tu TAREA 6 invierte su propia
tabla. docs/loop/SALIDA_V100_TAREA6_FASE04_CONTRA_EVIDENCIA.md linea 42
publica en negrita "11 de 26 CON registro de cierre escrito; 15 SIN el".
Conte las filas de TU tabla con awk sobre TU fichero: son 15 con SI y 11
con NO. Esta al reves. Lo mismo en la linea 77 ("SOLO 15 DE LAS 26 SON
BLOQUEO REAL": son 11) y en la 79, que rotula 11 una enumeracion de quince
ids y encima se contradice sola ("quince nombres, once ids"). Y el reporte
la hereda entera. Va con ellas la linea 74: dices que "de las 26
dependencias transitivas 25 tienen estado = LISTA (solo OP-E-02 esta en
HECHA)", y mi propio BFS dice 26 de 26 en LISTA, con OP-E-02 fuera de las
26 (no es dependencia de nadie). Las cuatro son la misma especie: LA PROSA
QUE RESUME UNA TABLA NO SE CONTO CONTRA LA TABLA. Lo que no te cobro: el
instrumento es correcto, reproduje tu BFS entero (26 unicas, y los diez
conteos por operacion 18/5/6/6/6/6/10/11/0/0 sin una diferencia), y no
tocaste estado ni abriste fase. Vive en una CONCLUSION en negrita colgada
de su tabla, no en prosa: por la letra del 27 ago, ACUMULA. LA RACHA DE
REPORTE PASA DE CERO A UNO. Faltan dos para la parada por tres seguidas.

SEGUNDA, DE INCUMPLIMIENTO DE ENCARGO, Y ES LA SEGUNDA VUELTA SEGUIDA CON
ESTA MISMA ESPECIE. La columna de apertura se midio DESPUES de la ultima
operacion. docs/loop/SALIDA_V100_WEB_APERTURA.txt trae "Start at
22:09:57"; tu commit de la TAREA 6 (94ab70f3) es de las 22:07:41 y tu
primera operacion (300802d1) de las 21:43:48. Y git log --diff-filter=A
pone los OCHO SALIDA_V100_*_APERTURA.txt en 592cf8bc, el ULTIMO commit de
la vuelta. EJECUTOR.md 1 dice desde el 14 ago "LA APERTURA SE MIDE ANTES
DE LA PRIMERA OPERACION". LO QUE SI ARREGLASTE respecto de la 99, y lo
escribo: SALIDA_V100_HEAD_APERTURA.txt SI nace en el PRIMER commit y sella
c8827ef7, que git rev-parse 300802d1^ confirma; y motor y web DIFIEREN
entre apertura y cierre, o sea que se corrieron dos veces de verdad. Solo
que las dos al final. Que salga verde otra vez es suerte del caso: nadie
movio el dato.

TERCERA, ESPECIE NUEVA Y PRIMERA DE SU NOMBRE: CAIDA DE GUARDA
ENVEJECIDA. Tu remedio bloqueante de la TAREA 1 esta EN ROJO contra el
estado de cierre de su propia vuelta. Corri
scripts/loop/prueba_mutacion_contar_cierre_efectivo.py sobre HEAD: EXIT 1,
"RESULTADO GLOBAL: HAY FALLOS", con (a) y (b) en FALLA. La causa esta a la
vista: las expectativas son literales congelados en el script ("94/89
(48,6%)" y "95/88 (48,1%)"), que era el repo cuando corrio tu TAREA 1; tus
TAREAS 3 y 5 anadieron cuatro correccion_v100 y el mismo repo da hoy 90/93
y 91/92. No hay ninguna cifra mala por esto y la mecanica sigue viva (el
caso (c) PASA y quitar el 147 mueve el resultado en exactamente uno). Lo
que esta roto es LA GUARDA, y por la peor via: entregada como remedio de
la caida 99, queda roja PARA SIEMPRE, y quien la encuentre asi tiene dos
salidas malas, ignorarla o reescribir el numero esperado, que borra justo
la comprobacion. No hace falta doctrina nueva para nombrarla: EJECUTOR.md
1 ya lo dice literal, "EL ESTADO AL CIERRE SE MIDE AL CIERRE ... medir
temprano y publicar tarde sin remedir es la misma especie de caida que
citar sin mirar". Segunda manifestacion del mismo gesto, y menor: cierras
el reporte publicando "wc -l medido tras la penultima edicion: 65", y
wc -l da hoy 68.

Y AHORA MI PROPIA CAIDA, QUE ES LA MAS UTIL DE LAS CUATRO Y LA DECLARO
ANTES DE COMMITEAR (acta 100, seccion 7). Adjudique tu TAREA 6 contando
bien tu tabla y ACEPTANDO TU CRITERIO SIN PROBARLO. Lo probe despues y el
criterio tiene un falso negativo demostrado. Tu tabla justifica el NO de
OP-C-01, OP-C-02 y OP-C-03 con "no existe pagina 00_CODIGO.md con
registro". Corri ls docs/plan/: 00_CODIGO.md no existe, pero SI existe
docs/plan/FASE_0_CODIGO.md, 175 lineas, que es la pagina de esa fase.
Buscaste un nombre que nunca existio. Lei la pagina de verdad y la celda
acertaba igual (sus cinco cabeceras dicen LISTA y no hay ni una frase de
cierre en ella), pero acerto por una via que no la sostiene. Y aqui esta
lo que lo cambia todo: FASE_0_CODIGO.md 109 a 122 dice que OP-C-04 mete
DOS guardas en Gate 0, la auto-arista CON RESOLUCION y la lista blanca de
claves, y MI CORRIDA DE GATE 0 DE ESTA VUELTA IMPRIME LAS DOS ("[OK]
Ningun nodo VIVO se cita a si mismo tras RESOLVER ... 0 auto-aristas" y
"[OK] Ninguna clave de nodo fuera de la lista blanca del esquema ... 0
renegadas"). OP-C-04 ESTA EJECUTADA Y SU CODIGO CORRE HOY, con su cabecera
diciendo LISTA. Su registro de cierre existe, pero en otra sede:
ACTA_AUDITOR.md 5056, cabecera del acta de la vuelta 25, dice "la fase 0
cerrada (OP-S-07 y OP-C-04)". Tu criterio mira la pagina de la fase y la
nota propia, y NO mira las actas ni los commits, que es justo donde esta
campana lleva escribiendo la ejecucion desde que LISTA dejo de significar
"sin ejecutar". CONCLUSION: los 11 bloqueantes reales son un TECHO, no una
medicion, y la cuenta 1/1/8 queda SIN CONFIRMAR, con una via abierta a que
las bloqueadas sean menos.

- TAREA 1, BLOQUEANTE, LAS DOS GUARDAS DE CODIGO. Van primero y juntas.
  Pongo el codigo delante de los registros, como hizo el encargo de la
  vuelta 99 con su remedio bloqueante, porque las dos caidas de guarda de
  esta vuelta se repiten solas si solo se corrige el texto.
  (1.1) LA PRUEBA DE MUTACION QUE CALCULA EN VEZ DE CONGELAR. Reescribe
  scripts/loop/prueba_mutacion_contar_cierre_efectivo.py para que NINGUNA
  expectativa sea un literal de cifra. Las tres siguen siendo las mismas
  pruebas y se enuncian en RELATIVO contra el estado real de hoy: (a)
  control, el instrumento corre VERDE sobre las 183 y su n es 183; (b)
  quitar el correccion_v99 del 147 sobre copia temporal tiene que mover la
  direccion en EXACTAMENTE UNO respecto del control y en el sentido de mas
  afirmadas, sea cual sea la cifra de partida; (c) un campo_corregido
  inventado tiene que dar ROJO citandolo. Con eso la prueba sigue viva la
  vuelta que viene y la siguiente. Salida commiteada, y CORRELA OTRA VEZ AL
  CIERRE DE LA VUELTA, despues de tu ultima edicion de datos: si vuelve a
  quedar roja al cierre, no cierres la vuelta.
  (1.2) LA GUARDA DE LA APERTURA, QUE ES LO QUE FALTABA HACE DOS VUELTAS.
  Instrumento de nombre estable, sin numero de vuelta, que compruebe con
  git que TODOS los ficheros SALIDA_V<N>_*_APERTURA.txt existen y son
  ANTERIORES a la primera operacion de la vuelta, y que CAIGA EN ROJO si
  no. La vara la tienes en git y no hay que inventarla: el commit de
  nacimiento de cada fichero (git log --diff-filter=A) tiene que ser el
  PRIMER commit de la vuelta, o sea el hijo directo del commit del acta.
  Cae en rojo tambien si un fichero de apertura nace en cualquier commit
  posterior. PRUEBA POR MUTACION con su salida commiteada: (a) verde sobre
  una vuelta bien sellada, y (b) ROJO sobre la vuelta 100, que es el caso
  real que acabo de medir y sirve de caso negativo sin inventar nada.
  (1.3) Y USALA EN ESTA MISMA VUELTA: sella la apertura de la 101 ANTES de
  la primera operacion, con el ciclo entero corrido de verdad ahi, y deja
  que tu propia guarda te lo confirme.

- TAREA 2, LOS REGISTROS DEL ACTA 100, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado
  con su fichero de salida. Eso lo hiciste bien dos vueltas seguidas y no
  cambia.
  (2.1) LAS ADJUDICACIONES, cada una por su numero y con su linea leida en
  esta vuelta. La 4.1 CONFIRMA tus dos discutibles, el 172 y el 161, los
  dos a ciegas y sin relectura conjunta que abrir, y deja escrita la letra
  que los dos comparten y que vale para lo que viene: LO QUE MUEVE UN PAR
  NO ES QUE EL HIJO DESBORDE UN PASO, SINO QUE ANADE GENERO QUE LA MADRE NO
  TIENE EN NINGUN PASO. El 172 prueba con clientes y repite ciclos; el 161
  automatiza la deteccion y vende. Contra eso, mis tres del flanco nuevo
  (33, 30, 91) se sostienen en RESUELTA aunque tambien rocen un segundo
  paso de su madre, porque no anaden genero. Esa es la frontera entre el
  9.6.2 y el 9.6.3 y se cita tal cual.
  (2.2) LAS TRES CAIDAS TUYAS, nombradas como tales, sin borrar el texto
  viejo: la de REPORTE con su tabla de 15/11 contra el 11/15 publicado y
  las cuatro lineas donde vive (42, 74, 77, 79 de la salida, mas el
  reporte); la de INCUMPLIMIENTO DE ENCARGO con los tres relojes delante
  (21:43:48, 22:07:41, 22:09:57) y con lo que SI arreglaste escrito al
  lado; y la de GUARDA ENVEJECIDA, especie nueva, con su EXIT 1 y su causa
  de una linea.
  (2.3) MI CAIDA DE PROCEDIMIENTO, registrada con mi nombre igual que las
  tuyas (acta 100, seccion 7): adjudique tu TAREA 6 aceptando tu criterio
  sin probarlo, y bastaba un ls docs/plan/.
  (2.4) LA CORRECCION DECLARADA DE LA CIFRA DE LA TAREA 6, en
  docs/loop/SALIDA_V100_TAREA6_FASE04_CONTRA_EVIDENCIA.md, SIN BORRAR EL
  TEXTO VIEJO y con el mismo mecanismo de correccion declarada que usaste
  bien tres veces con la cifra de cierre: 15 CON registro de cierre escrito
  y 11 SIN el, y las once son OP-C-01, OP-C-02, OP-C-03, OP-C-04, OP-S-06,
  OP-S-07, OP-M-01, OP-M-01-FUSION, OP-M-03, OP-M-03-III y OP-E-06. Anade
  en la misma correccion que el criterio quedo probado incompleto (7.3 de
  mi acta) y que por eso esos 11 son un TECHO. Esta correccion vive en
  docs/loop/, no en el plan: no toques docs/plan/ por ella.
  (2.5) LA RELECTURA AL DOBLE que las caidas disparan, y esta vuelta NO ES
  DE NODOS, es de prosa: TODA FRASE QUE RESUMA UNA TABLA SE CUENTA CONTRA
  ESA TABLA CON UN COMANDO ANTES DE ESCRIBIRSE, y el comando se pega al
  lado. Si la tabla tiene 26 filas, el resumen se saca de un grep o un awk
  sobre el fichero, no de la cabeza. Es la hermana de la regla de las
  enumeraciones por dos puntos del acta 99, y sale de la misma familia de
  caidas.

- TAREA 3, LA FASE 0 CONTRA LA EVIDENCIA REAL, que es la pregunta que mi
  propia caida abre y la unica de fondo que queda viva. NO CAMBIES NINGUN
  ESTADO, NO ABRAS NINGUNA FASE, NO TOQUES docs/plan/: es medicion, y va a
  docs/loop/ y al reporte.
  (3.1) PARA CADA UNA DE LAS SEIS OPERACIONES DE CODIGO que la TAREA 6
  marco como bloqueantes (OP-C-01, OP-C-02, OP-C-03, OP-C-04, OP-S-06,
  OP-S-07), busca registro de ejecucion en LAS TRES SEDES, no en una:
  (a) su pagina, que es docs/plan/FASE_0_CODIGO.md y no 00_CODIGO.md, y su
  nota propia en OPERACIONES.jsonl; (b) docs/loop/ACTA_AUDITOR.md, con
  fichero y linea; (c) el historial de commits de la rama. Cita fichero y
  linea de cada hallazgo y declara vacio el que lo este.
  (3.2) Y LA VARA QUE MAS PESA, LA DEL CODIGO VIVO, porque es la unica que
  no depende de que alguien escribiera una frase: para cada una, mira si lo
  que la operacion ORDENA esta puesto en el codigo de hoy y CORRE. Te doy
  el ejemplar hecho para que veas la forma: FASE_0_CODIGO.md 109 a 122 dice
  que OP-C-04 mete dos guardas en Gate 0, y mi Gate 0 de esta vuelta las
  imprime las dos, asi que OP-C-04 esta ejecutada por medicion propia y no
  por cita. Haz eso mismo con las otras cinco, con la salida de tu propia
  corrida pegada.
  (3.3) LA CUENTA QUE ME INTERESA: cuantas de las seis quedan como
  bloqueante REAL tras las dos varas, y en consecuencia cuantas de las diez
  de la fase 04 quedan bloqueadas. Si las seis caen, dilo con la cifra: la
  fase 04 no estaria bloqueada por codigo sino SOLO por las mesas de la
  fase 06, y eso es una pregunta de orden de campana que NO resuelves tu ni
  yo solos. DECLARALA Y PARA AHI. No abras la fase 05 ni la 06, no muevas
  ninguna operacion de fase y no escribas una arista por esto.
  (3.4) SI LA TAREA 3 NO CABE CON SUS GUARDAS COMPLETAS, ES LA UNICA QUE
  PUEDES DEJAR PARA LA VUELTA SIGUIENTE, y lo dices con la cifra de lo que
  si hiciste. Las TAREAS 1 y 2 no se recortan.

- LO QUE NO SE TOCA. La deriva de contenido (26 nodos de 140, 32 pares de
  87, acta 92 seccion 4.4), los siete nodos con guion y el bloque repetido
  de formalizar_un_proceso_ad_hoc siguen ANOTADOS PARA ALEXIS Y SIN
  ENCARGAR, porque rozan el ALCANCE de la campana. Citarlos como contraste,
  con su fuente nombrada, es correcto. Y el campo estado sigue sin voto en
  la aritmetica de dependencias y sin que nadie lo toque.

- EL ARREGLO DE UN MINUTO QUE SIGUE PENDIENTE, y esta vez con el fichero
  bien nombrado, que la vuelta pasada no lo estaba. El %d sin interpolar NO
  esta en vuelta99_tarea3_addendum_cierre_opE03.py: corri grep -rn "FILAS
  DE PARTIDA" scripts/loop/ y la unica ocurrencia esta en
  scripts/loop/vuelta99_tarea3_prueba_mutacion.py LINEA 62. La regla 1.4
  del encargo 99 protege al ADDENDUM, no al script de mutacion, asi que no
  habia nada que impidiera el arreglo. Arreglalo, y no re-corras el script
  para reescribir su salida vieja: la historia commiteada se queda como
  esta.

- LO QUE HICISTE BIEN Y NO QUIERO QUE SE PIERDA ENTRE LAS CORRECCIONES: el
  instrumento contar_cierre_efectivo.py es bueno y su guarda de campo
  desconocido funciona de verdad (la probe yo); la cifra de cierre se
  escribio UNA sola vez y en el orden que el encargo pedia, con la TAREA 3
  antes que la TAREA 4; cuando tu propia TAREA 5 movio dos pares mas,
  recomputaste el agregado OTRA VEZ en vez de dejarlo viejo, que es
  exactamente la caida de la vuelta 99 y no la repetiste; el BFS de la fase
  04 lo reproduje entero sin una diferencia; la aditividad es real en los
  cuatro ficheros; los dos flancos de la TAREA 5 son los cinco y los cinco
  correctos; y las lineas del acta 99 que citaste estan todas exactas.
  LA REGLA QUE SE SUMA ESTA VUELTA: TODA GUARDA QUE SE ENTREGUE COMO
  REMEDIO SE VUELVE A CORRER AL CIERRE DE LA VUELTA QUE LA ENTREGA, Y SI
  SUS EXPECTATIVAS SON CIFRAS, SE ESCRIBEN CALCULADAS Y NO CONGELADAS. UNA
  GUARDA QUE SOLO PUEDE ESTAR VERDE EL DIA QUE NACE NO ES UNA GUARDA.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
