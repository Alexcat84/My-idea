Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. LA FASE II ESTA CERRADA y LA FASE III ESTA ABIERTA por el
acta de la vuelta 20 del auditor (seccion 8). LA RAMA ACTIVA ES `pasada-unica`,
creada desde `bucle` por el auditor: verifica con `git branch --show-current`
que estas en ella ANTES de la primera edicion; si no lo estas, `git checkout
pasada-unica` primero. TODO el trabajo de la FASE III se commitea y pushea en
`pasada-unica` (origin/pasada-unica), incluidos docs/loop/. `bucle` NO se toca
mas y NADA se funde a staging ni a main: el merge es decision de Alexis.

MODO DE ESTA VUELTA: registros mas FASE 0 DE CODIGO. El cribado sigue CERRADO
en 3.388: docs/INTRA_DOMINIO_VEREDICTOS.jsonl NO se toca y no se lee ningun
par nuevo. Las fases 01 a 08 NO se empiezan: la verificacion completa de
apertura (recomputo mas fase 0 en verde) es del auditor en la vuelta
siguiente, y SOLO despues arranca el modo de ejecucion continua.

ESTADO DEL CREDITO: la tanda 20 salio con UNA caida de especie REPORTE (una
busqueda negativa citada que llego a 01_FUENTES.md: "la nomina de los 13 no
esta escrita en ninguna parte" es falsa, vive en OPERACIONES.jsonl,
OP-F-04-HOR, campo nodos). No acumula para la parada de dos tandas; caidas de
reporte seguidas: UNA (tres seguidas son parada). El contador de clase o
cifra sigue EN CERO. Las reglas de siempre: toda cifra sale de instrumento
corrido EN ESTA VUELTA; toda cifra que contradiga una publicada se declara al
lado de la vieja sin tocarla; los vivos se cuentan sin los deprecado; y una
busqueda negativa NO se cita sin barrer TODAS las sedes, incluida
OPERACIONES.jsonl y los campos nodos de las operaciones.

====================================================================
TAREA 1: cinco registros de las adjudicaciones del acta de la vuelta
20 (docs/loop/ACTA_AUDITOR.md, secciones 3 a 5), todos aditivos, de
una linea o una celda, con el texto viejo conservado entero
====================================================================
1. La fila 7 queda ADJUDICADA: en docs/plan/01_FUENTES.md, en la celda de
   decision_de_vender_startup de la tabla LOS TRES CASOS QUE NO SON UN
   SIMPLE APENDICE, correccion declarada aditiva: MANDA EL 34, medido por
   el auditor con git (el blob de dataset/metadata/master_graph.json es
   identico en 0e5e0c60 del 9 ago, en 23f9ac32 del 11 ago que crea
   01_FUENTES.md, y en HEAD): el nodo ya tenia 34 pasos el 11 ago, asi que
   el 25 y su tramo eran PARCIALES DE NACIMIENTO, no un nodo que crecio.
   El 25 y el tramo viejo quedan enteros; la frontera vigente (1 a 10 /
   11 a 34) ya esta impresa en la tabla de la vuelta 20 y se cita, no se
   recuenta. El caracter del hallazgo (no es un simple apendice) queda.
2. La nomina de los 13 SI existe: en docs/plan/01_FUENTES.md, en la
   subseccion de la vuelta 20 que dice que "no esta escrito en ninguna
   parte" y que "sigue sin poderse decir cual sobra", correccion declarada
   aditiva y la frase vieja entera: la nomina de los 13 vive en
   docs/plan/OPERACIONES.jsonl, OP-F-04-HOR, campo nodos (corte
   2026-08-11), y el que sobra ES principio_calidad_mvp, que tiene
   cobertura de plan propia (bloque de Hugos en OP-F-03 y destejido entero
   en OP-D-01). Adjudicado en el acta de la vuelta 20, secciones 1 y 5.
