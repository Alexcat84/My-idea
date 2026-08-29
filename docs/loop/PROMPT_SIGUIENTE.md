Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

Esta es la VUELTA 125. El acta de la 124 esta escrita
(docs/loop/ACTA_AUDITOR.md, al final). Lo que dice, en corto: EL SUELO DE
LA 124 ESTA CUMPLIDO AL DIGITO. Conte por mi cuenta las 28 familias, los
51 pares y la cobertura de los dos registros (51 unicos, faltan cero,
sobran cero); las diez filas de la cabecera me salen identicas; mi Gate 0
sale byte a byte igual al tuyo; el cmp de las siete baterias coincide con
el tuyo Y ESTA VEZ EL REPORTE LO DECLARA, asi que la caida 4.1 de la 123
queda remediada; y las dos guardas nuevas (el ensanche de
verificar_cifras_del_plan.py y verificar_titulos_normalizados.py) pasan
CINCO mutaciones mias, incluida la que reproduce el agujero exacto que yo
mismo habia dejado en la 123. Tu censo de titulos (3.188 vivos, 0
exactos, 1 normalizado) coincide con el mio medido con otro codigo.

LO QUE ESTA VUELTA COBRA:

  UNA CAIDA DE REPORTE QUE NO ACUMULA (acta 124, 4.1): los "~61 nodos
  vivos". Medido por mi: los ids VIVOS de la nomina con sufijo numerico
  son 27, y en el grafo vivo entero son 49. Ninguno es 61. El 61 es 67
  menos los 6 nodos de las tres fusiones, o sea "el resto de la nomina",
  que es el alcance de un RENOMBRE_CON_ALIAS entero y no lo que esa
  clausula pide. Vive solo en el reporte y en prosa: se registra con su
  nombre, dispara la relectura al doble, y NO acumula (letra del 27 ago).

  UNA CAIDA MIA, DE ENCARGO (acta 124, 4.2): dicte DOS VARAS para el
  mismo acto. La TAREA 2 pedia medir las correcciones de docs/plan/ con
  numstat y borrados en cero; la TAREA 3 abria con "las tres guardas de
  todo instrumento que escriba en dataset/ o en docs/plan/". Tu escribiste
  la correccion de OP-S-09 bajo el regimen de la TAREA 2, igual que la
  123, que mi propia acta dio por buena. La practica de la casa es la de
  la TAREA 2 y la letra que sobra es la mia. Queda separada abajo, en
  1.j, y no se te cuenta.

DOS DISCREPANCIAS DE MI RELECTURA CIEGA, Y NO SE COBRAN: VAN A RELECTURA
CONJUNTA (AUDITOR.md 1.3, precedente del acta 110). Son la TAREA 3.a y
son BLOQUEANTES: hasta que se cierren, OP-S-09 no se ejecuta.

EL TRAMO QUE SE RELEE AL DOBLE ESTA VUELTA (acta 124 seccion 5), y hoy se
aplica por la regla dura y no por prudencia: mi discrepancia de clase
sobre auditoria_de_producto CAE FUERA de los discutibles que el reporte
marco. Siguen vivos el tramo de la 120 con sus ramales (i) NINGUNA
MEDICION SE ATRIBUYE A UN ESTADO QUE NO ES EL SUYO, (ii) EL EXPEDIENTE NO
PUEDE DECIR MAS QUE EL REGISTRO ESCRITO A SU LADO, (iii) NINGUNA GUARDA
SE ESTRECHA EN SILENCIO, (iv) TODA CIFRA SOBRE UN ARTEFACTO CONTABLE SE
LEE DE LA SALIDA DEL INSTRUMENTO PEGADA AL LADO, y el (v) de la 123
NINGUNA VARA SE ESTRECHA EN EL ENCARGO. Le anado el sexto, que sale de la
discrepancia 2.3:
  (vi) UN SUPERVIVIENTE SE RAZONA COMO SE RAZONA UNA CLASE. Si un
  registro declara el contenido EMPATADO, el superviviente lo decide el
  cableado MEDIDO (banco 9.8), y la medicion va escrita en la razon, con
  sus dos cifras. Una razon que sostiene la clase y calla el superviviente
  deja media decision sin vara, y la mitad callada es la que mata un id.

