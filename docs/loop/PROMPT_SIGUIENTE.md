Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), en REGIMEN COMPLETO, con las
guardas obligatorias por operacion.

TU VUELTA ES LA 160. El acta que te abre es la 159. Va en la cabecera fija
por la adjudicacion 6.1 del acta 158, y no es cosmetico: las dos guardas
del cierre (tallar_cabecera_reporte.py y verificar_apertura_sellada.py)
localizan la apertura buscando el acta de la vuelta N menos 1, y el
invariante de la casa es ACTA N, VUELTA N MAS 1. Tus ficheros de esta
vuelta se llaman SALIDA_V160_*.

HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA: NINGUNO. No hay commit de
decision del fundador que admitir. Todo commit dentro del corredor es tuyo
y cuenta como intruso.

Y EL SELLO DE APERTURA VA EN EL PRIMER COMMIT DEL CORREDOR, NO EN EL
CIERRE. En la 159 lo hiciste bien: los diez SALIDA_V159_*_APERTURA.txt
nacieron todos en 9a0ae9d7, hijo directo del acta, y lo verifique yo
corriendo la guarda. Repitelo igual.

El acta que te encarga esto es ACTA_AUDITOR.md, VUELTA 159. Su veredicto:
las nueve tareas entregadas y TODO el cierre reproduce al digito con mi
propia mano (censo 3.853/3.169/684, aristas 8.780/8.740/17.520/9.914 con
solo_sig 1174 y solo_prev 1134 y cero auto enlaces, ciclo entero con
numstat en cero filas, Gate 0 en 26 de 26 y ademas IDENTICO al tuyo linea
por linea, motor 25/25, vitest 80 y 1.030 con 3 saltadas desde web/, tsc
exit 0 sin una linea, archivo 3.388 con A 551 B 72 C 5 D 2.760 y cero
huecos y cero duplicados, registro 154 con LECTURA_DIRIGIDA C 18 y D 104 y
CRIBADO B 1 y D 31, citas de lectura dirigida 122 con rastro 106 y cero en
la forma vieja de la 156, expediente 71/36/24/12/0/7, fase 03 16/12/4 con
sus cuatro nombradas, fase 06 16/16/0, fase 08 con OP-V-01, fase 09 3/0/3,
y la bateria de las 23 VERDE en corrida sola por mi mano con RUIDO DE
CONCURRENCIA 0). Tu aditividad la medi yo contra el commit del acta: 154
lineas a 154, cero pares perdidos y cero nuevos, 120 razones ampliadas con
PREFIJO ROTO 0, 43 clases movidas (41 de C a D y 2 de D a C), 106 citas
cambiadas, ninguna a A, y CERO borrados en los veintiun .py de tu TAREA 1.
Tus dos nominas, la de 41 y la de 53, las recompute desde git y salen
IDENTICAS a las tuyas elemento a elemento.

TU PARADA DE LA TAREA 5 ERA CORRECTA Y LA CIFRA MALA ERA LA MIA. Lo medi
en dos arboles distintos, el del commit del acta 158 y HEAD, y los dos dan
4 / 12 / 14 ficheros y 3 / 7 / 7 en la bateria: el once nunca fue cierto.
Ademas lei entero vuelta89_tarea4_guarda_op_c05.py y confirme que lleva
las dos anclas de la 6.7. Hiciste las tres cosas que importaban: paraste
por mandato literal, no tocaste un solo check, y nombraste el residuo. La
caida de cifra queda registrada con MI nombre en la seccion 2 del acta.

PERO MI CIEGA TRAE UNA DISCREPANCIA FUERA DE TUS DOCE DISCUTIBLES, Y POR
ESO EL CREDITO DE LA TANDA BAJA OTRA VEZ. Lei 29 casos a ciegas (sellados
en docs/loop/_auditor_v159_mis_adjudicaciones.txt, sha1 d7eefaca,
calculado antes de destapar): coincidimos en 27. Dentro de lo marcado
discrepo en uno, LD-OPC05-004, y ahi TE DOY LA RAZON A TI: tu razon ya
nombraba el par que a mi me convencio y lo descartaba con motivo escrito.
Fuera de lo marcado discrepo en UNO, LD-OPC05-100, y ese no lo habia
avisado nadie. La regla es literal: baja el credito de la tanda y el tramo
se relee al doble. Va encargado en la TAREA 2 y es bloqueante.

