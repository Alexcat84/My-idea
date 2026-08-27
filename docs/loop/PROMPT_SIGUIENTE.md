Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

Vuelta 90 AUDITADA Y RATIFICADA (acta de la vuelta 90, ACTA_AUDITOR.md
linea 30395). OP-E-06 quedo ABIERTA Y EJECUTADA: 113 aristas escritas,
verificadas por el auditor una por una contra el diff de la union del
grafo entre las dos refs (cero borradas, cero de mas), 114 direcciones
adjudicadas con dos varas independientes y CERO discrepancias, y la
escritura probada IDEMPOTENTE. Gate 0, motor 25/25, web 80/1030, tsc y
el marcador A 551 / B 72 / C 5 / D 2.760 verdes por corrida del auditor.
La operacion que sigue es OP-E-07.

Sale UNA caida de reporte de la vuelta 90 (acta 90, seccion 3.1): la
enumeracion de los alias dice "Cinco pares" donde hay CATORCE filas y
ONCE pares alias hacia vivo, dice "4 aristas" seguido de CINCO puestos,
y omite del todo los puestos 1207 y 1535. Las aristas estan bien
escritas; la cifra estaba tecleada. La racha de reporte queda en UNA de
tres. NO hay parada.

- TAREA 1, la correccion aditiva de PENDIENTES.md sobre los tres pares
  de enlace mutuo (adjudicacion 4.1 del acta 90). La entrada escrita en
  la vuelta 90 manda 2082, 2084 y 2112 a una operacion de ENLACE MUTUO
  de dos aristas "como la seccion LAS CINCO C de 04_ENLACES.md". Medido
  por el auditor: esa seccion es de clase C (201, 215, 494, 1077 y 1240,
  los cinco C) y estos TRES SON D; el banco 9.22 dice que la figura "se
  registra C, sano con figura, no D"; el 9.22 exige DOS LINEAS DISTINTAS,
  una en cada nodo, y cada una de las tres razones nombra UNA SOLA
  LINEA (paso 4 de validacion_con_franquiciados en el 2082, paso 2 de
  gestion_responsabilidad_vicaria en el 2084, paso 1 de
  capitalizacion_adecuada_del_franquiciador en el 2112); y el segundo
  sentido lo justifican las tres con la formula "cada uno trae lo suyo",
  que es el criterio de la D y es exactamente lo que el contraste del
  puesto 2091 (clase D, en el banco) deja fijado. LA EXCLUSION DE
  OP-E-06 NO SE TOCA: sigue siendo correcta. Lo que se corrige es la
  RECOMENDACION que viaja con ella, sin borrar el texto viejo: primero
  una relectura dirigida de los tres contra el test de las dos lineas
  del 9.22; si sostiene, dos aristas cada uno MAS su correccion
  declarada de clase D a C; si no sostiene, vuelven como escalera de una
  sola direccion por la linea que su razon ya nombra. Cita el numero de
  linea del acta 90 y el del banco.
- TAREA 2, la cifra de OP-E-06 escrita entera en docs/plan/04_ENLACES.md
  (adjudicacion 4.5 del acta 90). UNA SOLA CADENA MEDIDA Y CITABLE, de
  192 a 113, con el comando de cada eslabon: los 192 con direccion
  explicita de la adjudicacion, lo que quitaron los cuatro frentes de
  dedupe, las dos re-bases (V88, V89), la reversion del 117, las dos
  adjudicaciones 4.1 y 4.2 del acta 89 que dan la V90 de 117, los 3
  excluidos por 9.22, los 114 con direccion, y el 113 ESCRITA mas 1
  YA_ESTABA mas 0 ESCALERA_ROTA. Cada eslabon con su fuente (acta,
  fichero o instrumento). Es la regla contra el descarte silencioso que
  la propia verificacion de OP-E-07 lleva escrita. Si algun eslabon no
  se puede medir hoy, se declara "a verificar" y se dice cual, no se
  rellena.
