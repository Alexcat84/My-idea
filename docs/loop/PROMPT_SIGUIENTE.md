Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
(El acta de la vuelta 44 verifico el arbol LIMPIO y todo pusheado; si
git status muestra algo, PARAS y lo traes antes de seguir.)

TAREA 1, registros, en este orden:
1. En docs/plan/02_DESTEJIDOS.md, bajo el registro de cierre de OP-D-06,
   la seccion breve fechada de la auditoria: la vuelta 44 auditada ENTERA
   por el acta de la vuelta 44 (docs/loop/ACTA_AUDITOR.md, empieza en la
   linea 9452, leela hoy y cita las lineas que uses), con CERO caidas del
   ejecutor, ciega 7 de 7 (supervivientes del 392, 711 y 969, la D del
   233 adjudicada antes de destapar, las condiciones del 392, la costura
   del 711 y los grupos del 969), los nueve discutibles adjudicados A
   FAVOR o SIN ACCION, la racha de reporte en CERO con DOS reportes
   limpios seguidos, y la parada de la seccion 9 ADJUDICADA: la fase 02
   sigue por OP-D-08 y despues OP-D-09, por el criterio escrito de la
   propia fase (CONGELADOS LIBERADOS, aviso de la vuelta 17) y no por el
   campo orden; OP-D-07 queda esperando la lectura de su dependencia
   OP-M-03, anotada en el acta (seccion 4, punto 4).
2. VERIFICACION PUNTO POR PUNTO DE OP-D-01 Y OP-D-02, encargada por el
   acta (seccion 4, punto 3): cada una contra su campo verificacion de
   OPERACIONES.jsonl, con lo medido al lado, como el cierre de OP-D-06 lo
   modelo. Lo deferido se cita como deferido con su regla (el par nuevo
   entra POR EL RECOMPUTO, banco 9.10; las aristas son la fase 04): eso
   NO impide el registro. Si todo lo material cumple, escribes el
   REGISTRO DE OPERACION HECHA en la nota de cada una siguiendo el patron
   adjudicado en la vuelta 30 (el campo estado SE QUEDA EN LISTA y la
   declaracion vive en la nota con su evidencia, citando el acta de la
   vuelta 44). Si algo material NO cumple, no escribes el registro de esa
   operacion: lo declaras con la medicion delante y lo traes.
3. No hay caida de reporte que corregir: el reporte de la 44 salio limpio
   contra la corrida entera del auditor. Se dice asi y no se rellena la
   casilla.

TAREA 2, OP-D-08 y, si la vuelta tiene cuerda, OP-D-09. Las dos son
DESTEJIDO SOLO, sin fusion acoplada y sin superviviente que elegir; las
guardas del modo continuo aplican igual (simulacion previa sobre copia en
memoria, Gate 0 y suites en verde tras cada operacion, caso positivo, cero
duplicadas o auto-aristas tras resolver; aristas_nuevas esta VACIO en las
dos: cero aristas nuevas es parte del caso). Un destejido cambia el grafo
pero NO el censo: el ciclo Gate 0 lleva los comandos 1, 2 y 3, y el 4 SOLO
si tu operacion cambiara el censo, que aqui no debe pasar.
1. La apertura medida antes del primer acto (regla 1) y commiteada sola.
   Debe dar: marcador A 575, B 80, C 8, D 2.725 en n 3.388; grafo 3.853
   ficheros, 3.524 vivos, 329 deprecados, 16.898 enlaces; cola 1.494
   sobre 3.524. Son las cifras del cierre de la 44 verificadas por el
   acta; si tu medicion difiere, PARAS y lo declaras.
2. OP-D-08 (lienzo_modelo_negocio, destejido solo): la lees ENTERA de
   OPERACIONES.jsonl antes de tocar nada, y lees el nodo DE CERO. Su
   pregunta_pendiente se RESUELVE EN LA LECTURA, adjudicado por el acta
   (seccion 4, punto 2): la frase PARA LA SOLUCION DISENADA del paso 5 se
   lee con el ojo puesto en ella y se aplica la rama que corresponda de
   las dos que la propia operacion legisla (si es un MARCO propio, es
   material del bloque 2 y se reparte como el resto; si es solo un
   encabezado repetido, se va con su bloque). La resolucion se declara en
   el registro con la cita del texto delante y va como discutible marcado.
   El reparto ejecuta lo escrito: sobrevive UNA sola orden de completar
   los nueve bloques (la enumeracion 13 a 17, que preservar manda
   conservar como columna vertebral), se van los pasos 5 a 8 y el 9 en su
   forma actual, y NINGUNA linea de contenido propio se elimina, cada una
   comprobada en su casa antes de quitarla y no despues. CASO POSITIVO de
   la operacion, y es el que la manda: el par 784 SE DESCONGELA Y SE
   JUZGA (su razon es la unica del archivo con NO SE JUZGA HOY); su
   veredicto nuevo va con corregir_veredicto.py, correccion declarada y
   marcador recomputado. Tres commits como la forma asentada: lectura y
   plan sellado y simulacion ANTES de tocar; la cirugia con el ciclo
   verde; costuras post operacion, relecturas que vuelvan y registro de
   cierre.
3. OP-D-09 (planificacion_recoleccion_datos, destejido solo), SOLO si la
   vuelta tiene cuerda y OP-D-08 quedo cerrada con su ultimo commit
   pusheado: misma forma. Se van los pasos 2, 3 y 4 (el indice que se
   colo como pasos), cada uno con su paso del metodo que ya lo dice
   comprobado ANTES de quitarlo; el paso 1 se reparte como preservar
   manda; el metodo 5 a 16 no se toca. El desajuste 17 contra 16 del
   resumen_teorico NO SE RELLENA: es hueco nombrado que exige la fuente,
   fuera del repo. CASO POSITIVO: el par 2695 se relee contra el nodo
   destejido; si se vuelve A, ESO ES UN RESULTADO DE LA OPERACION Y SE
   ESCRIBE con su correccion declarada, no un fallo de la cirugia.
4. OP-D-07 NO SE ABRE en esta vuelta: su dependencia queda anotada en el
   acta y se adjudica cuando le toque por el criterio de la fase.
5. Si los actos no caben en la vuelta, cierras COMPLETA la operacion en
   curso hasta su ultimo commit pusheado, declaras cual queda y en que
   estado, y NINGUNA queda a medias SIN COMMIT. Reporte por vuelta con
   los discutibles marcados antes de saber si aciertas.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
