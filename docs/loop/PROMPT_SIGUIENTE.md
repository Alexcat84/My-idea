Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), en REGIMEN COMPLETO, con las
guardas obligatorias por operacion.

TU VUELTA ES LA 165. El acta que te abre es la 164. Va en la cabecera fija
por el invariante de la casa, ACTA N Y VUELTA N MAS 1, del que cuelgan
tallar_cabecera_reporte.py y verificar_apertura_sellada.py. Tus ficheros se
llaman SALIDA_V165_*.

LA 164 ENTREGO ENTERA Y LA VERIFIQUE CON MIS INSTRUMENTOS. Marcador
3.388 / 551 / 72 / 5 / 2.760 con cero huecos y cero duplicados, censo
3.853 / 3.169 / 684, aristas 8.780 / 8.740 / 17.520 / 9.914, registro 154
filas con 13 en C y 109 en D de lectura dirigida y 110 citas con rastro,
contador de P.5.2 en 92 / 17 / 30 / 117 / 9, las once fases sumadas en
catalogo 82 con 36 cumplidas y 46 sin cumplir (44 sin vara escrita y 2 con
vara que mide), la cabecera identica al tallador en sus once filas, la
apertura VERDE con los diez nacidos en 28dde491 hijo directo del acta, y
el motor en 25/25. TODAS ESAS LAS RECOMPUTE YO HOY. Si alguna se te mueve,
se dice por que.

Y LA BATERIA LA CORRI ENTERA YO, QUE ES LO QUE EL ACTA 163 NO CONSIGUIO:
VERDE exit 0, 53 entradas, 92 arneses, ANCLA PERDIDA 0, NO MORDIO 0, NO
REPRODUCIBLE 0, CASO DECLARADO 2, y cero posteriores fuera al abrir y al
cierre. Tu veredicto reproduce entero. PERO SU RELOJ EN MI MAQUINA ES
OTRO: 1.193,1 segundos, 19,9 minutos, contra tus 978,2 y 16,3. Ya esta
rozando los veinte SIN un solo arnes nuevo dentro, y de ahi sale el limite
de la TAREA 4.

Y MI CIEGA COINCIDIO CONTIGO EN LAS DOS: la LD-OPC05-005 en D y la
LD-OPC05-101 en D, selladas antes de destapar tu razon (sha1
12da2ca8d0677a7755187b52eadd7be6c472046d). La caida de clase de la 005
queda CONFIRMADA por segunda pluma y la 101 la FIRMO, como dije que haria.
Y VAN MIS TRES CAIDAS DE HOY, que se registran igual que las tuyas: corri
run_phase1 SUELTO y casi publico un numstat de 72 filas que era artefacto
de haber cortado el ciclo; selle a ciegas un rechazo de TU camino en la
101 que el fichero desmiente, porque el paso 2 de search SI esta del lado
de la linea limpia y tu tenias razon; y corri la bateria con mi propio
trabajo al lado, y su comprobacion de RUIDO DE CONCURRENCIA me nombro DOCE
ficheros mios. La casa dice que la bateria SE CORRE SOLA y la guarda hizo
su trabajo. Corre la tuya sola.

LO MAS GORDO DE ESTA VUELTA NO ES TUYO Y ES POSTERIOR A TU REPORTE: EL
FUNDADOR CORRIO LA SESION CON CREDENCIAL Y CERRO LA FASE 08. Entre tu
commit de cierre (c59d111a) y el acta hay 32 commits suyos, sellados en
docs/loop/SELLO_SESION_CREDENCIAL_2026-09-03.md y en el asunto de
e966d896. MEDIDO POR MI: dataset/ NO se toco (cero filas de numstat
contra tu cierre), OP-V-01 pasa de LISTA a HECHA en OPERACIONES.jsonl, y
el indice semantico se rehizo con sha256 42223fcc. EL MURO CAYO Y NO POR
EL BUCLE.

HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA: NINGUNO. El acta 164
escribe su encargo en el mismo commit y los 32 del fundador son ANTERIORES
al acta, o sea que no estan en tu corredor. Todo commit entre el acta y tu
bloque de apertura es tuyo y cuenta como intruso.

Y NO TE ASUSTES CON LA M DE dataset/metadata/master_graph.json QUE TRAE
git status: la medi hoy y es fin de linea, no contenido. El blob del arbol
da cb33552aedddab4d6c51c5c85a7416999b5c70a0, el mismo que el indice, y el
numstat de dataset/ web/ engine/ da CERO FILAS. No la arregles y no la
commitees sola.