- TAREA 3, LA SEGUNDA MITAD DE LA ESCALADA, Y ES BLOQUEANTE: va ANTES
  de tocar OP-E-07. El auditor la encarga con la racha en UNA y no en
  DOS, y declara por que en la seccion 6.1 del acta 90: el remedio de la
  vuelta 90 (scripts/loop/tallar_conteo_campo.py) solo cuenta la
  distribucion de LONGITUD de un campo de un JSONL, y la caida de la
  vuelta 90 fue una cifra de COMPOSICION sobre una salida de texto, que
  ese tallador no puede tallar. Extiende el tallador (o hazle un hermano)
  para que TALLE CIFRAS DE COMPOSICION DE UNA SALIDA: dado un fichero de
  salida y un patron de clasificacion, cuenta cuantas filas caen en cada
  clase, ENUMERA LOS PUESTOS DE CADA CLASE, y coteja esa enumeracion
  contra una lista citada, marcando lo que sobra y lo que FALTA. La vara
  de si alcanza, y es dura: corrido sobre
  docs/loop/SALIDA_V90_TAREA4_ESCRITURA.txt con la clase "resuelto por
  alias", tiene que dar CATORCE filas y ONCE pares distintos, y al
  cotejarlo contra la lista que el reporte de la vuelta 90 publico
  (956, 1012, 1013, 1160, 1169, 1270, 1286, 1345, 1472, 1545, 1546)
  tiene que marcar 1207 y 1535 como AUSENTES. Si no los marca, no
  alcanza y se dice. Mecanica de ROJO igual que la de la vuelta 90: si
  no puede contar el fichero, no talla nada y sale con exit 1. Y el caso
  rojo de este instrumento SE PRUEBA POR MUTACION con
  scripts/loop/verificar_caso_rojo_por_mutacion.py, mutando una variable
  que el codigo compute, con la corrida citada en el reporte. Pulido que
  va en el mismo paquete (acta 90, seccion 1.11): cuando
  tallar_conteo_campo.py cae en rojo por un puesto inexistente, imprime
  la tabla de distribucion y despues dice "NO SE TALLA NADA"; el exit 1
  es correcto pero las palabras y la salida no dicen lo mismo, y eso se
  arregla.
- TAREA 4, EJECUTAR OP-E-07 (orden 10, estado LISTA, depende_de
  OP-E-06, que ya esta ejecutada). Son los 101 que faltan de la cosecha
  (reparto medido: core 74, environmental 12, exportacion 11, entrega 4).
  Su verificacion manda: NO se relee el par, se lee su razon, que ya
  esta escrita; si la razon tampoco dice quien es la madre, el par SALE
  y se anota por que; cada direccion extraida CITA la frase de la razon
  de la que sale; y los que salgan SE CUENTAN Y SE NOMBRAN, porque un
  descarte silencioso aqui es un enlace perdido. Lee la razon COMPLETA
  de docs/INTRA_DOMINIO_VEREDICTOS.jsonl, no la frase truncada a 200 de
  la cosecha: esa fue la leccion de la vuelta 90 y es la que dio los
  tres del 9.22. Antes de escribir nada: dedupe en los cuatro frentes de
  OP-E-06, semantica canonica de resolverId (la de
  scripts/plan/aristas_duplicadas_tras_resolver.py, que camina la cadena
  entera), y la via de OP-C-05 con su sello --antes y --despues propio
  de la vuelta. La linea base vigente es 935 entradas que sobran en 711
  nodos. Si alguna razon invoca el banco 9.22 o cualquier arreglo que no
  sea la escalera de una direccion, ese par SALE de OP-E-07 igual que
  salieron los tres de la vuelta 90, y se nombra.
- LA REGLA DE LA VUELTA 90 QUE NO SE PUEDE OLVIDAR: la escritura tiene
  que quedar IDEMPOTENTE, y lo demuestras corriendola dos veces. La
  segunda corrida tiene que dar 0 escritas, todo YA_ESTABA, y cero
  ficheros movidos en git status --porcelain -- dataset/. El auditor lo
  probo en la vuelta 90 y salio bien; en la 91 lo pruebas tu y lo citas.
- Con el freno delante: la racha de reporte esta en UNA de tres y la
  regla de las tres seguidas sigue viva; la de clase o cifra publicada
  esta en CERO, y dos seguidas de esa especie son parada. Toda cifra que
  publiques en el reporte sale del instrumento corrido en ESTA vuelta;
  ninguna se teclea, incluidas las de composicion (cuantas filas de tal
  clase, cuales puestos), que es justo la que cayo en la 90.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
