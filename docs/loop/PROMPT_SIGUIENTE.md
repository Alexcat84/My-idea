Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion. EL MODO AUSTERO SIGUE ATANDO: reporte con tope de 80
lineas, medido con wc -l AL CIERRE y pegado en el propio reporte.

El acta de la vuelta 103 esta en docs/loop/ACTA_AUDITOR.md a partir de la
linea 36807. En resumen, y sin adornarlo:

LA BUENA PRIMERO, Y ES DOBLE. CERO CAIDAS DE REPORTE POR SEGUNDA VUELTA
SEGUIDA, Y NO POR NO HABER MIRADO: repase tus once afirmaciones una por una
contra su fichero. La apertura sellada la corri yo (VERDE, nueve ficheros
nacidos en 72142551, padre 715130c2). La cabecera con --comparar: 9 filas, 0
distintas, 0 ausentes. Las siete celdas las medi por mi cuenta: censo 3.853 /
3.188 / 665, aristas 9.190 / 9.169 / 18.359 / 9.813, cero auto-aristas, Gate 0
OK con alcanzabilidad 100,0%, motor 25/25, web 80 (80) / 1.030 y 3 skipped,
tsc EXITCODE 0. El marcador sin mover (A 551 / B 72 / C 5 / D 2.760, cero
huecos). Y el cierre de OP-E-03 lo reconte con mi propio contador: n=183,
A 3 B 2 C 1 (par 111) D 177, direccion 87 / 96 (52,5%), invertidas 2 (16 y
114), nueve correcciones vivas. Calza al digito, y la aritmetica de los dos
saltos tambien: 90/93 menos el 28 y el 40 da 88/95, y menos el 31 da 87/96.

Y LA SEGUNDA BUENA ES QUE TU ARREGLO FUNCIONA, Y NO ME FIE DE TU MUTACION:
HICE LA MIA. Copie el REPORTE.md a dos ficheros aparte y le pegue a cada uno
la misma frase falsa sobre el mismo fichero, una vez con el nombre pelado y
otra con docs/loop/ delante. LAS DOS DAN ROJO CON EXIT 1, y la pelada declara
en su salida que la resolvio. Y medi la cobertura donde dolia: corri tu
tallador arreglado contra el reporte que lo motivo (--commit f253842b) y pasa
de VER 1 DE 17 a VER 14 DE 17. El cerco ya no es ciego. Tambien conte a mano
la cifra del 31 que publicaste en docs/plan/, que es donde una cifra si
acumula racha: los pasos de causas_comunes_vs_especiales sin contraparte en
NINGUN paso de control_estadistico_del_proceso son el 6, 8, 9, 10, 11, 12,
13, 14 y 15. NUEVE EXACTAS. Tu cifra es correcta. Y la aditividad: 04_ENLACES
0 borradas / +4, PENDIENTES 0 borradas / +65, OPERACIONES.jsonl 71 filas
antes y despues con una sola tocada, un solo campo, y el valor viejo prefijo
estricto del nuevo; estado sin mover en las 71; y en el tramo 1 los puestos
28, 31 y 40 SOLO GANAN la clave correccion_v103, con la razon vieja intacta.

AHORA EL HALLAZGO GORDO, Y NO TE LO COBRO PORQUE ES MIO: EL CERCO PASO DE
CIEGO A GRITON. Corri tu tallador arreglado sobre el REPORTE.md de la vuelta
102 y termina en ROJO, 6 HALLAZGOS, EXIT 1. Fui a los seis. LOS SEIS SON
FALSOS. Los seis viven en el mismo parrafo (el bloque entero de tu TAREA 1 de
aquella vuelta, lineas 23 a 39, un solo parrafo con 3 citas y diecisiete
palabras de veredicto) y los seis nacen del emparejamiento: la palabra VERDE
de "contradice la afirmacion VERDE del reporte de la 101" es NARRACION DE UNA
MUTACION, no un veredicto sobre el fichero citado despues. Y esas mismas
afirmaciones yo las verifique una por una en el acta 102 y las di ciertas.

