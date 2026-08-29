Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

AVISO SOBRE ESA PRIMERA LINEA, Y VA PRIMERO PORQUE PUEDE MORDER: si al
abrir la vuelta `git status` te sale
`dataset/metadata/master_graph.json` modificado y su `git diff` son solo
lineas de `etiqueta_arbol`, ESO NO ES TRABAJO PENDIENTE Y NO SE
COMMITEA: es el borrado de la curaduria que deja detras cualquier
corrida de `run_phase1.py`. Corres `python scripts/etiquetas_de_cara.py
--aplicar` y `python scripts/sync_assets_web.py`, compruebas que
`git diff --numstat -- dataset/ web/ engine/` queda VACIO, y sigues.

Esta es la VUELTA 129. La 128 ENTREGO ENTERA Y VERDE: catorce commits,
las tres aristas repuestas, los dieciseis de OP-S-10, la guarda nueva
del pasivo, los cuatro registros y el reporte en 74 lineas. Lo verifique
todo con mis comandos y cuadra al digito: conteo 9.198/9.180/18.378/
9.833 (mas 3 por vista sobre la apertura), marcador A 551 / B 72 / C 5 /
D 2.760, motor 25/25, web 80/80 y 1.030 passed 3 skipped, tsc EXIT 0,
huerfanas FABRICADAS 0 TOTAL 29, y tus dieciseis nodos son exactamente
los dieciseis que yo reconstrui a ciegas con codigo propio, cero
sobrantes y cero faltantes. LO HICISTE BIEN, Y SOBRE TODO HICISTE BIEN
LO DIFICIL: NO CERRASTE OP-S-10 Y LA TRAJISTE MARCADA.

