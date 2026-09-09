Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. VUELTA 215. FASE III, EJECUCION. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas
obligatorias por operacion.

ESTA ES LA VUELTA DE BATERIA de la cadencia de cinco (AUDITOR.md 6.1), y
lleva ademas el CIERRE INTEGRAL del bucle. Las dos cosas caben juntas y lo
digo antes de que nadie lo discuta: la 6.1 prohibe TRABAJO DE PLAN al lado
de la bateria, y el cierre integral NO es trabajo de plan, es
VERIFICACION. No se escribe ni un nodo, ni un veredicto, ni una ficha.

EL TOPE DE SUB-TAREAS ES CINCO (acta 212, adjudicacion 6.8, linea 75168 de
docs/loop/ACTA_AUDITOR.md), y estas cinco lo agotan. SIGUE VIGENTE LA
MORATORIA DE MAQUINARIA (AUDITOR.md 6.3): no se fabrican arneses, guardas
ni lectores nuevos, no se toca el lanzador de la bateria, y la nomina
sigue CONGELADA EN 135. Lo que escribas en el arbol de scripts del bucle
lleva prefijo _v215_ y muere con la vuelta.

MI ACTA DE LA 214 ESTA ESCRITA Y ES LA FUENTE DE LAS ADJUDICACIONES QUE
SIGUEN. Ninguna de ellas se vuelve a discutir en tu reporte: se aplican.

- TAREA 1, LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA.
  (1.a) LEE MI ACTA DE LA VUELTA 214 en docs/loop/ACTA_AUDITOR.md, sus
  secciones 3 y 5, y REGISTRA EN TU REPORTE, con la linea de donde sale
  cada una, LAS NUEVE ADJUDICACIONES. Las cinco que tienes que aplicar
  como orden son estas:
     5.1  LA BATERIA SON ONCE TRAMOS, NO NUEVE. El NUEVE de AUDITOR.md
          6.1 es la cifra a SU corte y envejecio sola. Se declara corrida
          cuando LOS ONCE QUE --plan COMPUTE tengan salida sellada DEL
          MISMO CALIBRE. No reescribes AUDITOR.md: no es tuyo ni es mio.
     5.2  EL CARRIL --siguiente NO ES SENAL DE ARRANQUE. Lo detallo en la
          TAREA 2.
     5.3  EL 2.117 DE LAS CLAUSULAS DE OP-L-01 Y OP-L-02 MANDA POR SU
          CORTE. La clausula pide que ESA operacion no mueva el marcador,
          no afirma cuanto vale el marcador. CALZA si no lo mueves, y hoy
          el marcador esta en 3388. PENDIENTE CERRADO: no lo vuelvas a
          traer como pendiente de doctrina.
     5.4  UNA NEGATIVA SI SE PUEDE CITAR. Lo detallo en la TAREA 4.
     5.5  EL PUNTO 4 DE OP-I-01 NO ESTA ADJUDICADO PORQUE ES MEDICION.
          Lo detallo en la TAREA 4.
  (1.b) Y REGISTRA MI HALLAZGO 3.1 CONTRA TU PROPIO REPORTE DE LA 214, que
  es la unica caida que NO declaraste y la unica que acumula: tu seccion
  3.1, la del ciclo entero de Gate 0, salio publicada VACIA porque el
  fichero de consola que tu compositor busca NUNCA EXISTIO. Tu racha de
  reporte queda en UNO. El remedio va en la TAREA 5 y es bloqueante.

- TAREA 2, LA BATERIA ENTERA, POR TRAMOS, Y SIN EL FALSO VERDE.
  (2.a) ANTES DE CORRER NADA, PUBLICA DE QUE VUELTA SON LOS SELLOS QUE HAY
  HOY EN EL ARBOL. Los once ficheros SALIDA_V183_BATERIA_TRAMO_N.txt son
  de la vuelta 210 y estan fechados el 8 sep 2026: tabula cada uno con su
  ultimo commit y su fecha LEIDOS DE git log, nunca tecleados. Esta tabla
  es la que hace distinguible tu corrida nueva, y va ANTES.
  (2.b) NO USES --siguiente COMO SENAL DE ARRANQUE. Hoy dice que faltan 0
  tramos y que los once estan sellados, y es falso para esta vuelta: el
  lanzador nombra sus salidas con el numero de SU PROPIO fichero, el 183,
  asi que una corrida vieja y una fresca comparten nombre y ese carril no
  las distingue. CORRE --tramo 1 A --tramo 11, UNO A UNO, Y COMMITEA CADA
  SALIDA AL TERMINAR SU TRAMO. Una vuelta cortada retoma en el tramo
  siguiente, que es para lo que existe el regimen.
  (2.c) LA BATERIA VA ENTERA Y CON SU DOBLE CORRIDA, su reloj y su salida
  sellada, como manda la 6.1. NO SE AFLOJA NINGUNA GUARDA. Y una salida
  sellada que mide CERO BYTES NO CUENTA COMO HECHA.
  (2.d) SI ALGUN ARNES DE LA NOMINA CAE, PARAS Y LO TRAES. Un arnes en
  rojo en la vuelta del cierre integral no se arregla de paso.

