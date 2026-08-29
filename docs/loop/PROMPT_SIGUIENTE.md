Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

SOBRE ESA PRIMERA LINEA: al abrir esta vuelta el arbol tiene que estar
LIMPIO. Yo commitee mis cuatro ficheros de auditoria dentro de mi propio
commit de acta, asi que no te dejo nada colgando. Si ves
dataset/metadata/master_graph.json marcado ` M` con `git diff --numstat`
VACIO, ESO NO ES TRABAJO Y NO SE COMMITEA: es ruido de fin de linea. Si
ves lineas de `etiqueta_arbol` en el diff, tampoco: es el borrado de la
curaduria que deja cualquier corrida de `run_phase1.py`, y se repara
corriendo `python scripts/etiquetas_de_cara.py --aplicar` y
`python scripts/sync_assets_web.py` hasta que
`git diff --numstat -- dataset/ web/ engine/` quede VACIO. CUALQUIER OTRA
COSA SIN COMMITEAR: PARAS Y LA TRAES.

Esta es la VUELTA 131. LA 130 ENTREGO ENTERA Y ES LA MEJOR TANDA DE
MEDICION DE LA CAMPANA, Y TE LO DIGO CON LA ARITMETICA DELANTE PORQUE ES
TUYA: re-medi con codigo propio, escrito ANTES de abrir el tuyo, las
DIECIOCHO cifras que publicaste, y las DIECIOCHO cuadran al digito. Las
tres del separador (135 con `;`, 129 con `|`, 128 con los dos, todas en
primera posicion). Los TRECE grupos, miembro por miembro y candidata por
candidata. Las 98 sin agrupar. Las 129 filas de la tabla. Hugos 2/95 en
las dos unidades y Horowitz 3/71 contra 2/72. El 29/29 de la verificacion
1. CERO DISCREPANCIAS EN TODA LA TANDA. Y el separador lo adjudique yo por
mi cuenta antes de leer tu razon escrita, con los mismos datos delante (8
nodos con `|` que separan citas completas, 264 con `;` que separan
coautores o son residuo de truncamiento): elegi `|`, como tu.

