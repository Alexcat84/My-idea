Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion: simulacion previa sobre copia en memoria, Gate 0 y las
suites en verde tras cada tramo, caso positivo, la guarda 1B (ningun
absorbido puede ser semilla ni extremo de puente), y cero duplicadas o
auto-aristas NUEVAS tras resolver. Cualquier guarda en rojo, o cualquier
operacion cuyo texto no alcance para ejecutarse sin decidir, te detiene
y convoca al auditor.

AVISO DEL CREDITO, del acta de la vuelta 50: LA RACHA DE CLASE O CIFRA
VUELVE A CERO (la vuelta 50 salio limpia de esa especie). Reglas de
siempre: toda cifra publicada sale del instrumento corrido EN ESTA
vuelta; toda cita de linea a un fichero que esta vuelta edite se mide
DESPUES de la ultima edicion; quien mueve una clase o funde un acto
corre el barrido 9.10 (el sucesor vuelta50_barrido_910.py, con las
cifras viejas DE HOY) ANTES de cerrar la vuelta, sobre toda tabla
vigente que cite la clase, el marcador o el retrato. Y LA REGLA
ADJUDICADA NUEVA (acta 50, pregunta 5): una tabla propia que envejece
dentro de la vuelta se arregla segun lo que envejecio: si es tabla
vigente de estado, la CIFRA con tachado por 9.10; si la cifra fue
exacta para su corrida y lo que envejecio es el rotulo ("hoy"), se
corrige el ROTULO fechandolo a su corrida y la cifra se queda. Al
escribir registros nuevos, fecha los rotulos a su corrida desde el
principio (di "al abrir la vuelta N", no "hoy").

====================================================================
TAREA 1: registros y correcciones adjudicadas (tres puntos)
====================================================================
1.1. LA FILA DEL REGISTRO DE LA VUELTA 49 QUE DECIA 25 (adjudicacion
del acta 50, pregunta 4): en docs/plan/03_FUSIONES.md, la fila
"lecturas P.12 encargadas y NO hechas: 25" del registro de la vuelta 49
(hoy linea 680; buscala por su texto, no por el numero de linea) es una
cifra publicada equivocada de aquella vuelta: la cuenta buena al cierre
de la 49 era 26, medida por miembros (SALIDA_V50_TRAMO1_POR_MIEMBROS.txt)
y re-derivada por el auditor. Corrigela con tachado, fecha y motivo,
citando esa salida y el acta 50 como su relectura conjunta. NO toques
la fila hermana del registro de la vuelta 50 que dice 25 al cierre: esa
esta bien medida.

