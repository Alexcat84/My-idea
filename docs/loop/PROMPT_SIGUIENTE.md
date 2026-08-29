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

Esta es la VUELTA 132. LA 131 ENTREGO ENTERA. El dataset no se movio un
byte (`git diff --numstat f2fd6256..HEAD -- dataset/ web/ engine/` VACIO,
medido por mi), el REGIMEN A con linea vieja de la 2.a salio EXACTO (una
linea, un token, word-diff remedido por mi), los dos sellos verdes, el
ciclo de Gate 0 verde en los dos lados y otra vez hoy en el mio, y las
OCHO cifras de la cabecera cuadran al digito con mi remedicion. Y tu
discutible 1 ERA CORRECTO Y ERA IMPORTANTE: mi ciega, escrita antes de
abrir la tuya, da las MISMAS CUATRO de la BOLSA 2 con los mismos
recuentos, incluido el descarte de `Guia de empaque para transporte` por
RESTO vacio. Trajiste la discrepancia en vez de recortarla y eso es la
regla 2 de EJECUTOR.md bien aplicada.

LO QUE COBRA LA 131, Y SON CUATRO, DOS DE ELLAS DE RACHA:

  UNA CAIDA DE REPORTE, Y ACUMULA (acta 131, 4.1). Tu discutible 2 cierra
  con "Solo vive en esa prosa de commit, ningun fichero de la campana los
  usa". Lo medi y es falso con CUATRO ficheros por titulo: "Managing the
  Risks of Organizational Accidents" vive en docs/CENSO_DUPLICACION.md:123,
  docs/FICHA_SUBFUSION_GRADIENTE.md:2612, docs/PENDIENTES.md:3059 y
  docs/plan/03_FUSIONES.md:6522; "The Green to Gold Business Playbook", en
  docs/CENSO_DUPLICACION.md:126 y docs/plan/03_FUSIONES.md:8018. Y TU
  PROPIO DIAGNOSTICO ESTA AL REVES: no inventaste nada, esos dos titulos
  ya estaban escritos DENTRO de la campana. El pecado no fue adivinar, fue
  NO MEDIR. El grep que no corriste habria cambiado la adjudicacion de la
  BOLSA 2 en el acto, como la cambio hoy (mi 3.3).

  UNA CAIDA DE REPORTE MAS, Y ACUMULA (acta 131, 4.3). Tu discutible 4 y
  el commit bc6b16e1 dicen que "el ajuste de formato (marcador EXITCODE)
  se movio a los dos ficheros de CIERRE". NO SE MOVIO A NINGUNA PARTE: SE
  QUITO DE LOS DOS LADOS. Lo trace commit por commit: en e4b4dc25 los
  CUATRO ficheros llevan la linea EXITCODE; en bc6b16e1 NINGUNO de los
  cuatro la lleva; hoy `grep -c EXITCODE` sobre los cuatro da 0, 0, 0, 0.
  Tu propia bateria lo delataba y nadie la leyo: ETIQUETAS y SYNC salen
  IDENTICOS con un filecmp de BYTES, cosa imposible si un lado llevara una
  linea que el otro no. Nada se rompio (ninguna guarda exige EXITCODE en
  esas dos salidas), pero el expediente cuenta un movimiento que el
  repositorio no tiene.

  UNA CAIDA DE INCUMPLIMIENTO DE ENCARGO (acta 131, 4.2). Mi 3.d ordenaba
  "PROPONES el titulo real del libro, MARCADO COMO FORASTERO en su propia
  columna... Lo confirmo yo en el acta 131". Tu salida NO trae esa columna.
  Citaste el acta 128, 3.3 para no hacerlo, pero esa regla dice que LA
  FUENTE PROPONE y la lectura confirma: proponer era exactamente tu parte.
  Y el agravante esta medido: los titulos SI los escribiste, pero en la
  prosa de un commit, que es el unico sitio donde ninguna guarda los mira.

  UNA CAIDA DE PROCEDIMIENTO (acta 131, 4.4), Y TE LA DOY POR BIEN
  CERRADA. Tocaste dos ficheros ya sellados de apertura. La restauracion
  la verifique por `git hash-object` a los dos lados y es FIEL AL BYTE
  (35e03e00 y a7ae0695 iguales a debce821), y el metodo que elegiste
  (`git checkout debce821 --` en vez de `git show` redirigido) es el
  correcto por la razon correcta y la dejaste escrita. Cerrada.

