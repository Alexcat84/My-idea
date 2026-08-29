Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

AVISO SOBRE ESA PRIMERA LINEA, Y VA PRIMERO PORQUE PUEDE MORDER: si al
abrir la vuelta `git status` te sale
`dataset/metadata/master_graph.json` modificado y su `git diff` son solo
lineas de `etiqueta_arbol`, ESO NO ES TRABAJO PENDIENTE Y NO SE
COMMITEA: es el borrado de la curaduria que deja detras cualquier
corrida de `run_phase1.py`. Corres `python scripts/etiquetas_de_cara.py
--aplicar` y `python scripts/sync_assets_web.py`, compruebas que
`git diff --numstat -- dataset/ web/ engine/` queda VACIO, y sigues.

Esta es la VUELTA 128. La vuelta 127 NO ENTREGO: corrio tres minutos, no
commiteo nada y se detuvo en un motor ROJO. El acta de la 127 esta
escrita (docs/loop/ACTA_AUDITOR.md, al final) y lo que dice, en corto:
EL ROJO ERA REAL, ERA REPRODUCIBLE, Y LA RAIZ ERA MIA. El orden de
captura que yo escribi en 1.b y 1.c del encargo de la 127 garantizaba
ese rojo. Lo probe hoy en experimento controlado sobre arbol limpio
(docs/loop/SALIDA_AUD_V127_EXPERIMENTO_ORDEN.txt): UNA sola corrida de
`run_phase1.py --reaplico-curaduria` sale EXIT 0 y GATE 0: OK, y su
propio chequeo de gemelos dice 0 divergentes, PORQUE COMPARA EL SNAPSHOT
DE ANTES DEL PASO 6 (asi esta escrito y comentado en run_phase1.py:1176
y :941-947); y esa MISMA corrida deja 72 lineas de diff en
dataset/metadata/master_graph.json y 71 gemelos divergentes EN DISCO, y
detras `python engine/run_all_tests.py` cae en EXIT 1 con
test_gate_alias.py, que si lee los dos ficheros del disco
(engine/test_gate_alias.py:116 y :124). Repare el arbol con el remedio
que el propio run_phase1.py lleva escrito (REMEDIO_SYNC, :931-939) y lo
deje verde: numstat en CERO, gemelos 0, motor 25/25.

NO SE MOVIO UN SOLO DATO DEL CATALOGO EN LA 127, Y LO MEDI: marcador
A 551 / B 72 / C 5 / D 2760 con huecos [] y dups 0; conteo 3.853 nodos,
3.184 vivos, 669 deprecados, sig 9.195, prev 9.177, suma 18.372, union
9.830, auto 0. Identicos al cierre de la 126. Asi que EL ENCARGO DE LA
127 SE REPITE ENTERO, sin quitarle ni anadirle alcance, con el orden de
captura corregido y con los registros de la 127 sumados. Todo lo que
adjudique para la 127 SIGUE ADJUDICADO Y NO SE REABRE: la unidad
canonica del pasivo es el PAR VIVO RESUELTO, el pendiente de doctrina
32 contra 39 esta CERRADO (son dos unidades, no una discrepancia), la
forma de la condicion de OP-S-10 se queda LITERAL, y las tres aristas
fabricadas por la campana se reponen por las tres varas del acta 125
seccion 4.1 (banco 9.8 docs/BANCO_DE_TEXTOS.md:1841, banco 9.6 :1479,
P.16 punto 1 docs/plan/BANCO_DEL_PLAN.md:878) con la misma extension
declarada y revocable del acta 125 seccion 4.3.

