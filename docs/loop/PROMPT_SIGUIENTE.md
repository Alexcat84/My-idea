Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 121. El acta de la 120 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final): la 120 repuso las dos guardas que
la 119 habia perdido (sello de apertura VERDE, tallador IDENTICO, las dos
recorridas por el auditor), cerro OP-S-02 con nomina remapeada, y TODAS
sus cifras salieron ciertas al digito. Los dos instrumentos de escritura
llegaron con simulacion y mutacion negativa, y el auditor les corrio
ademas su ROJO real en segunda pasada: los dos muerden, EXIT 1, sin
escribir nada. No hay parada: ninguna de las diez condiciones se dispara.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 120 seccion 5, el
credito bajo por la caida 4.1, que aparecio FUERA de los discutibles
marcados): TODA CALIFICACION TECNICA QUE EL REPORTE COMPRIMA RESPECTO DE
SU REGISTRO LARGO. "limpio" contra "sucio", "verde" contra "rojo",
"cumplida" contra "cumplida con remision", "cerrada" contra "acotada".
EL REPORTE NO PUEDE DECIR MENOS PRECISO QUE EL REGISTRO QUE CITA: antes
de publicar cualquiera de esas palabras se lee la linea del registro que
la respalda y, si el registro distingue dos especies, el reporte las
distingue tambien o no las nombra. La caida concreta: la 120 escribio
"ambas EXIT 1 limpio" de dos guardas, y una de las dos cae con un
ValueError SIN CAPTURAR, que es EXIT 1 pero NO es un rojo limpio; el
registro de docs/PENDIENTES.md si lo distinguia bien, el reporte lo
aplano.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA
  ANTES DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA
  OPERACION: git rev-parse HEAD, hash completo de 40 caracteres, UNA
  linea, a docs/loop/SALIDA_V121_HEAD_APERTURA.txt. Al terminar la ultima
  operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V121_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 121 tiene
  que dar VERDE EXIT 0, y su salida se cita en el reporte. La 120 lo hizo
  bien; se repite igual.
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V121_GATE0_CMD1_<LADO>.txt   (scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V121_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V121_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V121_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V121_TSC_<LADO>.txt          (cd web y npx tsc --noEmit)
    docs/loop/SALIDA_V121_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V121_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  Y ANTES DEL COMMIT DEL REPORTE, la comprobacion que EJECUTOR.md pide
  literal (regla del 20 ago 2026):
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 121 --comparar docs/loop/REPORTE.md
  tiene que dar CABECERA IDENTICA AL TALLADOR, y esa salida se pega en el
  reporte. Si cae en ROJO, la causa se arregla o se declara como
  discutible con la salida entera pegada; no se publica una cabecera a
  mano en silencio.
  (1.c) EL HUECO QUE LA 120 DEJO ABIERTO Y QUE ESTA VUELTA SI MUERDE (acta
  120 seccion 4.2): LA BATERIA POR OPERACION LLEVA SU PROPIO tsc, CON
  NOMBRE. La 120 dejo GATE0_POST, MOTOR_POST y WEB_POST de su unica
  operacion, pero NO un TSC_POST; el tsc del cierre tapo el hueco porque
  la vuelta tuvo una sola operacion. ESTA VUELTA VAN DOS, asi que la
  primera se quedaria sin tsc. Por cada operacion N que se cierre, las
  CUATRO salidas con este nombre exacto:
    docs/loop/SALIDA_V121_<OP>_GATE0_POST.txt
    docs/loop/SALIDA_V121_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V121_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V121_<OP>_TSC_POST.txt
  con <OP> = OPS03, OPS04, etc. Mas las de etiquetas y sync del ciclo de
  tres, con el mismo prefijo.
  (1.d) EL CICLO DE TRES NO CAMBIA y no se corre run_phase1.py solo,
  nunca (acta 88 seccion 5.6): run_phase1.py --reaplico-curaduria, luego
  etiquetas_de_cara.py --aplicar, luego sync_assets_web.py, en ese orden,
  y git diff --numstat sobre dataset/, web/ y engine/ en cero detras.

- TAREA 2, LOS REGISTROS Y ADJUDICACIONES DEL ACTA 120. Aditivos puros
  donde toque texto viejo, medidos con git diff --numstat y con
  grep -c "^-[^-]" sobre el diff en cero. Son dos, y el orden da igual.
  (2.a) LA ADJUDICACION DEL "PENDIENTE DE DOCTRINA" DE OP-S-02, QUE YA
  NO ESTA PENDIENTE. El auditor lo adjudico en la vuelta 120 (acta 120
  seccion 3.1) y NO hizo falta doctrina nueva: se resuelve con DOS reglas
  escritas, y las dos se citan al escribir.
    - P.13 del BANCO_DEL_PLAN, clase VIVE DENTRO ("ya dicha"). El auditor
      leyo la fusion que produjo el superviviente: docs/plan/03_FUSIONES.md,
      ACTO 16 DEL LOTE A (seguro_exportacion absorbe
      seguro_de_carga_transporte), con 6 piezas repartidas en 2 enteras,
      3 ya dichas y 1 INCISO, y una UNICA perdida nombrada, DE
      CONDICIONES, no de pasos. O sea que el paso 1 del muerto se conto
      como "ya dicha": LA UNIDAD DEL REPARTO ES EL PASO, NO LA PALABRA, y
      el parentesis "(Incoterms)" cayo por debajo de esa granularidad. NO
      HAY PERDIDA SIN DECLARAR en la fusion 16, y restituir la palabra NO
      cabe en OP-S-02, cuyo acto literal es anadir version a una cita que
      YA existe.
    - Punto 2 de la decision del fundador del 28 ago 2026
      (docs/loop/paradas/2026-08-28-titulo-nafta-ops01-DECISION.md): el
      contenido que la operacion no alcanza SE ANOTA EN LA FICHA Y NO SE
      EJECUTA, y el punto de verificacion se acota por correccion
      declarada. Es lo que ya se hizo con OP-S-01.
  DOS ESCRITURAS, Y NINGUNA TOCA EL NODO:
    (i) SEXTA ENTRADA DE LA FICHA vigencia-del-marco-internacional en
    docs/PENDIENTES.md: seguro_exportacion perdio la palabra "Incoterms"
    de su paso 1 en la fusion del acto 16 (vuelta 57, commit 0481113f),
    su texto vivo dice hoy "Determinar segun terminos de venta quien es
    responsable del seguro de carga" donde el muerto decia "segun los
    terminos de venta (Incoterms)", y por eso queda FUERA de OP-S-02.
    Anotado como trabajo post campaña, NO ejecutado. EL NODO NO SE TOCA.
    Mide y pega el texto vivo de hoy antes de escribir la entrada: no lo
    copies de este encargo.
    (ii) LA NOTA DE OP-S-02 EN docs/plan/OPERACIONES.jsonl: el
    "PENDIENTE DE DOCTRINA, traido a la mesa" QUEDA ADJUDICADO. Se
    corrige POR REMISION, sin borrar una sola letra del texto viejo:
    correccion declarada al final que diga que el acta 120 seccion 3.1 lo
    adjudico citando P.13 y el punto 2 del 28 ago, que no hizo falta
    doctrina nueva, y que la anotacion vive en la ficha. La fila de
    OP-S-02 sigue HECHA y ninguna otra fila se toca.
  (2.b) LA CORRECCION DE "AMBAS EXIT 1 LIMPIO", que es la caida 4.1 del
  acta 120 y es del EJECUTOR. Va donde vive el registro largo, en
  docs/PENDIENTES.md, seccion R.3 de la vuelta 120, como correccion
  declarada al lado del texto viejo: el reporte de la 120 comprimio en
  "limpio" dos cierres de especie distinta, y el registro largo ya los
  distinguia bien. Texto viejo intacto. Y de ahi sale la regla del tramo
  doblado de arriba, que se escribe tambien.

- TAREA 3, EL TRABAJO: DOS OPERACIONES, Y EL SUELO ES DOS.
  MODO AUSTERO 1 pide dos cuando quepan, y el auditor MIDIO HOY que la
  primera cabe. LA REGLA DEL TRAMO DOBLADO SIGUE VIGENTE Y ES
  BLOQUEANTE: todo instrumento que escriba en dataset/ o en docs/plan/
  llega con (i) SIMULACION PREVIA sobre copia en memoria, con su salida
  pegada, (ii) SU MUTACION NEGATIVA corrida y pegada, y (iii) SU ROJO
  REAL EN SEGUNDA PASADA, que es lo que el auditor corrio por su cuenta
  en la 120 y que desde esta vuelta corre el ejecutor: tras escribir, el
  mismo instrumento se vuelve a correr y tiene que caer en ROJO EXIT 1
  sin escribir nada, con git status --porcelain vacio detras, y esa
  salida se pega. Un instrumento de escritura sin las tres NO SE CORRE.
  (3.a) OP-S-03, export.gov A trade.gov. LA MAS BARATA DE LAS TRES
  AVERIAS DE VIGENCIA, y su texto no deja nada que decidir
  (docs/plan/05_SANEO.md, seccion OP-S-03). MEDIDO POR EL AUDITOR HOY
  CONTRA EL GRAFO, y lo re-mides tu antes de escribir: LA NOMINA ESTA
  INTACTA, los TRES nodos vivos y ninguno deprecado
  (calculo_de_aranceles_importacion,
  evaluacion_preparacion_empresa_exportar, reglas_de_origen_fta_2), con
  CUATRO menciones de export.gov en total porque
  calculo_de_aranceles_importacion lo nombra DOS VECES. Son 4, no 3, y el
  propio plan avisa de que es facil dejarse una. Su verificacion: ningun
  nodo vivo cablea export.gov, las CUATRO menciones cambiadas, Gate 0
  verde. Al cerrarla, OPERACIONES.jsonl a HECHA con el mismo patron de
  guarda de la 120.
  (3.b) OP-S-04, LAS SEIS HERRAMIENTAS MUERTAS. Su remedio esta
  ADJUDICADO en docs/plan/05_SANEO.md (REMEDIO ESPEJO): en los CINCO
  nodos la herramienta es EJEMPLO y no OBJETO, asi que los cinco se
  GENERALIZAN y NINGUNO abre ficha de vigencia. La lista de vivas que la
  casa ya tiene verificada (AdRoll, MixRank, Adbeat, BuySellAds,
  InnoCentive) es de donde salen los ejemplos vivos: NO INVENTES una
  herramienta nueva ni verifiques por tu cuenta si algo sigue vivo. Su
  verificacion pide ademas que toda linea generalizada conserve AL MENOS
  UN ejemplo vivo verificado. RE-MIDE LA NOMINA CONTRA EL GRAFO DE HOY
  ANTES DE ESCRIBIR, como se hizo con OP-S-02: son cinco nodos del 11 ago
  2026 y el grafo se ha movido debajo otras veces. Si al medir resultara
  que algun nodo esta deprecado, se remapea al superviviente y se declara
  la correccion, igual que la 120.
  (3.c) Y SI CIERRAN LAS DOS CON SUS GUARDAS COMPLETAS, OP-S-05 CIERRA
  DETRAS POR REMISION: no tiene nodos, su adjudicacion ya esta escrita
  ("solo se verifican los nombres que son OBJETO del nodo o URL cableada;
  los que son ejemplo se genericalizan y no se verifican") y OP-S-04 es
  quien la consuma. Se cierra como registro, con su guarda, citando la
  linea del plan que lo dice.
  EL SUELO ES DOS OPERACIONES. Si solo entra una, el reporte publica LA
  CUENTA DE GUARDAS que consumio la vuelta, guarda por guarda con su
  fichero, y no la palabra "limite de alcance" a secas: el auditor
  midio que la primera cabe y quiere ver contra que se gasto el tiempo.
  OP-S-12 va al final de la fase y no se abre esta vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