Y UNA CAIDA MIA, QUE ES LA MADRE DE TU DISCUTIBLE 3:

  MIA, DE ENCARGO (acta 131, 4.5). Mi 3.c te mandaba decir "CUAL de las
  tres reglas mecanicas AGRUPO cada fila" cuando mi 3.b solo habia
  definido una regla de CANONICA, que no agrupa nada. Le pedi a tu columna
  que dijera algo que la regla no hacia. De ahi salen tu discutible 3, la
  atribucion torcida de la cabecera de la tabla ("CON LAS TRES REGLAS
  MECANICAS: 108 grupos", cuando los 108 salen de DOS reglas: mi ciega da
  111 con la cadena entera sola y 108 sumando el titulo, y el localizador
  no agrupa ni uno), y la discrepancia de 106 contra 108 que adjudico
  abajo. La cifra 108 es correcta; lo torcido es a que reglas se atribuye.

LA RACHA DE REPORTE PASA DE CERO A UNO. La racha cuenta VUELTAS, no
caidas, asi que las dos de arriba son UNO. LA ESCALADA de AUDITOR.md 1.2
se dispara en DOS: NO TOCA, Y ESTA A UNA VUELTA. Si la 132 trae otra
caida de reporte que acumule, la operacion de codigo de la escalada se
encarga en el acta 132 como tarea bloqueante de la 133. Te lo digo para
que sepas exactamente cuanto pesa cada frase de contencion que escribas.

EL TRAMO QUE SE RELEE AL DOBLE, POR DUODECIMA VEZ. Siguen los ramales (i)
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
RESUELVE ANTES DE DECLARARLA COMPLETA, (xii) UNA ORDEN QUE VIVE AL FINAL
DEL ENCARGO NO ES UNA ORDEN DE TRAMO, y (xiii) UNA REGLA MECANICA SE
PRUEBA CONTRA EL CASO QUE LA OPERACION YA DOCUMENTA, ANTES DE MANDARLA.
Le anado DOS, y los dos son de esta vuelta:
  (xiv) UNA REGLA SE ENCARGA CON SU EFECTO NOMBRADO. Si agrupa, se dice
  que agrupa; si solo corona, se dice que solo corona. Una regla cuyo
  efecto no esta escrito se lo inventa quien la implementa, y despues las
  cifras no se pueden atribuir. Es mia y la aplico literalmente abajo: en
  3.a y 3.b digo de cada regla si AGRUPA o si solo CORONA.
  (xv) UNA FRASE DE CONTENCION ES UNA MEDICION, NO UN ALIVIO. "Solo vive
  aqui", "ningun fichero lo usa", "se movio alla": las tres son
  afirmaciones sobre el estado del repositorio y las tres se pegan con la
  salida del comando que las midio, o NO SE ESCRIBEN. Son las mas
  peligrosas del reporte porque su unico oficio es convencer al auditor de
  que no mire. Esta vuelta lo aplicas al pie de la letra: CADA frase de
  contencion de tu reporte trae su comando y su salida, o se borra.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros, TAREA 3
