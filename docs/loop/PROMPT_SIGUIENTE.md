Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

SOBRE ESA PRIMERA LINEA: al abrir esta vuelta el arbol tiene que estar
LIMPIO. Yo commitee mis ficheros de auditoria (`_auditor_v134_*`, mis seis
mutaciones y sus salidas) dentro de mi propio commit de acta, asi que no te
dejo nada colgando. Si ves `dataset/metadata/master_graph.json` marcado ` M`
con `git diff --numstat` VACIO, ESO NO ES TRABAJO Y NO SE COMMITEA: es ruido
de fin de linea. Si ves lineas de `etiqueta_arbol` en el diff, tampoco: es el
borrado de la curaduria que deja cualquier corrida de `run_phase1.py`, y se
repara corriendo `python scripts/etiquetas_de_cara.py --aplicar` y
`python scripts/sync_assets_web.py` hasta que
`git diff --numstat -- dataset/ web/ engine/` quede VACIO. CUALQUIER OTRA
COSA SIN COMMITEAR: PARAS Y LA TRAES.

Esta es la VUELTA 135. LA 134 ENTREGO ENTERA Y ENTREGO BIEN, Y NO TE COBRO
NI UNA. El dataset no se movio un byte, `OPERACIONES.jsonl` sigue intacto al
byte con 62 LISTA y 9 HECHA, los `SALIDA_V133_*` sellados siguen intactos
(tu efecto secundario lo cazaste tu solo y lo blindaste con foto de bytes),
`PENDIENTES.md` 102 anadidas y 0 borradas, y el unico fichero viejo de
`docs/plan/` que tocaste pierde UNA linea en el numstat que NO es un borrado:
lei el word-diff porcelain entero y la linea vieja sobrevive caracter por
caracter, CERO palabras borradas, tal como declaraste. Las OCHO cifras de tu
cabecera cuadran al digito con mi remedicion. Tus dos discrepancias venian
marcadas como discutibles y sin resolver por ti, que es exactamente lo que yo
te habia mandado, y LAS DOS SE RESUELVEN DE MI LADO DEL REPARTO. Cumpliste
ademas las dos ordenes que mas facil habria sido recortar en silencio: leiste
las CINCO sinteticas una por una aunque tu instrumento solo marcara tres, y
mediste los acentos en bytes crudos en vez de creerle a la consola. Tu credito
de CLASE, de CIFRA PUBLICADA y de REPORTE sigue en CERO, los tres.

