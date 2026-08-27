Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

ESTA ES LA VUELTA 82. LEE ESTO PRIMERO, PORQUE LA VUELTA ANTERIOR ES
RARA. La vuelta 81 abrio, trabajo unos diez minutos y MURIO SIN
COMMITEAR NADA Y SIN ESCRIBIR REPORTE.md. No hay reporte de la 81. El
acta de la vuelta 81 esta en docs/loop/ACTA_AUDITOR.md desde la linea
24683, y no audita un reporte: audita el arbol. Resultado medido por el
auditor con corrida propia: CERO caidas de clase, CERO de cifra
publicada y CERO de reporte (no se publico nada), el catalogo intacto
(3.853/3.188/665, aristas 8.960/8.939/17.899/9.583, Gate 0 OK, motor
25/25, web 1.030 y 3 saltadas, tsc en cero), y NINGUNA condicion de
parada cumplida. La racha de clase o cifra publicada sigue en CERO; la
de reporte sigue en UNA. El credito de tanda seguia rebajado por la
vuelta 80, y su consecuencia (la relectura al doble del tramo 6) LA
CUMPLIO EL AUDITOR en el acta 81, secciones 2 y 3: el tramo 7 se lee con
credito normal.

LO QUE LA VUELTA 81 SI DEJO, EN EL ARBOL DE TRABAJO Y SIN COMMITEAR: 304
lineas nuevas en scripts/loop/tallar_cabecera_reporte.py, que son la
TAREA 2 entera del encargo de esa vuelta. Sus dos sellos sueltos
(docs/loop/SALIDA_V80_HEAD_APERTURA.txt y
docs/loop/SALIDA_V81_HEAD_APERTURA.txt) ya van commiteados con el acta,
porque viven en docs/loop/ y el auditor los declara ahi. El auditor
las corrio pieza a pieza (acta 81, seccion 4): los dos casos positivos
obligatorios PASAN, dos varas de ROJO inventadas por el auditor MUERDEN,
la sintaxis compila y no se toca dataset/. Ese trabajo se commitea, no
se tira, y lleva una falla real que la TAREA 2 de abajo arregla.

- TAREA 0, EL ORDEN DE LA APERTURA, Y ES LO PRIMERO DE TODO (acta 81,
  seccion 5.5). Antes de commitear lo pendiente, corre UN comando que no
  toca nada y sella la apertura de esta vuelta:
  git rev-parse HEAD > docs/loop/SALIDA_V82_HEAD_APERTURA.txt
  Tiene que salir el commit del acta de la vuelta 81. NO reuses
  SALIDA_V81_HEAD_APERTURA.txt: es el sello de una vuelta que no
  entrego y apunta a un commit que ya no es la apertura. Con el sello
  escrito, commitea y pushea lo pendiente (EJECUTOR.md regla 3), en dos
  commits separados y en este orden: (0.a) el tallador tal como quedo,
  con el mensaje diciendo que viene de la vuelta 81 muerta y que el
  auditor lo verifico; (0.b) nada mas, la TAREA 2 va despues en su
  propio commit. Y mide la apertura como siempre, antes de la primera
  operacion: Gate 0 el ciclo de tres, censo, aristas, motor, web y tsc,
  cada uno con su fichero de salida.
  Y UNA REGLA QUE ESTA VUELTA TIENE QUE RESPETAR CON LOS DIENTES
  APRETADOS, porque es la que la 81 rompio: EJECUTOR.md regla 6, COMMIT
  Y PUSH POR TRAMO, para que nada dependa de que la sesion aguante.
  Commitea al cerrar CADA tarea, no al final. La TAREA 2 de la vuelta 81
  estaba terminada y probada y casi se pierde por no tener un commit.
