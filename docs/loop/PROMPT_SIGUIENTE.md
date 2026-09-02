Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 07 ADUANA (en la puerta de
cerrarse). RAMA pasada-unica. MODO DE EJECUCION CONTINUA (AUDITOR.md
seccion 3), en REGIMEN COMPLETO, con las guardas obligatorias por
operacion.

La decision del fundador que desbloquea esta vuelta esta en
docs/loop/paradas/2026-09-02-aduana-vector-y-a13-DECISION.md, y la parada
entera en docs/loop/paradas/2026-09-02-aduana-vector-y-a13.md. En
resumen: PREGUNTA 1 por el CAMINO 1 con precision de sede, PREGUNTA 2 por
la OPCION 2, y CON LAS DOS LA FASE 07 CIERRA.

- TAREA 1, APLICAR LAS DOS DECISIONES.
  (1.a) EL CANDIDATO SE EMBEBE APARTE. scripts/integrar_packs.py gana un
  PASO DE EMBEBIDO PREVIO A LA COPIA: una llamada a Voyage POR CANDIDATO
  con el texto del propio candidato. La decision dice por que se puede, y
  esta comprobado en el codigo antes de encargartelo: NO HACE FALTA EL
  GRAFO PARA UN VECTOR. En scripts/build_semantic_index_voyage.py la
  costura ya existe y son dos piezas, _embeber(textos, input_type) (linea
  65), que toma una lista de textos sueltos y devuelve sus vectores en el
  mismo orden, y texto_nodo(n) (linea 56), que arma el texto desde el
  dict del nodo. NINGUNA DE LAS DOS LEE master_graph.json: lo que lee el
  grafo es main(). El texto del candidato sale de su propio fichero del
  pack. Decide con criterio propio si reusas _embeber importandola (es
  privada por el guion bajo, asi que si la reusas dilo y di por que) o si
  la factorizas a una funcion publica; lo que NO se hace es duplicar la
  llamada HTTP a mano.
  LA PUERTA NO SE MUEVE: sigue bloqueando EN LA INSERCION, en el
  shutil.copy2 de la linea 255, como la ficha OP-A-02 manda y como la
  vuelta 147 la cableo. Esto anade un paso antes, no mueve la puerta
  despues.
  LA DECLARACION EN EL DOCSTRING: integrar_packs.py --ejecutar es
  HERRAMIENTA DE SESION CON CREDENCIAL. Corre SOLO en sesiones post
  campaña, con humano presente y el .env disponible. JAMAS DENTRO DEL
  BUCLE AUTONOMO. Escrito en su docstring con esas palabras, no en un
  comentario suelto.
  EL FALLO RUIDOSO: invocada sin la clave, falla RUIDOSAMENTE NOMBRANDO
  LO QUE FALTA (la variable que falta y el fichero donde vive), no calla
  ni degrada ni sigue a medias.
  CASO POR MUTACION SOBRE COPIA, Y SIN RED: el fallo ruidoso SE PRUEBA
  SIN LLAMAR A VOYAGE, o sea sin gastar credencial y sin salir a la red,
  que es lo unico que el bucle puede probar por si mismo. La mutacion va
  sobre una variable QUE EL CODIGO COMPUTE, no sobre un literal (EJECUTOR
  regla 1, EL CASO ROJO SE PRUEBA POR MUTACION), sobre copia en memoria,
  y dataset/ queda IDENTICO antes y despues, comprobado por el propio
  arnes. Lo que NO se puede probar en el bucle (que la llamada real a
  Voyage devuelve un vector util) se DECLARA como no probado aqui, con su
  motivo, en vez de darlo por bueno callando.
  (1.b) LA VERIFICACION 3 DE OP-A-01, REESCRITA POR CORRECCION DECLARADA,
  con el texto de la decision y sin borrar el texto viejo. Hoy dice
  literal, leido de docs/plan/OPERACIONES.jsonl: "Gate 0 rechaza un nodo
  cuyo segundo libro no aparece en ningun paso", y es la tercera de sus
  tres verificaciones. SU MITAD MECANICA QUEDA COMO ESTA (el segundo
  libro contra la nomina adjudicada, instalada y mordiendo). SU MITAD
  SEMANTICA SE REMITE A LA PUERTA A2.6: la vecindad por contenido sobre
  el indice es la lectura ejecutable. Y SE CITA LA MEDICION DEL ACTA 146:
  la lectura literal dispara 9 DE 9 sobre nodos adjudicados enteros, o
  sea que rechazaria los ocho ya adjudicados porque ningun paso del
  catalogo nombra su libro: INEJECUTABLE.
  (1.c) EL CIERRE DE LA FASE 07, MEDIDO CONTRA SU VARA, no declarado de
  palabra. La vara de codigo hoy da 9 controles declarados / 7 distintos
  / 8 instalados y mordiendo enteros / 1 instalado solo en su mitad
  mecanica (A1.3) / 0 no instalados, y dice sola "LA FASE NO SE CIERRA
  CONTRA ESTA VARA, y lo que le falta va nombrado: A1.3 (solo su mitad
  mecanica)". Con la 1.b aplicada, la vara se RE CORRE y su salida se
  pega: si sigue diciendo que no cierra, PARAS Y LO TRAES en vez de
  cerrarla a mano. El rotulo de A1.3 en la vara tiene que reflejar lo que
  la decision dispone, no seguir diciendo lo de antes.
