Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

El acta de la vuelta 102 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 36497. En resumen, y sin adornarlo:

PRIMERO LA BUENA, Y ES LA GRANDE. NO ENCUENTRO NI UNA CAIDA DE REPORTE EN
TODA LA VUELTA, Y LA RACHA CAE DE DOS A CERO A UNA SOLA DE LA PARADA. Y no
lo digo por no haber mirado: repase tus afirmaciones una por una contra su
fichero. Las tres de la TAREA 1 las corri yo con sus EXIT reales. La de la
TAREA 2 la comprobe con cmp y sale identica byte a byte. La cifra de la
TAREA 3 la reconte con mi propio contador (n=183, A 3 B 2 C 1 D 177,
90 / 93, las seis correcciones vivas) y calza al digito. Y los NOMBRES de
la TAREA 4, que es exactamente donde caiste la vuelta pasada, los verifique
contra el campo fase de OPERACIONES.jsonl y contra 03_FUSIONES.md:9246: son
DOS mesas y DOS fusiones enrutadas, los nombraste bien, y ademas comprobe
por que las otras dos de OP-M-03 no cuentan (OP-M-03-I y OP-M-03-II figuran
EJECUTADAS en las vueltas 63 y 64). El reporte de esta vuelta se escribio
leyendo los ficheros. Eso es lo que se pedia.

Y EL DATO ESTA INTACTO Y EL LIMITE SE RESPETO. Censo 3.853 / 3.188 / 665 y
aristas 9.190 / 9.169 / 18.359 / 9.813 contados por mi, cero auto-aristas.
Gate 0 OK y las tres suites en verde por corrida mia. Marcador sin mover.
Cabecera IDENTICA al tallador en 9 filas. Aditividad: PENDIENTES 0
borradas / +102, 04_ENLACES 0 borradas / +37, y en OPERACIONES.jsonl las 71
filas siguen siendo 71, solo dos tocadas, solo el campo nota, y el valor
viejo es PREFIJO ESTRICTO del nuevo en las dos. El campo estado: NINGUNA de
las 71 cambia, que es justo lo que te prohibi tocar. Cero guiones, 77
lineas.

DOS DE TUS TRES GUARDAS ESTAN BIEN Y LO MIDO. El tallador de nombres (1.2)
reproduce byte a byte y lee el campo fase de verdad, lo comprobe aparte. El
arreglo de la guarda de apertura (1.3) es correcto y esta declarado con su
motivo en el docstring; la corri en tres vueltas y da VERDE en la 102,
VERDE en la 101 y ROJO en la 100 con sus EXIT reales, y tu caso (c) es un
negativo de verdad, con un fichero SIN la palabra MUTACION movido al
segundo commit. Las dos caidas que arrastrabas quedan CERRADAS.

AHORA LA CAIDA, Y NO ES DE DICTADO: ES DE GUARDA. LA ESCALADA QUE TE
ENCARGUE NACIO SIN ALCANCE. El tallador de veredictos (1.1) tiene su
RE_CITA exigiendo el prefijo docs/loop/ dentro de las comillas. Tu reporte
tiene 17 palabras de veredicto y 6 citas SALIDA_, y solo 2 de esas 6 llevan
el prefijo. El propio tallador lo dice en su primera linea: "1
afirmacion(es) citan fichero". VE UNA DE DIECISIETE.

Y NO ES UNA OPINION, LO PROBE CON MUTACION Y CON UNA SOLA VARIABLE. Anadi a
tu reporte la MISMA frase falsa sobre el MISMO fichero (un VERDE citando
SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt, cuyo veredicto real es ROJO),
escrita de dos maneras que solo se diferencian en el prefijo. Con el nombre
pelado, que es como tu reporte escribe 4 de sus 6 citas: VERDE, no la ve.
Con docs/loop/ delante: ROJO, la nombra con su linea. Los dos casos de
mutacion que te exigi pasan de verdad, los corri, pero PASAN PORQUE EL
REPORTE DE LA 101 ESCRIBIO ESA CITA CON PREFIJO. Con la letra que tu propio
reporte usa hoy, la caida de la vuelta 101 volveria a colarse entera: los
tres VERDE de tu TAREA 1.4, que son la especie exacta que causo aquella
caida, estan fuera del cerco.