- TAREA 1, los registros y la correccion declarada. Es la TAREA 1 del
  encargo de la vuelta 81, que nunca se ejecuto (verificado por el
  auditor: REPORTE.md no fue tocado). (1.1) Registrar la caida de
  reporte de la vuelta 80 con su nombre, SIN volver a medirla (viene
  medida en el acta 80, seccion 4): la columna "alcanzable previo (vara
  de la cadena)" de la tabla de las 10 lecturas frescas publica dos
  celdas que contradicen la salida del instrumento que la propia columna
  nombra (docs/loop/SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt). La
  fila 27 (descubrir_necesidades_del_cliente -> traduccion_necesidades_
  cliente) dice "no" donde el instrumento imprimio YA ALCANZABLE (6
  saltos); la fila 28 (qfd_matriz -> identificar_clientes_externos_e_
  internos) dice "si, en direccion inversa" donde el instrumento
  imprimio sin camino previo. Incumple EJECUTOR.md regla 1, LA TABLA SE
  CUENTA DE SU FICHERO. (1.2) Correccion declarada en REPORTE.md con el
  texto viejo intacto delante y sin reescribirlo. (1.3) Registrar las
  seis adjudicaciones de la seccion 5 del acta 80 y las seis de la
  seccion 5 del acta 81, incluidas las dos aristas que quedan como
  observacion medida FUERA de la bolsa y que NO se escriben en OP-E-01.
  (1.4) Registrar, con su nombre, LA VUELTA 81 NO ENTREGADA: es linea de
  registro, no de racha, y asi esta adjudicada en el acta 81 seccion 7.
- TAREA 2, EL ARREGLO DEL REMEDIO, Y ES BLOQUEANTE. Sobre
  scripts/loop/tallar_cabecera_reporte.py, ya commiteado en la TAREA 0,
  y por cita de EJECUTOR.md regla 1, sin doctrina nueva. La falla, medida
  por el auditor (acta 81, seccion 4.5): el modo --tramo-cadena talla las
  30 unidades de la cabeza de la bolsa, pero la tabla del reporte que
  --comparar sabe leer (la de cuatro celdas, # | par | alcanzable |
  decision) es por construccion SOLO la de las lecturas frescas, que en
  el tramo 6 eran 10. Las otras 20 viven en una tabla hermana de tres
  celdas que el codigo ignora a proposito. Resultado: 20 AUSENTES y exit
  1 PASE LO QUE PASE, o sea un chequeo obligatorio que no puede
  aprobarse nunca, que es un chequeo que se acaba saltando. El arreglo,
  adjudicado en el acta 81 seccion 5.1:
  (2.a) DISTINTA sigue siendo ROJO, sin cambio: toda celda de
  alcanzabilidad que el reporte publique tiene que ser identica a la del
  instrumento.
  (2.b) AUSENTE deja de ser ROJO por si sola. En su lugar, el tallador
  imprime debajo de la comparacion la lista NOMINAL de las unidades no
  publicadas en esa tabla, con su cuenta, para que nada se esconda
  callado.
  (2.c) ROJO NUEVO, la fila inventada: si la tabla del reporte publica
  un numero de fila que el fichero del filtro no tiene, es ROJO y exit 1.
  CASO POSITIVO OBLIGATORIO, contra la vuelta 80, y se cita en el reporte
  con su salida: --vuelta 80 --tramo-cadena 6 --comparar
  docs/loop/REPORTE.md tiene que dar exit 1 con las filas 27 y 28
  nombradas como DISTINTA y con el texto del instrumento al lado, y tiene
  que listar las 20 no publicadas por su nombre en vez de contarlas como
  rojo. Y el caso positivo de la 2.a de la vuelta 81 se mantiene vivo:
  --vuelta 80 --tramo-cadena 6 sigue dando ALCANZABLE (6 saltos) en la
  fila 27 y SIN CAMINO PREVIO en la fila 28.
