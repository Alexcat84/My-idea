Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

TAREA 1, registros (adjudicacion d6 del acta de las vueltas 34-36): anadir a
docs/loop/PROPUESTA_V35_RELECTURAS.json UN campo nuevo fechado (por ejemplo
"aviso_posterior") que diga que las cinco relecturas se volcaron el 18 ago 2026
en la vuelta 36 por scripts/loop/vuelta36_volcado_910.py (lote
docs/loop/_lote_v36.jsonl) y que el 643 fue por su propio carril
(docs/loop/_lote_v36_643.jsonl). SIN tocar el campo "estado" ni las filas
selladas: es la figura del AVISO DE CORTE, el sello se conserva y el aviso se
fecha. Nada mas de registro: las adjudicaciones viven en el acta.

TAREA 2, el trabajo: REANUDAR EL MODO DE EJECUCION CONTINUA (AUDITOR.md seccion
3) con OP-D-04 y las operaciones que sigan segun el orden del 00_INDICE. Para
OP-D-04 rige su nota tal como esta escrita: la fuente primero (verificar que
OP-F-02 y OP-F-03 estan ejecutadas antes de apoyarse en ellas), el destejido
despues, los tres gemelos 823, 834 y 844 al final y en un solo acto, y P.5 con
su alcance adjudicado: el acto se lee ENTERO despues de su destejido y antes de
su fusion, dentro del acto en operacion y nunca fuera. Guardas obligatorias por
operacion: simulacion previa sobre copia en memoria, Gate 0 y las suites en
verde tras cada fase con el derivado byte igual, caso positivo de cada
operacion, cero duplicadas o auto-aristas tras resolver, barrido del 9.10 de
toda tabla derivada en el mismo acto de cada volcado, y el criterio del
instrumento: toda cifra publicada sale de una corrida de ESTA vuelta. Si una
operacion necesita la cifra de costuras_internas.py mientras el instrumento se
declare mal calibrado, eso es guarda en rojo: PARAR y convocar, no improvisar
umbral. Una operacion cuyo texto no alcance para ejecutarse sin decidir es
PARADA, no una improvisacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
