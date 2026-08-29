Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 124. El acta de la 123 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final). Lo que dice, en corto: LA PARADA
QUE EL ACTA 122 DEJO AMENAZADA NO SE DISPARA. Busque la segunda cifra
falsa con todo lo que tengo (las diez filas de la cabecera remedidas una
a una, las dos correcciones de OPERACIONES.jsonl sin copiar tus numeros,
los dos censos de alias, las cuatro citas de linea, las cuatro llamadas
a cargarEntrySeeds, la nomina de OP-S-09 y sus tres cifras derivadas) y
NO HAY NINGUNA. La racha de cifra publicada BAJA DE UNO A CERO. Mi Gate
0 sale byte a byte igual al tuyo. El arreglo del tsc (EXIT=0) esta hecho
y la celda publica "EXITCODE 0, cero lineas" en sus dos columnas. Las
dos guardas de la TAREA 1 pasan mis mutaciones. Y mi relectura ciega de
los 39 pares de OP-S-09 COINCIDE EN LOS 39, incluidos los dos REPITE y
los dos supervivientes que elegiste: los adjudico a tu favor.

Lo que la vuelta cobro son TRES caidas y DOS DE ELLAS SON MIAS. Estan en
el acta 123 como 4.1, 4.2 y 4.3.

  LA QUE IMPORTA ES MIA (acta 123, 4.2): MI ENCARGO DE LA 123 ESTRECHO
  LA VARA. MESA_RACIMOS.md:214 dice "dentro del racimo se lee par a
  par", y yo te fije la cifra 39, que es la suma de (n-1) por familia, o
  sea PARES CONSECUTIVOS. Los pares del racimo son 51 (suma de C(n,2)).
  DOCE PARES NUNCA SE CONFRONTARON, todos en las nueve familias de tres
  y en la de cuatro. Tu obedeciste exacto y la caida es mia. Adjudicado
  en el acta 123 seccion 3.1, sin doctrina nueva: el alcance de "par a
  par" son TODOS los pares del racimo, y OP-S-09 NO SE EJECUTA hasta que
  los doce esten leidos. Los 39 ya leidos QUEDAN FIRMES Y NO SE RELEEN.

  LA SEGUNDA MIA (acta 123, 4.3): el contrato que dicte para
  verificar_cifras_del_plan.py pide el par "en la MISMA frase que una
  ruta citada", y la correccion 2.a que escribiste quedo partida en dos
  frases. Lo probe por mutacion propia: cambiando 27 por 99 DENTRO de la
  correccion declarada, la guarda sigue dando VERDE EXIT 0 con "0
  pares"; con la misma cifra falsa en la misma frase que la ruta, cae en
  ROJO. La guarda hace lo que su contrato dice y el contrato es corto.
  Se ensancha abajo, en la TAREA 1.f.

  LA TUYA (acta 123, 4.1), DE INCUMPLIMIENTO DE ENCARGO: mi encargo 1.d
  ordenaba "Si dos baterias salen identicas byte a byte, EL REPORTE LO
  DICE Y EXPLICA POR QUE", y te avisaba de que la 122 se lo habia
  saltado. Lo medi con cmp: CINCO de las siete salieron identicas
  (GATE0_CMD1, CONTEO, TSC, DESFASE_CALIBRADO, MARCADOR) y el reporte no
  lo nombra en ninguna parte. El determinismo es LEGITIMO (no se
  escribio nada en dataset/ y mi Gate 0 reproduce el tuyo byte a byte);
  lo que falto fue decirlo. No es cifra falsa ni afirmacion equivocada,
  no acumula para ninguna racha, pero van dos vueltas seguidas.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 123 seccion 5). Sigue
vivo el de la 120 (TODA CALIFICACION TECNICA QUE EL REPORTE COMPRIMA
RESPECTO DE SU REGISTRO LARGO) con sus ramales (i) NINGUNA MEDICION SE
ATRIBUYE A UN ESTADO QUE NO ES EL SUYO, (ii) EL EXPEDIENTE NO PUEDE
DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, (iii) NINGUNA GUARDA SE
ESTRECHA EN SILENCIO y (iv) TODA CIFRA SOBRE UN ARTEFACTO CONTABLE SE
LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO. Le anado el quinto, que
sale de mi propia caida 4.2:
  (v) NINGUNA VARA SE ESTRECHA EN EL ENCARGO. Si un encargo convierte un
  criterio escrito en una cuenta mecanica (un numero de pares, de
  familias, de sitios, de llamadas), REMIDES ese numero contra la vara
  escrita ANTES de trabajar y declaras la diferencia si la hay. Una
  cifra de alcance dictada por el auditor NO ES LA VARA: la vara es el
  texto que la cifra dice representar. Si difieren, trabajas sobre la
  vara y lo dices en el reporte.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2
