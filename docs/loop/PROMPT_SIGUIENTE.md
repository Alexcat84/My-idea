Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3): corre las fases seguidas sin
esperar acta, con las guardas obligatorias por operacion. dataset/ (los
nodos del grafo) SI se toca en esta fase, porque el texto de cada
operacion lo ordena; el caso positivo de cada guarda inyecta estado
malo SOLO en arbol de trabajo temporal cuando la operacion es de
codigo, nunca commiteado. Cualquier guarda en rojo, o cualquier
operacion cuyo texto no alcance para ejecutarse sin decidir, te detiene
a ti y convoca al auditor.

====================================================================
TAREA 1: los registros que el acta de la vuelta 25 dejo encargados,
mas las correcciones del fundador ya escritas (solo citarlas)
====================================================================
1. En docs/plan/08_VERIFICACION.md, añade al ciclo de Gate 0 un TERCER
   COMANDO CONDICIONAL: cuando una operacion cambia el grafo, despues
   de reaplicar la curaduria corre python scripts/sync_assets_web.py
   (el remedio escrito del propio validador). La vara: las dos copias
   quedan byte identicas a HEAD. Este comando es condicional, no corre
   en fases que no tocan el grafo.
2. En el mismo archivo, al blob que sirve de linea base, añadele su
   calificador de corte: es REGISTRO HISTORICO, no la vara operativa.
   La vara sigue siendo byte identico al HEAD del momento, y la cifra
   que se vigila es el conteo de 71 etiquetas.
3. Cita, sin reescribirlas, las correcciones que este commit ya dejo
   hechas: la nomina de OP-F-01 en OPERACIONES.jsonl (SEIS miembros, sin
   background_startup_vs_corporativo), la regla P.17 nueva en
   BANCO_DEL_PLAN.md, la correccion declarada en 01_FUENTES.md sobre la
   clase LARGO LEGITIMO, la regla de destino por lectura en la nota de
   OP-F-02, y el BACKLOG POST-CAMPAÑA en PENDIENTES.md.

====================================================================
TAREA 2: la fase 01 por su orden, y SEGUIR EN MODO CONTINUO
====================================================================
1. Ejecuta OP-F-01 con su nomina corregida (seis nodos): manda la
   clase, ningun nodo de los seis con pasos alterados, la cifra de 18
   reescrita con su corte donde este publicada, Gate 0 verde.
2. Ejecuta OP-F-02: primero lee cada uno de los tres nodos de Mollick
   (future_scenarios_planning, gut_check, brainstorming_divergente)
   contra sus pasos_accionables y publica la frontera del bloque de IA
   en 01_FUENTES.md, con el mismo metodo de la tabla de los 14 de
   Horowitz, ANTES de cortar. Con la frontera puesta, aplica la regla
   de destino por lectura (ya escrita en la nota de la operacion): el
   bloque va al miembro del racimo de supervision de la IA cuyo objeto
   coincida, o forma nodo propio si ninguno coincide; escribe el
   destino elegido como correccion declarada con la lectura que lo
   sostiene.
3. Ejecuta OP-F-03 por su letra (los 21 leidos uno a uno).
4. Ejecuta OP-F-04-HOR por su letra (la tanda de los 13, con
   background_startup_vs_corporativo ahora sin conflicto: ya salio de
   OP-F-01).
5. Con la fase 01 cerrada, SIGUE EN MODO CONTINUO a las fases
   siguientes del 00_INDICE, con Gate 0 verde por el ciclo escrito y
   las suites en verde tras cada fase, hasta que una guarda salga en
   rojo o una operacion no alcance para ejecutarse sin decidir.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