Y TE DIGO ESTO ANTES DE LAS TAREAS PORQUE TIENES QUE SABERLO AL LEER:
LA RACHA DE CIFRA PUBLICADA ESTA EN UNO. La LD-OPC05-005 se confirmo en tu
relectura conjunta, o sea que la D de la tanda 157 era caida de CLASE y
entra en la racha, como el acta 158 se comprometio a registrar. Si la
relectura conjunta de la TAREA 2.a confirma mi lectura de la 100, seran
DOS TANDAS SEGUIDAS y el bucle se para por la regla del credito. NO
QUIERO QUE ESO TE INCLINE LA LECTURA EN NINGUNA DIRECCION: mide contra los
nodos y publica lo que midas, incluso contra mi, que es lo que hiciste con
la 097 y con la 005. Una parada honesta vale mas que una C sostenida por
conveniencia.

- TAREA 1, LOS REGISTROS, Y ES LO PRIMERO: deja escritas en el repo las
  ocho adjudicaciones de la seccion 6 del acta 159 donde cada una vive
  (6.1 en los DOCE .py del alcance del patron de P.16, que son los mismos
  doce que la TAREA 1 de la 159 ya toco, y ahi la letra es que el alcance
  son DOCE y que la vara es la lectura B; 6.2 y 6.3 en la razon de
  LD-OPC05-004 y LD-OPC05-100 del registro; 6.4 en el instrumento de
  lectura del lote; 6.5 en scripts/loop/vuelta152_registro_de_citas_opc05.py,
  que es donde vive la doctrina de vias y clases, y en el instrumento del
  lote 2; 6.6 en la funcion de la P3b de
  scripts/loop/vuelta150_3_relectura_expediente.py; 6.7 en el instrumento
  del lote; 6.8 en scripts/loop/vuelta159_tarea9_marcador_cierre.py),
  TODAS POR ADICION Y CON CORRECCION DECLARADA, sin borrar una linea del
  texto viejo. Y la aditividad se MIDE, no se promete: numstat de git para
  los .py y prefijo comprobado por assert para el JSONL, como en la 156, la
  157 y la 159.

- TAREA 2, Y ES BLOQUEANTE, LA RELECTURA CONJUNTA Y EL TRAMO AL DOBLE.
  (2.a) LA UNA EN DISPUTA, POR LA 6.3. Mi caso escrito esta en la seccion
  3.2 del acta 159. LD-OPC05-100: concedo tu LINEA 2 (el paso 5 de
  proceso_ideacion, reducir a tres o cinco ideas y prototiparlas usando el
  lienzo, lo expanden los doce pasos de lienzo_modelo_negocio). Lo que no
  paso la vara es tu LINEA 1: el paso 2 de ideacion (realizar una fase de
  inmersion: investigar clientes, tecnologias y modelos de negocio
  existentes) NO procedimenta el paso 9 del lienzo (pausar para investigar
  mas informacion donde haya vacios importantes), porque es la misma orden
  con tres complementos, sin metodo ni instrumento ni secuencia. Es el
  caso de la 122: nombrar sin procedimentar. Y en tu propia 004 de la
  misma vuelta escribiste que UNA SOLA DIRECCION ES MADRE E HIJO. Verifica
  TU contra los nodos y decide con la vara, incluso contra mi, y publica lo
  que midas. Si sostienes la C, di QUE PROCEDIMIENTO del otro nodo expande
  el paso 9 del lienzo, no que linea lo repite. MI LECTURA NO ES LA VARA,
  EL NODO LO ES.
  (2.b) EL TRAMO AL DOBLE, POR LA 6.4: las 37 lecturas del lote 2 que
  nadie ha vuelto a mirar. La cuenta, para que la contrastes: el lote 2
  son 53; de esas relei yo hoy 16, que son los cinco marcados que caen
  dentro del lote (078, 081, 084, 103, 116) mas los once de mi muestra por
  computo (070, 075, 080, 085, 090, 095, 100, 105, 110, 115, 120); 53
  menos 16 da 37, de las cuales 8 estan hoy en C y 29 en D. TU INSTRUMENTO
  RECOMPUTA ESA NOMINA Y LA PUBLICA: si no da 37, paras y lo dices antes
  de leer nada. VAN LAS 37 ENTERAS, no solo las que cayeron a D, y el
  motivo esta escrito: la discrepancia que abrio la bajada, la 100, es una
  que SOSTUVO C, asi que restringir el tramo a las caidas dejaria fuera
  justo la especie que lo disparo. Segunda pasada independiente bajo la
  6.3 del acta 158.
  (2.c) Y DENTRO DE ESA MISMA PASADA, LA AUDITORIA DE CONSISTENCIA DE LA
  REGLA DE LA INSTANCIA, POR LA 6.5.b: en cada una de las 37, si la regla
  UNA INSTANCIA NO ES EL PROCEDIMIENTO DE SU CATEGORIA aplica, se dice; y
  si NO aplica pudiendo parecer que si, tambien se dice. Publica el conteo
  de las dos cosas. El riesgo de una regla nueva no es aplicarla mal una
  vez, es aplicarla solo cuando conviene.
  (2.d) LAS GUARDAS, LAS MISMAS Y NO SE AFLOJAN: cada cambio de clase con
  CORRECCION DECLARADA y el texto viejo entero como prefijo; n NO SE MUEVE
  y sigue en 3.388; assert de frontera con sha256 de dataset/ y conteo de
  censo y aristas antes y despues (el registro cambia, EL GRAFO NO); y
  Gate 0 corrido al terminar, con el ciclo entero y nunca run_phase1
  suelto.
  (2.e) Y EL LIMITE, QUE SIGUE VIGENTE DESDE LA 6.1 DEL ACTA 155: LA QUE
  SALGA A NO SE VOLTEA. Se marca como discutible, se publica su caso, y NO
  SE EJECUTA NINGUNA FUSION.

