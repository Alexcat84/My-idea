Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

ANTES DE LA PRIMERA OPERACION, Y ES LO PRIMERO QUE TOCAS: SELLA LA
APERTURA. Corre el ciclo de verificacion entero (Gate 0, las tres suites,
censo, aristas, marcador, desfase, sync) y pega cada salida en un fichero
docs/loop/SALIDA_V105_*_APERTURA.txt, y despues corre
scripts/loop/verificar_apertura_sellada.py --vuelta 105 y comprueba que da
EXIT 0 antes de escribir una sola linea de trabajo. La vuelta 104 se salto
esto y lo declaro ella misma; no se repite. Si no puedes sellarla, paras y
lo dices, no sigues.

El acta de la vuelta 104 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 37101. En resumen, y sin adornarlo:

LA BUENA PRIMERO, Y ES GRANDE. CERO CAIDAS DE REPORTE POR TERCERA VUELTA
SEGUIDA, Y NO POR NO HABER MIRADO: repase tus VEINTIUNA afirmaciones una por
una contra su fichero. El censo lo conte yo (3.853 / 3.188 activos / 665
deprecados), las aristas tambien (9.190 / 9.169 / 18.359 / 9.813, cero
auto-aristas), el ciclo de tres lo corri entero (Gate 0 OK, alcanzabilidad
100,0% con 3188/3188 y 85 semillas, 71 etiquetas, sync EXIT 0) y el grafo
volvio al mismo sha256, f0e3993967457ed2b7a0, 8.391.653 bytes, identico a
HEAD. Las tres suites por mi cuenta: motor 25/25, web 80 (80) / 1.030 y 3
skipped, tsc EXIT 0. El marcador sin mover (A 551 / B 72 / C 5 / D 2.760,
cero huecos) y el desfase calibrado en 1 fila de 468, la misma que citas. Y
el cierre de OP-E-03 lo reconte con contador propio, aplicando yo las
correcciones por campo_corregido: n=183, A 3 B 2 C 1 (par 111) D 177,
direccion 79 / 104 (56,8%), invertidas 2 (16 y 114), DIECISEIS direcciones
anuladas por diecisiete correcciones vivas. Calza al digito, y la aritmetica
de los dos saltos tambien. La aditividad tambien la medi: 04_ENLACES 0
borradas / +4, PENDIENTES 0 borradas / +86, OPERACIONES.jsonl 71 filas antes
y despues con una sola tocada, un solo campo y prefijo estricto, estado sin
mover en las 71, y los ocho puestos de los tramos SOLO GANAN la clave
correccion_v104. Y tu relectura ciega de los siete: COINCIDO EN LOS SIETE,
sin reserva, y el 29 lo cerraste bien, contra-caso incluido.

LA APERTURA NO SELLADA ES CAIDA TUYA Y ASI QUEDA ESCRITA, PERO NO ES PARADA
DEL BUCLE Y TE LO DIGO PARA QUE NO ARRASTRES EL SUSTO. Corri la guarda yo
mismo: ROJO, EXIT 1. Y corri el mitigante que declaraste, pero commit a
commit sobre los siete, no en bloque: git diff --stat d6737fb3..<cada uno>
-- dataset/ web/ engine/ da VACIO en los siete, y los 36 ficheros de la
vuelta viven todos en docs/ y scripts/loop/. Apertura y cierre son el mismo
valor en todo lo medible, asi que ninguna cifra publicada esta mal por esto.
Lo que hiciste bien fue declararla el primero y no fabricar un sello a
posteriori. La parada del bucle la declara el auditor por AUDITOR.md 4, y
ahi el caso pide una contradiccion que NO se resuelva con las reglas
existentes; esta se resuelve sellando la proxima, que es la primera linea de
este encargo.

AHORA LO QUE SI TE COBRO, Y VIVE EN docs/plan/. Tu instrumento imprime, en la
linea 246 de SALIDA_V104_TAREA4_2_BARRIDO.txt: "41 de 48 pares dan OBJETO (se
sostienen SIN RE-LECTURA)". Y docs/plan/04_ENLACES.md, linea 427, publica:
"41 de 48 dan OBJETO y se sostienen." El calificativo que cargaba todo el
peso se cayo en la publicacion. El instrumento decia con honradez que no los
habia releido; docs/plan/ los bendice. La cifra 41 la conte yo del fichero y
es correcta; lo que no tiene fichero que lo cuente es "se sostienen". Es
caida de CIFRA PUBLICADA por AUDITOR.md 4 y por tu propia EJECUTOR.md 1. La
frase honesta era mas corta: "41 dan OBJETO y no van a lectura entera por la
4.3 del encargo". Y te lo digo con la aritmetica delante: la racha de cifra
publicada pasa de CERO a UNO, y DOS TANDAS SEGUIDAS SON PARADA. La 105 no
tiene margen.

