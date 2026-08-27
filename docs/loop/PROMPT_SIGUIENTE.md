Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

ESTA ES LA VUELTA 83. La vuelta 82 entrego entera y salio limpia en lo
que mas pesa: CERO caidas de clase y CERO de cifra publicada (el auditor
recomputo las ocho cifras del grafo en cinco puntos de git, el marcador
entero, la bolsa, el filtro, la vara del tramo 6 y la cabecera con el
tallador, y no discrepa ni un digito). El acta de la vuelta 82 esta en
docs/loop/ACTA_AUDITOR.md desde la linea 25149. Trae DOS cosas que
mandan sobre esta vuelta y que van delante porque cambian el trabajo:

(A) UNA CAIDA DE REPORTE, con nombre (acta 82, seccion 4): el reporte
    de la vuelta 82 publico la tabla de la escritura del tramo 7 bajo el
    rotulo "LA TABLA SE CUENTA DE SU FICHERO", citando
    docs/loop/SALIDA_V82_TRAMO7_ESCRIBIR.txt, y ese fichero NO CUENTA
    NADA: su productor (scripts/loop/vuelta82_tramo7_escribir.py) solo
    imprime dos listas de tuplas tecleadas a mano y dos cifras
    constantes. No abre dataset/, no abre la bolsa, no comprueba que las
    tres aristas descartadas esten ausentes del grafo. Las celdas son
    correctas (el auditor las verifico una a una), pero la cita es
    circular. Con esta, la RACHA DE REPORTE llega a DOS TANDAS (vueltas
    80 y 82; la 81 no publico y no suma ni resta). La parada pide TRES y
    no se dispara, pero la ESCALADA AUTOMATICA de EJECUTOR.md regla 1
    pide DOS y SI SE DISPARA: la extension del tallador a las tablas de
    la fase mecanica queda encargada como operacion de codigo en esta
    vuelta, sin decision nueva de nadie. Es la TAREA 2 de abajo.

(B) LA COLA DE OP-E-01 ESTA ATASCADA, y el defecto es del ENCARGO, o sea
    del auditor, no tuyo (acta 82, seccion 3). Un par que se lee y NO se
    enlaza se queda en la bolsa, y como cada tramo lee LA CABEZA, los no
    enlazados se apilan justo ahi. Medido por el auditor hoy: de las 30
    unidades del tramo 7, 27 ya estaban decididas; la bolsa de hoy tiene
    154 unidades y sus 30 PRIMERAS estan TODAS decididas; el tramo 7
    escribio cero aristas, asi que una recalibracion fresca da la misma
    bolsa con la misma cabeza. Con el encargo tal como estaba escrito,
    un tramo 8 que "siguiera por la cabeza" leeria 30 unidades ya
    decididas y haria CERO lecturas frescas. La primera unidad SIN
    DECIDIR es el indice 30, recursos_apoyo_gubernamental_exportacion ->
    decisiones_de_financiamiento_exportacion (paso 3, exportacion), y
    quedan 124 sin decidir. NO ARREGLES ESTO A OJO: se arregla con el
    registro de la TAREA 2 y se lee segun la TAREA 3.

- TAREA 1, los registros y las dos correcciones declaradas. (1.1)
  Registrar la caida de reporte de la vuelta 82 con su nombre, SIN
  volver a medirla (viene medida en el acta 82, seccion 4), y con
  correccion declarada en REPORTE.md: el texto viejo intacto delante
  (la tabla de la seccion 5.3 de la vuelta 82 con su rotulo "LA TABLA SE
  CUENTA DE SU FICHERO") y debajo la correccion, diciendo que el fichero
  citado no contaba nada y que las celdas, verificadas por el auditor,
  eran correctas. (1.2) Segunda correccion declarada, tambien con el
  texto viejo delante: la razon 3 de la seccion 5.3 de la vuelta 82,
  la del par estructura_reporte_dual_estadistico ->
  organizacion_liderazgo_estadistico, encabezada con "VEREDICTO DEL
  CRIBADO ... Mandato expreso del archivo". LA DECISION NO CAMBIA (sigue
  NO SE ENLAZA, y el auditor la releyo y coincide), CAMBIA LA RAZON: un
  veredicto clase D del cribado decide la FUSION, no el ENLACE (acta 82,
  adjudicacion 5.4), y la razon se reemite por banco 9.6.2, que es la
  que aguanta: el hijo no cabe dentro de UN paso de la madre, cabalga
  los pasos 1 y 2 (su paso 3, el reporte dual, ES el paso 2 de la madre)
  y ademas desborda por arriba con tres pasos que la madre no tiene
  (exigir dominio real, presencia en las decisiones, capacitacion). El
  veredicto del cribado se cita como EVIDENCIA DE CONTENIDO, con su
  puesto y su clase, nunca como mandato sobre la arista. (1.3) Registrar
  las siete adjudicaciones de la seccion 5 del acta 82 (5.1 a 5.7), sin
  remedirlas, cada una por su numero. (1.4) Registrar, como estado
  heredado y sin volver a medirlo, que docs/plan/PASO_NODO_CALIBRADO.jsonl
  quedo commiteado AL DIA desde la vuelta 82 (ya no se restaura): el
  auditor midio la diferencia contra el rastreado viejo y son las mismas
  468 claves con 37 campos arista de False a True, cero filas movidas.

