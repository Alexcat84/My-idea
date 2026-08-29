Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 127. El acta de la 126 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final). Lo que dice, en corto: LA VUELTA
126 EJECUTA BIEN LAS SEIS TAREAS Y REPARA LAS DOS CAIDAS QUE SE LE
DIERON. Las diez filas de la cabecera me salen identicas, mi Gate 0 sale
byte a byte igual al tuyo, el ciclo de tres deja el arbol quieto a la
primera, la (4) nueva de verificar_fusion_ops09.py MUERDE (la corri yo
contra --ref 7150339f, que es el arbol exacto de antes de tu reposicion,
y da ROJO nombrando la arista dos veces, una por cada muerto que la
citaba), y verificar_aristas_vivas.py esta bien escrita: la corri en
cuatro parejas de refs y con --antes 7150339f --despues WORK sale
PERDIDAS 0 y NUEVAS 1, siendo esa unica nueva la arista que repusiste.
O sea que tu 3.a puso una arista y tu 3.d no movio ninguna, medido por
mi. Y tu tramo de OP-S-10 me sale EXACTO: reconstrui la nomina con codigo
propio (31 unicos, 28 vivos, 26 candidatos) y mis diez primeros son tus
diez, uno a uno, con la condicion nueva primera y las viejas enteras y
en su orden en los diez.

LO QUE ESTA VUELTA COBRA, Y OTRA VEZ LO GRUESO ES MIO:

  UNA CAIDA TUYA, DE REPORTE, QUE NO ACUMULA (acta 126, 5.1): el parrafo
  de las baterias escribe "CONTEO/MOTOR/WEB/DESFASE DISTINTOS" sin
  acotar, y tu propio SALIDA_V126_BATERIAS_CMP.txt registra "CONTEO:
  OPS09REP vs cierre: IDENTICOS". Ademas quedan DOS IDENTICOS sin listar
  ni explicar (ese y "GATE0: OPS09REP vs OPS10"), cuando mi 1.d pedia
  listarlos y explicarlos todos. Los abri yo: los dos GATE0 DISTINTOS
  difieren en UNA linea, el marcador EXITCODE que llevan las salidas de
  bateria y no llevan las de apertura y cierre, y el CONTEO IDENTICO es
  la mejor noticia de tu vuelta, porque prueba que el reencuadre de 3.d
  no movio ni una arista. Vive en prosa y no mueve dato: se registra,
  dispara la relectura al doble y NO acumula. Se arregla en 1.d.

  UNA CAIDA TUYA, DE EXPEDIENTE (acta 126, 5.2): la ficha nueva dice de
  las 32 aristas huerfanas que son "todas de fusiones ANTERIORES a esta
  campana de saneo". TRES no lo son, y las tengo con commit y vuelta
  (ver abajo). El encargo te pedia el TOTAL, no la procedencia: esa
  clausula la anadiste de mas y una afirmacion en ficha permanente sin
  instrumento detras es caida de expediente. LA RAIZ ES MIA, y por eso
  la mia se cobra tambien. Se corrige en 2.a.

  UNA CAIDA MIA, DE CIFRA, Y ES LA GRANDE (acta 126, 5.3): el acta 125
  dijo "las otras 38 son de fusiones anteriores de la campana" y las
  remitio enteras a pasivo historico. Medido hoy con codigo propio: de
  las 32 de hoy, 29 son heredadas (ya estaban al encender el bucle, con
  los extremos renombrados por fusiones posteriores) y TRES las fabrico
  esta campana. La cifra no estaba mal contada: estaba mal ATRIBUIDA, y
  la atribucion es lo que decidio que no se encargaran.

  UNA CAIDA MIA, DE PROCEDIMIENTO (acta 126, 5.4): publique el 39 sin su
  comando, no deje el codigo en el repo, y por eso no pudiste cotejar y
  la discrepancia acabo escrita como "pendiente de doctrina" cuando eran
  DOS UNIDADES. Remedio puesto: mis scripts van commiteados con el acta
  (docs/loop/_auditor_v127_*.py), correlos si quieres.

  UNA CAIDA MIA, DE ENCARGO (acta 126, 5.5): el --ref c9ac2fb8 de la
  1.g(ii) pedia el caso rojo en un ref donde la fusion aun no existia.
  Tu sustituiste por WORK, que a esa altura era el estado correcto, y
  DECLARASTE la discrepancia en vez de resolverla copiando: eso es
  exactamente lo que la casa manda. El ref que aisla era 7150339f.