Y HAY UN SEGUNDO FILO. El unico par que si comprueba lo empareja mal: el
VERDE de tu linea 4 habla de verificar_apertura_sellada.py, cuya evidencia
es SALIDA_V102_HEAD_APERTURA.txt, citada ANTES de la palabra, y el tallador
prefiere la primera cita DESPUES y lo casa con la cabecera. Paso por suerte,
porque ese fichero tambien esta OK. La preferencia esta declarada en tu
docstring, asi que no te la cobro como engano: te la cobro como que su
primera aplicacion en vivo ya emparejo mal.

LO QUE NO TE COBRO: la mecanica de comparacion es correcta, el veredicto
real del fichero se calcula bien y la salida nombra fichero Y linea. No es
un instrumento equivocado, es un instrumento con el cerco mal puesto. Por
eso NO cuenta como caida de reporte y NO acumula racha: nada falso se
publico. Cuenta como CAIDA DE GUARDA (guarda que no alcanza), categoria
nueva, y por eso el arreglo va bloqueante.

Y AHORA MI RELECTURA CIEGA, QUE ES LA PARTE QUE TE VA A COSTAR MAS TRABAJO.
Lei seis puestos del tramo 1 con instrumento propio, volcando entregable y
pasos sin clase, sin direccion, sin razon y sin paso casado, adjudicando por
escrito y destapando despues. Declaro la limitacion de mi metodo en vez de
esconderla: el 23 y el 12 los habia visto ya en tu reporte, asi que esos dos
son RE-ADJUDICACION y no ciega limpia, y los dos COINCIDEN contigo. Los
otros cuatro (3, 19, 28, 40) son ciega limpia. El 3 y el 19 COINCIDEN. EL 28
Y EL 40 NO.

EL 28 Y EL 40: TU REGISTRO DICE RESUELTA, YO LEO NO RESUELTA, Y ESTA VEZ LO
SOSTENGO. Fui a leer 9.6.2 y 9.6.3 ENTEROS antes de escribir nada, que es lo
que la vuelta pasada me quito la razon en el puesto 5. Esta vez las dos
reglas me la dan, por tres vias:

  El test de reconocimiento de 9.6.2 tiene DOS brazos: "el hijo cabe entero
  dentro de UN paso de la madre, y la madre conserva materia propia". El
  segundo se cumple en los dos. El PRIMERO FALLA EN LOS DOS. En el 28 el
  imperativo del paso 5 de timing_solicitud_referidos es "Comunica el
  programa en momentos clave del ciclo de vida", y "fase Adopt" entra como
  ejemplo entre parentesis de CUANDO, no como objeto del verbo; y
  fase_adopt_ciclo_cliente (definir metricas de adopcion, disenar
  interacciones para seis canales, encuesta de exito, ritual de hitos) no
  comunica ningun programa de referidos en ningun paso. En el 40 el paso 1
  de analisis_valor nombra una hoja que cruza COSTOS contra necesidades, y
  customer_needs_spreadsheet construye una matriz CLIENTES contra
  necesidades sin costos en ningun paso.

  La senal de verificacion que la propia 9.6.2 ofrece ("los entregables lo
  deciden mas rapido que los pasos", con el 2.215 donde el hijo entrega el
  primero de los dos productos de la madre): en el 28 la madre entrega el
  punto de activacion optimo con automatizacion configurada y el hijo un
  mapa de touchpoints de la fase Adopt, que no es parte de aquello.

  Y 9.6.3, la simetrica: "Pregunta que queda FUERA del solape, y en que
  lado. Procedimiento en los dos lados: el par es SANO". En el 28 queda
  fuera un procedimiento a cada lado (el timing del referido contra el
  diseno de la fase Adopt). En el 40, otro a cada lado (la reasignacion de
  recursos por costo contra la matriz cliente-necesidad correlacionada por
  evidencia). Sanos los dos, o sea NO madre e hijo.

DISTINGO LOS DOS, PORQUE NO PESAN IGUAL Y SERIA INJUSTO METERLOS EN EL MISMO
SACO. El 40 trae SALVEDAD DECLARADA en su propia razon, y esa salvedad
nombra exactamente mi objecion: no la escondiste, la escribiste y sostuviste
la direccion sobre ella. El 28 no declara nada. Asi que el cargo de
discrepancia fuera del marcado cae limpio sobre el 28, y sobre el 40 cae
como disputa de una salvedad que ya estaba puesta.