NO ES CULPA TUYA Y LO ESCRIBO EN EL ACTA CON MI NOMBRE. Mi encargo (1.4) fue
literal: "no te pido que cambies la preferencia por la cita posterior, que
esta declarada y es defendible; te pido que la salida DIGA con cual emparejo
y por que regla". Hiciste exactamente eso y lo hiciste bien. El fallo de
disenno es mio. PERO ES URGENTE, y por eso va bloqueante: mi propia 1.5 dice
"si alguna queda roja al cierre, NO CIERRES LA VUELTA", o sea que un reporte
que narre una mutacion (y cada vuelta con caso positivo narra una) puede
PARAR LA VUELTA por seis falsos sin que nada este mal. Tu reporte 103 se
salvo por composicion, no por disenno: solo tiene 4 palabras de veredicto y
ningun parrafo narrado.

Y EL SEGUNDO HALLAZGO, TAMBIEN MIO: TU MUESTRA DE LA TAREA 4 NO SE RE-CORRE.
Corri hoy vuelta103_tarea4_relectura_ciega_centro.py --modo blind y da 13,
19, 10, 29, 15, 35, 31, 32. La que commiteaste es 13, 19, 10, 31, 15, 36, 35,
32. La causa, medida: el instrumento decide el flanco con direccion_efectiva,
y la propia TAREA 4 escribio correccion_v103 sobre el 31, que salto de flanco
y arrastro la ventana. TU SELECCION ERA CORRECTA CUANDO LA SACASTE Y LA
REHICE A MANO PARA COMPROBARLO: con los 22 elegibles de entonces la mediana
del flanco RESUELTA cae en 84,35 y los cuatro mas cercanos son 10, 31, 19 y
13; con los 7 del otro flanco la mediana es 80,0 y los cuatro mas cercanos
son 35, 15, 36 y 32. Exactamente lo publicado. Ninguna cifra es falsa. Pero
una salida que no se puede re-correr no es evidencia auditable, y es la misma
familia que la guarda que se envenenaba sola de la vuelta 102. Lo registro
como INSTRUMENTO QUE SE MUEVE BAJO SU PROPIO RESULTADO, con la caida a mi
nombre: te mande sacar la muestra Y corregir dentro de ella en la misma tarea
sin decirte que la congelaras.

Y AHORA MI RELECTURA CIEGA. Lei cuatro puestos a ciegas con instrumento
propio (docs/loop/_auditor_v103_ciega.py, salidas _ciega_blind.txt y
_ciega_reveal.txt), volcando entregable y pasos sin clase, sin direccion, sin
razon y sin paso casado, adjudicando por escrito y destapando despues.
Declaro el limite de mi metodo en vez de esconderlo: mi volcado rotula los
nodos A y B en el orden madre_de_la_bolsa / hijo_de_la_bolsa, o sea que veo la
propuesta del barrido aunque no vea la lectura. Ademas re-adjudique el 31,
declarado como re-adjudicacion porque lei tu razon antes.

EL 34 Y EL 37 COINCIDEN. En el 34 tu paso 4 habla del MVP de BAJA fidelidad y
el hijo es el de ALTA, que arranca donde acaba el otro; en el 37 el hijo monta
campanas por un canal que la madre no nombra en ningun paso. NO RESUELTA los
dos, como tienes escrito.

EL 16 COINCIDE Y DECLARO MI RESERVA. Adjudique que la direccion esta INVERTIDA
(el proceso entero de venta de franquicias es la madre y la primera llamada el
hijo) y tu registro dice exactamente eso. Mi reserva: dude entre eso y NO
RESUELTA por 9.6.3, porque tu paso 1 manda DISENNAR el flujo y el hijo EJECUTA
una llamada. Tu letra es la mas fuerte y cedo.

EL 31 ESTA BIEN MOVIDO Y LO VERIFIQUE CONTANDO. Nueve de los quince pasos sin
contraparte, exceso de genero de la especie 172/161. Coincido.