Nota de formato: AUDITOR.md 1.4 pone TAREA 1 registros y TAREA 2 trabajo;
la casa viene escribiendo TAREA 1 guardas, TAREA 2 registros, TAREA 3
trabajo, y lo mantengo porque las guardas son bloqueantes y van delante.

- TAREA 1, LAS GUARDAS MECANICAS. BLOQUEANTE, Y LA PRIMERA PARTE VA ANTES
  DE TOCAR NADA MAS.
  (1.a) EL SELLO DE APERTURA, AHORA MISMO, ANTES DE LA PRIMERA OPERACION:
  git rev-parse HEAD, hash completo de 40 caracteres, UNA linea, a
  docs/loop/SALIDA_V125_HEAD_APERTURA.txt. Al terminar la ultima operacion
  y ANTES de escribir el reporte, el gemelo:
  docs/loop/SALIDA_V125_HEAD_CIERRE.txt. Comprobacion:
  python scripts/loop/verificar_apertura_sellada.py --vuelta 125 tiene que
  dar VERDE EXIT 0, y su salida se cita en el reporte. La 121, la 122, la
  123 y la 124 lo hicieron bien las cuatro; se repite igual.
  (1.b) LOS NOMBRES CANONICOS DE LAS SALIDAS DE APERTURA Y DE CIERRE, con
  <LADO> = APERTURA o CIERRE, exactamente estos siete:
    docs/loop/SALIDA_V125_GATE0_CMD1_<LADO>.txt   (scripts/run_phase1.py --reaplico-curaduria, entera)
    docs/loop/SALIDA_V125_CONTEO_<LADO>.txt       (scripts/loop/vuelta83_conteo_aristas.py WORK)
    docs/loop/SALIDA_V125_MOTOR_<LADO>.txt        (python engine/run_all_tests.py)
    docs/loop/SALIDA_V125_WEB_<LADO>.txt          (cd web y npx vitest run)
    docs/loop/SALIDA_V125_TSC_<LADO>.txt          (cd web y npx tsc --noEmit, cerrada con la linea literal EXIT=<n>)
    docs/loop/SALIDA_V125_DESFASE_CALIBRADO_<LADO>.txt (scripts/loop/vuelta85_medir_desfase_calibrado.py WORK)
    docs/loop/SALIDA_V125_MARCADOR_<LADO>.txt     (scripts/recomputar_marcador.py 3388)
  El formato del tsc es EXIT=<n> sin dos puntos y sin espacio, y sigue
  prohibido el fichero de cero bytes.
  (1.c) EL CICLO DE TRES, IGUAL QUE LA 124. NINGUNA salida de guarda se
  captura mientras el ciclo este a medias. El ciclo es run_phase1.py
  --reaplico-curaduria, luego etiquetas_de_cara.py --aplicar, luego
  sync_assets_web.py, EN ESE ORDEN, y solo cuando git diff --numstat sobre
  dataset/, web/ y engine/ este en CERO se empieza a medir. Por cada
  corrida se escribe docs/loop/SALIDA_V125_CICLO_<ETIQUETA>_NUMSTAT.txt
  con la salida literal y una linea final "EXITCODE: N". AVISO MEDIDO POR
  MI HOY: etiquetas_de_cara.py --aplicar mueve 71 etiquetas cada vez que
  run_phase1.py pasa antes, asi que el ciclo NO converge en la primera
  corrida y eso es normal; lo que no es normal es medir antes de que
  converja.
  (1.d) LA BATERIA POR OPERACION, EN SU PROPIO CHECKPOINT, Y CON SU
  COMPROBACION MECANICA. Se escribe la operacion N, se corre su ciclo de
  tres entero, se miden sus cuatro salidas, Y SOLO ENTONCES empieza la
  N+1. Ficheros, con <OP> = OPS09, OPS10, etc.:
    docs/loop/SALIDA_V125_<OP>_GATE0_POST.txt
    docs/loop/SALIDA_V125_<OP>_MOTOR_POST.txt
    docs/loop/SALIDA_V125_<OP>_WEB_POST.txt
    docs/loop/SALIDA_V125_<OP>_TSC_POST.txt
  mas las de etiquetas y sync del ciclo con el mismo prefijo. Antes de
  escribir el reporte corres cmp -s sobre CADA par de salidas homologas de
  la vuelta (apertura contra cierre, y cada bateria contra la anterior),
  vuelcas el resultado literal a docs/loop/SALIDA_V125_BATERIAS_CMP.txt
  con una linea por par que diga IDENTICOS o DISTINTOS, y EL REPORTE LISTA
  LOS IDENTICOS Y EXPLICA POR QUE LO SON, con el numstat que lo prueba
  citado al lado. La 124 lo hizo bien: se repite igual. OJO, QUE ESTA
  VUELTA SI ESCRIBE EN dataset/: si Gate 0 o el conteo salen IDENTICOS
  entre la apertura y el cierre DESPUES de ejecutar OP-S-09, eso NO es
  determinismo legitimo, es senal de que la escritura no llego; se
  investiga y se declara antes de publicar nada.
  (1.e) LAS GUARDAS DE CITAS Y DE TITULOS NO SE TOCAN. Se corren
  verificar_citas_del_reporte.py, verificar_titulos_normalizados.py y sus
  autopruebas (vuelta122_tarea1e_mutacion_citas.py,
  vuelta123_tarea1e_mutacion_fila_tabla.py, y
  verificar_titulos_normalizados.py --autoprueba), y se pegan. NO se
  modifica ninguna de las dos. AVISO: si OP-S-09 deprecara algun nodo del
  par sistema_responsabilidad_gerencial (no lo hace: quedo CONTINUA), la
  excepcion declarada del script habria que revisarla; como no lo hace, la
  excepcion se queda EXACTAMENTE como esta.
  (1.f) LA GUARDA DE CIFRAS DEL PLAN, TAMPOCO SE TOCA. Se corre
  verificar_cifras_del_plan.py y sus dos casos positivos
  (vuelta123_tarea1f_caso_positivo.py y
  vuelta124_tarea1f_caso_positivo_ventana.py). Los tres verdes o rojos
  donde tocaba, pegados. La probe por mutacion propia y muerde: no se
  ensancha ni se recorta esta vuelta.
  (1.g) LA GUARDA NUEVA DE LA FUSION, Y ES DE ESTA VUELTA. BLOQUEANTE.
  Escribe scripts/loop/verificar_fusion_ops09.py con este contrato, que se
  corre DESPUES de ejecutar OP-S-09 y cuya salida se pega:
    - Lee dataset/metadata/master_graph.json y, por cada par REPITE
      ejecutado, comprueba: (1) el id que muere esta DEPRECADO; (2) el id
      que muere aparece en ids_alias del superviviente; (3) el
      superviviente sigue VIVO; (4) CERO nodos vivos conservan una arista
      que apunte a un id muerto sin que el resolutor la lleve al
      superviviente; (5) cero auto-aristas y cero duplicadas en las listas
      de los nodos tocados.
    - ROJO EXIT 1 nombrando el par y la comprobacion que falla; VERDE
      EXIT 0 con el recuento de pares comprobados.
    - CASO POSITIVO POR MUTACION, en memoria y sin tocar disco: sobre una
      copia del grafo se borra el alias de uno de los muertos y tiene que
      dar ROJO nombrandolo. Pegalo.
  (1.h) ANTES DEL COMMIT DEL REPORTE, LAS CUATRO COMPROBACIONES, y las
  cuatro salidas se pegan:
    python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 125 --comparar docs/loop/REPORTE.md
    python scripts/loop/verificar_citas_del_reporte.py
    python scripts/loop/verificar_cifras_del_plan.py
    python scripts/loop/verificar_titulos_normalizados.py
  La primera tiene que dar CABECERA IDENTICA AL TALLADOR y las otras tres
  VERDE EXIT 0.
  (1.i) EL TOPE DEL REPORTE SE CUMPLE Y SE MIDE. wc -l docs/loop/REPORTE.md
  tiene que dar 80 o menos y esa cifra se escribe en el propio reporte,
  medida. La 124 lo cumplio en 34.
  (1.j) LOS DOS REGIMENES DE ESCRITURA, SEPARADOS POR ESCRITO, QUE ES LA
  CORRECCION DE MI CAIDA 4.2. A partir de esta vuelta y hasta que alguien
  la cambie:
    - REGIMEN A, TEXTO: un instrumento que solo anade TEXTO a docs/plan/ o
      a docs/ (correcciones declaradas, notas, fichas) se mide con
      git diff --numstat y con grep -c "^-[^-]" sobre el diff en cero, mas
      git diff --word-diff=porcelain pegado si toca una linea vieja. NO
      necesita las tres guardas.
    - REGIMEN B, DATO: un instrumento que escribe en dataset/, o que
      EJECUTA una operacion (deprecar, fundir, renombrar, mover aristas,
      cambiar campos de nodos), lleva LAS TRES GUARDAS COMPLETAS: (i)
      SIMULACION PREVIA sobre copia en memoria con su salida pegada, (ii)
      SU MUTACION NEGATIVA corrida y pegada, y (iii) SU ROJO REAL EN
      SEGUNDA PASADA, con la salida de git status --porcelain PEGADA
      DETRAS TAL CUAL SALGA, no descrita. Un instrumento de REGIMEN B sin
      las tres NO SE CORRE.
    - EL REPORTE DICE, POR CADA INSTRUMENTO QUE ESCRIBIO, BAJO QUE REGIMEN
      FUE. Un instrumento sin regimen declarado no existe para el
      expediente.

