Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

Vuelta 91 AUDITADA (acta de la vuelta 91, ACTA_AUDITOR.md linea 30958).
Lo medido salio verde entero por corrida propia del auditor: las ocho
cifras del grafo en dos refs con sha256 en las dos, el diff de la union
(cero borradas, 86 nuevas, y las 86 CALZAN EXACTO conjunto contra
conjunto contra las 86 ESCRITA), Gate 0, motor 25/25, web 80/1030 mas 3
skipped, tsc, el marcador A 551 / B 72 / C 5 / D 2.760, la cabecera (9
filas, 0 distintas), el desfase, la guarda de OP-C-05 (935 antes / 935
despues) y la idempotencia. La escalada de la TAREA 3 se re corrio
entera y da salida IDENTICA BYTE A BYTE, con sus tres ROJOS y sus dos
mutaciones. Los CUATRO discutibles marcados quedan CONFIRMADOS los
cuatro. La racha de reporte SE ROMPIO y vuelve a CERO.

PERO SALE UNA CAIDA DE CLASE, Y MUEVE DATO (acta 91, seccion 3.1). EL
PUESTO 1098 DE OP-E-07 TIENE UNA ARISTA ESCRITA EN EL GRAFO QUE SU
PROPIA RAZON PROHIBE. La razon del par (customer_validation_sell_phase
contra prueba_solucion_con_cliente, clase D, core) dice literalmente:
"Queda anotada UNA LINEA COMPARTIDA que no crea jerarquia porque
ninguno la expande: los dos preguntan como es el proceso interno de
aprobacion de compra, y los dos lo dicen en un solo paso". El criterio
automatico leyo la palabra "trae" de la otra mitad de la razon ("trae un
procedimiento de entrevista que el otro no tiene en ninguna forma", que
es la formula de la D, no la de madre e hijo) y le puso direccion. El
auditor lo verifico ademas sobre los pasos de los dos nodos: el paso 4
de customer_validation_sell_phase y el paso 5 de prueba_solucion_con_
cliente dicen la MISMA linea, uno cada uno, y ninguno la expande.
LA RACHA DE CLASE O CIFRA PUBLICADA QUEDA EN UNA DE DOS. DOS SEGUIDAS
SON PARADA. Si esta vuelta trae otra de esta especie, el bucle para.

Y LA CONTRAPRUEBA YA ESTA CORRIDA, para que no la repitas a ciegas: el
auditor barrio las 114 direcciones de OP-E-06 con la misma vara y solo
toco el puesto 1160, que leyo entero y CONFIRMO (ahi la jerarquia SI
esta nombrada con su paso, "dice en su paso 2, en UNA LINEA", y la
frase de linea compartida se refiere a una SEGUNDA linea distinta).
OP-E-06 NO SE REABRE y sus 113 aristas se quedan donde estan.

