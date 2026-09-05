# EJECUTOR.md, reglas permanentes del ejecutor del bucle

Eres la sesion ejecutora de la campaña My Idea. Cada vuelta del bucle te da un
encargo en docs/loop/PROMPT_SIGUIENTE.md. Estas reglas valen SIEMPRE, ademas de
lo que diga el encargo.

1. LA CITA LLEVA SU LINEA (14 ago 2026; motivo: tres tandas seguidas con
   caida de reporte, vueltas 24, 26 y 27, dos de ellas reincidiendo en
   afirmar el estado de una adjudicacion o de un conteo sin haberlo vuelto a
   mirar). Toda afirmacion sobre el estado del registro (actas previas,
   adjudicaciones, preguntas ya cerradas, conteos de ficheros o de salidas)
   se escribe CON LA MEDICION DEL DIA AL LADO: la linea del acta leida hoy, o
   el conteo corrido en esta vuelta. Si no hay linea que citar, la afirmacion
   no se escribe.
   EL ESTADO AL CIERRE SE MIDE AL CIERRE (14 ago 2026; motivo: la caida de la
   vuelta 28, donde la tabla del cierre traia la medicion de APERTURA
   despues de que la propia vuelta la moviera). Toda tabla o cifra que
   describa el estado al cerrar la vuelta se RECOMPUTA AL CIERRE si algo de
   la propia vuelta pudo haberla movido: medir temprano y publicar tarde sin
   remedir es la misma especie de caida que citar sin mirar.
   LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION (14 ago 2026; motivo:
   la caida de la vuelta 29, donde la cifra citada como apertura era el
   estado tras la primera operacion de la propia vuelta). El estado TRAS la
   primera operacion ya es estado intermedio, no apertura, y se cita como
   tal: con el nombre de la operacion que ya lo movio.
   LA TABLA SE IMPRIME, NO SE TECLEA (15 ago 2026; motivo: las paradas de
   credito de las vueltas 31 y 32, las dos por celdas manuales en tablas de
   prosa de docs/plan/ que ningun instrumento validaba: un nombre trunco, un
   numero de origen en el grupo equivocado). Toda tabla o mapa cuyo
   contenido exista en un instrumento o en un plan sellado se genera desde
   el instrumento y se pega entera, con el comando citado al lado. Toda
   tabla de particion (fila = destino, origenes, motivo) se pasa por
   scripts/loop/verificar_mapas_destejido.py antes del commit, con su
   salida citada en el reporte.
   LA CABECERA DEL REPORTE SE TALLA, NO SE TECLEA (20 ago 2026; motivo: la
   racha de las vueltas 54, 55 y 56, las TRES frases tecleadas en la
   cabecera del reporte, ninguna salida de un tallador. La de la 56 es el
   ejemplar: la celda del cierre publicaba 623 igual a 623, que era la cifra
   de la APERTURA heredada, cuando el instrumento del cierre dice 529). Las
   tablas de apertura y cierre del reporte se generan con
   scripts/loop/tallar_cabecera_reporte.py --vuelta N y se pegan enteras,
   con el comando citado al lado; LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
   SE ESCRIBE. Antes del commit, --comparar docs/loop/REPORTE.md tiene que
   dar CABECERA IDENTICA AL TALLADOR, y su salida se cita en el reporte.
   LA TABLA SE CUENTA DE SU FICHERO (26 ago 2026; motivo: la racha de las
   vueltas 74, 75 y 76, otra vez frases tecleadas, esta vez DONDE EL
   TALLADOR DEL CRIBADO NO ALCANZA. El tallador lee salidas de marcador y
   recomputo, y una fase mecanica no produce ninguna de las dos: desde que
   el bucle entro al tramo mecanico las cifras del reporte volvieron a
   teclearse. El ejemplar de la 76: el reporte publica 13 CONFIRMA y 12 DEJA
   IGUAL de la vara 9.6.1, y su propio fichero de salida, contado, dice 14 y
   11). TODA TABLA O CIFRA DEL REPORTE CITA EL FICHERO DE SALIDA DEL QUE
   SALE, Y SE RECONSTRUYE CONTANDO ESE FICHERO ANTES DE PUBLICARLA. Si no
   existe fichero que contar, LA TABLA NO SE PUBLICA: se corre el
   instrumento que la produzca, o se dice que no hay cifra.
   Y LA ESCALADA, escrita para que no haya que volver a pararse a decidirla:
   SI LA RACHA DE CAIDAS DE REPORTE LLEGA A DOS TANDAS OTRA VEZ, la
   extension del tallador a las fases mecanicas (toda tabla del reporte
   tallada de ficheros de salida, como ya se hace con la cabecera del
   cribado) queda AUTOMATICAMENTE ENCARGADA como operacion de codigo en la
   vuelta siguiente, SIN esperar parada ni decision nueva del fundador.
   LA IDENTIDAD SE LEE DE GIT (26 ago 2026; motivo: la racha de las vueltas
   77, 78 y 79, tres frases sueltas seguidas, y la de la 79 entro por LA
   PROSA DE IDENTIDAD, que queda fuera de las seis filas que el tallador
   --fase04 ya talla: la linea del commit de apertura es prosa suelta encima
   de la tabla y siguio tecleandose a mano. El ejemplar de la 79: el reporte
   publica como commit de apertura 43b02413, que es el commit de la TAREA 4
   de esa misma vuelta, escrito por el propio ejecutor a mitad del trabajo;
   la apertura verdadera es aea7cc81, el acta de la vuelta 78, y la propia
   tabla del reporte ya lo delataba, porque sus cifras de apertura son las
   que mide aea7cc81 y no las del arbol del hash publicado). TODO HASH,
   NOMBRE DE COMMIT, RAMA O FECHA DE APERTURA O DE CIERRE QUE EL REPORTE
   PUBLIQUE SE LEE DE git rev-parse O DE git log EN ESA VUELTA Y SE TALLA;
   UNA LINEA DE IDENTIDAD TECLEADA NO SE PUBLICA.
   EL CASO ROJO SE PRUEBA POR MUTACION (29 ago 2026; motivo: la caida 2 de
   la vuelta 89, un caso rojo que no puede fallar publicado como prueba de
   que el criterio se comporta. En scripts/loop/vuelta89_tarea3_rebase_ope06.py
   la variable del veredicto era una CONSTANTE LITERAL, veredicto_2 = "ENTRA",
   y el assert comparaba "ENTRA" con "ENTRA": no puede salir en rojo nunca. La
   clasificacion real de las 129 filas era una tabla escrita a mano, cosa que
   el reporte declaraba con honestidad; lo que faltaba era decir que ENTONCES
   NO HAY CASO ROJO AUTOMATICO, en vez de fabricar uno que se aprueba solo).
   NINGUN assert, GUARDA O CASO ROJO SE PUBLICA COMO PRUEBA SIN HABER CORRIDO
   ANTES SU PRUEBA DE MUTACION: se cambia el valor esperado y se comprueba que
   el caso CAE. Si la clasificacion es una tabla a mano y no hay nada que
   mutar, SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO, y esa declaracion es la
   que se publica.
   EL REPORTE ABRE CON LA VUELTA (4 sep 2026, decision del fundador; motivo:
   las vueltas 166 y 167 terminaron SIN REPORTE, dos seguidas, y en las dos la
   bateria quedo ademas en un fichero de cero bytes. docs/loop/REPORTE.md
   seguia siendo el de la 165. Un reporte que se escribe al final es lo primero
   que se cae cuando la vuelta se corta, y cuando se cae no queda NADA: ni las
   tareas que si salieron). EL REPORTE SE ABRE AL EMPEZAR Y CRECE POR ANEXION:
   el ESQUELETO se talla en la apertura, con la cabecera y las filas vacias de
   las tareas encargadas; CADA TAREA ANEXA SU FILA AL CERRARSE, no al final de
   la vuelta; y el cierre lo talla entero. UNA VUELTA CORTADA DEJA REPORTE
   PARCIAL, NUNCA VACIO, y el parcial dice hasta donde se llego. TOPE DE CINCO
   TAREAS POR VUELTA: si el encargo trae mas, se entregan cinco y las demas se
   declaran como cola, en vez de empezar seis y no cerrar ninguna.
   LA BATERIA CORRE CADA CINCO VUELTAS, NO CADA UNA (5 sep 2026, decision del
   fundador; el regimen entero vive en AUDITOR.md seccion 6.1 y es citable
   desde paradas/2026-09-05-la-bateria-sin-techo-DECISION.md). La bateria de
   mutaciones deja de ser obligatoria en cada vuelta: corre CADA CINCO, en una
   VUELTA DE BATERIA propia que NO LLEVA NADA MAS. En las vueltas intermedias
   la seccion 9 del reporte SE CIERRA IGUAL, con el HUECO DECLARADO Y MEDIDO
   por el carril de cerrar_reporte.py, que lleva su medicion, su atribucion y
   su corrida o no vale. Motivo medido: la nomina paso de 23 a 82 entradas,
   cada una se corre DOS veces, y la salida de la bateria del ejecutor salio en
   CERO BYTES tres vueltas seguidas (171, 172 y 173) mientras cuatro vueltas
   seguidas dejaban de cerrar su propio reporte. NO SE AFLOJA NINGUNA GUARDA:
   la bateria sigue entera y sola, y LA NOMINA SIGUE CRECIENDO porque nadie la
   poda sin el fundador.
   Y MIENTRAS DURE EL REGIMEN TEMPORAL (AUDITOR.md 6.2): los encargos traen
   MAXIMO DOS SUB-TAREAS hasta que DOS vueltas seguidas cierren su propio
   reporte con cerrar_reporte.py. Logrado eso, vuelve el tope de cinco.
   LA RUTA QUE PROMETE PRUEBA ES CIFRA (5 sep 2026): una ruta publicada como
   evidencia de una corrida cuenta como CIFRA PUBLICADA en su sede, y si apunta
   a un fichero inexistente o de CERO BYTES es CAIDA DE CIFRA. Antes de escribir
   una ruta como prueba, se comprueba que el fichero existe y que no esta vacio.
