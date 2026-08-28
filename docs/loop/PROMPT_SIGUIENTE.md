Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Ciclo de verificacion entero (Gate 0, las tres suites, censo,
aristas, marcador, desfase, sync), cada salida en su
docs/loop/SALIDA_V109_*_APERTURA.txt, y despues
scripts/loop/verificar_apertura_sellada.py --vuelta 109 con EXIT 0 antes
de escribir una sola linea de trabajo. Ahora la guarda tambien compara
CONTENIDO, no solo nacimiento: si reescribes una salida de apertura, la
guarda lo canta y el reporte lo explica.

El acta de la vuelta 108 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 38327. En resumen, y sin adornarlo:

LAS CINCO TAREAS ESTAN HECHAS Y TODAS TUS CIFRAS CALZAN AL DIGITO, Y NO
TE LO DIGO POR HABERLAS LEIDO SINO POR HABERLAS CORRIDO. Censo 3.853 /
3.188 / 665, aristas 9.190 / 9.169 / 18.359 / 9.813 con cero
auto-aristas, ciclo de tres en verde (Gate 0 OK, alcanzabilidad 100,0%
con 3188/3188 y 85 semillas, etiquetas EXIT 0, sync EXIT 0), grafo en
8.391.653 bytes y sha256 f0e3993967457ed2b7a0 identico a HEAD, motor
25/25, web 80 (80) / 1.030 y 3 skipped, tsc EXIT 0 con fichero de 0
bytes, marcador A 551 / B 72 / C 5 / D 2.760 sin huecos, desfase en 1
fila de 468, cierre efectivo n=183 con direccion 74 / 109 (59,6%) e
invertidas 2. La aditividad: PENDIENTES +104 puras, 04_ENLACES +2 puras,
OPERACIONES.jsonl 71 filas con una sola tocada, un solo campo, prefijo
estricto y estado sin mover en las 71, y en el tramo 2 una SOLA fila
tocada, el 46, que SOLO GANA la clave correccion_v108. El diff sobre
dataset/, web/ y engine/ corrido commit a commit sobre los nueve: VACIO
en los nueve, y los dos arboles de dataset/ son el mismo objeto,
2b8826f4. Guiones largos y medios anadidos: CERO y CERO. LA RACHA DE
CIFRA PUBLICADA VUELVE A CERO Y NO HAY PARADA.

TU INSTRUMENTO DE LA TAREA 2 ES UN INSTRUMENTO DE VERDAD, Y LO SE PORQUE
LO ATAQUE. Lo corri en sus cuatro estados con codigo mio: con los cuatro
ficheros previos da 74 vivas, 73 con pregunta y nombra el 46; con cinco
da 74/74; con seis da 74/74; con la tabla mutilada da 72 y saca el 3
junto al 46; y con una ruta inexistente cae en ROJO sin contar nada.
Imprime su lista de entrada, que era justo lo que se le pedia. Y
corregiste la cifra mal publicada ANTES de publicar la nueva, en ese
orden, como se te dijo.

Y EN LAS DOS DISCREPANCIAS QUE ME DECLARASTE TIENES RAZON TU, LAS DOS
VECES. El precedente del 46 es el 148 y no el 147: medido hoy, el 147
trae correccion_v99 sobre direccion_leida (direccion anulada) y el 148
trae correccion_v99 con campo_corregido "vara (cita)" y el mismo texto de
vara, por el mismo defecto de paso mal casado. LA CAIDA ES MIA, DE
ENCARGO. Y en la mutacion L tambien: tallar_cabecera_reporte.py
--comparar empareja por ETIQUETA y no por posicion, asi que intercambiar
motor y tsc no dispara DISTINTA ahi. LA CAIDA ES MIA, DE ACTA. Ahora
bien, corregi mi propia conclusion antes de publicarla: escribi que el
orden de las filas quedaba sin guarda y FUI A MEDIRLO. Fabrique la
mutacion M (docs/loop/_auditor_v108_mut/mM.md, tu REPORTE.md con las
filas motor y tsc intercambiadas) y la corri contra la OTRA guarda:
verificar_cabecera_pegada_o_condensada.py --vuelta 108 --reporte da ROJO
EXIT 1 senalando exactamente CUATRO celdas. EL ORDEN SI ESTA GUARDADO.
LA M ES TUYA DESDE HOY y va en la corrida de cada vuelta.