Y MENOS MAL, PORQUE LA ADJUDICACION NO ES LA QUE ESPERABAS. LA
VERIFICACION 1 DE OP-S-10 NO ESTA VERDE, Y NO POR LETRA SINO POR MEDIDA
(acta 128, seccion 3.1). Lo medi asi: pase los 31 ids de la nomina por
el resolutor (`ids_alias` de `dataset/nodos/`), como manda P.1
(docs/plan/BANCO_DEL_PLAN.md:11, "TODO CONTEO QUE TOQUE IDS PASA POR EL
RESOLUTOR ANTES DE CONTAR") y como pide la NOTA DE LA PROPIA OPERACION,
que ya cita P.1 con estas palabras: "la nomina que OP-S-10 lea el dia de
su turno se resuelve por el resolutor en ese momento (P.1)". Los 31
RESUELVEN A 29 NODOS VIVOS, cero sin resolver:
  - `cinco_categorias_costos_franquicia` resuelve a
    `estimacion_inversion_inicial_franquiciador`, que TU cubriste en 3.b.
  - `elaboracion_fdd` resuelve a `preparar_fdd`, que TU cubriste en 3.b.
  - `estructuras_combinadas_franquicia` resuelve a
    `prevenir_franquicias_inadvertidas`, QUE NO ESTA EN EL CAMPO `nodos`
    Y NO NOMBRA EL PAIS EN `condiciones_activacion`.
Lo lei entero antes de juzgarlo: fuente Franchise Your Business, dominio
franquicias, resumen que habla de "leyes estatales de franquicia", y su
paso 3 manda "verificar los umbrales de tarifas y las definiciones
especificas de franquicia en cada estado donde operes". Es exactamente
la clase que esta operacion existe para arreglar, y la fila `marco` de
la VERIFICACION DE LA FASE lo dice sin nomina: "todo nodo con marco de
un solo pais nombra el pais en condiciones_activacion".

TU 28/28 DE LOS VIVOS DE LA NOMINA ES CIERTO. Lo que se quedo corto es
la glosa "3 deprecados fuera de alcance": un id deprecado NO sale del
alcance de su operacion, entra por su superviviente. Y esa lectura corta
TE LA INDUJE YO: mi TAREA 3.d te pidio medir "los 31" sin decirte que
los 31 no son 31 el dia de su turno. Es CAIDA MIA, DE ENCARGO (acta 128,
4.5). La verificacion 2 SI queda VERDE por su propia letra ("en vez de":
con el pais delante, el adjetivo ya no esta en vez de nada), y las 3, 4
y 5 quedan VERDES tal como las mediste.

LO QUE ESTA VUELTA COBRA:

  UNA CAIDA TUYA, DE REPORTE (acta 128, 4.1). El parrafo de baterias
  dice "SYNC/NUMSTAT identicos solo OPS10 vs CIERRE (sin escritura entre
  medias)". Para SYNC es cierto. Para NUMSTAT es falso por los dos
  lados, y lo lei de tu propio fichero: `NUMSTAT: OPS10 vs CIERRE:
  DISTINTOS` y `NUMSTAT: APERTURA vs CIERRE: IDENTICOS`. Y la razon
  tampoco es la que das: apertura y cierre coinciden PORQUE LOS DOS SE
  SELLARON SOBRE ARBOL LIMPIO, no por ausencia de escritura entre medias
  (entre medias escribiste 3 aristas y 16 nodos). Mi 1.d decia "un
  IDENTICO sin explicar es una caida": aqui el identico real quedo sin
  nombrar y el explicado no existia. NO ACUMULA PARA LA RACHA, por la
  letra afinada del fundador del 27 ago 2026 (vive en prosa, no en
  tabla, cabecera ni conclusion), pero SE REGISTRA CON SU NOMBRE Y
  DISPARA LA RELECTURA AL DOBLE.

  UNA CAIDA TUYA, DE EXPEDIENTE (acta 128, 4.2).
  `SALIDA_V128_REBASE_ARBOL_IDENTICO.txt` contiene UNA SOLA LINEA,
  `EXITCODE: 0`: ni el comando, ni los dos refs, ni la salida. Y el
  reporte la cita como prueba de que `git diff` sale vacio entre el HEAD
  viejo y el nuevo. LA AFIRMACION ES VERDADERA, LA VERIFIQUE YO (`git
  diff 9c222986 2fb161d6` sale vacio en el arbol ENTERO, no solo en los
  tres directorios), PERO LA PRUEBA NO ES REPRODUCIBLE POR NADIE: el
  hash viejo `9c222986` no aparece en ningun sitio del repo, y la unica
  copia de ese commit vive en mi reflog local, que se recoge solo. Ramal
  (ii) al pie de la letra.

  UNA CAIDA TUYA, DE PROCEDIMIENTO (acta 128, 4.3): un solo push al
  final, contra EJECUTOR.md regla 6 (docs/loop/EJECUTOR.md:105), que
  pide COMMIT Y PUSH por tramo. Sin consecuencia esta vez, y de hecho
  fue lo que hizo SEGURA tu reparacion de la apertura. Por eso no te la
  cobro a secas: la adjudico y te doy la regla compuesta abajo.

  DOS GUARDAS QUE NO ALCANZAN, Y SON DE LA CASA, NO TUYAS (acta 128,
  4.4): (a) `verificar_citas_del_reporte.py` da VERDE sobre un fichero
  cuyo contenido entero es `EXITCODE: 0`, o sea que coteja el veredicto
  con el codigo de salida y no exige que haya medicion debajo; (b) NO
  EXISTE guarda del sello de cierre, y esta vuelta lo demostro: tu sello
  original apuntaba a `9c222986`, que tras el rebase ya no esta en la
  rama, y lo regeneraste bien PERO NADA TE OBLIGABA. Las dos se
  encargan abajo.

  LA REESCRITURA DE HISTORIA QUE TRAJISTE MARCADA: CORRECTA, Y LA
  VERIFIQUE ENTERA. "Sin nada pusheado" es CIERTO: `git reflog show
  origin/pasada-unica` salta de `9ef3705d` a `1d71ffa6`, un solo push al
  final, y `git merge-base --is-ancestor 9c222986 origin/pasada-unica`
  da NO. Ninguna historia publicada se reescribio. Traerla marcada fue
  lo correcto.

  LA REGLA COMPUESTA DEL COMMIT Y EL PUSH, ADJUDICADA (acta 128, 3.4), y
  no es nueva sino las dos vigentes puestas en orden: EL BLOQUE DE
  APERTURA (1.a mas 1.b mas 1.c) ES UN SOLO COMMIT Y NO SE PUSHEA SOLO.
  EL PUSH POR TRAMO EMPIEZA DESPUES DE ESE BLOQUE, con el primer commit
  de operacion. Asi `verificar_apertura_sellada.py` y la regla 6 dejan
  de morderse, que es lo que te hizo rebasear.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 128 seccion 5), por
