Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

SOBRE ESA PRIMERA LINEA: al abrir esta vuelta el arbol tiene que estar
LIMPIO. Yo commitee mis ficheros de auditoria (`_auditor_v135_*`) dentro de
mi propio commit de acta, asi que no te dejo nada colgando. Si ves
`dataset/metadata/master_graph.json` marcado ` M` con `git diff --numstat`
VACIO, ESO NO ES TRABAJO Y NO SE COMMITEA: es ruido de fin de linea. Si ves
lineas de `etiqueta_arbol` en el diff, tampoco: es el borrado de la curaduria
que deja cualquier corrida de `run_phase1.py`, y se repara corriendo
`python scripts/etiquetas_de_cara.py --aplicar` y
`python scripts/sync_assets_web.py` hasta que
`git diff --numstat -- dataset/ web/ engine/` quede VACIO. CUALQUIER OTRA
COSA SIN COMMITEAR: PARAS Y LA TRAES.

Esta es la VUELTA 136, Y ES LA VUELTA EN QUE SE VUELVE A ESCRIBIR EN EL
CATALOGO. Llevas muchas vueltas en REGIMEN A puro; esta es REGIMEN B, y el
primer nodo se toca despues de que las guardas esten verdes, no antes.

LA 135 ENTREGO EL TRABAJO ENTERO Y ME TAPIO LA PUERTA QUE YO DEJE ABIERTA.
Lo verifique con mutaciones mias que tu no corriste: le pegue `(sin
instrumento)` a una cifra que SI tiene fichero en la ventana y cayo ROJO
nombrando el fichero, le falsee `118` a `999` y `54` a `77` y cayo ROJO las
dos veces, y con el reporte intacto da VERDE 7 de 7. A la guarda de la
cabecera de mapeo, ya extendida a seis peldanos, le hice CINCO mutaciones mas
(las SINTETICAS de 3 a 5, el peldano 106 a 107, los 37 sin agrupar a 36,
borrarle una fila entera, y la intacta) y aguanto las cinco. LAS DOS GUARDAS
MUERDEN Y LA EXTENSION NO AFLOJO NINGUNA. La tabla la conte yo del fichero
escrito, sin usar tu motor: 129 filas, 54 canonicas, 17 grupos de 2 o mas, 92
en grupo, 37 solas, 3 SINTETICAS con 30, 13 y 10 grafias, pie 129 igual a
129. Al digito. Y las ocho cifras de tu cabecera cuadran con mi remedicion.

TE COBRO DOS, Y LAS DOS TIENEN LA MISMA RAIZ: LEISTE LA 2.d COMO SI FUERA
PARTE DE LA 2.a.

  DE REPORTE (acta 135, 4.1), Y ACUMULA. Tu reporte dice: "2.a
  (`SALIDA_V135_2A_DIAGNOSTICO.txt`): COBERTURA real de la 134 1 cotejadas /
  3 exentas / 4 cifras; dos SI tenian instrumento cerca, una NO". EL FICHERO
  QUE CITAS DICE LO CONTRARIO: UNA si y DOS no, y ademas empareja `118
  grafias` con `SALIDA_V134_4B_EFECTO_CAP.txt`, que es el fichero del vecino.
  Tu frase es CIERTA, la medi yo: con la ventana AMPLIA son 118 con `4A` y 54
  con `4B`. Pero esa medicion es la de tu guarda REPARADA, no la de tu 2.a,
  que corrio con la ventana forward-only porque era la unica que existia
  entonces. Publicaste el resultado de la vara nueva citando el fichero de la
  vara vieja. Esa es la caida, y de ahi sale el ramal (xx) de abajo. TENER
  RAZON NO ARREGLA LA CITA.

  DE INCUMPLIMIENTO DE ENCARGO (acta 135, 4.2). La 2.d ordenaba, literal,
  "esa linea SE PEGA EN EL REPORTE, tal cual", hablando de la COBERTURA DE TU
  PROPIO REPORTE. `grep -n COBERTURA docs/loop/REPORTE.md` da UNA sola linea
  y es la del diagnostico de la 134. La tuya, `COBERTURA: 7 cotejadas / 0
  exentas / 7 cifras`, vive en `SALIDA_V135_1J_CIFRAS_REPORTE.txt`, que el
  reporte ni siquiera cita. La 1.k preveia justo esto y mandaba PARAR antes
  que recortar; no paraste y no lo dijiste. TE ANOTO EL ATENUANTE Y NO ES
  MENOR: tu cobertura de verdad es 7 de 7 con CERO exentas, o sea que la
  puerta esta cerrada de hecho y lo unico que falta es la constancia.

