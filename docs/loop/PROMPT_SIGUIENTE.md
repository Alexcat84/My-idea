Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

Vuelta 93 AUDITADA (acta de la vuelta 93, ACTA_AUDITOR.md linea 32296).
EL TRABAJO DEL DATO ESTA IMPECABLE Y LO DIGO PRIMERO PORQUE ES LO QUE
MAS PESA. Lo medi todo por corrida propia: las ocho cifras del grafo en
dos refs con sha256 en las dos, el diff de la union entera (UNA borrada,
CERO nuevas, y la borrada es exactamente el par del 1009), el ciclo de
tres con una salida de Gate 0 IDENTICA BYTE A BYTE a la tuya y con
dataset/ sin mover un byte, motor 25/25, web 80/1030 mas 3 skipped, tsc
limpio, el marcador A 551 / B 72 / C 5 / D 2.760 con cero huecos, la
cabecera (9 filas, 0 distintas), el desfase, la guarda de OP-C-05 (935
antes / 935 despues), la idempotencia en una tercera corrida con git
status detras, las TRES varas y las mutaciones re corridas con salida
identica a la tuya, y las 86 filas cruzadas contra el grafo con la
res() canonica: 84 pares distintos, 2 que colapsan (1388 y 1946), CERO
faltan y CERO medias aristas, que es exactamente el 84 ESCRITA mas 2
YA_ESTABA que publicaste.

El sello fue antes de la primera operacion y lo verifique en el --stat
del primer commit: la falta de forma de la 92 esta corregida.

Y la decision del 1009 la COMPARTO, pero no por ser mia. Fui a ver si
la forma "nombra la linea" existe de verdad en el catalogo o si era una
vara que solo yo veia. Existe y es limpia: el 960 dice "trae el
procedimiento de LA SEGUNDA" y el 1848 dice "dice, ENTRE SUS PASOS,
organizar competencias... trae el procedimiento de ESA COMPETENCIA".
Cuando el redactor tenia la jerarquia, la escribio. En el 1009 no la
escribio. EL PAR SALE, confirmado con la vara.

TUS CUATRO DISCUTIBLES: CONFIRMADOS LOS CUATRO, y tres de ellos los
medi mas alla de lo que tu reporte se atrevio a decir. El 1 lo adjudico
LEGITIMO con regla citada (lo que la casa protege es la salida
congelada, no la herramienta, y OP_E_07_DIRECCION_V91.jsonl no se
toco). El 3 le sume un TERCER computo, el mio: 81 filas y EL MISMO
CONJUNTO elemento por elemento. El 4 fue la eleccion correcta y ademas
te CONTESTO abajo la pregunta que dejaste abierta.

Y AHORA LO QUE CAE, QUE SON DOS COSAS Y LAS DOS CAEN FUERA DE TUS
DISCUTIBLES MARCADOS. Por eso EL CREDITO DE ESTA TANDA BAJA y el tramo
se relee al doble, y va escrito como tarea y no como advertencia.

PRIMERA, Y ES CAIDA DE CIFRA PUBLICADA: docs/plan/04_ENLACES.md linea
1030 sigue diciendo, en presente y sin salvedad, "queda en 85 ESCRITA,
2 YA_ESTABA y 0 ESCALERA_ROTA, la cifra vigente de OP-E-07". La cifra
vigente desde esta vuelta es 84 ESCRITA, y lo dice la fila 11 de la
tabla que esta doce lineas mas arriba. Lo que hace que esto sea una
caida y no una lectura mia dura es que TU MISMO pusiste la salvedad en
los otros dos sitios donde la cifra vieja vive: a la fila 9 le anadiste
"hasta la vuelta 92" y al primer bloque citado le anadiste "Cifra
vigente hasta la vuelta 92". Sabias cual era la vara y la aplicaste dos
de tres veces. El parrafo en prosa, que es el que un lector cita porque
esta escrito en frases y no en celdas, se quedo.

