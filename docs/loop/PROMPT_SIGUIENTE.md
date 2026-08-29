Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 126. El acta de la 125 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final). Lo que dice, en corto: LA VUELTA
125 HACE BIEN TODO LO QUE SE LE PIDIO. Las diez filas de la cabecera me
salen identicas con mis instrumentos, mi Gate 0 sale byte a byte igual al
tuyo, el ciclo de tres deja el arbol quieto a la primera, las tres
guardas del REGIMEN B estan enteras y de verdad (simulacion con cero
escrituras, mutacion negativa que aborta sin escribir, rojo real en
segunda pasada con el porcelain pegado), y los cuatro pares REPITE estan
fundidos limpios: cuatro muertos, cuatro alias, cero resucitados, cero
ids nuevos, cero auto-aristas, cero duplicadas, cero vivos citando a un
muerto sin resolver, todo comprobado por mi con codigo propio. Tu mapeo
CUBIERTO me sale identico al mio leido a ciegas, y los dos APPEND son
genuinos, verificados en el grafo. Las dos discrepancias de mi ciega de
la 124 se cerraron las dos con la vara citada por fichero y linea, y las
dos moviendose contra tu propia lectura anterior: eso no es una caida,
es el procedimiento funcionando (precedente del acta 110).

LO QUE ESTA VUELTA COBRA, Y LO GRUESO ES MIO:

  UNA CAIDA TUYA, DE REPORTE, QUE NO ACUMULA (acta 125, 5.1): la linea de
  identidad llama "HEAD apertura 486ac73a" al HIJO del acta. El HEAD
  sellado de apertura es c9ac2fb8, que es lo que dice tu propio
  SALIDA_V125_HEAD_APERTURA.txt y lo que publica bien la fila de identidad
  de la cabecera tallada dos lineas mas abajo. La 124 escribia la forma
  correcta ("HEAD apertura 6d512a0d (acta 123, sellado antes de la 1.ª
  operacion)"). Vive en prosa y no mueve dato: se registra, dispara la
  relectura al doble, y NO acumula (letra del 27 ago). Se arregla en 1.a.

  UNA CAIDA MIA, DE ENCARGO, Y ES LA GRANDE (acta 125, 5.2): el contrato
  de guarda que dicte en la 1.g de la 124 tiene cinco comprobaciones y la
  (4) NO PUEDE CAER NUNCA. Pregunta "x == muere and resolver(x) != sup", y
  como el resolutor se construye del ids_alias del superviviente, en
  cuanto la (2) pasa la (4) es inalcanzable. Lo probe por mutacion propia:
  mute fijacion_de_metas para que volviera a citar a dia_cero_defectos_3
  con el alias intacto, que es EXACTAMENTE el fallo que la (4) dice
  vigilar, y tu guarda dio CERO FALLOS. Escribiste mis cinco puntos con
  fidelidad y corriste el unico caso positivo que te pedi. La guarda no
  vio nada porque yo no le pedi que mirara. Se arregla en 1.g.

  UNA CAIDA MIA, DE CIFRA (acta 125, 5.3): en el acta 124 publique el
  cableado de auditoria_de_producto como 8 (5 salientes, 3 entrantes).
  Son 7 (4 salientes, 3 entrantes): el quinto saliente,
  ciclo_de_retroalimentacion_control, esta DEPRECADO. Tu mediste 7 y lo
  publicaste sin copiarme, que es el instrumento mandando.

