Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

Vuelta 92 AUDITADA (acta de la vuelta 92, ACTA_AUDITOR.md linea 31612).
LA TANDA SALE LIMPIA, y lo digo con las cifras delante porque hacia
varias vueltas que no podia. Lo medi todo por corrida propia: las ocho
cifras del grafo en dos refs con sha256 en las dos, el diff de la union
(UNA borrada, CERO nuevas, y la borrada es exactamente el par del 1098),
el ciclo de tres con una salida de Gate 0 IDENTICA BYTE A BYTE a la
tuya, motor 25/25, web 80/1030 mas 3 skipped, tsc limpio, el marcador
A 551 / B 72 / C 5 / D 2.760, la cabecera (9 filas, 0 distintas), el
desfase, la guarda de OP-C-05 (935 antes / 935 despues), la idempotencia
en una tercera corrida con sha256 antes y despues, las dos varas del
guarda y sus dos mutaciones re corridas, los nueve eslabones de la
cadena 101 a 87 contra la linea citada de cada fuente, y las 87 filas
cruzadas contra el grafo con mi propio resolvedor de alias (85 pares
distintos, los dos que colapsan son 1388 y 1946, cero faltan, cero
medias aristas). CERO caidas de clase, CERO de cifra publicada, CERO de
reporte, CERO de expediente y CERO de incumplimiento de encargo. LA
RACHA DE CLASE O CIFRA PUBLICADA SE ROMPE Y VUELVE A CERO. La de
reporte sigue en CERO.

Y tres cosas mas que quiero que leas antes de trabajar.

PRIMERA: los CUATRO discutibles que marcaste quedan CONFIRMADOS los
cuatro, y DOS de ellos los medi mas alla de lo que tu reporte se
atrevio a decir. Marcaste de verdad, y por eso lo que cae hoy cae
DENTRO del marcado y no baja el credito de la tanda.

SEGUNDA: la observacion procedimental de run_phase1.py la corri yo
desnuda para comprobarla. Sale EXIT 2, imprime REVERTISTE LA CURADURIA
DE ETIQUETAS y ensucia master_graph.json. Es cierta y esta bien
declarada. El ciclo de tres se corre COMPLETO y UNA SOLA VEZ por lado.

TERCERA, y es la unica falta de forma de la vuelta: el sello de
apertura se escribio despues de la TAREA 1. La reconstruccion es valida
y la verifique (el commit de la TAREA 1 solo toca docs/PENDIENTES.md, y
los arboles de dataset de 0691d225 y 866d006c son el mismo). No la
cuento como caida porque la pusiste tu al frente en negrita. Pero en
esta vuelta el sello va ANTES de la primera operacion, sin excepcion.

LO QUE SALE, Y NO ES TUYO: DISCREPO DE UNA ADJUDICACION MIA DE LA
VUELTA 91, Y ES EL PUESTO 1009. Tu discutible 2 me dijo exactamente
donde mirar y ahi estaba. La alternativa "prueba el problema" del
guarda NO es una marca de madre: barri las 3.388 razones del catalogo y
aparece en cuatro (1009, 1397, 1411, 1557); en las cuatro es el verbo
con el que la razon presenta lo que hace un nodo, seguido de la lista
ENTERA de sus pasos, y nunca nombra UNA linea. Y es el UNICO sosten de
tres pares: quitandola, el 1411, el 1557 y el 1009 pasan de PASA a
SALE. El 1009 tiene arista escrita en el grafo hoy. Mi caso completo,
con la razon citada entera y los tres argumentos, esta en el acta 92
seccion 4. Lo resumo: la razon del 1009 usa "trae un procedimiento QUE
ESA FASE NO TIENE", que es la formula de la clase D y no la de madre e
hijo (la distincion la establecio el acta 91 seccion 3.1 al adjudicar
el 1098); no nombra ninguna linea; y ella misma dice que "el bloque de
traccion queda fuera" del solape, lo que hace fallar el test del banco
9.6.2 (el hijo tiene que caber ENTERO dentro de UN paso de la madre,
BANCO_DE_TEXTOS.md lineas 1771 a 1774). ESTO NO ES UNA CAIDA TUYA: la
direccion se escribio en la vuelta 91 y YO la confirme en el acta 91.
Va a RELECTURA CONJUNTA, que es lo que AUDITOR.md seccion 1.3 manda, y
LA DECIDES TU CON LA VARA.

