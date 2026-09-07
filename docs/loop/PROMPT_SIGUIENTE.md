Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

ESTA ES LA VUELTA DE BATERIA. AUDITOR.md 6.1 dice que NO LLEVA NADA MAS:
"la bateria entera, su doble corrida, su reloj y su salida sellada. Nada
de trabajo de plan al lado." Por eso este encargo tiene DOS tareas y la
segunda es la bateria. El trabajo de plan que YA ESTA ADJUDICADO por mi
acta 199 (la correccion declarada de OP-I-01 y la medicion de OP-L-02)
NO va aqui: va a la 201, y esta escrito al final para que no se pierda.

Lo que sigue vigente y no hay que rehacer:

- MORATORIA DE MAQUINARIA (AUDITOR.md 6.3). NO SE FABRICAN ARNESES,
  GUARDAS NI LECTORES NUEVOS. Esta vuelta NO TIENE NINGUNA EXCEPCION: las
  dos de la 199 se consumieron. Si una CAIDA DE DATO exige codigo, va CON
  SU CITA y se dice que lo es. LA NOMINA DE LA BATERIA SIGUE CONGELADA EN
  135: ni crece ni se poda. La poda se decide en la auditoria integral.
- EL TOPE NUMERICO DEL REPORTE SIGUE RETIRADO. Queda la letra
  cualitativa: nada que el registro ya diga, toda cifra tallada, las
  secciones obligatorias mandan.
- LA SERIE QUE DOBLA tiene RAIZ y TECHO EN 240. Mi tanda de la 199 NO
  rompio credito: la banda no llevaba marcado del ejecutor.
- RACHA DE REPORTE: 1. Mi acta 199 registra tu C.1 y acumula. Si esta
  vuelta trae otra que acumule, la racha llega a DOS y el acta 201
  encarga la operacion de codigo de la escalada sin esperar decision.

- TAREA 1, REGISTROS. Anexa mi acta 199 (docs/loop/ACTA_AUDITOR.md,
  lineas 69878 a 70229) al registro que corresponda, y escribe las TRES
  correcciones de cifra que mi seccion 3 levanta, cada una EN SU SEDE y
  por el carril del banco 9.10, con el texto viejo entero y sin tachar:
  (1.a) C.1, LA QUE ACUMULA. El reporte de la 199, seccion 8 y seccion 9,
  dice "1 arnes del censo queda fuera de la nomina con la vara 148" y
  nombra solo vuelta197_tarea2_mutacion_orden_del_turno.py. AL COMMIT DE
  CIERRE fceae11f SON DOS: el segundo es
  vuelta199_tarea1_mutacion_guardas_revividas.py, que lo escribio esa
  misma vuelta. NO LO CORRIJAS TECLEANDO EL DOS: vuelve a correr
  V.arneses_que_faltan(vara=148) y pega su salida con su corte. Mide
  tambien la cifra SIN VARA, que el reporte dio en 61 y por el mismo
  motivo ya no vale.
  (1.b) C.2. El reporte dice que docs/plan/10_INVENTARIO.md trae "el
  literal HUECO 4 veces". El literal sale 3; el 4 es el conteo insensible
  a mayusculas. Corrige la cifra O corrige la etiqueta, y di cual de las
  dos elegiste.
  (1.c) C.3. El mismo parrafo publica 414 lineas de ese fichero y tiene
  413. El 414 sale de split sobre un fichero que termina en salto de
  linea.
  Y LEE EL FILO DE MI SECCION 3 QUE NO COBRO: los tres grupos de tu
  seccion 4.c son la misma especie que la C.2 (la etiqueta nombra el tema
  y la cifra sale del patron). Tu cazaste esa especie tu mismo en tu
  TAREA 3 con el 'pares?'. Aparecio tres veces mas en la misma vuelta.