- TAREA 2, LOS SEIS PUNTOS DE LA SECCION 7 DEL ACTA 147, tal como el
  auditor los dejo medidos:
  (2.1) LA GUARDA DE LA NOMINA, CERRADA POR EL LADO DEL COMMIT (su
  4.4.a): que un movimiento que llega YA COMMITEADO no pueda pasar
  inadvertido, que es el agujero que su segunda mutacion encontro.
  Criterio libre, FIN NO NEGOCIABLE, con su caso rojo por mutacion sobre
  variable computada.
  (2.2) LA GUARDA DE CIFRAS, EL CAMINO POR CONJUNTO (su 4.4.b): que un
  valor no pueda cuadrar contra la etiqueta VECINA cuando las dos
  comparten casi todas sus palabras.
  (2.3) LA VARA, UNA UNIDAD MAS (su 4.4.c): un control con una parada
  abierta encima no puede publicarse con el mismo rotulo que uno que
  corre. Es la misma cura que la 147 le dio a A1.3.
  (2.4) LA SALIDA AUDITABLE DEL FALSO POSITIVO de la guarda de ausencias
  (su 3.15): un bloque de exencion declarada para la frase que no afirma
  nada sobre el repositorio, o la frase vieja pegada al lado de la nueva.
  NUNCA UNA REESCRITURA SIN RASTRO.
  (2.5) LA LETRA DE VIEJAS (su 3.5): decir en la regla que lo que exige
  es SUJETO CONGELADO, y no un plazo de una vuelta, porque el plazo era
  el medio y no el fin.
  (2.6) LAS CORRECCIONES 27 Y 28, POR ADICION: las dos cifras falsas del
  auditor en su acta 146, el SEIS de las coladas que son CINCO y las DOCE
  lineas de calibracion que son SIETE, con la medicion de hoy delante y
  SIN BORRAR EL TEXTO VIEJO.
- TAREA 3, SEGUIR EL ORDEN ESCRITO, EN MODO CONTINUO: OP-S-12 AL FINAL DE
  LA PASADA, por la atadura 2 del indice y porque las cinco mesas la
  nombran en su bloquea_a, y despues LA FASE 08 entera con su criterio de
  HECHO. Entre fases, el ciclo de Gate 0 y las tres suites en verde.
  La campana NO esta consumada hasta ahi, y EL MERGE NO SE PIDE NI SE
  HACE: es del fundador y solo suyo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
