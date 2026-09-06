Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

La decision del fundador esta en
docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md; la parada
entera en 2026-09-05-cola-post-fusion.md y el resumen del auditor en
2026-09-05-cola-post-fusion-RESUMEN.md. Lo que YA esta escrito y no hay
que rehacer: la correccion declarada de la cola en
docs/plan/08_VERIFICACION.md, y en AUDITOR.md los tramos resumibles (6.1),
la letra ROMPER UN REMEDIO ESCRITO ACUMULA y la P.2 de los bytes.

ESTE ENCARGO TRAE CINCO TAREAS, que es el tope. Ni una mas.

- TAREA 1, LOS REGISTROS Y LA DEUDA DE LECTURA.
  (1.a) El acta 181 y sus adjudicaciones, en la serie de registros.
  (1.b) LOS DOS PENDIENTES DEL ACTA 180, que llevan una vuelta esperando:
  el remedio del E.1 sobre scripts/loop/cerrar_reporte.py, y la P.1 del
  censo.
  (1.c) LA RELECTURA AL DOBLE del tramo de la ciega ya encargada.
- TAREA 2, LA APERTURA DEL AUDITOR COMO CODIGO (decision 3, opcion c).
  Fichero GEMELO del bloque de apertura del ejecutor: corre
  aislador_de_ciega.py y SELLA SU SALIDA ANTES de que el turno pueda tocar
  git log, git status o REPORTE.md. Con CASO POR MUTACION sobre variable
  computada: si el sello se intenta despues de tocar cualquiera de los
  tres, TIENE QUE CAER. Es la mitad que quita el problema de raiz; la otra
  mitad (que romper un remedio acumule) ya esta escrita.
- TAREA 3, EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO (decision 1, la b).
  Cruza LA RAZON ESCRITA de cada D contra LOS PASOS DE HOY del otro nodo,
  y SOLO las D con la lesion exacta vuelven a la cola. CASO POSITIVO
  OBLIGATORIO: EL 2.464 TIENE QUE SALIR NOMBRADO (cero_defectos contra
  zero_defects_concepto; su razon se apoya en el AQL y el otro nodo lo
  absorbio el 20 ago 2026 en 02384c6a, ocho dias despues del veredicto de
  de20c078). Si el 2.464 no sale, el instrumento no sirve y se dice.
  Y EL CENSO POR ESTADO DE LAS A, en el mismo instrumento: ejecutadas
  contra pendientes, y LAS PENDIENTES CON TEXTO MOVIDO MARCADAS RANCIAS
  POR P.5. Las A NO ganan cola nueva: la ejecutada es cosa consumada y la
  pendiente ya la cubre P.5.
- TAREA 4, LAS D QUE EL INSTRUMENTO NOMBRE ENTRAN A LA COLA, y se releen
  POR TRAMOS en las vueltas siguientes. En esta vuelta se entra a la cola
  y se declara el tramo; no se releen 543 pares, que es justo lo que la
  decision evita.
- TAREA 5, LA VUELTA DE BATERIA VA EN LA 183, POR TRAMOS RESUMIBLES. Aqui
  solo se deja preparada y declarada: nueve tramos, cada uno se commitea
  CON SU SALIDA SELLADA al terminar, una vuelta cortada RETOMA EN EL TRAMO
  SIGUIENTE, y la bateria se declara corrida cuando LOS NUEVE tienen
  salida sellada DEL MISMO CALIBRE. En esta vuelta la seccion 9 del
  reporte cierra con su HUECO DECLARADO Y MEDIDO, como el regimen 6.1
  manda.

RECORDATORIO DE DOS REGLAS QUE YA MUERDEN: LA RUTA QUE PROMETE PRUEBA ES
CIFRA (antes de escribir una ruta como prueba se comprueba que el fichero
existe y que NO esta vacio), y LOS TAMANOS EN BYTES EXACTOS, nunca
redondeados, con los KB solo entre parentesis.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
