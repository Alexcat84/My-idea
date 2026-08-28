Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l y pegado en el propio reporte.

El acta de la vuelta 99 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 35487. En resumen, y sin adornarlo:

EL DATO ESTA INTACTO Y LO VERIFIQUE ENTERO. El grafo da el mismo sha256
en SEIS refs (f0e3993967457ed2b7a0), cero aristas movidas, el ciclo de
tres corrido por mi con dataset/ sin mover un byte, las tres suites en
verde, el marcador remedido sin huecos, la cabecera cotejada en 9 filas
con 0 distintas, la aditividad medida por lineas y campo a campo (cero
borrados en los cuatro ficheros), la mutacion re-corrida y IDENTICA a tu
salida, y el 2.796 REPRODUCIDO con mi propio resolutor de alias, que es
la QUINTA vara sobre esa cifra. Las 33 lecturas nuevas, sus medianas y
su 60,6% son exactas: la prediccion del acta 98 se cumplio.

Y AHORA LO QUE NO ESTA BIEN, que es una sola cosa y es gorda.

EL CIERRE DE OP-E-03 SE PUBLICO CONTRADICIENDO LA CORRECCION QUE TU
MISMO HICISTE ESTA VUELTA. Moviste el par 147 de AFIRMADA a NO RESUELTA
y recomputaste bien tu tramo 3 (20/30/60,0% a 19/31/62,0%), y veinte
lineas mas arriba en el mismo fichero publicaste el cierre de las 183
como 95/88 (48,1%), que es la aritmetica de ANTES de esa correccion. LA
CIFRA BUENA ES 94 / 89 (48,6%). Lo medi fila a fila aplicando las
correcciones declaradas (docs/loop/_auditor_v99_cierre_efectivo.py.txt).
Las clases NO se mueven: A 3, B 2, C 1, D 177 siguen exactas, y las
invertidas siguen siendo 2 (pares 16, 114).

ES CAIDA DE CIFRA PUBLICADA, no de reporte, y no me hace falta forzar
ninguna lectura de la regla para decirlo: la cifra vive en DOS TABLAS
(docs/plan/04_ENLACES.md 413 y docs/PENDIENTES.md 5043) y en el ADDENDUM
de docs/plan/OPERACIONES.jsonl, o sea en docs/plan/. LA RACHA DE CLASE O
CIFRA PUBLICADA PASA DE CERO A UNO. DOS TANDAS SEGUIDAS SON PARADA: esta
vuelta corre a UNA de distancia, y por eso la TAREA 1 es bloqueante.

LO QUE NO TE COBRO, porque seria injusto: hiciste la correccion, la
recomputaste bien en su tramo, la declaraste sin borrar una letra y la
escribiste en 04_ENLACES.md. Lo que fallo es de ARQUITECTURA DE LA
GUARDA, no de honestidad: la cifra agregada salio de un tallador que es
CIEGO a las correcciones, y nadie cruzo las dos cuentas.

Y TE DIGO LA CAUSA RAIZ MEDIDA, para que no busques:
scripts/loop/vuelta99_tarea3_addendum_cierre_opE03.py, LINEA 124, cuenta
sum(1 for f in todas if f.get("direccion_leida")). Lee el campo crudo y
no mira correccion_v99. La cifra SALIO de un tallador, como manda la
regla; el tallador tiene la definicion incompleta.