- TAREA 3, EL CHECK DE P.16, QUE ES TU TAREA 5 DE LA 159 DEVUELTA CON EL
  ALCANCE YA FIJADO, POR LA 6.1. El alcance es DOCE ficheros y la vara es
  la lectura B (pathspec que empieza por dataset/), la que tu publicaste
  como principal. La lectura estrecha de cuatro NO vale. Los doce ya estan
  medidos y nombrados en docs/loop/SALIDA_V159_T5_ALCANCE.txt, y el
  duodecimo, vuelta89_tarea4_guarda_op_c05.py, ENTRA: lei su fuente y
  lleva las dos anclas de la 6.7.
  (3.a) EL REMEDIO: huella de CONTENIDO tomada ANTES y DESPUES de las
  mutaciones dentro del propio script, y comparada consigo misma, en los
  DOCE.
  (3.b) CASO POSITIVO POR MUTACION: si una mutacion escribe de verdad en
  dataset/ o docs/plan/, el check SIGUE SALIENDO ROJO. Y la bateria entera
  se re corre SOLA despues, para ver que las 23 siguen siendo 23.
  (3.c) SI LOS DOCE NO CABEN CON SUS GUARDAS COMPLETAS, PARTELO Y DILO,
  nombrando cuales quedan: mejor seis medidos que doce prometidos.

- TAREA 4, EL INSTRUMENTO DEL MARCADOR DE CIERRE SE PARAMETRIZA, POR LA
  6.8, Y NACE DE UN HALLAZGO MIO SOBRE TU PROPIO REMEDIO. Confirmo primero
  lo tuyo: git log --all -S sobre la cabecera de
  SALIDA_V157_T9_MARCADOR_CIERRE.txt no devuelve nada en scripts/, ni vivo
  ni muerto, o sea que era de un solo uso y tu reporte lo dice bien. Pero
  vuelta159_tarea9_marcador_cierre.py imprime en su linea 52 "VUELTA 159,
  CIERRE: ..." literal, sin --vuelta y sin argparse: en esta vuelta o
  miente en su cabecera o nace otro instrumento de un solo uso, que es el
  defecto que vino a cerrar. Toma --vuelta, interpola el rotulo, por
  adicion y con correccion declarada, y correlo con --vuelta 160 en el
  cierre.

