Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
LO PENDIENTE ES CONCRETO y viene de la vuelta 41, que un limite de sesion
de la API corto a mitad del acto 285 (acta de la vuelta 41): seis rutas,
docs/loop/SALIDA_V41_ACTO285_LECTURA.txt,
docs/loop/SALIDA_V41_ACTO285_PLAN.txt, docs/loop/PLAN_V41_ACTO285.json,
scripts/loop/vuelta41_lectura_acto.py, scripts/loop/vuelta41_plan_acto.py
y scripts/loop/v41_actos/ (sin __pycache__). El mensaje del commit declara
que son los sellados de la vuelta 41 interrumpida, commiteados TAL COMO
QUEDARON, y que la fusion del 285 NO se ejecuto.

TAREA 1, registros, en este orden:
1. En docs/plan/02_DESTEJIDOS.md, bajo la seccion fechada de la vuelta 41,
   una seccion breve fechada: la vuelta 41 quedo interrumpida por limite
   de sesion de la API (429, ultimo_ejecutor.json) tras commitear la
   apertura (9f9fc182) y la tarea 1 (aaa15cbd) y tras sellar en disco la
   lectura y el plan del acto 285 sin fundirlo. El acta de la vuelta 41
   verifico lo commiteado por corrida propia (apertura byte igual salvo
   la etiqueta del encabezado, costuras exit 0 linea a linea con el 42,4
   medido, las ocho lineas del acta citadas leidas al digito, ciclo Gate 0
   de tres comandos y suites verdes, arbol byte igual) y hallo CERO
   caidas; la relectura ciega del auditor sobre el acto 285 coincide 2 de
   2 en el fondo (sin costura en los dos nodos y superviviente
   producto_unico_superior por contenido, con el cableado impreso despues
   y no decisorio). Adjudicado: el acto 285 SE RETOMA desde su plan
   sellado previa reproduccion por instrumento, y desde esta vuelta rigen
   DOS COMMITS POR ACTO (el plan sellado con su lectura, pusheado ANTES de
   fundir; la fusion ejecutada, en commit propio), para que un corte de
   sesion nunca deje un sellado sin commit.
2. No hay caida de reporte que corregir: la vuelta 41 no dejo reporte y lo
   commiteado salio limpio. Se dice asi y no se rellena la casilla.

TAREA 2, OP-D-06 retomada, UNA operacion con NUEVE actos, en el orden de
su tabla sellada (285, 331, 341, 344, 361, 392, 494, 711, 969), con
vuelta40_acto_opd06.py como instrumento del acto y vuelta41_lectura_acto.py
y vuelta41_plan_acto.py como instrumentos de lectura y plan:
1. La apertura medida antes del primer acto (regla 1) y commiteada sola.
   Si es byte igual a la de la vuelta 41 se dice con su md5. La
   comprobacion de fuente primero (OP-F-02 y OP-F-03 HECHAS en su nota) ya
   quedo citable en 9f9fc182 y en la propia salida del estado: se cita, no
   se rehace.
2. EL ACTO 285, RETOMADO DESDE LO SELLADO y con la verificacion delante:
   a. Re-corre vuelta41_lectura_acto.py y vuelta41_plan_acto.py sobre el
      285 y comprueba que REPRODUCEN las dos salidas y el plan sellados
      (el plan JSON identico; la lectura puede diferir solo en lo que la
      linea de limite de costuras anade). Si algo difiere, DECLARAS la
      diferencia y el sellado NO se ejecuta hasta adjudicarla: paras y lo
      traes. El acta 41 ya verifico la aritmetica del plan (7
      redirecciones, 3 deprecados que nombran, 0 duplicadas, 16 origenes,
      7 simetrizaciones, 6 pasos finales): tu corrida debe calzar.
   b. verificar_mapas_destejido.py con --json del plan del 285 ademas de
      los sellados; simulacion previa sobre copia en memoria con las trece
      guardas en verde, sellada.
   c. PRIMER COMMIT DEL ACTO: el plan verificado, su simulacion y el
      verificador, pusheado ANTES de fundir.
   d. La fusion con las trece guardas del patron de la vuelta 40;
      reanclar_por_resolutor.py ENTRE la fusion y run_phase1; ciclo Gate 0
      de TRES comandos (la operacion cambia el grafo: run_phase1 mas
      etiquetas mas sync, con las dos copias del grafo byte iguales al
      cerrar) y las suites en verde; caso positivo antes y despues con el
      mismo instrumento; P.16, la duplicada que fabriques la limpias en la
      misma operacion (el plan del 285 predice CERO); censo exacto
      (ficheros 3.853, vivos menos 1, deprecados mas 1).
   e. El instrumento de costuras corrido sobre el resultante DESPUES de
      fundir: si cita, la lectura con el texto delante y declarar si la
      fusion encendio la senal (practica adjudicada en el acta 40).
   f. La relectura del par 835 (clase B, brief_competitivo con
      producto_unico_superior), que vuelve a la cola post fusion porque
      superioridad_producto_beneficios muere: se relee al cierre del acto
      y su veredicto se registra como manda 08_VERIFICACION.
   g. SEGUNDO COMMIT DEL ACTO: la fusion ejecutada con sus salidas
      selladas, pusheado.
