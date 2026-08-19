Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

TAREA 1, registros: en docs/plan/02_DESTEJIDOS.md, bajo el estado de OP-D-04
de la vuelta 38, una linea fechada: el acta del auditor de la vuelta 38
(docs/loop/ACTA_AUDITOR.md) confirma las tres lecturas en D, confirma las dos
elecciones de P.8, y adjudica (a3) que FAMILIA DECLARADA no gobierna las tres
lecturas autorizadas, asi que LAS DOS FUSIONES QUEDAN AUTORIZADAS. En el
proximo REPORTE.md, la correccion de la caida declarada en el acta: las
insertadas del diff de la vuelta 38 eran 4.044, no 4.043.

TAREA 2, la ejecucion de OP-D-04: mide la apertura ANTES de la primera
operacion (regla 1) y commitea la apertura. Antes de escribir nada, re-corre
las dos simulaciones selladas con el mismo comando de la vuelta 38: la salida
tiene que dar BYTE IGUAL contra SALIDA_V38_SIM_TALLER.txt y
SALIDA_V38_SIM_ALTERNANCIA.txt (nada del grafo se ha movido desde el sellado,
verificado en el acta); si difiere una linea, PARAS con el diff delante.

Luego ejecuta las DOS fusiones TAL COMO estan selladas, sin recalcular
ninguna decision: primero el taller (reglas_brainstorming absorbe a
brainstorming_divergente y a brainstorming_efectivo, plan
docs/loop/PLAN_V38_OPD04_TALLER.json), despues la alternancia
(pensamiento_convergente_divergente absorbe a generar_multiples_opciones y a
design_attitude_vs_decision_attitude, plan
docs/loop/PLAN_V38_OPD04_ALTERNANCIA.json). Guardas por operacion, todas
obligatorias:

1. P.16, quien fabrica limpia: la duplicada nueva que cada fusion fabrica
   (una y una, nombradas en las simulaciones) se resuelve en la misma
   operacion; cero duplicadas y cero auto aristas tras resolver.
2. Ciclo de Gate 0 (run_phase1 mas etiquetas mas sync) y las suites (motor,
   web, tsc) en verde tras cada fusion.
3. La guarda de los planes: symmetrize_added del ciclo trae EXACTAMENTE 16
   entradas para reglas_brainstorming y 4 para
   pensamiento_convergente_divergente, ni una mas ni una menos, cotejadas
   contra la lista de simetrizacion_esperada de cada plan. Si trae otra cosa,
   PARAS con las dos listas delante.
4. El censo no se mueve: 3.853 ficheros antes y despues. Los vivos bajan
   EXACTAMENTE en dos por fusion (3.538 a 3.536 a 3.534) y los deprecados
   suben igual (315 a 317 a 319); los cuatro absorbidos quedan deprecados con
   su texto intacto.
5. El enlace del cuarto miembro llego solo: tras el ciclo,
   reglas_brainstorming y brainstorming quedan declarados cada uno en el
   extremo del otro, medido sobre los dos ficheros.
6. Caso positivo de cada operacion con el mismo instrumento antes y despues.
7. Titulo y etiqueta del taller NO se tocan (adjudicacion a6 del acta).

Despues de las dos fusiones: enlaza los tres vivos que quedan
(reglas_brainstorming, pensamiento_convergente_divergente,
construir_sobre_ideas_ajenas) por P.10, con las aristas escritas resueltas al
dia de su escritura (P.9). Cierra OP-D-04: el campo superviviente QUEDA EN
NULL y la nota de cierre nombra los dos supervivientes con sus dos planes
sellados (adjudicacion a4 del acta); correccion declarada en 02_DESTEJIDOS
con el texto viejo entero delante. Con OP-D-04 cerrada y todo verde, retoma
el MODO DE EJECUCION CONTINUA con la siguiente operacion del orden del
00_INDICE; reporte por fase (regla 7), commit y push por operacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