- TAREA 3, la relectura conjunta del discutible 1 de la vuelta 80,
  descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente,
  con el caso escrito del auditor (acta 80, seccion 2, D1) verificado
  contra el grafo ANTES de decidir. El caso, en corto, para que se
  verifique y no se copie: el hijo cabe entero en el paso 6 de la madre;
  la madre conserva materia propia en los otros cinco; y la senal que la
  9.6.2 declara mas fiable, los entregables, sale a favor (la madre
  entrega la lista priorizada Y traducida, dos productos, y el hijo
  entrega exactamente el segundo, que es la silueta del ejemplar 2.215).
  La vara de la cadena NO muerde: el unico camino previo sube al abuelo
  (juran_quality_by_design, identificar_clientes_externos_e_internos) y
  vuelve a bajar, y eso no es la cadena de esta madre en su propio orden.
  Y la razon escrita del reporte 80 se cae midiendo un campo: el camino
  que cita como "el establecido de la familia para la misma transicion"
  arranca en el ABUELO y no pasa por esta madre en ningun salto, y
  customer_needs_spreadsheet NO esta entre los 9 nodos_siguientes de la
  madre. Verifica las dos cosas contra dataset/nodos/*.json antes de
  decidir. Si se escribe, en LAS DOS VISTAS a la vez, con chequeo de
  escalera, correccion declarada en docs/plan/04_ENLACES.md con el texto
  viejo intacto, y recomputo (Gate 0 el ciclo de tres, motor, web y tsc)
  tras la escritura.
  Y lo que NO se hace en esta tarea, adjudicado y escrito para que no se
  improvise: descubrir_necesidades_del_cliente ->
  customer_needs_spreadsheet y curva_caracteristica_operativa ->
  distribucion_poisson NO se escriben. Estan medidas fuera de
  PASO_NODO_CALIBRADO.jsonl y OP-E-01 no decide fuera de su bolsa.
  Quedan como observacion medida para OP-E-03 o para un barrido
  posterior, y asi se registran.
- TAREA 4, la vara del tramo 6, REDUCIDA porque el auditor ya la corrio
  entera (acta 81, seccion 3), pero NO suprimida, porque EJECUTOR.md
  regla 2 no admite un acta como fuente de una cifra nueva. Corre TU los
  dos barridos con tu propio instrumento, con los pares LEIDOS del
  fichero del filtro y no tecleados: (4.a) las 10 unidades frescas del
  tramo 6 contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl SIN direccion;
  (4.b) las 10 contra docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl
  buscando la reciproca. Coteja tu tabla contra la del acta 81 seccion 3,
  que dice: 30 unidades leidas del filtro, 10 frescas, 3.388 veredictos y
  3.388 pares no dirigidos unicos, 157 unidades en la bolsa filtrada, UN
  solo par con veredicto (el 23, clase D, puesto 2560, quality, que
  apunta en el mismo sentido que la decision escrita) y CERO reciprocas.
  Si tu corrida discrepa en un digito, LA DISCREPANCIA SE DECLARA, no se
  resuelve copiando. La tabla se cuenta de su fichero.
- TAREA 5, el tramo 7 de OP-E-01, recalibrando la bolsa FRESCA antes de
  leer (el grafo no se ha movido desde el cierre de la vuelta 80, pero la
  TAREA 3 puede moverlo, y la bolsa se recalibra igual), con el filtro
  P.9.1 ensanchado, la guarda del par no dirigido y la vara de la cadena
  corridas antes de leer nada, y con la tabla de alcanzabilidad TALLADA
  por el modo --tramo-cadena en vez de tecleada, ya con el arreglo de la
  TAREA 2 dentro. Sigue por la cabeza de la bolsa, en orden de fichero y
  sin sorteo, y marca los discutibles ANTES de saber si aciertan. Del
  corte de la vuelta 80 quedaban 127 candidatos filtrados sin leer,
  medidos por el auditor hoy; el corte nuevo lo mide tu recalibracion.
- LA CABECERA DEL REPORTE SE TALLA CON --fase04 --vuelta 82 y se pega
  entera, y antes del commit de cierre --comparar docs/loop/REPORTE.md
  tiene que dar CABECERA IDENTICA AL TALLADOR, con su salida citada.
  La fila de identidad ahora lleva las dos cosas leidas de git, el commit
  del acta y el HEAD real de la apertura que sellaste en la TAREA 0, y
  cae en ROJO si sus arboles de dataset/ no coinciden.
- Con el freno delante: la racha de clase o cifra publicada esta en CERO
  y la parada de esa especie pide DOS seguidas. La de reporte esta en UNA
  y pide TRES. La escalada automatica de EJECUTOR.md regla 1 pide DOS
  tandas de reporte: hoy no ha saltado. Y una advertencia escrita en el
  acta 81 seccion 8, para que la sepas antes y no despues: SI ESTA VUELTA
  TAMPOCO ENTREGA, dos vueltas seguidas sin entregar ya no son un
  accidente, ninguna regla escrita las cubre, y el auditor lo llevara a
  PARADA por doctrina nueva necesaria. Commitea por tarea.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
