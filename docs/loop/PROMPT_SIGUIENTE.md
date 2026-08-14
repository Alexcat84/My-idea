Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3): corre las fases seguidas sin
esperar acta, con las guardas obligatorias por operacion. dataset/ (los
nodos del grafo) NO se toca salvo lo que una operacion ordena; el caso
positivo de cada guarda inyecta estado malo SOLO en arbol de trabajo
temporal, nunca commiteado, restaurado a HEAD acto seguido, con la
salida guardada como prueba. Cualquier guarda en rojo, o cualquier
operacion cuyo texto no alcance para ejecutarse sin decidir, te detiene
a ti y convoca al auditor.

====================================================================
TAREA 1: los registros que el acta de la vuelta 23 dejo encargados
====================================================================
1. En docs/plan/08_VERIFICACION.md, a continuacion de la definicion de
   GATE 0 EN VERDE (la que ya cita el ciclo de dos comandos, alrededor
   de la linea 53), añade una linea expresa de registro: git status
   marca dataset/metadata/master_graph.json como modificado por el
   simple reemplazo de LF por CRLF al tocar el fichero en Windows; ESO
   NO ES LA VARA. La vara es el hash de blob byte identico a HEAD (el
   comando 2 del ciclo). Quien lea un movimiento en git status sobre
   ese fichero sin diferencia de contenido real no esta viendo una
   regresion.
2. Antes de ejecutar la TAREA 2, lee entera la nota corregida de
   OP-S-07 y de OP-C-04 en docs/plan/OPERACIONES.jsonl: llevan la
   correccion declarada del 14 ago 2026 (decision del fundador, camino
   A) con el eliminar y la verificacion de OP-S-07 ampliados a 66, el
   censo de las 48 alias contra alias como inertes, y el criterio de
   OP-C-04 sobre vivos con los deprecados fuera de la guarda. Esa es la
   letra vigente; no hace falta escribir nada nuevo ahi, solo leerla
   antes de ejecutar.

====================================================================
TAREA 2: OP-S-07, OP-C-04, cierre de la fase 0 y seguir en modo continuo
====================================================================
1. Ejecuta OP-S-07 por su letra nueva: retira los 66 enlaces (33 vivos
   mas sus 33 reciprocas literales del gemelo deprecado), deja las 48
   alias contra alias intactas, y corre GATE 0 VERDE POR EL CICLO
   ESCRITO. Verifica cero auto aristas tras resolver sobre vivos y que
   el conteo de aristas del grafo bajo en 66 exactamente.
2. Con OP-S-07 hecha, OP-C-04 se desbloquea (su depende_de era
   ['OP-S-06', 'OP-S-07'] y OP-S-06 ya esta ejecutada). Ejecutala: la
   guarda de auto arista mide sobre vivos, los deprecados quedan fuera.
   Su caso positivo va en arbol de trabajo temporal, nunca commiteado,
   tal como ya esta adjudicado en su propia nota: reinyecta el enlace
   de analisis_flujo_de_valor y la clave fase_proekto cirilica, corre
   Gate 0 para verlo CAER, y restaura dataset/ a HEAD.
3. OP-C-05 sigue diferida por su depende_de (OP-S-12); no la ejecutes.
   Con OP-S-07 y OP-C-04 hechas, LA FASE 0 SE CIERRA.
4. Sigue en MODO CONTINUO a las fases siguientes del 00_INDICE, con
   Gate 0 verde por el ciclo escrito y las suites en verde tras cada
   fase, hasta que una guarda salga en rojo o una operacion no alcance
   para ejecutarse sin decidir.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
