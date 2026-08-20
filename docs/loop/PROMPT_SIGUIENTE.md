Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion: simulacion previa sobre copia en memoria, Gate 0 y las
suites en verde tras cada tramo, caso positivo, la guarda 1B (ningun
absorbido puede ser semilla ni extremo de puente), y cero duplicadas o
auto-aristas NUEVAS tras resolver. Cualquier guarda en rojo, o cualquier
operacion cuyo texto no alcance para ejecutarse sin decidir, te detiene
y convoca al auditor.

AVISO DEL CREDITO, del acta de la vuelta 51, Y ES GRAVE: LA RACHA DE
CLASE O CIFRA ESTA EN UNA SEGUIDA. La vuelta 51 dejo DOS caidas de
cifra publicada (los contadores CORREGIDA N VECES de las filas 246, 247
y 248 sin cuadrar tras tachar sus cifras; y los ordinales de los cinco
declarados "al cerrar la vuelta 51" copiados de la corrida TRAS EL LOTE
A en vez de leidos de la salida que la propia celda cita). UNA CAIDA DE
CLASE O DE CIFRA PUBLICADA EN ESTA TANDA DETIENE EL BUCLE. Las reglas
de siempre, y esta vez al pie: toda cifra publicada se lee de la salida
del instrumento QUE LA CELDA CITA, corrida DESPUES del ultimo
movimiento; quien corrige una celda con contador CUADRA EL CONTADOR y
ADOSA la nota fechada (tu propia vara, D7 de la vuelta 50); los rotulos
se fechan a su corrida desde el principio; quien mueve una clase o
funde un acto corre el barrido 9.10 antes de cerrar.

====================================================================
TAREA 1: registros y correcciones adjudicadas (cinco puntos)
====================================================================
1.1. LOS CONTADORES DE LAS FILAS 246, 247 y 248 de
docs/plan/RECOMPUTO_3388.md (caida de cifra publicada, acta 51 seccion
3.1): sus cadenas tienen hoy OCHO, CINCO y OCHO tachados y los
contadores dicen SIETE, CUATRO y SIETE. Cuadralos con tachado
(~~SIETE~~ OCHO, ~~CUATRO~~ CINCO, ~~SIETE~~ OCHO) y ADOSA en cada
celda la nota fechada de la correccion de la vuelta 51 (fundio cuatro
actos y volteo cinco veredictos por P.16: puestos 820, 2426, 2523, 2662
y 498), sin reescribir las notas viejas, que estan fechadas y se
quedan. La vara es tu propio D7 de la vuelta 50.

1.2. LOS ORDINALES DE LOS CINCO DECLARADOS del registro de la vuelta 51
en docs/plan/03_FUSIONES.md (caida de cifra publicada, acta 51 seccion
3.2): la celda "Al cerrar la vuelta 51 son los actos 4, 21, 23, 27 y
28" trae los ordinales de la corrida TRAS EL LOTE A; la salida citada
(SALIDA_V51_TRAMO1_CIERRE.txt) imprime 3, 19, 21, 25 y 26. Corrige con
tachado, fecha y motivo (cifra que nacio mal: copiada de otra corrida).
En el MISMO registro, corrige la redaccion "las 25 combinaciones de
acto y superviviente viable se re-midieron": las combinaciones medidas
son 51 y el 25 es la cuenta de los actos mixtos (especie del rotulo,
acta 51 seccion 3.4).

1.3. EL ROTULO "hoy" DEL REGISTRO DE LA VUELTA 49 (acta 51, D10, con la
figura de la TAREA 1.2 de la vuelta 51): en docs/plan/03_FUSIONES.md,
la fila "los declarados 29, 32 y 36 (hoy 26, 28 y 32)" (hoy linea 683;
buscala por su texto). El 26/28/32 es la numeracion de la APERTURA de
la vuelta 49 (SALIDA_V51_TRAMO1_EN_CIERRE_V49.txt y las mediciones de
tu propio reporte 51): fecha el rotulo a esa corrida, cifras intactas,
con la nota de que al cerrar la 49 eran 24, 26 y 30 y al abrir la 51
eran 23, 25 y 29, cada una con su salida citada.