trabajo; la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros,
TAREA 3 trabajo, y lo mantengo porque las guardas son bloqueantes y
tienen que ir delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA
  ANTES DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA
  OPERACION: git rev-parse HEAD, hash completo de 40 caracteres, UNA
  linea, a docs/loop/SALIDA_V124_HEAD_APERTURA.txt. Al terminar la
  ultima operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V124_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 124 tiene
  que dar VERDE EXIT 0, y su salida se cita en el reporte. La 121, la
  122 y la 123 lo hicieron bien las tres; se repite igual.
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE,
  con <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V124_GATE0_CMD1_<LADO>.txt   (scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V124_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V124_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V124_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V124_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V124_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V124_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio (lo
  arreglaste bien en la 123, se mantiene), y sigue prohibido el fichero
  de cero bytes.
  (1.c) EL CICLO DE TRES, IGUAL QUE LA 123. NINGUNA salida de guarda se
  captura mientras el ciclo este a medias. El ciclo es
  run_phase1.py --reaplico-curaduria, luego etiquetas_de_cara.py
  --aplicar, luego sync_assets_web.py, EN ESE ORDEN, y solo cuando
  git diff --numstat sobre dataset/, web/ y engine/ este en CERO se
  empieza a medir. Por cada corrida se escribe
  docs/loop/SALIDA_V124_CICLO_<ETIQUETA>_NUMSTAT.txt con la salida
  literal y una linea final "EXITCODE: N". La 123 declaro que rompio
  esta regla dos veces y la corrigio en vivo antes de publicar nada: eso
  esta bien hecho y NO se te conto. Se sigue igual.
  (1.d) LA BATERIA POR OPERACION, EN SU PROPIO CHECKPOINT, Y AHORA CON
  COMPROBACION MECANICA PORQUE DOS VUELTAS SEGUIDAS SE SALTO LA
  DECLARACION (acta 123, 4.1). Se escribe la operacion N, se corre su
  ciclo de tres entero, se miden sus cuatro salidas, Y SOLO ENTONCES
  empieza la N+1. Ficheros, con <OP> = OPS09, OPS10, etc.:
    docs/loop/SALIDA_V124_<OP>_GATE0_POST.txt
    docs/loop/SALIDA_V124_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V124_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V124_<OP>_TSC_POST.txt
  mas las de etiquetas y sync del ciclo con el mismo prefijo.
  LO NUEVO, Y ES BLOQUEANTE: antes de escribir el reporte corres
  cmp -s sobre CADA par de salidas homologas de la vuelta (apertura
  contra cierre, y cada bateria contra la anterior), vuelcas el
  resultado literal a docs/loop/SALIDA_V124_BATERIAS_CMP.txt con una
  linea por par que diga IDENTICOS o DISTINTOS, y EL REPORTE LISTA LOS
  IDENTICOS Y EXPLICA POR QUE LO SON. Si la explicacion es determinismo
  legitimo, se dice y se dice de que estado (por ejemplo: no se escribio
  nada en dataset/ entre las dos capturas, con el numstat que lo prueba
  citado al lado). Un fichero de salida sin su linea en el cmp no
  existe para el expediente.
  (1.e) LA GUARDA DE CITAS NO SE TOCA. Quedo bien en la 123: la probe
  con tu caso positivo nuevo (vuelta123_tarea1e_mutacion_fila_tabla.py,
  ROJO) y con la mutacion vieja de la 122
  (vuelta122_tarea1e_mutacion_citas.py, sigue ROJO), y lei el diff
  entero. Solo se corre, no se modifica.
  (1.f) ENSANCHAR verificar_cifras_del_plan.py, Y ES CORRECCION DE MI
  CONTRATO, NO DE TU CODIGO (acta 123, 4.3). BLOQUEANTE. La guarda hoy
  solo ve el par (numero, ruta .test.ts) cuando los dos caen en la MISMA
  frase, y por eso no cotejo la correccion declarada que tu propia
  vuelta escribio. Cambios exactos, y nada mas:
    - El par se busca ahora en una VENTANA de frases, no en una sola: un
      numero seguido de "caso", "casos", "test", "tests", "prueba" o
      "pruebas" coteja contra la primera ruta terminada en ".test.ts"
      que aparezca en la MISMA frase o en las DOS FRASES SIGUIENTES del
      mismo texto anadido. Si en esa ventana hay mas de una ruta
      distinta, es ROJO por ambiguo, diciendo las rutas: prefiero un
      rojo ruidoso a un verde por no saber a cual mirar.
    - Si un numero del vocabulario no encuentra NINGUNA ruta en su
      ventana, NO es rojo (puede ser una cifra de otra cosa), pero se
      LISTA en la salida como "numero sin ruta en ventana", con su
      id_op, su campo y la frase, para que se vea que la guarda lo miro
      y decidio no cotejarlo.
    - El bloque CONTRATO del docstring se actualiza con el alcance REAL,
      incluida la ventana y las dos exclusiones de arriba. Ramal (iii):
      ningun recorte ni ningun ensanche vive solo en el commit.
  Y llega con SU CASO POSITIVO, que es el mio y ya esta probado, asi que
  tiene que reproducirlo: sobre una COPIA del OPERACIONES.jsonl de hoy
  en la que dentro de la correccion declarada de OP-S-08 se cambie
  "la cifra real es 27 casos" por "la cifra real es 99 casos", con
  --base 128d0e5b, TIENE QUE DAR ROJO nombrando 99 contra 27 (hoy da
  VERDE con "0 pares"). Pega el rojo de la copia y el verde del fichero
  real. Y vuelve a correr tu caso positivo de la 123
  (vuelta123_tarea1f_caso_positivo.py, --base ed916471): tiene que
  SEGUIR dando ROJO 32 contra 27. Si el ensanche rompe ese caso, el
  ensanche esta mal.
  (1.g) UNA GUARDA NUEVA DE TITULOS, Y NO SE TOCA run_phase1.py.
  BLOQUEANTE. Lo medi yo (acta 123, 3.4): la celda "duplicadas de titulo
  0" que la cabecera publica en sus dos columnas se calcula con
  find_exact_title_duplicates (scripts/run_phase1.py:671), que agrupa
  por el titulo_concepto CRUDO, mientras find_near_duplicate_titles
  (linea 689) si normaliza pero EXCLUYE expresamente los pares cuyo
  titulo normalizado es IGUAL. Un par que solo difiere en mayusculas o
  acentos se cae por las dos rendijas. Escribe
  scripts/loop/verificar_titulos_normalizados.py con este contrato:
    - Lee dataset/metadata/master_graph.json, se queda con los nodos
      VIVOS, normaliza titulo_concepto (NFKD, sin diacriticos,
      minusculas, espacios colapsados) y agrupa.
    - ROJO EXIT 1 si algun grupo normalizado tiene mas de un id, salvo
      los que esten en una lista de excepciones DECLARADA dentro del
      propio script, con el id, el motivo y la vuelta que la declaro.
    - VERDE EXIT 0 con el recuento (nodos vivos examinados, grupos
      normalizados, duplicados encontrados, excepciones vigentes).
    - Caso positivo por mutacion: sobre una copia en memoria del grafo
      con un titulo duplicado inventado, tiene que dar ROJO. Pegalo.
  MIDE TU PRIMERO y publica: cuantos vivos, cuantos duplicados exactos y
  cuantos normalizados. Mi medicion, para contraste y NO para copiar:
  3.188 vivos, 0 duplicados exactos, 1 normalizado,
  sistema_responsabilidad_gerencial / sistema_responsabilidad_gerencial_2
  ("El Sistema es tu Responsabilidad" / "El Sistema es Tu
  Responsabilidad"). Si tu medicion discrepa de la mia, LA DECLARAS, no
  la resuelves copiando. Ese par es una de las 28 familias de OP-S-09 y
  quedo CONTINUA por contenido: EL VEREDICTO NO SE REABRE. Arranca el
  script con esa unica excepcion declarada y con la vuelta que la
  declara, para que la guarda quede en VERDE hoy y muerda a partir de
  manana.
  (1.h) ANTES DEL COMMIT DEL REPORTE, LAS CUATRO COMPROBACIONES, y las
  cuatro salidas se pegan:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 124 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras
  tres VERDE EXIT 0.
  (1.i) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l
  docs/loop/REPORTE.md tiene que dar 80 o menos y esa cifra se escribe
  en el propio reporte, medida. La 123 lo cumplio exacto en 80.

- TAREA 2, LOS REGISTROS Y CORRECCIONES DEL ACTA 123. Aditivos puros
  donde toquen texto viejo, medidos con git diff --numstat y con
  grep -c "^-[^-]" sobre el diff en cero. Son tres y el orden da igual.
  (2.a) LA CORRECCION DEL ALCANCE DE OP-S-09, QUE ES LA CARA Y ES MIA
  (acta 123, 4.2 y 3.1). En docs/plan/OPERACIONES.jsonl, al final de la
  nota de OP-S-09, correccion declarada aditiva: que la lectura de la
  vuelta 123 cubrio 39 pares CONSECUTIVOS por una cifra que el encargo
  del auditor fijo; que MESA_RACIMOS.md:214 dice "par a par" sin decir
  consecutivos; que los pares del racimo son 51; que quedan 12 por leer;
  y que los 39 leidos quedan firmes. CUENTA TU LOS 51 Y LOS 12 con
  codigo propio antes de escribirlo (suma de C(n,2) sobre los miembros
  de cada familia del registro SALIDA_V123_OPS09_LECTURA.jsonl, menos
  los 39 ya leidos) y pega la salida. Mi lista de los 12, para
  contraste y NO para copiar, esta en el acta 123 seccion 2.
  (2.b) EL REGISTRO LARGO DE LAS TRES CAIDAS, en docs/PENDIENTES.md,
  seccion nueva R.6 de la vuelta 123, como correcciones declaradas: (1)
  la vara estrechada a pares consecutivos, con las dos cifras y con el
  ramal (v) que estrena; (2) el contrato corto de
  verificar_cifras_del_plan.py, con las dos salidas de mi mutacion
  (VERDE con 99 en frase separada, ROJO con 99 en la misma frase) y el
  ensanche de la TAREA 1.f; (3) las cinco baterias identicas byte a byte
  no declaradas, con la salida de cmp y con la comprobacion mecanica de
  la TAREA 1.d que la remedia. Las dos primeras dicen con todas sus
  letras QUE SON DEL AUDITOR, no tuyas.
  (2.c) LA FICHA DEL PUNTO CIEGO DE TITULOS (acta 123, 3.4), en la ficha
  permanente campos-sucios-dataset de docs/PENDIENTES.md, entrada nueva
  y aditiva: que la celda "duplicadas de titulo 0" de la cabecera es
  case-sensitive y por que (las dos funciones y sus lineas, leidas por
  ti, no copiadas de mi acta); el censo que midas en la TAREA 1.g; que
  el unico par vivo queda CONTINUA por contenido y que lo que hay que
  arreglar es el TITULO, no el veredicto; y que el arreglo del titulo
  queda ANOTADO COMO TRABAJO POST CAMPAÑA salvo que una operacion
  escrita lo ordene, porque cambiar un titulo publicado no lo decide el
  bucle. NO TOQUES run_phase1.py y NO TOQUES ningun titulo.

- TAREA 3, EL TRABAJO: CERRAR OP-S-09.
  LAS TRES GUARDAS DE TODO INSTRUMENTO QUE ESCRIBA en dataset/ o en
  docs/plan/ SIGUEN VIGENTES Y SON BLOQUEANTES: (i) SIMULACION PREVIA
  sobre copia en memoria con su salida pegada, (ii) SU MUTACION NEGATIVA
  corrida y pegada, y (iii) SU ROJO REAL EN SEGUNDA PASADA, con la
  salida de git status --porcelain PEGADA DETRAS TAL CUAL SALGA, no
  descrita. Un instrumento de escritura sin las tres NO SE CORRE.
  (3.a) LOS DOCE PARES QUE FALTAN, Y ES EL SUELO DE LA VUELTA. Mismo
  metodo y mismo registro que la 123, en un fichero nuevo
  docs/loop/SALIDA_V124_OPS09_LECTURA_RESTO.jsonl, con los mismos
  campos: familia, causa, miembros, y por cada par a, b, veredicto
  CONTINUA o REPITE, superviviente propuesto si REPITE, alias que
  hereda, y la razon en UNA linea citando el campo que la sostiene. LAS
  DECISIONES VIVEN EN EL REGISTRO, NO EN PROSA DEL REPORTE (MODO AUSTERO
  2). La vara es la misma: MESA_RACIMOS.md:214 ("si el segundo nodo
  continua al primero, otro momento, otro nivel, otro angulo, los dos
  viven; si repite, se fusiona") y la DECISION 4 de la linea 343 con su
  excepcion escrita. A contenido empatado desempata el grafo.
  DOS AVISOS QUE SALEN DE MI LECTURA CIEGA Y QUE NO TE AHORRAN EL
  TRABAJO, SOLO TE DICEN DONDE MIRAR DESPACIO: el par
  auditoria_de_producto <-> auditoria_producto y el par
  estrategia_de_innovacion_de_producto <-> estrategia_innovacion_producto
  son los dos solapes mas fuertes que vi, y a los dos los sostiene una
  fase_proyecto distinta, que es "otro momento" citable. LEELOS TU Y
  DECIDE TU: si tu lectura discrepa de mi aviso, LA DECLARAS.
  NO TOQUES estructura_de_gates NI estructura_gates: son de
  OP-M-01-FUSION por el toque unico de la vuelta 78 (banco 9.4).
  Y SI EL TEXTO DE LA OPERACION NO ALCANZA PARA RESOLVER UN PAR SIN
  DECIDIR ALGO QUE NINGUNA REGLA ESCRITA CUBRE, PARAS EN ESE PAR, LO
  TRAES CON SU CASO ESCRITO Y SIGUES CON LOS DEMAS.
  (3.b) LA EJECUCION DE OP-S-09, SOLO DESPUES DE QUE LOS 51 PARES ESTEN
  LEIDOS Y REGISTRADOS (los 39 de la 123 mas los 12 de hoy). Con sus
  tres guardas, con alias para todo id que muera (verificacion 1 de la
  fila), con las aristas que apuntaban al id viejo resolviendo detras
  (verificacion 2), con cero duplicadas y cero auto-aristas despues, y
  con Gate 0 y las suites en verde en su propio checkpoint (1.d).
  Si de los 12 sale algun REPITE nuevo, entra en la misma ejecucion.
  Y LO REPITO POR ESCRITO: SI LOS 12 SE LEEN Y REGISTRAN PERO LA
  EJECUCION NO CABE CON SUS TRES GUARDAS ENTERAS, ESO ES ENTREGA
  COMPLETA, NO UN LIMITE DE ALCANCE; la ejecucion pasa a la 125 y el
  reporte publica LA CUENTA DE GUARDAS que consumio la vuelta, guarda
  por guarda con su fichero. Lo que NO es entrega completa es leer parte
  de los doce.
  (3.c) SI Y SOLO SI OP-S-09 CIERRA ENTERA CON SU EJECUCION: OP-S-10
  (orden 9, REENCUADRE_DE_MARCO, 31 nodos en el campo nodos). NO SE
  ESCRIBE NADA DE ELLA ESTA VUELTA: solo se REMIDE su nomina contra el
  grafo de hoy, como se hizo con OP-S-02, OP-S-04 y OP-S-09 (cuantos de
  los 31 siguen vivos, cuantos deprecados, y a quien reclama el alias de
  cada deprecado), y se publica. Y REMIDE TAMBIEN, por el ramal (v), si
  la cifra 31 del campo nodos coincide con lo que la nota de la fila
  dice de si misma; si no coincide, lo declaras y no lo resuelves
  copiando. OP-S-11 y OP-S-12 no se abren.
  Y AVISO OTRA VEZ, PORQUE FALTAN POCAS: cuando la fase 05 quede cerrada
  y verificada se dispara la condicion de parada CIERRE DE LA FASE 05 de
  AUDITOR.md seccion 4. Quedan OP-S-09, OP-S-10, OP-S-11 y OP-S-12. NO
  declares la fase cerrada tu: mide, publica y dilo como discutible; el
  cierre lo adjudica el auditor.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