3. OP-F-04-HOR recibe su aviso: en docs/plan/OPERACIONES.jsonl, adicion
   declarada AL FINAL del campo nota de OP-F-04-HOR (el campo nodos NO se
   toca): su adjudicacion dice que en los 13 el bloque esta "al final de
   los pasos", y medido en la vuelta 20 uno de sus 13, metas_vs_proposito,
   tiene el bloque de Horowitz EN MEDIO porque Coleman cierra; la
   presencia 13 de 13 queda; puntero a la tabla de la vuelta 20 de
   01_FUENTES.md. Diff de UNA linea del archivo.
4. OP-S-11 recibe su segundo ejemplar: en el campo nota de OP-S-11,
   adicion declarada AL FINAL: el nodo que declara el mismo libro dos
   veces con dos grafias no es uno sino DOS en la tanda
   (decision_de_vender_startup y plan_mejora_procesos, The Hard Thing
   About Hard Things / The Hard Thing About Hard Thing), y fuera de la
   tanda hay DOS de Hugos con grafia truncada en el mismo nodo
   (asociaciones_clave y transicion_producto_a_experiencia, "Essentials
   of Supply Chain Mana"), medidos en las vueltas 20 y 21 del bucle. Diff
   de UNA linea del archivo.
5. El cierre queda escrito donde se mide: en docs/plan/RECOMPUTO_3388.md,
   al final de la seccion TAREA (vuelta 20), dos lineas aditivas: que la
   fila 7 de la lista B quedo ADJUDICADA por el acta de la vuelta 20 del
   auditor (manda el 34, conteo viejo parcial de nacimiento, medido con
   git) y la lista B queda VACIA; y que la FASE II queda CERRADA por esa
   acta, con la FASE III abierta en la rama pasada-unica.

====================================================================
TAREA 2: LA FASE 0 DE CODIGO, entera (OP-C-01 a OP-C-05), en
pasada-unica, tal como esta escrita en el plan
====================================================================
A. LINEA BASE PRIMERO, antes de tocar codigo: corre el Gate 0
   (python scripts/run_phase1.py) tal cual esta y guarda su salida. Es un
   orquestador idempotente que recompila master_graph.json: si tras
   correrlo `git status` muestra en dataset/ algo mas que
   dataset/metadata/phase1_run_log.json, PARAS y lo traes al reporte sin
   commitear dataset/ (un grafo ya limpio no debe moverse). Corre tambien
   la suite del web (cd web y pnpm test); si algo falla por el .env
   ausente, que falle VISIBLE y lo traes: es parada legitima y las
   credenciales NO vuelven al repo.
B. Las cinco operaciones de la fase 00_CODIGO (OP-C-01, OP-C-02, OP-C-03,
   OP-C-04, OP-C-05), cada una TAL COMO ESTA ESCRITA en
   docs/plan/OPERACIONES.jsonl y con el criterio de HECHO de
   docs/plan/08_VERIFICACION.md: el CASO POSITIVO de cada guarda se corre
   ANTES del arreglo y debe CAERSE; despues del arreglo pasa. Una prueba
   que pasa antes del arreglo no prueba nada y se rehace. Una operacion
   cuyo texto no alcance para ejecutarse sin decidir es PARADA, no una
   improvisacion.
C. Al cerrar la fase: Gate 0 en verde, suite en verde, y el resumen por
   operacion (guarda, caso positivo que se cayo antes y paso despues,
   archivos tocados). Commits por tramo, empujados a origin/pasada-unica.
D. NO empieces la fase 01. La verificacion completa de apertura es del
   auditor en la vuelta siguiente; de ahi arranca el modo continuo.

Reporte completo en docs/loop/REPORTE.md (en pasada-unica) con tus
discutibles marcados ANTES de saber si aciertan, el marcador recomputado,
lo reservado comprobado, y toda cifra leida de la salida de un instrumento
corrido EN ESTA VUELTA.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