DOS SON MIAS Y VAN CON NOMBRE (acta 135, 4.3 y 4.4): mi 1.l se contradecia
sola (prohibia borrar en ficheros viejos mientras mis TAREAS 2, 3.b y 4.c te
ordenaban borrar en tres scripts; elegiste bien, pero elegiste entre dos
ordenes mias), y mis MUTACIONES 1 y 2 de la 2.e no discriminaban nada, porque
tras tu reparacion el reporte de la 134 SIN MUTAR ya cae ROJO en esas dos
cifras. Te pedi dos pruebas que no podian fallar.

MIS DOS ADJUDICACIONES DE LA 135, QUE ESTA VUELTA SE REGISTRAN:

  (1) LA VENTANA AMPLIA DE TU 2.b QUEDA ADJUDICADA Y SE QUEDA COMO ESTA. No
  es doctrina nueva: la cubre el ramal (xix) por extension citable, que
  nombra "la ventana" sin fijarle forma, y va en la direccion segura, porque
  ensanchar solo puede encontrar MAS instrumentos, o sea hacer la exencion
  MAS dificil. El ramal (iii) prohibe ESTRECHAR una guarda en silencio; esto
  es lo contrario y ademas lo declaraste. Y LA ASIMETRIA QUE CONSERVASTE ES
  CORRECTA Y AHORA ES DOCTRINA: AMPLIA para decidir si la exencion es legal,
  FORWARD-ONLY para cotejar la cifra. Ensanchar el cotejo dejaria que una
  cifra cuadrara contra el fichero del vecino, que es exactamente el error
  que el forward comete al eximir. NO LA SIMPLIFIQUES NUNCA A UNA SOLA.

  (2) `OP-S-11` SE PUEDE EJECUTAR SIN DECIDIR NADA, Y NO LO SUPONGO: LO
  SIMULE ENTERA (`docs/loop/_auditor_v135_simulacion_ops11.txt`, en memoria,
  cero escritura). Las 129 grafias de primera posicion estan cubiertas al 100
  por ciento por las 129 filas de tu tabla; solo 8 nodos tienen 2 o mas
  declaraciones y las 7 grafias que viven fuera de la primera posicion estan
  TODAS en la tabla, CERO sin cubrir. La prueba de que la regla es la buena
  la da la propia operacion: `05_SANEO.md` documenta que
  `decision_de_vender_startup` declara el mismo libro dos veces, y ese es
  EXACTAMENTE el unico nodo que mi simulacion ve colapsar una declaracion.

