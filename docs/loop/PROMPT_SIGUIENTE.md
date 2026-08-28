Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 120. El acta de la 119 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final): la vuelta 119 entrego sus tres
tareas, todas sus cifras salieron ciertas al digito recomputadas por el
auditor, y OP-S-01 queda RATIFICADA como CUMPLIDA CON REMISION. Lo que
cobro fueron guardas, no cifras, y de ahi salen las tres primeras tareas.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 119 seccion 5, el
credito de la tanda bajo por la caida 4.4, que aparecio FUERA de los
discutibles marcados): (i) TODO INSTRUMENTO QUE ESCRIBA en dataset/ o en
docs/plan/, y (ii) TODA AFIRMACION UNIVERSAL sobre el comportamiento de
una herramienta ("siempre", "nunca", "no puede correr"). Los dos se
tratan abajo con letra explicita.

- TAREA 1, LAS DOS GUARDAS MECANICAS QUE LA 119 PERDIO. BLOQUEANTE, Y LA
  PRIMERA MITAD VA ANTES DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA
  OPERACION: git rev-parse HEAD y su hash completo de 40 caracteres,
  UNA linea, a docs/loop/SALIDA_V120_HEAD_APERTURA.txt. Al terminar la
  ultima operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V120_HEAD_CIERRE.txt. Los dos los pide
  scripts/loop/tallar_cabecera_reporte.py por su nombre, y su ausencia
  fue lo que puso en ROJO la vuelta pasada. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 120 tiene
  que dar VERDE EXIT 0, y su salida se cita en el reporte.
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS, para que el tallador pueda
  correr. La 119 escribio su Gate 0 en SALIDA_V119_TAREA3_GATE0.txt y por
  eso el tallador cayo con 37 celdas ilegibles: el CONTENIDO era correcto,
  el NOMBRE no. Esta vuelta las salidas de apertura y de cierre se
  escriben con estos nombres exactos, con <LADO> = APERTURA o CIERRE:
    docs/loop/SALIDA_V120_GATE0_CMD1_<LADO>.txt   (salida de
      scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V120_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V120_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V120_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V120_TSC_<LADO>.txt          (cd web y npx tsc --noEmit)
    docs/loop/SALIDA_V120_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V120_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  El marcador de EXIT=<n> al final de cada fichero se mantiene como
  siempre: el tallador ya sabe descontarlo. Y ANTES DEL COMMIT DEL
  REPORTE, la comprobacion que EJECUTOR.md (regla del 20 ago 2026) pide
  literal:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 120 --comparar docs/loop/REPORTE.md
  tiene que dar CABECERA IDENTICA AL TALLADOR, y esa salida se pega en el
  reporte. Si el tallador cae en ROJO, la causa se arregla o se declara
  como discutible con la salida entera pegada; no se publica una cabecera
  a mano en silencio.
  (1.c) EL CICLO DE TRES NO CAMBIA y no se corre run_phase1.py solo,
  nunca (acta 88 seccion 5.6): run_phase1.py --reaplico-curaduria, luego
  etiquetas_de_cara.py --aplicar, luego sync_assets_web.py, en ese orden,
  y git diff --numstat sobre dataset/, web/ y engine/ en cero detras.

- TAREA 2, LOS REGISTROS DEL ACTA 119 en docs/PENDIENTES.md, aditivos
  puros, medidos con git diff --numstat y con grep -c "^-[^-]" sobre el
  diff en cero. Son tres, y el orden da igual.
  (2.a) LA CORRECCION DEL "SIEMPRE" DE LA M ESPURIA, que es una caida del
  AUDITOR y asi se escribe. El acta 118 seccion 4.2 dijo que
  scripts/loop/vuelta89_tarea4_guarda_op_c05.py --caso-rojo no puede
  correr "porque git status --porcelain ve SIEMPRE la M espuria de fin de
  linea", y el reporte de la 119 y el docstring del fichero nuevo
  heredaron ese universal. ES FALSO COMO UNIVERSAL, medido por el auditor
  en la vuelta 119: la guarda vieja corrida tal cual, sin tocarla, sale
  VERDE EXIT 0, con las mismas cifras que la nueva (935 a 936 entradas
  que sobran, 711 nodos), y git status --porcelain -- dataset/ sale vacio
  en tres mediciones, una de ellas tras reescribir el fichero byte a byte
  a proposito para provocarla. El disparador de la M NO queda
  identificado y NO se inventa: lo que se registra es que NO ES
  PERMANENTE, y que el acta 88 seccion 5.6 ya exigia "git status
  --porcelain -- dataset/ web/lib/assets/ en cero detras" del ciclo de
  tres, que seria imposible de exigir si la M fuera perpetua. LO QUE NO
  SE TOCA ES EL REMEDIO: medir CONTENIDO (git diff --numstat) es
  estrictamente mejor que medir ESTADO aunque hoy el estado este limpio,
  la guarda nueva es correcta, y sus DOS ramas quedaron probadas por el
  auditor (--despues con un ANTES menor devuelve EXIT 1 con "ROJO: LA
  CUENTA CRECIO"; con el ANTES real devuelve EXIT 0 con "+0"). Se corrige
  el DIAGNOSTICO, no el arreglo. Texto viejo intacto, correccion
  declarada al lado, y el fichero vuelta119_tarea1_guarda_op_c05_contenido.py
  NO se reescribe: se le anade la correccion en el registro, no en el
  codigo.
  (2.b) LA QUINTA ENTRADA DE LA FICHA vigencia-del-marco-internacional.
  El auditor midio hoy sobre los 3.188 vivos que CINCO nodos nombran
  NAFTA en algun campo, y el quinto es EL SUPERVIVIENTE MISMO,
  certificado_de_origen_tratados_libre_comercio, en resumen_teorico ("el
  NAFTA Certificate of Origin", y "segun el tratado aplicable (NAFTA,
  CAFTA-DR, ...)") y en pasos_accionables ("el Certificado de Origen
  correspondiente (ej. NAFTA)"). La entrada que la 119 escribio nombra
  CUATRO ids y excluye al superviviente por su letra: o sea que hoy el
  TITULO dice T-MEC/USMCA y EL CUERPO DEBAJO SIGUE DICIENDO NAFTA, y ese
  cuerpo no esta anotado en ninguna parte. ADJUDICACION DEL AUDITOR POR
  EXTENSION NATURAL del punto 2 de la decision del fundador del 28 ago
  2026 (anotar, no ejecutar): el cuerpo del superviviente entra como
  QUINTA entrada de la ficha, anotado y NO ejecutado, con la nota
  expresa de que ids_alias y merged_originals quedan FUERA del barrido
  por ser PROCEDENCIA y no contenido. EL NODO NO SE TOCA en esta vuelta.
  (2.c) EL CASO POSITIVO QUE FALTABA, corrido por el auditor y
  registrado: vuelta119_tarea3_titulo_ops01.py y
  vuelta119_tarea3_2_3_operaciones_ops01.py escribieron sin simulacion
  previa y sin caso positivo. Corridos en segunda pasada, el del titulo
  cae en ROJO limpio EXIT 1 ("no se pisa un estado distinto al medido por
  la parada") y el de las operaciones cae en EXIT 1 con un ValueError sin
  capturar sobre verif.index(PUNTO4_VIEJO); ninguno de los dos escribio
  nada. Las guardas muerden; lo que faltaba era la prueba. Se registra, y
  con ella la regla que rige desde esta vuelta y que esta en la TAREA 3.

- TAREA 3, EL TRABAJO: OP-S-02 EN ADELANTE, EN MODO CONTINUO Y AUSTERO.
  LA REGLA DEL TRAMO DOBLADO, QUE ES BLOQUEANTE Y VALE PARA CADA
  OPERACION DE ESTA VUELTA: todo instrumento que escriba en dataset/ o en
  docs/plan/ llega con (i) SIMULACION PREVIA sobre copia en memoria, con
  su salida pegada, y (ii) SU CASO POSITIVO CORRIDO Y PEGADO, probado por
  MUTACION sobre una variable que el codigo compute, no sobre un literal
  (EJECUTOR regla 1). Un instrumento de escritura sin caso positivo
  corrido NO SE CORRE. Y ninguna afirmacion universal sobre una
  herramienta ("siempre", "nunca", "no puede") se escribe sin la medicion
  de ESTA vuelta al lado.
  (3.a) OP-S-02, INCOTERMS. Su verificacion pide que "los tres nodos
  citan Incoterms con su version". ANTES DE ESCRIBIR NADA, RE-MIDE LA
  NOMINA CONTRA EL GRAFO DE HOY y pega la medicion, porque el auditor
  encontro que la nomina de la operacion es del 11 ago 2026 y el grafo se
  movio debajo: de los tres nodos que nombra
  (incoterms_reglas_comerciales_internacionales,
  terminos_de_venta_incoterms, seguro_de_carga_transporte), DOS ESTAN
  HOY DEPRECADOS (terminos_de_venta_incoterms y
  seguro_de_carga_transporte). Mide cuales siguen vivos, a que
  superviviente resuelve cada deprecado, y si la cita de Incoterms viaja
  o no al superviviente. Si la operacion queda consumida o parcialmente
  consumida por una fase anterior, se clasifica como tal CON SU COMMIT
  citado (git log -S sobre el fichero del nodo), igual que se hizo con
  OP-S-01 y su vuelta 57.
  LA VERSION NO SE INVENTA: la edicion vigente que la casa ya tiene
  escrita es Incoterms 2020, y vive en docs/PENDIENTES.md, en el texto
  fundacional de la ficha vigencia-del-marco-internacional ("Incoterms
  2020 no es un dato local: un catalogo que lo cite desactualizado miente
  con precision"). Se cita esa linea al escribir. Si al medir resultara
  que ninguna linea del repo fija la edicion, PARAS Y LO TRAES: esa es
  exactamente la figura de la parada de OP-S-01 y no se improvisa dos
  veces.
  (3.b) Y DESPUES OP-S-03 EN ADELANTE (OP-S-03 export.gov, OP-S-04 y
  OP-S-05 herramientas, OP-S-08 campo sucio, OP-S-09 renombres con
  alias), en el orden del fichero, con las guardas completas por
  operacion: simulacion previa, Gate 0 y las tres suites en verde tras
  cada operacion, caso positivo, y cero duplicadas o auto-aristas tras
  resolver. OP-S-12 va al final y no se abre esta vuelta. Cuantas entren
  con sus guardas completas, entran; el limite de alcance se declara con
  su motivo, como hizo la 119, pero YA NO VALE como unica entrega: esta
  vuelta el trabajo de la fase 05 es el trabajo, no el registro.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