Y LO QUE ENCUENTRO FUERA DE LOS DISCUTIBLES MARCADOS, QUE NO SE TE COBRA
Y ES EL TRABAJO DE ESTA VUELTA:

  LA FUSION DE OP-S-09 CORTO UNA ARISTA ENTRE DOS NODOS VIVOS Y NO LA
  REPUSO NI LA DECLARO. Medido por mi: proyecte el grafo de c9ac2fb8 por
  el resolutor de hoy, me quede con las aristas vivo-vivo, y las reste
  contra las de hoy. PRE proyectadas 7.293, POST 7.292, PERDIDAS 1,
  NUEVAS 0. La perdida es dia_cero_defectos_2 -> eliminacion_causas_error_4,
  que antes de la vuelta existia como dia_cero_defectos_3 ->
  eliminacion_causas_error entre dos nodos vivos.
  POR QUE SE CAYO, y no es un descuido de teclado: fundir_por_plan.py
  redirige las listas de los nodos VIVOS que citan al absorbido, en una
  pasada al final. Cuando el que cita al absorbido es OTRO ABSORBIDO DE LA
  MISMA OPERACION, esa pasada ya no lo ve: eliminacion_causas_error murio
  en el acto 3 y su lista quedo intacta como registro historico, con
  dia_cero_defectos_3 dentro. La arista queda entre dos deprecados,
  resolviendo perfecto hacia atras y sin existir hacia adelante. Tu propia
  fila nueva de desfase del calibrado la ve por eso mismo.
  Y NO ES DE LABORATORIO: dia_cero_defectos_2 paso 6 dice hoy "Iniciar al
  dia siguiente el programa de eliminacion de causas de error", el nodo
  eliminacion_causas_error_4 esta VIVO, y nada lleva del uno al otro. Eso
  es contenido huerfano de camino, banco 9.6, docs/BANCO_DE_TEXTOS.md:1479.
  ADJUDICADO EN EL ACTA 125 SECCION 4.1, SIN DOCTRINA NUEVA, con tres
  reglas escritas: banco 9.8 (docs/BANCO_DE_TEXTOS.md:1841, "cada arista
  que no se reconstruye es contenido huerfano de camino"), banco 9.6 (el
  remedio es un enlace y no se toca ni un texto), y P.16 punto 1
  (docs/plan/BANCO_DEL_PLAN.md:878, quien fabrica limpia en su mismo
  commit). Que P.16 gobierne el faltante y no solo el sobrante es
  EXTENSION MIA y va declarada como tal en el acta 125 seccion 4.3.
  EL PASIVO HISTORICO, medido por mi sobre el catalogo entero: 39 aristas
  de esta especie. UNA es de hoy. LAS OTRAS 38 NO SE TOCAN: son el gemelo
  exacto de las 33 auto-aristas y las 1.056 duplicadas que P.16 declaro
  pasivo historico. Van a ficha y a nada mas.

  POR ESO OP-S-09 NO SE DECLARO HECHA EN LA 125 Y HOY SI SE CIERRA: tus
  cuatro verificacion estan cumplidas al digito y las comprobe una a una,
  pero una operacion que deja el catalogo con una arista menos y no lo
  dice no esta hecha. Queda CERRABLE, no cerrada, y el acto que la cierra
  es la TAREA 3.b de esta vuelta, DESPUES de que 3.a este verde.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 125 seccion 6), y otra
vez por la regla dura: la arista perdida y la etiqueta del HEAD caen las
dos FUERA de los discutibles que el reporte marco. Siguen vivos el tramo
de la 120 con sus ramales (i) NINGUNA MEDICION SE ATRIBUYE A UN ESTADO
QUE NO ES EL SUYO, (ii) EL EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO
ESCRITO A SU LADO, (iii) NINGUNA GUARDA SE ESTRECHA EN SILENCIO, (iv)
TODA CIFRA SOBRE UN ARTEFACTO CONTABLE SE LEE DE LA SALIDA DEL
INSTRUMENTO PEGADA AL LADO, el (v) de la 123 NINGUNA VARA SE ESTRECHA EN
EL ENCARGO, y el (vi) de la 124 UN SUPERVIVIENTE SE RAZONA COMO SE RAZONA
UNA CLASE. Le anado el septimo:
  (vii) UNA FUSION NO ACABA CUANDO EL ALIAS QUEDA ESCRITO, SINO CUANDO LA
  ULTIMA ARISTA DEL ABSORBIDO ESTA RECONSTRUIDA. Si dos absorbidos de la
  misma operacion se citaban entre ellos, esa arista no la ve ninguna
  pasada de redireccion sobre nodos vivos, y el resolutor la sigue viendo
  desde el muerto, asi que ningun instrumento acusa. Se mide como se mide
  todo lo demas: aristas vivo-vivo antes y despues, proyectadas por el
  alias de hoy, y la resta se publica.