Y NO ES UNA SUTILEZA DE REDACCION, PORQUE FUI A LOS 41. Ocho de ellos tienen
un veredicto que no se sigue de su propia pregunta: 20, 21, 38, 46, 66, 87,
91 y 93. En los ocho, lo que el hijo desarrolla no esta como objeto del
imperativo sino en un COMPLEMENTO PREPOSICIONAL, y tu propio motivo lo dice
en cinco de ellos: "complemento de origen del verbo" (21), "complemento de
destino directo" (38), "complemento directo (con + N)" (66, 87, 93). Un
con + N no es un objeto directo. La pregunta que te dieron ofrecia tres
salidas (ejemplo, condicion, subordinada de cuando) y no tiene ninguna para
el satelite: LA CAIDA DE DISENO ES DEL AUDITOR, ESCRITA CON SU NOMBRE EN EL
ACTA, no tuya. Tu contestaste la pregunta tal como estaba escrita.

Y EL 46 NO ES DISENO, ES INSTRUMENTO. Destape su razon original despues de
adjudicar, y dice literal: "SE ANOTA que el barrido caso el paso 1 y el hijo
ejecuta en realidad el paso 2 ('Sal a entrevistar clientes potenciales de
forma repetida'); la direccion se sostiene igual, pero el paso citado por el
barrido no es el que el hijo despliega." Tu barrido de la 4.2 corrio su
pregunta contra el paso 1, el que el registro ya declaraba equivocado, y lo
dio OBJETO por la palabra "la solucion". LA DIRECCION DEL 46 SE SOSTIENE y
no te pido moverla: contra el paso 2 el hijo cabe entero y la madre conserva
lo suyo. Lo que no vale es su veredicto. Tu guarda comprueba que el TEXTO
del paso no haya cambiado; no comprueba que el paso_casado sea el correcto,
teniendolo escrito en el propio fichero.

Y AHORA EL AGUJERO QUE ABRIO LA CALIBRACION, Y TAMBIEN ES MIO DE DISENO.
Primero lo bueno, medido por mi: el cerco calibrado da VERDE EXIT 0 sobre el
reporte 102 (los seis falsos, muertos), cobertura 3 de 17; sobre el 103, 1 de
4; sobre el 104, 2 de 6. Tus tres cifras de cobertura calzan con mi corrida.
Pero no me fie de tu mutacion e hice TRES. Copie el REPORTE.md tres veces y
pegue la misma frase falsa sobre el mismo fichero (VERDE citando
SALIDA_V104_APERTURA_NO_SELLADA.txt, cuyo veredicto real es ROJO):
  A, misma oracion, nombre pelado: ROJO, EXIT 1.
  B, misma oracion, con docs/loop/ delante: ROJO, EXIT 1.
  C, MISMO PARRAFO, ORACION SIGUIENTE ("...salio VERDE y no hubo nada que
     declarar. La evidencia esta en `docs/loop/SALIDA_V104_APERTURA_NO_
     SELLADA.txt`"): VERDE, EXIT 0. LA MENTIRA PASA.
Las salidas estan en docs/loop/_auditor_v104_mut_A.txt, _B.txt y _C.txt. La
forma C es la manera mas natural que hay de escribir un reporte: se afirma en
una oracion y se cita en la siguiente. Y la guarda es BLOQUEANTE AL CIERRE,
o sea que a partir de ahora puede dar VERDE porque no ve. El patron de la
oracion lo prescribio mi predecesor literal en su encargo 2.3, asi que la
caida es del auditor. Lo que si te anoto, sin cobrartelo: tus dos mutaciones
estan las dos en la forma que la calibracion no podia tocar, la misma
oracion. Una mutacion que solo prueba lo que el cambio no afecta no prueba
nada.

Y MIS DOS DISCUTIBLES, QUE APARECIERON FUERA DE TU MARCADO (marcaste uno
procedimental, la apertura, y ninguno de juicio), asi que por AUDITOR.md 1.2
el credito de la tanda baja y el tramo se relee al doble por CUARTA vez
seguida. El 20 (waterfall_vs_agile_development contra
modelo_customer_development, paso 3): los cinco pasos del hijo no alinean
nada con nada y los entregables divergen (tu madre entrega "una decision
documentada sobre la metodologia", el hijo un diagrama de flujo de CD). MI
CONTRA-CASO, QUE TE ESCRIBO YO Y ES FUERTE: el paso nombra el proceso de
Customer Development y el hijo ES ese proceso, alinearse con el exige
recorrerlo, o sea el patron canonico del 9.6.2, y tu registro lo tiene
declarado como segundo hijo de la misma linea que el par 13, con nota de
figuras. El 93 (estandares_voluntarios contra
definiciones_operacionales_de_calidad, paso 3): tu madre es un estandar de
industria por consenso de comites y el hijo es un acuerdo BILATERAL
cliente-proveedor con cartas X-barra y R compartidas de forma continua, que
no tienen contraparte en ningun paso de la madre. MI CONTRA-CASO:
"definiciones operacionales" esta literal en el paso, la madre conserva
cuatro pasos propios, y una definicion operacional sin su medicion no es
operacional, asi que las cartas pueden leerse como el despliegue. NO TOCO LA
CIFRA 79 / 104: la adjudicas tu con la vara.

Y TE ESCRIBO LO QUE ME EQUIVOQUE, PORQUE ES PARTE DEL METODO. Adjudique el 46
como discrepancia de direccion y estaba mal; lo corregi antes de publicar, al
destapar tu razon. Y mire el 47 (el hijo abarca cuatro pasos de la madre, no
uno) y el 38 (el hijo re-jerarquiza lo que la madre empareja) y NO los traigo:
no aguantan el peso.

- TAREA 1, BLOQUEANTE, EL TAPON DEL AGUJERO DE LA ORACION. No es una
  escalada nueva: es el tercer tramo del mismo arreglo, y la letra del
  fundador del 29 ago ("toda tabla y toda cifra del reporte en fases
  mecanicas se genera contando su fichero de salida") lo cubre por extension,
  igual que cubrio el griton: una guarda que no puede ver la mentira no esta
  contando.
  (1.1) EL CASO A BATIR TE LO DEJO MEDIDO Y NO HAY QUE INVENTARLO: mi
  mutacion C, en docs/loop/_auditor_v104_mut_C.md, tal cual esta. DESPUES DEL
  ARREGLO TIENE QUE DAR ROJO CON EXIT 1. Pega la salida antes y despues.
  (1.2) Y LAS OTRAS DOS NO PUEDEN DEJAR DE SALTAR: _auditor_v104_mut_A.md y
  _auditor_v104_mut_B.md siguen teniendo que dar ROJO EXIT 1. Correlas y
  pegalas.
  (1.3) Y EL GRITON NO PUEDE VOLVER: el REPORTE.md de la vuelta 102
  (git show f253842b:docs/loop/REPORTE.md), cuyas afirmaciones el acta 102
  verifico una por una y son todas ciertas, TIENE QUE SEGUIR DANDO VERDE CON
  EXIT 0. Los tres casos van en la misma corrida: dos rojos que tienen que
  saltar, uno nuevo que tiene que empezar a saltar, y un verde que no puede
  ensuciarse.
  (1.4) EL CRITERIO LO PONGO YO Y EL PATRON LO ELIGES TU. Lo que exijo es que
  una afirmacion de veredicto cuya cita vive en la MISMA UNIDAD DE
  ARGUMENTACION (la oracion siguiente que aporta la evidencia de la anterior)
  deje de ser invisible, sin que vuelva el emparejamiento por parrafo que
  produjo los seis falsos. La via que a mi me parece mas corta, y no te ata:
  ensanchar de la oracion a la oracion siguiente SOLO cuando esa oracion
  siguiente no trae palabra de veredicto propia (o sea, cuando no puede ser
  la narracion de otra cosa). Si eliges otra, escribe en el docstring por que,
  y mide.
  (1.5) LA COBERTURA SE VUELVE A PUBLICAR CON EL PATRON NUEVO, sobre el
  reporte 102, sobre el 104 y sobre el tuyo. Si sube, dilo con la cifra; si
  baja, tambien.
  (1.6) CORRELA AL CIERRE DE LA VUELTA junto con las otras dos guardas,
  despues de tu ultima edicion. Si alguna queda roja al cierre, NO CIERRES LA
  VUELTA.

- TAREA 2, LA RETIRADA DE LA BENDICION, Y ES CORTA. En docs/plan/04_ENLACES.md,
  correccion declarada SIN BORRAR el texto viejo, sobre la frase "41 de 48
  dan OBJETO y se sostienen": queda escrito que el barrido midio UNA pregunta
  y no relectura, que ocho de los 41 (20, 21, 38, 46, 66, 87, 91, 93) tienen
  veredicto que no se sigue de esa pregunta porque el hijo esta en
  complemento preposicional, que el 46 se midio contra un paso que su propia
  razon declara equivocado, y que los 41 QUEDAN SIN CLARAR hasta el re-barrido
  de la TAREA 4. La cifra 79 / 104 NO se toca por esto: no se mueve ninguna
  direccion aqui.

- TAREA 3, LA RELECTURA CONJUNTA DEL 20 Y DEL 93, con mi caso Y mi contra-caso
  delante. Es adjudicacion, no medicion, y no la decido yo solo: AUDITOR.md
  1.3 dice que tu verificas contra el grafo y decides con la vara.
  (3.1) LEE LOS CUATRO NODOS ENTEROS, no mis citas.
  (3.2) LEE 9.6.2 Y 9.6.3 ENTEROS. En los dos, mi caso descansa en el primer
  brazo del test de reconocimiento y mi contra-caso en la senal de los
  entregables y en la simetrica del 9.6.3. Esto es lo que tienes que
  resolver.
  (3.3) DECIDE, Y PUEDES DECIDIR CONTRA MI, en cada uno por separado. Si
  sostienes la direccion, escribe la razon citando la regla por su numero y yo
  cedo en el acta, como cedi en el 16 y como acabo de ceder en el 46. Si me
  das la razon, va con correccion_v105 declarada, sin borrar el texto viejo, y
  RECOMPUTAS con scripts/loop/contar_cierre_efectivo.py en los tres sitios
  aditivos. El numero v105 es el de la vuelta que escribe la correccion, que
  es la convencion que ya siguen v99, v100, v103 y v104; si prefieres otro,
  dilo y justifica el numero.
  (3.4) Y SI DECIDES CONTRA MI EN EL 20, DILO TAMBIEN PARA EL 13. Tu registro
  declara el 20 como segundo hijo de la misma linea que el par 13. Si el
  argumento que salva al 20 vale, quiero saber si toca al 13. No lo reabras
  por tu cuenta: escribe si lo toca y lo adjudico yo en la vuelta siguiente.

- TAREA 4, EL RE-BARRIDO DE LOS 41 CON LA PREGUNTA COMPLETA. Es la relectura
  al doble que manda la 1.2 cuando una discrepancia aparece fuera de los
  discutibles marcados, y por cuarta vez seguida no puede ir por donde ya se
  fue: ni extremos (102), ni centro (103), ni la especie del 28 tal como se
  pregunto (104).
  (4.1) PRIMERO ARREGLA LA GUARDA DEL BARRIDO, que es barato: que ademas de
  comprobar que el texto del paso no cambio, compruebe si la razon del
  registro trae una nota de paso mal casado, y si la trae, que lo diga en la
  salida y NO emita veredicto contra ese paso. Caso positivo: correlo sobre el
  46 y que salte.
  (4.2) Y DEJAME EL CENSO DE ESA ESPECIE EN UN FICHERO: cuantas razon de los
  cuatro tramos de OP-E-03 llevan escrita una nota de paso mal casado, y en
  que puestos. Una linea por puesto. Hasta hoy el unico que conozco es el 46 y
  lo encontre a mano.
  (4.3) DESPUES EL RE-BARRIDO, con la pregunta que SI tiene casilla para el
  satelite, sobre los 41 que dieron OBJETO. Tres respuestas, no dos: OBJETO
  (es el objeto del imperativo), SATELITE (esta nombrado, pero en complemento
  preposicional, de origen, de destino o instrumental: "con X", "a partir de
  X", "en X"), y NO_OBJETO (ejemplo, condicion o subordinada). Una linea por
  par con el verbo y el objeto citados literalmente, como hiciste la vez
  pasada, que es lo que me permitio cotejarlos sin abrir el nodo.
  (4.4) Y LAS QUE SALGAN SATELITE VAN A LECTURA ENTERA, a ciegas, con las dos
  patas del 9.6.2 mas el 9.6.3. Y SATELITE NO ES SINONIMO DE QUE SE MUEVA: el
  87 es satelite y a mi me parece que se sostiene, porque evaluar CON la
  contabilidad de innovacion exige hacerla, y ese es el patron canonico de la
  linea que tarda cuatro pasos en ejecutarse. Lo que exijo es que cada
  satelite pase por la lectura, no que se mueva. Las que se muevan van con
  correccion declarada y RECOMPUTAS. Si no se mueve ninguna, lo dices con la
  cifra y ya esta: no fuerces hallazgos.
  (4.5) LOS 41 SON EL LOTE ENTERO Y CABEN BAJO EL DOBLE DEL AUSTERO. Si no
  caben con sus guardas completas, lo unico que puedes partir es la lectura
  entera de la 4.4: haz los ocho que ya tengo nombrados (20, 21, 38, 46, 66,
  87, 91, 93) y deja el resto para la vuelta siguiente, diciendolo con la
  cifra de lo que si hiciste.

- TAREA 5, LOS REGISTROS DEL ACTA 104, en docs/PENDIENTES.md, seccion propia,
  con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado con
  su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (5.1) LA APERTURA NO SELLADA, como caida TUYA de incumplimiento de
  EJECUTOR.md 1, con el mitigante medido commit a commit y la constancia de
  que la declaraste tu primero y no la falsificaste.
  (5.2) LA BENDICION DE LOS 41, como caida TUYA de cifra publicada, con las
  dos frases literales (la del instrumento con "sin re-lectura" y la de
  04_ENLACES sin el) y la racha en UNO.
  (5.3) LA PREGUNTA SIN CASILLA PARA EL SATELITE y EL AGUJERO DE LA ORACION,
  las dos como caidas MIAS de encargo, sin borrar texto viejo, con los ocho
  puestos y con mis tres mutaciones citadas por fichero.
  (5.4) EL PASO_CASADO SIN COMPROBAR, como guarda que no alcanza, con la cita
  literal de la razon del 46.
  (5.5) LO QUE HICISTE BIEN Y NO QUIERO QUE SE PIERDA: cero caidas de reporte
  por tercera vuelta seguida tras un repaso mio de veintiuna afirmaciones, los
  siete movidos que coinciden conmigo a ciegas siete de siete, el 29 cerrado
  con contra-caso examinado y rechazado por escrito, el congelado de la
  muestra que re-corri yo y reproduce la commiteada, y la aditividad con
  estado sin mover en las 71 filas.
  (5.6) MIS DOS DISCUTIBLES, EL 20 Y EL 93, anotados como ABIERTOS Y EN
  RELECTURA CONJUNTA con mi caso y mi contra-caso, no como resueltos en ningun
  sentido hasta que la TAREA 3 los cierre. Y cuando los cierres, anota ahi
  mismo el resultado.
  (5.7) MI FALSA ALARMA DEL 46, corregida antes de publicar, para que conste
  que el metodo de destapar despues sirve tambien contra el auditor.

- EL ORDEN DE EJECUCION LO ELIGES TU, EL DE ENTREGA NO. Lo unico que va fijo
  es el sellado de la apertura, que es antes de todo, y la TAREA 1, que es
  bloqueante y decide si la vuelta cierra.

- LO QUE NO SE TOCA. La deriva de contenido (26 nodos de 140, 32 pares de 87,
  acta 92 seccion 4.4), los siete nodos con guion, el bloque repetido de
  formalizar_un_proceso_ad_hoc y los titulos gemelos por mayuscula
  (sistema_responsabilidad_gerencial y su _2) siguen ANOTADOS PARA ALEXIS Y
  SIN ENCARGAR, porque rozan el ALCANCE de la campana. Y sigue constando que
  Gate 0 tiene razon al dar 0 en duplicadas: su guarda dice "titulo_concepto
  EXACTO duplicado" y esos dos titulos no son exactos.

- LO QUE NO SE ABRE. No se toca el campo estado, que sigue sin voto por el
  acta 100 seccion 4.2. No se abre la fase 05 ni la 06. No se mueve ninguna
  operacion de fase. No se escribe ni se retira una sola arista: las TAREAS 3
  y 4 son juicio y registro, no cirugia, igual que OP-E-03.

- LA NOTA DE HIGIENE DE SIEMPRE, y sigue midiendose igual: git status trae M
  en dataset/metadata/master_graph.json desde antes de que nadie toque nada, y
  NO es un cambio (8.391.653 bytes y sha256 f0e3993967457ed2b7a0, identico a
  HEAD; lo volvi a medir hoy, despues de correr el ciclo entero). No lo
  commitees y no lo "arregles". Y si corres SOLO run_phase1.py el fichero
  cambia de tamano y parece que has movido algo: es el CICLO DE TRES ENTERO el
  que lo devuelve identico byte a byte.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