EL 29 DISCREPA, Y ES LA MISMA ESPECIE QUE EL 28 QUE ACABAS DE ACEPTAR.
abolir_inspeccion_masiva contra control_estadistico_del_proceso, paso casado
5, tu registro dice RESUELTA. El paso 5 dice "Reduce gradualmente la
inspeccion masiva A MEDIDA QUE tu proceso demuestre estar en control
estadistico". El imperativo es reducir la inspeccion; el control estadistico
es la CONDICION de cuando, no el OBJETO del verbo, igual que "fase Adopt" era
el ejemplo de CUANDO en el 28. Y 9.6.3 da procedimiento propio a cada lado (tu
madre: costo de la inspeccion al 100%, causa raiz, muestreo aleatorio,
redisenno, reserva del 100% para casos criticos; el hijo: graficos X-barra y
R, capacidad, dispersion contra nivel, intervencion en el sistema).

Y TE ESCRIBO YO MISMO LO QUE JUEGA EN MI CONTRA, PORQUE ES FUERTE. La senal de
los entregables del 9.6.2 apunta al otro lado: tu madre entrega "Plan de
transicion a muestreo aleatorio Y CONTROL ESTADISTICO DE PROCESO", dos
productos, y el hijo entrega el grafico de control, que es la pata de SPC.
Es el patron del 2.215. O sea: el primer brazo del test dice NO y la senal de
verificacion dice SI. Por eso va a RELECTURA CONJUNTA y no como caida, y por
eso la cifra 87/96 no la toco yo.

- TAREA 1, LOS REGISTROS DEL ACTA 103, en docs/PENDIENTES.md, seccion propia,
  con la composicion del anadido TALLADA con
  scripts/loop/tallar_composicion_salida.py y su caso positivo commiteado con
  su fichero de salida. Numera los subapartados COMO ESTAN AQUI. Va primera
  porque es barata y porque los registros no se quedan nunca fuera, pero
  ejecutala DESPUES de la TAREA 2 si prefieres tener la guarda arreglada
  antes de escribir: el orden de ejecucion lo eliges tu, el de entrega no.
  (1.1) MI CERCO GRITON, nombrado como caida MIA y sin borrar texto viejo: los
  6 hallazgos falsos sobre el reporte 102, con la cifra de cobertura al lado
  (de 1 de 17 a 14 de 17) para que se vea que el ensanche SI sirvio y lo que
  falla es el emparejamiento, no el cerco.
  (1.2) LA MUESTRA QUE NO SE RE-CORRE, tambien como caida MIA de encargo, con
  las dos listas (la commiteada y la de hoy), la causa medida y la constancia
  de que la seleccion original era correcta y la rehice a mano.
  (1.3) LO QUE HICISTE BIEN Y NO QUIERO QUE SE PIERDA: cero caidas de reporte
  por segunda vuelta seguida tras un repaso mio afirmacion por afirmacion, el
  arreglo del tallador probado con mi propia mutacion de dos variantes, la
  cifra de los nueve pasos del 31 verificada a mano, y la aditividad con
  estado sin mover en las 71 filas.
  (1.4) EL 29, anotado como ABIERTO Y EN RELECTURA CONJUNTA, con mi caso y mi
  contra-caso, no como resuelto en ningun sentido hasta que la TAREA 2 lo
  cierre. Y cuando lo cierres, anota ahi mismo el resultado.
  (1.5) EL PUNTO CIEGO NUEVO, con sus cifras: de las 26 RESUELTA efectivas del
  tramo 1, QUINCE no han sido releidas nunca (1, 2, 4, 6, 8, 9, 14, 17, 18,
  20, 21, 24, 25, 38, 39), y el tramo 2 tiene 33 RESUELTA escritas todas antes
  de que la especie del 28 existiera.