LO QUE COBRA LA 130, Y SON DOS, NINGUNA DE RACHA:

  UNA CAIDA DE REPORTE, QUE NO ACUMULA (acta 130, 4.1). Escribiste "21
  ficheros mencionan grafia" sin salida de instrumento pegada. Corri ONCE
  variantes del grep y ninguna da 21: 272, 266, 43, 37, 27, 26, 23, 19,
  15, 14 y 12. La afirmacion que carga el peso ("ninguna tabla de mapeo
  vive en docs/") SI es cierta y la verifique yo aparte sondeando las 124
  grafias largas contra todos los ficheros de docs/. La cifra vive en
  prosa de acompanamiento, asi que se registra, dispara relectura al
  doble, y NO acumula por la letra del fundador del 27 ago 2026.

  UNA CAIDA DE EXPEDIENTE (acta 130, 4.2). Tu commit `fc23b099` dice en el
  mensaje que corrige "dos salidas de guarda sin marcador de EXITCODE".
  Cierto de una. De la otra no: ese mismo commit REGENERO
  SALIDA_V130_1H_CIERRE_SELLADO.txt, 9 lineas anadidas y CINCO BORRADAS,
  cambiando los hashes sinteticos `8f5840bc` a `b7f0c50e` y `5e9c5c03` a
  `694e2a4f`, y el mensaje no lo dice. Lo medi: `grep -rl 8f5840bc docs/`
  da CERO, y ese hash es justo el que el docstring que commiteaste UN
  COMMIT ANTES (2.d, `b61a6c1b`) cita como prueba de que el hash varia.
  Nada falso se publico y el hash varia por diseno, pero el registro que
  el expediente senala lo sobrescribio un commit que no lo declaro. Ramal
  (ii) por el otro lado: cuando regeneres una salida ya commiteada, EL
  MENSAJE LO DICE.

Y TRES CAIDAS MIAS, Y LA TERCERA ES LA QUE MANDA SOBRE ESTA VUELTA:

  MIA, DE CIFRA (acta 130, 4.3). Mi acta 129 publico "veinte ficheros" del
  mismo grep. Tampoco reproduce. La mia fue primero y la cobro igual.

  MIA, DE ENCARGO (acta 130, 4.4). Mi 3.c te mandaba marcar un discutible
  "si la fase queda a una sola operacion con trabajo", y ese antecedente
  dependia de MI adjudicacion de OP-S-10, que todavia no existia. No
  podias evaluarlo. Una condicion cuyo disparador esta en la cabeza del
  auditor no es una condicion: es una adivinanza. Este encargo no trae
  ninguna.

  MIA, DE ENCARGO, Y ES LA GRANDE (acta 130, 4.5). Te escribi "agrupa las
  grafias TRUNCADAS (una es prefijo estricto de otra, QUE ES EL PATRON QUE
  LA OPERACION DOCUMENTA)". NO ES EL PATRON QUE LA OPERACION DOCUMENTA. Lo
  medi hoy: el recorte de importacion corta EL TITULO A 31 CARACTERES
  EXACTOS y el sufijo " - Autor" va DETRAS, asi que el prefijo sobre la
  cadena entera NO PUEDE CAZARLO. Los cuatro casos con len(titulo)=31:
  `Essentials of Supply Chain Mana`, `Co-Intelligence_ Living and Wor`,
  `Juran's Quality Handbook_ The C`, `The Hard Thing About Hard Thing`. Y
  al primero de esos se le escapa HUGOS, QUE ES EL CASO PROBADO DE LA
  PROPIA OPERACION. Mi regla ciega dio 13 grupos y la tuya dio 13 grupos:
  las dos cortas por la misma razon, la regla. La revoco abajo y la
  reemplazo, y de ahi sale el ramal nuevo.

EL TRAMO QUE SE RELEE AL DOBLE, POR UNDECIMA VEZ. Siguen los ramales (i)
NINGUNA MEDICION SE ATRIBUYE A UN ESTADO QUE NO ES EL SUYO, (ii) EL
EXPEDIENTE NO PUEDE DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, (iii)
NINGUNA GUARDA SE ESTRECHA EN SILENCIO, (iv) TODA CIFRA SOBRE UN ARTEFACTO
CONTABLE SE LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO, (v) NINGUNA
VARA SE ESTRECHA EN EL ENCARGO, (vi) UN SUPERVIVIENTE SE RAZONA COMO SE
RAZONA UNA CLASE, (vii) UNA FUSION NO ACABA HASTA QUE LA ULTIMA ARISTA DEL
ABSORBIDO ESTA RECONSTRUIDA, (viii) UNA CIFRA DE PASIVO SE PARTE EN DOS
ANTES DE REMITIRLA, (ix) TODA CIFRA DE PASIVO O DE CENSO SE PUBLICA CON SU
UNIDAD Y SU ESTADO PEGADOS, (x) UN ORDEN DE MEDICION SE PRUEBA CORRIENDOLO
ENTERO SOBRE ARBOL LIMPIO ANTES DE MANDARLO, (xi) UNA NOMINA DE IDS SE
RESUELVE ANTES DE DECLARARLA COMPLETA, y (xii) UNA ORDEN QUE VIVE AL FINAL
DEL ENCARGO NO ES UNA ORDEN DE TRAMO. Le anado UNO, y sale de mi caida:
  (xiii) UNA REGLA MECANICA SE PRUEBA CONTRA EL CASO QUE LA OPERACION YA
  DOCUMENTA, ANTES DE MANDARLA. Si la regla no caza el ejemplo que el plan
  escribio como sintoma, la regla no es mecanica: es decorativa. Esta
  vuelta lo aplicas literalmente: cada regla nueva trae su caso positivo
  (caza a Hugos) y su caso negativo (no funde dos libros distintos), o no
  se corre.

LA ESCALADA de AUDITOR.md 1.2 se dispara con la racha de reporte en DOS.
Estamos en CERO. NO TOCA, y la dejo dicha entera para que nadie la de por
gastada.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros, TAREA 3
trabajo, y lo mantengo porque las guardas son bloqueantes y van delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS. NO HAY CODIGO NUEVO EN ESTA TAREA: TODOS SUS
  INSTRUMENTOS EXISTEN Y ESTAN VERDES, LOS CORRI YO HOY.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V131_HEAD_APERTURA.txt. Al terminar la ultima operacion
  y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V131_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 131 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La linea de
  identidad del reporte mantiene los TRES rotulos: "HEAD sellado de
  apertura", "commit de nacimiento de las salidas de apertura" y "HEAD
  sellado de cierre".
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT Y NO SE
  PUSHEA SOLO (regla compuesta del acta 128, 3.4). El push por tramo
  empieza DESPUES de ese bloque. Es la UNICA excepcion a la linea de
  commit y push de cada tarea.
  (1.b) EL ORDEN DE CAPTURA, EL QUE FUNCIONO EN LA 128, LA 129 Y LA 130, Y
  NO SE TOCA. REGLA UNICA: `python scripts/run_phase1.py
  --reaplico-curaduria` NO SE CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0
  compara el snapshot de ANTES del paso 6 y sale verde sobre un estado que
  el mismo acaba de desalinear; el motor si lo ve.
  POR CADA LADO (APERTURA, CIERRE, y el POST de cada operacion) SE HACE
  ESTO Y EN ESTE ORDEN, UNA SOLA VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V131_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V131_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V131_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO (o, si la operacion de ese lado escribio de verdad,
       SOLO los ficheros que esa operacion escribio;
       `dataset/metadata/master_graph.json` con diff de puras lineas
       `etiqueta_arbol` NUNCA es escritura legitima, es el borrado).
       Salida a docs/loop/SALIDA_V131_CICLO_NUMSTAT_<LADO>.txt con su
       EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS, con <LADO> = APERTURA o CIERRE, estos siete:
    docs/loop/SALIDA_V131_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V131_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V131_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V131_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V131_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V131_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V131_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio, sigue
  prohibido el fichero de cero bytes, y el marcador de las demas salidas es
  la linea literal EXITCODE: <n>. EL EXITCODE SE LEE DEL INSTRUMENTO, NUNCA
  DE UN `$?` PUESTO DETRAS DE UNA TUBERIA.
  MI CONTRASTE, MEDIDO HOY POR MI Y NO PARA COPIAR: marcador A 551 / B 72 /
  C 5 / D 2.760, huecos [], dups 0; conteo 3.853 / 3.184 / 669, sig 9.198,
  prev 9.180, suma 18.378, union 9.833, auto 0, dups 0; motor 25/25; web 80
  passed (80) y 1.030 passed 3 skipped (1.033); tsc EXIT 0 cero lineas. SI
  TU MEDICION TE DA OTRA COSA, MANDA LA TUYA Y DECLARAS LA DISCREPANCIA.
  >>> COMMIT DEL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) EN UN SOLO
  >>> COMMIT, SIN PUSH.
  (1.d) LA BATERIA POR OPERACION. Esta vuelta NO HAY OPERACION DE REGIMEN
  B: no se escribe un solo nodo. Asi que la bateria de 1.d SE REDUCE A LOS
  DOS LADOS, APERTURA y CIERRE, y el cmp se corre entre esos dos. Salida
  literal a docs/loop/SALIDA_V131_BATERIAS_CMP.txt, una linea por par,
  IDENTICOS o DISTINTOS, mas la linea RESUMEN por familia. Y LA LETRA QUE
  SIGUE VIGENTE: SI UNA FAMILIA TIENE UN SOLO IDENTICO O UN SOLO DISTINTO,
  SE NOMBRA ESE PAR EXACTO, LEIDO DEL FICHERO, Y SE EXPLICA POR QUE ESE Y
  NO OTRO. EL CONTEO TIENE QUE SUBIR CERO ARISTAS, y si mueve alguna ES
  ROJO y paras.
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
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados. AVISO: la TAREA 2.a
  de esta vuelta CAMBIA UNA LINEA VIEJA de docs/plan/OPERACIONES.jsonl, asi
  que esta guarda puede tener algo que decir. Si te sale ROJO, LEELA: si
  nombra la linea de OP-S-10 que yo te mando cambiar, ES LA GUARDA
  HACIENDO SU TRABAJO y la declaras en el reporte con su salida pegada, no
  la silencias.
  (1.g) LAS TRES GUARDAS DE ARISTAS SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py con su --autoprueba, verificar_aristas_vivas.py
  con su --autoprueba, y verificar_huerfanas_por_fusion.py con su caso
  positivo por mutacion. verificar_aristas_vivas.py --antes <HEAD sellado
  de apertura> --despues WORK tiene que dar PERDIDAS 0 y NUEVAS 0 (esta
  vuelta no toca dataset), y huerfanas tiene que seguir en TOTAL 29 /
  FABRICADAS 0. MI CONTRASTE, MEDIDO HOY: aristas vivas 7.296 contra 7.296,
  PERDIDAS 0 NUEVAS 0; huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1
  FABRICADAS 0.
  (1.h) LA GUARDA DEL SELLO DE CIERRE SE CORRE:
  `python scripts/loop/verificar_cierre_sellado.py --vuelta 131` VERDE EXIT
  0 una vez escrito tu SALIDA_V131_HEAD_CIERRE.txt, y su salida se pega.
  Corre tambien `python scripts/loop/vuelta129_tarea1h_casos_positivos.py`
  y pega su VERDE GENERAL. NO renombres ese script por llevar 129 en el
  nombre. Y POR LA CAIDA 4.2 DE LA 130: sus hashes sinteticos CAMBIAN EN
  CADA CORRIDA; si eso te obliga a reescribir una salida ya commiteada, EL
  MENSAJE DEL COMMIT LO DICE con las palabras "regenerada" y el motivo.
  (1.i) LA GUARDA DE CITAS SOBRE TU PROPIO REPORTE, VERDE. Si te da ROJO
  nombrando un fichero tuyo, arreglas EL FICHERO pegandole la medicion que
  le falta, no la cita del reporte.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS CINCO COMPROBACIONES, y las cinco
  salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 131 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 131
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras cuatro
  VERDE EXIT 0.
  (1.k) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte, con
  su salida.
  (1.l) LOS DOS REGIMENES DE ESCRITURA, CON UNA PRECISION QUE ESTA VUELTA
  HACE FALTA Y QUE ADJUDICO AQUI PARA QUE NO LA ADIVINES:
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o
      a docs/ se mide con git diff --numstat y con grep -c "^-[^-]" sobre
      el diff EN CERO, mas git diff --word-diff=porcelain pegado si toca
      una linea vieja. NO necesita las tres guardas.
    - REGIMEN A CON LINEA VIEJA (la 2.a de esta vuelta, y es el UNICO caso
      autorizado): cambiar el estado de una operacion en
      docs/plan/OPERACIONES.jsonl SI borra una linea, asi que el
      "borrados en cero" NO aplica y no es una infraccion. Lo que aplica en
      su lugar, y es mas estrecho: EXACTAMENTE UNA linea cambiada,
      EXACTAMENTE el token LISTA a HECHA, cero caracteres mas movidos,
      probado con `git diff --word-diff=porcelain` PEGADO, y el recuento de
      estados ANTES y DESPUES pegado al lado (63 LISTA / 8 HECHA antes, 62
      LISTA / 9 HECHA despues). Cualquier otra diferencia en ese diff es
      ROJO y paras.
    - REGIMEN B, DATO: esta vuelta NO SE USA. Si te descubres necesitando
      uno, es que te saliste del encargo: paras y lo traes.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE.
  >>> COMMIT Y PUSH de 1.d a 1.l en cuanto las guardas de 1.e, 1.f, 1.g y
  >>> 1.h esten corridas y pegadas. NO ESPERES A LA TAREA 3.

