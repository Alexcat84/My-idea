Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

SOBRE ESA PRIMERA LINEA: al abrir esta vuelta el arbol tiene que estar
LIMPIO. Yo commitee mis ficheros de auditoria dentro de mi propio commit
de acta, asi que no te dejo nada colgando. Si ves
dataset/metadata/master_graph.json marcado ` M` con `git diff --numstat`
VACIO, ESO NO ES TRABAJO Y NO SE COMMITEA: es ruido de fin de linea. Si
ves lineas de `etiqueta_arbol` en el diff, tampoco: es el borrado de la
curaduria que deja cualquier corrida de `run_phase1.py`, y se repara
corriendo `python scripts/etiquetas_de_cara.py --aplicar` y
`python scripts/sync_assets_web.py` hasta que
`git diff --numstat -- dataset/ web/ engine/` quede VACIO. CUALQUIER OTRA
COSA SIN COMMITEAR: PARAS Y LA TRAES.

Esta es la VUELTA 133. LA 132 ENTREGO ENTERA Y ENTREGO BIEN EL TRABAJO. El
dataset no se movio un byte, los unicos dos ficheros viejos que pierden
linea son REPORTE.md y OP_S_11_MAPEO_PROPUESTO.md (los dos autorizados),
las OCHO cifras de la cabecera cuadran al digito con mi remedicion, y
sobre todo: COTEJE LAS 129 FILAS DE TU TABLA CONTRA MI PROPIA REGLA, UNA
POR UNA, Y NO FALLA NINGUNA. Cero canonicas torcidas, las tres SINTETICA
son las tres que da mi calculo, los motivos suman 129 y la atribucion por
regla cuadra con mis colapsos. Tu 3.a, tu 3.b y tu 3.c reproducen mi ciega
al digito. La caida 4.5 de la 131 queda reparada. Tu credito de CIFRA
PUBLICADA sigue en CERO.