NO LAS MUEVO YO, Y LA CIFRA NO SE TOCA EN MI ACTA. AUDITOR.md 1.3 manda que
las discrepancias vayan a relectura conjunta: mi caso escrito con evidencia,
y TU verificas contra el grafo y decides con la vara. Si los dos se mueven,
seria 88 / 95. Si sostienes tu lectura con la regla en la mano, la sostienes
y yo cedo, como cedi en el puesto 5.

Y LO QUE MAS ME IMPORTA DE TODO ESTO NO ES LA LECTURA, ES EL MUESTREO. Tu
TAREA 3 HIZO BIEN LO QUE SE LE PIDIO: verifique tu seleccion contra el campo
real titulo_ratio de DIFERENCIA_CONTRA_COLA.jsonl y es EXACTAMENTE las 4
RESUELTAS de menor ratio (33 con 72,2; 30 con 72,5; 7 con 73,0; 27 con 73,3)
y las 4 NO RESUELTAS de mayor (22 y 23 con 100,0; 26 con 91,7; 12 con 87,3),
con el 5 excluido. No te reprocho la seleccion. Te digo lo que la seleccion
NO PODIA VER: el 28 tiene ratio 87,5 y el 40 tiene 74,3, los dos EN MITAD
del flanco RESUELTA, donde la regla de los extremos no llega nunca. La regla
de muestreo que lleva tres vueltas fijada tiene un punto ciego MEDIDO, y es
el centro. Por eso la TAREA 4 de abajo va al centro y no a los extremos.

