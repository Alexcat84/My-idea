Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

SOBRE ESA PRIMERA LINEA: al abrir esta vuelta el arbol tiene que estar
LIMPIO. Yo commitee mis tres ficheros de auditoria (_auditor_v133_ciega.py,
_auditor_v133_sonda_cap.py y _auditor_v133_efecto_cap.py) dentro de mi
propio commit de acta, asi que no te dejo nada colgando. Si ves
dataset/metadata/master_graph.json marcado ` M` con `git diff --numstat`
VACIO, ESO NO ES TRABAJO Y NO SE COMMITEA: es ruido de fin de linea. Si
ves lineas de `etiqueta_arbol` en el diff, tampoco: es el borrado de la
curaduria que deja cualquier corrida de `run_phase1.py`, y se repara
corriendo `python scripts/etiquetas_de_cara.py --aplicar` y
`python scripts/sync_assets_web.py` hasta que
`git diff --numstat -- dataset/ web/ engine/` quede VACIO. CUALQUIER OTRA
COSA SIN COMMITEAR: PARAS Y LA TRAES.

Esta es la VUELTA 134. LA 133 ENTREGO ENTERA Y ENTREGO BIEN. El dataset no
se movio un byte, los unicos dos ficheros viejos que pierden linea son
REPORTE.md y OP_S_11_MAPEO_PROPUESTO.md (los dos autorizados),
PENDIENTES.md 155 anadidas y 0 borradas, OPERACIONES.jsonl intacto. Las
OCHO cifras de tu cabecera cuadran al digito con mi remedicion. Y SOBRE
TODO, LO QUE MAS IMPORTA DE ESTA VUELTA: MI CIEGA REPRODUCE TUS CINCO
PELDANOS AL DIGITO, 111 / 108 / 106 / 105 / 104, con 14 grupos de 2 o mas,
39 grafias, 90 solos, 19 pares unidos por el prefijo, CERO canonicas
SINTETICAS y la familia Lindstrom de 7 grafias y 23 nodos coronada por
`Diana L. Lindstrom, Procurement Project Management Success (J. Ross,
2014)`. Medi tambien la guarda de RESTO por separado: 104 con ella y 104
sin ella, exactamente como estaba encargado. Tu credito de CLASE y de
CIFRA PUBLICADA sigue en CERO.

Y LA ESCALADA QUE TE ENCARGUE EN LA 132 SE ENTREGO Y MUERDE. No me fie: le
hice a tallar_identidad_reporte.py --comparar TRES mutaciones mias sobre
copias, dos de ellas que tu no probaste (el rotulo del medio BORRADO
entero, y un caracter del PRIMER rotulo). Las tres cayeron ROJO EXIT 1
nombrando el rotulo, y un fichero inexistente tambien. Tus caidas 4.1 y
4.3 de la 132 quedan REPARADAS y lo medi yo: los ONCE ficheros de apertura
nacen todos en ccb4d351, que es justo lo que publica el segundo rotulo, y
los dos diff de 1.d estan pegados enteros y los lei linea a linea.

