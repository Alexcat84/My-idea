Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. La campaña entro
en fase de EJECUCION: el codigo de web/ y scripts/ SI se toca, segun el
texto de cada operacion. dataset/ (los nodos del grafo) NO se toca salvo
lo que una operacion ordena; el caso positivo de cada guarda inyecta
estado malo SOLO en arbol de trabajo temporal, nunca commiteado,
restaurado a HEAD acto seguido, con la salida guardada como prueba.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3): corre las fases
seguidas sin esperar acta, con las guardas obligatorias por operacion.
Cualquier guarda en rojo, o cualquier operacion cuyo texto no alcance
para ejecutarse sin decidir, te detiene a ti y convoca al auditor.

====================================================================
TAREA 1: los registros de las adjudicaciones del acta de la vuelta 21
====================================================================
1. Registra en docs/plan/08_VERIFICACION.md la definicion de GATE 0 EN
   VERDE adjudicada (ACTA_AUDITOR.md, vuelta 21, seccion 4, puntos 1 y
   2): el criterio es EL CICLO ESCRITO DE DOS COMANDOS, no la invocacion
   a secas del validador.
   - python scripts/run_phase1.py --reaplico-curaduria tiene que salir
     con EXITCODE 0 y GATE 0: OK.
   - python scripts/etiquetas_de_cara.py --aplicar, corrido justo
     despues, tiene que dejar dataset/metadata/master_graph.json
     byte-identico a HEAD (mismo hash de blob).
   La invocacion a secas del validador (sin --reaplico-curaduria) sale
   con exit 2 SIEMPRE que haya curaduria viva: eso NO es un rojo que
   clasificar, es la alarma del propio instrumento funcionando (comentario
   fechado 2026-08-07 en run_phase1.py, lineas 941 a 958). Quien recompila,
   reaplica: el ejecutor que corra Gate 0 reaplica la curaduria acto
   seguido, y si el conteo de etiquetas aplicadas encoge al reaplicar, lo
   declara en el reporte en vez de callarlo.
2. Registra en docs/plan/OPERACIONES.jsonl (nota, sin borrar el texto
   viejo) las dos adjudicaciones de esa misma acta:
   - OP-C-04: la sede de su caso positivo es EL ARBOL DE TRABAJO
     TEMPORAL, nunca commiteado, restaurado a HEAD acto seguido con la
     salida guardada como prueba.
   - OP-C-05: se queda en la fase 0, DIFERIDA POR SU depende_de ESCRITO
     (OP-S-12), sin bloquear nada y sin cambio de fondo.

====================================================================
TAREA 2: la FASE 0 entera, por el orden nuevo
====================================================================
Ejecuta en este orden: OP-C-01, OP-C-02, OP-C-03, OP-S-06, OP-S-07,
OP-C-04. (OP-C-05 sigue diferida por su depende_de; no entra en esta
tanda.)

Cada operacion, con su paquete completo: simulacion previa, ejecucion
tal como esta escrita, caso positivo corrido sobre arbol de trabajo
temporal nunca commiteado, y GATE 0 VERDE POR EL CICLO ESCRITO (TAREA
1, punto 1) tras cada una, no solo al final. Si alguna guarda sale en
rojo o el texto de una operacion no alcanza para ejecutarse sin
decidir, paras esa operacion, no partes la fase, restauras dataset/ a
HEAD si algo quedo inyectado, y traes la pregunta completa.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