LO QUE ADJUDICO Y QUE ES EL TRABAJO DE ESTA VUELTA:

  (A) EL 32 CONTRA EL 39 NO ES DOCTRINA PENDIENTE: SON DOS UNIDADES, Y
  LAS REPRODUJE LAS DOS CON CODIGO PROPIO HOY. Tu 32 son PARES VIVOS
  RESUELTOS que faltan HOY. Mi 39 eran PARES MUERTOS HISTORICOS (los dos
  extremos deprecados) medidos sobre 7150339f, antes de tu reposicion. La
  resta lo cierra por los dos lados: en pares resueltos, 7150339f da 33 y
  hoy 32, y la que desaparece es dia_cero_defectos_2 ->
  eliminacion_causas_error_4; en pares crudos, 39 y 38, y la que
  desaparece es dia_cero_defectos_3 -> eliminacion_causas_error. Es la
  MISMA arista contada con dos varas. ADJUDICADO: la unidad canonica de
  la ficha es EL PAR VIVO RESUELTO, porque es la que dice si hay o no hay
  camino, que es lo que banco 9.6 llama contenido huerfano. La otra se
  conserva escrita, con su nombre y su estado. PENDIENTE DE DOCTRINA
  CERRADO: no lo dejes abierto en la ficha.

  (B) TRES DE LAS 32 LAS FABRICO ESTA CAMPANA Y SE REPONEN. Medido por mi
  (docs/loop/_auditor_v127_proyeccion.py y _historia.py): huerfanas en
  50f03099 (encendido del bucle) 30; en cbc6ce51 (nacimiento de
  pasada-unica) 30, el mismo conjunto; hoy 32. Proyectando las 30 del
  baseline por el resolutor de HOY: 29 siguen huerfanas, 1 se reparo de
  rebote (definicion_calidad_conformidad ->
  programa_mejora_calidad_14_pasos) y TRES son huecos NUEVOS que no
  existian antes del bucle:
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
  29 mas 3 son tus 32, al digito. Son el gemelo exacto del caso de
  OP-S-09: dos absorbidos de la misma operacion que se citaban entre
  ellos. Se reponen por las MISMAS tres varas del acta 125 seccion 4.1
  (banco 9.8 docs/BANCO_DE_TEXTOS.md:1841, banco 9.6 :1479, y P.16 punto
  1 docs/plan/BANCO_DEL_PLAN.md:878), con la MISMA extension declarada y
  revocable del acta 125 seccion 4.3. LAS OTRAS 29 NO SE TOCAN: esas si
  son pasivo heredado y son trabajo post campana.
  MIS CIFRAS SON CONTRASTE Y NO SE COPIAN: MIDELAS TU. Si tu medicion
  discrepa de la mia, la DECLARAS, no la resuelves copiando.

  (C) LA FORMA DE LA CONDICION DE OP-S-10 SE QUEDA LITERAL, y el tramo
  sube a los DIECISEIS que faltan en UNA vuelta (MODO AUSTERO punto 1,
  lotes al doble). La forma se queda por regla escrita: la verificacion 4
  de la propia operacion congela a los dos contramodelos como modelo y la
  verificacion 1 pide el pais en condiciones_activacion para los 31;
  adaptar el verbo nodo a nodo es redactar, y la vara del reencuadre no
  se inventa. LO QUE MEDI EN CONTRA Y NO CAMBIA NADA HOY, pero va escrito
  y va a ficha: de tus diez, solo cuatro cablean norma de un pais
  (alternativa_business_opportunity_licensing,
  alternativa_trademark_licensing, cumplir_leyes_estatales_franquicia,
  decision_fpr); en los otros seis el contenido es metodo que sirve en
  cualquier pais, y "Solo aplica si..." afirma mas de lo que el nodo
  aguanta, contra la linea del banco que pone el puntero jurisdiccional
  en "los nodos que tocan tratados, aranceles, garantias o normativa"
  (docs/BANCO_DE_TEXTOS.md:112). NO LO CAMBIES: queda MARCADO para la
  auditoria de cierre, que es de Alexis, y es revocable con una linea por
  nodo.

  (D) Y ENCONTRE OTRA COSA FUERA DE LO MARCADO, QUE NO SE TE COBRA Y QUE
  ESTA VUELTA SOLO SE MIDE: condiciones_activacion se consume TRUNCADA en
  tres sitios que lei hoy, engine/prototipo_motor.py:1532 y :1823 toman
  [:2] y engine/build_question_cache.py:97 toma [:3]. Como la condicion
  nueva va PRIMERA (forma de los contramodelos, y asi lo mande yo), en
  todo nodo con dos o mas condiciones viejas la ultima que el consumidor
  veia se cae fuera de la ventana. Medido en tus diez: 7 pierden al menos
  una en la ventana [:2] y 3 en la [:3]. Es degradacion silenciosa de
  manual: ningun test cae. SE MIDE SOBRE LOS 31 Y SE ESCRIBE, NO SE
  ARREGLA: la decision de forma es de Alexis en el cierre.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 126 seccion 6), por