LO QUE COBRA LA 133, Y SON TRES TUYAS Y CUATRO MIAS. LA GRANDE ES MIA.

  UNA CAIDA DE INCUMPLIMIENTO DE ENCARGO (acta 133, 4.1). Mi 4.d nombro
  CINCO cifras una por una (111, 108, 106, 105, 104) y la cabecera de
  OP_S_11_MAPEO_PROPUESTO.md trae CUATRO: el 106 quedo plegado dentro del
  peldano (3) junto con la extension a Apendice. Mi ciega da 106 como
  peldano real y distinto. Nada de lo que escribiste es falso, y el 106
  sobrevive en tu ficha (docs/PENDIENTES.md:1745), pero un escalon se
  borro de una tabla de docs/plan/ y el reporte no dijo que se apartaba
  del encargo. Se repone por ADICION en tu TAREA 3.

  UNA CAIDA DE INCUMPLIMIENTO DE ENCARGO, CON DOS BRAZOS, Y ES LA TUYA QUE
  IMPORTA (acta 133, 4.2). Sobre 2.e: (a) mi contrato mandaba "esa lista
  se pega en el reporte" y la lista de "cifras sin fichero que contar" NO
  esta en el reporte; (b) mandaba mutar "una cifra cotejable en una COPIA
  del reporte" y la mutacion se corrio sobre un "reporte fabricado", no
  sobre el real. Los dos brazos tapan el mismo hecho, que medi yo
  corriendo tu guarda contra el reporte de verdad: COTEJA UNA CIFRA DE
  OCHO, Y ESA UNA ES UN CERO ("0 pares == 0"). Las siete que importan (155
  lineas, 7 grafias, 23 nodos, 14 grupos, 39 grafias, 49 colapsos, 67
  lineas) caen todas en la lista de no cotejadas. Y lo probe: mute
  "14 grupos" a "19 grupos" sobre una copia del reporte real y tu guarda
  sigue VERDE EXIT 0.

  UNA CAIDA DE REPORTE, Y NO ACUMULA (acta 133, 4.3). Tu discutible dice
  "la cita que si la trae, EN LA MISMA VECINDAD, es
  docs/PENDIENTES.md:1696". En docs/PENDIENTES.md TU SI escribiste el
  calificativo que la hace verdadera ("en esta misma vecindad DE LA FICHA
  del campo fuente"); el reporte lo perdio, y sin el la frase es falsa:
  1.696 esta a 1.363 lineas de 3.059. Por la letra del 27 ago 2026 la
  cifra vive en una ruta dentro de prosa de acompanamiento de un
  discutible declarado, no en tabla, cabecera ni conclusion: SE REGISTRA,
  DISPARA LA RELECTURA AL DOBLE Y NO ACUMULA, igual que el precedente de
  la vuelta 95. LA RACHA DE REPORTE BAJA DE DOS A CERO.

Y CUATRO MIAS, Y LA PRIMERA ES LA GRANDE DE LA VUELTA:

  MIA, DE GUARDA CEGADA AL NACER (acta 133, 4.4). La segunda mitad de la
  escalada nacio sin dientes POR MI LETRA, NO POR TU CODIGO: yo escribi en
  2.e "si un numero no encuentra fichero de salida en su ventana, NO es
  rojo: se LISTA". En MODO AUSTERO esa salida de emergencia se traga 7 de
  8. TU IMPLEMENTASTE MI CONTRATO AL PIE DE LA LETRA. Encargue una guarda
  que no puede fallar y la llame escalada. Su reparacion es tu TAREA 2 y
  es BLOQUEANTE.

  MIA, DE PROCEDIMIENTO (acta 133, 4.5). Lei un codigo de salida tomado
  DETRAS DE UNA TUBERIA (`| tail -6`) y por un momento tuve por bueno que
  el tallador daba EXIT 0 sobre un fichero inexistente. Es palabra por
  palabra la trampa que mi propio encargo de 1.c prohibe. Corrido sin
  tuberia da EXIT 1, como debe.

  MIA, DE ENCARGO, Y ES LA MISMA FORMA QUE CREI HABER REPARADO (acta 133,
  4.6). Mi 1.l mando "COMMIT Y PUSH de 1.d a 1.g en cuanto esas guardas
  esten corridas", y 1.d NECESITA EL LADO DE CIERRE, que no existe hasta
  despues de la ultima operacion. Encargo contradictorio consigo mismo
  otra vez, con otra cara. Tu lo resolviste bien y lo declaraste en el
  mensaje del commit. ESTA VUELTA LA CONTRADICCION NO EXISTE: ver la linea
  de commit de 1.l, que parte 1.d del resto.

  MIA, DE PROCEDIMIENTO, SOBRE MI PROPIO COMMIT DE ACTA (acta 133, 4.8).
  Escribi el mensaje del commit de mi acta con la sintaxis de aqui-cadena
  de PowerShell dentro de una llamada de bash, que no la entiende, y el
  asunto quedo en un `@` suelto. NO ES COSMETICO:
  tallar_cabecera_reporte.py LEE ESE ASUNTO Y LO PUBLICA en la fila de
  identidad de TU reporte, o sea que el `@` habria entrado en tu cabecera
  de esta vuelta. Lo vi corriendo el tallador contra el commit recien
  hecho y lo repare enmendandolo antes de que lo heredaras. Dos shells
  conviven en esta maquina y su sintaxis no se mezcla.

EL TRAMO QUE SE RELEE AL DOBLE, POR DECIMOCUARTA VEZ. Siguen los ramales
(i) NINGUNA MEDICION SE ATRIBUYE A UN ESTADO QUE NO ES EL SUYO, (ii) EL
EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, (iii)
NINGUNA GUARDA SE ESTRECHA EN SILENCIO, (iv) TODA CIFRA SOBRE UN ARTEFACTO
CONTABLE SE LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO, (v) NINGUNA
VARA SE ESTRECHA EN EL ENCARGO, (vi) UN SUPERVIVIENTE SE RAZONA COMO SE
RAZONA UNA CLASE, (vii) UNA FUSION NO ACABA HASTA QUE LA ULTIMA ARISTA DEL
ABSORBIDO ESTA RECONSTRUIDA, (viii) UNA CIFRA DE PASIVO SE PARTE EN DOS
ANTES DE REMITIRLA, (ix) TODA CIFRA DE PASIVO O DE CENSO SE PUBLICA CON SU
UNIDAD Y SU ESTADO PEGADOS, (x) UN ORDEN DE MEDICION SE PRUEBA CORRIENDOLO
ENTERO SOBRE ARBOL LIMPIO ANTES DE MANDARLO, (xi) UNA NOMINA DE IDS SE
RESUELVE ANTES DE DECLARARLA COMPLETA, (xii) UNA ORDEN QUE VIVE AL FINAL
DEL ENCARGO NO ES UNA ORDEN DE TRAMO, (xiii) UNA REGLA MECANICA SE PRUEBA
CONTRA EL CASO QUE LA OPERACION YA DOCUMENTA ANTES DE MANDARLA, (xiv) UNA
REGLA SE ENCARGA CON SU EFECTO NOMBRADO, (xv) UNA FRASE DE CONTENCION ES
UNA MEDICION, NO UN ALIVIO, (xvi) UNA REGLA MECANICA SE ADJUDICA POR SU
EFECTO SOBRE LA CANONICA, NO SOLO POR CUANTOS GRUPOS COLAPSA, y (xvii) UNA
CIFRA CON UNIDAD AMBIGUA SE ARRASTRA VUELTA A VUELTA. Le anado UNO, y sale
de mi adjudicacion del discutible que marcaste:
  (xviii) UN PAR fichero:linea ES UNA MEDICION CON ESTADO, NO UNA
  DIRECCION. En un fichero que crece, el numero de linea caduca solo y sin
  aviso: docs/PENDIENTES.md:3059 fue VERDADERO al medirse (lo comprobe con
  `git show 5eb04ca5:docs/PENDIENTES.md`), es FALSO hoy, y su contenido
  vive en el 3138. Se publica con el commit en que se midio, o con un
  ancla de texto citada al lado. Y el relevo de un par caducado SE BUSCA
  POR CONTENIDO: quien busca el numero encuentra el registro que lo cita,
  no el sitio donde la cosa vive. Eso es exactamente lo que te paso con el
  1696, y es la unica parte de tu hallazgo que no era correcta.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo las guardas delante porque son bloqueantes, y lo
mantengo. Esta vuelta hay CUATRO tareas.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS. NO HAY CODIGO NUEVO EN ESTA TAREA: TODOS SUS
  INSTRUMENTOS EXISTEN Y ESTAN VERDES, LOS CORRI YO HOY.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V134_HEAD_APERTURA.txt. EL GEMELO DE CIERRE VA AL FINAL
  DE VERDAD, DESPUES DE LA ULTIMA OPERACION DE LA TAREA 4 Y ANTES DE
  ESCRIBIR EL REPORTE: docs/loop/SALIDA_V134_HEAD_CIERRE.txt.
  Comprobacion: python scripts/loop/verificar_apertura_sellada.py --vuelta
  134 tiene que dar VERDE EXIT 0, y su salida se cita en el reporte. La
  linea de identidad del reporte mantiene los TRES rotulos y NINGUNO SE
  TECLEA: los tres salen de tallar_identidad_reporte.py, que ya existe y
  que rompi yo por tres sitios sin conseguir doblarlo.
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT Y NO SE
  PUSHEA SOLO (regla compuesta del acta 128, 3.4). El push por tramo
  empieza DESPUES de ese bloque. Es la UNICA excepcion a la linea de
  commit y push de cada tarea.
  (1.b) EL ORDEN DE CAPTURA, EL QUE FUNCIONO DE LA 128 A LA 133, Y NO SE
  TOCA. REGLA UNICA: `python scripts/run_phase1.py --reaplico-curaduria`
  NO SE CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0 compara el snapshot de
  ANTES del paso 6 y sale verde sobre un estado que el mismo acaba de
  desalinear; el motor si lo ve.
  POR CADA LADO (APERTURA y CIERRE) SE HACE ESTO Y EN ESTE ORDEN, UNA SOLA
  VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V134_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V134_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V134_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO. Salida a
       docs/loop/SALIDA_V134_CICLO_NUMSTAT_<LADO>.txt con su EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS, con <LADO> = APERTURA o CIERRE, estos siete:
    docs/loop/SALIDA_V134_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V134_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V134_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V134_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V134_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V134_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V134_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  EL FORMATO: el tsc cierra con EXIT=<n> sin dos puntos y sin espacio; las
  OTRAS SEIS canonicas cierran con la linea literal EXITCODE: <n>; y las
  TRES del ciclo de 1.b LLEVAN TAMBIEN SU LINEA EXITCODE: <n>, EN LOS DOS
  LADOS, PUESTA EN LA MISMA CORRIDA QUE LAS GENERA Y NO DESPUES. Sigue
  prohibido el fichero de cero bytes. EL EXITCODE SE LEE DEL INSTRUMENTO,
  NUNCA DE UN `$?` PUESTO DETRAS DE UNA TUBERIA. Esta linea la incumpli yo
  esta vuelta (mi 4.5), asi que la repito sin rebajarla: vale para los dos.
  MI CONTRASTE, MEDIDO HOY POR MI Y NO PARA COPIAR: marcador A 551 / B 72 /
  C 5 / D 2.760, huecos [], dups 0; conteo 3.853 / 3.184 / 669, sig 9.198,
  prev 9.180, suma 18.378, union 9.833, auto 0, dups 0; motor 25/25; web 80
  passed (80) y 1.030 passed 3 skipped (1.033); tsc EXIT 0 cero lineas;
  desfase 3 filas. SI TU MEDICION TE DA OTRA COSA, MANDA LA TUYA Y DECLARAS
  LA DISCREPANCIA.
  >>> COMMIT DEL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) EN UN SOLO
  >>> COMMIT, SIN PUSH.
  (1.d) LA BATERIA POR OPERACION. Esta vuelta NO HAY OPERACION DE REGIMEN
  B: no se escribe un solo nodo. La bateria SE REDUCE A LOS DOS LADOS,
  APERTURA y CIERRE, y el cmp se corre entre esos dos. Reusa
  scripts/loop/vuelta133_baterias_cmp.py adaptado a V134 (mismo filecmp de
  bytes, shallow=False, no lo aflojes). Salida literal a
  docs/loop/SALIDA_V134_BATERIAS_CMP.txt, una linea por par, IDENTICOS o
  DISTINTOS, mas la linea RESUMEN por familia. SI UNA FAMILIA TIENE UN
  SOLO IDENTICO O UN SOLO DISTINTO, SE NOMBRA ESE PAR EXACTO, LEIDO DEL
  FICHERO, Y SE EXPLICA POR QUE ESE Y NO OTRO.
  SE ESPERA que MOTOR y WEB salgan DISTINTOS por duraciones y por
  Start at, Y ESO SE PRUEBA PEGANDO EL DIFF ENTERO, como hiciste bien esta
  vuelta: corre `diff` entre los dos MOTOR y entre los dos WEB y escribe
  las salidas a docs/loop/SALIDA_V134_1D_DIFF_MOTOR.txt y _WEB.txt, cada
  una con su EXITCODE. SI EL DIFF TRAE UNA SOLA LINEA QUE NO SEA UNA
  DURACION O UN "Start at", ES ROJO Y PARAS. EL CONTEO TIENE QUE SUBIR
  CERO ARISTAS, y si mueve alguna ES ROJO y paras.
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
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados. Recuerda el limite
  de su contrato, que ya rectifique: SOLO mira docs/plan/OPERACIONES.jsonl
  y pares (numero, ruta .test.ts). No puede decir nada de
  OP_S_11_MAPEO_PROPUESTO.md. De eso se encarga la guarda nueva de 2.f.
  (1.g) LAS TRES GUARDAS DE ARISTAS SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py con su --autoprueba, verificar_aristas_vivas.py
  con su --autoprueba, y verificar_huerfanas_por_fusion.py con su
  --autoprueba (OJO CON EL NOMBRE DEL ARGUMENTO: es --autoprueba, yo probe
  hoy con --caso-positivo y el script lo rechaza, con razon).
  verificar_aristas_vivas.py --antes <HEAD sellado de apertura> --despues
  WORK tiene que dar PERDIDAS 0 y NUEVAS 0. MI CONTRASTE, MEDIDO HOY:
  aristas vivas 7.296 contra 7.296, PERDIDAS 0 NUEVAS 0; huerfanas TOTAL 29
  HEREDADAS 29 REPARADAS 1 FABRICADAS 0.
  (1.h) LA GUARDA DEL SELLO DE CIERRE, AL FINAL Y NO ANTES:
  `python scripts/loop/verificar_cierre_sellado.py --vuelta 134` VERDE EXIT
  0 una vez escrito tu SALIDA_V134_HEAD_CIERRE.txt, y su salida se pega.
  Corre tambien `python scripts/loop/vuelta129_tarea1h_casos_positivos.py`
  y pega su VERDE GENERAL. NO renombres ese script por llevar 129 en el
  nombre. Sus hashes sinteticos CAMBIAN EN CADA CORRIDA; si eso te obliga a
  reescribir una salida ya commiteada, EL MENSAJE DEL COMMIT LO DICE con la
  palabra "regenerada" y el motivo.
  (1.i) LA GUARDA DE CITAS SOBRE TU PROPIO REPORTE, VERDE. Si te da ROJO
  nombrando un fichero tuyo, arreglas EL FICHERO pegandole la medicion que
  le falta, no la cita del reporte.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS COMPROBACIONES, QUE ESTA VUELTA
  SON OCHO, y las ocho salidas se pegan CITADAS POR SU PROPIO NOMBRE DE
  FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 134 --comparar docs/loop/REPORTE.md
    python scripts/loop/tallar_identidad_reporte.py --vuelta 134 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 134
    python scripts/loop/verificar_cifras_del_reporte.py            (la REPARADA de 2.a a 2.e)
    python scripts/loop/verificar_cabecera_mapeo.py                (la NUEVA de 2.f)
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR, la segunda
  IDENTIDAD IDENTICA AL TALLADOR, y las otras SEIS VERDE EXIT 0.
  (1.k) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte, con
  su salida. SI LA COBERTURA QUE TE PIDE 2.c NO CABE EN 80 LINEAS, NO
  RECORTES LA COBERTURA NI TE INVENTES UN TOPE NUEVO: PARAS Y LO TRAES
  ESCRITO. El tope de 80 es decision del fundador (27 ago 2026) y no lo
  cambio yo.
  (1.l) LOS DOS REGIMENES DE ESCRITURA:
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o
      a docs/ se mide con git diff --numstat y con grep -c "^-[^-]" sobre
      el diff EN CERO, mas git diff --word-diff=porcelain pegado si toca
      una linea vieja. NO necesita las tres guardas.
    - REGIMEN A CON LINEA VIEJA: esta vuelta NINGUN fichero viejo pierde
      una linea. La reposicion del peldano 106 en
      docs/plan/OP_S_11_MAPEO_PROPUESTO.md es POR ADICION (3.c), igual que
      las correcciones de la TAREA 3. Si te descubres borrando en un
      fichero viejo, PARAS.
    - REGIMEN B, DATO: esta vuelta NO SE USA. NO SE TOCA UN SOLO NODO NI UN
      SOLO FICHERO DE dataset/. Si te descubres necesitando uno, es que te
      saliste del encargo: paras y lo traes.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE.
  >>> COMMIT Y PUSH de 1.e, 1.f, 1.g y 1.l en cuanto esas guardas esten
  >>> corridas y pegadas: ESAS CUATRO NO NECESITAN EL LADO DE CIERRE.
  >>> 1.d SI LO NECESITA, asi que 1.d VA AL FINAL, con 1.h, 1.i, 1.j y 1.k
  >>> y el sello de cierre, en el commit del reporte. ESTA ES LA REPARACION
  >>> DE MI 4.6 Y ESTA VUELTA NO SE CONTRADICE.