- TAREA 5, LA MARCA DE LA P3b, POR LA 6.6, Y ES CORTA. Las fichas de las
  dos salidas NO se reescriben: medi yo que las cuatro citas ya nombran a
  su productor (04_ENLACES.md:445 y OPERACIONES.jsonl:45 nombran
  verificar_cobertura_bolsa_tres_vias.py; OPERACIONES.jsonl:36 nombra
  verificar_fuente_canonico.py; PENDIENTES.md:6241 lo nombra dos lineas
  arriba en el mismo parentesis), CIFRA fichas que hay que reescribir: 0.
  Lo que si va, junto a la funcion de la P3b y por adicion: que EL ANGULO
  BARATO ERA LEER LA FICHA QUE CITA LA SALIDA, donde el productor llevaba
  meses escrito al lado. Ni el barrido de 998 .py de la 157 ni tus cuatro
  angulos de la 159 lo miraron. Esa leccion no esta en ningun sitio y es la
  que habria ahorrado dos vueltas. Recomputa tu esas cuatro citas antes de
  escribirlo: si no te dan cuatro, paras y lo dices.

- TAREA 6, LA PUERTA DEL CORREDOR NO PUEDE DECIR (no hallado) DE UN COMMIT
  QUE HALLO, POR LA 6.9, Y LA ENCONTRE PROBANDO MI PROPIO COMMIT DEL ACTA.
  Corri verificar_apertura_sellada.py --vuelta 160 antes de pushear, para
  probar que las guardas de tu vuelta encuentran el acta. La encuentran (lo
  comprobe llamando a commit_acta(160) directo: devuelve el hash y cero
  fallos), pero la primera linea que imprime dice COMMIT DEL ACTA (no
  hallado), y eso es falso. El motivo esta en el codigo: verificar() halla
  el acta en su linea 637, y cuando despues no hay ningun
  SALIDA_V160_*_APERTURA.txt sale por la salida temprana con
  return (fallos,) + vacio, cuyo ultimo hueco es None, y el main imprime
  ese None como (no hallado). La correccion declarada de la vuelta 156 que
  creo esas tuplas arreglo el ValueError y dejo pasar esta.
  (6.a) EL REMEDIO: las salidas tempranas llevan el acta que ya tienen en
  vez de un hueco, y si de verdad no se hallo, se dice. Por adicion y con
  correccion declarada, SIN tocar ningun veredicto.
  (6.b) CASO POSITIVO POR MUTACION: una corrida sin ficheros de apertura
  TIENE QUE SEGUIR SALIENDO ROJO, y ademas nombrar el commit del acta. Y
  una corrida en un estado donde el acta de verdad no exista tiene que
  seguir diciendo (no hallado).

- TAREA 7, EL CIERRE RECOMPUTADO AL CIERRE, con el ciclo entero en su
  orden (run_phase1 --reaplico-curaduria, etiquetas_de_cara --aplicar,
  sync_assets_web, y despues el numstat de dataset/ web/ engine/), NUNCA
  run_phase1 suelto, las tres suites (vitest DESDE web/), la cabecera
  tallada y comparada con --vuelta 160, el marcador con el instrumento ya
  parametrizado de la TAREA 4, y las guardas del cierre con su estado real
  aunque no te favorezcan. verificar_mutaciones_viejas.py se corre SOLA,
  SIN NADA AL LADO. Y el reporte con la regla que ya funciona: toda cifra
  que describa una salida va PEGADA de la salida.

- Y DESPUES, SEGUIR EL ORDEN ESCRITO EN MODO CONTINUO hasta el MURO
  CONOCIDO Y YA ADJUDICADO (acta 149, 3.10): la fase 08 no cierra sin una
  SESION CON CREDENCIAL Y CON EL FUNDADOR DELANTE. Medida hoy por mi, la
  fase 08 trae una operacion, una sin cumplir, OP-V-01, sin vara escrita.
  Ahi se para y se dice. Y corrijo tu conclusion de la seccion 14, que es
  lo unico que te discuto de fondo: EL SACO NO DEJA AL BUCLE SIN TRABAJO.
  La regla del credito acaba de abrir 37 segundas lecturas mas una
  relectura conjunta, y la 6.1 devuelve la TAREA 5 entera. Cuando eso se
  cierre volvemos a mirar si queda algo. EL MERGE NO SE PIDE NI SE HACE:
  es del fundador y solo suyo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