Y NO CORRAS run_phase1 SUELTO, QUE ES LA TRAMPA QUE PISE YO HOY: el ciclo
va ENTERO y en su orden (--reaplico-curaduria, etiquetas_de_cara
--aplicar, sync_assets_web, y despues el numstat). Cortado a la mitad da
72 filas de etiqueta_arbol que no son un movimiento del grafo.

LA VARA P.5.1 SIGUE CONGELADA Y NADIE LA TOCA: ninguna vuelta la estrecha
ni la ensancha sin correccion declarada del fundador.

- TAREA 1, LOS REGISTROS. ES BLOQUEANTE. El acta 164 y sus DIEZ
  adjudicaciones (6.1 a 6.10), registradas en la forma de la casa, en
  docs/PENDIENTES.md, con el numero COMPUTADO por
  scripts/loop/serie_de_registros.py y NUNCA tecleado (hoy la serie tiene
  25 entradas y el siguiente libre es R.34: eso lo recomputas tu, no lo
  copias de aqui). Y registra tambien, con su nombre, MIS DOS CAIDAS de la
  seccion 4 del acta, igual que hiciste con la de la 163. Idempotente y
  comprobado, como lo dejaste en la 164.

- TAREA 2, EL PUNTO CIEGO DEL CENSO DE ARNESES. ES BLOQUEANTE Y ES CODIGO
  (adjudicacion 6.3). El patron de verificar_mutaciones_viejas.py exige la
  palabra mutacion en el nombre del fichero. Medido por mi importando sus
  propias funciones: 92 arneses ve el censo, 53 entradas tiene la nomina,
  y DOS de esas 53 el censo NO LAS VE aunque existen en disco,
  vuelta144_3c_caso_positivo_1190.py y vuelta147_3e_simular_a26.py. La
  consecuencia no es cosmetica: arneses_que_faltan es quien produce el
  VERDE "NINGUN arnes posterior se queda fuera de la nomina", y ese verde
  SOLO cubre a los que se llamen mutacion. El dia que nazca uno llamado
  como esos dos, la guarda dira que no falta ninguno SIN HABERLO MIRADO.
  ARREGLALO EN LA FUENTE, y las dos salidas valen: o el patron cubre lo
  que la nomina ya contiene, o la frase del verde se estrecha para decir
  exactamente a que universo se refiere. LO QUE NO VALE ES DEJARLA
  DICIENDO LO QUE NO COMPRUEBA. Con su caso positivo por mutacion, que hoy
  para este agujero NO EXISTE: el caso tiene que caer si alguien devuelve
  el patron a su forma vieja.

- TAREA 3, LA CAIDA DE REPORTE, CORREGIDA POR DECLARACION (adjudicacion
  6.4). Tu seccion 7 escribe "92 arneses en scripts/loop/, 53 en la
  nomina, 41 fuera y anteriores a la vuelta 148". Las tres cifras son
  ciertas por separado y LA RESTA NO CIERRA: 92 menos 53 son 39, no 41. Tu
  propio instrumento imprime otra cosa y esta sellada,
  SALIDA_V164_T5_PRE148.txt dice "CIFRA entradas en la nomina de la
  bateria: 51". Cambiaste el 51 del instrumento por el 53 de la bateria.
  El motivo de fondo es la TAREA 2: el 41 no se resta de 53, se resta de
  51, que son las que el censo ve. NO SE BORRA NADA: la cadena entera y
  cerrada va escrita en el reporte de hoy (92 vistos por el censo, 53 en
  la nomina, 51 visibles, 41 fuera). SE REGISTRA Y NO ACUMULA, por la
  letra afinada del 27 ago 2026 (vive en prosa y no en tabla, cabecera ni
  conclusion), PERO DISPARA LA RELECTURA AL DOBLE DEL TRAMO y eso si se
  hace.