Y AHORA LO QUE TE COBRO, Y ES LA UNICA: EL BARRIDO DEL TRAMO 2 VUELCA DOS
VEREDICTOS REGISTRADOS Y NO DECLARA NINGUNO DE LOS DOS. Cruce los seis
ficheros de veredicto puesto a puesto con codigo mio. Cinco puestos han
cambiado de veredicto entre barridos en toda la historia, y dos son de
esta vuelta:

  87: v105 SATELITE -> v108 OBJETO. NO declarado, ni en la fila, ni en el
  reporte, y ni siquiera marcado DISCUTIBLE.

  91: v105 SATELITE -> v108 OBJETO. Marcado DISCUTIBLE, pero descrito
  como "podria leerse SATELITE con otra vara", cuando ya se leyo asi, con
  esta misma vara y por un instrumento de la casa.

Los otros tres vuelcos de la historia (109, 123, 145) SI se declararon, y
dos de ellos los declaraste TU, dentro de la propia fila del fichero de
la vuelta 107: "ya barrido SATELITE en la vuelta 106 y SOSTENIDO tras
lectura entera". La vara existia, la pusiste tu, y en la 108 se cayo el
habito.

LO QUE NO SE MUEVE, Y LO DIGO IGUAL DE FUERTE: el 87 y el 91 ya se
leyeron enteros y a ciegas en la vuelta 105 y los dos SOSTUVIERON, sin
correccion. Ninguna cifra publicada es falsa y el 74 / 109 esta bien. Lo
que falta es la declaracion, no el trabajo. Por eso lo registro como
caida de EXPEDIENTE con reflejo en el reporte, NO de cifra ni de clase, y
por la letra del fundador del 27 ago la parte del reporte vive en prosa
de acompanamiento: se registra con su nombre y dispara la relectura al
doble, pero NO acumula. La racha de reporte sigue en UNO.

Y HAY UN DETALLE MAS EN LA FILA DEL 87 QUE NO ES DE FORMA: su razon
invoca "el patron del 116", y el 116 dice lo contrario. Alli el tema del
hijo estaba "nombrado literalmente DENTRO de la enumeracion del objeto";
aqui el objeto directo es pronominal ("ese trabajo") y todo el contenido
sustantivo vive en el complemento instrumental. El precedente citado no
sostiene el veredicto que respalda.

Y COINCIDO CONTIGO EN LOS DOS DISCUTIBLES QUE MARCASTE, adjudicados por
mi sobre los nodos antes de destapar nada. El 64: OBJETO, porque el hijo
ejecuta el verbo sobre el objeto directo mismo (su paso 2 elabora la
lista DE DEFECTOS y su entregable es la tabla de esos defectos), y el
contra-caso de las tres ordenes coordinadas se cae porque en el 109 el
objeto directo no era lo que el hijo tocaba y aqui SI lo es. El 91:
OBJETO, y llego ahi por una razon distinta de la tuya: en "establecer
gates con criterios visibles" el sintagma cuelga del NOMBRE gates y no
del verbo (no se establecen gates POR MEDIO DE criterios, se establecen
gates QUE TIENEN criterios), asi que los criterios viven DENTRO del
objeto directo, patron del 102, y lo confirma la senal de entregables del
9.6.2.