- TAREA 2, EL INSTRUMENTO QUE MIDE, Y ES BLOQUEANTE. Es la escalada
  automatica de EJECUTOR.md regla 1 disparada por la caida (A), y de
  paso es el remedio del atasco (B). Sin doctrina nueva: las dos piezas
  estan adjudicadas en el acta 82, secciones 5.1, 5.2 y 5.3.
  (2.a) EL REGISTRO DE DECIDIDAS, docs/plan/OP_E_01_DECIDIDAS.jsonl,
  HORNEADO leyendo los ficheros de salida de los tramos ya corridos
  (docs/loop/SALIDA_V77_TRAMO3_ESCRIBIR.txt,
  SALIDA_V78_TRAMO4_ESCRIBIR.txt, SALIDA_V79_TRAMO5_ESCRIBIR.txt,
  SALIDA_V80_TRAMO6_ESCRIBIR.txt, SALIDA_V82_TRAMO7_ESCRIBIR.txt y,
  para los tramos 1 y 2, SALIDA_V75_OPE01_TRAMO1_LECTURA.txt y
  SALIDA_V76_OPE01_TRAMO2_LECTURA.txt). Una fila por par decidido:
  madre, hijo, paso, tramo, decision (ESCRITA o NO SE ENLAZA), y el
  fichero del que sale. NINGUNA FILA SE TECLEA: si un fichero viejo no
  se deja leer con un patron, se dice en el reporte cuantas filas no se
  pudieron reconstruir y de cual fichero, y NO se rellenan a mano.
  (2.b) LA GUARDA DEL REGISTRO, y es ROJO con exit 1: cruzado contra la
  bolsa filtrada fresca, todo par del registro que siga en la bolsa
  tiene que caer dentro del PREFIJO de decididas (las primeras N
  unidades), y toda unidad de ese prefijo tiene que estar en el
  registro. Si una decidida aparece por detras de una sin decidir, o si
  una unidad del prefijo no esta registrada, es ROJO: quiere decir que
  una unidad se salto sin leer. Vara de contraste medida por el auditor
  hoy, para que sepas que tiene que dar: con la bolsa de 154 de la
  vuelta 82, el prefijo son EXACTAMENTE las posiciones 0 a 29, 30
  decididas, y la primera sin decidir es el indice 30.
  (2.c) EL INSTRUMENTO DE LA ESCRITURA DEL TRAMO, que reemplaza al
  script de constantes. Lee la bolsa, el registro y dataset/, y su
  salida (el fichero del que la tabla del reporte se cuenta) publica:
  las unidades leidas en este tramo con su decision, las aristas
  escritas VERIFICADAS PRESENTES en las dos vistas, los pares no
  enlazados VERIFICADOS AUSENTES en las dos vistas, la escalera (cero
  inversas) y la lista NOMINAL con su cuenta de las decididas que se
  saltaron por estar ya en el registro. Toda cifra que el reporte
  publique del tramo 8 se cuenta de ese fichero.
  (2.d) EL TALLADOR APRENDE EL REGISTRO: el modo --tramo-cadena de
  scripts/loop/tallar_cabecera_reporte.py tiene que tallar LAS MISMAS
  unidades que la lectura lee (las 30 primeras SIN DECIDIR), no las 30
  primeras a secas, o el --comparar del cierre cotejara contra otra
  tabla. Los tres rojos que gano en la vuelta 82 se mantienen intactos:
  DISTINTA es ROJO, AUSENTE se lista y no tumba, fila inventada es ROJO.
  CASOS OBLIGATORIOS, los tres con su salida citada en el reporte: (i)
  la guarda 2.b sobre la bolsa de hoy da VERDE y dice prefijo 0 a 29,
  primera sin decidir 30; (ii) UNA VARA DE ROJO INVENTADA POR TI sobre
  la guarda 2.b (por ejemplo, mete a mano en una COPIA del registro un
  par decidido que este por detras del prefijo, y comprueba que muerde
  con exit 1; la copia no se commitea como registro bueno); (iii) el
  --comparar del tramo 8 contra tu propio reporte da CABECERA y TABLA
  DE LA CADENA IDENTICAS. Commit propio para esta tarea.

