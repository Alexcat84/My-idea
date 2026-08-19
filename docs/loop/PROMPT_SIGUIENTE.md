Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
(El acta de la vuelta 43 verifico el arbol LIMPIO y todo pusheado; si
git status muestra algo, PARAS y lo traes antes de seguir.)

TAREA 1, registros, en este orden:
1. En docs/plan/02_DESTEJIDOS.md, bajo el registro de cierre de la
   vuelta 43, la seccion breve fechada de la auditoria: la vuelta 43
   auditada ENTERA por el acta de la vuelta 43 (docs/loop/
   ACTA_AUDITOR.md, empieza en la linea 9137, leela hoy y cita las
   lineas que uses), con CERO caidas del ejecutor, ciega 6 de 6
   (supervivientes del 341, 344 y 361, la D del 599, las condiciones
   y las costuras), los siete discutibles adjudicados A FAVOR, y LA
   RACHA DE CAIDAS DE REPORTE ROTA A CERO por el primer reporte
   limpio. La caida de acta del 0 VIVOS es del AUDITOR y ya esta
   contada en su metrica: no se te carga a ti.
2. LA CORRECCION ENCARGADA DE LA GLOSA DE LA SENAL, por encargo
   escrito del acta de la vuelta 43 (seccion 4, punto 2): en
   scripts/loop/vuelta42_senal_antes_despues.py, SOLO el bloque de
   prosa que arranca en "Y LO QUE LA CIFRA SOSTIENE Y NADA MAS" (hoy
   en la linea 116) se reescribe para decir lo que las mediciones
   sostienen: que con el corte quieto la senal puede SUBIR O BAJAR
   con la fusion (medido en la vuelta 43: 331 quieta en 0, 341 menos
   0,7, 344 mas 1,7, 361 menos 9,4 y APAGADA), que lo que la mueve es
   si las piezas que entran reparten vocabulario entre los dos
   bloques o lo concentran en uno, y SE CONSERVA ENTERA la
   advertencia de que la cita no se descarta: el instrumento CITA Y
   NO JUZGA y la lectura se hace con el texto delante. La logica de
   medicion, el umbral 44 y el formato de las cifras NO SE TOCAN NI
   EN UN CARACTER. Correccion declarada: el texto viejo de la glosa
   va verbatim en el mensaje del commit. VERIFICACION: re-corre el
   instrumento sobre el acto 361 con los MISMOS refs de la vuelta 43
   (antes ed61c8f0, despues el fichero de hoy) y sella la salida en
   docs/loop/SALIDA_V44_GLOSA_VERIFICADA.txt; todas las cifras deben
   salir IDENTICAS a docs/loop/SALIDA_V43_ACTO361_SENAL.txt y solo la
   glosa distinta. Si alguna cifra se mueve, REVIERTES y PARAS.
3. No hay caida de reporte que corregir: el reporte de la 43 salio
   limpio contra la corrida entera del auditor. Se dice asi y no se
   rellena la casilla.

TAREA 2, OP-D-06 terminada: los TRES actos que faltan y el CIERRE de
la operacion, con la misma forma de tres commits por acto que la
vuelta 43 dejo asentada (primer commit lectura, plan sellado,
simulacion y verificador, pusheado ANTES de fundir; segundo commit la
fusion APENAS el ciclo este verde, con P.16 si la simulacion reporta
arista interna, reanclar entre la fusion y run_phase1, ciclo Gate 0 de
TRES comandos MAS EL CUARTO porque toda fusion cambia el censo, con el
4 ANTES del 3, suites y casos positivos; tercer commit costuras post
fusion, relecturas B o C que vuelvan y registro de cierre):
1. La apertura medida antes del primer acto nuevo (regla 1) y
   commiteada sola. Debe dar: marcador A 575, B 81, C 8, D 2.724 en
   n 3.388; grafo 3.853 ficheros, 3.527 vivos, 326 deprecados,
   16.887 enlaces; cola 1.493. Son las cifras del cierre de la 43
   verificadas por el acta; si tu medicion difiere, PARAS y lo
   declaras.
2. ACTO 392 (metricas_de_adquisicion_activacion con
   build_metrics_toolset): tiene REPARTO ESCRITO en la tabla de
   OP-D-06 y SE CUMPLE TAL COMO ESTA. El cruce con OP-F-04-WEI
   (fuente primero) esta satisfecho por precedencia: WEI declara
   HECHA en su nota, verificado por el acta de la 43 contra
   OPERACIONES.jsonl. Si la lectura del acto contradice el reparto
   escrito, PARAS y lo traes.
3. ACTO 711 (future_scenarios_planning con escenarios_futuros): el
   cruce con OP-F-02 (injerto de Mollick, fuente primero) esta
   satisfecho: HECHA en su nota. Si el injerto cambio el texto que el
   par leia, la lectura lo declara con la cita delante.
4. ACTO 969 (retention_metrics con
   customer_retention_metrics_webmobile): el bloqueo de OP-F-04-COL
   sobre OP-D-06 esta levantado: HECHA en su nota. Misma
   comprobacion de precedencia que el 341.
5. Cada acto COMPLETO antes de abrir el siguiente, con
   vuelta40_acto_opd06.py, vuelta41_lectura_acto.py,
   vuelta41_plan_acto.py y su modulo por acto en
   scripts/loop/v41_actos/: P.11 para separar advertencia de
   procedimiento, P.5 con el subconjunto cerrado por transitividad
   sobre las A, P.8 en orden con el contenido primero y el cableado
   impreso despues, perdidas repartidas por la regla adjudicada (cada
   una al bloque del que proviene y la que no tenga bloque al
   superviviente).
6. EL CIERRE DE OP-D-06, cuando el 969 quede cerrado: el recomputo
   del cierre transitivo sobre los nueve, los pares congelados de la
   operacion releidos contra su superviviente, la verificacion punto
   por punto de la lista de OPERACIONES.jsonl con lo medido al lado,
   el estado recomputado al cierre (regla 1), y el REGISTRO DE
   OPERACION HECHA en la nota de OP-D-06 siguiendo el patron
   adjudicado en la vuelta 30: el campo estado SE QUEDA EN LISTA y la
   declaracion vive en la nota con su evidencia.
7. Si OP-D-06 queda cerrada y la vuelta tiene cuerda, sigues el orden
   del 00_INDICE con la siguiente operacion de la fase en curso,
   leida ENTERA antes de tocar nada, con las guardas del modo
   continuo (simulacion previa, Gate 0 y suites en verde tras cada
   fase, caso positivo, cero duplicadas o auto-aristas tras
   resolver). Si su texto no alcanza para ejecutarse sin decidir,
   PARAS y la traes. Si los actos no caben en la vuelta, cierras
   COMPLETO el acto en curso hasta su ultimo commit pusheado,
   declaras cuales quedan y en que estado, y NINGUN acto queda a
   medias SIN COMMIT. Reporte por fase con los discutibles marcados
   antes de saber si aciertas.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si
algo contradice una regla vigente, paras y lo traes. No adivines.