- TAREA 2, LA BATERIA ENTERA, POR TRAMOS, Y CON UNA TRAMPA MEDIDA
  DELANTE. El lanzador es scripts/loop/vuelta183_bateria_por_tramos.py y
  NO SE CLONA salvo que decidas lo contrario con su motivo escrito.
  LEE ESTO ANTES DE CORRER NADA, porque lo medi corriendolo y te va a
  mentir:
  (2.a) EL LANZADOR COMPUTA SU VUELTA DE SU PROPIO NOMBRE DE FICHERO (lo
  imprime: "vuelta (computada del nombre, no tecleada): 183") y NO admite
  --vuelta, asi que escribe siempre SALIDA_V183_BATERIA_TRAMO_N.txt.
  Corrido hoy, --siguiente dice: reparto de 11 tramos, 9 con salida
  sellada, faltan el 10 y el 11, EL SIGUIENTE ES EL TRAMO 10. ESOS NUEVE
  SON DE LA CORRIDA DE LA VUELTA 183, NO DE LA TUYA. Si te fias de
  --siguiente corres dos tramos y declaras la bateria hecha sobre nueve
  salidas ajenas, que es exactamente lo que la seccion 9 de la doctrina
  prohibe con estas palabras: "una corrida de otra vuelta pegada aqui
  tampoco vale".
  (2.b) Y LA OTRA MITAD: correr el tramo 1 PISA la sellada del 183.
  PRESERVA LAS NUEVE ANTES DE TOCAR NADA, por copia, con sus bytes y su
  sha256 medidos antes y despues, y publica las dos medidas. Copiar no es
  borrar: no se pierde ninguna prueba y por eso lo mando asi.
  (2.c) CORRE LOS ONCE TRAMOS, no los dos que faltan. AUDITOR.md 6.1 dice
  NUEVE tramos y HOY SON ONCE, medido con --plan: esa frase de la
  doctrina se escribio con una nomina menor y envejecio. Lo digo yo en el
  hallazgo 5.3 de mi acta 199 y va sin tocar AUDITOR.md, que es del
  fundador.
  (2.d) CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR, antes
  de seguir. Una vuelta cortada retoma en el tramo siguiente. Y UNA
  SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA.
  (2.e) LA BATERIA SE DECLARA CORRIDA CUANDO LOS ONCE TIENEN SALIDA
  SELLADA DEL MISMO CALIBRE, y el calibre lo coteja --componer, no tu
  criterio. Con su DOBLE CORRIDA y su reloj, que no se aflojan.
  (2.f) EN LA SECCION 9 DEL REPORTE, NOMBRA LOS DOS ARNESES DEL CENSO QUE
  QUEDAN FUERA DE LA NOMINA CON LA VARA 148, medidos por ti al abrir y al
  cerrar. No es un descuido de nadie: es consecuencia del congelado de
  6.3, y por eso se dice en vez de callarse. El segundo es de la vuelta
  199 y la bateria NO lo va a correr.

LO QUE LA 201 RECIBE, YA ADJUDICADO POR MI ACTA 199 Y FUERA DE ESTA
VUELTA POR LA CADENCIA DE 6.1, para que no se pierda:
- la CORRECCION DECLARADA de la evidencia de OP-I-01, por el carril del
  banco 9.10 mas 9.21 (adjudicacion 4.1 del acta 199): la ficha promete
  323 entradas y el fichero tiene 672. El 323 NO se borra, es testigo de
  su corte. La via es la que OP-L-01 uso en la vuelta 166 y OP-L-03 en la
  72, y el acta 71 la adjudico CON LAS PALABRAS NO ES PARADA;
- la MEDICION DE OP-L-02 CONTRA SU verificacion, no contra su evidencia
  (adjudicacion 4.2 del acta 199): sus tres clausulas son medibles y dos
  ya tienen salida sellada. Una ficha sin documento en evidencia NO es
  una ficha sin vara: la vara es verificacion, igual que la vara del
  trabajo pendiente es el instrumento y no el campo estado.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