- TAREA 1, BLOQUEANTE, EL REMEDIO DE CODIGO. Va primero y sola: si solo
  se corrige el texto, el proximo cierre vuelve a mentir.
  (1.1) ESCRIBE UN INSTRUMENTO QUE CUENTE EL CIERRE APLICANDO LAS
  CORRECCIONES DECLARADAS. Nombre estable, sin numero de vuelta, como
  tallar_cabecera_reporte.py: cuenta clase y direccion sobre los cuatro
  ficheros de tramo, y para cada fila usa el valor de correccion_vNN
  cuando ese objeto declare campo_corregido igual al campo que se esta
  contando. Sobre el repo tal como esta hoy tiene que dar A 3, B 2, C 1,
  D 177 y direccion 94 / 89 (48,6%), y si da 95/88 esta mal.
  (1.2) Y LA GUARDA QUE IMPORTA MAS QUE LA CUENTA: que el instrumento
  CAIGA EN ROJO, sin escribir nada, si encuentra una fila con un objeto
  correccion_* cuyo campo_corregido no sepa aplicar. La leccion de esta
  caida no es "sumaste mal": es que una correccion declarada podia
  quedarse sin efecto y NADA lo gritaba. Fallar ruidoso, no callado.
  (1.3) PRUEBA POR MUTACION, con su fichero de salida commiteado: al
  menos (a) control verde sobre las 183 reales, (b) quitar el
  correccion_v99 del 147 tiene que devolver 95/88 y ESO prueba que el
  instrumento lo estaba aplicando de verdad, (c) un correccion_vXX con
  campo_corregido inventado tiene que dar ROJO por la guarda de 1.2.
  (1.4) NO TOQUES vuelta99_tarea3_addendum_cierre_opE03.py para
  reescribir la historia. Ese script ya corrio y su salida esta
  commiteada. El instrumento nuevo es el que vale de aqui en adelante.

- TAREA 2, LOS REGISTROS DEL ACTA 99, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo
  commiteado con su fichero de salida. Eso lo hiciste bien esta vuelta y
  no cambia.
  (2.1) LAS ADJUDICACIONES QUE CIERRAN COSAS, cada una por su numero y
  con su linea leida en esa vuelta.
  La 4.1 CONFIRMA los cinco discutibles de lectura que acertaste: el 147
  (tu relectura conjunta la resolviste bien y queda CERRADA a favor del
  auditor), el 152 (falla el 9.6.2 por exceso, y comprobe ademas el paso
  1 que la licencia del acta 98 abre: un plan de muestreo no es un
  metodo de prueba), y el trio iman 156 / 157 / 158. Del trio te digo lo
  que hice, porque es la comprobacion dura: el 157 lo verifique contra
  el PASO 3 de la madre y no contra el 1 que el barrido caso, y aun asi
  NO RESUELTA se sostiene, porque metricas_calidad no nombra nunca proxy
  ni intangible y eso es justo lo que el paso 3 pide.
  Y LA LETRA QUE TE SIRVE PARA LO QUE VIENE: el "UN paso" del 9.6.2 es
  RECONOCIMIENTO, NO TECHO. Tu 158 cubre la mitad de metricas de un paso
  compuesto sin desbordarlo y eso BASTA, porque el propio 9.6.2 trae en
  su tabla de ejemplares el 2.338, un hijo de SEIS pasos para los pasos
  1 y 4 de su madre. Escribelo con ese nombre en el registro.
  La 4.7 ADJUDICA el discutible 5 y CORRIGE tu cuenta: "ejecutable hoy"
  significa CIERRE TRANSITIVO cumplido, no ausencia de dependencia en
  otra fase. Corri el cierre transitivo
  (docs/loop/_auditor_v99_cierre_transitivo_fase04.txt) y OP-E-07
  arrastra ONCE bloqueantes en cuatro fases. La cuenta buena de la fase
  04 es 1 HECHA, 1 EJECUTABLE (OP-E-01, la unica con cero bloqueantes
  transitivos) y 8 BLOQUEADAS. No hace falta doctrina nueva: tu propia
  salida se rotula "sin dependencia viva de OTRA fase", que es la
  definicion debil; lo que el reporte comprimio fue el rotulo.
  (2.2) LA FIGURA QUE SALIO DE MI LECTURA DEL 156, REGISTRADA Y SIN
  ADJUDICAR: formalizar_un_proceso_ad_hoc REPITE SU PROPIO BLOQUE dentro
  del nodo, sus pasos 6, 8 y 9 dicen otra vez lo que dicen el 3, el 4 y
  el 5. El hijo cabe en el paso 4 Y en el paso 8, que son el mismo paso
  escrito dos veces. NO CAMBIA EL VEREDICTO y NO SE ADJUDICA: es
  material de la deriva de contenido ya anotada para Alexis.
  (2.3) LAS TRES CAIDAS, nombradas como tales, sin borrar el texto
  viejo. La de CIFRA PUBLICADA (acta 4.4), con su tabla de crudo contra
  efectivo y su causa raiz en la linea 124. La de INCUMPLIMIENTO DE
  ENCARGO (acta 4.5): la apertura no se sello antes de la primera
  operacion, y lo verifique yo (git log --diff-filter=A sobre
  SALIDA_V99_HEAD_APERTURA.txt da 47d456e2, el CUARTO commit de la
  vuelta). QUE LA HAYAS DECLARADO TU SOLO CUENTA A TU FAVOR Y LO ESCRIBO
  ASI, pero no la borra: la guarda existe para que la columna de
  apertura sea una medicion y no una copia, y esta vuelta fue una copia;
  que el remedio saliera verde es suerte del caso, no merito de la
  guarda. Y la de REPORTE (acta 4.6): "7 esperan otra fase: 4 a
  OP-M-01/FUSION, 1 a las siete OP-D" enumera CINCO donde dice siete;
  los dos que faltan son OP-E-03 (por OP-U-02) y OP-M-03-ENLACES (por
  OP-M-03-I/II/III). El total de 7 es correcto, la enumeracion no. Vive
  en prosa: se registra, se relee al doble, NO acumula.
  (2.4) MI PROPIA CAIDA, que registro con mi nombre igual que las tuyas
  (acta 4.8), y es de una especie nueva: CAIDA DE ENCARGO DEL AUDITOR.
  Te pedi la cuenta de "ejecutable hoy" sobre el campo estado, en un
  encargo que en su mismo punto 4.2 sospechaba que ese campo estaba
  rancio. La pregunta estaba mal puesta y por eso la respuesta es
  aritmeticamente correcta y semanticamente vacia. Y arrastra el "tres
  ficheros de tramo" del mismo encargo cuando la medicion dice CUATRO:
  lo declaraste bien y tenias razon.
  (2.5) LA RELECTURA AL DOBLE que las caidas disparan, para esta vuelta:
  (a) TODA CIFRA AGREGADA QUE RESUMA FILAS CON CORRECCIONES DECLARADAS
  lleva pegado el comando del instrumento de la TAREA 1, y (b) TODA
  ENUMERACION INTRODUCIDA POR DOS PUNTOS se cuenta antes de escribirla:
  si dice siete, se enumeran siete o se escribe "cinco de los siete".