- TAREA 2, LA REPARACION DE LA GUARDA CEGADA. OPERACION DE CODIGO,
  BLOQUEANTE. LA CAIDA ES MIA (acta 133, 4.4) Y LA REPARACION ES TUYA, ASI
  QUE TE LA ESCRIBO CERRADA PARA QUE NO TENGAS QUE DECIDIR NADA.
  (2.a) PRIMERO EL DIAGNOSTICO, Y ANTES DE TOCAR UNA LINEA DEL CODIGO.
  Corre verificar_cifras_del_reporte.py contra el REPORTE.md de la vuelta
  133 (el que hay en el arbol al abrir esta vuelta, antes de que lo
  reescribas) y, POR CADA UNA de las SIETE cifras que hoy caen en "cifra
  sin fichero que contar", escribe cual de estas DOS cosas le pasa:
    (A) NO SE ENCONTRO NINGUN docs/loop/SALIDA_V133_*.txt en su ventana, o
    (B) SI se encontro fichero, pero la cifra no se pudo CONTAR en el.
  La respuesta se mide, no se supone: si hace falta, le anades al script
  una traza que lo diga. Salida a
  docs/loop/SALIDA_V134_2A_DIAGNOSTICO.txt, con las siete lineas, cada una
  con su motivo (A) o (B) y, si es (B), el nombre del fichero que si
  encontro. ESTO ES LO QUE MIDE POR QUE MI CONTRATO FALLO, y sin ello la
  reparacion seria a ciegas.
  (2.b) LA SALIDA DE EMERGENCIA SE ESTRECHA, Y ASI QUEDA ESCRITA. Donde mi
  contrato decia "si un numero no encuentra fichero de salida en su
  ventana, NO es rojo: se LISTA", ahora dice:
    - Una cifra (numero, unidad del vocabulario cerrado) SIN fichero en su
      ventana es ROJO EXIT 1, nombrando la linea y la cifra, SALVO que
      caiga en una de estas TRES exenciones, que son cerradas y son todas:
      (i) las cifras del parrafo de identidad y de la tabla tallada de la
      cabecera, que ya cubren tallar_identidad_reporte.py y
      tallar_cabecera_reporte.py; (ii) la cifra del tope de 1.k, que habla
      del propio REPORTE.md y se coteja con `wc -l` en vez de con un
      fichero de salida; (iii) una cifra que el reporte marque
      explicitamente con el literal `(sin instrumento)` pegado, que
      obliga a declararlo en vez de callarlo, y que la guarda LISTA aparte
      y CUENTA.
    - NINGUNA OTRA EXENCION. Si te descubres necesitando una cuarta,
      PARAS y la traes escrita: eso seria doctrina nueva y no es tuya ni
      mia sin medirla.
  (2.c) LA COBERTURA SE PUBLICA SIEMPRE, VERDE O ROJA. La guarda termina
  con una linea literal:
    COBERTURA: <cotejadas> cotejadas / <exentas> exentas / <total> cifras
  y esa linea SE PEGA EN EL REPORTE, tal cual. Una guarda que no dice
  cuanto abarca es la que me cegó a mi: que lo diga ella sola cada vuelta.
  (2.d) SU PRUEBA POR MUTACION, Y ESTA VEZ SOBRE UNA COPIA DEL REPORTE
  REAL, NO SOBRE UNO FABRICADO. Dos casos, los dos obligatorios:
    - MUTACION 1: cambias una cifra COTEJABLE del reporte de esta vuelta
      en una copia y compruebas ROJO EXIT 1 nombrando la linea, la cifra
      escrita y la contada.
    - MUTACION 2: BORRAS la cita del fichero de salida que acompana a una
      cifra, en otra copia, y compruebas que la guarda cae en ROJO por la
      regla nueva de 2.b, en vez de listarla y callarse. ESTA ES LA
      MUTACION QUE HABRIA CAZADO MI PROPIO CONTRATO.
  Salidas a docs/loop/SALIDA_V134_2D_MUTACION_1.txt y _2.txt.
  (2.e) SE CABLEA en 1.j como septima comprobacion, tal como quedo escrito
  arriba. El reporte de esta vuelta ya pasa por ella.
  (2.f) LA GUARDA QUE FALTABA, Y QUE HOY TIENE CASO (acta 133, 4.7):
  scripts/loop/verificar_cabecera_mapeo.py. Contrato cerrado:
    - Recomputa desde dataset/ los CINCO peldanos de la tabla de
      OP_S_11_MAPEO_PROPUESTO.md (cadena entera; mas titulo; mas
      localizador con la cola VIEJA; mas Apendice en la cola; mas prefijo
      sobre recortada) reusando tus propios scripts vuelta131_*,
      vuelta132_* y vuelta133_*, no reimplementandolos.
    - Lee la cabecera de docs/plan/OP_S_11_MAPEO_PROPUESTO.md, extrae las
      cifras de peldano que declare, y coteja UNA A UNA. Si la cabecera
      declara MENOS peldanos de los que el recomputo produce, ES ROJO EXIT
      1 nombrando el peldano que falta: ESE es exactamente el caso de esta
      vuelta, el 106 que desaparecio.
    - Coteja tambien las cifras de cierre de la cabecera (grupos de 2 o
      mas, grafias en grupo, solos, cuantos faltan para 55) y el TOTAL
      filas del pie contra las filas reales de la tabla.
    - Su prueba por mutacion, obligatoria: sobre una COPIA de la tabla,
      borras el peldano de 106 de la cabecera y compruebas que cae ROJO
      nombrandolo. Salida a
      docs/loop/SALIDA_V134_2F_MUTACION.txt.
  SI EL TEXTO DE ESTA TAREA NO TE ALCANZA PARA EJECUTARLA SIN DECIDIR,
  PARAS Y LO TRAES ESCRITO. No la recortes en silencio: eso seria el ramal
  (iii), y esta vuelta el ramal (iii) lo incumpli yo, no tu.
  >>> COMMIT Y PUSH detras de 2.d y otro detras de 2.f.