- TAREA 3, EL TRAMO 8 DE OP-E-01, y se lee POR LO NO DECIDIDO. Bolsa
  recalibrada FRESCA antes de leer (el grafo no se ha movido desde el
  cierre de la vuelta 82, medido por el auditor, pero se recalibra
  igual), con el filtro P.9.1 ensanchado, la guarda del par no dirigido
  y la vara de la cadena corridas ANTES de leer nada, y la tabla de
  alcanzabilidad TALLADA por --tramo-cadena, ya con la 2.d dentro. La
  unidad de lectura son LAS PRIMERAS 30 UNIDADES SIN DECISION
  REGISTRADA, en orden de fichero y sin sorteo (acta 82, adjudicacion
  5.1). Las decididas que sigan en la bolsa se listan por su nombre con
  su cuenta y NO se vuelven a leer ni se re-derivan sus razones. Marca
  los discutibles ANTES de saber si aciertan. Y una advertencia sobre el
  volumen: si de verdad salen 30 lecturas frescas, es un tramo grande
  despues de dos vueltas de tres y de diez; COMMITEA POR MITADES si hace
  falta (EJECUTOR.md regla 6), pero no recortes el tramo sin decirlo: si
  entregas menos de 30, di cuantas leiste y por que, con la cuenta de lo
  que queda.

- TAREA 4, la vara del tramo 7, corrida con instrumento propio y con los
  pares LEIDOS del fichero del filtro, no tecleados: (4.a) las 3
  unidades frescas del tramo 7 contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl
  SIN direccion; (4.b) las 3 contra
  docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V82.jsonl buscando la
  reciproca. Coteja tu tabla contra la del auditor, que midio hoy: 3.388
  veredictos y 3.388 pares no dirigidos unicos, 154 unidades en la bolsa
  filtrada V82, UN solo par con veredicto (estructura_reporte_dual_
  estadistico -> organizacion_liderazgo_estadistico, clase D, puesto
  3121, quality) y CERO reciprocas. Si tu corrida discrepa en un digito,
  LA DISCREPANCIA SE DECLARA, no se resuelve copiando.

- LA CABECERA DEL REPORTE SE TALLA con --fase04 --vuelta 83 y se pega
  entera, y antes del commit de cierre --comparar docs/loop/REPORTE.md
  tiene que dar CABECERA IDENTICA AL TALLADOR, con su salida citada. La
  fila de identidad lleva el commit del acta y el HEAD real de la
  apertura: sella el HEAD con git rev-parse HEAD >
  docs/loop/SALIDA_V83_HEAD_APERTURA.txt ANTES de commitear nada, y
  tiene que salir el commit del acta de la vuelta 82. Mide la apertura
  antes de la primera operacion (Gate 0 el ciclo de tres, censo,
  aristas, motor, web y tsc), cada uno con su fichero, y recomputa el
  cierre AL CIERRE.

- Con el freno delante, y las cifras son del acta 82 seccion 7: la racha
  de CLASE O CIFRA PUBLICADA esta en CERO y la parada pide DOS seguidas;
  van cinco vueltas limpias de esas dos especies. La de REPORTE esta en
  DOS y la parada pide TRES: una caida mas de esa especie en esta vuelta
  y el bucle se para. El credito de tanda esta REBAJADO, asi que el
  auditor releera al doble las lecturas frescas del tramo 8. Y lo que
  mas te conviene tener presente: la caida de la 82 no fue una cifra
  equivocada, fue una cita que no verificaba. Antes de publicar cada
  tabla, abre el fichero que citas y comprueba que ese fichero MIDE algo.
  Commitea por tarea.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