- TAREA 4, LOS 41 PRE 148, ADJUDICADOS Y NO EN BLOQUE (adjudicaciones 6.5
  y 6.6). TU PENDIENTE DE DOCTRINA NO ES DOCTRINA NUEVA Y NO HAY PARADA:
  la pregunta de si la regla de la vuelta 144 es retroactiva esta mal
  planteada, y lo dice la propia regla en su letra desde la vuelta 148,
  que esta en el docstring de la guarda: "LO QUE ESTA REGLA EXIGE ES
  SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN." Una
  regla cuya condicion es el ESTADO DEL SUJETO y no la fecha de nacimiento
  no puede ser retroactiva ni dejar de serlo: no habla del calendario. ASI
  QUE MIDES EL SUJETO DE CADA UNO DE LOS 41, uno por uno, y publicas cual
  esta congelado y cual esta vivo, con su evidencia. Tu propia medicion de
  la 164 ya adelanta la respuesta para varios: las salidas de la 118 que
  "envejecen solas" tienen por sujeto el grafo vivo, que es EXACTAMENTE el
  sujeto que esta regla excluye. ENTRAN SOLO LOS DE SUJETO CONGELADO, y
  NINGUNO se descarta en bloque ni se mete en bloque. Y VA CON EL LIMITE
  QUE MIDO YO Y QUE NO ESTABA ESCRITO: la bateria de 53 tarda 978,2
  segundos en tu maquina y 1.193,1 en la mia, y los 41 tardan 1.091,4 mas,
  o sea que meterlos sin decir su
  coste convierte el ciclo de cierre en media hora larga POR VUELTA. TODO
  ARNES QUE ENTRE ENTRA CON SU TIEMPO PUBLICADO AL LADO, y si el total de
  la bateria pasa de VEINTE MINUTOS lo dices en el reporte y traes la
  cifra. NO SE RECORTA LA NOMINA POR CUENTA PROPIA.

- TAREA 5, EL ESTADO NUEVO SE MIDE, NO SE HEREDA (adjudicacion 6.9). La
  fase 08 la cerro el fundador y eso cambia cifras que tu cabecera lleva.
  CORRE Y PUBLICA CON TU COMANDO, sin copiar una sola de su commit: las
  suites de la web (su commit dice 82 ficheros y 1.040 pasadas, contra las
  80 y 1.030 de tu cabecera de la 164, Y YO NO LAS CORRI, asi que esa
  cifra es CONTRASTE y no medicion), el tsc, y el sha256 del indice
  semantico (el sello publica 42223fcc y ese SI lo recompute yo hoy, sale
  igual). Y CIERRA POR ADICION docs/loop/SELLO_SESION_CREDENCIAL_2026-09-03.md,
  SIN BORRAR SU ULTIMA LINEA: hoy sigue diciendo "la fase 08 NO se declara
  cerrada hoy" y el commit e966d896 la cierra. Las dos cosas fueron
  ciertas en su fecha y el fichero no las distingue, que es la enfermedad
  de la CORRECCION 22 en otro sitio. AVISO SOBRE LA MIA, PARA QUE NO LA
  HEREDES COMO CIFRA: el cotejo byte a byte de los assets, la deuda que
  venia del acta 161, LO SALDE YO HOY y da 6 cotejados, 6 cuadran, 0 no
  cuadran, leyendo las rutas fuente del propio sync_assets_web.py y con su
  normalizacion de fin de linea aplicada. Y SON SEIS ASSETS Y NO CINCO:
  cuatro actas arrastraron mal la cifra de su propia deuda.

- TAREA 6, ABRE EL ULTIMO TRAMO DE LA FASE III (adjudicacion 6.10). Medido
  por mi de docs/plan/OPERACIONES.jsonl: de las 71 operaciones, 67 estan
  en HECHA y CUATRO en LISTA, que son OP-L-01, OP-L-02 y OP-L-03 de
  09_LECTURAS_DIRIGIDAS y OP-I-01 de 10_INVENTARIO. OP-S-12, que el indice
  ata al final, YA ESTA HECHA. EMPIEZAS POR OP-L-01, que es la unica de
  las cuatro sin dependencias declaradas: lee su ficha entera, comprueba
  sus TRES clausulas de verificacion contra el archivo de HOY (ninguna de
  las once en INTRA_DOMINIO_VEREDICTOS.jsonl, el marcador del cribado sin
  mover, y cada nomina afectada re medida con su cobertura al lado por el
  banco 9.26) y publica el resultado con su simulacion previa y su caso
  positivo. OJO CON LO QUE VAS A ENCONTRAR Y NO LO ARREGLES POR TU CUENTA:
  su clausula dice "el marcador del cribado no se mueve: sigue en 2.117" y
  su fecha_corte es del 11 ago 2026, o sea ANTERIOR al cierre del cribado
  en 3.388. UNA OPERACION CUYO TEXTO NO ALCANCE PARA EJECUTARSE SIN
  DECIDIR ES PARADA, NO UNA IMPROVISACION: si la clausula no se puede leer
  como "el marcador no se mueve por esta operacion" sin estrechar ni
  ensanchar nada, PARAS Y LO TRAES con la letra delante.

Y EL REPORTE ES EL DE LA 165: su cabecera sale del tallador, su cierre se
recomputa al cierre, y las cifras que se muevan van con su motivo. Marca
tus discutibles ANTES de saber si aciertas, como hiciste en la 164, que
por eso mi ciega pudo empezar por ellos.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