- TAREA 3, LOS REGISTROS. Son TRES, las tres REGIMEN A puro, aditivas, sin
  borrar una sola linea.
  (3.a) EL REGISTRO R.15 EN docs/PENDIENTES.md, seccion nueva,
  correcciones declaradas de la vuelta 133, con estas SEIS cosas y con la
  medicion de cada una escrita, no resumida: (1) tu incumplimiento del
  peldano 106, con las cinco cifras que el encargo nombro y las cuatro que
  la cabecera trajo; (2) tu incumplimiento de 2.e con sus DOS brazos, y
  con la medicion que hice yo escrita entera (UNA cifra cotejada de OCHO,
  y esa una un CERO; las siete no cotejadas listadas por su nombre; y mi
  mutacion de "14 grupos" a "19 grupos" que la guarda dejo pasar VERDE);
  (3) tu caida de reporte del "en la misma vecindad", con la constancia de
  que en PENDIENTES.md TU SI escribiste el calificativo que la hace
  verdadera y de que por la letra del 27 ago 2026 NO ACUMULA, y de que la
  racha de reporte BAJA DE DOS A CERO; (4) MI CAIDA DE GUARDA CEGADA AL
  NACER, con mi frase de contrato citada literal y con la constancia de
  que tu la implementaste al pie de la letra; (5) mis otras TRES, la del
  codigo de salida detras de una tuberia, la del encargo contradictorio de
  1.l y la del asunto de commit malformado que habria entrado en tu propia
  cabecera; y (6) el ramal (xviii) entero.
  (3.b) LA CORRECCION DEL PAR CADUCADO, POR ADICION Y CON SU ESTADO. Al
  pie de la BOLSA 2a de la ficha del campo fuente Y al pie de R.13(6), sin
  tocar una linea de las ya escritas, se anade la medicion de hoy:
  `docs/PENDIENTES.md:3059` FUE VERDADERO medido en el commit `5eb04ca5`
  (la fila del 2.283, `defensas_en_profundidad_2` / `_3`, con
  *Managing the Risks of Organizational Accidents* dentro), esta CADUCADO
  hoy porque el fichero paso de 8.183 a 8.444 lineas, y su contenido vive
  hoy en `docs/PENDIENTES.md:3138`. Se escribe con las DOS cosas pegadas,
  el par y el commit, por el ramal (xviii). Y se deja dicho que
  `docs/PENDIENTES.md:1696` NO era el relevo: es el registro que CITA a
  3059, dentro de la propia ficha, no un sitio donde el titulo viva por si
  mismo. Los otros seis pares de R.13(6) se re-miden hoy igual y cada uno
  se reescribe por adicion con el commit en que lo mediste.
  (3.c) LA REPOSICION DEL PELDANO 106 EN LA CABECERA DE
  docs/plan/OP_S_11_MAPEO_PROPUESTO.md, POR ADICION Y SIN BORRAR NADA: la
  cabecera pasa a declarar los CINCO peldanos por separado, cadena entera
  111, mas titulo 108, mas localizador con la cola VIEJA 106, mas Apendice
  en la cola 105, mas prefijo sobre recortada 104. Su word-diff va pegado
  y el grep de lineas borradas tiene que dar CERO. Cuando 2.f este escrita,
  esta cabecera tiene que pasarla en VERDE.
  >>> COMMIT Y PUSH de 3.a, 3.b y 3.c en cuanto esten escritas.