septima vez y otra vez por la regla dura: lo de (B), lo de (D) y la
caida 5.1 caen los tres FUERA de los discutibles que marcaste. Siguen
vivos el tramo de la 120 con sus ramales (i) NINGUNA MEDICION SE
ATRIBUYE A UN ESTADO QUE NO ES EL SUYO, (ii) EL EXPEDIENTE NO PUEDE
DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, (iii) NINGUNA GUARDA SE
ESTRECHA EN SILENCIO, (iv) TODA CIFRA SOBRE UN ARTEFACTO CONTABLE SE LEE
DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO, el (v) de la 123 NINGUNA
VARA SE ESTRECHA EN EL ENCARGO, el (vi) de la 124 UN SUPERVIVIENTE SE
RAZONA COMO SE RAZONA UNA CLASE, y el (vii) de la 125 UNA FUSION NO
ACABA CUANDO EL ALIAS QUEDA ESCRITO, SINO CUANDO LA ULTIMA ARISTA DEL
ABSORBIDO ESTA RECONSTRUIDA. Le anado DOS:
  (viii) UNA CIFRA DE PASIVO SE PARTE SIEMPRE EN DOS ANTES DE REMITIRLA:
  lo que la campana HEREDO y lo que la campana FABRICO. Se mide
  proyectando el conjunto del baseline por el resolutor de hoy y
  restando, igual que las aristas vivas. Remitir un pasivo sin partirlo
  es remitir trabajo propio como si fuera ajeno.
  (ix) TODA CIFRA DE PASIVO O DE CENSO SE PUBLICA CON SU UNIDAD Y SU
  ESTADO PEGADOS. Dos numeros distintos del mismo fenomeno no son una
  discrepancia mientras no compartan unidad y ref: cotejar sin unidad
  fabrica pendientes de doctrina que no existen.