1.2. EL ROTULO "hoy" DE LA TABLA DE LOS CINCO DECLARADOS (acta 50,
seccion 3.1, con la figura de tu propio D6): en el registro de la
vuelta 50 de 03_FUSIONES.md, la columna "numero en la vuelta 48 / hoy"
trae los numeros de la APERTURA (7, 24, 26, 30, 31) y el cierre de la
misma vuelta los re-midio distintos (6, 23, 25, 29, 30,
SALIDA_V50_TRAMO1_CIERRE.txt). Las CIFRAS no se tocan (fueron exactas
para su corrida): corrige el ROTULO fechandolo a su corrida ("al abrir
la vuelta 50, SALIDA_V50_TRAMO1_POR_MIEMBROS.txt"), con la nota de que
al cierre eran los de la otra salida. Revisa con la misma vara la linea
del "hoy el acto 156" de los imposibles, en el mismo registro.

1.3. EL PARENTESIS DE LA FILA 528 DE docs/plan/RECOMPUTO_3388.md (acta
50, seccion 3.2): la celda del checkpoint ii conserva "(... 525)" sin
tachar en sus dos parentesis mientras su nota vigente del cierre
publica 522 y 522. Completa el tachado (525 tachado, 522 vigente) en
los DOS parentesis para que la pareja mostrada calce con la nota, sin
tocar la cadena de notas. Es correccion de forma adjudicada, no cifra
nueva: la vara es tu propio tratamiento de las filas 246 y 248.

====================================================================
TAREA 2: OP-U-01, las 25 lecturas P.12 del tramo 1 por la receta
RATIFICADA, y el tramo 2 si hay cuerda
====================================================================
2.1. LA RECETA QUEDA RATIFICADA (acta 50, preguntas 1 a 3, sin doctrina
nueva) y rige para los 25 mixtos que quedan:
  - dado un superviviente S: PARTE A = S mas los miembros con arista A
    contra S; MIXTOS = los miembros sin arista A contra S. S es VIABLE
    si su parte A es clique A y deja al menos un mixto fuera.
  - entre los VIABLES elige por CONTENIDO (las dos reglas de la pagina
    mas P.8 con la vara de las puertas). En la estrella el centro casi
    nunca es viable y muere UNA vez, absorbido por el viable elegido.
  - CHOQUE letra contra aritmetica (los cinco medidos en cuatro actos,
    hoy 3 con dos, 27, 28 y 29): MANDA LA ARITMETICA. La formula
    *Sobrevive X* es cierre de una razon de PAR y el racimo decide (lo
    escribe el propio 2237); X sigue vivo aunque no absorba. Registra
    cada choque en el registro del tramo con sus puestos citados.
  - por cada mixto: lee contra el superviviente elegido y decide ENTRA
    (comparte procedimiento) o CONTINUA (comparte la idea en lineas).
    Cada veredicto a la tabla del REGISTRO DEL TRAMO de 03_FUSIONES.md
    (mixto, superviviente, veredicto, citas).
  - si ENTRA: fundes la parte A mas el mixto en UNA operacion, con las
    guardas de siempre. Si CONTINUA: fundes la parte A sola; declaras
    la arista con id RESUELTO (P.9) SIN ejecutarla, poda del solape
    anotada a la fase 04; y LIMPIAS EN EL MISMO ACTO la colision que la
    fusion fabrique (P.16): correccion declarada del A viejo con la
    razon vieja entera pegada por maquina, citando la lectura P.12 como
    su relectura conjunta, marcador recomputado, y el barrido de la
    regla del aviso. ESPERA una colision por cada CONTINUA sobre mixto
    CON forma y CERO por cada ENTRA; una colision que no calce con esa
    cuenta te detiene.

2.2. LOS CINCO DECLARADOS SIGUEN DECLARADOS y ninguno se funde.
IDENTIFICALOS POR SUS MIEMBROS: obtencion_compromiso y hermanos
(colision medida); mejora_del_sistema_responsabilidad_gerencial y
hermanos (el 2572 llama PROVISIONAL a su ganador); dia_cero_defectos y
hermanos (el 2525 manda decidir, no apilar); domina_lo_que_compras con
investiga_con_fuentes_objetivas (imposible por puerta);
cultura_climatica_innovacion con cultura_de_innovacion (colision
medida). La vara de las puertas sigue entera: el contenido manda la
eleccion, el GATE 0 manda lo ejecutable, lo que choca se declara y se
acumula para el PARA_ALEXIS del cierre.

2.3. Si hay cuerda tras cerrar el tramo 1 ENTERO, abre el TRAMO 2 de 50
actos por la misma vara: nomina RE-MEDIDA al abrirlo con
recomputo_3388.py y --salida fuera de docs/plan, el orden impreso, la
guarda de los cuatro ajenos, P.5 por acto, y las guardas de siempre.

2.4. AL CIERRE: Gate 0 por el ciclo escrito y las suites en verde, el
marcador recomputado del archivo, EL BARRIDO DE LA REGLA DEL AVISO
corrido despues del ultimo movimiento, y el registro del tramo en
03_FUSIONES.md con sus cifras impresas por instrumento y sus rotulos
fechados a su corrida (actos fundidos, lecturas P.12 con veredictos,
colisiones limpiadas, nodos deprecados, enlaces, lo que quede).

Reporte con la apertura medida antes de la primera operacion, los
discutibles marcados ANTES de saber si aciertas, y lo que la vuelta NO
hizo dicho en vez de callado.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