- TAREA 2, LOS REGISTROS Y LO QUE YO ADJUDIQUE. Son CUATRO. La 2.a es la
  que mueve estado y va con la vara estrecha de 1.l.
  (2.a) `OP-S-10` SE CIERRA. YO LA ADJUDICO, TU LA ESCRIBES. En
  docs/plan/OPERACIONES.jsonl, la linea de `id_op` = `OP-S-10` pasa de
  `LISTA` a `HECHA`. LA RAZON, PARA QUE LA COPIES AL REPORTE Y NO LA
  INVENTES: sus CINCO verificaciones estan verdes y las cinco las remedi yo
  hoy con codigo propio (acta 130, 3.1). V1 por P.1
  (docs/plan/BANCO_DEL_PLAN.md:11), 31 ids que resuelven a 29 vivos y 29 de
  29 nombrando el pais tras tu 3.a. V2 ya quedo adjudicada VERDE por el
  acta 128 (3.2) y hoy la remedi. V3 verde, siete de siete tras resolver.
  V4 verde, los dos contramodelos sin tocar. V5 verde, Gate 0 OK. Y el
  "CONDICIONAL" de su cabecera queda adjudicado POR SU PROPIO CRITERIO
  ESCRITO ("entra si la medicion muestra ley con alcance real"): la
  medicion del 11 ago da 31 nodos de franquicias con marco de un solo pais
  y el 80,6 por ciento sin condicionarlo en ningun sitio. ANTES DE
  ESCRIBIR, MIDE TU los estados y pega el recuento; DESPUES, remidelos y
  pega el recuento nuevo.
  >>> COMMIT Y PUSH de 2.a en cuanto el word-diff este verde.
  (2.b) LA NOTA DE CIERRE EN docs/plan/05_SANEO.md, REGIMEN A puro,
  aditiva, sin borrar nada, debajo de las dos correcciones declaradas que
  ya viven ahi: que `OP-S-10` queda CERRADA por el acta 130, con las cinco
  verificaciones nombradas una a una y con la vara de cada una, y que el
  condicional de su cabecera queda adjudicado por su propio criterio. Cita
  el acta por su seccion (3.1).
  (2.c) EL REGISTRO R.12 EN docs/PENDIENTES.md, REGIMEN A puro, seccion
  nueva, correcciones declaradas de la vuelta 130, con estas CINCO cosas:
  (1) la caida de reporte del "21 ficheros", con las once variantes del
  grep y sus once cifras escritas, y que NO acumula por la letra del 27
  ago; (2) la caida de expediente del commit `fc23b099`, con las dos
  parejas de hashes y con la constancia de que `8f5840bc` quedo huerfano en
  docs/ y solo sobrevive en el docstring de scripts/; (3) MI caida de
  cifra, el "veinte ficheros" del acta 129, escrita con todas sus letras;
  (4) MIS DOS caidas de encargo, la condicion inevaluable de la 3.c y la
  regla mecanica que no caza el patron documentado; y (5) el ramal (xiii)
  entero.
  (2.d) LA FICHA DEL CAMPO `fuente` EN docs/PENDIENTES.md recibe una
  entrada aditiva con lo que hoy se sabe y no se sabia: que el truncamiento
  corta EL TITULO A 31 CARACTERES EXACTOS (los cuatro casos con su
  longitud), que `RECORTE_POSICIONAL.md` NO ES LA VARA de la lista canonica
  porque trae la misma suciedad que la operacion existe para limpiar (su
  propia tabla publica "The Field Guide to Understandin - Dekker, Sidney;"
  como nombre canonico, truncado y con el punto y coma dentro) y su 55 es
  de otro corte (3.521 vivos), y que la lista canonica es lo que `OP-S-11`
  PRODUCE, no lo que consume.
  >>> COMMIT Y PUSH de 2.b, 2.c y 2.d en cuanto esten escritas.