- TAREA 1, los registros. Deja constancia en docs/PENDIENTES.md de la
  caida del 1098 y de su correccion, sin borrar texto viejo, citando
  ACTA_AUDITOR.md (seccion 3.1 del acta 91) y BANCO_DE_TEXTOS.md linea
  1737 y siguientes (9.6.2, el test de "el hijo cabe entero dentro de UN
  paso de la madre" y el ejemplar del puesto 2.195, "no era madre e
  hijo: linea compartida y procedimiento propio a cada lado"). Cita
  numeros de linea reales, leidos por ti en esta vuelta.
- TAREA 2, LA ESCALADA DEL CRITERIO DE DIRECCION, Y ES BLOQUEANTE: va
  ANTES de tocar ninguna arista. El auditor la encarga con la racha de
  CLASE en UNA y no en DOS, y declara por que en la seccion 6.5 de su
  acta: el umbral de parada de esta especie es DOS, no tres, asi que
  esperar seria tener el remedio despues de la parada. Lo que hay que
  construir: un GUARDA para extraer_direccion_automatica (o su hermano)
  que exija LAS DOS CONDICIONES y no una sola:
  (a) que la razon traiga una MARCA DE MADRE POSITIVA, es decir una
      linea NOMBRADA con su paso o una formula de indice ("dice en su
      paso N", "en UNA LINEA", "en DOS/TRES LINEAS", "es UNA LINEA",
      "ES EL INDICE", "ENUMERA", "ORDENA", "ES LA ETAPA", "ES EL
      PROGRAMA", "MANDA", "ENUNCIA", "es un repertorio", "NOMBRA EL
      PROBLEMA", "ESCRIBE EL ENCARGO ENTERO", "es POSTURA", "MONTA EL
      MARCO", "describe las piezas", "compara los", "calcula dos
      indicadores", "la madre" nombrada literalmente), y
  (b) que la razon NO NIEGUE la jerarquia sobre esa misma linea ("no
      crea jerarquia", "ninguno la expande", "sin jerarquia").
  UN PAR QUE FALLE (a), O QUE NIEGUE POR (b) SIN TENER (a), SALE, y se
  cuenta y se nombra, que es lo que la verificacion de OP-E-07 manda.
  LA VARA DE SI ALCANZA, Y ES DURA, y son DOS casos y los dos
  obligatorios: corrido sobre las 88 razones de
  docs/plan/OP_E_07_REBASE_V91.jsonl tiene que marcar el 1098 como SALE
  y ningun otro de los 88; y corrido sobre las 114 de
  docs/plan/OP_E_06_DIRECCION_V90.jsonl tiene que dejar PASAR el 1160
  (si tumba el 1160, el guarda esta mal y se dice: seria una caida en el
  otro sentido). Si no cumple los dos, no alcanza y lo declaras.
  Mecanica de ROJO igual que la de la TAREA 3 de la vuelta 91: si no
  puede leer la razon de algun puesto, NO TALLA NADA y sale con exit 1,
  sin imprimir tabla parcial delante. Y el caso rojo SE PRUEBA POR
  MUTACION con scripts/loop/verificar_caso_rojo_por_mutacion.py, mutando
  una variable que el codigo compute y no un literal, con la corrida
  citada en el reporte.
  OJO CON LA TRAMPA QUE EL AUDITOR YA PISO Y DECLARA EN SU SECCION 6.3:
  su propia expresion regular de marca de madre marco 21 de 80 como
  sospechosas y 20 eran BUENAS, porque las formulas de madre son muchas
  y no una. Un guarda que marque de mas y se crea es peor que no
  tenerlo. Por eso las dos varas de arriba son obligatorias: la de las
  88 mide que no se te escape, y la del 1160 mide que no te pases.
- TAREA 3, LA CORRECCION DEL 1098, con correccion declarada y recomputo
  (adjudicaciones 5.1 y 5.2 del acta 91). Va DESPUES de la TAREA 2, y el
  guarda nuevo es el que tiene que senalar el 1098 antes de que tu lo
  saques a mano: si lo sacas a mano y el guarda no lo veia, el remedio
  no sirve y lo dices.
  (a) Saca el puesto 1098 de docs/plan/OP_E_07_DIRECCION_V91.jsonl (queda
      en 87 filas) y anota POR QUE sale, con la frase literal de su
      razon, en el propio fichero de salida o en su log.
  (b) RETIRA la arista customer_validation_sell_phase ->
      prueba_solucion_con_cliente de dataset/nodos/, las DOS vistas
      (nodos_siguientes de la madre y nodos_previos del hijo), con un
      instrumento que lo haga y lo imprima, no a mano. Es lo que la
      verificacion de OP-E-07 ordena ("el par sale de la cosecha"): no
      es un borrado sin regla.
  (c) Corre el ciclo de tres entero y verifica: censo IGUAL (3.853 /
      3.188 / 665), Gate 0 OK, y el diff de la union del grafo contra el
      cierre de la vuelta 91 (0691d225) tiene que dar EXACTAMENTE UNA
      borrada y CERO nuevas, y esa una tiene que ser la del 1098. Si da
      cualquier otra cosa, PARAS y lo traes.
  (d) Reescribe el ADDENDUM DE EJECUCION de OP-E-07 en
      docs/plan/OPERACIONES.jsonl con el corte nuevo: de los 88, UNO
      SALE por el banco 9.6.2 (puesto 1098, nombrado), 85 ESCRITA, 2
      YA_ESTABA, 0 ESCALERA_ROTA. estado se queda en LISTA, mismo
      criterio que OP-E-01, OP-E-04 y OP-E-06.
  (e) Prueba la IDEMPOTENCIA de la retirada: correrla dos veces tiene
      que dar 0 retiradas la segunda y cero ficheros movidos en git
      status --porcelain -- dataset/.
- TAREA 4, LA CIFRA DE OP-E-07 ESCRITA ENTERA en docs/plan/04_ENLACES.md,
  igual que la TAREA 2 de la vuelta 91 hizo con OP-E-06 y por la misma
  regla contra el descarte silencioso. UNA SOLA CADENA MEDIDA Y CITABLE:
  101 de la ficha (con su reparto core 74, environmental 12, exportacion
  11, entrega 4), menos 13 del frente 4 del dedupe (los otros tres en 0,
  los trece nombrados uno a uno), igual a 88; menos 1 que SALE por el
  banco 9.6.2 (el 1098, con su frase literal), igual a 87 con direccion;
  85 ESCRITA mas 2 YA_ESTABA (1388 y 1946, con la cadena de alias que
  los explica) mas 0 ESCALERA_ROTA. Cada eslabon con su fuente (fichero,
  linea o instrumento). Si algun eslabon no se puede medir hoy, se
  declara "a verificar" y se dice cual, no se rellena.
- LO QUE NO SE TOCA, y es explicito: OP-E-06 NO SE REABRE (la
  contraprueba ya esta corrida, acta 91 seccion 3.2). El MARCADOR no se
  toca: la clase D del 1098 es correcta y no se discute, lo que no
  sostiene es la DIRECCION. La cabecera de la vuelta 91 es una medicion
  historica cerrada y NO se retoca; la resta se vera en la apertura de
  esta vuelta.
- SI DESPUES DE LA TAREA 4 QUEDA VUELTA, la operacion que sigue en la
  fase 04 por orden del 00_INDICE. Pero NO la empieces si las tareas 1 a
  4 no estan cerradas y en verde: la prioridad de esta vuelta es dejar
  el remedio puesto y el dato limpio, no ganar aristas.
- Con el freno delante: la racha de CLASE O CIFRA PUBLICADA esta en UNA
  de DOS y DOS SEGUIDAS SON PARADA. La de reporte esta en CERO y tres
  seguidas serian parada. Toda cifra que publiques en el reporte sale
  del instrumento corrido en ESTA vuelta; ninguna se teclea. Y marca de
  verdad tus discutibles: en la vuelta 91 los cuatro marcados salieron
  confirmados y la caida estaba en el tramo que el reporte declaraba
  mecanico y sin lectura. Si una pieza tuya descansa en una regla
  automatica sobre texto, esa regla es un discutible, no una certeza.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
