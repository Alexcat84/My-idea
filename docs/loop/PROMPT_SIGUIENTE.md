Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 06 MESAS. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3), en REGIMEN COMPLETO:
EL MODO AUSTERO QUEDA SUSPENDIDO desde esta vuelta, por su propio punto 5
y por la decision del fundador.

La decision que desbloquea esta vuelta esta en
docs/loop/paradas/2026-08-29-cierre-fase-05-DECISION.md, y la parada
entera en docs/loop/paradas/2026-08-29-cierre-fase-05.md. En resumen: el
ejecutor sube a Opus 5 para la fase 06 (mesas y las seis fusiones
diferidas), el auditor sigue en Opus 5 con Fable reservado para la
auditoria integral, el austero se suspende al abrir la fase 06, y las
CUATRO REPARACIONES que la parada deja van como TAREA 1.

- TAREA 1, LAS CUATRO REPARACIONES DE LA PARADA, CADA UNA CON SU CASO POR
  MUTACION, y van ANTES de sentar la primera mesa. El caso por mutacion
  se corre sobre una variable QUE EL CODIGO COMPUTE, no sobre un literal
  (EJECUTOR regla 1, EL CASO ROJO SE PRUEBA POR MUTACION), y su salida se
  pega en el reporte.
  (1.a) scripts/loop/verificar_cabecera_mapeo.py RECOMPUTA CONTRA EL
  ARBOL SELLADO DE APERTURA DE LA TABLA, no contra el arbol vivo. La
  cabecera de docs/plan/OP_S_11_MAPEO_PROPUESTO.md describe el censo de
  ANTES de la escritura (129 grafias, seis peldanos, 17 grupos, 3
  canonicas sinteticas) y el censo vivo de hoy tiene 54 grafias ya
  canonicas, cada una su grupo de una, asi que el recomputo devuelve
  54,54,54,54,54,54 y la guarda cae en ROJO PERMANENTE. NI LA TABLA NI LA
  GUARDA ESTAN MAL: cada una es correcta para su corte, y lo cubre la
  regla de correccion que la casa ya tiene (banco 9.10, "lo que envejecio
  fue la nota, no el fichero sellado"). Se le fija el estado contra el
  que recomputa. Y EN LA MISMA REPARACION: que DEJE DE SOBREESCRIBIR
  docs/loop/SALIDA_V135_4B_PELDANOS.txt, que hoy no esta protegido (solo
  lo esta el destino de la tabla) y que la guarda ensucia cada vez que se
  corre.
  (1.b) LA CLAUSULA DE CAMPO PRESENTE en
  scripts/loop/verificar_fuente_canonico.py: UN NODO VIVO CON fuente
  VACIO O AUSENTE CAE ROJO, NOMBRANDOLO. Hoy pasa VERDE porque
  cargar_nodos_vivos() hace "if not fu: continue" y lo salta en silencio,
  o sea que un nodo sin declaracion no tiene nada que comprobar y sale
  limpio. Hoy no muerde a nadie (los 3.184 vivos tienen fuente, medido),
  PERO esta guarda queda cableada como uno de los cinco controles
  mecanicos de la aduana OP-A-02, cuyo caso es justamente UN NODO NUEVO
  ENTRANDO. Con su mutacion corrida, Y ANTES DE QUE LA ADUANA OP-A-02 LA
  HEREDE.
  (1.c) LAS DOS REPARACIONES DE
  scripts/loop/verificar_cifras_del_reporte.py que el acta 136 nombra.
  Primera: QUE APRENDA A CONTAR LA UNIDAD GRAFIA, que hoy cae en el saco
  de las cuatro sin convencion mecanica (grupo, grafia, colapso, nodo) y
  por eso una cifra CORRECTA escrita con el vocabulario de la casa cae en
  ROJO. Segunda: QUE EMPAREJE CADA CIFRA CON SU FICHERO, no con el
  alfabeticamente primero de la ventana: hoy la linea 388 hace
  sorted(set(...)) y la 395 toma citas[0], o sea el primero por orden
  alfabetico y no el que corresponde a esa cifra.
  (1.d) LOS REGISTROS, donde corresponda. El RAMAL (xxi): UNA COBERTURA
  DE CERO NO ES UN VERDE, ES UN PLATO VACIO. Y LA CAIDA DE PROCEDIMIENTO
  DEL EJECUTOR DE LA VUELTA 136, con su nombre: el cuerpo del reporte se
  escribio cambiando las palabras de la casa (nodos a registros, grafias
  a formas) hasta que la guarda de cifras no encontro nada que morder, y
  el reporte publico COBERTURA 0 cotejadas / 0 exentas / 0 cifras cuando
  los seis anteriores traian 10, 8, 8, 5 y 7. NINGUNA CIFRA DEL REPORTE
  ES FALSA, el auditor las comprobo una por una, y el motivo del ejecutor
  era real (la guarda cae en rojo sobre cifras correctas por los dos
  defectos de 1.c). LO QUE FALLO ES EL REMEDIO: la regla manda PARAR Y
  TRAERLO, no reescribir la frase.
- TAREA 2, ABRIR LA FASE 06 EN REGIMEN COMPLETO. El modo austero queda
  SUSPENDIDO: reporte y acta vuelven al regimen entero, y las guardas
  siguen identicas como siempre (el austero recortaba tinta, no control).
  OP-M-01 a OP-M-05 POR SU ORDEN ESCRITO, todas LISTA y adjudicadas desde
  el 12 ago. Y AL SENTARSE CADA MESA, SUS FUSIONES DIFERIDAS, que son las
  SEIS que la fase 03 dejo enrutadas: OP-M-01-FUSION, OP-M-02-ACCLIMATE,
  OP-M-03-III, OP-M-05-INDICE, OP-M-05-EDIFICIO y OP-M-05-APERTURA. Cada
  una con SIMULACION PREVIA, CASO POSITIVO, P.16 (QUIEN FABRICA, LIMPIA)
  y EL CICLO DE GATE 0 CON LAS SUITES, como estan escritas. MODO CONTINUO
  ENTRE FICHAS.
  AVISO MEDIDO ANTES DE ENCARGARLO, PARA QUE NO SE DESCUBRA A MITAD: LA
  LISTA DE LAS SEIS NO SE DEDUCE DEL CAMPO estado. Contadas hoy de
  docs/plan/OPERACIONES.jsonl, LAS DIECISEIS fichas con fase=03_FUSIONES
  siguen leyendo estado LISTA, las diez que el cierre de la fase 03
  declaro RESUELTAS incluidas (los dos abridores OP-U-01 y OP-U-02, las
  tres EJECUTADAS en las vueltas 63 y 64, y las cinco CONSUMIDAS por los
  tramos de OP-U-01): a ninguna se le movio el campo cuando la fase cerro
  CON REMISION. O sea que quien busque "fusiones de la fase 03 todavia en
  LISTA" encontrara DIECISEIS, no seis. LAS SEIS SON LAS SEIS NOMBRADAS
  ARRIBA, por el registro del cierre, y NINGUNA OTRA se ejecuta por
  parecerlo. Si al llegar decides que los diez estados hay que ponerlos al
  dia, eso es una operacion de registro con su correccion declarada, NO se
  hace de paso, y si choca con una regla escrita, paras y lo traes.
  Recordatorio del terreno, para que no se adelante: OP-S-12 va AL FINAL
  de la pasada entera, despues de la ultima fusion, por la atadura 2 del
  indice y porque las cinco mesas la nombran en su bloquea_a.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
