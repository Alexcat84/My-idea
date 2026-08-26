Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

El acta de la vuelta 77 esta en docs/loop/ACTA_AUDITOR.md y NO hay
parada: la racha de clase o cifra publicada queda en UNA (la parada pide
DOS SEGUIDAS) y la de reporte en UNA tanda (pide TRES). Aviso que el acta
escribe con todas las letras y que este encargo repite: UNA SOLA caida de
clase o de cifra publicada en esta vuelta ES PARADA, y una segunda tanda
seguida con caidas de reporte dispara la escalada automatica del tallador
(opcion b de la decision del fundador del 26 ago 2026).

EL CREDITO DE LA TANDA QUEDA REBAJADO: las dos caidas de reporte cayeron
FUERA de los discutibles marcados, asi que por AUDITOR.md seccion 1.2 el
tramo 3 se relee al doble (TAREA 2).

- TAREA 1, los registros y las cuatro correcciones declaradas. Ninguna
  borra texto viejo: la correccion se ANADE con el texto viejo delante y
  citado sin reescribir.
  (1.1) Registrar con su nombre la caida de CLASE de la vuelta 77 (dentro
  del marcado) y las DOS caidas de REPORTE (las dos fuera del marcado),
  tal como el acta 77 secciones 3 y 4 las describe, sin volver a
  remedirlas y citando el acta como fuente.
  (1.2) ESCRIBIR LA ARISTA QUE FALTA, con correccion declarada:
  mejora_calidad_crosby -> programa_mejora_calidad_14_pasos. La razon
  publicada para no escribirla ("los dos son miembros del mismo racimo
  declarado") es FALSA: mejora_calidad_crosby no aparece en ninguno de
  los 32 racimos de docs/RACIMOS_MIEMBROS.jsonl, solo el hijo. Y el par
  TIENE veredicto propio, puesto 2583, clase D, cuyo texto dice que
  mejora_calidad_crosby "literalmente REMITE al de catorce pasos como su
  contenido". Por el criterio adjudicado en el acta 76 y repetido en el
  encargo de la 77 (veredicto del cribado primero: A espera la fusion, D
  se escribe), se escribe. Verificalo tu contra el fichero antes de
  escribir, no te fies de este parrafo: si tu medicion no da lo mismo,
  paras y lo traes.
  (1.3) Corregir en REPORTE.md la cifra "4 de 30 tenian veredicto propio"
  de la seccion 3.3. Contado por el auditor sobre los mismos 30
  candidatos: SIETE sin direccion (puestos 1369, 2464, 1951, 2826, 223,
  1746 y 2583) y SEIS si se empareja solo en direccion madre a hijo. Los
  siete son D, asi que ninguna arista se revierte por esta via.
  RECUENTALO TU CON UN INSTRUMENTO Y DEJA EL FICHERO DE SALIDA: esta
  caida existe justamente porque esa cifra no tenia fichero que contar,
  dentro de la vuelta que estrenaba LA TABLA SE CUENTA DE SU FICHERO.
  (1.4) Corregir en REPORTE.md la etiqueta "las fusiones de fase 06" de
  la tabla de la seccion 3.2. El conteo de 15 esta bien; el nombre no:
  las siete operaciones que apartan (OP-M-01-FUSION, OP-M-02-PROG,
  OP-M-03-II, OP-M-03-III, OP-M-05-APERTURA, OP-M-05-EDIFICIO y
  OP-M-05-INDICE) llevan fase 03_FUSIONES en su ficha, y OP-M-02-PROG y
  OP-M-03-II ni siquiera estan entre las seis enrutadas a la fase 06 por
  la remision de 03_FUSIONES.md.
  (1.5) EL TOQUE UNICO DE LOS DOS IDS DE GATES, por banco 9.4. Medido por
  el auditor: dos de los 69 ids de la nomina nueva de OP-S-09,
  estructura_de_gates y estructura_gates, estan en el campo eliminar de
  OP-M-01-FUSION, que corre antes (fase 03, orden 5) que OP-S-09 (fase
  05, orden 8). Es el mismo caso que 05_SANEO.md ya declara para OP-S-01
  y OP-S-04 en su tabla de EL TOQUE UNICO. Declaralo como tercer caso de
  toque unico en 05_SANEO.md y en la nota de la ficha, y RE-MIDE la
  nomina con esos dos remitidos a OP-M-01-FUSION, publicando la cifra que
  salga sea cual sea. No fuerces el 69.
- TAREA 2, LA RELECTURA AL DOBLE DEL TRAMO 3 (credito rebajado). Cruza
  las 28 aristas escritas del tramo 3 contra docs/INTRA_DOMINIO_VEREDICTOS.jsonl
  y publica par a par, con su fichero de salida, si el cribado ya leyo
  ese par y con que clase. Cualquier par fallado A y escrito se revierte
  con correccion declarada. El auditor ya lo corrio y le dio CERO clase
  A, pero la relectura al doble es tuya y se corre igual: si tu medicion
  discrepa de la del acta, DECLARAS LA DISCREPANCIA en vez de copiar.
- TAREA 3, LA RELECTURA CONJUNTA DE LAS ONCE ARISTAS QUE LA VARA DE LOS
  VEREDICTOS A TOCA. El auditor adjudico, POR CITA y sin doctrina nueva
  (P.9 punto 1 "los enlaces corren DESPUES de las fusiones que tocan sus
  destinos", P.9 punto 2, y AUDITOR.md seccion 0 punto 3), que el filtro
  P.9.1 debe cruzar tambien los veredictos A VIVOS del cribado, tengan o
  no operacion escrita: un A sin operacion es una fusion que el plan aun
  no ha citado. Su caso y su medicion estan en el acta 77 seccion 3 (D4)
  y en docs/loop/_auditor_v77_guardaA.txt: 551 veredictos A, 187 nodos
  vivos que participan en al menos un A con otro nodo vivo, 6 de las 28
  del tramo 3 y 11 de las 79 de toda la fase 04 con un extremo ahi.
  Lo que se hace, en este orden:
  (3.1) ENSANCHA EL FILTRO P.9.1 con la vara de los A, con su caso
  positivo escrito y su fichero de salida, sin romper lo que ya aparta
  (eliminar, superviviente y nodos de RENOMBRE_CON_ALIAS).
  (3.2) VERIFICA POR TU CUENTA contra el grafo las once aristas, una a
  una, y decide con la vara par a par: cual es el A que toca, si el
  extremo escrito es el que la fusion mataria o el que sobreviviria, y si
  hay operacion que lo cubra. La mas clara es
  waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development,
  cuyo hijo tiene un A con customer_development_modelo (puesto 1052) que
  SI esta en la nomina de OP-S-09. Lo que se mueva se mueve con
  correccion declarada y recomputo de las cuatro cifras; lo que se quede,
  se queda con la razon escrita. NO revertir en bloque: once aristas no
  se borran por un barrido.
  (3.3) Deja registrado, con su fichero, cuantas de las 79 de la fase 04
  quedan tocadas por la vara despues de tu decision.
- TAREA 4, EL TRAMO 4 DE OP-E-01, y solo si las tres anteriores quedaron
  cerradas y en verde. Recalibra la bolsa antes de leer (EL INSTRUMENTO
  MANDA: no reuses PASO_NODO_CALIBRADO_FILTRADO_V77.jsonl, el grafo se
  movio con las 28 aristas del tramo 3). Corre el filtro P.9.1 YA
  ENSANCHADO CON LA VARA DE LOS A antes de leer nada. Criterio de
  lectura, sin cambio: veredicto del cribado primero (A espera la fusion,
  D se escribe); el sufijo y el racimo solo opinan cuando NO hay
  veredicto; y cuando el paso que el calibrador senala no es el que
  calza, manda tu lectura y declaras cual es el paso bueno en la razon
  (adjudicado en el acta 77, D1, por el criterio del forastero de
  AUDITOR.md seccion 3).
- LO QUE YA ESTA ADJUDICADO Y NO SE REABRE: las aristas de los
  discutibles 1, 2 y 3 de la vuelta 77 se quedan; la abstencion de
  human_error_como_sintoma -> preguntar_que_no_quien SE CONFIRMA (los dos
  extremos si estan en el mismo racimo, el par no tiene veredicto, y P.9
  punto 1 mas el criterio de prudencia del acta 76 lo cubren); y el
  PENDIENTE DE DOCTRINA que el reporte de la 77 declaraba en su seccion 6
  QUEDA DISUELTO, porque no habia dos ejemplares sino uno y ese uno lo
  cubren reglas escritas citables por numero.
- Y el renglon que esta vuelta estreno sigue vigente y se aprieta: LA
  TABLA SE CUENTA DE SU FICHERO. Toda cifra del reporte, incluidas las de
  prosa que no van en tabla, cita el fichero de salida del que sale y se
  reconstruye contando ese fichero antes de publicarse. Las dos caidas de
  esta tanda son cifras de prosa sin fichero detras.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
