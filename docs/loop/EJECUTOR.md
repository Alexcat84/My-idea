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