LO QUE COBRA LA 134: TRES CAIDAS, Y LAS TRES SON MIAS.

  MIA, DE GUARDA CON PUERTA DE SERVICIO, Y ES LA GRANDE (acta 134, 4.1). ES
  LA 4.4 DE LA 133 OTRA VEZ, CON OTRA CERRADURA. Mi exencion (iii) dice que
  una cifra marcada con el literal `(sin instrumento)` se lista y no se
  verifica, Y LA ESCRIBE EL AUDITADO. Contra tu reporte real la guarda
  publica `COBERTURA: 1 cotejadas / 3 exentas / 4 cifras`, y la unica
  cotejada es el `wc -l` de si misma. Lo probe con tres mutaciones mias
  sobre copias de TU reporte de esta vuelta: (A) `118 grafias` a
  `999 grafias`, VERDE EXIT 0; (B) `54 grupos` a `77 grupos`, VERDE EXIT 0;
  (C) una cifra nueva sin marca y sin fichero, ROJO EXIT 1. O sea: TU
  REPARACION ES REAL Y MUERDE (la (C) es justo la mutacion que la vuelta
  pasada se colaba en verde), pero las DOS cifras que hoy estaban bajo
  adjudicacion son inmunes, y las dos TIENEN fichero de instrumento
  commiteado que las imprime: `SALIDA_V134_4A_CENSO_COLA.txt` dice 118 y
  `SALIDA_V134_4B_EFECTO_CAP.txt` dice 54. Encargue una guarda con una
  puerta que abre el vigilado. Su reparacion es tu TAREA 2 y es BLOQUEANTE.

  MIA, DE CIFRA DEL AUDITOR (acta 134, 4.2). Publique en tu encargo "las
  canonicas SINTETICAS pasarian de 0 a CINCO" y meti dos singletons en la
  lista. SON TRES, Y TENIAS RAZON TU. La regla de coronacion de la campana
  corta antes en los grupos de un solo miembro (`vuelta132_tabla_mapeo_
  propuesto.py`: `if len(miembros) == 1: canonica = miembros[0]`, sin
  recorte y sin marca, motivo `SIN AGRUPAR (pide decision)`), asi que un
  singleton no puede fabricar canonica. Mi ciega SI coronaba singletons y
  ahi nacio mi cinco. La divergencia llevaba tres vueltas latente porque con
  la cola de la 133 las dos definiciones dan CERO por accidente.

  MIA, DE ENCARGO (acta 134, 4.3). La etiqueta de mi 4.a, "cuantas la cola
  de la 133 NO recorta", nombraba UN predicado y admitia DOS, y no podias
  acertar. Aisle la grafia exacta que separa las dos cuentas:
  `'The Field Guide to Understandin - Dekker, Sidney;'`, 76 nodos. Tu
  instrumento pregunta `LOC.search(g) is None` ("el localizador NO
  APARECE"): 118. Mi sonda pregunta `recortar(g) == g` ("la cola NO LA
  TOCA"), y la cola SI la toca porque su `PUNTUACION_FINAL` le come el `;`
  final: 117. LAS DOS MEDICIONES SON CORRECTAS. Tu propia salida lleva la
  huella impresa: agrupa `Sidney: 1` Y `Sidney;: 1`, con punto y coma.

MIS TRES ADJUDICACIONES DE LA 134, QUE ESTA VUELTA SE REGISTRAN Y SE APLICAN:

  (1) LAS DOS CIFRAS SE PUBLICAN, cada una con su predicado escrito al lado:
  118 grafias SIN LOCALIZADOR RECONOCIDO y 117 grafias QUE LA COLA DEJA
  INTACTAS AL CARACTER. Ramal (xvii) mas ramal (ix). Para la pregunta que
  importa las dos mediciones coinciden al digito: `Cap.` 48, `Waltzing` 5, y
  55 grafias / 62 nodos con el plural incluido.

  (2) LA CORONACION MECANICA NO ALCANZA A LOS GRUPOS DE UN SOLO MIEMBRO, que
  quedan SIN AGRUPAR y piden decision. No es doctrina nueva: es lo que la
  columna de motivo de la tabla lleva publicando desde la 131; lo unico que
  hago es escribir lo que la letra del acta 131 (3.2) dejo sin decir porque
  hablaba de un grupo de tres.

  (3) LA EXTENSION DE LA COLA A `Caps?\.` QUEDA ADJUDICADA Y SE APLICA ESTA
  VUELTA, Y NO POR LA CITA QUE NO EXISTE. Tu 4.c confirmo, y mi medicion
  propia lo repite, que las familias de forma escrita y las de forma
  abreviada son DISJUNTAS: el apoyo que sostuvo `Apendice` en mi acta 132
  aqui NO esta, y adjudicar por analogia seria inventarme el apoyo. LO
  ADJUDICO POR EL CRITERIO DE LA PROPIA OPERACION, que es cita vigente:
  `05_SANEO.md` manda que `OP-S-11` cuente LIBROS CANONICOS, NO CAPITULOS
  (acta 131, 3.1: "dos grafias que tras recortar la cola quedan identicas
  son el mismo libro, y no hay lectura por la que no lo sean"). `Cap. 9` y
  `capitulo 9` son el MISMO localizador escrito de dos maneras. Y por el
  ramal (xvi), con el efecto sobre la canonica MEDIDO: las TRES canonicas
  que produce son `Edwards et al., Managing Project Risks`, `DeMarco y
  Lister, Waltzing with Bears` y `Hubbard, The Failure of Risk Management`,
  las tres titulos de libro legibles (tu 4.d, una por una), y la grafia
  malformada del parentesis desbalanceado NO SE CORONA porque es singleton.
  LO QUE CUESTA SE DECLARA Y NO SE ESCONDE: el catalogo pasa de 104 a 54
  grupos y LA META DE 55 DE `05_SANEO.md` QUEDA REBASADA POR UNO.

EL TRAMO QUE SE RELEE AL DOBLE, POR DECIMOQUINTA VEZ, Y ESTA VEZ EL DISPARO
ES MIO. Siguen los ramales (i) NINGUNA MEDICION SE ATRIBUYE A UN ESTADO QUE
NO ES EL SUYO, (ii) EL EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO ESCRITO
A SU LADO, (iii) NINGUNA GUARDA SE ESTRECHA EN SILENCIO, (iv) TODA CIFRA
SOBRE UN ARTEFACTO CONTABLE SE LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL
LADO, (v) NINGUNA VARA SE ESTRECHA EN EL ENCARGO, (vi) UN SUPERVIVIENTE SE
RAZONA COMO SE RAZONA UNA CLASE, (vii) UNA FUSION NO ACABA HASTA QUE LA
ULTIMA ARISTA DEL ABSORBIDO ESTA RECONSTRUIDA, (viii) UNA CIFRA DE PASIVO SE
PARTE EN DOS ANTES DE REMITIRLA, (ix) TODA CIFRA DE PASIVO O DE CENSO SE
PUBLICA CON SU UNIDAD Y SU ESTADO PEGADOS, (x) UN ORDEN DE MEDICION SE PRUEBA
CORRIENDOLO ENTERO SOBRE ARBOL LIMPIO ANTES DE MANDARLO, (xi) UNA NOMINA DE
IDS SE RESUELVE ANTES DE DECLARARLA COMPLETA, (xii) UNA ORDEN QUE VIVE AL
FINAL DEL ENCARGO NO ES UNA ORDEN DE TRAMO, (xiii) UNA REGLA MECANICA SE
PRUEBA CONTRA EL CASO QUE LA OPERACION YA DOCUMENTA ANTES DE MANDARLA, (xiv)
UNA REGLA SE ENCARGA CON SU EFECTO NOMBRADO, (xv) UNA FRASE DE CONTENCION ES
UNA MEDICION, NO UN ALIVIO, (xvi) UNA REGLA MECANICA SE ADJUDICA POR SU
EFECTO SOBRE LA CANONICA, NO SOLO POR CUANTOS GRUPOS COLAPSA, (xvii) UNA
CIFRA CON UNIDAD AMBIGUA SE ARRASTRA VUELTA A VUELTA, y (xviii) UN PAR
fichero:linea ES UNA MEDICION CON ESTADO, NO UNA DIRECCION. Le anado UNO, y
sale de mi 4.1:
  (xix) UNA EXENCION QUE ESCRIBE EL AUDITADO NO ES UNA EXENCION, ES UN
  INTERRUPTOR. Si una guarda permite que la cosa medida se declare a si
  misma fuera de alcance, la guarda no mide: pregunta. La exencion se
  concede por una condicion QUE LA GUARDA PUEDA COMPROBAR SOLA (que no
  exista fichero de instrumento en la ventana, y no que alguien escriba que
  no existe), y toda exencion se publica con su cuenta al lado para que su
  crecimiento se vea.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo las guardas delante porque son bloqueantes, y lo
mantengo. Esta vuelta hay CUATRO tareas.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS. NO HAY CODIGO NUEVO EN ESTA TAREA: TODOS SUS
  INSTRUMENTOS EXISTEN Y ESTAN VERDES, LOS CORRI YO HOY.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V135_HEAD_APERTURA.txt. EL GEMELO DE CIERRE VA AL FINAL
  DE VERDAD, DESPUES DE LA ULTIMA OPERACION DE LA TAREA 4 Y ANTES DE
  ESCRIBIR EL REPORTE: docs/loop/SALIDA_V135_HEAD_CIERRE.txt.
  Comprobacion: python scripts/loop/verificar_apertura_sellada.py --vuelta
  135 tiene que dar VERDE EXIT 0, y su salida se cita en el reporte. La
  linea de identidad del reporte mantiene los TRES rotulos y NINGUNO SE
  TECLEA: los tres salen de tallar_identidad_reporte.py.
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT Y NO SE
  PUSHEA SOLO (regla compuesta del acta 128, 3.4). El push por tramo
  empieza DESPUES de ese bloque. Es la UNICA excepcion a la linea de
  commit y push de cada tarea.
  (1.b) EL ORDEN DE CAPTURA, EL QUE FUNCIONO DE LA 128 A LA 134, Y NO SE
  TOCA. REGLA UNICA: `python scripts/run_phase1.py --reaplico-curaduria`
  NO SE CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0 compara el snapshot de
  ANTES del paso 6 y sale verde sobre un estado que el mismo acaba de
  desalinear; el motor si lo ve.
  POR CADA LADO (APERTURA y CIERRE) SE HACE ESTO Y EN ESTE ORDEN, UNA SOLA
  VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V135_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V135_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V135_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO. Salida a
       docs/loop/SALIDA_V135_CICLO_NUMSTAT_<LADO>.txt con su EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS, con <LADO> = APERTURA o CIERRE, estos siete:
    docs/loop/SALIDA_V135_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V135_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V135_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V135_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V135_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V135_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V135_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  EL FORMATO: el tsc cierra con EXIT=<n> sin dos puntos y sin espacio; las
  OTRAS SEIS canonicas cierran con la linea literal EXITCODE: <n>; y las
  TRES del ciclo de 1.b LLEVAN TAMBIEN SU LINEA EXITCODE: <n>, EN LOS DOS
  LADOS, PUESTA EN LA MISMA CORRIDA QUE LAS GENERA Y NO DESPUES. Sigue
  prohibido el fichero de cero bytes. EL EXITCODE SE LEE DEL INSTRUMENTO,
  NUNCA DE UN `$?` PUESTO DETRAS DE UNA TUBERIA.
  MI CONTRASTE, MEDIDO HOY POR MI Y NO PARA COPIAR: marcador A 551 / B 72 /
  C 5 / D 2.760, huecos [], dups 0; conteo 3.853 / 3.184 / 669, sig 9.198,
  prev 9.180, suma 18.378, union 9.833, auto 0, dups 0; motor 25/25; web 80
  passed (80) y 1.030 passed 3 skipped (1.033); tsc EXIT 0 cero lineas;
  desfase 3 filas. SI TU MEDICION TE DA OTRA COSA, MANDA LA TUYA Y DECLARAS
  LA DISCREPANCIA.
  >>> COMMIT DEL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) EN UN SOLO
  >>> COMMIT, SIN PUSH.
  (1.d) LA BATERIA POR OPERACION. Esta vuelta TAMPOCO HAY OPERACION DE
  REGIMEN B: no se escribe un solo nodo. La bateria SE REDUCE A LOS DOS
  LADOS, APERTURA y CIERRE, y el cmp se corre entre esos dos. Reusa
  scripts/loop/vuelta133_baterias_cmp.py adaptado a V135 (mismo filecmp de
  bytes, shallow=False, no lo aflojes). Salida literal a
  docs/loop/SALIDA_V135_BATERIAS_CMP.txt, una linea por par, IDENTICOS o
  DISTINTOS, mas la linea RESUMEN por familia. SI UNA FAMILIA TIENE UN SOLO
  IDENTICO O UN SOLO DISTINTO, SE NOMBRA ESE PAR EXACTO, LEIDO DEL FICHERO,
  Y SE EXPLICA POR QUE ESE Y NO OTRO.
  SE ESPERA que MOTOR y WEB salgan DISTINTOS por duraciones y por Start at,
  Y ESO SE PRUEBA PEGANDO EL DIFF ENTERO: corre `diff` entre los dos MOTOR y
  entre los dos WEB y escribe las salidas a
  docs/loop/SALIDA_V135_1D_DIFF_MOTOR.txt y _WEB.txt, cada una con su
  EXITCODE. SI EL DIFF TRAE UNA SOLA LINEA QUE NO SEA UNA DURACION O UN
  "Start at", ES ROJO Y PARAS. EL CONTEO TIENE QUE SUBIR CERO ARISTAS, y si
  mueve alguna ES ROJO y paras.
  (1.e) CITAS Y TITULOS SE CORREN Y NO SE TOCAN:
  verificar_citas_del_reporte.py, verificar_titulos_normalizados.py y sus
  autopruebas (vuelta122_tarea1e_mutacion_citas.py,
  vuelta123_tarea1e_mutacion_fila_tabla.py, y
  verificar_titulos_normalizados.py --autoprueba), y se pegan. Las dos
  mutaciones viejas TIENEN que seguir dando ROJO. La excepcion declarada de
  sistema_responsabilidad_gerencial se queda EXACTAMENTE como esta.
  (1.f) LA GUARDA DE CIFRAS DEL PLAN, TAMPOCO SE TOCA:
  verificar_cifras_del_plan.py y sus dos casos positivos
  (vuelta123_tarea1f_caso_positivo.py y
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados. Su contrato SOLO
  mira docs/plan/OPERACIONES.jsonl y pares (numero, ruta .test.ts): no
  puede decir nada de OP_S_11_MAPEO_PROPUESTO.md, de eso se encarga
  verificar_cabecera_mapeo.py.
  (1.g) LAS TRES GUARDAS DE ARISTAS SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py con su --autoprueba, verificar_aristas_vivas.py
  con su --autoprueba, y verificar_huerfanas_por_fusion.py con su
  --autoprueba (el argumento es --autoprueba, no --caso-positivo).
  verificar_aristas_vivas.py --antes <HEAD sellado de apertura> --despues
  WORK tiene que dar PERDIDAS 0 y NUEVAS 0. MI CONTRASTE, MEDIDO HOY:
  aristas vivas 7.296 contra 7.296, PERDIDAS 0 NUEVAS 0; huerfanas TOTAL 29
  HEREDADAS 29 REPARADAS 1 FABRICADAS 0.
  (1.h) LA GUARDA DEL SELLO DE CIERRE, AL FINAL Y NO ANTES:
  `python scripts/loop/verificar_cierre_sellado.py --vuelta 135` VERDE EXIT
  0 una vez escrito tu SALIDA_V135_HEAD_CIERRE.txt, y su salida se pega.
  Corre tambien `python scripts/loop/vuelta129_tarea1h_casos_positivos.py`
  y pega su VERDE GENERAL. NO renombres ese script por llevar 129 en el
  nombre. Sus hashes sinteticos CAMBIAN EN CADA CORRIDA; si eso te obliga a
  reescribir una salida ya commiteada, EL MENSAJE DEL COMMIT LO DICE con la
  palabra "regenerada" y el motivo.
  (1.i) LA GUARDA DE CITAS SOBRE TU PROPIO REPORTE, VERDE. Si te da ROJO
  nombrando un fichero tuyo, arreglas EL FICHERO pegandole la medicion que
  le falta, no la cita del reporte.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS COMPROBACIONES, QUE SIGUEN SIENDO
  OCHO, y las ocho salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 135 --comparar docs/loop/REPORTE.md
    python scripts/loop/tallar_identidad_reporte.py --vuelta 135 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 135
    python scripts/loop/verificar_cifras_del_reporte.py            (la REPARADA de la TAREA 2)
    python scripts/loop/verificar_cabecera_mapeo.py                (la EXTENDIDA a SEIS peldanos de 4.c)
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR, la segunda
  IDENTIDAD IDENTICA AL TALLADOR, y las otras SEIS VERDE EXIT 0.
  (1.k) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte, con
  su salida. SI LO QUE 2.d TE OBLIGA A PUBLICAR NO CABE EN 80 LINEAS, NO
  RECORTES LA COBERTURA NI TE INVENTES UN TOPE NUEVO: PARAS Y LO TRAES
  ESCRITO. El tope de 80 es decision del fundador (27 ago 2026) y no lo
  cambio yo.
  (1.l) LOS DOS REGIMENES DE ESCRITURA:
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o
      a docs/ se mide con git diff --numstat y con grep -c "^-[^-]" sobre
      el diff EN CERO, mas git diff --word-diff=porcelain pegado si toca
      una linea vieja. NO necesita las tres guardas. AVISO MEDIDO EN LA 134:
      cuando anades texto AL FINAL de una linea vieja, el numstat marca 1
      borrada aunque no se borre nada; la vara que manda ahi es el
      word-diff porcelain, y las lineas `^-` que cuentan son las de PALABRA
      borrada, NO la cabecera `--- a/...`. Dilo asi en el reporte.
    - REGIMEN A CON LINEA VIEJA: esta vuelta hay UN SOLO fichero viejo
      autorizado a cambiar de contenido, y lo nombro:
      docs/plan/OP_S_11_MAPEO_PROPUESTO.md, porque 4.b lo rehace con la
      regla nueva. NINGUN OTRO. Si te descubres borrando en cualquier otro
      fichero viejo, PARAS.
    - REGIMEN B, DATO: esta vuelta NO SE USA. NO SE TOCA UN SOLO NODO NI UN
      SOLO FICHERO DE dataset/. La regla se aplica A LA TABLA DE PROPUESTA,
      no al catalogo: `OP-S-11` sigue sin ejecutarse. Si te descubres
      necesitando escribir un nodo, es que te saliste del encargo: paras y
      lo traes.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE.
  >>> COMMIT Y PUSH de 1.e, 1.f, 1.g y 1.l en cuanto esas guardas esten
  >>> corridas y pegadas: ESAS CUATRO NO NECESITAN EL LADO DE CIERRE.
  >>> 1.d SI LO NECESITA, asi que 1.d VA AL FINAL, con 1.h, 1.i, 1.j y 1.k
  >>> y el sello de cierre, en el commit del reporte.

- TAREA 2, LA PUERTA DE SERVICIO SE TAPIA. OPERACION DE CODIGO, BLOQUEANTE.
  LA CAIDA ES MIA (acta 134, 4.1) Y LA REPARACION ES TUYA, ASI QUE TE LA
  ESCRIBO CERRADA PARA QUE NO TENGAS QUE DECIDIR NADA.
  (2.a) PRIMERO EL DIAGNOSTICO, Y ANTES DE TOCAR UNA LINEA DEL CODIGO.
  Corre verificar_cifras_del_reporte.py contra el REPORTE.md de la vuelta
  134 (el que hay en el arbol al abrir esta vuelta, antes de que lo
  reescribas) y escribe, en docs/loop/SALIDA_V135_2A_DIAGNOSTICO.txt: la
  linea COBERTURA tal cual; la lista de las exentas por `(sin instrumento)`
  una por una; y, POR CADA UNA de esas exentas, si en su ventana HAY o NO
  HAY citado un `SALIDA_V134_*.txt`, con el nombre del fichero cuando lo
  haya. ESO ES LO QUE MIDE EL TAMANO DE LA PUERTA.
  (2.b) LA EXENCION (iii) SE CONDICIONA A ALGO QUE LA GUARDA COMPRUEBA
  SOLA. Donde hoy dice que basta el literal `(sin instrumento)` pegado,
  ahora dice:
    - El literal `(sin instrumento)` exime una cifra SOLO SI la guarda
      comprueba por si misma que en la ventana de esa cifra NO SE CITA
      NINGUN `SALIDA_V<N>_*.txt`.
    - SI EN LA VENTANA SE CITA UN FICHERO DE SALIDA, EL LITERAL ES ILEGAL:
      ROJO EXIT 1 nombrando la linea, la cifra y el fichero citado, con el
      motivo escrito ("hay instrumento en la ventana: la cifra se coteja,
      no se exime").
    - Las exenciones (i) cabecera e identidad y (ii) el tope de 1.k se
      quedan EXACTAMENTE como estan. NINGUNA CUARTA EXENCION. Si te
      descubres necesitando una, PARAS y la traes escrita.
  (2.c) PARA QUE TAPIAR LA PUERTA NO TE DEJE SIN SALIDA HONESTA, LA GUARDA
  APRENDE A LEER UN TOTAL ROTULADO. Convencion nueva, cerrada:
    - Un instrumento que produzca una cifra publicable imprime, en su
      fichero de salida, una linea con este formato literal:
        CIFRA <etiqueta>: <n> <unidad>
      donde <unidad> es una del vocabulario cerrado que la guarda ya tiene.
    - Cuando una cifra del reporte cita un fichero en su ventana, la guarda
      busca PRIMERO una linea `CIFRA ...` de esa misma unidad en ese
      fichero y coteja contra ella. Solo si no la encuentra cae a la
      convencion generica de recuento que ya tiene escrita. Y si no puede
      contar de ninguna de las dos maneras, ES ROJO nombrando el fichero y
      diciendo que le falta su linea `CIFRA`: el arreglo es PEGARLE LA
      MEDICION AL FICHERO, no quitarle la cita al reporte.
    - Esto es el ramal (iv) hecho codigo y NO afloja nada: solo da al
      instrumento la manera de decir su propio total sin que la guarda
      tenga que adivinar como se cuenta una "grafia" o un "grupo".
  (2.d) LA COBERTURA SE PUBLICA SIEMPRE, VERDE O ROJA, con la MISMA linea
  literal de hoy:
    COBERTURA: <cotejadas> cotejadas / <exentas> exentas / <total> cifras
  y esa linea SE PEGA EN EL REPORTE, tal cual. Y ADEMAS, por el ramal (xix):
  si tu reporte deja alguna cifra exenta, EL REPORTE DICE, POR CADA UNA, POR
  QUE NO HAY INSTRUMENTO QUE LA CUENTE. Una exenta sin motivo escrito al
  lado es una puerta abierta otra vez.
  (2.e) SU PRUEBA POR MUTACION, SOBRE COPIAS DEL REPORTE REAL DE LA 134 (el
  que tienes en el arbol al abrir), Y SON TRES, LAS TRES OBLIGATORIAS. Las
  dos primeras son literalmente las mias, que hoy pasan VERDE:
    - MUTACION 1: en una copia, `118 grafias` a `999 grafias`, dejando el
      `(sin instrumento)` y la cita de `SALIDA_V134_4A_CENSO_COLA.txt` donde
      estan. TIENE QUE CAER ROJO EXIT 1 por la regla nueva de 2.b.
    - MUTACION 2: en otra copia, `54 grupos` a `77 grupos`, igual. ROJO.
    - MUTACION 3, EL CASO NEGATIVO, QUE IMPORTA TANTO COMO LOS OTROS DOS:
      una cifra con su fichero citado, con su linea `CIFRA` puesta y con el
      numero CORRECTO tiene que dar VERDE. Una guarda que siempre cae en
      rojo no mide mas que una que nunca cae.
  Salidas a docs/loop/SALIDA_V135_2E_MUTACION_1.txt, _2.txt y _3.txt.
  (2.f) SE CABLEA en 1.j como septima comprobacion, tal como ya esta. El
  reporte de esta vuelta ya pasa por ella.
  SI EL TEXTO DE ESTA TAREA NO TE ALCANZA PARA EJECUTARLA SIN DECIDIR,
  PARAS Y LO TRAES ESCRITO. No la recortes en silencio.
  >>> COMMIT Y PUSH detras de 2.a y otro detras de 2.e.

- TAREA 3, LOS REGISTROS. Son TRES, las tres REGIMEN A puro, aditivas, sin
  borrar una sola linea.
  (3.a) EL REGISTRO R.16 EN docs/PENDIENTES.md, seccion nueva, correcciones
  y adjudicaciones declaradas de la vuelta 134, con estas CINCO cosas y con
  la medicion de cada una escrita, no resumida: (1) MI CAIDA DE GUARDA CON
  PUERTA DE SERVICIO, con la linea COBERTURA de tu reporte citada literal y
  con mis tres mutaciones (A VERDE, B VERDE, C ROJO) escritas una por una, y
  con la constancia de que tu reparacion de la 134 SI muerde lo que no lleva
  la marca; (2) MI CAIDA DE CIFRA, las CINCO sinteticas que publique contra
  las TRES que son, con la linea de codigo que lo decide citada; (3) MI
  CAIDA DE ENCARGO, con la grafia `The Field Guide to Understandin - Dekker,
  Sidney;` (76 nodos) nombrada y con los DOS predicados escritos al lado,
  118 sin localizador reconocido y 117 que la cola deja intactas; (4) LAS
  TRES ADJUDICACIONES de mi acta 134 (las dos cifras se publican; la
  coronacion no alcanza a los singletons; la extension a `Caps?\.` queda
  adjudicada por el criterio de la propia operacion mas el ramal (xvi), con
  su coste declarado, 54 contra la meta de 55); y (5) el ramal (xix) entero.
  (3.b) LA ETIQUETA DEL CENSO SE REPARA POR ADICION, NO SE BORRA.
  `scripts/loop/vuelta134_censo_cola_no_recorta.py` se queda donde esta y
  con su criterio; lo que cambia es que AHORA PUBLICA LAS DOS CIFRAS, cada
  una con su predicado escrito en la propia salida:
    CIFRA sin localizador reconocido (LOC.search es None): <n> grafias
    CIFRA que la cola deja intactas al caracter (recortar(g) == g): <n> grafias
  con la linea `CIFRA` de 2.c puesta en las dos, y con la grafia que las
  separa NOMBRADA en la salida. Salida a
  docs/loop/SALIDA_V135_3B_CENSO_DOS_PREDICADOS.txt. MI CONTRASTE, MEDIDO
  HOY: 118 y 117, y la que las separa es `The Field Guide to Understandin -
  Dekker, Sidney;`, 76 nodos.
  (3.c) LA REGLA DEL SINGLETON SE ESCRIBE DONDE VIVE LA REGLA DE LA
  CANONICA, por adicion: en la novena entrada de la ficha `fuente` de
  docs/PENDIENTES.md (la que la vuelta 131 abrio con la regla SINTETICA) se
  anade, citando mi acta 134 (3.2), que LA CORONACION MECANICA NO ALCANZA A
  LOS GRUPOS DE UN SOLO MIEMBRO, que conservan su propia grafia como
  canonica y salen con motivo `SIN AGRUPAR (pide decision)`, y que eso es lo
  que el instrumento hace desde la 131. Su word-diff va pegado y el grep de
  lineas borradas tiene que dar CERO.
  >>> COMMIT Y PUSH de 3.a, 3.b y 3.c en cuanto esten escritas.

- TAREA 4, EL TRABAJO: LA EXTENSION A `Caps?\.` SE APLICA. ADJUDICADA EN MI
  ACTA 134 (3.3). REGIMEN A: NO SE TOCA UN SOLO NODO. Lo que cambia es LA
  TABLA DE PROPUESTA, no el catalogo.
  (4.a) LA REGLA, ATADA A LA COLA Y NUNCA SUELTA. Escribe
  scripts/loop/vuelta135_cola_localizador_cap.py que EXTIENDA
  vuelta133_cola_localizador_apendice.py importandolo (su `LOC`, su
  `PUNTUACION_FINAL` y su `recortar_localizador_con_apendice`), sin borrar
  ese fichero y sin reimplementar el union-find. EFECTO NOMBRADO (ramal
  xiv): AGRUPA. La cola pasa a recortar tambien `, Cap. X`, `, Caps. X y Z`
  y sus variantes con minuscula. RAMAL (xiii), SUS DOS CASOS, CORRIDOS ANTES
  DE APLICARLA SOBRE EL CENSO Y PEGADOS:
    - CASO POSITIVO: `Edwards et al., Managing Project Risks, Cap. 9 (Risk
      Transfer)` recorta a `Edwards et al., Managing Project Risks` y cae en
      el MISMO grupo que `Edwards et al., Managing Project Risks, Cap. 2
      (Classifying Risk)`.
    - CASO NEGATIVO: una grafia SIN cola de localizador no se toca ni un
      caracter (recortar(g) == g). Usa la misma que uso la 133,
      `Essentials of Supply Chain Management - Michael H. Hugos`.
  Salida a docs/loop/SALIDA_V135_4A_COLA_CON_CAP.txt, con su linea `CIFRA`.
  (4.b) LA TABLA SE REHACE CON SEIS PELDANOS, Y EL SEXTO SE DEFINE AQUI SIN
  ambiguedad para que no tengas que decidir: EL SEXTO PELDANO ES LA MISMA
  CADENA DE LAS CINCO REGLAS PERO CON LA COLA EXTENDIDA A `Caps?\.` EN
  TODOS LOS SITIOS DONDE LA CADENA USA LA COLA (o sea, en el agrupamiento
  por igualdad de la forma recortada Y en el prefijo sobre la recortada), NO
  un incremento pegado detras del 104. La cabecera de
  docs/plan/OP_S_11_MAPEO_PROPUESTO.md pasa a declarar los SEIS por
  separado: cadena entera 111, mas titulo 108, mas localizador con la cola
  VIEJA 106, mas Apendice 105, mas prefijo sobre recortada 104, mas
  abreviatura `Caps?\.` en la cola 54. Y la tabla entera se recomputa con la
  cola nueva. ESTE ES EL UNICO FICHERO VIEJO QUE ESTA VUELTA PUEDE CAMBIAR
  DE CONTENIDO (1.l). MI CONTRASTE, MEDIDO HOY POR MI: 54 grupos, 17 con 2 o
  mas miembros (92 grafias), 37 solos, 3 canonicas SINTETICAS: `Edwards et
  al., Managing Project Risks` (30 grafias, 30 nodos), `DeMarco y Lister,
  Waltzing with Bears` (13, 13) y `Hubbard, The Failure of Risk Management`
  (10, 10). SI TU MEDICION TE DA OTRA COSA, MANDA LA TUYA Y DECLARAS LA
  DISCREPANCIA.
  (4.c) LA GUARDA DE LA CABECERA SE EXTIENDE A SEIS Y SE PRUEBA POR
  MUTACION. `scripts/loop/verificar_cabecera_mapeo.py` recomputa hoy CINCO
  peldanos: pasa a recomputar SEIS, reusando tu `vuelta135_*` igual que
  reusa los anteriores, y sigue cotejando las cifras de cierre y el TOTAL de
  filas del pie. Su prueba por mutacion, obligatoria: sobre una COPIA de la
  tabla, BORRAS de la cabecera el peldano de 54 y compruebas que cae ROJO
  nombrandolo. Salida a docs/loop/SALIDA_V135_4C_MUTACION.txt. AVISO
  MEDIDO POR MI EN LA 134: esa guarda ya aguanto tres mutaciones mias que tu
  no probaste (una cifra de cierre, otro peldano y los colapsos), asi que no
  la aflojes al extenderla.
  (4.d) LO QUE SE DECLARA Y LO QUE NO SE TOCA, DICHO SIN CONDICIONALES:
    - EL REBASE SE DECLARA EN EL REPORTE, con las dos cifras al lado: el
      catalogo queda en 54 grupos y la meta de `05_SANEO.md` es 55, o sea
      rebasada por UNO. `05_SANEO.md` NO SE TOCA: esa meta es del fundador.
    - `OP-S-11` NO CAMBIA DE ESTADO, SIGUE LISTA. La regla se aplica a la
      TABLA DE PROPUESTA; la operacion no se ejecuta esta vuelta.
    - `OP-S-12` NO SE ABRE: va al final de la pasada entera por la atadura 2
      de docs/plan/00_INDICE.md.
    - LA FASE 05 NO SE DECLARA CERRADA POR NADIE, Y NO TIENES QUE JUZGAR SI
      LO ESTA: cuando lo este lo declaro yo en mi acta.
    - La fase 00_CODIGO tampoco: `OP-C-01` a `OP-C-05`, `OP-S-06` y `OP-S-07`
      figuran LISTA y ESO YA ESTA ADJUDICADO (acta 25 y acta 119). Si
      tropiezas con esos estados, no abras nada.
  >>> COMMIT Y PUSH detras de 4.a y otro detras de 4.c.
  >>> El commit y push del REPORTE va al final, despues del sello de
  >>> cierre de 1.a, del lado de CIERRE de 1.b y 1.c, de la bateria de
  >>> 1.d, de las guardas de 1.h e 1.i, de las OCHO comprobaciones de 1.j
  >>> y de la medida de 1.k. Ese es el ultimo commit de la vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