2. EL INSTRUMENTO MANDA (14 ago 2026; motivo: las caidas de las vueltas 15
   y 16 fueron las dos de esta especie). Toda cifra o nombre propio que se
   publique se lee de la salida del instrumento corrido EN ESTA VUELTA. Una
   nota vieja, un acta previa o un reporte anterior NUNCA son fuente de una
   cifra nueva: se citan como contraste, y si discrepan de la medicion de
   hoy, la discrepancia se declara en vez de resolverse copiando.
3. Commitea y pushea lo pendiente en la rama activa ANTES de tocar nada.
4. MODO DE CIERRE mientras la campaña este en fase de cribado o recomputo: se
   lee, se mide y se documenta; CERO reparaciones de nodos. Los nodos solo se
   tocan cuando el encargo diga explicitamente que la campaña entro en fase de
   EJECUCION, y entonces solo en la rama que el encargo indique.
5. Doctrinas tal como estan escritas (docs/BANCO_DE_TEXTOS.md secciones 9.x,
   docs/plan/BANCO_DEL_PLAN.md P.1 a P.15). No inventes reglas. Si un par o una
   operacion pide una regla que no existe: NO pares, registra lo mejor
   sostenido, marcalo PENDIENTE DE DOCTRINA en su razon, y sigue. Paras SOLO si
   algo contradice una regla vigente o una cifra publicada con su corte: en ese
   caso lo escribes en el reporte como PARADA y no lo arreglas tu.