LA ESCALADA de AUDITOR.md 1.2 se dispara con la racha de reporte en DOS.
Estamos en CERO de las que acumulan. NO TOCA, y la dejo dicha entera para
que nadie la de por gastada.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros, TAREA 3
trabajo, y lo mantengo porque las guardas son bloqueantes y van delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V126_HEAD_APERTURA.txt. Al terminar la ultima operacion
  y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V126_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 126 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte.
  Y LA CORRECCION DE LA CAIDA 5.1: la linea de identidad del reporte
  nombra TRES cosas y con estos tres rotulos exactos, sin mezclarlos:
  "HEAD sellado de apertura" (el que esta DENTRO de
  SALIDA_V126_HEAD_APERTURA.txt, o sea el commit del acta), "commit de
  nacimiento de las salidas de apertura" (el primer commit de la vuelta,
  el que verificar_apertura_sellada.py nombra como padre-hijo) y "HEAD
  sellado de cierre". Si los tres no se leen de un fichero o de git en esa
  misma linea, no se escriben.
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V126_GATE0_CMD1_<LADO>.txt   (scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V126_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V126_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V126_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V126_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V126_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V126_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio, y sigue
  prohibido el fichero de cero bytes.
  (1.c) EL CICLO DE TRES, IGUAL QUE LA 125. NINGUNA salida de guarda se
  captura mientras el ciclo este a medias. El ciclo es run_phase1.py
  --reaplico-curaduria, luego etiquetas_de_cara.py --aplicar, luego
  sync_assets_web.py, EN ESE ORDEN, y solo cuando git diff --numstat sobre
  dataset/, web/ y engine/ este en CERO se empieza a medir. Por cada
  corrida se escribe docs/loop/SALIDA_V126_CICLO_<ETIQUETA>_NUMSTAT.txt
  con la salida literal y una linea final "EXITCODE: N". MEDIDO POR MI HOY
  SOBRE TU ARBOL: etiquetas_de_cara.py --aplicar reasienta 71 etiquetas y
  aun asi el numstat cierra en CERO a la primera pasada. Si a ti no te
  cierra, NO midas: repite el ciclo y dilo.
  (1.d) LA BATERIA POR OPERACION, EN SU PROPIO CHECKPOINT, Y CON SU
  COMPROBACION MECANICA. Se escribe la operacion N, se corre su ciclo de
  tres entero, se miden sus cuatro salidas, Y SOLO ENTONCES empieza la
  N+1. Ficheros, con <OP> = OPS09REP (la reposicion de 3.a), OPS10, etc.:
    docs/loop/SALIDA_V126_<OP>_GATE0_POST.txt
    docs/loop/SALIDA_V126_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V126_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V126_<OP>_TSC_POST.txt
  mas las de etiquetas y sync del ciclo con el mismo prefijo. Antes de
  escribir el reporte corres cmp -s sobre CADA par de salidas homologas de
  la vuelta (apertura contra cierre, y cada bateria contra la anterior),
  vuelcas el resultado literal a docs/loop/SALIDA_V126_BATERIAS_CMP.txt
  con una linea por par que diga IDENTICOS o DISTINTOS, y EL REPORTE LISTA
  LOS IDENTICOS Y EXPLICA POR QUE LO SON. LA LETRA DE ESA EXPLICACION SE
  AFINA HOY, PORQUE LA MIA DE LA 125 PEDIA UN numstat QUE EN UNA VUELTA
  QUE ESCRIBE EN dataset/ NO PUEDE PROBAR NADA: la explicacion es POR QUE
  ESA SALIDA NO DEPENDE DE LO QUE LA OPERACION TOCO, con el fichero o el
  campo nombrado. Y SI ALGUN par DISTINTO no lo explicas, lo abro yo: en
  la 125 abri OPS09_GATE0_POST contra CIERRE y salio una sola linea de
  diferencia, la reciprocidad completandose. ESTA VUELTA TAMBIEN ESCRIBE
  EN dataset/: si Gate 0 o el conteo salen IDENTICOS entre apertura y
  cierre despues de 3.a, eso NO es determinismo, es que la escritura no
  llego; se investiga y se declara antes de publicar nada.
  (1.e) LAS GUARDAS DE CITAS Y DE TITULOS NO SE TOCAN. Se corren
  verificar_citas_del_reporte.py, verificar_titulos_normalizados.py y sus
  autopruebas (vuelta122_tarea1e_mutacion_citas.py,
  vuelta123_tarea1e_mutacion_fila_tabla.py, y
  verificar_titulos_normalizados.py --autoprueba), y se pegan. NO se
  modifica ninguna de las dos. La excepcion declarada de
  sistema_responsabilidad_gerencial se queda EXACTAMENTE como esta: 3.a no
  deprecia a ninguno de los dos.
  (1.f) LA GUARDA DE CIFRAS DEL PLAN, TAMPOCO SE TOCA. Se corre
  verificar_cifras_del_plan.py y sus dos casos positivos
  (vuelta123_tarea1f_caso_positivo.py y
  vuelta124_tarea1f_caso_positivo_ventana.py). Los tres verdes o rojos
  donde tocaba, pegados.
  (1.g) EL ENSANCHE DE verificar_fusion_ops09.py, QUE ES LA CORRECCION DE
  MI CAIDA 5.2. BLOQUEANTE, Y VA ANTES DE 3.a. La comprobacion (4) actual
  es inalcanzable y se REEMPLAZA, no se le anade una sexta al lado.
  Contrato nuevo de la (4):
    - POR CADA ABSORBIDO, se leen sus DOS listas (nodos_siguientes y
      nodos_previos) TAL COMO QUEDARON EN EL NODO MUERTO, que es el
      registro historico y sigue ahi.
    - Cada id de esas listas se resuelve con el resolutor de hoy. Si
      resuelve a un nodo VIVO distinto del superviviente, entonces esa
      arista TIENE QUE EXISTIR HOY entre el superviviente y ese nodo vivo,
      en la direccion que tenia (lo que estaba en nodos_siguientes del
      muerto va de superviviente hacia alla; lo que estaba en
      nodos_previos viene de alla hacia el superviviente), mirando LAS DOS
      VISTAS para darla por presente.
    - Si no existe, ROJO EXIT 1 nombrando el par, la arista que falta y de
      que id muerto venia.
    - Los ids que resuelven al PROPIO superviviente no cuentan (esa es la
      arista interna que P.16 manda retirar) y los que resuelven a un
      nodo que sigue DEPRECADO tampoco (no hay a donde llevarla).
  CASO POSITIVO POR MUTACION, en memoria y sin tocar disco, y van DOS:
    (i) sobre una copia del grafo se borra del superviviente una arista
        heredada de su absorbido y tiene que dar ROJO nombrandola;
    (ii) se corre la guarda contra el grafo de c9ac2fb8 con --ref, ANTES
        de tu reposicion de 3.a: como la arista aun no esta puesta, la (4)
        nueva tiene que dar ROJO nombrando dia_cero_defectos_2 ->
        eliminacion_causas_error_4. ESA ES LA PRUEBA DE QUE MUERDE: la
        guarda vieja daba VERDE sobre ese mismo estado.
  Las dos salidas se pegan. Y EL REPORTE DICE, con todas sus letras, que
  la (4) vieja era inalcanzable y que la nueva la reemplaza: NINGUNA
  GUARDA SE ENSANCHA NI SE ESTRECHA EN SILENCIO, ramal (iii).
  (1.h) LA GUARDA NUEVA DE ARISTAS, Y ES LA QUE FALTABA EN LA CASA.
  BLOQUEANTE. Escribe scripts/loop/verificar_aristas_vivas.py con este
  contrato, que se corre DESPUES de cada operacion que escriba en dataset/
  y cuya salida se pega:
    - Uso: --antes <ref de git> --despues WORK.
    - Construye, en cada lado, el conjunto de aristas VIVO-VIVO (un nodo
      no deprecado que cita a otro no deprecado, mirando las dos vistas y
      normalizando cada arista a un par ordenado origen-destino).
    - PROYECTA el conjunto de "antes" por el resolutor de "despues" (cada
      extremo se resuelve; se descartan los pares cuyo extremo resuelto ya
      no esta vivo y las auto-aristas resultantes).
    - Imprime, con estas cuatro cifras y en este orden: aristas vivo-vivo
      ANTES proyectadas, aristas vivo-vivo DESPUES, PERDIDAS, NUEVAS; y
      lista los pares de las dos ultimas.
    - ROJO EXIT 1 si PERDIDAS no es cero. VERDE EXIT 0 si lo es.
    - CASO POSITIVO POR MUTACION, en memoria y sin tocar disco: sobre una
      copia del grafo de "despues" se borra una arista vivo-vivo y tiene
      que dar ROJO nombrandola. Pegalo.
  MI CONTRASTE, MEDIDO HOY Y NO PARA COPIAR: con --antes c9ac2fb8
  --despues WORK sobre el arbol que dejo la 125, me sale ANTES proyectadas
  7.293, DESPUES 7.292, PERDIDAS 1 (dia_cero_defectos_2 ->
  eliminacion_causas_error_4), NUEVAS 0. MIDELO TU con tu propio codigo.
  SI TU MEDICION DISCREPA DE LA MIA, LA DECLARAS, NO LA RESUELVES
  COPIANDO. Y tras 3.a, la misma corrida tiene que dar PERDIDAS 0.
  (1.i) ANTES DEL COMMIT DEL REPORTE, LAS CUATRO COMPROBACIONES, y las
  cuatro salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO (esa es
  la observacion 5.5 del acta: en la 125 los tres SALIDA_V125_1H_*_FINAL
  no se citaron y la seccion se rotulo con la letra equivocada):
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 126 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras tres
  VERDE EXIT 0.
  (1.j) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte,
  medida. La 125 lo cumplio en 80 exactos.
  (1.k) LOS DOS REGIMENES DE ESCRITURA SIGUEN COMO LOS DEJO LA 125 Y NO SE
  TOCAN:
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o
      a docs/ se mide con git diff --numstat y con grep -c "^-[^-]" sobre
      el diff en cero, mas git diff --word-diff=porcelain pegado si toca
      una linea vieja. NO necesita las tres guardas.
    - REGIMEN B, DATO: un instrumento que escribe en dataset/, o que
      EJECUTA una operacion, lleva LAS TRES GUARDAS COMPLETAS: (i)
      SIMULACION PREVIA sobre copia en memoria con su salida pegada, (ii)
      SU MUTACION NEGATIVA corrida y pegada, y (iii) SU ROJO REAL EN
      SEGUNDA PASADA, con git status --porcelain PEGADO DETRAS TAL CUAL
      SALGA. Un instrumento de REGIMEN B sin las tres NO SE CORRE.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE. Un instrumento sin regimen declarado no existe para el
      expediente.

- TAREA 2, LOS REGISTROS Y CORRECCIONES DEL ACTA 125. REGIMEN A. Aditivos
  puros donde toquen texto viejo, medidos con git diff --numstat y con
  grep -c "^-[^-]" sobre el diff en cero. Son tres y el orden da igual,
  pero 2.a se escribe DESPUES de que 3.a este verde, porque cita su
  resultado medido.
  (2.a) LA CORRECCION DECLARADA DE LA ARISTA, EN LA PROPIA OPERACION. En
  docs/plan/OPERACIONES.jsonl, en el campo nota de la fila de OP-S-09, al
  final, una correccion declarada que diga: que la ejecucion de la vuelta
  125 corto UNA arista vivo-vivo y no la declaro; cual es, con sus dos
  extremos de hoy y sus dos extremos de ayer; POR QUE se corto (el citante
  era otro absorbido de la misma operacion y la pasada de redireccion solo
  mira vivos); las CUATRO CIFRAS QUE TU MIDAS con verificar_aristas_vivas.py
  antes y despues de la reposicion, con el fichero de salida citado al
  lado; y las tres varas de la adjudicacion del acta 125 seccion 4.1
  (banco 9.8 en docs/BANCO_DE_TEXTOS.md:1841, banco 9.6 en :1479, y P.16
  punto 1 en docs/plan/BANCO_DEL_PLAN.md:878), diciendo que la aplicacion
  de P.16 al faltante es EXTENSION declarada del auditor y revocable.
  (2.b) EL REGISTRO LARGO EN docs/PENDIENTES.md, seccion nueva R.8 de la
  vuelta 125, como correcciones declaradas: (1) la caida de reporte de la
  etiqueta "HEAD apertura", con los dos hashes y su rotulo correcto;
  (2) la caida MIA de la guarda con la comprobacion inalcanzable, que dice
  con todas sus letras QUE ES DEL AUDITOR, con la mutacion que la
  desenmascaro y la cita del criterio de HECHO (docs/plan/08_VERIFICACION.md:9,
  "correr la prueba ANTES del arreglo. Si pasa, no prueba nada"), y que la
  remedia la 1.g de esta vuelta; (3) la caida MIA de cifra, el cableado 8
  contra 7, diciendo que conte un vecino deprecado usando un metodo
  distinto del que declare dos parrafos mas abajo en la misma acta; y (4)
  el ramal (vii) del tramo que se relee al doble, escrito entero.
  (2.c) LA FICHA NUEVA docs/PENDIENTES.md, permanente, con el nombre
  aristas-huerfanas-por-fusion, aditiva y con su primera entrada: que
  existe una especie de perdida que ningun instrumento de la casa acusaba,
  la arista entre dos absorbidos de la misma operacion cuyos supervivientes
  quedan sin enlazar; que el resolutor la sigue viendo desde el muerto y
  por eso ni Gate 0 ni el conteo ni el desfase la delatan; CUANTAS HAY EN
  EL CATALOGO DE HOY (MIDELO TU con el mismo codigo de 1.h ampliado a todo
  el grafo; mi contraste, medido hoy y NO para copiar, es 39 en total, de
  las cuales 1 es de la vuelta 125 y 38 son de fusiones anteriores); que
  la de la 125 se repone en esta vuelta por P.16; y que LAS OTRAS NO SE
  TOCAN, por la misma letra de P.16 que dejo las 33 auto-aristas y las
  1.056 duplicadas como pasivo historico: son trabajo post campana y
  crear su operacion no lo decide el bucle. NO REPONGAS NINGUNA DE LAS 38.

- TAREA 3, EL TRABAJO.
  (3.a) LA REPOSICION DE LA ARISTA. REGIMEN B, LAS TRES GUARDAS COMPLETAS
  (1.k). BLOQUEANTE Y VA PRIMERA, porque 3.b depende de que salga verde.
  Se repone UNA arista y UNA sola: dia_cero_defectos_2 ->
  eliminacion_causas_error_4, en las dos vistas (nodos_siguientes del
  origen y nodos_previos del destino, que es como el ciclo de tres la deja
  de todos modos). Guardas de la propia reposicion, ademas de las tres del
  REGIMEN B: cero auto-aristas y cero duplicadas nuevas tras resolver, los
  dos nodos siguen VIVOS, ningun otro campo de ninguno de los dos se toca
  (numstat que lo pruebe), y verificar_aristas_vivas.py --antes c9ac2fb8
  --despues WORK pasa de PERDIDAS 1 a PERDIDAS 0 con las dos salidas
  pegadas, antes y despues. Detras, su bateria de 1.d entera con etiqueta
  OPS09REP, y la 1.g ensanchada en VERDE.
  SI AL REPONERLA APARECE CUALQUIER COSA QUE NINGUNA REGLA ESCRITA CUBRA,
  PARAS, LA TRAES CON SU CASO ESCRITO, Y SIGUES CON LO DEMAS.
  (3.b) EL CIERRE DE OP-S-09, Y SOLO SI 3.a ESTA VERDE. En
  docs/plan/OPERACIONES.jsonl, el campo estado de la fila de OP-S-09 pasa
  de LISTA a HECHA. NO ES DECISION TUYA: la adjudica el acta 125 seccion
  4.2 y asi se cita. Con el cambio va, en el mismo commit, una nota de
  cierre que recorra LAS CUATRO verificacion UNA POR UNA con la evidencia
  MEDIDA HOY y su fichero al lado:
    1. las familias resueltas por continua o repite: 51 pares, con el
       recuento que tu corras sobre los tres registros;
    2. todo id que muere deja alias: los cuatro pares, con la salida de
       verificar_fusion_ops09.py ya ensanchada;
    3. las aristas que apuntaban al id viejo siguen resolviendo: con la
       (4) NUEVA en verde y con verificar_aristas_vivas.py en PERDIDAS 0;
    4. ningun id vivo lleva sufijo numerico de duplicado: acotada a la
       nomina por la correccion declarada de la vuelta 125, con su unico
       residuo (eliminacion_causas_error_4) remitido a ficha.
  El estado es un campo de docs/plan/: REGIMEN A, numstat y borrados en
  cero, word-diff pegado.
  (3.c) LA REMEDICION DE LAS CIFRAS DERIVADAS DE OP-S-10, por el ramal (v)
  y por la observacion 5.5 del acta 125. Su campo nodos dice 31 y el 31
  cuadra (lo verifique yo: 31 unicos, cero ausentes). Lo que ya no cuadra
  es lo que la NOTA deriva de ese 31: dice "ENTRAN 29 NODOS AL TRABAJO:
  los 31 medidos menos los DOS que ya condicionan en la puerta", y de esos
  31 hoy solo 28 estan VIVOS (tres deprecados con su alias, que tu ya
  publicaste bien en la 125). Remide contra el grafo de HOY, con codigo
  propio y salida pegada, y escribe una correccion declarada aditiva en la
  nota con lo que TE SALGA: cuantos de los 31 estan vivos; cuantos de los
  vivos ya nombran el pais en condiciones_activacion; cuantos no lo
  nombran en ningun sitio; cuantos solo en el resumen; y cuantos de los 8
  que la nota da como "dentro de un acto" siguen vivos. NO CAMBIES el 31
  ni borres el 29: correccion declarada por remision.
  (3.d) EL PRIMER TRAMO DE OP-S-10. REGIMEN B, LAS TRES GUARDAS COMPLETAS.
  La vara del reencuadre NO se inventa: esta dentro de la propia
  operacion. Su verificacion 1 dice "los 31 nodos de marco de franquicias
  nombran EL PAIS en condiciones_activacion" y su verificacion 4 nombra
  los DOS contramodelos que "ya condicionan bien". Leelos: la primera
  condicion de comprender_definicion_legal_franquicia es "Solo aplica si
  vendes o piensas vender franquicias en Estados Unidos" y la de
  cumplimiento_ftc_rule_436 es "Esto aplica solo si vendes o piensas
  vender franquicias en Estados Unidos". ESA ES LA FORMA: una PRIMERA
  condicion de activacion que nombra el pais, delante de las que ya tiene,
  y las demas condiciones intactas.
  ALCANCE DE ESTE TRAMO: los DIEZ primeros nodos VIVOS de la nomina, en
  orden alfabetico de id, que hoy NO nombren el pais en
  condiciones_activacion. Los DOS contramodelos NO se tocan (verificacion
  4). Los tres deprecados NO se tocan.
  Guardas propias del tramo, ademas de las tres del REGIMEN B: ningun otro
  campo de ningun nodo cambia (numstat y diff que lo prueben), las
  condiciones que ya existian quedan enteras y en su orden, cero guiones
  largos y cero guiones medios en el texto nuevo, y el texto nuevo se
  escribe con la voz del banco (docs/BANCO_DE_TEXTOS.md) sin claims
  prohibidos. Detras, su bateria de 1.d entera con etiqueta OPS10 y
  verificar_aristas_vivas.py en PERDIDAS 0 (un reencuadre de texto no debe
  mover ni una arista: si mueve alguna, ES ROJO y paras).
  SI EL TEXTO DE OP-S-10 NO ALCANZA PARA REENCUADRAR ALGUN NODO SIN
  DECIDIR ALGO QUE NINGUNA REGLA ESCRITA CUBRE, PARAS EN ESE NODO, LO
  TRAES CON SU CASO ESCRITO Y SIGUES CON LOS DEMAS. Y si el tramo no cabe
  con sus guardas enteras, eso es entrega completa y no un limite de
  alcance: pasa a la 127 y el reporte publica LA CUENTA DE GUARDAS
  consumidas, guarda por guarda con su fichero.
  MARCA COMO DISCUTIBLE, para que yo lo adjudique: si diez por vuelta es
  el tramo correcto para lo que queda de OP-S-10, y si la forma de la
  primera condicion que escribas debe ser literal la de un contramodelo o
  adaptada al verbo de cada nodo.
  OP-S-11 y OP-S-12 no se abren.
  Y AVISO OTRA VEZ, PORQUE ESTA CERCA: cuando la fase 05 quede cerrada y
  verificada se dispara la condicion de parada CIERRE DE LA FASE 05 de
  AUDITOR.md seccion 4. Con el cierre de 3.b quedan OP-S-10, OP-S-11 y
  OP-S-12. NO declares la fase cerrada tu: mide, publica y dilo como
  discutible; el cierre lo adjudica el auditor.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