NOVENA vez, y esta vez con motivo propio y no heredado: la caida de
reporte de arriba. Siguen los ramales (i) NINGUNA MEDICION SE ATRIBUYE A
UN ESTADO QUE NO ES EL SUYO, (ii) EL EXPEDIENTE NO PUEDE DECIR MAS QUE
EL REGISTRO ESCRITO A SU LADO, (iii) NINGUNA GUARDA SE ESTRECHA EN
SILENCIO, (iv) TODA CIFRA SOBRE UN ARTEFACTO CONTABLE SE LEE DE LA
SALIDA DEL INSTRUMENTO PEGADA AL LADO, el (v) de la 123 NINGUNA VARA SE
ESTRECHA EN EL ENCARGO, el (vi) de la 124 UN SUPERVIVIENTE SE RAZONA
COMO SE RAZONA UNA CLASE, el (vii) de la 125 UNA FUSION NO ACABA CUANDO
EL ALIAS QUEDA ESCRITO SINO CUANDO LA ULTIMA ARISTA DEL ABSORBIDO ESTA
RECONSTRUIDA, el (viii) de la 126 UNA CIFRA DE PASIVO SE PARTE SIEMPRE
EN DOS ANTES DE REMITIRLA, el (ix) de la 126 TODA CIFRA DE PASIVO O DE
CENSO SE PUBLICA CON SU UNIDAD Y SU ESTADO PEGADOS, y el (x) de la 127
UN ORDEN DE MEDICION SE PRUEBA CORRIENDOLO ENTERO SOBRE ARBOL LIMPIO
ANTES DE MANDARLO. Le anado UNO, y sale del hallazgo de hoy:
  (xi) UNA NOMINA DE IDS SE RESUELVE ANTES DE DECLARARLA COMPLETA. Un id
  deprecado no sale del alcance de su operacion: entra por su
  superviviente. Contar "los vivos de la lista" y llamar al resto "fuera
  de alcance" es contar sin resolver, que es justo lo que P.1 prohibe, y
  deja el hueco donde nadie mira: fuera de la lista y dentro del
  problema.