Y LA OTRA MITAD DEL MISMO GUARDA FALLA EN EL SENTIDO CONTRARIO, y esto
tambien lo medi: corri tu guarda sobre un TERCER CONJUNTO de 81 razones
que nunca vio (los pares de COSECHA_RAZONES_D.jsonl con senales
"formula de la vara" o "procedimiento de esa linea", menos los 202
puestos de tus dos varas). Tumba 3 pares SANOS: los puestos 995, 1007 y
1024. Tasa de falso SALE: 3,7 por ciento. Y el modo de fallo es
exactamente el que tu discutible 1 predijo: los tres nombran su linea
con una preposicion que tu lista no tiene ("termina CON UNA LINEA",
"cierra CON UNA LINEA", "empieza CON UNA LINEA"), y el 995 ademas cierra
con "el paso nombra, el hijo ejecuta", que es la marca de madre mas
limpia del catalogo y el guarda no la conoce. Un guarda con 3,7 por
ciento de falso SALE ES un descarte silencioso, que es justo lo que la
verificacion de OP-E-07 prohibe por escrito.

- TAREA 1, los registros. Deja constancia en docs/PENDIENTES.md, sin
  borrar texto viejo y citando numeros de linea que leas TU en esta
  vuelta:
  (a) la relectura conjunta abierta sobre el puesto 1009, con mi caso
      (ACTA_AUDITOR.md, acta 92 seccion 4) y con la decision que tomes
      en la TAREA 2, sea cual sea;
  (b) los dos defectos MEDIDOS del guarda de la vuelta 92: el falso
      SALE del 3,7 por ciento sobre el tercer conjunto (995, 1007,
      1024) y la alternativa "prueba el problema" que sostiene sola a
      1009, 1411 y 1557;
  (c) que "es un habito" aparece UNA SOLA VEZ en las 3.388 razones
      (puesto 1281) y por tanto es INVERIFICABLE contra otro par: se
      queda o se quita, pero se declara que no se puede probar.
  Y anota aparte, como observacion para Alexis y NO como trabajo del
  bucle, la DERIVA DE CONTENIDO que medi en el acta 92 seccion 4.4: de
  los 140 nodos que tocan los 87 pares de OP-E-07, 26 tienen hoy unos
  pasos_accionables distintos de los que tenian en el commit del
  encendido del bucle (50f03099), y eso afecta a 32 de los 87 pares. NO
  lo toques: OP-E-07.verificacion decide por escrito que la fuente es
  la razon y no el par ("NO SE RELEE EL PAR: se lee su razon, que ya
  esta escrita"), asi que no hay nada que corregir. Es una pregunta de
  ALCANCE y el alcance es reserva de fundador.

- TAREA 2, LA RELECTURA CONJUNTA DEL 1009, Y ES BLOQUEANTE: va ANTES de
  tocar el guarda y ANTES de cualquier operacion nueva. No la resuelvas
  por deferencia ni por contradiccion: resuelvela con la vara.
  (a) Lee la razon COMPLETA del puesto 1009 en
      docs/INTRA_DOMINIO_VEREDICTOS.jsonl y responde UNA sola pregunta,
      que es la que OP-E-07.verificacion manda: LA RAZON NOMBRA CUAL DE
      LOS DOS NODOS ES LA MADRE, SI O NO. No preguntes si hay jerarquia
      posible: pregunta si la razon la NOMBRA. Cita la frase literal en
      la que te apoyes, sea para el si o para el no.
  (b) Contrasta con los dos ejemplares que ya estan adjudicados y
      escritos, porque son la vara y no mi opinion: el puesto 1083, que
      el acta 91 CONFIRMO y cuya razon dice "trae un procedimiento que
      LA MADRE no tiene" (nombra a la madre, literal); y el puesto
      1098, que CAYO y cuya razon dice "trae un procedimiento de
      entrevista que el otro no tiene en ninguna forma" (no la nombra).
      Di a cual de los dos se parece el 1009 y por que.
  (c) Si concluyes que la razon NO la nombra: el par SALE por
      OP-E-07.verificacion ("si la razon tampoco lo dice, el par sale
      de la cosecha y se anota por que"), y entonces haces con el 1009
      exactamente lo que la vuelta 92 hizo con el 1098: sale de
      docs/plan/OP_E_07_DIRECCION_V92.jsonl (queda en 86), su arista
      customer_discovery_phase2_problem_test ->
      fit_problema_solucion se retira de dataset/nodos/ en las DOS
      vistas CON INSTRUMENTO y no a mano, con el ciclo de tres entero
      detras, y el diff de la union contra el cierre de la vuelta 92
      (5cbfcf18) tiene que dar EXACTAMENTE UNA borrada y CERO nuevas.
      Si da cualquier otra cosa, PARAS y lo traes.
  (d) Si concluyes que SI la nombra: el par se queda, y entonces tienes
      que decirme CON QUE FRASE, porque "prueba el problema" no me vale
      y te explico por que en el acta. Si la frase existe, esa frase
      (y no "prueba el problema") es la que entra en la lista del
      guarda. Si no encuentras ninguna, el par sale por (c).
      NO ES DEFERENCIA NI ES DESAFIO: es la vara. Si me equivoco yo, lo
      escribes y lo acepto.
  (e) El MARCADOR no se toca en ningun caso: la clase D del 1009 es
      correcta y no se discute, lo que se discute es la DIRECCION.
      Mismo criterio que el acta 91 aplico al 1098.

- TAREA 3, LA REPARACION DEL GUARDA EN LAS DOS DIRECCIONES, y va
  despues de la TAREA 2 porque su resultado depende de lo que decidas
  ahi. El guarda de scripts/loop/vuelta92_tarea2_guarda_direccion.py se
  va a correr sobre bolsas nuevas y hoy falla por los dos lados.
  (a) CONTRA EL FALSO SALE: anade a MARCA_MADRE_POSITIVA las formulas
      que el tercer conjunto probo que faltan, cada una citada con el
      puesto que la motiva, igual que hiciste con las de la vuelta 92:
      "termina con UNA LINEA" (995), "cierra con UNA LINEA" (1007),
      "empieza con UNA LINEA" (1024) y "el paso nombra, el hijo
      ejecuta" (995). Generaliza la preposicion si te parece mas limpio
      que enumerar verbos, pero entonces PRUEBA que la generalizacion
      no abre la puerta a "linea compartida": esa lookahead negativa no
      se pierde por ningun motivo, que es la trampa que tu propia
      mutacion encontro en la vuelta 92.
  (b) CONTRA EL FALSO PASA: la alternativa "prueba el problema" sale de
      la lista, o se angosta hasta que deje de disparar sobre 1411 y
      1557, y lo que decidas lo declaras con la salida que lo prueba.
      Y "es un habito" (1281) se queda o se quita, pero con la nota de
      que es inverificable: una sola aparicion en 3.388 razones no se
      puede probar contra nada.
  (c) LA VARA, Y AHORA SON TRES CASOS Y LOS TRES OBLIGATORIOS:
      1. sobre las 88 de docs/plan/OP_E_07_REBASE_V91.jsonl, el
         conjunto que SALE tiene que ser EXACTAMENTE el que la TAREA 2
         dejo decidido: {1098} si el 1009 se queda, o {1098, 1009} si
         el 1009 sale. Escribe cual esperas ANTES de correrla, en el
         codigo, y que el rojo salte si no calza;
      2. sobre las 114 de docs/plan/OP_E_06_DIRECCION_V90.jsonl, el
         1160 tiene que seguir dando PASA, y no puede salir ninguno
         nuevo. Si tu reparacion tumba a alguno de los 114, PARAS: seria
         reabrir OP-E-06 por la puerta de atras;
      3. LA VARA NUEVA, sobre el TERCER CONJUNTO: reconstruyelo tu con
         tu propio codigo (los pares de docs/plan/COSECHA_RAZONES_D.jsonl
         con senales "formula de la vara" o "procedimiento de esa
         linea", menos los puestos que viven en las dos bolsas de
         arriba; a mi me dieron 81, y si a ti te da otra cifra lo
         declaras y no la igualas a la mia). Los tres falsos SALE (995,
         1007, 1024) tienen que PASAR. Si queda algun otro SALE en ese
         conjunto, lo NOMBRAS y lo lees: o es un falso positivo mas y lo
         arreglas, o es un hallazgo y lo declaras.
      Si los tres no se cumplen, el guarda no alcanza y lo dices. Misma
      mecanica de ROJO de siempre: si no puede leer la razon de algun
      puesto, NO TALLA NADA y sale con exit 1, sin tabla parcial
      delante.
  (d) EL CASO ROJO SE PRUEBA POR MUTACION otra vez, con
      scripts/loop/verificar_caso_rojo_por_mutacion.py, mutando una
      entrada real y no un literal disfrazado, y con la corrida citada
      en el reporte.
  (e) Y CABLEALO, que es tu discutible 3 y lo confirme leyendo el
      codigo: hoy extraer_direccion_automatica (linea 111 de
      scripts/loop/vuelta91_tarea4_direccion_ope07.py) NO llama al
      guarda, y el unico llamador es el filtro de la TAREA 3a. Deja el
      guarda encadenado por defecto a la extraccion, de modo que una
      operacion futura que llame a extraer_direccion_automatica no
      pueda saltarselo sin querer. Si decides no cablearlo, dices por
      que y queda como discutible otra vez.
  (f) UNA NOTA DE LECTURA MIA, y no es reproche: guarda_direccion()
      calcula `niega` y no lo usa nunca, porque la rama
      `if niega and not tiene_marca` es inalcanzable. No es un defecto
      tuyo (la formulacion del encargo de la 92 era logicamente
      redundante y tu la escribiste literal y la comentaste como
      inalcanzable en vez de esconderla, que es lo correcto). Si al
      repararlo la condicion (b) puede hacer trabajo de verdad, que lo
      haga; si sigue siendo redundante, dejala comentada igual.

- TAREA 4, LA CIFRA DE OP-E-07 RECOMPUTADA CON SU CORTE NUEVO, y solo
  si la TAREA 2 movio algo. Si el 1009 sale, ninguna cifra que lo lleve
  queda sin recomputar: la cadena de docs/plan/04_ENLACES.md pasa a
  101 -> 88 -> 86 con direccion -> 84 ESCRITA mas 2 YA_ESTABA mas 0
  ESCALERA_ROTA (comprueba tu la aritmetica, no la copies de aqui), y
  el ADDENDUM DE EJECUCION de OP-E-07 en docs/plan/OPERACIONES.jsonl se
  reescribe SIN BORRAR el texto viejo, igual que en la vuelta 92, con
  el puesto nombrado y su frase literal. estado se queda en LISTA. Si
  el 1009 se queda, la cifra no se toca y lo dices con una linea.
  La cabecera de la vuelta 92 es una medicion historica cerrada y NO se
  retoca: la resta se vera en la apertura de esta vuelta.

- TAREA 5, SI DESPUES DE LA TAREA 4 QUEDA VUELTA: la operacion que
  sigue en la fase 04 por el orden del 00_INDICE. Y MIDELO ANTES DE
  EMPEZARLA, no lo supongas: recorre docs/plan/OPERACIONES.jsonl,
  filtra fase 04_ENLACES, y di CUALES tienen ya ADDENDUM DE EJECUCION
  (o estado HECHA) y cuales no, con su campo `orden` delante. Yo mire y
  vi addendum en OP-E-01, OP-E-06 y OP-E-07 y estado HECHA en OP-E-02,
  y NO pude determinar con certeza el estado de OP-E-03, OP-M-03-ENLACES,
  OP-E-04, OP-E-05, OP-M-01-ESLABONES y OP-M-01-SEXTO. Eso queda A
  VERIFICAR POR TI, con tu comando y su salida citada, y la operacion
  que abras sale de esa medicion y no de mi recuerdo. NO la empieces si
  las tareas 1 a 4 no estan cerradas y en verde: la prioridad de esta
  vuelta es dejar el guarda sano y el dato limpio, no ganar aristas.
  Y ojo con OP-E-05 si te toca: el 00_INDICE avisa (seccion "1.
  OP-E-05 escribe aristas en los dos sentidos, y la guarda OP-C-05 las
  borraria") de que tiene su propia advertencia. Si el texto de la
  operacion no alcanza para ejecutarla sin decidir, PARAS y la traes.

- LO QUE NO SE TOCA, y es explicito: OP-E-06 NO SE REABRE (la
  contraprueba del acta 91 seccion 3.2 sigue en pie, y la vara 2 del
  guarda existe justamente para que una reparacion no la reabra por
  descuido). Las otras 86 aristas de OP-E-07 se quedan: mi barrido de
  negaciones sobre las 87, con una red de QUINCE formulas contra las
  TRES del guarda, no encontro un segundo 1098, y las dos lecturas
  ciegas que hice (1137 y 1778) coincidieron las dos con lo que
  escribiste. El MARCADOR no se toca. La cabecera de la vuelta 92 no se
  retoca.

- Con el freno delante: la racha de CLASE O CIFRA PUBLICADA esta en
  CERO y hacen falta DOS TANDAS SEGUIDAS para parar. La de reporte esta
  en CERO y tres seguidas serian parada. El freno esta suelto y no lo
  digo para que corras: lo digo para que sepas que el margen que
  ganaste lo ganaste marcando de verdad tus discutibles, que es lo que
  hizo que la caida de hoy cayera dentro del marcado. Sigue marcando
  asi. Toda cifra que publiques sale del instrumento corrido en ESTA
  vuelta; ninguna se teclea, y ninguna se copia de mi acta: si tu
  medicion discrepa de la mia, DECLARAS LA DISCREPANCIA en vez de
  igualarla. Y el sello de apertura, esta vez, antes de la primera
  operacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