LO QUE ESTA VUELTA COBRA:

  UNA CAIDA MIA, DE ENCARGO, Y ES LA GRANDE (acta 127, 4.3): el orden
  imposible de 1.b y 1.c, mas la frase "aun asi el numstat cierra en
  CERO a la primera pasada", que era verdad DEL CICLO y falsa DEL ORDEN
  COMPLETO que yo mandaba, y que ademas te decia que si a ti no te
  cerraba el problema era tuyo. Medi el ciclo y no medi el encargo. Se
  corrige en 1.b y 1.c de este encargo.

  UNA CAIDA MIA, DE PROCEDIMIENTO (acta 127, 4.4): lei un codigo de
  salida desde un `$?` puesto detras de una tuberia, que devuelve el
  codigo de `tail` y no el del instrumento. Lo cace remidiendo. Va
  escrito porque te toca a ti tambien: un EXITCODE leido detras de un
  `|` no es una medicion.

  UNA VUELTA NO ENTREGADA, DEL EJECUTOR (acta 127, 4.1): nueve salidas
  buenas de instrumento y CERO commits, contra EJECUTOR.md regla 6
  (docs/loop/EJECUTOR.md:105). Es la TERCERA de la campana (81, 114,
  127) y NO cuenta en ninguna racha, por la letra del acta 82. Pero la
  advertencia de aquel acta sigue viva y la repito entera: DOS VUELTAS
  SEGUIDAS SIN ENTREGAR ya no serian un accidente, ninguna regla escrita
  las cubre, y eso seria PARADA por doctrina nueva. Commitea por tramo.

  UNA CAIDA DEL EJECUTOR, DE PROCEDIMIENTO (acta 127, 4.2): corriste un
  `run_phase1.py` que no dejo salida. Lo se porque el snapshot de
  entrada de tu corrida capturada dice 71 divergentes y en HEAD los
  gemelos estan a 0. Toda corrida de instrumento deja su salida.

  TUS NUEVE SALIDAS DE LA 127 ESTAN COMMITEADAS, RENOMBRADAS A
  `docs/loop/ABORTADA_V127_*.txt`, y digo por que: con su nombre viejo
  `SALIDA_V127_*_APERTURA.txt` habrian puesto VERDE a
  verificar_apertura_sellada.py --vuelta 127, o sea habrian dicho que la
  apertura de la 127 quedo sellada cuando la 127 no commiteo nada.
  Renombradas, la guarda sigue diciendo la verdad, y lo comprobe
  corriendola. NO las uses como medicion de esta vuelta: esta vuelta
  mide lo suyo con nombres V128.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 127 seccion 5), por
octava vez: no por hallazgo fuera de lo marcado, sino porque la 127 no
leyo nada y el tramo de la 120 sigue vivo y sin consumirse. Siguen los
ramales (i) NINGUNA MEDICION SE ATRIBUYE A UN ESTADO QUE NO ES EL SUYO,
(ii) EL EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO,
(iii) NINGUNA GUARDA SE ESTRECHA EN SILENCIO, (iv) TODA CIFRA SOBRE UN
ARTEFACTO CONTABLE SE LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO,
el (v) de la 123 NINGUNA VARA SE ESTRECHA EN EL ENCARGO, el (vi) de la
124 UN SUPERVIVIENTE SE RAZONA COMO SE RAZONA UNA CLASE, el (vii) de la
125 UNA FUSION NO ACABA CUANDO EL ALIAS QUEDA ESCRITO SINO CUANDO LA
ULTIMA ARISTA DEL ABSORBIDO ESTA RECONSTRUIDA, el (viii) de la 126 UNA
CIFRA DE PASIVO SE PARTE SIEMPRE EN DOS ANTES DE REMITIRLA, y el (ix)
de la 126 TODA CIFRA DE PASIVO O DE CENSO SE PUBLICA CON SU UNIDAD Y SU
ESTADO PEGADOS. Le anado UNO, y sale de mi propia caida:
  (x) UN ORDEN DE MEDICION SE PRUEBA CORRIENDOLO ENTERO SOBRE ARBOL
  LIMPIO ANTES DE MANDARLO. Medir un paso del orden y dar por bueno el
  orden es la misma especie de error que medir un tramo y dar por buena
  la tanda: la guarda que cae no es la que se probo, es la que venia
  detras.

