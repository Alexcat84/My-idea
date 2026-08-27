Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

El acta de la vuelta 80 esta en docs/loop/ACTA_AUDITOR.md desde la linea
24049. Resultado: CERO caidas de clase y CERO de cifra publicada (todo lo
medible se reprodujo al digito por corrida propia del auditor), UNA caida
de reporte fuera del marcado, y NINGUNA condicion de parada cumplida. La
racha de clase o cifra publicada sigue en CERO; la de reporte queda en UNA
tanda. El credito de la tanda queda REBAJADO, y eso es lo que dispara la
TAREA 4 de abajo.

- TAREA 1, los registros y la correccion declarada. (1.1) Registrar la
  caida de reporte de la vuelta 80 con su nombre, SIN volver a medirla (ya
  viene medida en el acta 80, seccion 4): la columna "alcanzable previo
  (vara de la cadena)" de la tabla de las 10 lecturas frescas publica dos
  celdas que contradicen la salida del instrumento que la propia columna
  nombra (docs/loop/SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt). La
  fila 27 (descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente)
  dice "no" donde el instrumento imprimio YA ALCANZABLE (6 saltos); la fila
  28 (qfd_matriz -> identificar_clientes_externos_e_internos) dice "si, en
  direccion inversa" donde el instrumento imprimio sin camino previo.
  Incumple EJECUTOR.md regla 1, LA TABLA SE CUENTA DE SU FICHERO. (1.2)
  Correccion declarada en REPORTE.md con el texto viejo intacto delante y
  sin reescribirlo. (1.3) Registrar las seis adjudicaciones de la seccion 5
  del acta 80, incluidas las dos aristas que quedan como observacion medida
  FUERA de la bolsa y que NO se escriben en OP-E-01.
- TAREA 2, EL REMEDIO, Y ES BLOQUEANTE, en dos piezas, las dos sobre
  scripts/loop/tallar_cabecera_reporte.py y las dos por cita de EJECUTOR.md
  regla 1, sin doctrina nueva.
  (2.a) LA TABLA DEL TRAMO SE TALLA, NO SE TECLEA. Que el tallador gane un
  modo que lea la salida del filtro de la vuelta
  (SALIDA_V<N>_TRAMO<K>_FILTRO_P91_GUARDA_CADENA.txt) y emita la tabla de
  las unidades leidas con la columna de alcanzabilidad TALLADA de ese
  fichero: por cada unidad, ALCANZABLE con su numero de saltos, o SIN
  CAMINO PREVIO, con la misma mecanica de ROJO que las demas filas (si no
  puede leer el fichero o una unidad, no talla nada y sale con exit 1) y
  con --comparar cotejando esa tabla contra REPORTE.md celda por celda.
  LA COLUMNA CONTESTA UNA SOLA PREGUNTA, la que su titulo dice: si la
  lectura quiere decir ademas si el camino es o no la cadena propia de la
  madre, eso va en una columna APARTE con su propio titulo, nunca mezclado
  en la de alcanzabilidad (es la distincion que el acta 79 dejo escrita:
  alcanzable no es lo mismo que encadenado). CASO POSITIVO OBLIGATORIO
  contra la vuelta 80: la tabla tallada tiene que dar ALCANZABLE (6 saltos)
  en la fila 27 y SIN CAMINO PREVIO en la fila 28, o sea exactamente lo
  contrario de lo que el reporte de la 80 publico, y esa corrida se cita en
  el reporte con su salida.
  (2.b) LA FILA DE IDENTIDAD GANA EL HEAD REAL DE LA APERTURA. Hoy el
  tallador publica como commit de apertura el commit del acta de la vuelta
  anterior, y en la vuelta 80 el HEAD real al abrir NO era ese (era
  3cdf90d1, el commit de la decision del fundador, que entro entre el acta
  y la primera tarea; medido en el acta 80, seccion 1.8, y esa vez fue
  inocuo porque los tres ficheros del commit intermedio eran de docs/).
  Que el ejecutor selle git rev-parse HEAD ANTES de la primera operacion en
  una salida propia de la vuelta, y que el tallador talle la fila de
  identidad con las DOS cosas leidas de git: el commit del acta y el HEAD
  real de la apertura; y que salga en ROJO si el arbol de dataset/ de los
  dos commits no coincide, porque entonces las cifras de apertura no son
  las del commit que la fila nombra. CASO POSITIVO OBLIGATORIO contra la
  vuelta 80: los dos hashes distintos (bc9cde6f y 3cdf90d1) y VERDE, porque
  sus arboles de dataset/ son iguales.