- TAREA 1, LOS REGISTROS DEL ACTA 108, en docs/PENDIENTES.md, seccion
  propia, con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado
  con su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (1.1) LOS DOS VUELCOS SIN DECLARAR (87 y 91), como caida TUYA de
  EXPEDIENTE con reflejo en el reporte, con la tabla de los cinco vuelcos
  de la historia y cual se declaro y cual no, con la constancia de que NO
  es de clase ni de cifra publicada (ninguna cifra sale falsa y las dos
  lecturas enteras de la 105 ya SOSTUVIERON), y de que por la letra del
  27 ago NO acumula: la racha de reporte sigue en UNO y la de cifra
  publicada vuelve a CERO.
  (1.2) EL PRECEDENTE MAL CITADO EN LA FILA DEL 87, con la cita literal
  del 116 ("nombrado literalmente DENTRO de la enumeracion del objeto") y
  la del 87 ("todo el contenido sustantivo vive en el complemento
  instrumental"), y con la constancia de que son formas contrarias.
  (1.3) EL 64 Y EL 91, los dos CERRADOS y los dos a tu favor, con la
  razon del 91 escrita de las DOS maneras (la tuya y la mia, que llegan
  al mismo sitio por caminos distintos). Deja escrito que dejan de estar
  marcados DISCUTIBLE.
  (1.4) MIS DOS CAIDAS PROPIAS: la de ENCARGO (el 147 que era el 148) y
  la de ACTA (las cuatro celdas de la L, que eran de la otra guarda), con
  la constancia de que la segunda la corregi yo mismo antes de publicar,
  midiendo con la mutacion M en vez de dejar la afirmacion dicha.
  (1.5) LA GUARDA DEL ORDEN SI ALCANZA, con la salida de la mutacion M
  (docs/loop/_auditor_v108_mut/out_mM.txt, ROJO EXIT 1 en cuatro celdas),
  para que no vuelva a anotarse como hueco lo que no lo es.
  (1.6) EL CHOQUE DE LAS DOS GUARDAS DE CABECERA, ADJUDICADO POR MI
  (acta 108 seccion 2), con la regla tal como queda escrita abajo en la
  TAREA 4.

- TAREA 2, BLOQUEANTE: EL VUELCO DE VEREDICTO SE CAZA CON UN INSTRUMENTO,
  NO CON LA MEMORIA DEL QUE ESCRIBE LA FILA. Es el remedio de la caida
  1.1 y lo adjudico por extension de la misma letra del fundador del 29
  ago por la que la vuelta 108 adjudico su TAREA 2 (toda cifra del
  reporte en fases mecanicas se genera contando su fichero de salida): si
  el habito de declarar el vuelco se puede caer, entonces la declaracion
  la tiene que exigir una guarda, no la buena memoria.
  (2.1) Nace un instrumento de nombre estable, SIN numero de vuelta, que
  recorre los MISMOS ficheros de veredicto que ya declara
  scripts/loop/verificar_cobertura_bolsa_tres_vias.py (reusa su constante
  FICHEROS_VEREDICTO, no la vuelvas a teclear: una lista que se copia es
  una lista que se desincroniza), extrae el veredicto de CADA puesto en
  CADA fichero, y saca la lista NOMINAL de los puestos que tienen dos
  veredictos distintos en dos ficheros, con el fichero y el veredicto de
  cada lado.
  (2.2) Y NO SE QUEDA EN LISTAR: por cada vuelco, comprueba si el fichero
  MAS NUEVO lo DECLARA, buscando en la fila de ese puesto la mencion del
  veredicto anterior o de la vuelta anterior. Vuelco declarado: pasa.
  Vuelco mudo: ROJO EXIT 1 nombrando el puesto. La forma de declarar que
  el 123 y el 145 ya traen en el fichero de la vuelta 107 es la que sirve
  de patron; leela antes de decidir como reconoces la mencion, y escribe
  en el docstring que patron aceptas.
  (2.3) CASO POSITIVO SOBRE EL ESTADO DE HOY: tiene que dar CINCO vuelcos
  (87, 91, 109, 123, 145), reconocer declarados el 109, el 123 y el 145,
  y caer en ROJO nombrando el 87 y el 91. Pega la salida. Si te da otra
  cosa, PARA Y LO TRAES: mi cifra es de codigo mio corrido hoy
  (docs/loop/_auditor_v108/satelites.py) y la discrepancia se declara, no
  se resuelve copiando.
  (2.4) CASO ROJO POR MUTACION, y que muerda: sobre una COPIA, borra de
  la fila del 123 del fichero de la vuelta 107 la frase que declara su
  veredicto anterior, y comprueba que el 123 pasa de declarado a mudo. Si
  da lo mismo con la frase quitada, no esta leyendo la declaracion.
  (2.5) Y CUANDO ESTE VERDE EL INSTRUMENTO, no antes, se arregla el
  fichero: las filas del 87 y del 91 en
  docs/loop/SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md ganan su declaracion
  del vuelco, ADITIVA, sin borrar una letra de lo que ya dicen, con el
  veredicto anterior, la vuelta que lo dio, y el hecho de que los dos
  fueron leidos enteros en la 105 y SOSTUVIERON.

- TAREA 3, BLOQUEANTE: EL 87, RESUELTO EN VEZ DE VOLTEADO EN SILENCIO.
  Es mi discrepancia FUERA de los discutibles marcados y por eso es
  bloqueante, no porque mueva ninguna cifra (no mueve ninguna).
  (3.1) LEE EL 87 ENTERO, los dos nodos, HOY, contra el grafo. No copies
  de la razon vieja ni de la lectura entera de la 105: puede que las dos
  se equivoquen.
  (3.2) ESCRIBE EL CONTRA-CASO FUERTE ANTES DE DECIDIR, como hiciste con
  el 109, y esta vez el contra-caso es el mio: objeto directo pronominal,
  contenido sustantivo entero en el complemento instrumental, que es la
  forma del SATELITE.
  (3.3) DECIDE, Y LAS DOS SALIDAS SON LEGITIMAS. Si sostienes OBJETO,
  sostienlo con un precedente QUE DIGA ESA FORMA, no con el 116, que dice
  la contraria; si no encuentras precedente para esa forma, dilo: un
  veredicto sin precedente se declara sin precedente, no se apoya en uno
  prestado. Si vuelves a SATELITE, la lectura entera de la 105 ya existe
  y ya SOSTUVO, asi que la direccion no se mueve igualmente: lo que
  cambia es solo la fila de la criba, y se declara.
  (3.4) EN CUALQUIERA DE LOS DOS CASOS, la fila se corrige de forma
  ADITIVA y la cifra se recuenta con contar_cierre_efectivo.py: tiene que
  seguir dando 74 / 109 (59,6%). Si se mueve, paras y lo traes.

- TAREA 4, EL CERCO NO PESA EL TEXTO QUE PEGA UN TALLADOR. Es la
  adjudicacion de la pendiente de doctrina que tu mismo levantaste, y
  la resuelvo por AUDITOR.md 1.3 como CHOQUE ENTRE DOS REGLAS ESCRITAS,
  no como doctrina nueva: verificar_cabecera_pegada_o_condensada.py exige
  que la cabecera sea IDENTICA a la del tallador, y
  tallar_veredictos_reporte.py exige que cada palabra de veredicto cite
  un fichero con veredicto legible; la fila de identidad la escribe el
  tallador y editarla para contentar a la segunda rompe la primera. LA
  REGLA QUEDA ASI: el cerco de tallar_veredictos_reporte.py pesa LA PROSA
  QUE EL EJECUTOR ESCRIBE, no el texto pegado literal de un tallador.
  NO es bloqueante.
  (4.1) tallar_veredictos_reporte.py aprende a reconocer las lineas del
  reporte que son texto de tallador y a excluirlas del cerco. Y no vale
  excluirlas a ojo: se excluyen porque el instrumento COMPRUEBA que esas
  lineas salen del tallador (correr tallar_cabecera_reporte.py y casar,
  o el mecanismo que prefieras, pero comprobado, no supuesto).
  (4.2) LO QUE SE EXCLUYE SE DICE EN LA SALIDA, con su numero de lineas.
  Un cerco que calla lo que no mira no es un cerco mas estrecho, es un
  cerco mas corto.
  (4.3) CASO POSITIVO: el REPORTE.md de la vuelta 108 (git show
  7f697c00:docs/loop/REPORTE.md), que hoy da ROJO por la fila 18, tiene
  que dar VERDE con la regla nueva, y decir que excluyo las filas de la
  cabecera.
  (4.4) CASO ROJO POR MUTACION: una copia de ese mismo reporte con una
  afirmacion de veredicto FALSA anadida EN PROSA, fuera de la cabecera,
  tiene que seguir dando ROJO. Si el arreglo apaga tambien esa, has
  abierto un boquete en vez de cerrar un choque.

- TAREA 5, LA ESPECIE DEL VUELCO AL DOBLE. Es la relectura al doble que
  dispara mi discrepancia fuera del marcado (AUDITOR.md 1.2), y por
  octava vez seguida no va por donde ya se fue: ni extremos, ni centro,
  ni la especie del 28, ni los tramos 1 y 2, ni los 3 y 4, ni el tramo 1
  solo, ni el tramo 2 solo, sino por LA ESPECIE.
  (5.1) EL LOTE son los puestos que alguna vez recibieron un veredicto
  SATELITE en cualquier barrido y siguen RESUELTA vivos hoy. Contados por
  mi hoy son SEIS: 87, 91, 109, 123, 145, 154. RECUENTALOS TU antes de
  correr nada y declara la cifra que te salga; si difiere, la
  discrepancia se declara, no se resuelve copiando. Ya me has ganado tres
  recuentos seguidos.
  (5.2) A cada uno, la pregunta de tres vias con el formato de TRES
  CAMPOS, y ADEMAS, en la misma fila, SU HISTORIA DE VEREDICTOS: que dijo
  cada barrido y en que vuelta. El 87 sale de aqui si la TAREA 3 ya lo
  resolvio: dilo con su cita, no lo repitas.
  (5.3) Si alguno se mueve, va a lectura entera con las dos patas del
  9.6.2 mas el 9.6.3 y su contra-caso escrito fuerte, y si cambia la
  direccion, correccion_v109 declarada y recomputo en los tres sitios
  aditivos. Si no se mueve ninguno, dilo con la cifra y ya esta: no
  fuerces hallazgos.
  (5.4) EL LOTE ENTERO CABE DE SOBRA BAJO EL DOBLE DEL AUSTERO (6 pares
  contra un tope de 160). No hay nada que partir aqui.

- LAS GUARDAS DEL CIERRE, y desde hoy son OCHO instrumentos y QUINCE
  casos. Contados uno por uno.
  INSTRUMENTOS (8): tallar_veredictos_reporte.py sobre tu propio reporte;
  tallar_nombre_de_operacion.py OP-E-03; verificar_apertura_sellada.py
  --vuelta 109; verificar_cabecera_pegada_o_condensada.py --vuelta 109;
  verificar_cobertura_bolsa_tres_vias.py; contar_cierre_efectivo.py; el
  instrumento nuevo de la TAREA 2; y tallar_cabecera_reporte.py --fase04
  --vuelta 109.
  CASOS DE MUTACION (15): las TRECE de la vuelta 108 (_auditor_v104_mut_A,
  _B, _C, _auditor_v105_mut_D, _E, _F, _auditor_v106_mut_G,
  _auditor_v106_mut_H, el reporte 102 por git show f253842b, y
  docs/loop/_auditor_v107_mut/mI.md, mJ.md, mK.md, mL.md), MAS la M nueva
  (docs/loop/_auditor_v108_mut/mM.md), MAS la mutacion de la TAREA 2.4.
  LOS RESULTADOS QUE NO PUEDEN CAMBIAR: A, B, C, E, F y G en ROJO EXIT 1;
  D y H en VERDE EXIT 0; el reporte 102 en VERDE EXIT 0; I ROJO por la
  promesa falsa; J ROJO senalando fila 7 apertura; K ROJO por numero de
  filas; L ROJO EXIT 1 con 0 DISTINTA y 3 AUSENTE (esa es la cifra buena,
  la del acta 108, no la del acta 107); y M ROJO EXIT 1 con CUATRO celdas
  (filas 4 y 6, apertura y cierre). La H sigue siendo la frontera
  declarada por diseno: si algun dia da ROJO, eso no es una mejora, es
  que se movio el perimetro sin decidirlo, y paras.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Lo unico que va
  fijo es el sellado de la apertura, que es antes de todo, y que en la
  TAREA 2 el instrumento se pone VERDE ANTES de que se toquen las filas
  del 87 y del 91 (2.5), no despues: primero la guarda que lo va a
  exigir, despues el arreglo que ella exige.

- LO QUE NO SE TOCA. La deriva de contenido (26 nodos de 140, 32 pares de
  87, acta 92 seccion 4.4), los siete nodos con guion, el bloque repetido
  de formalizar_un_proceso_ad_hoc y los titulos gemelos por mayuscula
  (sistema_responsabilidad_gerencial y su _2) siguen ANOTADOS PARA ALEXIS
  Y SIN ENCARGAR, porque rozan el ALCANCE de la campana. Y sigue
  constando que Gate 0 tiene razon al dar 0 en duplicadas: su guarda dice
  "titulo_concepto EXACTO duplicado" y esos dos titulos no son exactos.

- LO QUE NO SE ABRE. No se toca el campo estado, que sigue sin voto por
  el acta 100 seccion 4.2 (medido hoy: LISTA 70, HECHA 1, y en la fase 04
  diez operaciones con una HECHA y nueve LISTAS). No se abre la fase 05
  ni la 06. No se mueve ninguna operacion de fase. No se escribe ni se
  retira una sola arista: las TAREAS 3 y 5 son juicio y registro, no
  cirugia, igual que OP-E-03.

- LA NOTA DE HIGIENE DE SIEMPRE, y sigue midiendose igual: git status
  trae M en dataset/metadata/master_graph.json desde antes de que nadie
  toque nada, y NO es un cambio (8.391.653 bytes y sha256
  f0e3993967457ed2b7a0, identico a HEAD; lo volvi a medir hoy, despues de
  correr el ciclo entero, y git diff sobre ese fichero da CERO lineas).
  No lo commitees y no lo "arregles". Y si corres SOLO run_phase1.py el
  fichero cambia de tamano y parece que has movido algo: es el CICLO DE
  TRES ENTERO el que lo devuelve identico byte a byte. Ojo con la ruta:
  el validador vive en scripts/run_phase1.py, no en la raiz.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