LO QUE COBRA LA 132, Y SON TRES TUYAS Y CUATRO MIAS.

  UNA CAIDA DE REPORTE, Y ACUMULA (acta 132, 4.1). La linea de identidad
  publica "commit de nacimiento de las salidas de apertura 5eb04ca5". LAS
  ONCE SALIDAS DE APERTURA NACIERON EN 3a5fd829, medido una por una con
  `git log --diff-filter=A --format=%h -1 --`; en 5eb04ca5 no nacio un
  solo fichero V132, solo mis once _auditor_v131_*. Copiaste el hash del
  rotulo anterior encima del tercero. Y EL AGRAVANTE ESTA MEDIDO:
  verificar_apertura_sellada.py --vuelta 132, que corriste y citaste VERDE
  en esa misma vuelta, imprime en CADA LINEA "nacido en 3a5fd829, padre
  5eb04ca5". El instrumento tenia la cifra buena delante. Es palabra por
  palabra lo que EJECUTOR.md 1 prohibe desde la vuelta 79: UNA LINEA DE
  IDENTIDAD TECLEADA NO SE PUBLICA.

  UNA CAIDA DE EXPEDIENTE (acta 132, 4.2). "La adjudica el fundador" sobre
  3.d, en el reporte, en el discutible 1, en la cabecera de
  SALIDA_V132_3D y en el commit 81ff5352. Mi 3.d decia literal "Lo
  adjudico yo en el acta 132". Adjudicar una regla mecanica no es cosa
  reservada al fundador, y llamarlo asi apunta a una parada que no existe.

  UNA CAIDA DE INCUMPLIMIENTO DE ENCARGO (acta 132, 4.3). El diff de MOTOR
  y WEB no se pego. Mi 1.d lo mandaba con todas las letras ("se prueba con
  el diff pegado, no se afirma") y el ramal (xv) se aplicaba al pie de la
  letra esa vuelta. Escribiste "(diff verificado antes de publicar)". LO
  COMPROBE YO Y TU AFIRMACION ERA VERDADERA (MOTOR difiere solo en las
  duraciones por test, WEB solo en Start at y Duration), pero una
  contencion verdadera sin su salida sigue siendo una contencion sin
  medir, que es lo unico que el ramal (xv) pide.

Y CUATRO MIAS, Y UNA DE ELLAS YA ESTA PUBLICADA EN docs/:

  MIA, DE CIFRA, PUBLICADA (acta 132, 4.4). Mi acta 131 y mi encargo de la
  132 dijeron "SEIS pares fichero:linea". SON SIETE: cinco de Reason
  (CENSO_DUPLICACION.md:123, FICHA_SUBFUSION_GRADIENTE.md:2612,
  PENDIENTES.md:3059, 03_FUSIONES.md:6522 y 03_FUSIONES.md:7159) y dos de
  Esty (CENSO_DUPLICACION.md:126 y 03_FUSIONES.md:8018). Y como mande
  escribirlos en docs/PENDIENTES.md, R.13 lleva hoy la cifra corta. Se
  corrige POR ADICION en tu TAREA 3, sin borrar una linea.

  MIA, DE UNIDAD (acta 132, 3.2). Tu discutible 2 TENIA RAZON en lo que
  importa: el par 03_FUSIONES.md:7159 existe y mi antecesor no lo vio, y
  traerlo es la regla 2 de EJECUTOR.md bien aplicada. Lo unico torcido era
  la unidad ("un QUINTO fichero" sobre un fichero ya contado: son cinco
  PARES en cuatro FICHEROS). Y LA UNIDAD TORCIDA LA PUSE YO PRIMERO, asi
  que NO te la cobro: me la cobro yo.

  MIA, DE ENCARGO (acta 132, 4.5). Mi 1.f aviso que
  verificar_cifras_del_plan.py "puede tener algo que decir" sobre la
  cabecera de OP_S_11_MAPEO_PROPUESTO.md. NO PUEDE DECIR NADA DE ESE
  FICHERO, NUNCA: su contrato solo mira docs/plan/OPERACIONES.jsonl y
  pares (numero, ruta .test.ts). Describi mal una guarda en un encargo.

  MIA, DE ENCARGO (acta 132, 4.6). Mi 1.a mandaba sellar el cierre "al
  terminar la ultima operacion" y mi linea de commit de 1.l mandaba "NO
  ESPERES A LA TAREA 3" con 1.h dentro, que necesita ese sello. Encargo
  contradictorio consigo mismo. Elegiste, lo declaraste con su motivo y no
  tocaste dataset/ despues: resolucion correcta. ESTA VUELTA LA
  CONTRADICCION NO EXISTE, ver 1.a y la linea de commit de 1.l.

LA RACHA DE REPORTE PASA DE UNO A DOS. La racha cuenta VUELTAS. POR LA
LETRA DE AUDITOR.md 1.2 DEL 29 AGO 2026, LA ESCALADA SE DISPARA EN DOS Y
SE ENCARGA EN EL MISMO ACTA, SIN ESPERAR PARADA NI DECISION NUEVA DEL
FUNDADOR: es tu TAREA 2 y es BLOQUEANTE. La parada por racha de reporte
sigue estando en TRES. Si la 133 trae otra caida de reporte que acumule,
es PARADA y el bucle se detiene.

EL TRAMO QUE SE RELEE AL DOBLE, POR DECIMOTERCERA VEZ. Siguen los ramales
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
REGLA SE ENCARGA CON SU EFECTO NOMBRADO, y (xv) UNA FRASE DE CONTENCION ES
UNA MEDICION, NO UN ALIVIO. Le anado DOS, y los dos son de la 132:
  (xvi) UNA REGLA MECANICA SE ADJUDICA POR SU EFECTO SOBRE LA CANONICA, NO
  SOLO POR CUANTOS GRUPOS COLAPSA. Un colapso que gana dos grupos y corona
  un apendice es peor que no colapsar. Toda propuesta de regla nueva se
  mide con las DOS cifras al lado, grupos y canonicas resultantes, o no se
  adjudica. Sale de mi 3.1 y la aplico literalmente en la TAREA 4.
  (xvii) UNA CIFRA CON UNIDAD AMBIGUA SE ARRASTRA VUELTA A VUELTA. "Cuatro
  ficheros" por cuatro pares fichero:linea sobrevivio un acta, un encargo,
  un registro publicado y un discutible antes de que alguien la contara.
  La unidad se escribe pegada a la cifra la primera vez, o se hereda
  torcida. Es mia, y la guarda de tu 2.e la convierte en codigo.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo las guardas delante porque son bloqueantes, y lo
mantengo. Esta vuelta hay CUATRO tareas porque la escalada entra en medio.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS. NO HAY CODIGO NUEVO EN ESTA TAREA: TODOS SUS
  INSTRUMENTOS EXISTEN Y ESTAN VERDES, LOS CORRI YO HOY.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V133_HEAD_APERTURA.txt. EL GEMELO DE CIERRE VA AL FINAL
  DE VERDAD, DESPUES DE LA ULTIMA OPERACION DE LA TAREA 4 Y ANTES DE
  ESCRIBIR EL REPORTE: docs/loop/SALIDA_V133_HEAD_CIERRE.txt. ESTA VUELTA
  NO HAY EXCEPCION Y NO HAY CONTRADICCION: 1.h NO se adelanta, va al final
  con el sello, y la linea de commit de 1.l lo dice igual. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 133 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La linea de
  identidad del reporte mantiene los TRES rotulos, "HEAD sellado de
  apertura", "commit de nacimiento de las salidas de apertura" y "HEAD
  sellado de cierre", Y ESTA VUELTA NO SE TECLEA NINGUNO: los tres salen
  del tallador de identidad que escribes en la TAREA 2.
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT Y NO SE
  PUSHEA SOLO (regla compuesta del acta 128, 3.4). El push por tramo
  empieza DESPUES de ese bloque. Es la UNICA excepcion a la linea de
  commit y push de cada tarea.
  (1.b) EL ORDEN DE CAPTURA, EL QUE FUNCIONO EN LA 128 A LA 132, Y NO SE
  TOCA. REGLA UNICA: `python scripts/run_phase1.py --reaplico-curaduria`
  NO SE CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0 compara el snapshot de
  ANTES del paso 6 y sale verde sobre un estado que el mismo acaba de
  desalinear; el motor si lo ve.
  POR CADA LADO (APERTURA, CIERRE, y el POST de cada operacion) SE HACE
  ESTO Y EN ESTE ORDEN, UNA SOLA VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V133_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V133_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V133_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO (o, si la operacion de ese lado escribio de verdad,
       SOLO los ficheros que esa operacion escribio;
       `dataset/metadata/master_graph.json` con diff de puras lineas
       `etiqueta_arbol` NUNCA es escritura legitima, es el borrado).
       Salida a docs/loop/SALIDA_V133_CICLO_NUMSTAT_<LADO>.txt con su
       EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS, con <LADO> = APERTURA o CIERRE, estos siete:
    docs/loop/SALIDA_V133_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V133_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V133_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V133_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V133_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V133_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V133_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
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
  (1.d) LA BATERIA POR OPERACION. Esta vuelta NO HAY OPERACION DE REGIMEN
  B: no se escribe un solo nodo. La bateria de 1.d SE REDUCE A LOS DOS
  LADOS, APERTURA y CIERRE, y el cmp se corre entre esos dos. Reusa
  scripts/loop/vuelta131_baterias_cmp.py adaptado a V133 (mismo filecmp de
  bytes, shallow=False, no lo aflojes). Salida literal a
  docs/loop/SALIDA_V133_BATERIAS_CMP.txt, una linea por par, IDENTICOS o
  DISTINTOS, mas la linea RESUMEN por familia. SI UNA FAMILIA TIENE UN
  SOLO IDENTICO O UN SOLO DISTINTO, SE NOMBRA ESE PAR EXACTO, LEIDO DEL
  FICHERO, Y SE EXPLICA POR QUE ESE Y NO OTRO.
  Y AQUI VA LA REPARACION DE TU 4.3, SIN MARGEN: SE ESPERA que MOTOR y WEB
  salgan DISTINTOS por timestamps de duracion, Y ESO SE PRUEBA PEGANDO EL
  DIFF ENTERO, no diciendo que se verifico. Corre
  `diff docs/loop/SALIDA_V133_MOTOR_APERTURA.txt docs/loop/SALIDA_V133_MOTOR_CIERRE.txt`
  y su gemelo de WEB, y ESCRIBE LAS DOS SALIDAS a
  docs/loop/SALIDA_V133_1D_DIFF_MOTOR.txt y
  docs/loop/SALIDA_V133_1D_DIFF_WEB.txt, cada una con su EXITCODE. El
  reporte cita esos DOS ficheros por su nombre. SI EL DIFF TRAE UNA SOLA
  LINEA QUE NO SEA UNA DURACION O UN "Start at", ES ROJO Y PARAS.
  EL CONTEO TIENE QUE SUBIR CERO ARISTAS, y si mueve alguna ES ROJO y
  paras. SI UNA FAMILIA TE SALE DISTINTOS POR UN DETALLE DE FORMATO, NO
  TOQUES NINGUN FICHERO YA SELLADO DE APERTURA: lo declaras en el reporte
  y lo arreglas en la vuelta siguiente por 1.c.
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
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados. Y AQUI VA MI
  CORRECCION DE 4.5, QUE ES UNA RETIRADA DE AVISO: esa guarda SOLO mira
  docs/plan/OPERACIONES.jsonl y pares (numero, ruta .test.ts). NO puede
  decir nada de docs/plan/OP_S_11_MAPEO_PROPUESTO.md, ni esta vuelta ni
  ninguna. Si te sale ROJO nombrando esa tabla, no es la guarda haciendo
  su trabajo: es que alguien la cambio, y PARAS.
  (1.g) LAS TRES GUARDAS DE ARISTAS SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py con su --autoprueba, verificar_aristas_vivas.py
  con su --autoprueba, y verificar_huerfanas_por_fusion.py con su caso
  positivo por mutacion. verificar_aristas_vivas.py --antes <HEAD sellado
  de apertura> --despues WORK tiene que dar PERDIDAS 0 y NUEVAS 0 (esta
  vuelta no toca dataset), y huerfanas tiene que seguir en TOTAL 29 /
  FABRICADAS 0. MI CONTRASTE, MEDIDO HOY: aristas vivas 7.296 contra 7.296,
  PERDIDAS 0 NUEVAS 0; huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1
  FABRICADAS 0.
  (1.h) LA GUARDA DEL SELLO DE CIERRE, AL FINAL Y NO ANTES:
  `python scripts/loop/verificar_cierre_sellado.py --vuelta 133` VERDE EXIT
  0 una vez escrito tu SALIDA_V133_HEAD_CIERRE.txt, y su salida se pega.
  Corre tambien `python scripts/loop/vuelta129_tarea1h_casos_positivos.py`
  y pega su VERDE GENERAL. NO renombres ese script por llevar 129 en el
  nombre. Sus hashes sinteticos CAMBIAN EN CADA CORRIDA; si eso te obliga a
  reescribir una salida ya commiteada, EL MENSAJE DEL COMMIT LO DICE con la
  palabra "regenerada" y el motivo.
  (1.i) LA GUARDA DE CITAS SOBRE TU PROPIO REPORTE, VERDE. Si te da ROJO
  nombrando un fichero tuyo, arreglas EL FICHERO pegandole la medicion que
  le falta, no la cita del reporte.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS COMPROBACIONES, QUE ESTA VUELTA
  SON SEIS, y las seis salidas se pegan CITADAS POR SU PROPIO NOMBRE DE
  FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 133 --comparar docs/loop/REPORTE.md
    python scripts/loop/tallar_identidad_reporte.py --vuelta 133 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 133
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR, la SEGUNDA (la
  que escribes en la TAREA 2) IDENTIDAD IDENTICA AL TALLADOR, y las otras
  cuatro VERDE EXIT 0.
  (1.k) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte, con
  su salida.
  (1.l) LOS DOS REGIMENES DE ESCRITURA:
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o
      a docs/ se mide con git diff --numstat y con grep -c "^-[^-]" sobre
      el diff EN CERO, mas git diff --word-diff=porcelain pegado si toca
      una linea vieja. NO necesita las tres guardas.
    - REGIMEN A CON LINEA VIEJA: esta vuelta el UNICO fichero viejo que
      puede cambiar de contenido es docs/plan/OP_S_11_MAPEO_PROPUESTO.md,
      que se REHACE entera por 4.d. Su word-diff va pegado. Ningun otro
      fichero viejo pierde una linea; si te descubres borrando en otro,
      paras. LA CORRECCION DE R.13 DE LA TAREA 3 ES POR ADICION: no se
      borra ni se edita una sola linea de las ya escritas.
    - REGIMEN B, DATO: esta vuelta NO SE USA. NO SE TOCA UN SOLO NODO NI UN
      SOLO FICHERO DE dataset/. Si te descubres necesitando uno, es que te
      saliste del encargo: paras y lo traes.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE.
  >>> COMMIT Y PUSH de 1.d a 1.g y de 1.l en cuanto esas guardas esten
  >>> corridas y pegadas. 1.h, 1.i, 1.j y 1.k VAN AL FINAL, con el sello de
  >>> cierre, y NO se adelantan. Esta es la reparacion de mi 4.6.

- TAREA 2, LA ESCALADA. OPERACION DE CODIGO, BLOQUEANTE, Y NO ES
  OPCIONAL. La encargo yo en el acta 132 porque la racha de caidas de
  reporte llego a DOS y AUDITOR.md 1.2 (letra del 29 ago 2026) manda
  encargarla en el mismo acta, sin esperar parada ni decision nueva del
  fundador. EJECUTOR.md 1 la tiene escrita como "la extension del tallador
  a las fases mecanicas", y yo la apunto al sitio EXACTO por donde entro la
  caida de la 132: LA LINEA DE IDENTIDAD, que es prosa suelta encima de la
  tabla tallada y por eso se sigue tecleando a mano desde la vuelta 79.
  (2.a) scripts/loop/tallar_identidad_reporte.py --vuelta N. Emite, en
  texto listo para pegar, el parrafo de identidad del reporte con sus TRES
  rotulos, y NINGUNO se teclea:
    - "HEAD sellado de apertura": la unica linea de
      docs/loop/SALIDA_V<N>_HEAD_APERTURA.txt, validada con git rev-parse
      y git cat-file -t (tiene que ser un commit, y de esta rama).
    - "commit de nacimiento de las salidas de apertura": se calcula con
      `git log --diff-filter=A --format=%h -1 --` sobre TODOS los ficheros
      docs/loop/SALIDA_V<N>_*_APERTURA.txt que existan, uno por uno. Si no
      salen TODOS del MISMO commit, es ROJO y se nombra cada fichero con
      su commit. Ese es el numero del rotulo, y no otro.
    - "HEAD sellado de cierre": la unica linea de
      docs/loop/SALIDA_V<N>_HEAD_CIERRE.txt, validada igual.
  Y LA REGLA QUE HABRIA CAZADO LA 132 SOLA: si DOS rotulos cualesquiera
  salen con el MISMO hash, el tallador NO calla y NO lo da por bueno: lo
  escribe con todas las letras, "rotulo X y rotulo Y coinciden en <hash>",
  y anade la razon medida de por que coinciden (por ejemplo, el sello de
  cierre puesto en el commit de apertura). Una coincidencia declarada es un
  dato; una coincidencia muda es la caida de la 132.
  (2.b) --comparar docs/loop/REPORTE.md: extrae del reporte el parrafo de
  identidad, coteja ROTULO POR ROTULO contra lo medido, y termina con
  "IDENTIDAD IDENTICA AL TALLADOR" o con ROJO EXIT 1 nombrando el rotulo,
  el hash escrito y el hash medido. Si el reporte no trae los tres
  rotulos, tambien es ROJO, nombrando el que falta.
  (2.c) SUS DOS PRUEBAS POR MUTACION, Y SIN ELLAS LA GUARDA NO SE PUBLICA
  (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION). Sobre una COPIA
  del reporte, nunca sobre el fichero real: mutacion A, poner en el
  segundo rotulo el hash del primero, que es EXACTAMENTE la caida de la
  132, y comprobar que --comparar cae en ROJO nombrando ese rotulo;
  mutacion B, cambiar un caracter del hash del tercer rotulo y comprobar
  lo mismo. Las dos salidas a
  docs/loop/SALIDA_V133_2C_MUTACION_A.txt y _MUTACION_B.txt.
  (2.d) SE CABLEA en 1.j como segunda comprobacion, tal como quedo escrito
  arriba. El reporte de esta vuelta ya pasa por ella.
  (2.e) LA SEGUNDA MITAD DE LA ESCALADA, LA QUE EJECUTOR.md NOMBRA LITERAL
  ("toda tabla del reporte tallada de ficheros de salida"):
  scripts/loop/verificar_cifras_del_reporte.py. Contrato, y lo escribo
  cerrado para que no haya que decidir nada:
    - Recorre docs/loop/REPORTE.md SALTANDO la tabla tallada de la
      cabecera (que ya la cubre el tallador) y el parrafo de identidad
      (que ya lo cubre 2.a).
    - Busca pares (numero, unidad) con VOCABULARIO CERRADO de unidades:
      fichero/ficheros, par/pares, grupo/grupos, grafia/grafias,
      colapso/colapsos, nodo/nodos, linea/lineas, arista/aristas.
    - Para cada par, busca en la MISMA frase o en las DOS SIGUIENTES una
      cita de docs/loop/SALIDA_V<N>_*.txt (misma doctrina de ventana que
      verificar_cifras_del_plan.py, reusala, no la reinventes). Si la hay,
      CUENTA la cifra en ese fichero y coteja. SI NO CUADRA, ROJO EXIT 1
      con la linea, el numero escrito, el numero contado y el fichero.
    - Y AQUI VA EL RAMAL (xvii) HECHO CODIGO: la unidad manda como se
      cuenta. "N ficheros" se cuenta como ficheros DISTINTOS; "N pares" se
      cuenta como pares fichero:linea. Si las dos cuentas del mismo bloque
      dan numeros distintos y la cifra escrita coincide con la que NO
      corresponde a su unidad, ROJO, y el mensaje dice las dos cuentas.
    - Si un numero no encuentra fichero de salida en su ventana, NO es
      rojo: se LISTA en la salida como "cifra sin fichero que contar" con
      su linea, para que se vea que la guarda la miro y decidio no
      cotejarla. Esa lista se pega en el reporte.
    - Su prueba por mutacion, obligatoria igual que la de 2.c: cambiar una
      cifra cotejable en una COPIA del reporte y comprobar que cae en ROJO
      nombrando la linea. Salida a
      docs/loop/SALIDA_V133_2E_MUTACION.txt.
  SI EL TEXTO DE ESTA TAREA NO TE ALCANZA PARA EJECUTARLA SIN DECIDIR,
  PARAS Y LO TRAES ESCRITO. No la recortes en silencio: eso seria el ramal
  (iii).
  >>> COMMIT Y PUSH detras de 2.c y otro detras de 2.e.

- TAREA 3, LOS REGISTROS. Son DOS, las dos REGIMEN A puro, aditivas, sin
  borrar una sola linea.
  (3.a) EL REGISTRO R.14 EN docs/PENDIENTES.md, seccion nueva,
  correcciones declaradas de la vuelta 132, con estas CINCO cosas y con la
  medicion de cada una escrita, no resumida: (1) tu caida de reporte de la
  linea de identidad, con los ONCE ficheros de apertura y su commit de
  nacimiento 3a5fd829 escritos uno por uno, con el agravante de que
  verificar_apertura_sellada.py imprimia "nacido en 3a5fd829, padre
  5eb04ca5", y con la constancia de que ACUMULA y de que la racha queda en
  DOS de tres; (2) tu caida de expediente del "la adjudica el fundador",
  con la cita literal de mi 3.d de la 132; (3) tu incumplimiento del diff
  pegado de MOTOR y WEB, con la constancia de que la afirmacion era
  VERDADERA y lo que falto fue la prueba; (4) MI CAIDA DE CIFRA: la
  correccion de R.13, que se hace POR ADICION al pie de R.13 y sin tocar
  una linea de las ya escritas, diciendo que donde dice SEIS pares son
  SIETE, listando los CINCO de Reason (los cuatro ya escritos mas
  docs/plan/03_FUSIONES.md:7159) y los DOS de Esty, y diciendo la unidad
  con todas las letras: CINCO PARES fichero:linea en CUATRO FICHEROS
  DISTINTOS para Reason; y (5) mis otras dos caidas de encargo, la guarda
  mal descrita y el sello de cierre contradictorio. Cierra con los ramales
  (xvi) y (xvii) enteros.
  (3.b) LA FICHA DEL CAMPO `fuente` EN docs/PENDIENTES.md recibe la
  UNDECIMA entrada, aditiva: la cola de localizador vigente recorta
  `, Anexo X` pero NO recorta `, Apendice X`, y por eso
  `Diana L. Lindstrom, Procurement Project Management Success, Apendice B
  (RFPS)` pasa por LIBRO ante la regla de la canonica. Con la tabla de las
  cuatro combinaciones que medi en el acta 132 (3.1) copiada entera, y con
  el dato de que las tres grafias del censo que llevan Anexo o Apendice
  son las TRES de la misma familia Lindstrom, medido.
  >>> COMMIT Y PUSH de 3.a y 3.b en cuanto esten escritas.

- TAREA 4, EL TRABAJO. LA SEGUNDA MITAD DE `OP-S-11`, TERCERA PARTE.
  REGIMEN A ESTRICTO: NO SE TOCA UN SOLO NODO NI UN SOLO FICHERO DE
  dataset/. Y NO SE APLICA LA TABLA A NINGUN NODO. Todo lo de abajo lo
  adjudique yo en el acta 132 (3.1) y aqui solo se programa.
  (4.a) LA COLA DE LOCALIZADOR SE EXTIENDE CON `Apendice`. EFECTO
  NOMBRADO, POR EL RAMAL (xiv): AGRUPA, igual que el resto de la cola.
  Escribe scripts/loop/vuelta133_cola_localizador_apendice.py o extiende
  el vuelta132_grupos_por_localizador.py sin borrarlo. La cola pasa a
  recortar tambien `, Apendice X`, `, Apendices X y Z` y `, Anexos X`
  (plural del que ya estaba). ADJUDICADO Y NO DISCUTIBLE: `Apendice` es el
  mismo localizador que `Anexo` escrito en la otra grafia, y las dos
  formas conviven en la MISMA familia del censo, asi que la extension es
  por cita, no doctrina nueva.
  SUS DOS CASOS, POR EL RAMAL (xiii): POSITIVO, la grafia
  `Diana L. Lindstrom, Procurement Project Management Success, Apendice B
  (RFPS)` recorta a `Diana L. Lindstrom, Procurement Project Management
  Success` y DEJA DE SER LIBRO; NEGATIVO, una grafia sin cola no se toca
  ni un caracter. Salida a
  docs/loop/SALIDA_V133_4A_COLA_CON_APENDICE.txt.
  MI CONTRASTE, MEDIDO HOY POR MI: con la cola extendida y SIN 3.d, los
  106 grupos pasan a 105; los grupos de 2 o mas siguen siendo 15 pero con
  39 grafias; los solos bajan de 91 a 90; las SINTETICAS siguen en 1 y el
  singleton de Apendice B entra al grupo SINTETICO de capitulos, que queda
  de CUATRO miembros. Si te sale otra cosa, manda la tuya y declara la
  discrepancia.
  >>> COMMIT Y PUSH detras de 4.a.
  (4.b) EL PREFIJO SOBRE LA RECORTADA SE APLICA, ATADO A 4.a Y NUNCA
  SUELTO. EFECTO NOMBRADO: AGRUPA. Esta es la adjudicacion de tu
  discutible 1, y la hago yo, no el fundador. Prefijo ESTRICTO sobre la
  forma recortada, guarda de longitud de 20 caracteres o mas sobre la
  recortada mas corta, MAS la guarda de RESTO por simetria con la regla
  del titulo (si las dos grafias tienen resto y ninguno es prefijo del
  otro, no se unen). Escribe
  scripts/loop/vuelta133_prefijo_sobre_recortada.py.
  POR QUE ATADO: lo medi, y aplicar el prefijo SOLO, sobre la cola vieja,
  corona `..., Apendice B (RFPS)` como canonica de 23 nodos y deja las
  SINTETICAS del censo en CERO. Es el mismo vicio que el acta 131 (3.2)
  escribio la regla sintetica para matar, entrando por otra puerta. Con
  4.a puesta, la misma familia queda coronada por
  `Diana L. Lindstrom, Procurement Project Management Success (J. Ross,
  2014)`, que es el libro con su edicion.
  MI CONTRASTE, MEDIDO HOY POR MI: con 4.a y 4.b, 105 grupos pasan a 104;
  14 grupos de 2 o mas con 39 grafias; 90 solos; UNA familia Lindstrom de
  SIETE grafias y 23 nodos; canonica `Diana L. Lindstrom, Procurement
  Project Management Success (J. Ross, 2014)`, NO sintetica. La guarda de
  RESTO no cambia el resultado hoy (104 con ella y sin ella, los mismos 19
  pares): PONLA IGUAL, y dilo en la salida, porque cierra el agujero para
  cuando el censo crezca. Salida a
  docs/loop/SALIDA_V133_4B_PREFIJO_APLICADO.txt, con TODOS los pares que
  une, uno por uno.
  >>> COMMIT Y PUSH detras de 4.b.
  (4.c) LA CONSECUENCIA QUE SE MIRA CON LOS OJOS ABIERTOS Y SE ESCRIBE.
  Con 4.a y 4.b puestas, las canonicas SINTETICAS del censo pasan de UNA a
  CERO. LA REGLA SINTETICA DE LA 132 (3.b) NO SE BORRA, NO SE MARCA MUERTA
  Y NO SE SACA DEL CODIGO: queda VIGENTE Y SIN CASO EN ESTE CORTE, y eso
  se dice con esas palabras en la cabecera de la tabla de 4.d y en la
  ficha de 3.b. Una regla sin caso hoy no es una regla equivocada; es una
  regla esperando. Salida contada, no afirmada.
  (4.d) LA TABLA REHECHA. Reescribe docs/plan/OP_S_11_MAPEO_PROPUESTO.md
  con 4.a y 4.b puestas. MISMAS CUATRO COLUMNAS de la 132 (grafia,
  canonica propuesta, motivo con las DOS cosas separadas, bolsa), y el
  vocabulario de la columna de motivo gana los dos valores nuevos: la
  regla que agrupa puede ser ahora `cadena entera`, `titulo`,
  `localizador` o `prefijo sobre recortada`, y de donde sale la canonica
  sigue siendo `la propia grafia`, `recorte de localizador` o `SINTETICA`.
  En la cabecera, CADA REGLA POR SEPARADO Y ACUMULADA, con las cinco
  cifras: cadena entera sola 111, mas titulo 108, mas localizador 106, mas
  Apendice en la cola 105, mas prefijo sobre recortada 104; cuantos grupos
  de 2 o mas y cuantos solos; que sigue siendo PROPUESTA y sin aplicarse a
  ningun nodo; que `OP-S-11` sigue LISTA; y CUANTOS COLAPSOS FALTAN PARA
  55, que con mi medicion son 49. Su word-diff va pegado. Y CORRIGE LA
  FRASE DE ATRIBUCION de la cabecera vieja: las reglas mecanicas las
  adjudica el auditor en su acta; lo que queda para decision humana del
  fundador son los colapsos que ninguna regla mecanica alcanza.
  >>> COMMIT Y PUSH detras de 4.d.
  (4.e) LO QUE NO SE TOCA ESTA VUELTA, DICHO SIN CONDICIONALES:
  `OP-S-11` NO CAMBIA DE ESTADO, SIGUE LISTA. `OP-S-12` NO SE ABRE: va al
  final de la pasada entera por la atadura 2 de docs/plan/00_INDICE.md. LA
  FASE 05 NO SE DECLARA CERRADA POR NADIE, Y NO TIENES QUE JUZGAR SI LO
  ESTA: no lo esta, porque `OP-S-11` tiene trabajo, y cuando lo este lo
  declaro yo en mi acta. Y la fase 00_CODIGO tampoco: `OP-C-01` a
  `OP-C-05`, `OP-S-06` y `OP-S-07` figuran LISTA y ESO YA ESTA ADJUDICADO
  (acta 25 y acta 119). Si tropiezas con esos estados, no abras nada.
  >>> El commit y push del REPORTE va al final, despues del sello de
  >>> cierre de 1.a, de las guardas de 1.h e 1.i, de las SEIS
  >>> comprobaciones de 1.j y de la medida de 1.k. Ese es el ultimo commit
  >>> de la vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
