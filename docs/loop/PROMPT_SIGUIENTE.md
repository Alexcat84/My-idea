Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
LO PENDIENTE ES LA FUSION DEL ACTO 331 EJECUTADA Y VERIFICADA, que el
error 521 de la API dejo sin su segundo commit (acta de la vuelta 42):
los 8 ficheros modificados (dataset/nodos/analisis_de_gastos_de_capital.json,
dataset/nodos/propuesta_gasto_capital.json,
dataset/nodos/comparacion_metodos_inversion.json,
dataset/nodos/gestion_capital_trabajo.json, los dos master_graph.json,
web/lib/assets/manifest.json y dataset/metadata/phase1_run_log.json) y
las 11 salidas selladas docs/loop/SALIDA_V42_*_331.txt. Es el SEGUNDO
COMMIT del acto 331 y se commitea TAL COMO QUEDO, sin re-ejecutar ni
recalcular nada: el acta de la vuelta 42 verifico la fusion contra el
plan sellado (trece guardas, censo 3.853 con 3.530 vivos y 323
deprecados, enlaces 16.880, cero vivos nombrando al absorbido) y
re-corrio el ciclo Gate 0 y las tres suites en verde. El mensaje
declara: la ejecuto la vuelta 42, el 521 cayo entre la fusion y su
commit, y el acta de la vuelta 42 la verifico entera. Si git status
muestra algo DISTINTO de esas rutas, PARAS y lo traes.

TAREA 1, registros, en este orden:
1. En docs/plan/02_DESTEJIDOS.md, bajo la seccion del plan del acto 331,
   el REGISTRO DE CIERRE del acto (la seccion que el corte impidio):
   la fusion ejecutada en la vuelta 42 con sus trece guardas, el ciclo
   y las suites verdes, el censo (vivos 3.531 a 3.530, deprecados 322 a
   323, enlaces mas 2), la simetrizacion 2 de 2 releida en el fichero,
   reanclar en blanco, caso positivo 33 pasan y 0 caen, CERO pares B o
   C a releer (medido en la lectura sellada), y el corte del 521
   declarado con el acta de la vuelta 42 como verificacion. Cita las
   lineas del acta que uses, leidas hoy (el acta de la 42 empieza en la
   linea 8869 de docs/loop/ACTA_AUDITOR.md).
2. La seccion breve fechada de la interrupcion de la vuelta 42: murio
   por 521 (servidor caido, ultimo_ejecutor.json) a las 14:15:39 con el
   acto 285 cerrado y pusheado, el primer commit del 331 pusheado y la
   fusion del 331 en el arbol; el acta de la vuelta 42 verifico TODO
   por corrida propia (byte igual donde aplica, ciega del 331 con 3 de
   3, relectura del 835 confirmada) y hallo CERO caidas. El patron de
   DOS vueltas seguidas cortadas por la API queda registrado con sus
   causas distintas (429 y 521); a la TERCERA seguida se escribe
   PARA_ALEXIS.md como patron operativo.
3. No hay caida de reporte que corregir: la vuelta 42 no dejo reporte y
   todo lo commiteado y lo sellado salio limpio. Se dice asi y no se
   rellena la casilla.

TAREA 2, OP-D-06 continuada, UNA operacion con NUEVE actos, con el
AFINAMIENTO ADJUDICADO EN EL ACTA 42: dentro de cada acto, el SEGUNDO
COMMIT se hace APENAS la fusion, reanclar, el ciclo Gate 0 y las suites
esten verdes; la costura post fusion con su senal, las relecturas B o C
y el registro de cierre van DESPUES, en un TERCER commit del acto. Lo
que muta el grafo se registra apenas esta verde; la prosa que lo lee
viene detras.
1. La apertura medida antes del primer acto nuevo (regla 1) y
   commiteada sola. NO sera byte igual a la de la vuelta 42 y el commit
   dice POR QUE, cifra a cifra: el 835 movio B 83 a 82 y D 2.722 a
   2.723; las dos fusiones bajaron vivos 3.532 a 3.530 y subieron
   deprecados 321 a 323; los enlaces 16.871 a 16.880 (mas 7 del 285 y
   mas 2 del 331). Si tu medicion difiere de estas cifras, PARAS y lo
   declaras.
2. EL CIERRE DEL ACTO 331 (el tercer commit de ese acto): el
   instrumento de costuras corrido sobre analisis_de_gastos_de_capital
   DESPUES de la fusion, con el antes y despues medido desde git
   (instrumento vuelta42_senal_antes_despues.py o su sucesor declarado)
   y la lectura con el texto delante si cita; el registro de cierre de
   la TAREA 1; y el commit pusheado. CERO pares vuelven a la cola: se
   cita la medicion sellada, no se rehace.
3. Cada acto A siguiente (341, 344, 361, 392, 711, 969), completo antes
   de abrir el siguiente, con vuelta40_acto_opd06.py,
   vuelta41_lectura_acto.py y vuelta41_plan_acto.py y su modulo por
   acto bajo scripts/loop/v41_actos/:
   a. La lectura: costuras leido de su cola entregada, lectura textual
      con la cita delante (P.11 para separar advertencia de
      procedimiento), P.5 con el subconjunto cerrado por transitividad
      sobre las A, P.8 en orden con el contenido primero y el cableado
      impreso despues.
   b. El reparto del 392 y del 341 ya esta escrito en la tabla de
      OP-D-06 y SE CUMPLE tal como esta; los demas con la regla
      adjudicada: cada perdida al bloque del que proviene y la que no
      tenga bloque al superviviente.
   c. Plan sellado GENERADO (origenes verbatim, redirecciones medidas
      incluidos los registros que no son el grafo, tabla de P.13,
      simetrizacion esperada), simulacion previa sellada,
      verificar_mapas_destejido.py con el plan nuevo ademas de los
      sellados. PRIMER COMMIT, pusheado ANTES de fundir.
   d. La fusion con las trece guardas; reanclar_por_resolutor.py ENTRE
      la fusion y run_phase1; ciclo Gate 0 de TRES comandos y las
      suites en verde; caso positivo antes y despues; P.16; censo
      exacto por acto. SEGUNDO COMMIT INMEDIATO, pusheado.
   e. Costuras sobre el resultante despues con su antes y despues, los
      pares B o C que vuelvan a la cola releidos al cierre del acto con
      su veredicto volcado como manda 08_VERIFICACION, y el registro de
      cierre. TERCER COMMIT, pusheado.
4. El acto 494 (clase C) NO elige superviviente: es la MISMA pareja que
   OP-D-01 trato, como el aviso de solape del plan declara. Verificas
   contra el registro y el plan sellado de OP-D-01 que ya quedo
   tratada, lo declaras con la cita delante, y el acto se cierra sin
   tocar nodos, en UN commit propio. Si lo que encuentras contradice el
   aviso, PARAS y lo traes.
5. Al cierre de la operacion (o de la vuelta, lo que llegue primero):
   el recomputo del cierre transitivo corrido, los pares congelados de
   la operacion releidos contra su superviviente, la verificacion punto
   por punto de OPERACIONES.jsonl, y el estado recomputado al cierre
   (regla 1). Si los actos no caben en la vuelta, cierras COMPLETO el
   acto en curso hasta su ultimo commit pusheado, declaras cuales
   quedan y en que estado, y NINGUN acto queda a medias SIN COMMIT.
   Reporte por fase (regla 7), discutibles marcados antes de saber si
   aciertas.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
