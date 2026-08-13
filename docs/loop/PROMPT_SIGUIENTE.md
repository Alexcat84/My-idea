Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. Ficheros del cribado solamente; docs/plan/ solo lectura.
MODO DE CIERRE: cero reparaciones.

====================================================================
TAREA 1: registros de la vuelta 3 del auditor
====================================================================
1. CORRECCION DECLARADA EN EL 9.28.1 (adjudicada en el acta vuelta 3):
   dos cifras secundarias del barrido del cuerpo no reproducen con
   instrumento independiente. La cota titular (6 de 234 = 2,6 %), la
   tasa secundaria de 2,9 % y la leccion de las dos cotas quedan como
   estan; NO se tocan.
   a) EL 204: con los tres fragmentos declarados (total, of, value) el
      recomputo del auditor da 209 (pares del universo fuerte cuya
      senal no se reduce a esos tokens; replicando la logica del
      script sobre el grafo, corte 2800, dominio quality). Ningun
      conjunto natural de fragmentos da 204. Re-corre con instrumento
      declarado: si tienes el comando exacto que produce 204,
      publicalo al lado de la cifra; si no, corrige con tachado (sin
      borrar) 204 a 209 en los dos lugares del 9.28.1 donde aparece, y
      6 de 204 = 2,9 % a 6 de 209 = 2,9 % (la tasa sobrevive
      identica). Deja el comando o la definicion exacta al lado.
   b) EL 59 DE BENCHMARKING: el recomputo del auditor da 20 pares
      fuertes de quality con el token benchmarking al corte 2800 (por
      raiz benchmark* son 25 pares y 24 nodos; sumando todos los
      dominios no core da 34; nada da 59). El ranking cualitativo
      (benchmarking al frente, luego sigma, pareto, lean) se sostiene.
      Igual que en (a): comando exacto que produzca 59, o correccion
      con tachado a la cifra que tu instrumento declarado reproduzca.
   La correccion se registra como manda la casa: tachado sin borrar,
   correccion declarada con su comando, y la leccion en una linea.
2. NADA MAS DE REGISTRO: los discutibles 2747 y 2756 quedaron
   adjudicados D sin correccion (acta vuelta 3, criterio del paso
   entero propio); las preguntas del Consejo de Calidad y de la
   responsabilidad gerencial siguen abiertas y la cola las trae sola,
   no las adelantes.

====================================================================
TAREA 2: CRIBADO CONTINUO hasta el checkpoint 2.900
====================================================================
Del 2801 al 2900 (python scripts/volcar_pares.py 2801 2806 para
retomar). La cola en orden y sin saltos. Manten el barrido de familia
antes de dictaminar cada par, como lo sistematizaste desde el 2.567:
los dictamenes citan a sus hermanos. Convencion del contador de
mutuas, ahora explicita (acta vuelta 3): solo los casos nuevos abren
numero; las mutuas de gemelos ya en cumulo no lo mueven. El contador
va en diecisiete (la ultima fue el 2.666).
Reporte completo EN el checkpoint, escrito en docs/loop/REPORTE.md:
marcador recomputado, tasa por dominio, vara por tramo, familias del
9.3 al dia con su especie de ganador, figuras al dia (fusiones mutuas,
senal del idioma, perdidas de nombre a reponer), y los discutibles
marcados ANTES de saber si aciertas, para la relectura ciega del
auditor. Checkpoint compacto tambien al informe (seccion 95), como el
94. Si la sesion alcanza, sigue hacia el 3.000 con la misma regla.
Los hallazgos que no puedan esperar, al mensaje del commit.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