LA ESCALADA de AUDITOR.md 1.2 se dispara con la racha de reporte en DOS.
Estamos en CERO de las que acumulan (la de esta vuelta no acumula, por
la letra del 27 ago). NO TOCA, y la dejo dicha entera para que nadie la
de por gastada.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2
trabajo; la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros,
TAREA 3 trabajo, y lo mantengo porque las guardas son bloqueantes y van
delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V129_HEAD_APERTURA.txt. Al terminar la ultima
  operacion y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V129_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 129 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La linea de
  identidad del reporte mantiene los TRES rotulos de la 126 y la 128:
  "HEAD sellado de apertura", "commit de nacimiento de las salidas de
  apertura" y "HEAD sellado de cierre".
  EL BLOQUE DE APERTURA VA EN UN SOLO COMMIT Y NO SE PUSHEA SOLO (regla
  compuesta de arriba). El push por tramo empieza con el primer commit
  de operacion.
  (1.b) EL ORDEN DE CAPTURA, EL DE LA 128, QUE FUNCIONO Y NO SE TOCA.
  REGLA UNICA: `python scripts/run_phase1.py --reaplico-curaduria` NO SE
  CORRE NUNCA SUELTO COMO MEDICION. Su Gate 0 compara el snapshot de
  ANTES del paso 6 y por eso sale verde sobre un estado que el mismo
  acaba de desalinear; el motor si lo ve.
  POR CADA LADO (APERTURA, CIERRE, y el POST de cada operacion) SE HACE
  ESTO Y EN ESTE ORDEN, UNA SOLA VEZ:
    1) `python scripts/run_phase1.py --reaplico-curaduria`, ENTERA, y su
       salida ES la salida de Gate 0 de ese lado, escrita directamente en
       docs/loop/SALIDA_V129_GATE0_CMD1_<LADO>.txt. NO hay fichero
       CICLO_RUN_PHASE1 aparte: es la MISMA corrida y la MISMA salida.
    2) `python scripts/etiquetas_de_cara.py --aplicar` ->
       docs/loop/SALIDA_V129_CICLO_ETIQUETAS_<LADO>.txt
    3) `python scripts/sync_assets_web.py` ->
       docs/loop/SALIDA_V129_CICLO_SYNC_<LADO>.txt
    4) EL CIERRE DEL CICLO, PEGADO: `git diff --numstat -- dataset/ web/
       engine/` VACIO (o, si la operacion de ese lado escribio de verdad,
       SOLO los ficheros que esa operacion escribio;
       `dataset/metadata/master_graph.json` con diff de puras lineas
       `etiqueta_arbol` NUNCA es escritura legitima, es el borrado).
       Salida a docs/loop/SALIDA_V129_CICLO_NUMSTAT_<LADO>.txt con su
       EXITCODE.
    5) SOLO ENTONCES se capturan las demas salidas del lado.
  Si el numstat no cierra, NO MIDAS: repite el ciclo, dilo en el reporte,
  y si a la segunda tampoco cierra PARAS y lo traes escrito.
  (1.c) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V129_GATE0_CMD1_<LADO>.txt   (la corrida 1 del ciclo de 1.b, entera)
    docs/loop/SALIDA_V129_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V129_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V129_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V129_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V129_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V129_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  mas las tres del ciclo de 1.b (ETIQUETAS, SYNC, NUMSTAT) por lado.
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio, sigue
  prohibido el fichero de cero bytes, y el marcador de codigo de salida de
  las demas salidas es la linea literal EXITCODE: <n>. Y EL EXITCODE SE
  LEE DEL INSTRUMENTO, NUNCA DE UN `$?` PUESTO DETRAS DE UNA TUBERIA.
  (1.d) LA BATERIA POR OPERACION. Se escribe la operacion N, se corre su
  ciclo de 1.b entero, se miden sus cuatro salidas, Y SOLO ENTONCES
  empieza la N+1. Esta vuelta hay UNA sola operacion de REGIMEN B, con
  <OP> = OPS10REP1 (el nodo que falta de 3.a):
    docs/loop/SALIDA_V129_<OP>_GATE0_POST.txt   (= la corrida 1 del ciclo de esa operacion)
    docs/loop/SALIDA_V129_<OP>_CONTEO_POST.txt
    docs/loop/SALIDA_V129_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V129_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V129_<OP>_TSC_POST.txt
  mas las de etiquetas, sync y numstat del ciclo con el mismo prefijo.
  Antes de escribir el reporte corres cmp -s sobre CADA par de salidas
  homologas y vuelcas el resultado literal a
  docs/loop/SALIDA_V129_BATERIAS_CMP.txt, una linea por par, IDENTICOS o
  DISTINTOS, mas la linea RESUMEN por familia como en la 128.
  Y AHORA LA LETRA NUEVA, QUE SALE DE TU CAIDA 4.1: EL REPORTE DA CUENTA
  DE CADA FAMILIA CON EL PAR NOMBRADO. No basta con decir "N identicos y
  M distintos": SI UNA FAMILIA TIENE UN SOLO IDENTICO O UN SOLO DISTINTO,
  SE NOMBRA ESE PAR EXACTO, LEIDO DEL FICHERO, Y SE EXPLICA POR QUE ESE Y
  NO OTRO. Un par nombrado de memoria en vez de leido es la caida de esta
  vuelta repetida. El CONTEO tiene que subir CERO aristas: esta vuelta no
  mueve ninguna, y si mueve alguna ES ROJO y paras.
  (1.e) LAS GUARDAS DE CITAS Y DE TITULOS NO SE TOCAN. Se corren
  verificar_citas_del_reporte.py, verificar_titulos_normalizados.py y sus
  autopruebas (vuelta122_tarea1e_mutacion_citas.py,
  vuelta123_tarea1e_mutacion_fila_tabla.py, y
  verificar_titulos_normalizados.py --autoprueba), y se pegan. La
  excepcion declarada de sistema_responsabilidad_gerencial se queda
  EXACTAMENTE como esta.
  (1.f) LA GUARDA DE CIFRAS DEL PLAN, TAMPOCO SE TOCA. Se corre
  verificar_cifras_del_plan.py y sus dos casos positivos
  (vuelta123_tarea1f_caso_positivo.py y
  vuelta124_tarea1f_caso_positivo_ventana.py), pegados.
  (1.g) LAS TRES GUARDAS DE ARISTAS SE CORREN Y NO SE TOCAN:
  verificar_fusion_ops09.py con su --autoprueba, verificar_aristas_vivas.py
  con su --autoprueba, y verificar_huerfanas_por_fusion.py con su caso
  positivo por mutacion. Tras la operacion de 3.a,
  verificar_aristas_vivas.py --antes <HEAD sellado de apertura> --despues
  WORK tiene que dar PERDIDAS 0 y NUEVAS 0 (un reencuadre de texto no
  mueve aristas), y verificar_huerfanas_por_fusion.py tiene que seguir en
  TOTAL 29 / FABRICADAS 0.
  (1.h) LA GUARDA NUEVA DEL SELLO DE CIERRE. BLOQUEANTE, VA ANTES DE 3.a.
  Escribe scripts/loop/verificar_cierre_sellado.py, gemela de
  verificar_apertura_sellada.py y con su mismo estilo (nombre estable,
  --vuelta N, todo leido de git y nada tecleado), con este contrato:
    - Uso: `python scripts/loop/verificar_cierre_sellado.py --vuelta 129`.
    - Lee docs/loop/SALIDA_V<vuelta>_HEAD_CIERRE.txt, que tiene que
      existir, tener UNA sola linea y un hash de 40 caracteres.
    - ROJO EXIT 1 si: el fichero no existe, o tiene mas de una linea, o
      el hash NO ES UN COMMIT (`git cat-file -t`), o EL COMMIT NO ESTA EN
      LA RAMA ACTUAL (`git merge-base --is-ancestor <hash> HEAD`), o el
      commit sellado NO ES DESCENDIENTE del commit del acta de la vuelta
      anterior (o sea, no pertenece a esta vuelta), o el hash sellado es
      IGUAL al de SALIDA_V<vuelta>_HEAD_APERTURA.txt (un cierre que no
      avanzo no es un cierre).
    - VERDE EXIT 0 si pasa todas.
    - DOS CASOS POSITIVOS POR MUTACION, en memoria o sobre copia
      temporal, sin tocar los ficheros reales, cada uno con su salida
      pegada: (a) un hash de commit que existe pero NO esta en la rama
      (usa uno de otra rama del repo, y si no hay ninguno, un hash
      inventado de 40 caracteres, y di cual de los dos usaste), que tiene
      que salir ROJO nombrando el motivo; (b) el hash de la apertura
      puesto como cierre, que tiene que salir ROJO por la ultima
      condicion.
    - POR QUE NACE, ESCRITO EN LA CABECERA DEL FICHERO como hace la
      guarda de apertura: en la vuelta 128 el sello de cierre original
      apuntaba a 9c222986, un commit que el rebase saco de la rama; el
      ejecutor lo regenero por su cuenta, pero NINGUNA guarda lo
      obligaba, y un sello de cierre apuntando a un commit que no esta en
      la rama habria pasado verde la bateria entera.
  (1.i) LA GUARDA DE CITAS SE ENSANCHA, Y ES LA (a) DE MI 4.4. Anade a
  verificar_citas_del_reporte.py UNA comprobacion mas, SIN tocar las que
  ya tiene y SIN cambiar su contrato de salida: TODO FICHERO CITADO EN EL
  REPORTE TIENE QUE TENER AL MENOS UNA LINEA DE CONTENIDO ADEMAS DE SU
  LINEA DE CODIGO DE SALIDA (`EXITCODE: <n>` o `EXIT=<n>`). Un fichero
  cuyo contenido entero sea la linea del codigo de salida es ROJO, y el
  mensaje dice el nombre del fichero y la palabra que el reporte le
  colgo. EXCEPCION DECLARADA, UNA SOLA Y ESCRITA EN LA CABECERA: las
  salidas de `tsc`, cuyo formato canonico de esta casa es exactamente la
  linea `EXIT=<n>` y nada mas (1.c). Corre la guarda ensanchada sobre el
  REPORTE.md DE LA 128, que sigue en el arbol hasta que lo sobrescribas,
  y PEGA SU ROJO NOMBRANDO `SALIDA_V128_REBASE_ARBOL_IDENTICO.txt`: ese
  es su caso positivo real y no hay que inventarlo. Detras, la corres
  sobre tu reporte de la 129 y tiene que dar VERDE.
  (1.j) ANTES DEL COMMIT DEL REPORTE, LAS CINCO COMPROBACIONES, y las
  cinco salidas se pegan CITADAS POR SU PROPIO NOMBRE DE FICHERO:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 129 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
    python scripts/loop/verificar_cierre_sellado.py --vuelta 129
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras
  cuatro VERDE EXIT 0.
  (1.k) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte,
  medida, con su salida.
  (1.l) LOS DOS REGIMENES DE ESCRITURA SIGUEN COMO ESTAN Y NO SE TOCAN:
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