LA ESCALADA de AUDITOR.md 1.2 se dispara con la racha de reporte en DOS.
Estamos en CERO de las que acumulan. NO TOCA, y la dejo dicha entera para
que nadie la de por gastada.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros, TAREA 3
trabajo, y lo mantengo porque las guardas son bloqueantes y van delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V127_HEAD_APERTURA.txt. Al terminar la ultima
  operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V127_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 127 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La linea de
  identidad del reporte mantiene los TRES rotulos exactos que estrenaste
  en la 126 y que salieron bien: "HEAD sellado de apertura", "commit de
  nacimiento de las salidas de apertura" y "HEAD sellado de cierre".
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V127_GATE0_CMD1_<LADO>.txt   (scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V127_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V127_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V127_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V127_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V127_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V127_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio, sigue
  prohibido el fichero de cero bytes, y el marcador de codigo de salida de
  las demas salidas es la linea literal EXITCODE: <n>, que es la que
  verificar_citas_del_reporte.py sabe leer (esa fue tu correccion
  declarada de la 126 y se queda como convencion de la casa).
  (1.c) EL CICLO DE TRES, IGUAL QUE LA 126. NINGUNA salida de guarda se
  captura mientras el ciclo este a medias. El ciclo es run_phase1.py
  --reaplico-curaduria, luego etiquetas_de_cara.py --aplicar, luego
  sync_assets_web.py, EN ESE ORDEN, y solo cuando git diff --numstat sobre
  dataset/, web/ y engine/ este en CERO se empieza a medir. Por cada
  corrida se escribe docs/loop/SALIDA_V127_CICLO_<ETIQUETA>_NUMSTAT.txt
  con la salida literal y una linea final "EXITCODE: N". MEDIDO POR MI HOY
  SOBRE TU ARBOL: etiquetas_de_cara.py --aplicar reasienta 71 etiquetas y
  aun asi el numstat cierra en CERO a la primera pasada. Si a ti no te
  cierra, NO midas: repite el ciclo y dilo.
  (1.d) LA BATERIA POR OPERACION Y LA CORRECCION DE TU CAIDA 5.1. Se
  escribe la operacion N, se corre su ciclo de tres entero, se miden sus
  cuatro salidas, Y SOLO ENTONCES empieza la N+1. Ficheros, con <OP> =
  OPS09REP3 (las tres reposiciones de 3.a) y OPS10 (el tramo de 3.b):
    docs/loop/SALIDA_V127_<OP>_GATE0_POST.txt
    docs/loop/SALIDA_V127_<OP>_CONTEO_POST.txt
    docs/loop/SALIDA_V127_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V127_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V127_<OP>_TSC_POST.txt
  mas las de etiquetas y sync del ciclo con el mismo prefijo. Antes de
  escribir el reporte corres cmp -s sobre CADA par de salidas homologas
  de la vuelta y vuelcas el resultado literal a
  docs/loop/SALIDA_V127_BATERIAS_CMP.txt con una linea por par que diga
  IDENTICOS o DISTINTOS. Y AQUI VA LA LETRA NUEVA, QUE ES LA CORRECCION:
  EL REPORTE DA CUENTA DE LOS 21 (o los que salgan) PARES, NO DE UNA
  SELECCION. La forma barata que cabe en el tope: una linea por FAMILIA
  de par (GATE0, CONTEO, MOTOR, WEB, TSC, DESFASE, MARCADOR) que diga
  cuantos IDENTICOS y cuantos DISTINTOS salieron en esa familia y POR QUE
  lo son, y si dentro de una familia hay pares que van por motivos
  distintos, se nombran esos pares. UN IDENTICO SIN EXPLICAR ES UNA
  CAIDA, Y UN DISTINTO SIN EXPLICAR TAMBIEN. Recordatorio medido por mi
  en tu 126: dos GATE0 salieron DISTINTOS solo por la linea EXITCODE que
  llevan las salidas de bateria y no las de apertura y cierre; si esta
  vuelta vuelve a pasar, esa es la explicacion y se escribe asi. Y COMO
  ESTA VUELTA VUELVE A ESCRIBIR EN dataset/: si Gate 0 o el conteo salen
  IDENTICOS entre apertura y cierre despues de 3.a, eso NO es
  determinismo, es que la escritura no llego; se investiga y se declara
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
  ser exactamente las tres aristas de (B), nombradas. Tras 3.b, la misma
  corrida no debe anadir ninguna mas: un reencuadre de texto no mueve
  aristas, y si mueve alguna ES ROJO y paras.
  (1.h) LA GUARDA NUEVA DEL PASIVO, Y ES LA CORRECCION DE MI CAIDA 5.3.
  BLOQUEANTE, VA ANTES DE 3.a. Escribe
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
      Es tu metodo de la 126, sin cambios: la unidad canonica adjudicada.
    - UNIDAD par-crudo: lo mismo, pero deduplicando por el par HISTORICO
      (los dos ids muertos) y contando solo los casos en que el otro
      extremo tambien estaba deprecado. Es la unidad de mi 39.
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
  MI CONTRASTE, MEDIDO HOY Y NO PARA COPIAR: unidad par-resuelto, baseline
  50f03099, ref WORK: TOTAL 32, HEREDADAS 29, REPARADAS DE REBOTE 1,
  FABRICADAS 3. Unidad par-crudo sobre 7150339f: 39. MIDELO TU. SI TU
  MEDICION DISCREPA DE LA MIA, LA DECLARAS, NO LA RESUELVES COPIANDO. Y
  tras 3.a, la misma corrida tiene que dar FABRICADAS 0 y TOTAL 29.
  (1.i) ANTES DEL COMMIT DEL REPORTE, LAS CUATRO COMPROBACIONES, y las
  cuatro salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 127 --comparar docs/loop/REPORTE.md
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

- TAREA 2, LOS REGISTROS Y CORRECCIONES DEL ACTA 126. REGIMEN A. Aditivos
  puros donde toquen texto viejo, medidos con git diff --numstat y con
  grep -c "^-[^-]" sobre el diff en cero. Son tres, y 2.a se escribe
  DESPUES de que 3.a este verde porque cita su resultado medido.
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
  vuelta 126, como correcciones declaradas: (1) tu caida de reporte del
  parrafo de baterias, con las dos lineas del cmp que la desmienten;
  (2) tu caida de expediente de la clausula de procedencia, diciendo que
  la raiz es del auditor; (3) LA CAIDA DEL AUDITOR, DE CIFRA, escrita con
  todas sus letras: un pasivo publicado sin partir entre heredado y
  fabricado, y que por eso tres aristas propias se remitieron a pasivo
  historico durante una vuelta entera; (4) la caida del auditor, de
  procedimiento, por publicar el 39 sin su comando, con el remedio (los
  scripts del auditor viven ahora en docs/loop/_auditor_v127_*.py); (5) la
  caida del auditor, de encargo, por el --ref c9ac2fb8 que no aislaba; y
  (6) los ramales (viii) y (ix) del tramo que se relee al doble, escritos
  enteros.
  (2.c) LA FICHA NUEVA docs/PENDIENTES.md, permanente, con el nombre
  ventana-truncada-de-condiciones-activacion, aditiva y con su primera
  entrada: que condiciones_activacion se consume RECORTADA en tres sitios
  (engine/prototipo_motor.py:1532 y :1823 con [:2],
  engine/build_question_cache.py:97 con [:3]), verificalo tu y cita
  fichero y linea de lo que TU leas; que por eso una condicion ANTEPUESTA
  desplaza fuera de la ventana la ultima condicion vieja de todo nodo con
  dos o mas; CUANTOS DE LOS 31 DE OP-S-10 quedan afectados en cada ventana
  DESPUES de tu 3.b (MIDELO TU; mi contraste sobre los diez de la 126, no
  para copiar, es 7 en [:2] y 3 en [:3]); que NO SE ARREGLA en esta
  campana porque la forma esta aprobada y la decision es del fundador en
  la auditoria de cierre; y que se revoca con una linea por nodo. NO
  TOQUES NI UN NODO POR ESTA FICHA.

- TAREA 3, EL TRABAJO.
  (3.a) LA REPOSICION DE LAS TRES ARISTAS FABRICADAS POR LA CAMPANA.
  REGIMEN B, LAS TRES GUARDAS COMPLETAS (1.k). BLOQUEANTE Y VA PRIMERA.
  Se reponen las TRES de (B) y ninguna mas, cada una en las dos vistas
  (nodos_siguientes del origen y nodos_previos del destino). Guardas
  propias, ademas de las tres del REGIMEN B: los seis extremos siguen
  VIVOS, cero auto-aristas y cero duplicadas nuevas tras resolver, ningun
  otro campo de ningun nodo se toca (numstat que lo pruebe),
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
  pais en condiciones_activacion y que no tocaste en la 126. Los DOS
  contramodelos NO se tocan (verificacion 4). Los tres deprecados NO se
  tocan. Guardas propias del tramo, ademas de las tres: ningun otro campo
  cambia, las condiciones viejas quedan enteras y en su orden, cero
  guiones largos y cero guiones medios, y verificar_aristas_vivas.py sin
  aristas nuevas. Detras, su bateria de 1.d entera con etiqueta OPS10.
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
  Y AVISO POR TERCERA VUELTA, PORQUE YA ESTA ENCIMA: cuando la fase 05
  quede cerrada y verificada se dispara la condicion de parada CIERRE DE
  LA FASE 05 de AUDITOR.md seccion 4, y esa parada es del fundador.
  MARCA COMO DISCUTIBLE, para que yo lo adjudique: si con OP-S-10 medida
  entera la fase 05 queda a dos operaciones (OP-S-11 y OP-S-12) o si
  alguna de las dos tiene texto que no alcance para ejecutarse sin
  decidir, cosa que seria PARADA y no improvisacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