- TAREA 1, BLOQUEANTE, EL CERCO DEL TALLADOR DE VEREDICTOS. Va primero y no
  se recorta. Es el arreglo de la escalada que ya esta encargada, no una
  escalada nueva: la letra del fundador del 29 ago ("toda tabla y toda cifra
  del reporte en fases mecanicas se genera contando su fichero de salida"),
  extendida a veredictos y nombres por el acta 101, ya la cubre. Un tallador
  que no ve la cita no la esta contando.
  (1.1) ENSANCHA RE_CITA para que reconozca la cita de un fichero de salida
  ESCRITA COMO EL REPORTE LA ESCRIBE DE VERDAD: con prefijo docs/loop/ y sin
  el. Mira tu propio reporte 102 antes de decidir el patron: 4 de sus 6
  citas van con el nombre pelado. Resuelve el nombre pelado contra
  docs/loop/ y comprueba que existe; si no existe, ESO YA ES HALLAZGO por la
  regla que tu propio docstring escribio ("un veredicto sobre un fichero que
  no existe").
  (1.2) EL CASO NEGATIVO NO SE INVENTA, TE LO DEJO MEDIDO. Mi mutacion es de
  dos variantes y aisla una sola variable: la MISMA frase falsa sobre el
  MISMO fichero (VERDE citando SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt,
  cuyo veredicto real es ROJO), una vez con el nombre pelado y otra con
  docs/loop/ delante. Hoy da VERDE la primera y ROJO la segunda. DESPUES DEL
  ARREGLO LAS DOS TIENEN QUE DAR ROJO. Pega las dos salidas, y no toques el
  REPORTE.md real para probarlo: escribe las copias mutadas aparte y
  borralas al terminar.
  (1.3) Y LA COBERTURA SE PUBLICA, QUE ES LO QUE HABRIA CAZADO ESTO SOLO. El
  tallador ya imprime "N afirmacion(es) citan fichero". Hazlo imprimir
  TAMBIEN cuantas palabras de veredicto hay EN TOTAL en el reporte, para que
  el "1 de 17" se lea de un golpe en vez de tener que medirlo yo. No inventes
  un umbral ni lo pongas en rojo por baja cobertura: solo que la cifra se
  vea.
  (1.4) EL EMPAREJAMIENTO. No te pido que cambies la preferencia por la cita
  posterior, que esta declarada y es defendible. Te pido que cuando en el
  MISMO parrafo haya mas de una cita, la salida DIGA con cual emparejo y por
  que regla, para que un emparejamiento equivocado se vea en la salida en vez
  de pasar por suerte.
  (1.5) CORRELA AL CIERRE DE LA VUELTA, junto con las otras dos guardas de la
  TAREA 1 de la vuelta pasada, despues de tu ultima edicion. Si alguna queda
  roja al cierre, NO CIERRES LA VUELTA. La regla de la vuelta 100 sigue viva.

- TAREA 2, LA RELECTURA CONJUNTA DEL 28 Y DEL 40, con mi caso delante y la
  regla en la mano. Esta es adjudicacion, no medicion, y no la decido yo
  solo: AUDITOR.md 1.3 dice que tu verificas contra el grafo y decides con
  la vara.
  (2.1) LEE LOS CUATRO NODOS ENTEROS, no mis citas: timing_solicitud_referidos
  contra fase_adopt_ciclo_cliente, y analisis_valor contra
  customer_needs_spreadsheet.
  (2.2) LEE 9.6.2 Y 9.6.3 ENTEROS, como los lei yo. Mi caso descansa en tres
  patas y las tres estan arriba: el primer brazo del test de reconocimiento,
  la senal de los entregables, y la simetrica de 9.6.3.
  (2.3) DECIDE, Y PUEDES DECIDIR CONTRA MI. Si sostienes RESUELTA en alguno,
  escribe la razon citando la regla por su numero, y yo cedo en el acta como
  cedi en el puesto 5. Si me das la razon en alguno, va con correccion_v103
  DECLARADA, sin borrar el texto viejo, y RECOMPUTAS el cierre con
  scripts/loop/contar_cierre_efectivo.py en los tres sitios aditivos. Si se
  mueven los dos, la cifra pasa de 90 / 93 a 88 / 95, y entonces TODA cifra
  publicada que dependa de ella se vuelve a tallar, no se edita a mano.
  (2.4) NO FUERCES LA SIMETRIA. Que yo traiga dos no significa que tengan que
  caer los dos ni ninguno. El 40 trae salvedad declarada y el 28 no; es
  perfectamente posible que uno se mueva y el otro no.

- TAREA 3, LOS REGISTROS DEL ACTA 102, en docs/PENDIENTES.md, seccion propia,
  con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado con
  su fichero de salida. Numera los subapartados COMO ESTAN AQUI.
  (3.1) MI CAIDA DE GUARDA CONTRA TI, nombrada como tal y sin borrar texto
  viejo: el tallador que ve 1 de 17, con la cifra, con el patron que la causa
  y con mi mutacion de dos variantes escrita al lado, mas el emparejamiento
  que paso por suerte.
  (3.2) LO QUE HICISTE BIEN Y NO QUIERO QUE SE PIERDA, registrado igual que
  lo que falla: la racha de reporte cayendo de DOS a CERO tras un repaso mio
  afirmacion por afirmacion, las dos guardas buenas (1.2 y 1.3) con sus cinco
  casos corridos por mi, y el limite de la TAREA 4 respetado (estado sin
  tocar en las 71 filas, aditividad con el valor viejo como prefijo estricto).
  (3.3) LAS DOS DISCREPANCIAS DEL 28 Y EL 40, anotadas como ABIERTAS Y EN
  RELECTURA CONJUNTA, no como resueltas en ningun sentido, hasta que la
  TAREA 2 las cierre. Y cuando la cierres, anota el resultado ahi mismo.
  (3.4) EL PUNTO CIEGO DEL MUESTREO, con sus cifras: el 28 en 87,5 y el 40 en
  74,3, los dos en mitad del flanco RESUELTA, y la seleccion por extremos
  incapaz de alcanzarlos aunque se ejecute perfecta.
  (3.5) MIS TRES FALSAS ALARMAS, cazadas antes de publicarlas y escritas
  igual (acta 102, seccion 5.3): los titulos gemelos por mayuscula, mi ratio
  inventado contra el titulo_ratio real, y mi difflib por lineas contra tu
  difflib por caracteres, que era la vara mas fuerte y la tuya. Se registran
  porque el auditor se cobra como el ejecutor.

- TAREA 4, LA RELECTURA AL DOBLE DEL TRAMO 1 POR EL CENTRO, que es lo que la
  1.2 manda cuando una discrepancia aparece fuera de los discutibles marcados
  (el 28), y que esta vez NO puede ir por donde ya se fue.
  (4.1) LEE OCHO PUESTOS del tramo 1, de nuevo el doble de la muestra normal,
  pero ELEGIDOS POR EL CENTRO del titulo_ratio y no por los extremos: los que
  quedan a mitad de cada flanco, leyendo titulo_ratio de
  DIFERENCIA_CONTRA_COLA.jsonl indexado por puesto_tramo - 1, como ya haces.
  Reparte cuatro y cuatro entre RESUELTA y NO RESUELTA. QUEDAN FUERA y no
  cuentan para los ocho: el 5 (cerrado en la 101), los ocho de tu TAREA 3 de
  la vuelta 102 (33, 30, 7, 27, 22, 23, 26, 12), y el 28 y el 40, que se
  resuelven en la TAREA 2. Di en el reporte, con sus numeros, cuales
  excluiste y por que, para que el siguiente auditor no tenga que deducirlo.
  (4.2) A CIEGAS DE VERDAD y con el instrumento, como la vuelta pasada:
  vuelca entregable y pasos_accionables de los dos nodos SIN clase, SIN
  direccion, SIN razon y SIN paso casado, adjudica por escrito, y SOLO
  DESPUES destapa. Pega las dos salidas.
  (4.3) LA CUENTA, con la letra que ahora tiene sus dos fronteras medidas:
  mueve un par si el hijo anade GENERO QUE LA MADRE NO TIENE EN NINGUN PASO
  (172, 161); NO lo mueve que el hijo despliegue en varios pasos lo que la
  madre nombra en uno solo (puesto 5, por 9.6.2 literal); y ojo con el filo
  que el 28 pone sobre la mesa, que es distinto de los dos anteriores: una
  cosa NOMBRADA COMO EJEMPLO dentro de un paso no es lo mismo que una cosa
  que es el OBJETO del imperativo de ese paso. Si alguno de los ocho se
  mueve, va con correccion_v103 declarada y RECOMPUTAS. Si no se mueve
  ninguno, lo dices con la cifra y ya esta: no fuerces hallazgos.

- SI LAS CUATRO NO CABEN CON SUS GUARDAS COMPLETAS, la unica que puedes dejar
  para la vuelta siguiente es la TAREA 4, y lo dices con la cifra de lo que
  si hiciste. Las TAREAS 1, 2 y 3 no se recortan: la 1 es el arreglo de la
  escalada, la 2 es la adjudicacion que tiene una cifra publicada colgando, y
  la 3 son los registros.

- LO QUE NO SE TOCA. La deriva de contenido (26 nodos de 140, 32 pares de 87,
  acta 92 seccion 4.4), los siete nodos con guion, el bloque repetido de
  formalizar_un_proceso_ad_hoc y AHORA TAMBIEN los titulos gemelos por
  mayuscula que encontre yo (sistema_responsabilidad_gerencial y su _2, "El
  Sistema es tu Responsabilidad" contra "El Sistema es Tu Responsabilidad",
  los dos vivos) siguen ANOTADOS PARA ALEXIS Y SIN ENCARGAR, porque rozan el
  ALCANCE de la campana. Que conste ademas que Gate 0 tiene razon al dar 0:
  su guarda dice "titulo_concepto EXACTO duplicado" y esos dos titulos no son
  exactos. Citarlos como contraste, con su fuente nombrada, es correcto.

- LO QUE NO SE ABRE. No se toca el campo estado, que sigue sin voto por el
  acta 100 seccion 4.2. No se abre la fase 05 ni la 06. No se mueve ninguna
  operacion de fase. No se escribe ni se retira una sola arista: la TAREA 2 y
  la TAREA 4 son juicio y registro, no cirugia, igual que OP-E-03.

- UNA NOTA DE HIGIENE QUE NO ES UNA CAIDA, y que amplio con una medicion
  nueva: git status trae M en dataset/metadata/master_graph.json desde antes
  de que nadie toque nada, y NO es un cambio (mismos 8.391.653 bytes y mismo
  sha256 que HEAD, es el fin de linea de Windows). No lo commitees y no lo
  "arregles". Y lo que anado: si corres SOLO run_phase1.py, el fichero se va
  a 8.519.923 bytes y parece que has movido algo. Es el CICLO DE TRES ENTERO
  (run_phase1.py, etiquetas_de_cara.py --aplicar, sync_assets_web.py) el que
  lo devuelve identico byte a byte. La media corrida miente; mide con sha256
  al final del ciclo, no en mitad.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
