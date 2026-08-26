Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

La decision del fundador que desbloquea esta vuelta esta en
docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md: remedio
(c) como regla inmediata, ya escrita en EJECUTOR.md regla 1 como LA
TABLA SE CUENTA DE SU FICHERO, con la extension del tallador (opcion b)
como ESCALADA AUTOMATICA si la racha vuelve a DOS. Sin cambio de
modelos.

- TAREA 1, los registros y las correcciones declaradas. (1.1) Registrar
  las dos caidas de reporte de la vuelta 76 con su nombre, y la del
  auditor de la 75. (1.2) Corregir en REPORTE.md la frase del discutible
  2 sobre RACIMOS_MIEMBROS.jsonl, con el texto viejo delante y sin
  reescribirlo, y con la fila de la seccion 1.4 citada al lado. (1.3)
  Corregir scripts/loop/vuelta76_relectura_9_6_1.py: o filtra deprecado
  de verdad, o su docstring y el reporte dejan de decir vivos; y
  re-publicar la tabla CONTADA DEL FICHERO DE SALIDA, sea cual sea la
  cifra que salga. (1.4) Anadir a la etiqueta del instrumento de
  OP-E-02 su definicion: miembros con nodo vivo TRAS RESOLVER ALIAS,
  porque 38 de los 171 estan deprecados y solo llegan a vivos por esa
  via.
  (1.5) LLEVAR LA NOMINA DE OP-S-09 A SU FICHA, POR INSTRUMENTO, para
  tapar el agujero que el acta 76 midio: hoy la ficha tiene nodos [],
  eliminar [] y superviviente null, y sus 53 familias y 125 nodos vivos
  viven en prosa, asi que el filtro P.9.1 no puede verla jamas.
  AVISO MEDIDO ANTES DE ENCARGARLO, para que no lo descubras a mitad:
  docs/plan/05_SANEO.md NO trae la lista de los 125 ids. Trae el
  CRITERIO (35 familias por sufijo numerico, 12 por particulas, 6 por
  orden de palabras, 0 por sinonimo puro), las CIFRAS (53 familias, 125
  nodos vivos) y los ids de solo las CUATRO familias mayores. Asi que la
  nomina se RECOMPUTA del grafo aplicando ese criterio escrito, y la
  pagina es la VARA contra la que se comprueba: si tu recomputo no da 53
  familias, lo declaras en vez de forzarlo, y recuerda que la propia
  ficha ya lleva un delta declarado (el auditor dio 123 nodos y el
  recomputo 125).
  DONDE ESCRIBIRLOS, y es la parte que hay que hacer con cuidado: el
  filtro P.9.1 (scripts/loop/vuelta76_op_e01_tramo2_filtrar.py) cruza
  HOY solo el campo eliminar. Pero OP-S-09 es RENOMBRE_CON_ALIAS: sus
  nodos NO se eliminan, se renombran conservando alias, asi que meterlos
  en eliminar haria que la ficha diga algo falso. Escribelos en el campo
  nodos, que es su sitio verdadero, con correccion declarada y el conteo
  citado, Y ENSANCHA EL FILTRO para que lea tambien nodos en las
  operaciones de tipo RENOMBRE_CON_ALIAS, con su caso positivo en las
  dos direcciones. Asi el filtro la ve desde esta vuelta, que es lo que
  la decision pide, sin que la ficha mienta. Si al ejecutarlo ves que
  esto choca con una regla escrita, paras y lo traes.
  (1.6) ESTRENAR EL RENGLON LA TABLA SE CUENTA DE SU FICHERO en el
  reporte de esta vuelta y CITARLO: cada tabla del reporte con el
  fichero de salida del que sale, reconstruida contando ese fichero
  antes de publicarla.
- TAREA 2, la relectura al doble del tramo 2 (la manda AUDITOR.md
  seccion 1.2 porque la segunda caida cayo fuera del marcado), y con la
  vara que esta parada encontro: cruzar las 26 aristas del tramo 2
  contra INTRA_DOMINIO_VEREDICTOS.jsonl y publicar, par a par, si el
  cribado ya habia leido ese par y con que clase. Cualquier par que el
  cribado haya fallado A y este escrito, se revierte con correccion
  declarada.
- TAREA 3, el tramo 3 de OP-E-01, recalibrando la bolsa antes de leer
  (el grafo se movio otra vez), con el filtro P.9.1 corrido antes de
  leer nada, y con el criterio adjudicado: veredicto del cribado
  primero, sufijo solo cuando no hay veredicto.
- Con el freno nuevo delante: la racha de reporte vuelve a cero al
  relanzar, pero la regla de las tres seguidas sigue viva; y la de clase
  o cifra publicada esta en CERO, no en una.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