1.4. LAS DOS FAMILIAS DE FOTOS FECHADAS (adjudicacion del acta 51,
pregunta 4; D11):
  a) El apendice 95.1 de docs/INTRA_DOMINIO_INFORME.md es un CHECKPOINT
     DEL CRIBADO, no una tabla vigente: fecha su rotulo a su corte y su
     corrida, cierra su cadena con una nota fechada que declare que el
     mantenimiento por resta trato una foto como tabla vigente y
     termina aqui, y deja la medicion de hoy como CONTRASTE dentro de
     la nota (A 554, B 77, C 8, D 2.261, con el comando
     `python scripts/recomputar_marcador.py 2900` citado), NO como
     cifra vigente de la tabla.
  b) Las dos tablas "EL MARCADOR ... AL CERRAR LA VUELTA" de
     docs/plan/RECOMPUTO_3388.md (hoy lineas 1790 y 1837, registros de
     las vueltas 19 y 20) publican 575/83/8/2722 bajo "medido hoy".
     ANTES de fechar, verifica por git la cifra de su corrida: checkout
     del cierre de la vuelta 19 y de la 20, recomputa el marcador de
     cada estado, y compara con la PRIMERA cifra de cada cadena. Si
     calza, fecha el rotulo a esa vuelta y cierra la cadena con nota
     (misma figura que a). Si NO calza ni con su propia corrida, NO
     fechas: lo traes con las dos mediciones.
  El marcador vigente vive en las filas 246 y 1079 y en el 100.1, y en
  ningun otro sitio.