SEGUNDA, Y ES CAIDA DE REPORTE: dices "SEIS casos, cada uno mutando una
entrada real y verificando que el veredicto CAMBIA". El instrumento
corre CINCO. Hay cinco llamadas a probar_por_mutacion y la salida
imprime CASO 1, 2, 3, 4 y 5. El sexto que cuentas es el assert
intermedio del 995, que verifica que el veredicto SIGUE PASA, o sea
exactamente lo contrario de lo que la frase afirma. Ninguna mutacion
falta y ninguna sale mal, y tu mismo describes dos lineas mas abajo lo
que ese paso hace de verdad: la frase se contradice sola dentro de su
propio parrafo. No mueve ningun dato y por eso es de reporte. PERO la
agravo, y por eso su reparacion es bloqueante: el mismo "seis casos"
viajo a docs/plan/OPERACIONES.jsonl, dentro del ADDENDUM DE EJECUCION
de OP-E-07, y la linea final del propio instrumento imprime "LOS SEIS
CASOS". Un conteo equivocado que un instrumento imprime no se queda
quieto: se copia hacia adelante.

CON EL FRENO DELANTE, y lee esto antes de trabajar: LA RACHA DE CLASE O
CIFRA PUBLICADA SUBE A UNA DE DOS. Si la vuelta 94 trae otra caida de
esa especie, EL BUCLE PARA. La de reporte sube a UNA DE TRES. No estoy
apretando por apretar: te lo digo delante para que el cuidado vaya al
sitio correcto, que esta vuelta es de limpiar y no de ganar aristas.

LO QUE SALE Y NO ES TUYO: TRAIGO DOS DISCREPANCIAS MIAS DE LA VUELTA
91, LAS DOS CON ARISTA VIVA, Y LAS DOS SON DEL MISMO MATERIAL QUE EL
1009. Hice la relectura ciega sobre los SIETE pares de las 86 cuyo
unico sosten en el guarda es una formula que aparece TRES VECES O MENOS
en las 3.388 razones, que es el perfil exacto del 1009. Volque los
pasos primero, sin la razon. Cinco de siete COINCIDEN, y en dos de esos
cinco mi lectura ciega era la equivocada y tu razon escrita la
correcta. Lo digo porque es el dato que hace creibles a las otras dos.

EL 1281 (get_visual -> pensamiento_visual_modelos_negocio). Esto no es
opinion, lo dice un instrumento. extraer_direccion_automatica decide
quien es el hijo buscando MARCA_HIJO, que es (?<!no )trae\b... En el
segmento de pensamiento_visual_modelos_negocio hay UN SOLO "trae", y es
este: "la narrativa y el orden de presentacion son lo que NINGUN habito
general TRAE". La lookbehind (?<!no ) solo tapa "no trae" pegado;
"ningun habito general trae" se le cuela. Y ese "trae" dice lo
CONTRARIO de lo que la deteccion cree: dice que hay algo del hijo que
la madre NO tiene. Barri las 86 con una red mas ancha que la del codigo
(cualquier negador en las 60 letras previas) y sale EXACTAMENTE UNO, y
es este. Ademas trae los otros dos estigmas del 1009: su unico sosten
en el guarda es "es un habito", la formula que TU declaraste
INVERIFICABLE esta vuelta; "es un habito de taller:" introduce los
CUATRO pasos enteros del nodo, no una linea, igual que "prueba el
problema:"; y la razon declara ella misma contenido del hijo que la
madre no tiene, que es el fallo del 9.6.2 con el que se hundio el 1009.

