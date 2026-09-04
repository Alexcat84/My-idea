Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

La decision del fundador esta en
docs/loop/paradas/2026-09-04-estado-de-las-fichas-DECISION.md, y la parada
entera en docs/loop/paradas/2026-09-04-estado-de-las-fichas.md. Lo que ya
esta aplicado y no hay que volver a hacer:

- EL CAMPO estado QUEDA JUBILADO COMO HISTORICO. LA VARA DEL TRABAJO
  PENDIENTE ES EL INSTRUMENTO,
  scripts/loop/vuelta150_3_relectura_expediente.py, NUNCA EL CAMPO. Ya
  esta declarado en docs/plan/00_INDICE.md por correccion declarada y
  citado en AUDITOR.md seccion 0.
- EL REPORTE ABRE CON LA VUELTA, ya escrito en EJECUTOR.md regla 1:
  esqueleto tallado en la apertura, cada tarea anexa su fila AL CERRARSE,
  el cierre lo talla, y TOPE DE CINCO TAREAS POR VUELTA. Este encargo trae
  exactamente cinco.

- TAREA 1, LOS REGISTROS. El acta 167 y sus adjudicaciones a R.37. Y LA
  NOTA ADOSADA AL R.36 por la adjudicacion 6.5 del acta 167: sus glosas de
  la 6.1, 6.3, 6.4 y 6.9 describen LO ENCARGADO y no LO OCURRIDO, y la
  nota lo dice sin borrar el texto viejo.
- TAREA 2, EL REPORTE QUE CUBRA LAS VUELTAS 166 Y 167. Es la deuda de dos
  vueltas: docs/loop/REPORTE.md sigue siendo el de la 165. Se abre POR
  ANEXION DESDE YA, con la regla nueva estrenandose sobre si misma: el
  esqueleto primero, y cada tarea de ESTA vuelta anexa su fila al
  cerrarse. Lo de las 166 y 167 se reconstruye de los commits y de las
  actas, y lo que no se pueda reconstruir SE DECLARA COMO NO
  RECONSTRUIBLE en vez de rellenarse.
- TAREA 3, EL MANTENIMIENTO DE LA BATERIA, autorizado por la decision 4.
  Los dos rojos son guardas que muerden algo cierto, no guardas rotas:
  (3.a) LOS SEIS ARNESES nacidos en las vueltas 166 y 167 entran A LA
  NOMINA; (3.b) EL ANCLA DE MUTACION de
  vuelta165_tarea6_mutacion_op_l_01.py pasa de TRES clausulas a CINCO,
  porque la vuelta 166 le puso cinco a OP-L-01 por adicion y el auditor lo
  adjudico bien; (3.c) LA BATERIA SE RE CORRE ENTERA Y SE PEGA su salida,
  y tiene que salir en VERDE. Si algun rojo sobrevive al arreglo, se trae:
  no se afloja la guarda para llegar al verde.
- TAREA 4, OP-V-01 POR LA DECISION 5, y viene medio resuelta: EL COMMIT
  QUE MOVIO SU estado ES e966d896, "LA FASE 08 QUEDA CERRADA: el vuelo
  completo en 16 de 16 con exitcode 0", de la SESION CON CREDENCIAL del
  fundador. Lo comprobe por git antes de escribir esto, que es lo que la
  decision manda y lo que el acta 167 declaro no haber hecho. Asi que hay
  prueba: la nota de la ficha se escribe con LA CORRIDA K y LOS CINCO
  PUNTOS TRANSVERSALES como prueba por cita (Gate 0 con su ciclo entero y
  26 en OK, las tres suites, el vuelo 16 de 16, la prueba de rumbos sin
  deriva, y el reindexado con sus sellos d70adc1d y 42223fcc). VERIFICALO
  TU TAMBIEN antes de escribirlo: si el commit no dice lo que aqui se
  dice, la ficha vuelve a pendiente, que es lo que la decision manda.
- TAREA 5, ABRIR LAS SEIS POR LA VARA DEL INSTRUMENTO, y en este orden:
  (5.a) OP-I-01 (10_INVENTARIO, sin dependencias) y OP-L-01
  (09_LECTURAS_DIRIGIDAS, su clausula 3 sigue abierta) PRIMERO, que son
  las dos que no dependen de nadie.
  (5.b) LAS DOS OP-M-02 CON SU VALVULA DE VIGENCIA, Y LA VALVULA VA ANTES
  DE TOCAR NADA: OP-M-02-MEDIOS y OP-M-02-ADMIT son de la fase 03, que
  quedo CERRADA CON REMISION el 26 ago, y las seis fusiones que esa
  remision enruto NO SON ESTAS DOS. Asi que ANTES de ejecutar, SUS NOMINAS
  SE RESUELVEN CONTRA EL GRAFO DE HOY. Si el acto ya lo consumieron las
  unificaciones, LA OPERACION SE DECLARA CUMPLIDA POR CONSUNCION con la
  medicion citada, y no se ejecuta. SOLO SE EJECUTA LO QUE SIGA VIVO.
  (5.c) LOS depende_de DE OP-L-02 Y OP-L-03 SE LEEN POR EL INSTRUMENTO, no
  por el campo. Sus seis OP-D-* estan en LISTA y TODAS con prueba de
  ejecucion: por la vara nueva eso es cumplido, y por eso las dos dejan de
  estar bloqueadas. Si el instrumento dice otra cosa, paras y lo traes.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
