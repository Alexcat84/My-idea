Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE EJECUCION
CONTINUA (AUDITOR.md seccion 3), en REGIMEN COMPLETO, con las guardas
obligatorias por operacion.

LA FASE 07 ADUANA QUEDA CERRADA por adjudicacion 3.12 del acta 149, sobre la
letra de la decision del fundador del 2 sep 2026 ("Con las dos, la fase 07
CIERRA") y con la vara de codigo en 9 de 9 enteros, sostenida por mutacion
propia del auditor. No la vuelvas a abrir ni la vuelvas a discutir: registrala
como cerrada y sigue.

LA FASE 08 NO SE CIERRA EN ESTA VUELTA Y NO SE INTENTA: tres de sus cinco
puntos transversales piden la credencial del .env, que esta fuera del repo
mientras el bucle corra. Eso quedo adjudicado (acta 149, 3.10) y no se
readjudica. Lo que SI se hace de la fase 08 es su OTRA mitad, la tabla POR
FASE, que no pide ni una credencial. Va en la TAREA 4.

- TAREA 1, REGISTROS DEL ACTA 149.
  (1.a) EL ACTA 149 ESTA EN docs/loop/ACTA_AUDITOR.md. Registra sus
  adjudicaciones en docs/plan/CORRECCIONES_A_APLICAR.md como R.29, POR ADICION
  y sin borrar un solo texto viejo: los nueve discutibles adjudicados a favor
  (con reserva en el 2, el 4 y el 5), las dos preguntas contestadas, el cierre
  de la fase 07, las dos caidas del ejecutor (expediente 4.2 e incumplimiento
  de encargo 4.3), la de la casa (4.5) y las dos del auditor (4.6.a de
  procedimiento y 4.6.b de cifra).
  (1.b) LA CORRECCION 30, LA VERIFICACION 4 DE OP-S-12, POR ADICION Y CON EL
  RASTRO DELANTE. La ficha de OP-S-12 exige "el numero total de entradas baja
  en exactamente 1.056" y bajo 925. NO es contradiccion y NO se resuelve
  borrando: se escribe la correccion declarada con la cifra vieja intacta, su
  corte (11 ago 2026) y su universo (3.521 vivos), y con el rastro que el
  auditor midio y que TIENES QUE REPRODUCIR CON INSTRUMENTO PROPIO antes de
  escribirlo: docs/plan/ARISTAS_DUPLICADAS.jsonl tiene TREINTA versiones en
  git; la primera (af467eb1) da 1.015 grupos / 802 nodos / 1.056 sobran, o sea
  que la evidencia de la ficha era fiel a su corte; la de HEAD (d6341ebe) da
  898 / 711 / 935; y de esas 935, DIEZ viven sobre nodos hoy deprecados, con lo
  que quedan 925 sobre vivos, el mismo numero que retiro la operacion. Si tu
  medicion no reproduce alguna de esas cifras, LA DECLARAS y no la copias
  (EJECUTOR.md 2).
  (1.c) EL ESTADO DE OP-S-12 PASA A HECHA, Y SOLO DESPUES DE LA 1.b. Hoy es la
  unica de las diez de 05_SANEO que sigue en LISTA despues de haberse
  ejecutado, y eso es la caida de expediente 4.2. El orden no es negociable
  (acta 149, 3.14): primero la correccion de la verificacion 4, entonces el
  estado. Un estado en HECHA con una cuenta abierta encima es un verde sobre
  una pregunta abierta. El esquema NO se toca: 71 fichas, un solo esquema, 18
  claves, comprobado despues.
  (1.d) EL HALLAZGO DEL INDICE SEMANTICO VA A docs/PENDIENTES.md como trabajo
  de la sesion con credencial, con la medicion de hoy y no con la de nadie:
  3.521 ids en el indice, 3.169 vivos, 18 vivos SIN VECTOR nombrados uno a uno,
  y 370 ids que ya no estan vivos, que el auditor midio y son 370 DEPRECADOS y
  CERO FANTASMAS. Anade lo que el auditor verifico en el codigo: main() de
  scripts/build_semantic_index_voyage.py reconstruye la lista ids desde cero
  con los no deprecados, asi que una corrida completa arregla los 18 y los 370
  en la misma pasada.

- TAREA 2, OP-C-05, Y ES BLOQUEANTE. VA ANTES QUE TODO LO DEMAS DEL TRABAJO.
  ES LA OPERACION QUE ESTA VUELTA EXISTE PARA EJECUTAR. Su ficha esta en
  docs/plan/OPERACIONES.jsonl: fase 00_CODIGO, tipo GUARDA, orden 7,
  depende_de ["OP-S-12"] y nada mas. Esa dependencia SE CUMPLIO en la vuelta
  148, asi que la operacion esta desbloqueada desde el commit a34328b2. El
  encargo de la 148 salto de OP-S-12 a la fase 08 sin pasar por ella y eso fue
  un hueco de la casa (acta 149, 4.5): queda reparado aqui.
  POR QUE AHORA Y NO ANTES, con la letra de su propia nota: "SE ENCIENDE
  DESPUES DEL SANEO FINAL: encenderla antes para el trabajo, porque el grafo de
  hoy la falla 1.056 veces y eso NO es una regresion, es el estado conocido.
  Una limpieza sin guarda se deshace sola". Las 925 entradas que la 148 retiro
  no tienen hoy quien las defienda: esta guarda es quien.
  (2.a) LA GUARDA: ninguna lista de aristas puede tener dos entradas que
  RESUELVAN al mismo destino. RESUELVE, no compara literal, y la ficha explica
  por que con su cifra: las entradas duplicadas son todas distintas como texto
  y una guarda literal daria verde sobre todas. Se cablea en el ciclo de Gate 0
  como las demas guardas de la aduana, no en un script suelto.
  (2.b) LA LISTA BLANCA, POR EVIDENCIA Y NO POR EXCEPCION. Esta escrita desde
  el 12 ago 2026 y nace de un hueco real: OP-E-05 escribe cuatro aristas en los
  dos sentidos A PROPOSITO. La regla de la escalera vale para escaleras, no
  para enlaces mutuos: en una escalera la vuelta es una instruccion falsa; en
  un enlace mutuo cada direccion expande UNA LINEA DISTINTA del otro nodo, y
  quitar una borra un procedimiento. Cada entrada de la lista blanca CITA SU
  LECTURA: una entrada sin su C del 9.22 detras no es una excepcion, es un
  agujero.
  (2.c) LAS SIETE VERIFICACIONES DE LA FICHA, UNA A UNA Y CADA UNA CON SU
  SALIDA PEGADA. Estan escritas en su campo verificacion y no las resumo aqui:
  las lees de la ficha y las contestas en ese orden. Ninguna de las siete pide
  credencial ni sale a la red. Las dos que mandan sobre las demas: el CASO
  POSITIVO (se mete a mano [destino, alias_de_destino] en una copia y la guarda
  TIENE que fallar nombrando nodo, campo y destino; si pasa, la guarda no
  sirve) y el CASO POSITIVO DE LA LISTA BLANCA (se mete a mano una arista
  bidireccional que NO este en la lista y la guarda TIENE que fallar; si pasa,
  la lista blanca esta abierta de mas).
  (2.d) LAS GUARDAS DE SIEMPRE: simulacion previa sobre copia en memoria, el
  caso rojo POR MUTACION SOBRE VARIABLE COMPUTADA y no sobre un literal
  comparado consigo mismo, dataset/ identico antes y despues comprobado por el
  propio arnes, y el ciclo entero de Gate 0 mas las tres suites en verde
  despues.
  (2.e) EL ESTADO DE OP-C-05 SE MUEVE CUANDO SUS SIETE VERIFICACIONES ESTEN
  CONTESTADAS, no antes, y con el mismo criterio que la 1.c.
  SI EL TEXTO DE LA FICHA NO ALCANZA PARA EJECUTARLA SIN DECIDIR, PARAS Y LA
  TRAES. Eso es AUDITOR.md 3 y no es una formula: es la salida legitima si la
  encuentras.

- TAREA 3, LA RELECTURA AL DOBLE DEL TRAMO DEL EXPEDIENTE. El credito de la
  tanda BAJO en el acta 149 (seccion 5) porque las dos cosas que el auditor
  encontro cayeron FUERA de los discutibles marcados, y las dos son de
  expediente. La regla de AUDITOR.md 1.2 manda releer ese tramo al doble y aqui
  se encarga:
  (3.a) RECORRE docs/plan/OPERACIONES.jsonl ENTERO, las 71 fichas, y coteja el
  campo estado de cada una contra lo que el repo dice que se ejecuto. Publica
  la tabla de las que NO calzan, con su motivo, y CERO de las que si: la tabla
  corta es la que se lee.
  (3.b) DECLARA EL CRITERIO que usaste para decir "esta ejecutada", y que sea
  medible contra el repo y no contra un acta. Un estado congelado a proposito
  es legitimo (el de OP-A-01 y OP-A-02 lo esta, y lo esta DICIENDOLO): lo que
  no es legitimo es congelado en silencio.
  (3.c) SI ENCUENTRAS OTRA OPERACION DESBLOQUEADA que nadie nombro, como paso
  con OP-C-05, la traes en el reporte con su depende_de medido. NO la ejecutes
  en esta vuelta sin encargo: la nombras.

- TAREA 4, LA MITAD DE LA FASE 08 QUE SI SE PUEDE RECORRER. La tabla POR FASE
  de docs/plan/08_VERIFICACION.md tiene OCHO filas (0 CODIGO a 07 ADUANA) y la
  vuelta 148 midio UNA. Ninguna de las ocho pide credencial.
  (4.a) RECORRE LAS OCHO, cada una contra su celda "que tiene que dar verde"
  tal como esta escrita, con el instrumento que corras pegado al lado. La fila
  de 05 SANEO se lee ACOTADA A LAS NOMINAS DE SUS OPERACIONES por la correccion
  declarada de la vuelta 122, que esta escrita en esa misma pagina: la citas y
  no la reinterpretas.
  (4.b) LA FILA DE 07 ADUANA se lee con la fase ya cerrada por el acta 149:
  "los cuatro controles mecanicos corriendo en Gate 0", medido contra Gate 0 y
  no contra la vara de codigo, que es otra unidad.
  (4.c) LO QUE NO CALCE SE DECLARA CON SU CIFRA, no se redondea hacia lo comodo
  ni se deja para luego. Una fila que no calza no cierra la fase: la abre, y
  eso es informacion, no un fracaso.
  (4.d) LA VERIFICACION TRANSVERSAL NO SE TOCA. Los cinco puntos ya estan
  medidos en la vuelta 148 y adjudicados en el acta 149: dos corren verdes, uno
  corre y cae ruidosamente por la clave que falta, y dos no se pueden invocar.
  No la vuelvas a correr y no la declares cerrada.
  (4.e) UNA PALABRA POR SENTIDO. La cabecera de la seccion 5 del reporte 148
  decia "Tres corren y tres piden credencial" sobre cinco puntos, y no era
  falso: eran dos conjuntos verdaderos que se solapan en el punto 4 sin decirlo
  (acta 149, 4.4). En el reporte de esta vuelta, "correr" no puede significar
  "se invoco" y "quedo satisfecho" en la misma frase. Si dos conjuntos se
  solapan, se dice.

- TAREA 5, LA GUARDA DEL CICLO DE GATE 0, Y NACE DE UNA CAIDA DEL AUDITOR. En
  la vuelta 149 el auditor corrio run_phase1.py suelto, fuera del orden del
  ciclo, y se saco un falso rojo de la suite del motor (71 nodos divergentes).
  Es la MISMA trampa que el acta 147 registro contra si misma en su 4.3.c, y es
  la cuarta acta seguida en que un auditor cae en ella. El aviso escrito no
  basta: hace falta que muerda.
  (5.a) QUE EL FALSO ROJO SE DELATE SOLO. Cuando la suite del motor caiga por
  nodos divergentes entre las dos copias del grafo, o cuando el numstat salga
  sucio en dataset/metadata/master_graph.json, el mensaje TIENE QUE DECIR que
  el ciclo pudo quedarse a medias y nombrar el comando que falta. Criterio
  libre, FIN NO NEGOCIABLE: que quien lea el rojo sepa en un segundo si es un
  rojo de verdad o un ciclo sin cerrar.
  (5.b) NO AFLOJES NADA. La guarda no puede tapar un rojo legitimo: si las dos
  copias divergen DESPUES del ciclo entero, eso sigue siendo rojo y sigue
  parando. Lo que se anade es el diagnostico, no una excepcion.
  (5.c) SU CASO ROJO POR MUTACION sobre variable computada, y su caso de
  control: el ciclo corrido en orden no puede disparar el aviso.

- TAREA 6, EL CIERRE. El ciclo entero de Gate 0 en su orden y las tres suites
  en verde, las guardas del cierre re corridas sobre el fichero commiteado, la
  cabecera tallada y pegada entera, y el bloque de apertura sellado ANTES de la
  primera operacion. EL MERGE NO SE PIDE NI SE HACE: es del fundador y solo
  suyo, y la campaña no esta consumada.

LO QUE QUEDA DESPUES DE ESTA VUELTA, DICHO PARA QUE NO SORPRENDA: si las seis
tareas salen, al bucle no le queda mas que la sesion con credencial, y esa es
parada legitima por la seccion 4 de AUDITOR.md. No la anticipes y no la
declares tu: entregas la vuelta y el auditor la mide.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