6. COMMIT Y PUSH POR TRAMO (~50 a 100 pares, o por operacion en ejecucion), para
   que nada dependa de que la sesion aguante. Los hallazgos que no pueden
   esperar van al mensaje del commit.
7. Reportes SOLO en checkpoints (multiplos de 100 en el cribado; por fase en la
   ejecucion). El reporte completo va en docs/loop/REPORTE.md (sobrescribe el
   anterior) con: hash final, rutas tocadas, marcador recomputado del archivo,
   tasa por dominio, vara por tramo, figuras y familias al dia, correcciones
   declaradas, PENDIENTES DE DOCTRINA, y LOS DISCUTIBLES MARCADOS para la
   relectura ciega del auditor (marcados ANTES de saber si aciertas).
8. Toda cifra con su fecha de corte; toda glosa con el corte de la cifra que
   interpreta; toda correccion declarada sin borrar el texto viejo ("una
   correccion que tapa lo que corrige no se puede auditar"); toda cifra de un
   autor con su atribucion.
9. Todo conteo que toque ids pasa por el resolutor antes de contar (P.1).
   Toda perdida de catalogo declarada se re-verifica contra el grafo, sin
   importar quien la declare ("una busqueda negativa no se puede citar").
10. Cero guiones largos y cero guiones medios en todo lo que escribas. Deja
    correr el hook; si falla, corriges y reintentas, jamas lo saltas.
11. No adivines. Lo que no este escrito y no puedas medir, lo traes como
    pregunta en el reporte.

## MODO AUSTERO (27 ago 2026)

MODO AUSTERO (decision del fundador, 27 ago 2026), vigente desde la
proxima vuelta y hasta la apertura de la fase 06:

1. LOTES AL DOBLE: las lecturas dirigidas van en tramos de 80 pares (no 40);
   cuando dos operaciones quepan en una vuelta con sus guardas completas, van
   las dos.
2. EL REPORTE SE ENCOGE: tope de 80 lineas. Cabecera tallada, tablas talladas
   con su comando, adjudicaciones por numero y linea, y las decisiones de
   lectura en el registro JSONL (no narradas en prosa). Queda prohibida la
   prosa de acompanamiento que repite lo que el registro ya dice.
3. EL ACTA SE ENCOGE IGUAL: tope de 60 lineas cuando no hay caidas ni
   discutibles fuera del marcado. La verificacion NO se recorta: Gate, suites,
   talladores y ciega sobre el registro siguen enteros; lo que se recorta es su
   narracion.
4. NINGUNA GUARDA SE TOCA: simulaciones, casos positivos por mutacion, ciclo de
   Gate 0, talladores y la metrica de credito siguen identicos. El austero
   recorta tinta, no control.
5. Al abrir la fase 06 (cirugia), el modo austero SE SUSPENDE solo y vuelve el
   regimen completo.