- TAREA 3, EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL.
  (3.a) EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, LOS OCHO COMANDOS, con
  su consola SELLADA (ver TAREA 5) y las dieciocho salidas en disco.
  (3.b) LAS TRES SUITES: motor, tsc y web, con su exitcode y sus bytes.
  (3.c) EL INVENTARIO DE LAS 71 FICHAS CONTRA SUS PRUEBAS, corrido con
  scripts/loop/vuelta150_3_relectura_expediente.py --corte con el hash de
  tu apertura. PUBLICA LA CIFRA QUE SALGA, no la que te guste: yo la medi
  hoy en 40 de 71 que NO calzan, y dos de ellas, OP-V-01 y OP-L-01, siguen
  en HECHA SIN NINGUNA PRUEBA. Si tu cifra difiere de 40, dilo y no la
  ajustes.
  (3.d) EL MARCADOR Y EL CENSO RECOMPUTADOS, cada uno con su comando. Los
  mios de hoy, para que los cotejes y NO para que los copies: marcador
  3388 filas, A 550, B 72, C 5, D 2761, huecos 0; censo 3853 nodos, 3169
  vivos, 684 deprecados; aristas 8780 siguientes, 8740 previos, suma
  17520. Si algo no calza, la discrepancia se declara, no se resuelve
  copiando.

- TAREA 4, LOS DOS PUNTOS QUE OP-I-01 DEJO EN A MEDIAS, Y NO SE CIERRAN
  A OJO.
  (4.a) EL PUNTO 3, POR SU NEGATIVA, QUE SI SE PUEDE CITAR. Dijiste que
  una busqueda negativa no se puede citar y eso no es asi: tu propio
  reporte publica dos, la de rutas que no existen en 0 y la de tu sonda en
  0 de 27. Lo que AUDITOR.md 2 prohibe es AFIRMAR UNA BUSQUEDA NO CORRIDA,
  no publicar la que da cero. CORRE LA BUSQUEDA, publica su CERO CON EL
  COMANDO DELANTE, y mide el punto contra eso.
  (4.b) EL PUNTO 4, Y AQUI HAY QUE MEDIR ANTES DE DECIDIR. Su mitad
  pendiente es regenerar la vista humana, y docs/plan/10_INVENTARIO.md
  declara en su linea 19 que AHI NO SE REGENERA A PROPOSITO. NO INVENTES
  LA SEDE: busca cual es el instrumento y cual el fichero que SI la
  regeneran, publica la busqueda con su comando, y solo entonces di si el
  punto CUBRE, queda A MEDIAS o NO CUBRE. Si la sede no existe en el repo,
  eso tambien es un resultado y se dice.
  (4.c) NO MUEVAS EL CAMPO estado DE NINGUNA FICHA. La vara del trabajo
  pendiente es el instrumento, nunca el campo, y esa doctrina no se ha
  movido.

- TAREA 5, TU REPORTE, Y SU SECCION 3.1 ESTA VEZ CON CIFRAS DENTRO.
  (5.a) SELLA LA CONSOLA DEL CICLO. El ciclo de Gate 0 imprime su consola
  por stdout y en la 214 nadie la redirigio: por eso tu tabla salio en
  blanco. Redirigela a los dos ficheros que tu compositor busca, uno por
  lado, y commitealos.
  (5.b) Y LO QUE IMPORTA MAS QUE LA CONSOLA: TU COMPOSITOR CAE EN ROJO SI
  NO LA ENCUENTRA. El de la 214 escribio una fila en blanco y siguio, que
  es degradacion silenciosa y es exactamente lo que el banco 9 prohibe.
  Una guarda que no encuentra su fuente REVIENTA, no rellena con un hueco.
  Esto no fabrica maquinaria: el compositor de cierre lo escribes cada
  vuelta de todas formas, y lo unico que cambia es que falle ruidoso.
  (5.c) LA SECCION 9 CIERRA CON LA BATERIA CORRIDA, no con hueco
  declarado: esta es su vuelta. Si por lo que sea quedara hueco, lleva sus
  TRES piezas juntas o el instrumento cae en rojo.

Y LO QUE ESTA VUELTA NO ESCRIBE, Y ES BLOQUEANTE: docs/loop/PARA_ALEXIS.md
NO LO ESCRIBES TU. Tu lo propones en tu reporte, que es tu sede, con las
cifras delante y diciendo si la condicion se cumple o no. La escritura es
del AUDITOR de la 215, por la adjudicacion 4.2 del acta 203 (linea 71543
de docs/loop/ACTA_AUDITOR.md), RATIFICADA POR EL FUNDADOR el 9 sep 2026:
PROMPT_SIGUIENTE.md, ACTA_AUDITOR.md y PARA_ALEXIS.md son SEDE DEL
AUDITOR. Tu precision de la 214 sobre esto era correcta y se te abona.

LA CONDICION DE LA PARADA FELIZ, ESCRITA ANTES DE SABER SI SE CUMPLE: si
la bateria da los ONCE tramos en verde y del mismo calibre, si el cierre
integral sale limpio, y si los dos puntos de la TAREA 4 quedan medidos y
dichos, entonces la campaña esta consumada EN LO QUE EL BUCLE PUEDE
CONSUMAR, y el paso siguiente es la AUDITORIA INTEGRAL CON CREDENCIAL Y
CON EL FUNDADOR DELANTE. NO SE PIDE EL MERGE EN ESA PARADA: el merge de
pasada-unica es decision del fundador y viene DESPUES de esa auditoria. EL
BUCLE NO FUNDE RAMAS. Si algo no da verde, se dice cual y con su cifra, y
no se declara nada consumado.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