- TAREA 3, EL TRABAJO. LA SEGUNDA MITAD DE `OP-S-11`, PRIMERA PARTE.
  REGIMEN A ESTRICTO: NO SE TOCA UN SOLO NODO NI UN SOLO FICHERO DE
  dataset/. Si te descubres editando dataset/, es que te saliste. Y NO SE
  APLICA LA TABLA A NADA: las 53 decisiones que quedan son mias, no tuyas.
  LO QUE ADJUDIQUE Y AHORA SE PROGRAMA (acta 130, 3.3 y 3.4):
  (3.a) LA REGLA DE PREFIJO SOBRE EL TITULO. Escribe
  scripts/loop/vuelta131_grupos_por_titulo.py. Parte cada grafia en TITULO
  (el segmento anterior al primer " - ") y RESTO. Une dos grafias cuando el
  titulo de una es PREFIJO ESTRICTO del titulo de la otra Y el titulo corto
  tiene 20 caracteres o mas. SUS DOS CASOS, POR EL RAMAL (xiii), Y SIN
  ELLOS NO SE CORRE: caso POSITIVO, la regla tiene que unir
  `Essentials of Supply Chain Mana - Michael H. Hugos` con
  `Essentials of Supply Chain Management - Michael H. Hugos`, que es el
  caso probado de la operacion y el que mi regla vieja perdia; caso
  NEGATIVO, la regla NO puede unir dos grafias cuyo RESTO (el autor) sea
  distinto y no vacio, y lo pruebas fabricando el par y viendo que no une.
  Salida a docs/loop/SALIDA_V131_3A_GRUPOS_POR_TITULO.txt.
  MI CONTRASTE, MEDIDO HOY (docs/loop/_auditor_v130_titulo.py): sumada a la
  de prefijo sobre la cadena entera, la regla del titulo baja de 111 grupos
  a 108, o sea GANA TRES COLAPSOS. Si te sale otra cosa, manda la tuya y
  declara la discrepancia.
  >>> COMMIT Y PUSH detras de 3.a.
  (3.b) LA REGLA DEL LOCALIZADOR, QUE REVOCA "LA CANONICA ES LA MAS LARGA".
  Escribe scripts/loop/vuelta131_canonica_sin_localizador.py. Mi regla
  vieja elige un localizador como nombre de libro en CUATRO de los trece
  grupos, y lo medi: `..., Anexo de aviso de no participacion` (Lindstrom),
  `..., seccion Packaging Flowers and Plants` (FedEx), `..., capitulos 1 y
  2` (Max Muller), `..., capitulo 25` (Rushton); y en un quinto elige la
  forma con punto y coma final (Dekker). LA VARA ES LA LETRA DE LA PROPIA
  OPERACION, QUE CUENTA LIBROS CANONICOS, NO CAPITULOS. La regla nueva:
  se recorta la cola de localizador (`, capitulo N`, `, capitulos N y M`,
  `, Capitulo N: ...`, `, seccion X`, `, Anexo X`) y la puntuacion final, y
  la canonica es LA FORMA MAS LARGA QUE SIGUE SIENDO UN LIBRO. Su caso
  positivo: los cinco que nombre arriba cambian de canonica. Su caso
  negativo: una grafia SIN cola de localizador no se toca ni un caracter.
  Salida a docs/loop/SALIDA_V131_3B_CANONICAS_SIN_LOCALIZADOR.txt.
  >>> COMMIT Y PUSH detras de 3.b.
  (3.c) LA TABLA REHECHA. Reescribe docs/plan/OP_S_11_MAPEO_PROPUESTO.md
  con las dos reglas nuevas puestas, MISMAS TRES COLUMNAS, y en el motivo
  di CUAL de las tres reglas mecanicas agrupo cada fila (cadena entera,
  titulo, o localizador) o SIN AGRUPAR. Es el unico fichero viejo que esta
  vuelta puede cambiar de contenido, y su word-diff va pegado. En la
  cabecera, ACTUALIZADA: que sigue siendo PROPUESTA, que sigue SIN
  aplicarse a ningun nodo, que `OP-S-11` sigue LISTA, cuantos grupos quedan
  con las tres reglas, y CUANTOS COLAPSOS FALTAN PARA 55.
  >>> COMMIT Y PUSH detras de 3.c.
  (3.d) EL RESIDUO, QUE ES LO QUE YO TENGO QUE DECIDIR Y NO PUEDO DECIDIR A
  CIEGAS. Salida a docs/loop/SALIDA_V131_3D_RESIDUO_PARA_DECISION.txt, una
  linea por grupo que las tres reglas dejaron sin colapsar, con su recuento
  de nodos, ORDENADAS DE MAYOR A MENOR RECUENTO. Y PARTIDO EN DOS BOLSAS,
  con su nombre y su cifra cada una:
    BOLSA 1, RECONSTRUIBLE: la grafia truncada TIENE en el catalogo una
    contraparte sin truncar que las reglas no unieron. Aqui la propuesta
    sale del propio dataset.
    BOLSA 2, FORASTERA: la grafia truncada NO tiene contraparte en el
    catalogo, asi que su nombre completo NO SE PUEDE RECONSTRUIR DESDE EL
    DATASET. Las dos que ya conozco y medi: `Juran's Quality Handbook_ The
    C` con 459 nodos y `Co-Intelligence_ Living and Wor` con 39. Para estas
    y solo para estas se aplica EL CRITERIO DEL FORASTERO que esta campana
    ya usa (acta 128, 3.3): la fuente propone la nomina, la lectura y el
    cableado la confirman. PROPONES el titulo real del libro, MARCADO COMO
    FORASTERO en su propia columna, y NO LO ESCRIBES EN NINGUN SITIO MAS
    QUE EN ESA SALIDA. Lo confirmo yo en el acta 131.
  >>> COMMIT Y PUSH detras de 3.d.
  (3.e) LO QUE NO SE TOCA ESTA VUELTA, DICHO SIN CONDICIONALES PARA NO
  REPETIR MI CAIDA 4.4: `OP-S-11` NO CAMBIA DE ESTADO, SIGUE LISTA.
  `OP-S-12` NO SE ABRE: va al final de la pasada entera por la atadura 2 de
  docs/plan/00_INDICE.md. LA FASE 05 NO SE DECLARA CERRADA POR NADIE, Y NO
  TIENES QUE JUZGAR SI LO ESTA: no lo esta, porque `OP-S-11` tiene trabajo,
  y cuando lo este lo declaro yo en mi acta y con ello disparo la condicion
  de parada CIERRE DE LA FASE 05, que es de fundador. Y la fase 00_CODIGO
  tampoco: `OP-C-01` a `OP-C-05`, `OP-S-06` y `OP-S-07` figuran LISTA y ESO
  YA ESTA ADJUDICADO (acta 25 y acta 119). Si tropiezas con esos estados,
  no abras nada.
  >>> El commit y push del REPORTE va al final, despues de las cinco
  >>> comprobaciones de 1.j, de la medida de 1.k y del sello de cierre de
  >>> 1.a. Ese es el ultimo commit de la vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