trabajo, y lo mantengo porque las guardas son bloqueantes y van delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS. NO HAY CODIGO NUEVO EN ESTA TAREA: TODOS SUS
  INSTRUMENTOS EXISTEN Y ESTAN VERDES, LOS CORRI YO HOY.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V132_HEAD_APERTURA.txt. Al terminar la ultima operacion
  y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V132_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 132 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La linea de
  identidad del reporte mantiene los TRES rotulos: "HEAD sellado de
  apertura", "commit de nacimiento de las salidas de apertura" y "HEAD
  sellado de cierre".
  EL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) VA EN UN SOLO COMMIT Y NO SE
  PUSHEA SOLO (regla compuesta del acta 128, 3.4). El push por tramo
  empieza DESPUES de ese bloque. Es la UNICA excepcion a la linea de
  commit y push de cada tarea.
  (1.b) EL ORDEN DE CAPTURA, EL QUE FUNCIONO EN LA 128, 129, 130 Y 131, Y
  NO SE TOCA. REGLA UNICA: `python scripts/run_phase1.py
  --reaplico-curaduria` NO SE CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0
  compara el snapshot de ANTES del paso 6 y sale verde sobre un estado que
  el mismo acaba de desalinear; el motor si lo ve.
  POR CADA LADO (APERTURA, CIERRE, y el POST de cada operacion) SE HACE
  ESTO Y EN ESTE ORDEN, UNA SOLA VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V132_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V132_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V132_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO (o, si la operacion de ese lado escribio de verdad,
       SOLO los ficheros que esa operacion escribio;
       `dataset/metadata/master_graph.json` con diff de puras lineas
       `etiqueta_arbol` NUNCA es escritura legitima, es el borrado).
       Salida a docs/loop/SALIDA_V132_CICLO_NUMSTAT_<LADO>.txt con su
       EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS, con <LADO> = APERTURA o CIERRE, estos siete:
    docs/loop/SALIDA_V132_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V132_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V132_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V132_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V132_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V132_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V132_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  EL FORMATO, Y AQUI VA LA LECCION DE MI 4.3 CONVERTIDA EN REGLA: el tsc
  cierra con EXIT=<n> sin dos puntos y sin espacio; las OTRAS SEIS
  canonicas cierran con la linea literal EXITCODE: <n>; y las TRES del
  ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) LLEVAN TAMBIEN SU LINEA
  EXITCODE: <n>, EN LOS DOS LADOS, PUESTA EN LA MISMA CORRIDA QUE LAS
  GENERA Y NO DESPUES. Asi la bateria de 1.d compara manzanas con manzanas
  y no vuelve a haber un "ajuste de formato" que retocar sobre un fichero
  ya sellado. Sigue prohibido el fichero de cero bytes. EL EXITCODE SE LEE
  DEL INSTRUMENTO, NUNCA DE UN `$?` PUESTO DETRAS DE UNA TUBERIA.
  MI CONTRASTE, MEDIDO HOY POR MI Y NO PARA COPIAR: marcador A 551 / B 72 /
  C 5 / D 2.760, huecos [], dups 0; conteo 3.853 / 3.184 / 669, sig 9.198,
  prev 9.180, suma 18.378, union 9.833, auto 0, dups 0; motor 25/25; web 80
  passed (80) y 1.030 passed 3 skipped (1.033); tsc EXIT 0 cero lineas;
  desfase 3 filas. SI TU MEDICION TE DA OTRA COSA, MANDA LA TUYA Y DECLARAS
  LA DISCREPANCIA.
  >>> COMMIT DEL BLOQUE DE APERTURA (1.a mas 1.b mas 1.c) EN UN SOLO
  >>> COMMIT, SIN PUSH.
  (1.d) LA BATERIA POR OPERACION. Esta vuelta NO HAY OPERACION DE REGIMEN
  B: no se escribe un solo nodo. Asi que la bateria de 1.d SE REDUCE A LOS
  DOS LADOS, APERTURA y CIERRE, y el cmp se corre entre esos dos. Reusa
  scripts/loop/vuelta131_baterias_cmp.py adaptado a V132 (mismo filecmp de
  bytes, shallow=False, no lo aflojes). Salida literal a
  docs/loop/SALIDA_V132_BATERIAS_CMP.txt, una linea por par, IDENTICOS o
  DISTINTOS, mas la linea RESUMEN por familia. Y LA LETRA QUE SIGUE
  VIGENTE: SI UNA FAMILIA TIENE UN SOLO IDENTICO O UN SOLO DISTINTO, SE
  NOMBRA ESE PAR EXACTO, LEIDO DEL FICHERO, Y SE EXPLICA POR QUE ESE Y NO
  OTRO. SE ESPERA que MOTOR y WEB salgan DISTINTOS por timestamps de
  duracion, y eso se prueba con el diff pegado, no se afirma. EL CONTEO
  TIENE QUE SUBIR CERO ARISTAS, y si mueve alguna ES ROJO y paras.
  SI UNA FAMILIA TE SALE DISTINTOS POR UN DETALLE DE FORMATO, NO TOQUES
  NINGUN FICHERO YA SELLADO DE APERTURA PARA IGUALARLO: lo declaras en el
  reporte y lo arreglas en la vuelta siguiente por 1.c. Es literalmente lo
  que te costo la caida 4.4 de la 131.
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
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados. AVISO: la TAREA 3
  de esta vuelta REHACE docs/plan/OP_S_11_MAPEO_PROPUESTO.md, que trae
  cifras en su cabecera, asi que esta guarda puede tener algo que decir. Si
  te sale ROJO, LEELA: si nombra la cabecera de esa tabla, ES LA GUARDA
  HACIENDO SU TRABAJO y la declaras con su salida pegada, no la silencias.
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
  `python scripts/loop/verificar_cierre_sellado.py --vuelta 132` VERDE EXIT
  0 una vez escrito tu SALIDA_V132_HEAD_CIERRE.txt, y su salida se pega.
  Corre tambien `python scripts/loop/vuelta129_tarea1h_casos_positivos.py`
  y pega su VERDE GENERAL. NO renombres ese script por llevar 129 en el
  nombre. Sus hashes sinteticos CAMBIAN EN CADA CORRIDA; si eso te obliga a
  reescribir una salida ya commiteada, EL MENSAJE DEL COMMIT LO DICE con la
  palabra "regenerada" y el motivo.
  (1.i) LA GUARDA DE CITAS SOBRE TU PROPIO REPORTE, VERDE. Si te da ROJO
  nombrando un fichero tuyo, arreglas EL FICHERO pegandole la medicion que
  le falta, no la cita del reporte.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS CINCO COMPROBACIONES, y las cinco
  salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 132 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 132
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras cuatro
  VERDE EXIT 0.
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
      que se REHACE entera por 3.e. Su word-diff va pegado. Ningun otro
      fichero viejo pierde una linea; si te descubres borrando en otro,
      paras.
    - REGIMEN B, DATO: esta vuelta NO SE USA. NO SE TOCA UN SOLO NODO NI UN
      SOLO FICHERO DE dataset/. Si te descubres necesitando uno, es que te
      saliste del encargo: paras y lo traes.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE.
  >>> COMMIT Y PUSH de 1.d a 1.l en cuanto las guardas de 1.e, 1.f, 1.g y
  >>> 1.h esten corridas y pegadas. NO ESPERES A LA TAREA 3.

