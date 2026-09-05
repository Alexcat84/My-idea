Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

La decision del fundador esta en
docs/loop/paradas/2026-09-05-la-bateria-sin-techo-DECISION.md, y la parada
entera en docs/loop/paradas/2026-09-05-la-bateria-sin-techo.md. Lo que ya
esta escrito y NO hay que volver a hacer:

- LA BATERIA SALE DEL CICLO POR VUELTA y corre CADA CINCO, en una VUELTA
  DE BATERIA propia (AUDITOR.md 6.1, citado en EJECUTOR.md regla 1).
  ESTA VUELTA NO LLEVA BATERIA: su hueco va DECLARADO Y MEDIDO por el
  carril de cerrar_reporte.py, con su medicion, su atribucion y su
  corrida. La proxima VUELTA DE BATERIA es la 175, o cuando el regimen
  diga.
- REGIMEN TEMPORAL DE DOS SUB-TAREAS (AUDITOR.md 6.2) hasta que DOS
  vueltas seguidas cierren su propio reporte. POR ESO ESTE ENCARGO TRAE
  EXACTAMENTE DOS, y no una mas.
- DOS REGLAS NUEVAS que ya rigen: LA RUTA QUE PROMETE PRUEBA ES CIFRA
  (una ruta a un fichero inexistente o de cero bytes es CAIDA DE CIFRA:
  antes de escribir una ruta como prueba, se comprueba que existe y que
  no esta vacia), y LOS DIENTES DE LA CAIDA DEL AUDITOR.

- TAREA 1, EL REPORTE, Y ES LA QUE ROMPE LA RACHA DE CUATRO. Dos mitades
  y ninguna es opcional:
  (1.a) CERRAR Y ARCHIVAR EL REPORTE DE LA VUELTA 172 con
  scripts/loop/cerrar_reporte.py. El instrumento EXISTE y esta probado
  con 17 mas 24 casos, y su pieza (4) ya admite el hueco declarado y
  medido, que era justo lo que le faltaba. Es la deuda mas vieja: el de
  la 172 no lo archivo nadie.
  (1.b) ABRIR EL REPORTE DE LA 174 Y CERRARLO, aunque esta vuelta no
  traiga mas trabajo que este. Un reporte que se abre y se cierra en la
  misma vuelta es exactamente lo que lleva cuatro vueltas sin pasar, y es
  la unica forma de empezar a contar las DOS seguidas que levantan el
  regimen temporal.
- TAREA 2, LAS DOS SUB-TAREAS QUE QUEDARON SIN EJECUTAR de la 172:
  (2.a) EL ACTA 172 AL R.42, que es el siguiente libre recomputado hoy
  (la serie tiene 33 entradas y su mayor es R.41).
  (2.b) QUE NAZCA scripts/loop/vuelta172_tarea1b_confirmar_r41.py, que el
  recuadro del R.41 PROMETE y que LLEVA DOS VUELTAS SIN EXISTIR. Ojo con
  la regla nueva: mientras ese fichero no exista, el R.41 esta publicando
  una ruta que promete prueba sobre un vacio, y eso ya es caida de cifra.

- OP-L-03 ESPERA A LA 175. Lleva cuatro vueltas aplazada y aguanta una
  mas: primero se recupera el cierre del reporte, que es lo que impide
  que cualquier otro trabajo quede registrado.
- DEUDA DE LECTURA ANOTADA, que no se ejecuta aqui pero no se pierde: el
  tramo 1 a 1085 del archivo queda en RELECTURA AL DOBLE por la regla del
  credito (AUDITOR.md 1.2). La discrepancia que la dispara es del puesto
  737, y el auditor la adjudico A FAVOR DEL ARCHIVO: el equivocado fue el.
- Y EL UNICO ARREGLO DE TEXTO PENDIENTE: la clausula de la 4.4 se corrige
  por el carril 9.10 (se tacha con su correccion fechada debajo, NO se
  borra).

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
