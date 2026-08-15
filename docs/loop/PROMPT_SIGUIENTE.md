Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3): corre las fases seguidas sin
esperar acta, con las guardas obligatorias por operacion. dataset/ SI
se toca en esta fase, porque el texto de cada operacion lo ordena.
Cualquier guarda en rojo fuera de lo que 08_VERIFICACION.md declara
permitido, o cualquier operacion cuyo texto no alcance para ejecutarse
sin decidir, te detiene a ti y convoca al auditor.

LA CITA LLEVA SU LINEA (EJECUTOR.md, regla 1): toda afirmacion sobre el
estado del registro va con la medicion del dia al lado. Si no hay
linea que citar, no se escribe.

====================================================================
TAREA 1: registros
====================================================================
1. Hornea la entrada HUGOS-SISTEMAS al inventario
   (docs/plan/INVENTARIO.jsonl, tipo familia_de_ids), adjudicacion 7 del
   acta de la vuelta 27, citando la correccion del fundador del 14 ago
   2026 (docs/plan/BANCO_DEL_PLAN.md P.18 y la nota de OP-F-03). Nomina:
   los ocho de la salida de sistemas mas tecnologia_como_medio_no_fin,
   nueve en total, con la lectura que los junta.
2. RELECTURA CONJUNTA de las dos discrepancias de la relectura ciega del
   acta 27, seccion 2: economia_circular_como_modelo_de_negocio (el
   auditor lee nodo propio, el reporte lo repartio) y
   superioridad_producto_beneficios (el auditor lee otro miembro FAB).
   Verifica cada una contra el grafo y decide con la vara de P.18 (el
   objeto coincide, si o no). Si alguna voltea, correccion declarada y
   recomputo: el reparto se deshace o se muda de miembro, sin borrar el
   texto de la lectura anterior.
3. Registra las adjudicaciones 1 a 3 del acta de la vuelta 27 donde
   corresponda: OP-F-03 sigue PARCIAL hasta que existan los cuatro
   nodos propios pendientes (adjudicacion 1); la repeticion que un
   reparto crea entra a la cola de relectura post fusion de la fase 02,
   no se desteje en el acto (adjudicacion 2); dos bloques que caen en
   el mismo nodo propio se funden en UNO con las dos procedencias
   declaradas en su fuente, nunca dos nodos gemelos (adjudicacion 3).

====================================================================
TAREA 2: aplicar los planes sellados y seguir en modo continuo
====================================================================
1. Aplica los planes sellados docs/loop/PLAN_V27_*.json que sigan
   pendientes: el corte completo de OP-F-02 (los tres nodo propio) y
   los bloques de OP-F-03 bloqueados por el muro (hasta los cuatro
   nodos propios que le faltan para declararse HECHA, con el ajuste
   que traiga la relectura conjunta de la TAREA 1 si economia_circular
   voltea). Cada plan trae su corte con frontera, prefijos por paso,
   textos enteros y fuente por corte: ejecutalo tal como esta sellado.
2. POR CADA NODO NUEVO QUE CREES, añade su linea a
   docs/plan/INDICE_ROJO_DECLARADO.jsonl: {"id", "operacion", "fecha"}.
   Corre el ciclo de Gate 0 entero (los tres comandos de
   08_VERIFICACION.md) despues de cada operacion: los ids recien
   declarados tienen que aparecer como ROJO DECLARADO, impresos uno a
   uno, y Gate 0 tiene que cerrar en verde en todo lo demas. Cualquier
   id sin vector que NO este en la lista es PARADA.
3. Con OP-F-02 y OP-F-03 cerradas, ejecuta las tres tandas restantes de
   OP-F-04 (COL, HOR, WEI) con destino por P.18 en cada bloque
   apendice: el miembro cuyo objeto coincida, o nodo propio si ninguno
   coincide (mismo tratamiento de la lista del punto 2 para cualquier
   nodo propio nuevo).
4. Con la fase 01 cerrada, SIGUE EN MODO CONTINUO a las fases
   siguientes del 00_INDICE, con Gate 0 verde por el ciclo escrito
   (incluido el rojo declarado cuando aplique, y ningun otro rojo) y
   las suites en verde tras cada fase, hasta que una guarda salga en
   rojo fuera de lo permitido o una operacion no alcance para
   ejecutarse sin decidir.

Las lecturas ya publicadas y verificadas dos veces (fronteras de
Mollick, los 21 de Hugos veredicto por veredicto salvo las dos en
relectura conjunta, los diez del racimo de supervision de la IA) NO se
rehacen: ejecuta sobre esa lectura.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
