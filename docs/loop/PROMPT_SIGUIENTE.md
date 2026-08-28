Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 122. El acta de la 121 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final). Lo que dice, en corto: el trabajo
material de la 121 es bueno y lo ratifique al digito con mis propios
instrumentos. OP-S-03, OP-S-04 y OP-S-05 cierran, las tres escrituras son
quirurgicas, ningun otro campo se toco, y mi barrido propio sobre los
3.188 vivos confirma export.gov en CERO y trade.gov en CUATRO. Adjudique
los dos PENDIENTES DE DOCTRINA sin doctrina nueva: el (b) citando la
adjudicacion escrita de OP-S-05, y el (c) citando el punto 2 de la
decision del fundador del 28 ago 2026. No hay parada: ninguna de las diez
condiciones se dispara.

Lo que la vuelta cobro es el dictado, y son tres, las tres FUERA de los
discutibles marcados y las tres de la especie que el acta 120 ya habia
doblado. Estan en el acta 121 como 4.1, 4.2 y 4.3, y las tres se
corrigen en la TAREA 2 de abajo.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 121 seccion 5). Sigue
vivo el tramo de la 120, TODA CALIFICACION TECNICA QUE EL REPORTE
COMPRIMA RESPECTO DE SU REGISTRO LARGO, y le anado DOS RAMALES NUEVOS,
que son de donde salieron las tres caidas:
  (i) NINGUNA MEDICION SE ATRIBUYE A UN ESTADO QUE NO ES EL SUYO. Ni a
  una vuelta, ni a un lado (APERTURA contra CIERRE), ni a un checkpoint.
  Antes de escribir "el motor de X paso 25/25" se abre el fichero de X y
  se lee. La 121 llamo "motor APERTURA real" a un fichero que ella misma
  habia declarado nueve lineas antes como medido despues de las dos
  escrituras.
  (ii) EL EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO ESCRITO A SU
  LADO. Si docs/PENDIENTES.md transcribe una linea viva, ninguna fila de
  docs/plan/OPERACIONES.jsonl puede declararla resuelta. La 121 escribio
  "generalizando Quantcast" en la nota de OP-S-05 mientras su propia
  Entrada 7 de PENDIENTES.md transcribia la linea con Quantcast dentro,
  viva y sin tocar.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA
  ANTES DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA
  OPERACION: git rev-parse HEAD, hash completo de 40 caracteres, UNA
  linea, a docs/loop/SALIDA_V122_HEAD_APERTURA.txt. Al terminar la ultima
  operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V122_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 122 tiene
  que dar VERDE EXIT 0, y su salida se cita en el reporte. La 120 y la
  121 lo hicieron bien las dos; se repite igual.
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V122_GATE0_CMD1_<LADO>.txt   (scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V122_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V122_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V122_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V122_TSC_<LADO>.txt          (cd web y npx tsc --noEmit)
    docs/loop/SALIDA_V122_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V122_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  Y ANTES DEL COMMIT DEL REPORTE, la comprobacion que EJECUTOR.md pide
  literal (regla del 20 ago 2026):
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 122 --comparar docs/loop/REPORTE.md
  tiene que dar CABECERA IDENTICA AL TALLADOR, y esa salida se pega en el
  reporte. La 121 lo dejo en ROJO y lo declaro bien, sin publicar una
  cabecera a mano en silencio. ESTA VUELTA TIENE QUE SALIR VERDE: si
  vuelve a caer en ROJO, son DOS VUELTAS SEGUIDAS con el tallador rojo y
  eso ya entra en la condicion de fallo tecnico repetido de AUDITOR.md
  seccion 4.
  (1.c) EL ORDEN QUE LA 121 ROMPIO DOS VECES, Y ESTA VUELTA ES
  BLOQUEANTE, NO CONSEJO. El encargo de la 121 decia literal "no se corre
  run_phase1.py solo, nunca", y se corrio solo y se midio encima dos
  veces: en la apertura (SALIDA_V121_MOTOR_APERTURA.txt, 71 divergentes)
  y otra vez despues de las escrituras
  (SALIDA_V121_OPS03_MOTOR_POST_PRIMER_INTENTO.txt, 79 divergentes). La
  regla, entera:
    NINGUNA salida de guarda se captura mientras el ciclo de tres este a
    medias. El ciclo es run_phase1.py --reaplico-curaduria, luego
    etiquetas_de_cara.py --aplicar, luego sync_assets_web.py, EN ESE
    ORDEN, y solo cuando git diff --numstat sobre dataset/, web/ y
    engine/ este en CERO se empieza a medir.
  Y esa comprobacion deja fichero, no palabra: por cada corrida del ciclo
  se escribe docs/loop/SALIDA_V122_CICLO_<ETIQUETA>_NUMSTAT.txt con la
  salida literal de git diff --numstat -- dataset/ web/ engine/ y una
  linea final "EXITCODE: N", con <ETIQUETA> = APERTURA, OPS08, OPS09,
  CIERRE, la que toque.
  (1.d) LA BATERIA POR OPERACION SE MIDE EN SU PROPIO CHECKPOINT, Y ESO
  ES LO QUE CAMBIA RESPECTO DE LA 121 (acta 121, caida 4.4). La 121 dejo
  las cuatro salidas de cada operacion, pero GATE0_POST, MOTOR_POST,
  WEB_POST, ETIQUETAS_POST y SYNC_POST salieron byte a byte identicos
  entre OPS03 y OPS04: una sola medicion con dos nombres, tomada despues
  de las dos escrituras. Lo declaro y por eso no fue mentira, pero la
  guarda no sirve para lo unico que sirve, que es saber a que operacion
  culpar de un rojo. ESTA VUELTA: se escribe la operacion N, se corre su
  ciclo de tres entero, se miden sus cuatro salidas, Y SOLO ENTONCES se
  empieza la operacion N+1. Los ficheros, con <OP> = OPS08, OPS09, etc.:
    docs/loop/SALIDA_V122_<OP>_GATE0_POST.txt
    docs/loop/SALIDA_V122_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V122_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V122_<OP>_TSC_POST.txt
  mas las de etiquetas y sync del ciclo con el mismo prefijo. Si dos
  baterias salen identicas, el reporte lo dice y explica por que.
  Y el tsc deja de evidenciarse con un fichero vacio: TODA salida de tsc
  de esta vuelta termina con una linea "EXITCODE: N" escrita por el
  ejecutor, porque un fichero de cero bytes no distingue "corrio y salio
  limpio" de "no corrio".
  (1.e) UNA GUARDA DE CODIGO NUEVA, PEQUEÑA, Y ES BLOQUEANTE. NO ES LA
  ESCALADA de AUDITOR.md 1.2 (esa sigue reservada para cuando la racha de
  reporte llegue a DOS; hoy esta en UNO). Es el remedio del tramo
  doblado, que ya no se paga solo con lectura porque en la 121 no
  aguanto. Escribe scripts/loop/verificar_citas_del_reporte.py con este
  contrato exacto y nada mas:
    - Lee docs/loop/REPORTE.md y busca los pares (afirmacion, fichero
      citado) sobre un vocabulario CERRADO y corto, en la misma frase o
      en la frase anterior: "25/25", "vacio", "GATE 0 OK" o "Gate 0
      verde", "EXIT 0", "EXIT 1", "ROJO", "IDENTICA AL TALLADOR".
    - Para cada par, abre el fichero citado y comprueba: "25/25" pide que
      el fichero contenga "TODOS LOS TESTS PASARON (25/25)"; "vacio"
      pide que el fichero no tenga ninguna linea que empiece por espacio
      y una letra de estado de git (M, A, D, R) seguida de espacio;
      "Gate 0 verde" pide "GATE 0: OK"; "EXIT 0" pide que no haya
      "EXIT:1" ni "EXITCODE: 1"; "EXIT 1" y "ROJO" piden lo contrario;
      "IDENTICA AL TALLADOR" pide esa cadena literal.
    - Si un par no cuadra, ROJO EXIT 1 diciendo la frase, el fichero y la
      linea. Si cuadran todos, VERDE EXIT 0 con el recuento de pares
      cotejados.
    - Si el reporte cita un fichero que no existe, es ROJO.
  Y llega con su CASO POSITIVO por el criterio de HECHO de la fase 08
  (docs/plan/08_VERIFICACION.md: "una fase esta hecha cuando su
  verificacion se caeria si el fallo volviera"): corre la guarda sobre
  UNA COPIA MUTADA del REPORTE.md de la vuelta 121 en la que la frase del
  git status "vacio" siga citando SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.
  txt, y tiene que dar ROJO. Pega las dos salidas, la del rojo de la
  copia mutada y la del verde sobre el reporte de esta vuelta. La guarda
  se corre ANTES del commit del reporte, junto al tallador.

- TAREA 2, LOS REGISTROS Y CORRECCIONES DEL ACTA 121. Aditivos puros
  donde toque texto viejo, medidos con git diff --numstat y con
  grep -c "^-[^-]" sobre el diff en cero. Son cuatro y el orden da igual.
  (2.a) LA CORRECCION DE OP-S-05, QUE ES LA MAS CARA DE LAS TRES CAIDAS
  (acta 121, seccion 4.3). En docs/plan/OPERACIONES.jsonl, la fila de
  OP-S-05 dice hoy, en su segundo punto de verificacion, "CUMPLIDO POR
  REMISION (vuelta 121): Quantcast y las seis muertas de OP-S-04,
  generalizados", y su nota repite "generalizando Quantcast junto con las
  seis muertas". ES FALSO Y LO MEDI: Quantcast NO fue generalizado, vive
  hoy en inteligencia_de_anuncios_de_la_competencia.pasos_accionables[1],
  el mismo nodo y la misma linea que la Entrada 7 de docs/PENDIENTES.md
  transcribe literal. MIDELO TU PRIMERO contra el grafo de hoy y pega el
  texto vivo; no lo copies de este encargo. La correccion va POR
  REMISION, sin borrar una sola letra del texto viejo: correccion
  declarada al final de la nota y al final de ese punto de verificacion,
  diciendo que Quantcast queda FUERA del alcance de OP-S-05 porque su
  unico sitio vivo es un nodo que ninguna nomina toca, nacido de
  OP-F-04-WEI el 14 ago 2026, DESPUES del censo del 11 ago; que el punto
  se acota por correccion declarada por el punto 2 de la decision del
  fundador del 28 ago 2026 (docs/loop/paradas/2026-08-28-titulo-nafta-
  ops01-DECISION.md), igual que se hizo con OP-S-01 y OP-S-04; y que la
  anotacion vive en la ficha. LA FILA SIGUE HECHA: el acta 121 seccion
  3.2 ratifica el estado y solo condena la frase. Ninguna otra fila se
  toca.
  (2.b) LA ENTRADA 7 DE docs/PENDIENTES.md SE AMPLIA, ADITIVA, PARA QUE
  NOMBRE LO QUE HOY SOLO TRANSCRIBE. La entrada habla de Alexa y de
  OP-S-04, y la linea que cita lleva TAMBIEN Quantcast, que es el sujeto
  entero de OP-S-05. Anade el parrafo: que la misma linea arrastra las
  DOS averias, la de OP-S-04 (Alexa, muerta) y la de OP-S-05 (Quantcast,
  sin verificar); que las dos quedan anotadas como trabajo post campaña
  por el punto 2 del 28 ago; y que el nodo NO SE TOCA. Texto viejo
  intacto.
  (2.c) EL ACOTAMIENTO DE LA FILA DE FASE 05 EN docs/plan/08_VERIFICACION.md,
  Y ES ADJUDICACION MIA DE HOY (acta 121, seccion 3.3). La fila de la
  fase 05 dice, categorica, "ningun nodo cablea export.gov; ninguna de
  las seis herramientas muertas". Lo primero esta CUMPLIDO y lo medi. Lo
  segundo NO lo esta: Alexa vive en el sexto nodo. Acotar OP-S-04 no
  acota la fila de la fase, y si la fila se queda como esta, la fase 05
  no se puede declarar cerrada sin mentir. Escribe una CORRECCION
  DECLARADA debajo de la tabla, aditiva, citando el punto 2 de la
  decision del 28 ago 2026 (que ya saco el barrido global de NAFTA de la
  campaña dejando viva la fila gemela "ningun id vivo con tratado
  extinto"): la fila de la fase 05 se lee ACOTADA A LAS NOMINAS DE SUS
  OPERACIONES, con el residuo global anotado en las fichas de
  docs/PENDIENTES.md como trabajo post campaña. Nombra las dos fichas
  (vigencia-del-marco-internacional y vigencia-de-herramientas-nombradas)
  y di cuantas entradas tiene cada una HOY, medido, no recordado. La
  tabla vieja no se toca.
  (2.d) LAS DOS CAIDAS DE REPORTE, DONDE VIVE EL REGISTRO LARGO, en
  docs/PENDIENTES.md, seccion nueva R.4 de la vuelta 121, como
  correcciones declaradas: (1) la cabecera de la 121 llamo "motor
  APERTURA real" a SALIDA_V121_OPS03_MOTOR_POST.txt, que es post ambas
  escrituras por declaracion del propio reporte, y no existe ninguna
  medicion de motor en verde en el estado de apertura de esa vuelta; (2)
  la TAREA 3.a de la 121 escribio "git status --porcelain vacio tras el
  rojo" y las tres ultimas lineas del fichero que cita muestran tres
  ficheros modificados, que eran los de la escritura previa. Lo cierto,
  que si verifique yo, es que los dos instrumentos vuelven a caer en ROJO
  EXIT 1 sin escribir nada, con el git status limpio una vez commiteado.
  Y de ahi salen los dos ramales del tramo doblado de arriba, que se
  escriben tambien.

- TAREA 3, EL TRABAJO: DOS OPERACIONES, Y EL SUELO ES DOS.
  MODO AUSTERO 1 pide dos cuando quepan, y MEDI HOY que la primera cabe
  entera. LAS TRES GUARDAS DE TODO INSTRUMENTO QUE ESCRIBA en dataset/ o
  en docs/plan/ SIGUEN VIGENTES Y SON BLOQUEANTES: (i) SIMULACION PREVIA
  sobre copia en memoria con su salida pegada, (ii) SU MUTACION NEGATIVA
  corrida y pegada, y (iii) SU ROJO REAL EN SEGUNDA PASADA, con la salida
  de git status --porcelain PEGADA DETRAS TAL CUAL SALGA, no descrita. Un
  instrumento de escritura sin las tres NO SE CORRE.
  (3.a) OP-S-08, LOS VEINTE ACCESOS EXTERNOS. ES LA SIGUIENTE POR ORDEN
  (orden 7) Y MEDI HOY QUE ESTA CASI ENTERA EN EL CODIGO. Rastree las
  marcas y las encontre: OP-C-01 en web/lib/compass.ts:163,
  web/lib/engine/planRedactor.ts:53 y las dos rutas de organizer
  (route.ts:63 y stream/route.ts:84, las dos ya llamando
  cargarEntrySeeds(graph)); OP-C-02 en web/lib/engine/graph.ts:189
  (conceptosDeRuta RESUELVE, ya no filtra) y graph.ts:201 (faseDeNodo
  RESUELVE, ya no cae al ?? ideacion); OP-C-03 en graph.ts:274 y
  graph.ts:293, web/app/api/session/start/route.ts:97 y
  web/app/api/project/[id]/world/[pack]/start/route.ts:149; y sus pruebas
  vivas en web/lib/engine/accesosResueltos.test.ts. RE-MIDELO TU, SITIO
  POR SITIO, ANTES DE ESCRIBIR NADA, y publica la cuenta: de los VEINTE
  externos de la nota de OP-S-08, cuantos estan cubiertos por una
  operacion de la fase 0 ya ejecutada y cuantos no. Si salen los veinte,
  OP-S-08 cierra CUMPLIDA CON REMISION, que es el patron ya usado en
  OP-S-01 y en OP-S-05, con la remision nombrada operacion por operacion.
  ADVERTENCIA MEDIDA, Y ES LA PARTE QUE NO ESTA HECHA: la nota de
  OP-S-08 incluye ademas "los 77 alias huerfanos se limpian aqui" y "los
  314 a nodo deprecado NO se tocan". MI CENSO PROPIO DE HOY, leyendo los
  cuatro alias_map_*.json de dataset/metadata/, da 230 claves unicas, 15
  huerfanos y 37 a nodo deprecado, que NO son 77 ni 314. NO RESUELVAS LA
  DISCREPANCIA COPIANDO NI LA MIA NI LA DE LA NOTA: encuentra cual es la
  FUENTE CANONICA de alias que usa el resolutor, cuentala con tu propio
  codigo, publica la cifra de hoy y DECLARA el delta contra las dos. Si
  la fuente canonica no queda clara del codigo, ESO ES PARADA y lo traes:
  no se borra un alias por una cuenta que no se sabe de donde sale.
  (3.b) OP-S-09, EL RENOMBRE CON ALIAS DE 67 IDS. Es la siguiente por
  orden (orden 8) y su nomina vive escrita en el campo nodos de su fila
  de docs/plan/OPERACIONES.jsonl, con el toque unico ya resuelto en la
  vuelta 78 (67 ids, no 69). RE-MIDE LA NOMINA CONTRA EL GRAFO DE HOY
  ANTES DE ESCRIBIR, como se hizo con OP-S-02 y con OP-S-04: cuantos de
  los 67 siguen vivos, cuantos estan deprecados y a quien reclama el
  alias de cada deprecado. SI LA NOMINA SALE INTACTA, la operacion se
  ejecuta entera con sus tres guardas. SI LA NOMINA SE MOVIO, paras en el
  censo, publicas el remapeo nodo por nodo con la correccion declarada, y
  ESO ES ENTREGA COMPLETA, no un limite de alcance: lo digo yo aqui por
  escrito para que no haya duda.
  EL SUELO ES DOS OPERACIONES ABIERTAS Y MEDIDAS. Si alguna no cierra, el
  reporte publica LA CUENTA DE GUARDAS que consumio la vuelta, guarda por
  guarda con su fichero, y no la palabra "limite de alcance" a secas.
  OP-S-12 va al final de la fase y no se abre esta vuelta.
  Y AVISO CON TIEMPO, PORQUE FALTAN POCAS: cuando la fase 05 quede
  cerrada y verificada se dispara la condicion de parada CIERRE DE LA
  FASE 05 de AUDITOR.md seccion 4. NO declares la fase cerrada tu: mide,
  publica y dilo como discutible; el cierre lo adjudica el auditor, y no
  se podra adjudicar hasta que la TAREA 2.c este escrita.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