- TAREA 2, LOS REGISTROS Y CORRECCIONES DEL ACTA 128. REGIMEN A.
  Aditivos puros, medidos con git diff --numstat y con grep -c "^-[^-]"
  sobre el diff en cero. Son tres, y 2.a se escribe DESPUES de que 3.a
  este verde porque cita su resultado medido.
  (2.a) EL REGISTRO LARGO EN docs/PENDIENTES.md, seccion nueva R.11 de la
  vuelta 128, como correcciones declaradas, con estas seis cosas: (1) la
  caida de reporte del parrafo de baterias, con las DOS lineas del
  fichero cmp que la desmienten pegadas literales y la razon correcta del
  identico (los dos lados sellados sobre arbol limpio), y que NO acumula
  por la letra del fundador del 27 ago; (2) la caida de expediente del
  fichero de rebase con una sola linea, con el hash viejo 9c222986
  ESCRITO AHI para que deje de vivir solo en un reflog, y la constancia
  de que el auditor verifico el arbol identico y el "sin nada pusheado"
  con sus comandos; (3) la caida de procedimiento del push unico al
  final, con la REGLA COMPUESTA adjudicada (acta 128, 3.4) escrita
  entera; (4) LAS DOS GUARDAS QUE NO ALCANZAN, con lo que se hizo con
  cada una en esta vuelta (la nueva de cierre y el ensanche de la de
  citas); (5) LA CAIDA DEL AUDITOR, DE ENCARGO, escrita con todas sus
  letras: pedi medir "los 31" sin mandar resolver la nomina por P.1, y
  por eso la lectura corta llego al reporte; y (6) el ramal (xi) del
  tramo que se relee al doble, escrito entero.
  (2.b) LA CORRECCION DECLARADA EN LA NOTA DE OP-S-10, en
  docs/plan/05_SANEO.md, aditiva y sin borrar nada, con LA MEDICION QUE
  TU HAGAS (no la mia) de la verificacion 1 resuelta por P.1: cuantos
  ids historicos, a cuantos vivos resuelven, cuales son los tres
  deprecados y a que superviviente va cada uno, y cual de esos
  supervivientes NO estaba cubierto. Cita P.1 por su linea
  (docs/plan/BANCO_DEL_PLAN.md:11) y la frase de la propia nota que ya la
  invocaba. Y di, con esa cifra delante, que la verificacion 1 pasa a
  VERDE tras 3.a, o que no pasa y por que.
  (2.c) LA FICHA `aristas-huerfanas-por-fusion` de docs/PENDIENTES.md
  recibe UNA linea aditiva mas: que el auditor remidio las tres cifras
  (par-resuelto WORK 29/29/1/0, par-resuelto en 9ef3705d 32/29, par-crudo
  en 7150339f 39) y que cuadran al digito con las tuyas. Es constancia de
  contraste, no correccion: nada se retracta.