EL TRAMO QUE SE RELEE AL DOBLE, POR DECIMOSEXTA VEZ. Siguen los ramales (i)
NINGUNA MEDICION SE ATRIBUYE A UN ESTADO QUE NO ES EL SUYO, (ii) EL
EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, (iii)
NINGUNA GUARDA SE ESTRECHA EN SILENCIO, (iv) TODA CIFRA SOBRE UN ARTEFACTO
CONTABLE SE LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO, (v) NINGUNA VARA
SE ESTRECHA EN EL ENCARGO, (vi) UN SUPERVIVIENTE SE RAZONA COMO SE RAZONA UNA
CLASE, (vii) UNA FUSION NO ACABA HASTA QUE LA ULTIMA ARISTA DEL ABSORBIDO
ESTA RECONSTRUIDA, (viii) UNA CIFRA DE PASIVO SE PARTE EN DOS ANTES DE
REMITIRLA, (ix) TODA CIFRA DE PASIVO O DE CENSO SE PUBLICA CON SU UNIDAD Y SU
ESTADO PEGADOS, (x) UN ORDEN DE MEDICION SE PRUEBA CORRIENDOLO ENTERO SOBRE
ARBOL LIMPIO ANTES DE MANDARLO, (xi) UNA NOMINA DE IDS SE RESUELVE ANTES DE
DECLARARLA COMPLETA, (xii) UNA ORDEN QUE VIVE AL FINAL DEL ENCARGO NO ES UNA
ORDEN DE TRAMO, (xiii) UNA REGLA MECANICA SE PRUEBA CONTRA EL CASO QUE LA
OPERACION YA DOCUMENTA ANTES DE MANDARLA, (xiv) UNA REGLA SE ENCARGA CON SU
EFECTO NOMBRADO, (xv) UNA FRASE DE CONTENCION ES UNA MEDICION, NO UN ALIVIO,
(xvi) UNA REGLA MECANICA SE ADJUDICA POR SU EFECTO SOBRE LA CANONICA, NO SOLO
POR CUANTOS GRUPOS COLAPSA, (xvii) UNA CIFRA CON UNIDAD AMBIGUA SE ARRASTRA
VUELTA A VUELTA, (xviii) UN PAR fichero:linea ES UNA MEDICION CON ESTADO, NO
UNA DIRECCION, y (xix) UNA EXENCION QUE ESCRIBE EL AUDITADO NO ES UNA
EXENCION, ES UN INTERRUPTOR. Le anado UNO, y sale de mi 4.1:
  (xx) UNA CONCLUSION SE LEE DEL INSTRUMENTO QUE SE CITA, NO DEL QUE SE
  CORRIO DESPUES. Cuando una vuelta mide lo mismo dos veces con dos varas (el
  diagnostico ANTES de reparar y la guarda DESPUES), la frase que cita el
  fichero del diagnostico dice lo que dice ESE fichero. Si lo que se quiere
  publicar es la medicion nueva, se cita el fichero nuevo. Tener razon no
  arregla la cita.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo; la
