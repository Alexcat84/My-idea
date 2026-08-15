Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3): corre las fases seguidas sin
esperar acta, con las guardas obligatorias por operacion. dataset/ SI
se toca en esta fase, porque el texto de cada operacion lo ordena.
Cualquier guarda en rojo fuera de lo que 08_VERIFICACION.md declara
permitido, o cualquier operacion cuyo texto no alcance para ejecutarse
sin decidir, te detiene a ti y convoca al auditor.

EJECUTOR.md, regla 1, con sus tres renglones: LA CITA LLEVA SU LINEA; EL
ESTADO AL CIERRE SE MIDE AL CIERRE; LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION. La vuelta 30 los cumplio los tres y la racha de
caidas de reporte quedo cortada en cero: sostenlo.

====================================================================
TAREA 1: registros del acta de la vuelta 30
====================================================================
1. Registra en docs/plan/OPERACIONES.jsonl (nota, correccion declarada,
   sin borrar el texto viejo) que OP-F-04-WEI y OP-F-04-HOR quedan
   HECHAS, citando la adjudicacion 1 del acta de la vuelta 30 con sus
   palabras (13 de 13 cada una, 11 mas 2 y 12 mas 1, casos positivos y
   guardas verdes por la corrida del auditor); y que OP-F-04-RAC queda
   HECHA citando las actas 27 y 29, que ya la adjudicaron.
2. Registra en la nota de OP-F-04-COL, como correccion declarada, que
   su campo adjudicacion (11 ago, los 15 con bloque apendice) queda
   corregido por la medicion de la vuelta 30: son 14 de 15, y
   keep_customers_strategy trae el material EMBEBIDO (el nodo no se
   toca desde el 8 ago; la lectura vieja era floja en ese nodo). El
   campo viejo se queda entero.
3. Registra en 01_FUENTES.md, junto al hallazgo de
   keep_customers_strategy, la adjudicacion 2 del acta de la vuelta 30
   citada con sus palabras: MULTIFUENTE LEGITIMO por extension citable
   de P.19 (el material de Coleman comparte el objeto del nodo, no
   repite y no forma bloque: ya esta en el estado final que P.19
   produce, no hay operacion que ejecutar), SIN corte y con la fuente
   intacta. La marca DISCUTIBLE se queda con la adjudicacion al lado.
   Limites escritos: si una lectura futura declara un tramo AJENO al
   objeto, entra por la segunda puerta de la cola.
4. Amplia el detector de fronteras (vuelta30_estado.py o sucesor) para
   que reconozca la forma de subseccion que P.20 le dio a la frontera
   de viral_loop_marketing, con el cambio declarado dentro del script
   y el motivo escrito, y verifica que de 14 de 15 con
   keep_customers_strategy como el unico NO (adjudicacion 4 del acta:
   la vara de cierre del primer tiempo es la lectura, 14 de 15).
5. Pregunta 3 del reporte: adjudicada NO. P.20 no se toca; el registro
   de metas_vs_proposito en 01_FUENTES.md es su sede. El valor HECHA
   del campo estado tampoco se estrena (adjudicacion 7): las
   declaraciones siguen en nota.

====================================================================
TAREA 2: OP-F-04-COL, SEGUNDO TIEMPO, y la fase 01 CERRADA
====================================================================
1. Ejecuta los destinos por P.18 sobre la nomina de Coleman medida AL
   DIA (no la de una vuelta anterior). LA CUENTA CONFIRMADA POR EL
   ACTA ES 13 DESTINOS: 15 de la nomina, menos viral_loop_marketing
   (su mitad ya esta hecha por el corte unico de P.20 y la nota lo
   cita) menos keep_customers_strategy (adjudicado sin corte, TAREA
   1.3). metas_vs_proposito entra con su frontera vigente 1 a 4 / 5 a
   9. El bloque 5 a 17 de blueprint_de_experiencia puede partirse en
   subbloques por OBJETO (la frontera es de libros y el destino es de
   objetos, como su propia fila lo declara): cada subbloque con su
   lectura y su destino propios.
2. Guardas por corte, las de siempre: simulacion previa sobre copia en
   memoria, guarda de texto, caso positivo antes y despues con su
   prueba de conservacion, cero duplicadas y cero auto-aristas. Cada
   miembro elegido o nodo propio con su correccion declarada por P.18
   punto 2; cada nodo propio que nazca, declarado en
   docs/plan/INDICE_ROJO_DECLARADO.jsonl; ciclo de Gate 0 entero tras
   cada operacion (el cuarto comando solo si se mueve el censo) y las
   suites en verde.
3. Con los trece destinos ejecutados y las guardas verdes, declara en
   el reporte OP-F-04-COL ENTERA con su medicion, y con las cuatro
   OP-F-04 mas OP-F-02 y OP-F-03 HECHAS, LA FASE 01 QUEDA CERRADA.
4. Sigue en MODO CONTINUO a la FASE 02 DESTEJIDOS, en el orden del
   00_INDICE, con Gate 0 verde por el ciclo escrito y las suites en
   verde tras cada fase. Recuerda: las cuatro entradas de LA COLA DEL
   OBJETO AJENO son operaciones de la fase 02 y su comprobacion vence
   al cierre de esa fase, no antes.

Las lecturas ya publicadas y verificadas (las fronteras de la tabla de
los doce, la frontera de tres libros de viral_loop_marketing, los doce
discutibles de la ciega del acta 30) NO se rehacen: ejecuta sobre esa
lectura.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
