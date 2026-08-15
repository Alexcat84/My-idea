Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3): corre las fases seguidas sin
esperar acta, con las guardas obligatorias por operacion. dataset/ SI
se toca en esta fase, porque el texto de cada operacion lo ordena.
Cualquier guarda en rojo fuera de lo que 08_VERIFICACION.md declara
permitido, o cualquier operacion cuyo texto no alcance para ejecutarse
sin decidir, te detiene a ti y convoca al auditor.

EJECUTOR.md, regla 1: LA CITA LLEVA SU LINEA, y ahora con su segundo
renglon, EL ESTADO AL CIERRE SE MIDE AL CIERRE. Toda tabla o cifra que
describa el estado al cerrar la vuelta se recomputa al cierre si algo
de la propia vuelta pudo haberla movido.

====================================================================
TAREA 1: registros
====================================================================
1. Declara las tres costuras que los cortes de OP-F-04-WEI crearon en
   docs/plan/08_VERIFICACION.md, seccion LA COLA DE RELECTURA POST
   FUSION, en la misma tabla y con el mismo formato de la primera
   costura ya registrada: fases_traccion_producto, clasificacion_leads_abc
   y bullseye_framework. Mide cada una con instrumento propio (pasos
   totales tras el reparto, contra los que tenia antes) y revisa
   tambien publicidad_offline_pruebas_locales por el solape parcial que
   el acta de la vuelta 28 senalo. No destejas nada: solo se declara.
2. Cita, sin reescribirlas, las correcciones que este commit ya dejo
   hechas: web/lib/engine/graph.test.ts mide paridad contra total_nodos
   en vez de clavar 3835 (con su caso positivo en las dos direcciones);
   el cuarto comando condicional del ciclo de Gate 0
   (engine/plan_readiness.py, corrido despues del 2 y antes del 3) en
   docs/plan/08_VERIFICACION.md; y el renglon EL ESTADO AL CIERRE SE
   MIDE AL CIERRE en docs/loop/EJECUTOR.md.

====================================================================
TAREA 2: aplicar los planes sellados que el muro tenia presos
====================================================================
Aplica, en el orden que prefieras, los planes sellados en docs/loop/:
PLAN_V27_OPF02.json (los tres nodo propio de Mollick), PLAN_V28_RELECTURA.json
(el nodo propio de economia circular) y los cinco bloques nodo propio
de OP-F-03 (PLAN_V27_OPF03_SISTEMAS.json y lo que falte de
PLAN_V27_OPF03_CADENA.json), recordando la adjudicacion 3 del acta de
la vuelta 27: analisis_tco_roi_b2b y criterios_seleccion_proveedores
van a UN solo nodo propio, con las dos procedencias declaradas en su
fuente, nunca dos nodos gemelos.

Por cada nodo que crees: añade su linea a
docs/plan/INDICE_ROJO_DECLARADO.jsonl ({"id", "operacion", "fecha"}), y
corre el ciclo de Gate 0 entero (los cuatro comandos de
08_VERIFICACION.md, el cuarto solo si la operacion cambio el censo)
tras cada operacion. Los ids recien declarados tienen que aparecer
como ROJO DECLARADO, impresos uno a uno; cualquier id sin vector que
NO este en la lista es PARADA.

====================================================================
TAREA 3: cerrar OP-F-04 y la fase 01
====================================================================
1. Ejecuta los nueve bloques restantes de OP-F-04-WEI (fronteras ya
   leidas y publicadas en 01_FUENTES.md; dos van con TOQUE UNICO), con
   destino por P.18 en cada uno.
2. Ejecuta OP-F-04-COL entera, con destino por P.18.
3. Ejecuta OP-F-04-HOR con la adjudicacion 3 del acta de la vuelta 28
   citada: NO esta bloqueada en bloque. Se ejecuta como WEI, miembro
   por P.18 sobre la nomina medida al dia; nodo propio SOLO en el
   bloque sin miembro coincidente, y ese nodo (si lo hay) entra al
   mismo tratamiento de la TAREA 2: declarado en la lista, Gate 0
   entero despues.
4. Con las cuatro OP-F-04 hechas y OP-F-02 y OP-F-03 cerradas, LA FASE
   01 QUEDA CERRADA. Sigue en MODO CONTINUO a las fases siguientes del
   00_INDICE, con Gate 0 verde por el ciclo escrito (los cuatro
   comandos, el cuarto cuando aplique) y las suites en verde tras cada
   fase, hasta que una guarda salga en rojo fuera de lo permitido o una
   operacion no alcance para ejecutarse sin decidir.

Las lecturas ya publicadas y verificadas (fronteras, destinos, los
ocho discutibles de la ciega del acta 28) NO se rehacen: ejecuta sobre
esa lectura.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