- TAREA 2, BLOQUEANTE, LA CALIBRACION DEL CERCO. No es una escalada nueva: es
  el segundo tramo del mismo arreglo, y la letra del fundador del 29 ago
  ("toda tabla y toda cifra del reporte en fases mecanicas se genera contando
  su fichero de salida") la cubre por extension: una guarda que grita seis
  falsos no esta contando, esta adivinando.
  (2.1) EL CASO A BATIR TE LO DEJO MEDIDO Y NO HAY QUE INVENTARLO: el
  REPORTE.md de la vuelta 102 (git show f253842b:docs/loop/REPORTE.md), cuyas
  afirmaciones yo verifique una por una en el acta 102 y son TODAS CIERTAS.
  DESPUES DEL ARREGLO ESE REPORTE TIENE QUE DAR VERDE, con exit 0. Pega la
  salida antes y despues.
  (2.2) Y LOS DOS NEGATIVOS SIGUEN TENIENDO QUE DAR ROJO: tu mutacion de dos
  variantes de la vuelta 103 (misma frase falsa, mismo fichero, nombre pelado
  y con prefijo) NO PUEDE DEJAR DE SALTAR. Si tu calibracion apaga el falso
  positivo apagando tambien el verdadero, no sirve: correla y pegala.
  (2.3) EL CRITERIO LO PONGO YO Y EL PATRON LO ELIGES TU. Lo que exijo es que
  el emparejamiento deje de tomar como veredicto lo que es narracion. La via
  que a mi me parece mas corta, y no te ata: emparejar por FRASE y no por
  PARRAFO (la cita tiene que estar en la misma oracion que la palabra), y
  cuando no la haya en la oracion, contar la palabra en la cobertura pero NO
  levantar hallazgo. Si eliges otra, escribe en el docstring por que, y mide.
  (2.4) LA COBERTURA SE VUELVE A PUBLICAR CON EL PATRON NUEVO, sobre el
  reporte 102 y sobre el tuyo. Si el arreglo baja la cobertura, DILO CON LA
  CIFRA en vez de esconderlo: una cobertura menor y honesta vale mas que
  catorce emparejamientos de los que seis mienten.
  (2.5) CORRELA AL CIERRE DE LA VUELTA junto con las otras dos guardas,
  despues de tu ultima edicion. Si alguna queda roja al cierre, NO CIERRES LA
  VUELTA. La regla de la vuelta 100 sigue viva.

- TAREA 3, LA RELECTURA CONJUNTA DEL 29, con mi caso Y mi contra-caso delante.
  Es adjudicacion, no medicion, y no la decido yo solo: AUDITOR.md 1.3 dice
  que tu verificas contra el grafo y decides con la vara.
  (3.1) LEE LOS DOS NODOS ENTEROS, no mis citas: abolir_inspeccion_masiva
  contra control_estadistico_del_proceso.
  (3.2) LEE 9.6.2 Y 9.6.3 ENTEROS. Mi caso descansa en el primer brazo del
  test de reconocimiento y en la simetrica del 9.6.3; MI CONTRA-CASO, que te
  escribo yo, descansa en la senal de los entregables del propio 9.6.2, y es
  el patron del 2.215. LAS DOS PATAS SON DE LA MISMA REGLA. Esto es lo que
  tienes que resolver, no cual de los dos tiene mas ganas.
  (3.3) DECIDE, Y PUEDES DECIDIR CONTRA MI. Si sostienes RESUELTA, escribe la
  razon citando la regla por su numero y yo cedo en el acta, como cedi en el
  puesto 5 y como acabo de ceder en el 16. Si me das la razon, va con
  correccion_v103 (no v104: la vuelta que la origina es esta relectura, y si
  prefieres correccion_v104 dilo y justifica el numero) DECLARADA, sin borrar
  el texto viejo, y RECOMPUTAS con scripts/loop/contar_cierre_efectivo.py en
  los tres sitios aditivos. Si se mueve, la cifra pasa de 87 / 96 a 86 / 97, y
  entonces TODA cifra publicada que dependa de ella se vuelve a tallar, no se
  edita a mano.
  (3.4) Y SI DECIDES CONTRA MI, DILO TAMBIEN EN EL 28. Si el argumento de los
  entregables gana aqui, tengo que saber si el 28 y el 40 sobreviven a ese
  mismo argumento o si hay que reabrirlos. No los reabras por tu cuenta:
  escribe si el argumento los toca y lo adjudico yo en la vuelta siguiente.

- TAREA 4, EL CONGELADO DE LA MUESTRA Y EL BARRIDO POR LA ESPECIE DEL 28. Es
  la relectura al doble que manda la 1.2 cuando una discrepancia aparece fuera
  de los discutibles marcados (el 29), y por tercera vez seguida NO puede ir
  por donde ya se fue: ni por los extremos (vuelta 102) ni por el centro
  (vuelta 103).
  (4.1) PRIMERO CONGELA LA MUESTRA, que es barato. Que el instrumento de
  muestreo acepte una lista explicita de puestos (--puestos) o fije el flanco
  contra un commit dado, de modo que la salida commiteada SE PUEDA RE-CORRER Y
  DAR LO MISMO despues de que las correcciones de la propia vuelta entren.
  Caso positivo: re-corre la muestra de la vuelta 103 con el modo congelado y
  que devuelva 13, 19, 10, 31, 15, 36, 35, 32, la commiteada, no la de hoy.
  (4.2) DESPUES EL BARRIDO, Y ES DIRIGIDO, NO CIEGO. Sobre las QUINCE RESUELTA
  del tramo 1 que nadie ha releido nunca (1, 2, 4, 6, 8, 9, 14, 17, 18, 20,
  21, 24, 25, 38, 39) y las TREINTA Y TRES RESUELTA del tramo 2, cuarenta y
  ocho en total, que caben de sobra bajo el lote de 80 del modo austero. Para
  cada una, UNA SOLA PREGUNTA, la del 28: en el paso casado, la cosa que el
  hijo desarrolla, es EL OBJETO DEL IMPERATIVO de ese paso, o esta nombrada
  como EJEMPLO, COMO CONDICION o dentro de una SUBORDINADA de cuando? Una
  linea por par en el fichero de salida, con el verbo del paso y el objeto
  citados literalmente para que yo pueda cotejarlos sin abrir el nodo.
  (4.3) Y SOLO LAS QUE SALGAN "NO ES EL OBJETO" VAN A LECTURA ENTERA, a ciegas
  y con las dos patas del 9.6.2 (el primer brazo Y la senal de los
  entregables, que es justo lo que el 29 pone en tension) mas 9.6.3. Las que
  se muevan van con correccion declarada y RECOMPUTAS. Si no se mueve
  ninguna, lo dices con la cifra y ya esta: no fuerces hallazgos.
  (4.4) Y DEJAME EL CENSO EN UN FICHERO, que hasta hoy lo he reconstruido yo a
  mano de las actas. Un JSONL o un txt con, por puesto de OP-E-03, en que
  vuelta se releyo y por que instrumento. Sin el, la proxima "relectura al
  doble" vuelve a elegir a ojo y a repetir puestos.

- SI LAS CUATRO NO CABEN CON SUS GUARDAS COMPLETAS, lo unico que puedes partir
  es el barrido de la 4.2: haz el tramo 1 entero (las quince) y deja el tramo
  2 para la vuelta siguiente, diciendolo con la cifra de lo que si hiciste.
  Las TAREAS 1, 2 y 3 y el congelado de la 4.1 no se recortan: la 2 es una
  guarda bloqueante que puede parar la vuelta por falsos, la 3 tiene una cifra
  publicada colgando, la 1 son los registros y la 4.1 es de una tarde.

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
  HEAD; lo volvi a medir hoy). No lo commitees y no lo "arregles". Y si corres
  SOLO run_phase1.py el fichero cambia de tamano y parece que has movido algo:
  es el CICLO DE TRES ENTERO el que lo devuelve identico byte a byte. Lo corri
  entero hoy y volvio al mismo sha256.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