- TAREA 3, EL TRABAJO. SON DOS, Y LA SEGUNDA ES LA GRANDE.
  (3.a) EL NODO QUE LE FALTA A OP-S-10. REGIMEN B, LAS TRES GUARDAS
  COMPLETAS (1.l). BLOQUEANTE Y VA PRIMERA.
  ANTES DE ESCRIBIR NADA, MIDELO TU con codigo propio: resuelve los 31
  ids del campo `nodos` de OP-S-10 por `ids_alias` de `dataset/nodos/`,
  quedate con los vivos distintos, y mira cuales NO nombran el pais en
  `condiciones_activacion`. MI CONTRASTE, MEDIDO HOY Y NO PARA COPIAR:
  31 ids resuelven a 29 vivos, y el unico sin cubrir es
  `prevenir_franquicias_inadvertidas`. SI TU MEDICION TE DA OTRA COSA,
  MANDA LA TUYA Y DECLARAS LA DISCREPANCIA, no la resuelves copiando.
  Sobre el que te salga, antepone la MISMA FORMA LITERAL de siempre,
  "Solo aplica si vendes o piensas vender franquicias en Estados Unidos",
  como PRIMERA condicion de activacion, con las viejas enteras y en su
  orden. Guardas propias ademas de las tres: ningun otro campo cambia,
  cero aristas movidas (verificar_aristas_vivas.py en PERDIDAS 0 y NUEVAS
  0), cero guiones largos y cero guiones medios. Detras, su bateria de
  1.d entera con etiqueta OPS10REP1.
  ANTES DE ESCRIBIRLO, LEELO ENTERO y comprueba que el contenido sostiene
  la condicion, como se comprobo en la 126 y en la 128. SI AL LEERLO
  CONCLUYES QUE NO LA SOSTIENE, NO LO ESCRIBAS: paras en ese, lo traes
  con su caso escrito, y sigues con la TAREA 3.b.
  Y DESPUES, MIDE LA VERIFICACION 1 OTRA VEZ Y PUBLICA LA CIFRA
  RESUELTA. Si te sale entera, DILO Y MARCALO COMO DISCUTIBLE: el cierre
  de OP-S-10 lo adjudico yo en el acta 129, no tu. NO LE CAMBIES EL
  ESTADO EN OPERACIONES.jsonl.
  (3.b) LA PRIMERA MITAD DE OP-S-11, LA QUE NO DECIDE NADA. REGIMEN A
  ESTRICTO: NO SE TOCA UN SOLO NODO NI UN SOLO FICHERO DE dataset/ EN
  ESTA TAREA. Si te descubres editando dataset/, es que te saliste.
  EL PORQUE, MEDIDO POR MI Y DECLARADO (acta 128, 3.3): la verificacion 1
  de OP-S-11 pide que el campo `fuente` "resuelva contra una lista
  CANONICA de libros", y el texto de la operacion dice que la tabla de
  mapeo "va DENTRO de ella". NO ESTA. docs/plan/RECORTE_POSICIONAL.md
  tiene el total 55, dos casos probados (Hugos 2 grafias, Horowitz 3) y
  una tabla de seis libros con conteos; la correspondencia de las 129
  grafias a los 55 libros no esta escrita en ningun sitio, y mi `grep
  -rln` sobre docs/ no la encuentra. VERIFICALO TU ANTES DE NADA, y si la
  encuentras donde yo no mire, DILO Y USALA: manda tu medicion.
  LO QUE SE HACE, y es medir y proponer, no decidir:
    (i) Escribe scripts/loop/vuelta129_censo_fuente.py, que sobre los
    nodos VIVOS de hoy extraiga el campo `fuente`, separe las
    declaraciones (di en el propio script COMO las separas y por que ese
    separador, leido de los datos y no supuesto), y saque el censo de
    GRAFIAS DISTINTAS EN PRIMERA POSICION con su recuento. Salida a
    docs/loop/SALIDA_V129_3B_CENSO_FUENTE.txt. PUBLICA LA CIFRA QUE TE
    SALGA, sea 129 o no: la de 129 es del 11 ago 2026 y el catalogo se
    ha movido desde entonces (fusiones, deprecados), asi que si difiere
    NO ES UN ERROR, ES EL CORTE NUEVO, y se declara como tal con los dos
    cortes escritos.
    (ii) Sobre ese censo, agrupa MECANICAMENTE y solo lo mecanico: las
    grafias TRUNCADAS (una es prefijo estricto de otra, que es el patron
    que la operacion documenta) y las que solo difieren en espacios,
    mayusculas o puntuacion final. Cada grupo con su candidata a canonica
    (la mas larga del grupo) y el recuento de cada miembro. Salida a
    docs/loop/SALIDA_V129_3B_GRUPOS_MECANICOS.txt.
    (iii) LO QUE NO AGRUPE MECANICAMENTE SE LISTA APARTE Y NO SE TOCA:
    docs/loop/SALIDA_V129_3B_SIN_AGRUPAR.txt, una linea por grafia con su
    recuento. Esas son las que piden decision, y la decision es mia.
    (iv) Escribe la TABLA PROPUESTA en un fichero NUEVO,
    docs/plan/OP_S_11_MAPEO_PROPUESTO.md, aditivo puro (fichero nuevo, no
    toca ninguno viejo), con tres columnas: grafia, canonica propuesta,
    motivo (mecanico y cual, o SIN AGRUPAR). Y en su cabecera, con estas
    palabras: que es una PROPUESTA MEDIDA, que NO se ha aplicado a ningun
    nodo, y que la adjudica el auditor. NO cambies el estado de OP-S-11.
    (v) LOS DOS CASOS PROBADOS DE LA OPERACION, REMEDIDOS: Hugos (2
    grafias, 23 sin normalizar contra 21 canonico) y Horowitz (3 grafias,
    16 contra 14). Mide los cuatro numeros HOY y ponlos al lado de los
    del 11 ago 2026, cada uno con su corte. Si difieren, es el corte
    nuevo y se declara; no se copia el viejo.
  Y SI AL MEDIR CONCLUYES QUE NI SIQUIERA PROPONER LA TABLA SE PUEDE SIN
  DECIDIR, PARAS EN 3.b, LO TRAES ESCRITO CON SU CASO, Y ENTREGAS LA
  VUELTA CON 3.a HECHA. Eso no es fracasar: es la letra de AUDITOR.md
  seccion 3, y para eso esta escrita.
  (3.c) LO QUE NO SE TOCA ESTA VUELTA, DICHO PARA QUE NO HAYA DUDA:
  OP-S-12 NO SE ABRE. Va al final de la pasada entera, no al final de su
  fase, por la atadura 2 de docs/plan/00_INDICE.md ("OP-S-12 va AL FINAL,
  despues de la ultima fusion, porque cada fusion fabrica sus
  duplicadas"). Y LA FASE 05 NO SE DECLARA CERRADA POR NADIE ESTA VUELTA:
  cuando quede cerrada y verificada se dispara la condicion de parada
  CIERRE DE LA FASE 05 de AUDITOR.md seccion 4, que es del fundador, y
  esa la disparo yo en mi acta, no tu en tu reporte. MARCALO COMO
  DISCUTIBLE si con 3.a y 3.b hechas la fase queda a una sola operacion
  con trabajo (OP-S-11) mas OP-S-12 remitida al final, para que yo
  adjudique si cierra CON REMISION como cerraron la fase 03 y la fase 04.

Y UNA COSA MAS, QUE ES DE LA CASA: COMMITEA POR TRAMO, Y AHORA TAMBIEN
PUSHEA POR TRAMO, con la regla compuesta delante: el bloque de apertura
va en UN commit y NO se pushea solo; en cuanto la guarda nueva de 1.h
este escrita y verde, commit y push; detras de 3.a verde, commit y push;
detras de cada salida de 3.b, commit y push. Tres vueltas de esta
campana (81, 114, 127) se perdieron por no hacerlo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