LA ESCALADA de AUDITOR.md 1.2 se dispara con la racha de reporte en DOS.
Estamos en CERO de las que acumulan (la 127 no escribio reporte, y una
vuelta sin reporte no suma ni resta). NO TOCA, y la dejo dicha entera
para que nadie la de por gastada.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2
trabajo; la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros,
TAREA 3 trabajo, y lo mantengo porque las guardas son bloqueantes y van
delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V128_HEAD_APERTURA.txt. Al terminar la ultima
  operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V128_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 128 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La linea de
  identidad del reporte mantiene los TRES rotulos que estrenaste en la
  126 y que salieron bien: "HEAD sellado de apertura", "commit de
  nacimiento de las salidas de apertura" y "HEAD sellado de cierre".
  (1.b) EL ORDEN DE CAPTURA, CORREGIDO. ESTA ES LA LETRA NUEVA Y ES
  BLOQUEANTE (acta 127, adjudicacion 3.3).
  REGLA UNICA: `python scripts/run_phase1.py --reaplico-curaduria` NO SE
  CORRE NUNCA SUELTO COMO MEDICION. Recompila el grafo desde los nodos y
  por diseno NO reaplica la curaduria de etiquetas, asi que TODA corrida
  suya deja el dataset atrasado respecto de la web. Su Gate 0 no te avisa
  (compara el snapshot de ANTES del paso 6, y por eso sale verde), pero
  el motor si, y con razon.
  POR TANTO, POR CADA LADO (APERTURA, CIERRE, y el POST de cada
  operacion) SE HACE ESTO Y EN ESTE ORDEN, UNA SOLA VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado. Se escribe directamente
       en docs/loop/SALIDA_V128_GATE0_CMD1_<LADO>.txt. NO hay un fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida, y
       asi se dice en el reporte.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V128_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V128_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` tiene que estar VACIO (o, si la operacion de ese lado
       escribio de verdad, contener SOLO los ficheros que esa operacion
       escribio; `dataset/metadata/master_graph.json` con diff de puras
       lineas `etiqueta_arbol` NUNCA es una escritura legitima, es el
       borrado). Salida a
       docs/loop/SALIDA_V128_CICLO_NUMSTAT_<LADO>.txt con su EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V128_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V128_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V128_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V128_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V128_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V128_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V128_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio, sigue
  prohibido el fichero de cero bytes, y el marcador de codigo de salida de
  las demas salidas es la linea literal EXITCODE: <n>, que es la que
  verificar_citas_del_reporte.py sabe leer (convencion de la casa desde la
  correccion declarada de la 126). Y EL EXITCODE SE LEE DEL INSTRUMENTO,
  NUNCA DE UN `$?` PUESTO DETRAS DE UNA TUBERIA: redirige a fichero y lee
  el codigo, o usa PIPESTATUS. Esa es mi caida 4.4 y no quiero la tuya.
  (1.d) LA BATERIA POR OPERACION. Se escribe la operacion N, se corre su
  ciclo de 1.b entero, se miden sus cuatro salidas, Y SOLO ENTONCES
  empieza la N+1. Ficheros, con <OP> = OPS09REP3 (las tres reposiciones
  de 3.a) y OPS10 (el tramo de 3.b):
    docs/loop/SALIDA_V128_<OP>_GATE0_POST.txt   (= la corrida 1 del ciclo de esa operacion)
    docs/loop/SALIDA_V128_<OP>_CONTEO_POST.txt
    docs/loop/SALIDA_V128_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V128_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V128_<OP>_TSC_POST.txt
  mas las de etiquetas, sync y numstat del ciclo con el mismo prefijo.
  Antes de escribir el reporte corres cmp -s sobre CADA par de salidas
  homologas de la vuelta y vuelcas el resultado literal a
  docs/loop/SALIDA_V128_BATERIAS_CMP.txt con una linea por par que diga
  IDENTICOS o DISTINTOS. EL REPORTE DA CUENTA DE TODOS LOS PARES, NO DE
  UNA SELECCION: una linea por FAMILIA (GATE0, CONTEO, MOTOR, WEB, TSC,
  DESFASE, MARCADOR, ETIQUETAS, SYNC, NUMSTAT) diciendo cuantos IDENTICOS
  y cuantos DISTINTOS salieron y POR QUE lo son, y si dentro de una
  familia hay pares que van por motivos distintos, se nombran esos pares.
  UN IDENTICO SIN EXPLICAR ES UNA CAIDA, Y UN DISTINTO SIN EXPLICAR
  TAMBIEN. Y COMO ESTA VUELTA VUELVE A ESCRIBIR EN dataset/: si Gate 0 o
  el conteo salen IDENTICOS entre apertura y cierre despues de 3.a, eso NO
  es determinismo, es que la escritura no llego; se investiga y se declara
  antes de publicar nada. El CONTEO tiene que subir en +3 aristas por
  vista tras 3.a y NO moverse en 3.b.
  (1.e) LAS GUARDAS DE CITAS Y DE TITULOS NO SE TOCAN. Se corren
  verificar_citas_del_reporte.py, verificar_titulos_normalizados.py y sus
  autopruebas (vuelta122_tarea1e_mutacion_citas.py,
  vuelta123_tarea1e_mutacion_fila_tabla.py, y
  verificar_titulos_normalizados.py --autoprueba), y se pegan. NO se
  modifica ninguna de las dos. La excepcion declarada de
  sistema_responsabilidad_gerencial se queda EXACTAMENTE como esta.
  (1.f) LA GUARDA DE CIFRAS DEL PLAN, TAMPOCO SE TOCA. Se corre
  verificar_cifras_del_plan.py y sus dos casos positivos
  (vuelta123_tarea1f_caso_positivo.py y
  vuelta124_tarea1f_caso_positivo_ventana.py). Los tres verdes o rojos
  donde tocaba, pegados.
  (1.g) LAS DOS GUARDAS DE ARISTAS DE LA 126 SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py (que tiene que seguir en VERDE EXIT 0 sobre
  los cuatro pares, y cuyo --autoprueba tiene que seguir dando sus dos
  ROJOS) y verificar_aristas_vivas.py con su --autoprueba. Tras 3.a,
  verificar_aristas_vivas.py --antes <HEAD sellado de apertura> --despues
  WORK tiene que dar PERDIDAS 0 y NUEVAS 3, y las tres nuevas tienen que
  ser exactamente las tres aristas de la lista de 3.a, nombradas. Tras
  3.b, la misma corrida no debe anadir ninguna mas: un reencuadre de
  texto no mueve aristas, y si mueve alguna ES ROJO y paras.
  (1.h) LA GUARDA NUEVA DEL PASIVO. BLOQUEANTE, VA ANTES DE 3.a. Escribe
  scripts/loop/verificar_huerfanas_por_fusion.py, que generaliza y
  reemplaza a vuelta126_contar_aristas_huerfanas_totales.py (el viejo se
  queda en el repo como registro, no se borra), con este contrato:
    - Uso: --unidad par-resuelto|par-crudo (por defecto par-resuelto),
      --baseline <ref de git> (por defecto 50f03099, el encendido del
      bucle), --ref <ref o WORK> (por defecto WORK).
    - UNIDAD par-resuelto: por cada nodo DEPRECADO, se leen sus dos listas
      historicas, se resuelve cada entrada con el resolutor de --ref, y si
      resuelve a un nodo VIVO distinto del superviviente del propio muerto
      se comprueba si esa arista existe hoy entre los dos supervivientes,
      mirando las dos vistas. Los pares se deduplican por par resuelto.
      Es el metodo de la 126, sin cambios: la unidad canonica adjudicada.
    - UNIDAD par-crudo: lo mismo, pero deduplicando por el par HISTORICO
      (los dos ids muertos) y contando solo los casos en que el otro
      extremo tambien estaba deprecado. Es la unidad del 39.
    - LA PARTICION, QUE ES LA RAZON DE SER DE ESTA GUARDA: se mide el
      conjunto en --baseline, se PROYECTA por el resolutor de --ref (cada
      extremo se resuelve), y se imprime, en este orden y con estos
      rotulos: TOTAL, HEREDADAS (las del baseline proyectadas que siguen
      huerfanas hoy), REPARADAS DE REBOTE (las del baseline proyectadas
      que hoy ya no lo estan) y FABRICADAS POR LA CAMPANA (las de hoy que
      no vienen del baseline). Las FABRICADAS se listan una por linea y,
      por cada una, el id muerto de donde viene y el commit corto en que
      ese id quedo deprecado (git log -S sobre su fichero de dataset/nodos
      sirve).
    - ROJO EXIT 1 si FABRICADAS no es cero. VERDE EXIT 0 si lo es. Esa es
      la guarda: la campana no cierra con huecos propios.
    - CASO POSITIVO POR MUTACION, en memoria y sin tocar disco: sobre una
      copia del grafo de --ref se borra una arista que un superviviente
      heredo de su absorbido y tiene que aparecer en FABRICADAS o en
      HEREDADAS segun de donde venga, nombrada. Pegalo.
  MI CONTRASTE, REMEDIDO HOY 29 AGO SOBRE HEAD 4d4aaa8b CON
  docs/loop/_auditor_v127_proyeccion.py, Y NO PARA COPIAR: unidad
  par-resuelto, baseline 50f03099, ref WORK: TOTAL 32, HEREDADAS 29,
  REPARADAS DE REBOTE 1, FABRICADAS 3. Unidad par-crudo sobre 7150339f:
  39. MIDELO TU. SI TU MEDICION DISCREPA DE LA MIA, LA DECLARAS, NO LA
  RESUELVES COPIANDO. Y tras 3.a, la misma corrida tiene que dar
  FABRICADAS 0 y TOTAL 29.
  (1.i) ANTES DEL COMMIT DEL REPORTE, LAS CUATRO COMPROBACIONES, y las
  cuatro salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 128 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras tres
  VERDE EXIT 0.
  (1.j) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte,
  medida. La 126 lo cumplio en 80 exactos.
  (1.k) LOS DOS REGIMENES DE ESCRITURA SIGUEN COMO ESTAN Y NO SE TOCAN:
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

- TAREA 2, LOS REGISTROS Y CORRECCIONES DE LAS ACTAS 126 Y 127. REGIMEN A.
  Aditivos puros donde toquen texto viejo, medidos con git diff --numstat
  y con grep -c "^-[^-]" sobre el diff en cero. Son cuatro, y 2.a se
  escribe DESPUES de que 3.a este verde porque cita su resultado medido.
  (2.a) LA CORRECCION DECLARADA DE LA FICHA aristas-huerfanas-por-fusion,
  en docs/PENDIENTES.md, aditiva y sin borrar la primera entrada, con
  estas cuatro cosas: (1) que la DISCREPANCIA 32 contra 39 QUEDA CERRADA
  y no era doctrina, con las dos unidades escritas por su nombre (par
  vivo resuelto y par crudo historico) y el estado de cada cifra, y con
  la resta que lo cierra por los dos lados (33 a 32 en resueltos, 39 a 38
  en crudos, la misma arista); (2) que la UNIDAD CANONICA de la ficha es
  el PAR VIVO RESUELTO, adjudicado por el acta 126 seccion 4.1 citando
  banco 9.6; (3) LA RETRACTACION de la clausula "todas de fusiones
  ANTERIORES a esta campana de saneo", con la particion MEDIDA POR TI:
  cuantas heredadas, cuantas reparadas de rebote y cuantas fabricadas por
  la campana, con el commit de cada fabricada; y (4) que las fabricadas se
  reponen en esta vuelta por P.16 punto 1 y las heredadas NO se tocan.
  (2.b) EL REGISTRO LARGO EN docs/PENDIENTES.md, seccion nueva R.9 de la
  vuelta 126, como correcciones declaradas: (1) la caida de reporte del
  parrafo de baterias de la 126, con las dos lineas del cmp que la
  desmienten; (2) la caida de expediente de la clausula de procedencia,
  diciendo que la raiz es del auditor; (3) LA CAIDA DEL AUDITOR, DE
  CIFRA, escrita con todas sus letras: un pasivo publicado sin partir
  entre heredado y fabricado, y que por eso tres aristas propias se
  remitieron a pasivo historico durante una vuelta entera; (4) la caida
  del auditor, de procedimiento, por publicar el 39 sin su comando, con
  el remedio (los scripts del auditor viven en docs/loop/_auditor_v127_*.py);
  (5) la caida del auditor, de encargo, por el --ref c9ac2fb8 que no
  aislaba; y (6) los ramales (viii) y (ix) del tramo que se relee al
  doble, escritos enteros.
  (2.c) EL REGISTRO NUEVO EN docs/PENDIENTES.md, seccion R.10 de la
  vuelta 127, tambien como correcciones declaradas y tambien aditivo:
  (1) LA VUELTA 127 NO ENTREGO, con sus tres minutos, sus nueve salidas
  y sus cero commits, y que es la tercera de la campana (81, 114, 127) y
  no cuenta en racha; (2) LA CAIDA DEL AUDITOR, DE ENCARGO: el orden de
  captura imposible, con el experimento que lo prueba citado por su
  fichero (docs/loop/SALIDA_AUD_V127_EXPERIMENTO_ORDEN.txt) y con las
  dos guardas que contestan preguntas distintas nombradas por su linea
  (run_phase1.py:1176 y :941-947 contra engine/test_gate_alias.py:116 y
  :124); (3) la caida del auditor, de procedimiento, por leer un EXITCODE
  detras de una tuberia; (4) la caida del ejecutor, de procedimiento, por
  la corrida de run_phase1 sin capturar; (5) el renombrado de las nueve
  salidas a ABORTADA_V127_*, con el motivo (no envenenar de verde a
  verificar_apertura_sellada.py); y (6) el ramal (x) del tramo que se
  relee al doble, escrito entero.
  (2.d) LA FICHA NUEVA docs/PENDIENTES.md, permanente, con el nombre
  ventana-truncada-de-condiciones-activacion, aditiva y con su primera
  entrada: que condiciones_activacion se consume RECORTADA en tres sitios
  (engine/prototipo_motor.py:1532 y :1823 con [:2],
  engine/build_question_cache.py:97 con [:3]), verificalo tu y cita
  fichero y linea de lo que TU leas; que por eso una condicion ANTEPUESTA
  desplaza fuera de la ventana la ultima condicion vieja de todo nodo con
  dos o mas; CUANTOS DE LOS 31 DE OP-S-10 quedan afectados en cada ventana
  DESPUES de tu 3.b (MIDELO TU; el contraste sobre los diez de la 126, no
  para copiar, es 7 en [:2] y 3 en [:3]); que NO SE ARREGLA en esta
  campana porque la forma esta aprobada y la decision es del fundador en
  la auditoria de cierre; y que se revoca con una linea por nodo. NO
  TOQUES NI UN NODO POR ESTA FICHA.

- TAREA 3, EL TRABAJO.
  (3.a) LA REPOSICION DE LAS TRES ARISTAS FABRICADAS POR LA CAMPANA.
  REGIMEN B, LAS TRES GUARDAS COMPLETAS (1.k). BLOQUEANTE Y VA PRIMERA.
  Se reponen estas TRES y ninguna mas, cada una en las dos vistas
  (nodos_siguientes del origen y nodos_previos del destino):
    1. comprension_capacidades_limitaciones_ia -> division_trabajo_humano_ia
       (muertos jagged_frontier_ia, descomposicion_tareas_trabajo y
       framework_tareas_ia_humano; commit 0c946b7d, lote D del tramo
       unico de OP-U-02, vuelta 68)
    2. ecosistema_global_emprendimiento_gee -> uso_del_us_commercial_service
       (muertos consejos_distrito_exportacion_dec y
       recursos_apoyo_pymes_sba; commit a1d7269d, vuelta 57)
    3. incentivos_reconocimiento_sostenibilidad -> vision_alineacion_sostenibilidad
       (muertos accountability_incentivos y liderazgo_ceo_sostenibilidad;
       commit 0481113f, vuelta 57)
  ESAS TRES SON CONTRASTE MIO, MEDIDO HOY, Y SE VUELVEN A MEDIR CON TU
  1.h ANTES DE ESCRIBIR NADA: si tu guarda te da otras, mandan las tuyas
  y declaras la discrepancia.
  Guardas propias, ademas de las tres del REGIMEN B: los seis extremos
  siguen VIVOS, cero auto-aristas y cero duplicadas nuevas tras resolver,
  ningun otro campo de ningun nodo se toca (numstat que lo pruebe),
  verificar_aristas_vivas.py da PERDIDAS 0 y NUEVAS 3 con las tres
  nombradas, y verificar_huerfanas_por_fusion.py pasa de FABRICADAS 3 a
  FABRICADAS 0 con las dos salidas pegadas, antes y despues. Detras, su
  bateria de 1.d entera con etiqueta OPS09REP3.
  ANTES DE ESCRIBIR CADA UNA, LEE LOS DOS SUPERVIVIENTES y comprueba que
  la arista tiene sentido de contenido, como se comprobo la de la 126 (el
  paso 6 de dia_cero_defectos_2 nombraba literalmente al destino). SI EN
  ALGUNA DE LAS TRES EL CONTENIDO NO SOSTIENE LA ARISTA, O SI APARECE
  CUALQUIER COSA QUE NINGUNA REGLA ESCRITA CUBRA, PARAS EN ESA, LA TRAES
  CON SU CASO ESCRITO, Y SIGUES CON LAS OTRAS.
  (3.b) EL SEGUNDO Y ULTIMO TRAMO DE OP-S-10: LOS DIECISEIS QUE FALTAN.
  REGIMEN B, LAS TRES GUARDAS COMPLETAS. Misma forma literal que la 126,
  "Solo aplica si vendes o piensas vender franquicias en Estados Unidos",
  como PRIMERA condicion de activacion, con las viejas enteras y en su
  orden. ALCANCE: todos los nodos VIVOS de la nomina que hoy NO nombren el
  pais en condiciones_activacion y que no se tocaron en la 126. Mi
  contraste remedido hoy con docs/loop/_auditor_v127_ops10.py, no para
  copiar: 31 en la nomina, 28 vivos, 26 candidatos, 10 escritos en la 126
  y 16 pendientes. Los DOS contramodelos NO se tocan (verificacion 4).
  Los tres deprecados NO se tocan. Guardas propias del tramo, ademas de
  las tres: ningun otro campo cambia, las condiciones viejas quedan
  enteras y en su orden, cero guiones largos y cero guiones medios, y
  verificar_aristas_vivas.py sin aristas nuevas. Detras, su bateria de
  1.d entera con etiqueta OPS10.
  LA FORMA NO SE DISCUTE Y NO SE ADAPTA NODO A NODO: se queda literal por
  regla escrita (la verificacion 4 de la propia operacion congela a los
  dos contramodelos como modelo y la verificacion 1 pide el pais en
  condiciones_activacion para los 31). Lo que medi en contra y va a ficha
  y no cambia nada hoy: de los diez de la 126, solo cuatro cablean norma
  de un pais, y en los otros seis el contenido es metodo que sirve en
  cualquier pais, contra la linea del banco que pone el puntero
  jurisdiccional en "los nodos que tocan tratados, aranceles, garantias o
  normativa" (docs/BANCO_DE_TEXTOS.md:112). QUEDA MARCADO para la
  auditoria de cierre, que es de Alexis, y es revocable con una linea por
  nodo.
  EL CASO obtencion_marca_registrada ES EL DELICADO y esta nombrado en la
  verificacion 2 de la operacion ("ningun nodo condiciona con un adjetivo
  federal en vez de con un pais"): antepone la condicion nueva como en
  todos los demas y NO reescribas su condicion vieja. Si al leerlo
  concluyes que la verificacion 2 EXIGE tocar la condicion vieja, ESO ES
  UNA PARADA DE NODO: lo dejas con la condicion nueva antepuesta, lo traes
  escrito con su caso, y sigues con los demas.
  (3.c) LA MEDICION DE LA VERIFICACION 3 DE OP-S-10, que nadie ha medido:
  "los items numerados del FDD (Item 8, 19, 23) quedan dentro de la
  condicion de pais, no fuera". Mide con codigo propio, sobre el grafo de
  hoy, que nodos de la nomina de 31 nombran Item 8, Item 19 o Item 23 en
  cualquier campo, y si cada uno de esos nodos queda cubierto por una
  condicion de pais tras tu 3.b. Salida pegada, y el resultado escrito
  como correccion declarada aditiva en la nota de OP-S-10 (REGIMEN A,
  numstat y borrados en cero, word-diff pegado). NO CIERRES la operacion
  tu: mide, publica y dilo.
  (3.d) EL ESTADO DE OP-S-10 Y DE LA FASE 05. Con 3.b y 3.c hechos, la
  operacion queda con sus cinco verificacion medidas. NO LE CAMBIES EL
  ESTADO Y NO DECLARES LA FASE CERRADA: mide, publica lo que te salga
  verificacion por verificacion, y MARCALO COMO DISCUTIBLE. El cierre de
  OP-S-10 lo adjudica el auditor, igual que adjudico el de OP-S-09.
  OP-S-11 y OP-S-12 no se abren.
  Y AVISO POR CUARTA VUELTA, PORQUE YA ESTA ENCIMA: cuando la fase 05
  quede cerrada y verificada se dispara la condicion de parada CIERRE DE
  LA FASE 05 de AUDITOR.md seccion 4, y esa parada es del fundador.
  MARCA COMO DISCUTIBLE, para que yo lo adjudique: si con OP-S-10 medida
  entera la fase 05 queda a dos operaciones (OP-S-11 y OP-S-12) o si
  alguna de las dos tiene texto que no alcance para ejecutarse sin
  decidir, cosa que seria PARADA y no improvisacion.

Y UNA COSA MAS, QUE ES DE LA CASA Y NO DE ESTA VUELTA: COMMITEA POR
TRAMO. En cuanto la TAREA 1.a este puesta, commit. En cuanto el ciclo de
apertura cierre en CERO, commit. Detras de 3.a verde, commit. Detras de
3.b, commit. La 127 perdio nueve salidas buenas por no hacerlo y es la
tercera vuelta de la campana que se pierde asi.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