3. Cada acto A siguiente (331, 344, 361, 392, 711, 969), completo antes de
   abrir el siguiente y con los DOS commits por acto:
   a. vuelta41_lectura_acto.py sobre el par: el instrumento de costuras
      leido de su cola entregada y la lectura textual con la cita delante
      (P.11 para separar advertencia de procedimiento); si hay costura que
      destejer, plan de particion con su tabla pasada por
      verificar_mapas_destejido.py, simulacion previa y guardas.
   b. P.5 con el par delante: UNA familia o DOS, con el subconjunto
      cerrado por transitividad sobre las A.
   c. P.8 EN ORDEN, contenido primero, cableado que acompana y no decide
      (cero razones nombran ganador: los ocho son POR ELEGIR).
   d. El reparto del 392 y del 341 ya esta escrito en la tabla de OP-D-06
      y SE CUMPLE tal como esta; los demas con la regla adjudicada, cada
      perdida al bloque del que proviene y la que no tenga bloque al
      superviviente.
   e. Plan sellado GENERADO con vuelta41_plan_acto.py y su modulo por acto
      bajo scripts/loop/v41_actos/ (lo tecleado es solo la lectura: grupos,
      motivos, entregable, resumen); origenes verbatim, redirecciones
      medidas INCLUIDOS los registros que no son el grafo, tabla de P.13,
      simetrizacion esperada, simulacion previa sellada, y
      verificar_mapas_destejido.py con --json del plan nuevo ademas de los
      sellados. PRIMER COMMIT, pusheado antes de fundir.
   f. Fusion con las trece guardas; reanclar_por_resolutor.py ENTRE la
      fusion y run_phase1; ciclo Gate 0 y suites en verde; caso positivo
      antes y despues; P.16; censo exacto por acto. Costuras sobre el
      resultante despues, con su lectura si cita. Los pares B o C que
      vuelvan a la cola post fusion, releidos al cierre del acto. SEGUNDO
      COMMIT, pusheado.
4. El acto 494 (clase C) NO elige superviviente: es la MISMA pareja que
   OP-D-01 trato, como el aviso de solape del plan declara (la seccion
   54.3 lo cuenta como acto; el plan de cirugia lo trata como cura
   acoplada mayor). Verificas contra el registro y el plan sellado de
   OP-D-01 que ya quedo tratada, lo declaras con la cita delante, y el
   acto se cierra sin tocar nodos, en UN commit propio. Si lo que
   encuentras contradice el aviso, PARAS y lo traes.
5. Al cierre de la operacion (o de la vuelta, lo que llegue primero): el
   recomputo del cierre transitivo corrido, los pares congelados de la
   operacion releidos contra su superviviente, la verificacion punto por
   punto de OPERACIONES.jsonl, y el estado recomputado al cierre (regla
   1). Si los nueve actos no caben en la vuelta, cierras COMPLETO el acto
   en curso (como minimo su primer commit ya pusheado; si la fusion abrio,
   la terminas), declaras cuales quedan y en que estado, y NINGUN acto
   queda a medias SIN COMMIT. Reporte por fase (regla 7), discutibles
   marcados antes de saber si aciertas.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