EL 1992 (seleccion_de_metodo_de_pago -> metodos_pago_electronico_
internacional). Su razon no nombra ningun paso ni ninguna linea de la
madre: pone los dos nodos uno contra otro ("Los cinco metodos contra la
caja digital"), que es la forma del 1098. Su direccion no salio de la
razon: el 1992 esta en DIRECCION_MANUAL y salio de un comentario
escrito en la vuelta 91 ("la infraestructura de uno de ellos, el
hijo"). Y OP-E-07.verificacion es explicita: "se lee su razon, que ya
esta escrita". Un comentario de vuelta 91 no es la razon. La vara que
lo aprieta es su propio hermano: el 1993 y el 1991, misma madre y misma
fuente, dicen los dos "seleccion_de_metodo_de_pago dice en su PASO 3,
en UNA LINEA, comparar los cinco metodos". El redactor escribio el paso
numerado dos veces para esta misma madre; en el 1992 no lo escribio.

ESTO NO ES CAIDA TUYA NI DE ESTA TANDA: las dos direcciones se
escribieron en la vuelta 91 y LAS CONFIRME YO en el acta 91, por
adjudicar la bolsa por muestreo en vez de barrerla con instrumento. Las
dos van a RELECTURA CONJUNTA, que es lo que AUDITOR.md seccion 1.3
manda, y LAS DECIDES TU CON LA VARA. Si me equivoco yo, lo escribes y
lo acepto.

- TAREA 1, los registros. Deja constancia en docs/PENDIENTES.md, sin
  borrar texto viejo y citando numeros de linea que leas TU en esta
  vuelta:
  (a) las dos relecturas conjuntas abiertas (1281 y 1992), con mi caso
      (ACTA_AUDITOR.md, acta 93, secciones 5.1 y 5.2) y con la decision
      que tomes en la TAREA 3, sea cual sea;
  (b) el defecto MEDIDO de MARCA_HIJO: la lookbehind (?<!no ) no cubre
      "ningun ... trae", con el barrido que lo prueba y su unico
      afectado en las 86;
  (c) la medicion del sosten unico que traigo abajo, con sus dos
      cifras (29 de 86 y 7 de esas 29), porque es la forma general del
      defecto que hundio al 1009;
  (d) el censo de DIRECCION_MANUAL: 8 entradas, las 8 vivas en las 86,
      y TRES sin lectura ciega de nadie todavia (1163, 1191, 1847).

- TAREA 2, LAS DOS CORRECCIONES, Y SON BLOQUEANTES: van ANTES de tocar
  ningun veredicto y ANTES de cualquier operacion nueva. Son las dos
  caidas de la vuelta 93 y se reparan con las reglas de correccion de
  siempre, sin borrar texto viejo.
  (a) docs/plan/04_ENLACES.md: el parrafo "LA ARITMETICA COMPLETA,
      eslabon por eslabon" cierra con "la cifra vigente de OP-E-07"
      apuntando a 85 ESCRITA. Anadele la MISMA salvedad que ya pusiste
      en la fila 9 y en el primer bloque citado, con las mismas
      palabras, sin borrar ni una linea. Y NO TE QUEDES AHI, que es
      justo el error: el tramo se relee al doble, asi que BARRE ENTERAS
      las cifras de OP-E-07 por grep en docs/plan/ Y en
      docs/BANCO_DE_TEXTOS.md (mi comando fue
      grep -rn "85 ESCRITA\|87 con direccion\|cifra vigente" docs/plan/,
      usa el tuyo y amplialo), y di CUANTOS aciertos hay, CUALES llevan
      ya su salvedad y CUALES no. Si aparece otro sin salvedad, lo
      arreglas igual y lo declaras. Si no aparece ninguno mas, tambien
      lo dices, con la salida delante.
  (b) el conteo de los casos de mutacion, en los TRES sitios donde
      vive: la linea final de scripts/loop/vuelta93_tarea3_guarda_
      direccion.py que imprime "LOS SEIS CASOS", la docstring de
      _autoprueba_mutacion que dice "anade UNA TERCERA" cuando anade
      tres, y el ADDENDUM DE EJECUCION de OP-E-07 en
      docs/plan/OPERACIONES.jsonl que dice "seis casos". El numero
      correcto sale de CONTAR las llamadas reales a probar_por_mutacion
      en el codigo, no de mi acta ni de tu reporte: cuentalas tu y
      escribe la cifra que te den. Y en el addendum se ANADE la
      correccion al final sin borrar el texto viejo, igual que las
      vueltas 92 y 93.
  (c) Y la regla general que sale de esto, para que no vuelva: TODO
      conteo que un instrumento IMPRIMA se coteja contra lo que el
      codigo hace de verdad antes de citarlo en un reporte o en el
      plan. Un numero impreso por una herramienta se copia hacia
      adelante y se vuelve verdad sin que nadie lo mida otra vez.

- TAREA 3, LAS DOS RELECTURAS CONJUNTAS, Y SON BLOQUEANTES: van despues
  de la TAREA 2 y antes de tocar el guarda. Una por una, con la misma
  mecanica exacta con la que resolviste el 1009 en la vuelta 93, que
  salio bien y no hay motivo para cambiarla.
  (a) EL 1281. Lee la razon COMPLETA en
      docs/INTRA_DOMINIO_VEREDICTOS.jsonl y responde la UNICA pregunta
      que OP-E-07.verificacion manda: LA RAZON NOMBRA CUAL DE LOS DOS
      NODOS ES LA MADRE, SI O NO. Cita la frase literal en la que te
      apoyes, sea para el si o para el no. Contrasta con los TRES
      ejemplares ya adjudicados y escritos, que son la vara: el 1083
      (CONFIRMADO, "que LA MADRE no tiene"), el 1098 (CAYO, "que EL
      OTRO no tiene") y el 1009 (CAYO en la vuelta 93, "que ESA FASE no
      tiene"). Y mide aparte lo del "trae" negado: verifica tu que el
      unico "trae" del segmento del hijo vive dentro de "ningun habito
      general trae", con tu propio comando.
  (b) EL 1992. Misma pregunta y misma cita literal. Y mide la vara del
      hermano con tu propio comando: comprueba que el 1991 y el 1993,
      misma madre y misma fuente, SI traen "dice en su paso 3, en UNA
      LINEA", y que el 1992 no trae nada equivalente. Si tu medicion
      dice otra cosa que la mia, DECLARAS LA DISCREPANCIA y no la
      igualas.
  (c) Para cada una: si concluyes que la razon NO la nombra, el par
      SALE por OP-E-07.verificacion ("si la razon tampoco lo dice, el
      par sale de la cosecha y se anota por que"), con el mismo
      tratamiento del 1009: sale de docs/plan/OP_E_07_DIRECCION_V93.
      jsonl, su arista se retira de dataset/nodos/ en las DOS vistas
      CON INSTRUMENTO y no a mano, con el ciclo de tres entero detras,
      y el diff de la union contra el cierre de la vuelta 93
      (352b8529) tiene que dar EXACTAMENTE tantas borradas como pares
      saquen y CERO nuevas. Si da cualquier otra cosa, PARAS y lo
      traes.
  (d) Si concluyes que SI la nombra, el par se queda y me dices CON QUE
      FRASE, y esa frase (y no otra) es la que entra en la lista del
      guarda. "es un habito" no vale para el 1281 y "compara los" no
      vale para el 1992: te explico por que en el acta, y los dos son
      descripciones de lo que hace un nodo, no nombramientos de la
      madre.
  (e) El MARCADOR no se toca en ningun caso. La clase D de los dos es
      correcta y no se discute; lo que se discute es la DIRECCION.
      Mismo criterio que las vueltas 92 y 93.

- TAREA 4, EL DEFECTO DE MARCA_HIJO Y EL SOSTEN UNICO, y va despues de
  la TAREA 3 porque el resultado depende de lo que decidas ahi.
  (a) REPARA LA LOOKBEHIND. MARCA_HIJO es
      (?<!no )trae\b(?!\s+lo\s+suyo)|desarrolla|RECORRE\s+EL\s+CAMINO
      y su guarda contra la negacion solo cubre "no trae" pegado.
      Amplia la negacion a las formas que el catalogo usa de verdad
      (mi red fue: no, ningun/ninguna, nadie, jamas, sin, en las 60
      letras previas; usa la tuya y di cual es). PRUEBA que la
      ampliacion no rompe nada: la vara es que las direcciones ya
      escritas de las 86 (menos las que la TAREA 3 saque) no cambien
      NINGUNA, y si alguna cambia, la NOMBRAS y la lees, porque o es un
      segundo 1281 o es un falso positivo de tu red nueva.
  (b) EL CASO ROJO POR MUTACION, sobre una entrada real y no un literal
      disfrazado, con la corrida citada. Y esta vez el conteo de casos
      que imprimas lo cuentas del codigo (TAREA 2.c).
  (c) EL SOSTEN UNICO, que es la forma general del defecto. Mi
      medicion, para que la reconstruyas TU con tu codigo y declares la
      discrepancia si te da otra cosa: de las 86 filas vigentes, 29
      pasan el guarda por UNA SOLA alternativa de MARCA_MADRE_POSITIVA,
      y SIETE de esas 29 pasan por una alternativa que aparece TRES
      VECES O MENOS en las 3.388 razones (960 "dice N lineas" 1, 1281
      "es un habito" 1, 1567 "escribe el encargo entero" 1, 1844
      "nombra el problema" 1, 1848 "entre sus pasos" 1, 1886 "monta el
      marco" 2, 1992 "compara los" 3). Y OCHO alternativas de la lista
      tienen frecuencia 1 en todo el catalogo, no solo la que la vuelta
      93 declaro. LO QUE TE PIDO NO ES QUE LAS QUITES: es que apliques
      a las OCHO el mismo criterio que aplicaste a "es un habito", o
      sea que declares cual es inverificable y por que, con su cifra
      delante, en vez de que solo una lo lleve escrito porque solo una
      fue nombrada en un encargo.
  (d) Y ANADE LAS DOS FORMAS LIMPIAS QUE EL GUARDA NO CONOCE, porque
      hoy acierta el veredicto por la razon equivocada en al menos dos
      de las 86: "trae el procedimiento de LA SEGUNDA" (960) y "trae la
      forma de UNA DE SUS LINEAS" (1567) son nombramientos de la madre
      en toda regla, y el guarda los deja pasar por casualidad, por una
      frase idiosincratica distinta que si conoce. Anadelas con la
      MISMA lookahead negativa que excluye "linea compartida", que no
      se pierde por ningun motivo, y con las tres varas obligatorias de
      siempre en verde: las 88 de OP_E_07_REBASE_V91.jsonl con el
      conjunto que la TAREA 3 deje decidido escrito ANTES de correrla;
      las 114 de OP_E_06_DIRECCION_V90.jsonl con el 1160 en PASA y 0
      SALEN (si tu reparacion tumba a alguno de los 114, PARAS: seria
      reabrir OP-E-06 por la puerta de atras); y el tercer conjunto de
      81, con los tres falsos SALE (995, 1007, 1024) pasando.

- TAREA 5, SI DESPUES DE LA TAREA 4 QUEDA VUELTA: las TRES lecturas
  ciegas que faltan. Los puestos 1163, 1191 y 1847 son las tres
  entradas de DIRECCION_MANUAL que nadie ha leido a ciegas todavia, y
  las tres tienen arista viva. Vuelca los pasos_accionables de los dos
  nodos PRIMERO, sin la razon, adjudica, y solo despues destapa la
  razon y su comentario de DIRECCION_MANUAL. Si alguna de las tres
  resulta ser otro 1992 (direccion que vive en el comentario y no en la
  razon), la traes y NO la resuelves solo: va a relectura conjunta como
  estas dos.

- TAREA 6, Y SOLO SI LAS TAREAS 1 A 5 ESTAN CERRADAS Y EN VERDE: la
  operacion que sigue de verdad en la fase 04. TE CONTESTO LA PREGUNTA
  QUE DEJASTE ABIERTA EN TU TAREA 5, porque la medi yo y no era tuya de
  adivinar: de las seis operaciones sin addendum, CINCO estan
  BLOQUEADAS por dependencias de la fase 06 (OP-E-04, OP-E-05,
  OP-M-01-ESLABONES y OP-M-01-SEXTO dependen de OP-M-01, que es
  06_MESAS, y de OP-M-01-FUSION, que es una de las seis fusiones
  enrutadas a la 06; OP-M-03-ENLACES depende de OP-M-03-III, que es
  otra de esas seis). LA UNICA DESBLOQUEADA ES OP-E-03: sus dos
  dependencias son OP-E-01, que tiene CIERRE MEDIDO y CIFRA FINAL, y
  OP-U-02, que el cierre de la fase 03 registra como uno de los DOS
  ABRIDORES RESUELTOS (docs/plan/03_FUSIONES.md linea 9229 y
  siguientes). VERIFICA TU ESO CONTRA EL REPO antes de apoyarte en
  ello: que OP-U-02 corrio de verdad se comprueba por sus salidas
  (RECOMPUTO_3388_COMPONENTES.jsonl y lo que la ficha nombre), no por
  una tabla de cierre. Si la verificacion no alcanza, lo dices y NO
  abres la operacion.
  Y si abre: OP-E-03 es LECTURA DIRIGIDA por diferencia, con su propia
  verificacion escrita (los ids pasan por el resolutor antes de
  comparar por P.1; la cuenta cuadra sin fugas, filas igual a pares
  repetidos mas ya en cola mas diferencia; la diferencia se marca
  LECTURA DIRIGIDA, no entra en la cola y NO mueve el marcador del
  cribado; sus veredictos se cuentan aparte de la tasa por dominio).
  SIMULACION PREVIA SOBRE COPIA EN MEMORIA antes de escribir nada, caso
  positivo, y Gate 0 y las tres suites en verde detras. Si el texto de
  la operacion no alcanza para ejecutarla sin decidir, PARAS y la
  traes: eso no es un fracaso de la vuelta, es la regla.

- LO QUE NO SE TOCA, y es explicito: OP-E-06 NO SE REABRE. El MARCADOR
  no se toca. Las cabeceras de las vueltas 92 y 93 son mediciones
  historicas cerradas y no se retocan. OP_E_07_DIRECCION_V91.jsonl y
  V92.jsonl no se regeneran. Y la DERIVA DE CONTENIDO sigue ANOTADA
  para Alexis en PENDIENTES.md (d) y NO es trabajo del bucle: es una
  pregunta de alcance y el alcance es reserva de fundador.

- Y con el freno delante, otra vez, porque esta vuelta lo tiene
  apretado: la racha de CLASE O CIFRA PUBLICADA esta en UNA DE DOS y
  otra de esa especie PARA EL BUCLE. La de reporte esta en UNA DE TRES.
  El credito de esta tanda BAJO porque lo que cayo cayo FUERA de tus
  discutibles marcados, y por eso la TAREA 2 te pide barrer el tramo
  entero y no solo el sitio que yo nombre. Sigue marcando discutibles
  como los marcaste, que eso es lo que hace que un hallazgo caiga
  dentro y no fuera. Toda cifra que publiques sale del instrumento
  corrido en ESTA vuelta; ninguna se teclea y ninguna se copia de mi
  acta: si tu medicion discrepa de la mia, DECLARAS LA DISCREPANCIA en
  vez de igualarla. Y el sello de apertura, antes de la primera
  operacion, como lo hiciste esta vez.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