casa viene escribiendo las guardas delante porque son bloqueantes, y lo
mantengo. Esta vuelta hay TRES tareas.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES DE
  TOCAR NADA MAS. TODOS SUS INSTRUMENTOS EXISTEN Y ESTAN VERDES, LOS CORRI YO
  HOY, salvo la guarda NUEVA de la 3.d, que nace con la operacion.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V136_HEAD_APERTURA.txt. EL GEMELO DE CIERRE VA AL FINAL DE
  VERDAD, DESPUES DE LA ULTIMA OPERACION DE LA TAREA 3 Y ANTES DE ESCRIBIR EL
  REPORTE: docs/loop/SALIDA_V136_HEAD_CIERRE.txt.
  Comprobacion: python scripts/loop/verificar_apertura_sellada.py --vuelta
  136 tiene que dar VERDE EXIT 0, y su salida se cita en el reporte. La linea
  de identidad del reporte mantiene los TRES rotulos y NINGUNO SE TECLEA: los
  tres salen de tallar_identidad_reporte.py.
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT Y NO SE
  PUSHEA SOLO (regla compuesta del acta 128, 3.4). El push por tramo empieza
  DESPUES de ese bloque. Es la UNICA excepcion a la linea de commit y push de
  cada tarea.
  (1.b) EL ORDEN DE CAPTURA, EL QUE FUNCIONO DE LA 128 A LA 135, Y NO SE
  TOCA. REGLA UNICA: `python scripts/run_phase1.py --reaplico-curaduria` NO
  SE CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0 compara el snapshot de ANTES
  del paso 6 y sale verde sobre un estado que el mismo acaba de desalinear;
  el motor si lo ve.
  POR CADA LADO (APERTURA y CIERRE) SE HACE ESTO Y EN ESTE ORDEN, UNA SOLA
  VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V136_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V136_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V136_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO. Salida a
       docs/loop/SALIDA_V136_CICLO_NUMSTAT_<LADO>.txt con su EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  AVISO QUE ESTA VUELTA IMPORTA Y LAS ANTERIORES NO, PORQUE HAY REGIMEN B: EL
  NUMSTAT DEL PASO 4 SOLO PUEDE SALIR VACIO SOBRE ARBOL YA COMMITEADO. En el
  lado CIERRE, eso significa que el ciclo se corre DESPUES de commitear la
  escritura de `OP-S-11` (dataset mas web), no antes. Si lo corres con la
  escritura sin commitear te saldra un numstat lleno que NO es un fallo: es
  tu propio trabajo sin guardar. El orden esta escrito en la 3.c y se sigue
  al pie.
  Si el numstat no cierra sobre arbol commiteado, NO MIDAS: repite el ciclo,
  dilo en el reporte, y si a la segunda tampoco cierra PARAS y lo traes
  escrito.
  (1.c) LOS NOMBRES CANONICOS, con <LADO> = APERTURA o CIERRE, estos siete:
    docs/loop/SALIDA_V136_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V136_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V136_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V136_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V136_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V136_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V136_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  EL FORMATO: el tsc cierra con EXIT=<n> sin dos puntos y sin espacio; las
  OTRAS SEIS canonicas cierran con la linea literal EXITCODE: <n>; y las TRES
  del ciclo de 1.b LLEVAN TAMBIEN SU LINEA EXITCODE: <n>, EN LOS DOS LADOS,
  PUESTA EN LA MISMA CORRIDA QUE LAS GENERA Y NO DESPUES. Sigue prohibido el
  fichero de cero bytes. EL EXITCODE SE LEE DEL INSTRUMENTO, NUNCA DE UN `$?`
  PUESTO DETRAS DE UNA TUBERIA.
  MI CONTRASTE, MEDIDO HOY POR MI Y NO PARA COPIAR: marcador A 551 / B 72 /
  C 5 / D 2.760, huecos [], dups 0; conteo 3.853 / 3.184 / 669, sig 9.198,
  prev 9.180, suma 18.378, union 9.833, auto 0, dups 0; motor 25/25; web 80
  passed (80) y 1.030 passed 3 skipped (1.033); tsc EXIT 0 cero lineas;
  desfase 3 filas. SI TU MEDICION TE DA OTRA COSA, MANDA LA TUYA Y DECLARAS
  LA DISCREPANCIA.
  Y LA PREDICCION QUE ESTA VUELTA ES UNA GUARDA, PORQUE `fuente` ES UN CAMPO
  DE TEXTO Y NO UNA ARISTA: DESPUES DE `OP-S-11`, LAS SIETE CANONICAS DEL
  LADO CIERRE TIENEN QUE DAR LO MISMO QUE LAS DE APERTURA, AL DIGITO. Censo
  3.853 / 3.184 / 669, aristas 9.198 / 9.180 / 18.378 / 9.833, auto 0, dups
  0, marcador identico, desfase 3 filas. SI EL CONTEO MUEVE UNA SOLA ARISTA,
  O EL CENSO UN SOLO NODO, O EL MARCADOR UN SOLO PUESTO, ES ROJO Y PARAS: la
  operacion habria tocado algo que no es suyo.
  >>> COMMIT DEL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) EN UN SOLO COMMIT,
  >>> SIN PUSH.
  (1.d) LA BATERIA POR OPERACION, Y ESTA VUELTA SI HAY REGIMEN B. Reusa
  scripts/loop/vuelta135_baterias_cmp.py adaptado a V136 (mismo filecmp de
  bytes, shallow=False, no lo aflojes). Los lados son DOS, APERTURA y CIERRE,
  y el cmp se corre entre esos dos. Salida literal a
  docs/loop/SALIDA_V136_BATERIAS_CMP.txt, una linea por par, IDENTICOS o
  DISTINTOS, mas la linea RESUMEN por familia. SI UNA FAMILIA TIENE UN SOLO
  IDENTICO O UN SOLO DISTINTO, SE NOMBRA ESE PAR EXACTO, LEIDO DEL FICHERO, Y
  SE EXPLICA POR QUE ESE Y NO OTRO.
  SE ESPERA que MOTOR y WEB salgan DISTINTOS por duraciones y por Start at, Y
  ESO SE PRUEBA PEGANDO EL DIFF ENTERO: corre `diff` entre los dos MOTOR y
  entre los dos WEB y escribe las salidas a
  docs/loop/SALIDA_V136_1D_DIFF_MOTOR.txt y _WEB.txt, cada una con su
  EXITCODE. SI EL DIFF TRAE UNA SOLA LINEA QUE NO SEA UNA DURACION O UN
  "Start at", ES ROJO Y PARAS.
  Y SE ESPERA, POR LA PREDICCION DE 1.c, QUE GATE0, CONTEO, MARCADOR y
  DESFASE SALGAN **IDENTICOS** PESE AL REGIMEN B. Si alguno sale DISTINTO,
  ES ROJO Y PARAS: lo traes escrito con el diff pegado, no lo explicas.
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
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados.
  (1.g) LAS TRES GUARDAS DE ARISTAS SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py con su --autoprueba, verificar_aristas_vivas.py
  con su --autoprueba, y verificar_huerfanas_por_fusion.py con su
  --autoprueba (el argumento es --autoprueba, no --caso-positivo).
  verificar_aristas_vivas.py --antes <HEAD sellado de apertura> --despues
  WORK tiene que dar PERDIDAS 0 y NUEVAS 0. ESTA VUELTA ESA GUARDA ES LA QUE
  DEMUESTRA QUE `OP-S-11` NO TOCO EL GRAFO, ASI QUE SE CORRE DESPUES DE LA
  ESCRITURA Y NO ANTES. MI CONTRASTE, MEDIDO HOY: aristas vivas 7.296 contra
  7.296, PERDIDAS 0 NUEVAS 0; huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1
  FABRICADAS 0.
  (1.h) LA GUARDA DEL SELLO DE CIERRE, AL FINAL Y NO ANTES:
  `python scripts/loop/verificar_cierre_sellado.py --vuelta 136` VERDE EXIT 0
  una vez escrito tu SALIDA_V136_HEAD_CIERRE.txt, y su salida se pega. Corre
  tambien `python scripts/loop/vuelta129_tarea1h_casos_positivos.py` y pega
  su VERDE GENERAL. NO renombres ese script por llevar 129 en el nombre. Sus
  hashes sinteticos CAMBIAN EN CADA CORRIDA; si eso te obliga a reescribir
  una salida ya commiteada, EL MENSAJE DEL COMMIT LO DICE con la palabra
  "regenerada" y el motivo.
  (1.i) LA GUARDA DE CITAS SOBRE TU PROPIO REPORTE, VERDE. Si te da ROJO
  nombrando un fichero tuyo, arreglas EL FICHERO pegandole la medicion que le
  falta, no la cita del reporte.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS COMPROBACIONES, QUE ESTA VUELTA SON
  NUEVE, y las nueve salidas se pegan CITADAS POR SU PROPIO NOMBRE DE
  FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 136 --comparar docs/loop/REPORTE.md
    python scripts/loop/tallar_identidad_reporte.py --vuelta 136 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 136
    python scripts/loop/verificar_cifras_del_reporte.py
    python scripts/loop/verificar_cabecera_mapeo.py
    python scripts/loop/verificar_fuente_canonico.py            (LA NUEVA de la 3.d)
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR, la segunda IDENTIDAD
  IDENTICA AL TALLADOR, y las otras SIETE VERDE EXIT 0.
  (1.k) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte, con su
  salida. Y ESTA VUELTA, POR MI 4.2 DE LA 135: LA LINEA LITERAL
  `COBERTURA: <cotejadas> cotejadas / <exentas> exentas / <total> cifras` DE
  TU PROPIO REPORTE SE PEGA EN EL REPORTE, TAL CUAL, CITANDO
  `SALIDA_V136_1J_CIFRAS_REPORTE.txt`. NO ES OPCIONAL Y NO ES LA DE NINGUNA
  VUELTA ANTERIOR: ES LA TUYA. Si por pegarla no cabes en 80 lineas, NO
  RECORTAS LA COBERTURA NI TE INVENTAS UN TOPE NUEVO: PARAS Y LO TRAES
  ESCRITO. El tope de 80 es decision del fundador (27 ago 2026) y no lo
  cambio yo.
  (1.l) LOS DOS REGIMENES DE ESCRITURA. LEE ESTO ENTERO, PORQUE LA CLAUSULA
  DE LA 135 SE CONTRADECIA SOLA Y ES CAIDA MIA (acta 135, 4.3):
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o a
      docs/ se mide con git diff --numstat y con grep -c "^-[^-]" sobre el
      diff EN CERO, mas git diff --word-diff=porcelain pegado si toca una
      linea vieja. NO necesita las tres guardas. Cuando anades texto AL FINAL
      de una linea vieja, el numstat marca 1 borrada aunque no se borre nada;
      la vara que manda ahi es el word-diff porcelain, y las lineas `^-` que
      cuentan son las de PALABRA borrada, NO la cabecera `--- a/...`.
    - FICHEROS VIEJOS QUE PUEDEN CAMBIAR DE CONTENIDO ESTA VUELTA, Y SON
      EXACTAMENTE ESTOS TRES, NINGUNO MAS:
        docs/plan/OPERACIONES.jsonl        (el estado de `OP-S-11`, tarea 3.e)
        dataset/nodos/*.json               (la escritura de `OP-S-11`, REGIMEN B)
        web/ y engine/ derivados           (lo que produzcan etiquetas y sync)
      LA CLAUSULA NO ALCANZA A LOS SCRIPTS QUE ESTE ENCARGO TE MANDA ESCRIBIR
      O EXTENDER: un script que yo te ordeno tocar se toca, y eso no es un
      borrado clandestino. Si te descubres borrando en un fichero viejo que
      NO esta en esa lista y que NINGUNA tarea de este encargo nombra, PARAS.
    - REGIMEN B, DATO: ESTA VUELTA SI SE USA, y es la primera en muchas. Se
      escribe el campo `fuente` de nodos vivos y NADA MAS. NO se toca un solo
      `nodos_siguientes`, `nodos_previos`, `titulo`, `deprecado` ni
      `etiqueta_arbol`. Cada escritura va con su simulacion previa sobre
      copia en memoria (3.b), su caso positivo (3.d) y el ciclo de Gate 0
      detras (1.b lado CIERRE).
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE.
  >>> COMMIT Y PUSH de 1.e, 1.f y 1.l en cuanto esas guardas esten corridas y
  >>> pegadas. 1.d, 1.g, 1.h, 1.i, 1.j y 1.k NECESITAN el lado de cierre y
  >>> van al final, en el commit del reporte.

- TAREA 2, LOS REGISTROS. Son CUATRO, las cuatro REGIMEN A puro, aditivas,
  sin borrar una sola linea, y las cuatro van ANTES de tocar un nodo.
  (2.a) LA CORRECCION DECLARADA DE MI 4.1, y va en el registro y no solo en
  el reporte. En docs/PENDIENTES.md, seccion nueva R.17, escribes la caida
  con su medicion: la frase literal de tu reporte de la 135, lo que dice de
  verdad `SALIDA_V135_2A_DIAGNOSTICO.txt` (las tres exentas una por una, con
  su SI o su NO y con el fichero cuando lo haya), la razon (2.a corrio con la
  ventana forward-only, que era la unica que existia), y la medicion CORRECTA
  con la ventana amplia: `118 grafias` con `SALIDA_V134_4A_CENSO_COLA.txt` y
  `54 grupos` con `SALIDA_V134_4B_EFECTO_CAP.txt`, y `0 pares` sin ninguno.
  Y EL RAMAL (xx) ENTERO.
  (2.b) LA CONSTANCIA DE MI 4.2, en la misma R.17: que la 2.d ordenaba pegar
  la linea COBERTURA de tu propio reporte, que no se pego, que la 1.k mandaba
  parar antes que recortar, y que tu cobertura real de la 135 era
  `COBERTURA: 7 cotejadas / 0 exentas / 7 cifras`, leida de
  `SALIDA_V135_1J_CIFRAS_REPORTE.txt`.
  (2.c) LA ASIMETRIA DE LAS DOS VENTANAS SE ESCRIBE DONDE VIVE LA GUARDA, por
  adicion, en el docstring de scripts/loop/verificar_cifras_del_reporte.py:
  AMPLIA (mas menos 2 frases, bidireccional) para decidir si la exencion
  (iii) es LEGAL; FORWARD-ONLY para COTEJAR la cifra contra su fichero; y por
  que NO se unifican (ensanchar el cotejo dejaria que una cifra cuadrara
  contra el fichero del vecino, y ese es exactamente el error que el forward
  comete al eximir). Citas mi acta 135, 3.1. Su word-diff va pegado y el grep
  de lineas de palabra borrada tiene que dar CERO.
  (2.d) EL CIERRE CON REMISION SE REGISTRA ANTES DE QUE HAGA FALTA, en la
  misma R.17: que la parada del fundador de la fase 05 (26 ago 2026) y la
  atadura 2 de docs/plan/00_INDICE.md:458 (`OP-S-12` va AL FINAL, despues de
  la ultima fusion) se muerden la cola leidas al pie de la letra, y que lo
  resuelve la figura de CERRADA CON REMISION que el fundador ya uso en la
  fase 03 (docs/loop/paradas/2026-08-26-cierre-fase-03-DECISION.md). TU NO
  DECLARAS CERRADA LA FASE 05 NI HOY NI NUNCA: eso lo declaro yo en mi acta.
  Tu solo dejas el registro escrito.
  >>> COMMIT Y PUSH de la TAREA 2 entera en cuanto este escrita.

- TAREA 3, EL TRABAJO: SE EJECUTA `OP-S-11`. REGIMEN B. ES LA OPERACION, NO
  LA TABLA. Va en este orden y no en otro.
  (3.a) LEE LA OPERACION ENTERA ANTES DE TOCAR NADA: docs/plan/05_SANEO.md a
  partir de la linea 586, y la tabla docs/plan/OP_S_11_MAPEO_PROPUESTO.md
  entera. LA TABLA ES LA FUENTE DEL MAPEO Y NO SE REHACE ESTA VUELTA: quedo
  adjudicada y verificada en la 135 y su guarda `verificar_cabecera_mapeo.py`
  esta verde. Si al leerla encuentras una fila que no puedas aplicar sin
  decidir, PARAS Y LA TRAES NOMBRADA.
  (3.b) LA SIMULACION PREVIA, SOBRE COPIA EN MEMORIA, ANTES DE ESCRIBIR UN
  SOLO BYTE. Escribe scripts/loop/vuelta136_simular_ops11.py, que lee el
  grafo y la tabla y publica, con sus lineas `CIFRA <etiqueta>: <n>
  <unidad>`: nodos vivos con `fuente`; grafias distintas en primera posicion;
  grafias distintas en posicion NO primera; cuantas de esas NO estan en la
  tabla; nodos cuyo campo CAMBIA; nodos cuyo campo NO cambia; grafias
  distintas en cualquier posicion DESPUES; y LAS PERDIDAS REPARTIDAS. Salida
  a docs/loop/SALIDA_V136_3B_SIMULACION.txt.
  LA REGLA DE APLICACION, ESCRITA PARA QUE NO DECIDAS TU: el campo `fuente`
  se parte por ` | `, CADA declaracion se sustituye por su canonica de la
  tabla, y el resultado se vuelve a unir por ` | ` QUITANDO las repetidas que
  la normalizacion produzca, CONSERVANDO EL ORDEN de la primera aparicion. Se
  aplica a TODAS las posiciones, no solo a la primera, y la razon esta
  medida: las 7 grafias que viven fuera de la primera posicion estan todas en
  la tabla.
  LAS PERDIDAS REPARTIDAS: ningun nodo muere y ninguna arista se mueve, asi
  que la tabla de seis motivos no aplica aqui y lo dices asi. La UNICA
  perdida es de DECLARACION REPETIDA dentro del propio campo, y se nombra
  nodo por nodo.
  MI CONTRASTE, MEDIDO HOY POR MI Y NO PARA COPIAR
  (`docs/loop/_auditor_v135_simulacion_ops11.txt`): 3.184 nodos vivos con
  `fuente`; 129 grafias en primera posicion, cubiertas al 100 por ciento por
  las 129 filas de la tabla; 7 grafias en posicion no primera, 0 sin cubrir;
  reparto de declaraciones 3.176 nodos con una, 6 con dos y 2 con tres; 726
  nodos CAMBIAN y 2.458 NO; 54 grafias distintas en cualquier posicion
  despues; y UNA sola perdida de declaracion repetida, en
  `decision_de_vender_startup`, que es justo el nodo que `05_SANEO.md` ya
  documenta. SI TU MEDICION TE DA OTRA COSA, MANDA LA TUYA Y DECLARAS LA
  DISCREPANCIA, Y SI LA DIFERENCIA ES EN "grafias sin cubrir", PARAS.
  (3.c) LA ESCRITURA, Y SU ORDEN EXACTO. Escribe
  scripts/loop/vuelta136_aplicar_ops11.py, que REUSA el modulo de 3.b (lo
  importa, no reimplementa el mapeo) y escribe el campo `fuente` en los
  ficheros de dataset/nodos/. Orden:
    1) corres 3.b otra vez y pegas su salida (la simulacion manda),
    2) escribes,
    3) `python scripts/run_phase1.py --reaplico-curaduria`,
    4) `python scripts/etiquetas_de_cara.py --aplicar`,
    5) `python scripts/sync_assets_web.py`,
    6) COMMIT de la escritura (dataset mas web mas los dos scripts), y SOLO
       DESPUES el ciclo del lado CIERRE de 1.b, que es el que tiene que dar
       numstat VACIO.
  SI GATE 0 CAE EN ROJO EN EL PASO 3, PARAS Y LO TRAES: no lo remiendas.
  (3.d) EL CASO POSITIVO, Y ES EL CRITERIO DE HECHO DE LA FASE 08, NO UN
  ADORNO. `docs/plan/08_VERIFICACION.md:9` dice: "UNA FASE ESTA HECHA CUANDO
  SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA", y trae la comprobacion
  barata: "correr la prueba ANTES del arreglo. Si pasa, no prueba nada".
  Escribe scripts/loop/verificar_fuente_canonico.py: recorre los nodos vivos,
  parte `fuente` por ` | `, y cae ROJO EXIT 1 nombrando el nodo y la grafia
  si ALGUNA declaracion no esta en el conjunto de canonicas de la tabla.
  SUS DOS PRUEBAS, LAS DOS OBLIGATORIAS Y LAS DOS PEGADAS:
    - LA DE ANTES: la corres contra el estado PREVIO a la escritura (el HEAD
      sellado de apertura vale) y TIENE QUE CAER ROJO. Si pasa verde ahi, no
      prueba nada y PARAS. Salida a docs/loop/SALIDA_V136_3D_ANTES.txt.
    - LA DE MUTACION: sobre una COPIA en memoria del grafo ya escrito, le
      devuelves a UN nodo su grafia vieja no canonica y compruebas que cae
      ROJO nombrandolo. Salida a docs/loop/SALIDA_V136_3D_MUTACION.txt.
  Y contra el arbol real, despues de la escritura, VERDE EXIT 0. Se cablea en
  1.j como novena comprobacion.
  (3.e) EL ESTADO DE LA OPERACION. `OP-S-11` pasa de `LISTA` a `HECHA` en
  docs/plan/OPERACIONES.jsonl, con su campo de evidencia apuntando a
  `SALIDA_V136_3B_SIMULACION.txt`, `SALIDA_V136_3D_ANTES.txt` y
  `SALIDA_V136_3D_MUTACION.txt`. NADA MAS de ese fichero se toca: el conteo
  tiene que quedar en 61 LISTA y 10 HECHA, y esa cifra se publica con su
  comando. NINGUNA OTRA operacion cambia de estado.
  (3.f) LO QUE SE DECLARA Y LO QUE NO SE TOCA, DICHO SIN CONDICIONALES:
    - EL REBASE SE DECLARA OTRA VEZ, ahora con el campo ya escrito: el
      catalogo queda en 54 grafias canonicas y la meta de `05_SANEO.md` es
      55, o sea rebasada por UNO. `05_SANEO.md` NO SE TOCA: esa meta es del
      fundador, es una medicion del 11 ago 2026, y la regla de verificacion
      de AUDITOR.md manda declarar la discrepancia y no copiar la vieja.
    - `OP-S-12` NO SE ABRE Y NO SE TOCA: va al final de la pasada entera por
      la atadura 2 de docs/plan/00_INDICE.md:458.
    - LA FASE 05 NO SE DECLARA CERRADA POR NADIE, Y NO TIENES QUE JUZGAR SI
      LO ESTA: cuando lo este lo declaro yo en mi acta 136.
    - La fase 00_CODIGO tampoco: `OP-C-01` a `OP-C-05`, `OP-S-06` y `OP-S-07`
      figuran LISTA y ESO YA ESTA ADJUDICADO (acta 25 y acta 119). Si
      tropiezas con esos estados, no abras nada.
  >>> COMMIT Y PUSH detras de 3.b, otro detras de 3.c mas 3.d, y otro detras
  >>> de 3.e.
  >>> El commit y push del REPORTE va al final, despues del sello de cierre
  >>> de 1.a, del lado de CIERRE de 1.b y 1.c, de la bateria de 1.d, de las
  >>> guardas de 1.g, 1.h e 1.i, de las NUEVE comprobaciones de 1.j y de la
  >>> medida de 1.k. Ese es el ultimo commit de la vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