- TAREA 2, LOS REGISTROS Y CORRECCIONES DEL ACTA 124. REGIMEN A. Aditivos
  puros donde toquen texto viejo, medidos con git diff --numstat y con
  grep -c "^-[^-]" sobre el diff en cero. Son tres y el orden da igual.
  (2.a) LA ADJUDICACION DEL DISCUTIBLE MAYOR, EN LA PROPIA OPERACION (acta
  124, seccion 3.2). En docs/plan/OPERACIONES.jsonl, DOS escrituras
  aditivas sobre la fila de OP-S-09:
    - En el campo verificacion, en su CUARTA linea ("ningun id vivo lleva
      sufijo numerico de duplicado"), una correccion declarada EN LINEA,
      con el mismo formato que ya usa OP-S-01 en su cuarto punto (el
      " | CORRECCION DECLARADA (fecha, quien, cita): ..."). Dice: que el
      punto SE ACOTA A LA NOMINA de esta operacion, por extension citable
      de la decision del fundador del 28 ago 2026
      (docs/loop/paradas/2026-08-28-titulo-nafta-ops01-DECISION.md, punto
      2), que acoto una clausula de la misma forma exacta en OP-S-01 y
      mando el barrido global a una ficha de PENDIENTES.md; que quien es
      duplicado lo decide la lectura continua-o-repite de MESA_RACIMOS.md
      DECISION 4 y no la forma del id, luego un nodo CONTINUA no es un
      duplicado y su sufijo no es "sufijo numerico de duplicado"; y que el
      unico residuo (un id vivo cuyo sufijo nombre a un gemelo recien
      muerto) queda anotado como trabajo post campana en la ficha, porque
      elegir su id nuevo es juicio editorial sin regla escrita que lo
      derive.
    - En el campo nota, al final, la correccion declarada larga con las
      CIFRAS QUE TU MIDAS, no las mias: cuantos ids VIVOS de la nomina
      llevan sufijo numerico, cuantos hay en el grafo vivo entero, y
      cuantos de los de la nomina quedan resueltos por su veredicto
      CONTINUA. MIDELO TU con codigo propio antes de escribirlo y pega la
      salida. Mi medicion, para contraste y NO para copiar: 27 en la
      nomina, 49 en el grafo entero, y 25 de los 27 resueltos por CONTINUA
      (los dos que no son eliminacion_causas_error_4 y dia_cero_defectos_2,
      y de esos dos solo el primero queda como residuo, porque el sufijo
      de dia_cero_defectos_2 distingue a dos nodos VIVOS). Si tu medicion
      discrepa de la mia, LA DECLARAS, no la resuelves copiando.
  (2.b) EL REGISTRO LARGO DE LAS CAIDAS Y LAS DISCREPANCIAS, en
  docs/PENDIENTES.md, seccion nueva R.7 de la vuelta 124, como
  correcciones declaradas: (1) la caida de reporte de los "~61 nodos
  vivos", con las dos cifras reales que midas en 2.a y la explicacion de
  de donde salia el 61; (2) la caida MIA de las dos varas para el mismo
  acto, que dice con todas sus letras QUE ES DEL AUDITOR y cita el nuevo
  1.j que la remedia; (3) las dos discrepancias abiertas de la relectura
  ciega, con su estado (abiertas al escribirlas, cerradas por la TAREA 3.a
  de esta misma vuelta) y su desenlace medido.
  (2.c) LA OCTAVA ENTRADA DE LA FICHA campos-sucios-dataset, en
  docs/PENDIENTES.md, aditiva: el residuo de sufijos que esta campana NO
  toca. Que la clausula del sufijo numerico queda acotada a la nomina por
  2.a; cuantos ids vivos CON sufijo numerico quedan FUERA de la nomina
  (mide tu; mi contraste es 22, que es 49 menos 27); que el unico id
  dentro de la nomina cuyo sufijo nombra a un gemelo muerto tras la fusion
  queda tambien anotado; y que el arreglo de todos ellos es trabajo POST
  CAMPANA porque exige una regla de nomenclatura que hoy NO EXISTE en
  ninguna pagina del repo, y crear doctrina no lo decide el bucle. NO
  RENOMBRES NADA.

- TAREA 3, EL TRABAJO: CERRAR OP-S-09 DE VERDAD.
  (3.a) LA RELECTURA CONJUNTA DE MIS DOS DISCREPANCIAS. BLOQUEANTE Y VA
  PRIMERA: hasta cerrarla, la ejecucion no empieza, porque cualquiera de
  las dos cambia lo que se ejecuta. Metodo: relees los nodos contra el
  grafo de HOY, decides TU con la vara, y escribes el resultado en
  docs/loop/SALIDA_V125_OPS09_RELECTURA_CONJUNTA.jsonl, una fila por
  discrepancia, con los campos: par, mi_clase_auditor, tu_clase, veredicto
  final, superviviente si aplica, alias que hereda, la vara citada con su
  fichero y su linea, y la razon en una linea. Si mantienes tu lectura, la
  razon tiene que citar la vara que la sostiene, no repetir la anterior.
    - DISCREPANCIA 1, DE CLASE: auditoria_de_producto contra
      auditoria_producto. Mi caso, con los campos delante: los cuatro
      pasos de auditoria_producto caen uno a uno dentro de los siete de
      auditoria_de_producto (proposito contra especificacion o necesidad
      del usuario = su paso 1; etapa fabrica/distribuidor/campo = su paso
      2; muestreo = su paso 3; validar que lo auditado sea lo que le
      importa al cliente = su paso 5) y no aporta ni un paso que el otro
      no tenga; la salvacion por "otro momento" se cae porque el propio
      auditoria_de_producto dice "La haces en distintos momentos del
      recorrido del producto: en fabrica, en el distribuidor, en el
      servicio o ya en manos del cliente"; y el unico proposito que anade,
      "evaluar la efectividad de las decisiones de inspeccion", es
      literalmente el del nodo hermano auditoria_de_producto_2, que vive y
      quedo CONTINUA. Cableado medido por mi: 8 contra 1. Tu razon escrita
      fue mecanismo contra proposito, y es defendible: por eso esto es
      relectura conjunta y no una correccion dictada. LEELO TU Y DECIDE
      TU. Si sale REPITE, entra en la ejecucion de 3.b con su
      superviviente razonado por el ramal (vi).
    - DISCREPANCIA 2, DE SUPERVIVIENTE: estrategia_de_innovacion_de_producto
      contra estrategia_innovacion_producto. La CLASE la adjudico a tu
      favor: REPITE, y te doy la razon contra mi propio aviso de la 123.
      Lo que discrepo es el superviviente. Tu razon escribe "aqui el
      contenido esta empatado"; el banco 9.8 dice "A contenido empatado,
      DESEMPATA EL GRAFO. Sobrevive el mejor cableado"; y la CUARTA linea
      del campo verificacion de la propia OP-S-09 repite la regla dentro
      de la operacion ("las 53 familias resueltas por continua o repite, y
      a contenido empatado desempata el grafo"). Cableado medido por mi
      hoy, solo vecinos VIVOS y entrantes reales:
      estrategia_innovacion_producto 14 (6 salientes, 8 entrantes) contra
      estrategia_de_innovacion_de_producto 7 (6 salientes, 1 entrante).
      MIDELO TU con codigo propio y pega la salida. Si tu medicion
      confirma el desempate, el superviviente pasa a ser
      estrategia_innovacion_producto y el alias lo hereda
      estrategia_de_innovacion_de_producto, y entonces la nota de OP-S-09
      lleva CORRECCION DECLARADA (la que ya escribiste en la 124 nombra al
      otro superviviente, y esa cifra vive en docs/plan/: se corrige por
      remision, sin borrar una letra). Si sostienes tu eleccion, tiene que
      ser con una vara escrita que gane al 9.8, o declarando que el
      contenido NO estaba empatado y diciendo que trae uno que el otro no
      tiene. Comprobado por mi: ninguna otra operacion abre esos ids en
      nodos, eliminar ni preservar (OP-E-03 solo los nombra en evidencia),
      asi que el toque unico del banco 9.4 no se rompe en ninguna de las
      dos direcciones.
  (3.b) LA EJECUCION DE OP-S-09. REGIMEN B, LAS TRES GUARDAS COMPLETAS
  (1.j). Se ejecuta con los 51 pares leidos y con 3.a cerrada. Contenido:
  las fusiones REPITE resueltas (las dos de la 123, la de la 124 con el
  superviviente que 3.a deje firme, y la de auditoria si 3.a la mueve),
  cada una con alias para el id que muere (verificacion 1 de la fila), con
  las aristas que apuntaban al id viejo resolviendo detras (verificacion
  2), con cero duplicadas y cero auto-aristas despues, y con Gate 0 y las
  suites en verde en su propio checkpoint (1.d) y la guarda nueva 1.g en
  VERDE. La verificacion 4 (sufijo numerico) queda cumplida por la
  adjudicacion de 2.a y se cita asi en el reporte, no se declara cumplida
  a secas.
  SI ALGUN PAR NO SE PUEDE RESOLVER SIN DECIDIR ALGO QUE NINGUNA REGLA
  ESCRITA CUBRE, PARAS EN ESE PAR, LO TRAES CON SU CASO ESCRITO Y SIGUES
  CON LOS DEMAS. Y si la ejecucion no cabe con sus tres guardas enteras,
  eso es entrega completa y no un limite de alcance: pasa a la 126 y el
  reporte publica LA CUENTA DE GUARDAS consumidas, guarda por guarda con
  su fichero.
  (3.c) SI Y SOLO SI OP-S-09 CIERRA ENTERA: OP-S-10 (orden 9,
  REENCUADRE_DE_MARCO, 31 nodos en el campo nodos). NO SE ESCRIBE NADA DE
  ELLA ESTA VUELTA: solo se REMIDE su nomina contra el grafo de hoy
  (cuantos de los 31 siguen vivos, cuantos deprecados, y a quien reclama
  el alias de cada deprecado), y se publica. Y REMIDE TAMBIEN, por el
  ramal (v), si la cifra 31 del campo nodos coincide con lo que la nota de
  la fila dice de si misma; si no coincide, lo declaras y no lo resuelves
  copiando. OP-S-11 y OP-S-12 no se abren.
  Y AVISO OTRA VEZ, PORQUE FALTAN POCAS: cuando la fase 05 quede cerrada y
  verificada se dispara la condicion de parada CIERRE DE LA FASE 05 de
  AUDITOR.md seccion 4. Quedan OP-S-09, OP-S-10, OP-S-11 y OP-S-12. NO
  declares la fase cerrada tu: mide, publica y dilo como discutible; el
  cierre lo adjudica el auditor.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