1.5. EL INSTRUMENTO DE LAS PUERTAS (adjudicacion del acta 51, pregunta
3): repara scripts/loop/vuelta48_puertas_en_el_lote.py con el TERCER
caso, MAS DE UNA PUERTA CON ALGUNA OBLIGADA A MORIR por la estructura
del acto (hoy los cuenta SALVABLES bajo un rotulo que dice "una sola
puerta" imprimiendo dos), con el texto viejo delante en el docstring.
Los dos actos afectados quedan DECLARADOS IMPOSIBLES POR PUERTA,
identificados por miembros (decision_cuando_fundar mas
evaluacion_capacidades_fundador mas tres_preguntas_carrera; y
enfoque_paso_a_paso_investigacion_mercado mas
evaluacion_mercados_objetivo mas screening_mercados_potenciales):
registralos en el registro del tramo como declarados que se acumulan
para el PARA_ALEXIS del cierre, junto a los cinco de siempre.

====================================================================
TAREA 2: OP-U-01, el tramo 1 con la guarda nueva y los carriles
adjudicados, y el tramo 2 si hay cuerda
====================================================================
2.1. LA GUARDA DE COLISIONES CAMBIA (acta 51, pregunta 2c): la cuenta
fija del encargo viejo SE RETIRA. Antes de cada lote corres
scripts/loop/vuelta51_colisiones_esperadas.py sobre la nomina re-medida
del dia: EL CENSO ESPERADO ES EL QUE LA SIMULACION IMPRIME, por PAR
RESUELTO (ratificado, acta 51 pregunta 1). Tras ejecutar, el censo real
del archivo entero tiene que calzar con la prediccion: una colision
real fuera de la prediccion te detiene.

2.2. LA LIMPIEZA P.16, con el carril del filo (acta 51, pregunta 2):
  - colision predicha cuyo veredicto arrastrado es A: se voltea a la
    clase del veredicto DIRECTO del par resuelto, citandolo como
    relectura conjunta, razon vieja entera pegada (la figura de los
    cinco de la vuelta 51).
  - colision predicha cuyo veredicto arrastrado es del FILO (B o C): NO
    se voltea por maquina. Su nodo muere o cambia de texto, asi que es
    la COLA DE RELECTURA POST FUSION de 08_VERIFICACION: RELEES el par
    resuelto EN EL MISMO ACTO con el veredicto directo como contraste,
    y la correccion declarada cita ESA relectura. Si la relectura
    encuentra que lo congelado es una pregunta de POLITICA de catalogo,
    el acto NO se funde: se declara y se acumula para la mesa.
  - marcador recomputado y barrido de la regla del aviso tras cada
    volteo, como siempre.

2.3. EL ACTO DEL EQUITY SE EJECUTA (adjudicado, acta 51 pregunta 2): el
superviviente es criterios_equity_split (el contenido manda, P.8, y tu
plan quedo escrito entero). La colision interna (el 502 A) se voltea a
D citando el 871. Las dos de fuera van por el carril del filo: relees
los pares resueltos criterios_equity_split contra reparto_inicial_equity
(hoy el 266 B del absorbido; el directo 754 es D) y contra
timing_equity_split (el 246 C; el directo 688 es D). Si alguna de esas
dos relecturas destapa politica viva, detienes ESTE acto, lo declaras y
sigues con los demas.

2.4. LAS DEMAS LECTURAS P.12 DEL TRAMO 1 (quedan 21 mixtos, 20 sin
adjudicacion previa) por la receta RATIFICADA: viables por parte A
clique con mixto fuera; entre viables elige por CONTENIDO como P.8 lo
define (el texto de los pasos, el material propio y el padre declarado
EN LAS RAZONES del archivo cuentan como contenido; el conteo de
caracteres del resumen NO desempata); si el contenido calla, EL
CABLEADO DECIDE SOLO (P.8, ejemplar 328); si tambien empata, DECLARAS
el acto como empate sin vara y lo traes. Los choques de letra contra
aritmetica se registran con sus puestos (manda la aritmetica). Con
estas notas:
  - LOS CUATRO MIXTOS CON PAR EN B (entre ellos el 703 del S&OP): lee
    la razon del B ANTES de fundir (acta 51, pregunta 5). Condicion de
    TEXTO: la relectura post fusion decide y el B se corrige citandola.
    Pregunta de POLITICA: el acto se DECLARA, no se funde, y se acumula
    para la mesa.
  - LOS REGALOS ESTRATEGICOS: corre P.8 en su orden (acta 51, pregunta
    6): lee las razones 799, 251 y 1348 y los tres textos buscando
    material propio o padre declarado; si el contenido calla, cableado
    solo; si empata todo, DECLARA y trae.
  - LOS DOS BLOQUEADOS POR PUERTAS de 1.5 no se funden: ya estan
    declarados.
2.5. LOS CINCO DECLARADOS SIGUEN DECLARADOS y ninguno se funde,
identificados por sus miembros como en el encargo anterior.

2.6. Si hay cuerda tras cerrar el tramo 1 ENTERO (fundidos, declarados
o detenidos todos sus actos, con registro), abre el TRAMO 2 de 50 actos
por la misma vara: nomina RE-MEDIDA al abrirlo con recomputo_3388.py y
--salida fuera de docs/plan, el orden impreso, la guarda de los cuatro
ajenos, P.5 por acto, y las guardas de siempre.

2.7. AL CIERRE: Gate 0 por el ciclo escrito y las suites en verde, el
marcador recomputado del archivo, EL BARRIDO DE LA REGLA DEL AVISO
corrido despues del ultimo movimiento (y el barrido CUADRA CONTADORES y
ADOSA NOTAS FECHADAS donde toque una celda con contador), y el registro
del tramo en 03_FUSIONES.md con sus cifras LEIDAS DE LA SALIDA QUE CADA
CELDA CITA y sus rotulos fechados a su corrida.

Reporte con la apertura medida antes de la primera operacion, los
discutibles marcados ANTES de saber si aciertas, y lo que la vuelta NO
hizo dicho en vez de callado.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