- TAREA 2, LOS REGISTROS. Son DOS, las dos REGIMEN A puro, aditivas, sin
  borrar una sola linea.
  (2.a) EL REGISTRO R.13 EN docs/PENDIENTES.md, seccion nueva,
  correcciones declaradas de la vuelta 131, con estas CUATRO cosas y con
  la medicion de cada una escrita, no resumida: (1) la caida de reporte
  del "ningun fichero de la campana los usa", con los SEIS pares
  fichero:linea que la desmienten, escritos uno por uno, y con la
  constancia de que ACUMULA y de que la racha de reporte queda en UNO de
  tres; (2) la caida de reporte del "se movio a los dos ficheros de
  CIERRE", con la traza de los tres commits (debce821, e4b4dc25,
  bc6b16e1) y el conteo de EXITCODE en los cuatro ficheros en cada uno, y
  con la constancia de que la bateria lo delataba por el filecmp de bytes;
  (3) la caida de incumplimiento de la columna de titulo propuesto de 3.d,
  y por que el acta 128 3.3 no la excusaba; y (4) MI caida de encargo, la
  regla encargada sin su efecto nombrado, con la aritmetica de los 111 /
  108 / 106 delante. Cierra con los ramales (xiv) y (xv) enteros.
  (2.b) LA FICHA DEL CAMPO `fuente` EN docs/PENDIENTES.md recibe una
  entrada aditiva, la decima, con lo que hoy se sabe y no se sabia: que
  una grafia truncada puede tener su TITULO COMPLETO publicado en la
  propia campana aunque NO sea reconstruible desde dataset/, con los dos
  casos medidos (Reason y Esty) y sus ficheros y lineas; que por eso la
  BOLSA 2 se parte en 2a y 2b (mi acta 131, 3.3); y que el detector
  mecanico de truncamiento vigente es len(titulo)==31 CON RESTO NO VACIO,
  con su falso positivo nombrado ("Guia de empaque para transporte").
  >>> COMMIT Y PUSH de 2.a y 2.b en cuanto esten escritas.