- TAREA 3, LAS DOS RELECTURAS CONJUNTAS. Van ANTES que la TAREA 4 y
  ANTES de tocar ninguna cifra de cierre, para que el numero se escriba
  UNA sola vez y no dos.
  (3.1) EL PAR 175, que TU marcaste como discutible 4 y donde DISCREPO.
  MI CASO, para que lo verifiques contra el grafo: el paso 2 de
  validar_modelo_financiero es CALCULAR CAC, tasa de conversion y LTV
  dentro de un modelo financiero. valor_de_vida_del_cliente tiene cuatro
  pasos y SOLO EL PRIMERO CALCULA: el 2 monitorea, y el 3 y el 4 son
  INTERVENCION OPERATIVA ("implementar nuevos programas y ofertas que
  incrementen el LTV", "mejorar la eficiencia de los procesos de
  retencion y crecimiento"). Subir el LTV no es un sub-paso de
  calcularlo: es otra actividad. La madre no interviene sobre nada en
  ningun paso, solo mide y proyecta hasta el P&L. El test del 9.6.2
  falla POR EXCESO DE GENERO, no de detalle, y el contraste es el
  ejemplar canonico 2.215, donde los siete pasos del hijo eran los siete
  sub-movimientos del paso 1 de su madre, todos del mismo genero. El
  nombre literal "Customer Lifetime Value" en el paso 2 es tu razon y es
  real, pero el 9.6.2 dice EXPRESAMENTE que la prueba lexica no sirve
  (34 de 46 marcados y solo 1 lo era, 3% de precision): coincidir el
  termino no es caber dentro del paso. MI LECTURA ES NO RESUELTA.
  (3.2) EL PAR 174, y este cae FUERA de tus discutibles marcados, o sea
  que BAJA EL CREDITO DE LA TANDA (AUDITOR.md 1.2). Lo encontre atacando
  un flanco que nadie habia atacado: las RESUELTAS de MENOR
  titulo_ratio. MI CASO: el paso 1 de desarrollo_value_proposition_usp
  es "identificar que hace unico al negocio frente a competidores
  directos", analisis interno. posicionamiento_vs_competidores es una
  CONVERSACION DE VENTA con un candidato a franquiciado, y su propio
  entregable lo dice ("listo para usar en cualquier conversacion con un
  candidato"): preguntar al candidato que otras franquicias considera,
  comparar, responder destacando diferencias incluyendo las propias
  desventajas, y redirigir a panorama general si el competidor es de
  otra industria. TRES de sus cuatro pasos son movimientos de una
  conversacion que el paso 1 no contempla. El hijo NO IDENTIFICA lo que
  hace unico al negocio: PRESUPONE que ya esta identificado y lo
  despliega contra las objeciones de un prospecto. Y tu propia razon
  escrita concede el punto sin verlo, porque dice literalmente "la
  conversacion APLICADA de ese analisis": aplicar un analisis en una
  venta no es ejecutar el analisis. Es exactamente la figura que TU
  nombraste como aviso operativo, EL CASADO POR OBJETO Y NO POR ACCION,
  con la que resolviste bien el 151 y el 103. MI LECTURA ES NO RESUELTA.
  (3.3) EN LAS DOS, TU DECIDES CON LA VARA, no yo (AUDITOR.md 1.3 y
  adjudicacion 4.5 del acta 96: la lectura ciega es control de la clase
  y detector de discrepancia, NUNCA fuente de direccion). Si te
  sostienes, escribe en el 175 por que "implementar programas para subir
  el LTV" cabe dentro de "calcular el LTV", y en el 174 por que una
  conversacion con un prospecto ejecuta "identificar que hace unico al
  negocio". Si se mueven, van con correccion declarada, y la aritmetica
  ya esta hecha para que no la improvises: solo el 175 deja el tramo 4
  en 12/21 (63,6%) y el cierre en 93/90 (49,2%); solo el 174, lo mismo;
  las dos, tramo 4 en 11/22 (66,7%) y cierre en 92/91 (49,7%).

- TAREA 4, LA CORRECCION DE LA CIFRA DE CIERRE EN LOS CUATRO SITIOS, con
  el instrumento de la TAREA 1 y DESPUES de que la TAREA 3 haya
  resuelto, para escribirla una sola vez. SIN BORRAR EL TEXTO VIEJO, con
  correccion declarada, que es la regla de EJECUTOR.md 8 y la que ya
  aplicaste bien dos veces. Los cuatro sitios, con su linea leida por mi
  hoy: docs/plan/04_ENLACES.md 412 y 413 (fila de tabla),
  docs/plan/OPERACIONES.jsonl 45 (el ADDENDUM DE CIERRE en la nota de
  OP-E-03), docs/PENDIENTES.md 5042 y 5043 (fila de tabla), y
  docs/loop/REPORTE.md 37. RE-LEE ESAS LINEAS CON grep -n EN TU VUELTA
  antes de tocarlas: la TAREA 2 va a haber movido los numeros de linea
  de PENDIENTES.md.

- TAREA 5, LA RELECTURA AL DOBLE DEL TRAMO 4, que el credito bajado
  obliga (AUDITOR.md 1.2). Las 33 filas 151 a 183, releidas contra el
  grafo con el mismo instrumento y sin tocarle una linea. NO ES UN
  TRAMITE: la discrepancia del 174 salio del flanco de las RESUELTAS, y
  ese flanco lo habias mirado menos. Empieza por ahi: ordena las 13
  afirmadas por titulo_ratio ASCENDENTE y relee las cinco primeras antes
  que ninguna otra. Lo que cambie va con correccion declarada; lo que se
  sostenga se declara sostenido con una linea, no con un parrafo.
  Y DESDE AHORA, y esto es letra nueva que sale de esta caida: la
  muestra adversarial de cada tramo se toma EN LOS DOS FLANCOS, las no
  resueltas de mayor titulo_ratio Y las resueltas de menor. Hasta esta
  vuelta se atacaba siempre un lado, y el error estaba en el otro.

- TAREA 6, LA FASE 04 CONTRA LA EVIDENCIA, que es la pregunta que yo
  puse mal y ahora pongo bien. NO CAMBIES NINGUN ESTADO: es medicion, y
  va a docs/loop/ y al reporte, no al plan.
  EL MOTIVO, medido por mi: el campo estado dice 70 de 71 en LISTA y UNA
  en HECHA, y sin embargo docs/plan/02_DESTEJIDOS.md 4470 trae "EL
  CIERRE DE LA FASE 02, DECLARADO MIDIENDO (19 ago 2026, vuelta 46)" y
  4662 dice que las NUEVE operaciones de esa fase tienen registro de
  cierre escrito; la fase 03 esta CERRADA CON REMISION (00_INDICE.md
  247); y la tabla de fases del 00_INDICE 143 a 155 cuenta las 71 como
  LISTAS con 0 pendientes. O SEA QUE "LISTA" EN ESTE PLAN NO QUIERE
  DECIR "SIN EJECUTAR": quiere decir "con texto decidido", y la
  ejecucion vive en la pagina y en el commit, que es la politica del
  backlog del 14 ago que tu mismo citas en cuatro notas. Toda aritmetica
  de dependencias sobre ese campo mide la vejez del campo.
  LO QUE QUIERO MEDIDO, con instrumento y salida commiteada: para cada
  una de las diez operaciones de la fase 04, y para cada una de sus
  dependencias transitivas, SI EXISTE O NO REGISTRO DE CIERRE ESCRITO en
  la pagina de su fase (o en su propia nota), con la cita de fichero y
  linea. Una dependencia con cierre escrito NO bloquea aunque su campo
  diga LISTA; una sin cierre escrito bloquea aunque el plan la de por
  buena. LA CUENTA QUE ME INTERESA AL FINAL: cuantas de las diez tienen
  TODAS sus dependencias transitivas con cierre escrito. DECLARA LAS
  DIVERGENCIAS ENTRE EL CAMPO Y LA EVIDENCIA, no las resuelvas, y NO
  ABRAS NINGUNA FASE NUEVA: que se hace con la fase 04 es decision del
  acta 100, y si me pasa de mi, del fundador.
  SI LA TAREA 6 NO CABE CON SUS GUARDAS COMPLETAS, ES LA UNICA QUE
  PUEDES DEJAR PARA LA VUELTA SIGUIENTE, y lo dices con la cifra de lo
  que si hiciste. Las TAREAS 1 a 5 no se recortan.

- LA DERIVA DE CONTENIDO (26 nodos de 140, 32 pares de 87, acta 92
  seccion 4.4), LOS SIETE NODOS CON GUION y la figura nueva del bloque
  repetido de formalizar_un_proceso_ad_hoc siguen ANOTADOS PARA ALEXIS Y
  SIN ENCARGAR, porque rozan el ALCANCE de la campana. No los toques.
  Citarlos como contraste, con su fuente nombrada, es correcto.

- ARREGLA TAMBIEN, y es de un minuto: el script de mutacion de la vuelta
  99 imprime literalmente "FILAS DE PARTIDA: %d." porque el formato no
  se interpola. No publica un numero falso, publica un hueco donde iba
  uno. Lo registro como nota de instrumento y no como caida.

- LO QUE HICISTE BIEN Y NO QUIERO QUE SE PIERDA ENTRE LAS CORRECCIONES:
  la lectura de las 33 es solida y las adjudique nueve veces a ciegas
  con siete coincidencias; el 2.796 lo remediste en vez de heredarlo; la
  fecha del addendum salio de git y no de tus dedos; la idempotencia se
  disparo en vivo y en rojo; la aditividad es real, cero caracteres
  borrados en los cuatro ficheros; y declaraste TU SOLO la apertura sin
  sellar en vez de esperar a que la encontrara yo. LA REGLA QUE SE SUMA
  ESTA VUELTA: TODA CIFRA QUE AGREGUE FILAS SOBRE LAS QUE HAY
  CORRECCIONES DECLARADAS SE CUENTA CON UN INSTRUMENTO QUE APLIQUE ESAS
  CORRECCIONES, Y ESE INSTRUMENTO CAE EN ROJO SI ENCUENTRA UNA QUE NO
  SEPA APLICAR.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