- TAREA 4, EL TRABAJO. LA COLA DE LOCALIZADOR NO RECONOCE LA ABREVIATURA
  `Cap.`, Y ESO NO LO VIO NADIE HASTA HOY. REGIMEN A ESTRICTO: NO SE TOCA
  UN SOLO NODO NI UN SOLO FICHERO DE dataset/, Y NO SE APLICA NINGUNA
  REGLA NUEVA A LA TABLA. ESTA VUELTA SOLO SE MIDE. YO ADJUDICO EN EL ACTA
  134, Y DIGO POR QUE NO ADJUDICO YA: la cita que sostuvo la adjudicacion
  de `Apendice` en mi acta 132 (3.1) fue que las dos formas convivian en
  la MISMA familia del censo, y aqui esa cita NO EXISTE. Lo medi.
  (4.a) EL CENSO DE LO QUE LA COLA NO RECORTA. Escribe
  scripts/loop/vuelta134_censo_cola_no_recorta.py: de las 129 grafias, di
  cuantas la cola de la 133 NO recorta, y para esas, agrupa por la primera
  palabra que sigue a su ULTIMA coma, con su cuenta. Salida a
  docs/loop/SALIDA_V134_4A_CENSO_COLA.txt.
  MI CONTRASTE, MEDIDO HOY POR MI: 117 de 129 no se recortan, y la palabra
  que encabeza es `Cap.` con 48; detras van `Waltzing` 5 y luego colas de
  uno. Con el plural incluido, 55 grafias y 62 nodos llevan `, Cap.` o
  `, Caps.`. Si te sale otra cosa, manda la tuya y declara la discrepancia.
  (4.b) EL EFECTO, CON LAS DOS CIFRAS QUE EL RAMAL (xvi) EXIGE Y NO CON
  UNA. Escribe scripts/loop/vuelta134_efecto_cap_abreviado.py: la misma
  cadena de cuatro reglas de la 133, pero con la cola extendida a
  `Caps?\.`, y publica LAS DOS COSAS AL LADO, grupos resultantes Y
  canonicas resultantes, con las SINTETICAS listadas UNA POR UNA con su
  numero de grafias y de nodos. Salida a
  docs/loop/SALIDA_V134_4B_EFECTO_CAP.txt.
  MI CONTRASTE, MEDIDO HOY POR MI: 104 grupos pasarian a 54 (o sea que la
  meta de 55 de 05_SANEO.md quedaria rebasada por UNO) y las canonicas
  SINTETICAS pasarian de 0 a CINCO: `Edwards et al., Managing Project
  Risks` (30 grafias), `DeMarco y Lister, Waltzing with Bears` (13),
  `Hubbard, The Failure of Risk Management` (10), `Sharon Cullinane,
  E-Logistics` (1 grafia, 8 nodos) y una quinta que es una grafia
  malformada, ver 4.d.
  (4.c) LA CONVIVENCIA, MEDIDA Y NO SUPUESTA, PORQUE DE ELLA DEPENDE MI
  ADJUDICACION. Para cada familia del censo que traiga un localizador de
  capitulo, di si lo trae ESCRITO (`capitulo`), ABREVIADO (`Cap.`) o LAS
  DOS FORMAS. MI CONTRASTE, MEDIDO HOY POR MI: NINGUNA familia trae las
  dos; las de forma escrita (las dos Lindstrom, Max Muller, Rushton et
  al.) y las de forma abreviada (Edwards, DeMarco y Lister, Hubbard,
  Cullinane) son conjuntos DISJUNTOS. SI ESO SE CONFIRMA, la extension a
  `Cap.` NO se puede adjudicar por la misma cita que `Apendice` y hay que
  adjudicarla por otra o no adjudicarla: eso lo hago yo, no tu. Salida
  dentro de docs/loop/SALIDA_V134_4C_CONVIVENCIA.txt.
  (4.d) LAS CINCO SINTETICAS SE LEEN UNA POR UNA Y SE ESCRIBE SI CADA UNA
  ES EL TITULO DEL LIBRO O ES BASURA. El ramal (xvi) dice que una regla se
  juzga por su efecto sobre la CANONICA: pues se mira. Por cada una de las
  cinco, escribe la canonica que produciria y una linea diciendo si eso es
  un titulo de libro legible o no. Y MIRA CON ATENCION LA QUINTA, que en
  mi medicion sale asi: una grafia que es una frase entera con comas y un
  parentesis sin cerrar, del estilo `Sintesis del metodo aplicado al
  emprendedor individual (riesgo de rotacion, Waltzing with Bears, Cap.
  ...`. DOS COSAS DE ESA, LAS DOS MEDIDAS Y NINGUNA SUPUESTA: (1) si la
  cola la cortase, que canonica saldria, y (2) si sus acentos estan bien
  en el dato o estan rotos. Yo la vi con interrogantes en mi consola y NO
  AFIRMO que el dato este corrupto: lee el JSON con encoding utf-8 y
  dilo con la salida delante. Salida a
  docs/loop/SALIDA_V134_4D_SINTETICAS.txt.
  (4.e) LO QUE NO SE TOCA ESTA VUELTA, DICHO SIN CONDICIONALES: la tabla
  OP_S_11_MAPEO_PROPUESTO.md NO se rehace (lo unico que cambia en ella es
  la ADICION del peldano 106 de 3.c). `OP-S-11` NO CAMBIA DE ESTADO, SIGUE
  LISTA. `OP-S-12` NO SE ABRE: va al final de la pasada entera por la
  atadura 2 de docs/plan/00_INDICE.md. LA FASE 05 NO SE DECLARA CERRADA
  POR NADIE, Y NO TIENES QUE JUZGAR SI LO ESTA: cuando lo este lo declaro
  yo en mi acta. Y la fase 00_CODIGO tampoco: `OP-C-01` a `OP-C-05`,
  `OP-S-06` y `OP-S-07` figuran LISTA y ESO YA ESTA ADJUDICADO (acta 25 y
  acta 119). Si tropiezas con esos estados, no abras nada.
  >>> COMMIT Y PUSH detras de 4.b y otro detras de 4.d.
  >>> El commit y push del REPORTE va al final, despues del sello de
  >>> cierre de 1.a, del lado de CIERRE de 1.b y 1.c, de la bateria de
  >>> 1.d, de las guardas de 1.h e 1.i, de las OCHO comprobaciones de 1.j
  >>> y de la medida de 1.k. Ese es el ultimo commit de la vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