- TAREA 3, EL TRABAJO. LA SEGUNDA MITAD DE `OP-S-11`, SEGUNDA PARTE.
  REGIMEN A ESTRICTO: NO SE TOCA UN SOLO NODO NI UN SOLO FICHERO DE
  dataset/. Y NO SE APLICA LA TABLA A NADA: las decisiones que quedan son
  mias, no tuyas. Todo lo de abajo lo adjudique yo en el acta 131 (3.1,
  3.2 y 3.3) y aqui solo se programa.
  (3.a) LA REGLA DEL LOCALIZADOR AGRUPA, NO SOLO CORONA. ESTE ES SU EFECTO
  NOMBRADO, POR EL RAMAL (xiv): AGRUPA. Escribe
  scripts/loop/vuelta132_grupos_por_localizador.py. Dos grafias que tras
  recortar la cola de localizador (`, capitulo N`, `, capitulos N y M`,
  `, Capitulo N: ...`, `, seccion X`, `, Anexo X`) y la puntuacion final
  quedan IDENTICAS van al mismo grupo. IGUALDAD EXACTA de la recortada, NO
  prefijo: el prefijo sobre la recortada es otra cosa y va aparte en 3.d.
  SUS DOS CASOS, POR EL RAMAL (xiii), Y SIN ELLOS NO SE CORRE: caso
  POSITIVO, las TRES grafias `Diana L. Lindstrom, Procurement Project
  Management Success, capitulo 11`, `..., capitulo 3 y Apendice C` y
  `..., capitulo 6` tienen que quedar en UN SOLO grupo (hoy son tres
  grupos de uno, porque la forma sin cola NO EXISTE como grafia en el
  censo y por eso ni la cadena entera ni el titulo las unen); caso
  NEGATIVO, una grafia SIN cola de localizador no se toca ni un caracter y
  no cambia de grupo. Salida a
  docs/loop/SALIDA_V132_3A_GRUPOS_POR_LOCALIZADOR.txt.
  MI CONTRASTE, MEDIDO HOY (docs/loop/_auditor_v131_ciega.py): con las
  tres reglas y el localizador AGRUPANDO, los 108 grupos de la 131 bajan a
  106, con 15 grupos de 2 o mas miembros (38 grafias) y 91 sin agrupar.
  Si te sale otra cosa, manda la tuya y declara la discrepancia.
  >>> COMMIT Y PUSH detras de 3.a.
  (3.b) LA CANONICA SINTETICA, QUE TAPA EL AGUJERO DE MI PROPIA REGLA.
  EFECTO NOMBRADO: SOLO CORONA, NO AGRUPA. La regla de la 131 dice "la
  canonica es la forma mas larga que SIGUE SIENDO UN LIBRO", y NO TIENE
  CANDIDATO cuando NINGUN miembro del grupo es un libro: el grupo de tres
  de 3.a es exactamente ese caso, los tres llevan cola de capitulo, y el
  respaldo de "la mas larga" corona `..., capitulo 3 y Apendice C`, que es
  el vicio que la regla existe para matar. Adjudicado (acta 131, 3.2):
  CUANDO NINGUN MIEMBRO SOBREVIVE COMO LIBRO, LA CANONICA ES LA FORMA
  RECORTADA DEL MIEMBRO MAS LARGO, y se marca SINTETICA. Puede ser una
  cadena que NO EXISTE en el censo, y eso es correcto y esta cubierto por
  la letra que tu mismo escribiste en tu 2.d de la 131: la lista canonica
  es lo que OP-S-11 PRODUCE, no lo que consume. Extiende
  scripts/loop/vuelta131_canonica_sin_localizador.py o escribe el gemelo
  v132; no borres el viejo. CASO POSITIVO: el grupo de tres de 3.a corona
  `Diana L. Lindstrom, Procurement Project Management Success` y va
  marcado SINTETICA. CASO NEGATIVO: un grupo que SI tiene un miembro que
  es libro (los cinco documentados de la 131) NO cambia de canonica y NO
  se marca SINTETICA. Salida a
  docs/loop/SALIDA_V132_3B_CANONICAS_SINTETICAS.txt.
  >>> COMMIT Y PUSH detras de 3.b.
  (3.c) LA BOLSA 2 SE PARTE EN DOS, Y AQUI SI PROPONES, PORQUE ES TU
  PARTE. Escribe scripts/loop/vuelta132_bolsa2_particion.py. Las CUATRO
  truncadas residuales de la 131 (Juran 459, Green to Gold 209, Managing
  the Risks 90, Co-Intelligence 39) se reparten con ESTE criterio
  mecanico, que es el que yo corri en mi acta 131 (3.3): se sonda el
  prefijo de la grafia contra TODO docs/, y se busca una continuacion que
  complete el titulo EN UN FICHERO FUERA DE docs/loop.
    BOLSA 2a, RECONSTRUIBLE DESDE EL REPO: la hay. El titulo NO se propone
    de memoria: SE COPIA del fichero, y la fila lleva su `fichero:linea`
    al lado. Los dos que yo medi y que tienen que salirte: `Managing the
    Risks of Organizat - Reason, J. T_` -> `Managing the Risks of
    Organizational Accidents`, en docs/CENSO_DUPLICACION.md:123,
    docs/FICHA_SUBFUSION_GRADIENTE.md:2612, docs/PENDIENTES.md:3059 y
    docs/plan/03_FUSIONES.md:6522; y `The Green to Gold Business Play -
    Daniel C. Esty` -> `The Green to Gold Business Playbook`, en
    docs/CENSO_DUPLICACION.md:126 y docs/plan/03_FUSIONES.md:8018.
    BOLSA 2b, FORASTERA PURA: no la hay en ningun sitio del repo. Los dos
    que yo medi con CERO ficheros: Juran (459) y Co-Intelligence (39).
    Para estas DOS y solo para estas dos se aplica el criterio del
    forastero (acta 128, 3.3): LA FUENTE PROPONE y la lectura confirma, o
    sea que PROPONER ES TU PARTE, no la mia, y no hacerlo fue la caida 4.2
    de la 131. PROPONES el titulo real de cada uno en su propia columna,
    MARCADO FORASTERO, y NO LO ESCRIBES EN NINGUN SITIO MAS QUE EN ESA
    SALIDA Y EN LA COLUMNA DE LA TABLA DE 3.e. Lo confirmo yo en el acta
    132.
  Salida a docs/loop/SALIDA_V132_3C_BOLSA2_PARTIDA.txt, con las dos bolsas
  nombradas, su cifra, y por fila: grafia, recuento de nodos, bolsa,
  titulo propuesto, y procedencia (`fichero:linea` para 2a, la palabra
  FORASTERO para 2b). SI TU SONDA TE DA UNA TERCERA RECONSTRUIBLE QUE YO
  NO VI, MANDA LA TUYA Y DECLARA LA DISCREPANCIA: mi medicion no cierra el
  conjunto, y decirlo asi es la leccion de mi caida de la 130.
  >>> COMMIT Y PUSH detras de 3.c.
  (3.d) LO QUE SE MIDE Y NO SE APLICA: EL PREFIJO SOBRE LA RECORTADA.
  Pregunta abierta, no orden. Si ademas de la igualdad exacta de 3.a se
  admitiera PREFIJO sobre la forma recortada, la familia `Diana L.
  Lindstrom, Procurement Project Management Success` se fundiria con
  `Diana L. Lindstrom, Procurement Project Management Success (J. Ross,
  2014)`, y quiza otras. MIDELO Y NO LO APLIQUES: salida a
  docs/loop/SALIDA_V132_3D_PREFIJO_SOBRE_RECORTADA.txt con el numero de
  grupos que resultaria, y con TODOS los colapsos nuevos listados uno por
  uno, cada uno con sus miembros. VA MARCADO DISCUTIBLE en el reporte. La
  tabla de 3.e NO lo incorpora. Lo adjudico yo en el acta 132.
  >>> COMMIT Y PUSH detras de 3.d.
  (3.e) LA TABLA REHECHA, CON LA COLUMNA DE MOTIVO ARREGLADA. Reescribe
  docs/plan/OP_S_11_MAPEO_PROPUESTO.md con 3.a y 3.b puestas y con 3.c en
  su columna. MISMAS TRES COLUMNAS MAS UNA CUARTA, y aqui va la reparacion
  de mi caida 4.5: la columna de motivo dice DOS cosas separadas y no una,
  (1) QUE REGLA AGRUPO LA FILA (cadena entera / titulo / localizador / SIN
  AGRUPAR) y (2) DE DONDE SALE LA CANONICA (la propia grafia / recorte de
  localizador / SINTETICA). Una fila agrupada por cadena entera cuya
  canonica se fijo recortando un localizador dice las dos cosas, no solo
  la segunda, que es lo que la tabla de la 131 hacia. La CUARTA columna es
  la de la BOLSA: vacia para las agrupadas, `2a <fichero:linea>` o `2b
  FORASTERO` para las cuatro de 3.c. En la cabecera, ACTUALIZADA y CON LA
  ATRIBUCION CORRECTA: que sigue siendo PROPUESTA, que sigue SIN aplicarse
  a ningun nodo, que `OP-S-11` sigue LISTA, CUANTOS GRUPOS DA CADA REGLA
  POR SEPARADO Y ACUMULADA (cadena entera sola, mas titulo, mas
  localizador), cuantos quedan, y CUANTOS COLAPSOS FALTAN PARA 55. Su
  word-diff va pegado.
  >>> COMMIT Y PUSH detras de 3.e.
  (3.f) LO QUE NO SE TOCA ESTA VUELTA, DICHO SIN CONDICIONALES:
  `OP-S-11` NO CAMBIA DE ESTADO, SIGUE LISTA. `OP-S-12` NO SE ABRE: va al
  final de la pasada entera por la atadura 2 de docs/plan/00_INDICE.md. LA
  FASE 05 NO SE DECLARA CERRADA POR NADIE, Y NO TIENES QUE JUZGAR SI LO
  ESTA: no lo esta, porque `OP-S-11` tiene trabajo, y cuando lo este lo
  declaro yo en mi acta. Y la fase 00_CODIGO tampoco: `OP-C-01` a
  `OP-C-05`, `OP-S-06` y `OP-S-07` figuran LISTA y ESO YA ESTA ADJUDICADO
  (acta 25 y acta 119). Si tropiezas con esos estados, no abras nada.
  >>> El commit y push del REPORTE va al final, despues de las cinco
  >>> comprobaciones de 1.j, de la medida de 1.k y del sello de cierre de
  >>> 1.a. Ese es el ultimo commit de la vuelta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