- TAREA 3, la relectura conjunta del discutible 1 de la vuelta 80,
  descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente, con
  el caso escrito del auditor (acta 80, seccion 2, D1) verificado contra el
  grafo ANTES de decidir. El caso, en corto, para que se verifique y no se
  copie: el hijo cabe entero en el paso 6 de la madre; la madre conserva
  materia propia en los otros cinco; y la senal que la 9.6.2 declara mas
  fiable, los entregables, sale a favor (la madre entrega la lista
  priorizada Y traducida, dos productos, y el hijo entrega exactamente el
  segundo, que es la silueta del ejemplar 2.215). La vara de la cadena NO
  muerde: el unico camino previo sube al abuelo (juran_quality_by_design,
  identificar_clientes_externos_e_internos) y vuelve a bajar, y eso no es
  la cadena de esta madre en su propio orden. Y la razon escrita del
  reporte 80 se cae midiendo un campo: el camino que cita como "el
  establecido de la familia para la misma transicion" arranca en el ABUELO
  y no pasa por esta madre en ningun salto, y customer_needs_spreadsheet NO
  esta entre los 9 nodos_siguientes de la madre. Verifica las dos cosas
  contra dataset/nodos/*.json antes de decidir. Si se escribe, en LAS DOS
  VISTAS a la vez, con chequeo de escalera, correccion declarada en
  docs/plan/04_ENLACES.md con el texto viejo intacto, y recomputo (Gate 0
  el ciclo de tres, motor, web y tsc) tras la escritura.
  Y lo que NO se hace en esta tarea, adjudicado y escrito para que no se
  improvise: descubrir_necesidades_del_cliente -> customer_needs_spreadsheet
  y curva_caracteristica_operativa -> distribucion_poisson NO se escriben.
  Estan medidas fuera de PASO_NODO_CALIBRADO.jsonl y OP-E-01 no decide
  fuera de su bolsa. Quedan como observacion medida para OP-E-03 o para un
  barrido posterior, y asi se registran.
- TAREA 4, la relectura al doble del TRAMO 6 por el credito rebajado
  (AUDITOR.md seccion 1.2: la caida cayo fuera de los discutibles
  marcados). El tramo 6 son las 2 aristas escritas en la vuelta 80
  (curva_caracteristica_operativa -> distribucion_binomial y
  desarrollo_de_controles_de_proceso -> bucle_retroalimentacion_control).
  Barrido 1: las 2 contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl sin
  direccion. Barrido 2: las 2 contra la bolsa filtrada de la vuelta 80
  (docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl) buscando la reciproca.
  Y como la tanda es corta, la relectura al doble alcanza tambien a las 7
  NO ESCRITAS del tramo 6: cruza las 7 contra el archivo sin direccion y
  declara si alguna trae un veredicto que contradiga la razon escrita. Las
  tres tablas CONTADAS DE SU FICHERO.
- TAREA 5, el tramo 7 de OP-E-01, recalibrando la bolsa FRESCA antes de
  leer (el grafo se movio con las 2 escrituras del tramo 6 y con lo que la
  TAREA 3 decida), con el filtro P.9.1 ensanchado, la guarda del par no
  dirigido y la vara de la cadena corridas antes de leer nada, y con la
  tabla de la TAREA 2.a tallada en vez de tecleada. Sigue por la cabeza de
  la bolsa, en orden de fichero y sin sorteo, y marca los discutibles
  ANTES de saber si aciertan.
- Con el freno delante: la racha de clase o cifra publicada esta en CERO y
  la parada de esa especie pide DOS seguidas. La de reporte esta en UNA y
  pide TRES. La escalada automatica de EJECUTOR.md regla 1 pide DOS tandas
  de reporte: hoy no ha saltado, y la TAREA 2 se encarga igual porque la
  caida cayo encima de una tabla que un instrumento ya imprime.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
