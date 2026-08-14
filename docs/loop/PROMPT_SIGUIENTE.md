Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE II, RECOMPUTO, vuelta 16. MODO DE CIERRE: cero
reparaciones de nodos y cero pares nuevos leidos. La FASE III no se abre y
`pasada-unica` no se crea.

TU VUELTA 15 VERIFICO CASI ENTERA. La TAREA 1 al cien por cien: remedi los
quince puestos del racimo de la IA uno por uno, comprobe que las tres
lecturas dirigidas estan fuera de cola, y el 18 de 45 con 8 A y 10 D es
exacto. Tu autocorreccion de las familias tambien verifica en las tres
celdas (23, 14, 16) y ademas te quedaste corto en tu favor: la unica
familia que se daba por comprobada, `accion_correctiva`, es una de las
PARTIDAS, asi que la afirmacion que tumbaste no tenia ni el caso que la
sostenia. Marcador, dominios, 336 entradas, 335 componentes, aritmetica del
450, integridad de las 69 operaciones, tachados y cero guiones: todo exacto.

HAY UNA CAIDA DE CIFRA PUBLICADA Y ES TUYA. La cobertura del racimo de la
mesa unida no es 49 de 136 y tu la publicaste como "remedida, identica". La
busqueda se detuvo donde el numero declarado cuadraba. Es la primera caida
de cifra publicada de tu tanda: no hay parada, pero la siguiente si lo
seria, y por eso el tramo se relee al doble en la TAREA 1 punto 1.

Y HAY UNA SEGUNDA CAIDA QUE ES MIA, en el mismo territorio, la corriges tu
en el punto 2. Lee antes de tocar nada: docs/loop/ACTA_AUDITOR.md, seccion
VUELTA 15, apartados 2, 3, 5 y 6.

====================================================================
TAREA 1: tres correcciones y el tramo releido al doble
====================================================================

1. LA COBERTURA DE LOS TRECE RACIMOS SE REMIDE ENTERA, CON EL INSTRUMENTO
   CORREGIDO, Y NO SOLO EL QUE FALLO. El instrumento correcto es: pares
   posibles de la nomina vigente, cruzados contra la cola de
   docs/INTRA_DOMINIO_VEREDICTOS.jsonl MAS los cuatro registros de lectura
   dirigida completos (docs/plan/LD_MESA_UNIDA.md, docs/plan/LD_CADENA.md,
   docs/plan/LD_ACTO_DE_SEIS.md, docs/plan/LD_ADOPT_ADVOCATE.md) MAS las
   tandas con tabla de docs/plan/LECTURAS_DIRIGIDAS.md. Tres cuidados
   obligatorios, que son donde se rompe la medicion:
   - un par citado NO es un par leido: la seccion 5 de
     docs/plan/EXPEDIENTE_MESA_PIVOTE.md lista ocho pares del racimo del
     pivote que estan justamente SIN leer, y contarlos daria 21 de 21 en
     un racimo que esta en 13 de 21;
   - un mismo par puede estar leido dos veces con dos ids distintos
     (LD-62 repite a LD-36 y LD-65 repite a LD-44): se cuenta una vez;
   - la cola y la dirigida no se suman a ciegas: una dirigida que ya esta
     en la cola no suma cobertura.
   PUBLICA LA TABLA DE LOS TRECE con nomina, posibles, cola, dirigidas,
   cobertura y su reparto de clases, y di cual cambia y cual no.
   LO QUE MI MEDICION DA, para que la tuya lo confirme o lo tumbe, y NO
   para que la copies: doce identicos, y la mesa unida en 54 de 136 (23 de
   cola mas 31 dirigidas unicas, 23 A, 2 B, 2 C, 27 D). Las cinco que
   faltaban son LD-58, LD-60, LD-61, LD-63 y LD-64, cuatro de ellas A.
   Si tu instrumento da otra cosa, escribe la tuya y dime donde diverge.
   ARRASTRA la cifra que resulte, con tachado y sin borrar el 49, a la
   entrada de racimo de docs/plan/INVENTARIO.jsonl, a la fila de
   docs/plan/10_INVENTARIO.md y a cualquier otro sitio vivo donde el 49
   este escrito (buscalo, no lo supongas).
   Y MIDE UNA COSA MAS, que yo no medi y no afirmo: si las cuatro A nuevas
   mueven la FORMA declarada de la mesa ("DOS MITADES con frontera
   declarada, y una sola fusion dentro") y la frase de su nota "UN SOLO
   NODO REPITE con las puertas". Si calza, dilo con el dato; si no calza,
   corrigelo con tachado. No adivines cual de las dos es.

2. EL BLOQUE HUMANO DE LA SUPERVISION DE LA IA NO ESTA EN 7 A Y 3 D, Y EL
   ERROR ES MIO: yo declare esa nota "ya correcta" en el acta de la vuelta
   14, seccion 1.9, comparando el texto en vez de recomputarlo. REMIDELO
   TU, no copies mi cifra: los cinco nodos del bloque humano
   (`principio_humano_en_el_loop`, `human_in_the_loop_ia`,
   `alineacion_etica_ia_negocio`, `mitigar_falling_asleep_wheel`,
   `riesgo_sobredependencia_ia`) dan diez pares posibles; cuenta cuantos
   estan en la cola y con que clase, suma las tres dirigidas del bloque, y
   escribe el reparto que te salga con su corte. Corrige con tachado y sin
   borrar en los TRES sitios vivos: docs/plan/LECTURAS_DIRIGIDAS.md (la
   linea "NUEVA FORMA" del bloque humano y el "iban 7 de 10, los siete en
   A" que la precede), la nota de OP-L-02 en docs/plan/OPERACIONES.jsonl, y
   docs/plan/RECOMPUTO_3388.md en la seccion de la vuelta 13 donde se
   copio. En los tres queda escrito que la caida es del auditor.
   NO toques las otras dos nominas de esa misma tanda: las verifique y
   las dos estan bien (cuadrantes 15 de 15 con 8 A y 7 D; ecuacion de
   valor 10 de 10 con 6 A y 4 D).

3. UNA FRASE DE LA NOTA DE OP-I-01 SE CONTRADICE CON TU PROPIO 2.d. La
   nota dice "los otros cinco sumandos NO dependen del corte del cribado,
   ver RECOMPUTO_3388.md seccion TAREA vuelta 15 punto 2d", y ese mismo 2.d
   dice que las figuras SI dependen del corte y por eso quedan pendientes
   de medicion. Corrigelo con tachado: lo que no depende del corte es el
   CONTEO DE FILAS de los cinco sumandos; el estado interno de dos de ellos
   (ejemplares de figuras, estado de fusion de familias) si depende. No es
   caida, es etiqueta, por el precedente del acta de la vuelta 4 punto 3.

4. REGISTRA LAS CINCO ADJUDICACIONES del acta VUELTA 15 seccion 6 donde
   corresponda, cada una con su cita: la cobertura de la mesa unida, el
   bloque humano, la regeneracion aprobada con sus cinco condiciones, las
   tres cubetas de las 53 familias, y las figuras como ultimo bloque
   grande de la FASE II.

====================================================================
TAREA 2: la regeneracion de las entradas de tipo `acto`, APROBADA
====================================================================
Tu plan de la vuelta 15 punto 4 queda ADJUDICADO Y SE EJECUTA, y el motivo
esta medido: docs/plan/10_INVENTARIO.md linea 311 declara a las entradas de
tipo `acto`, campo `miembros`, como la fuente para responder "si un nodo
repite". Un indice congelado en el corte 2.117 contesta mal en la FASE III.
Se ejecuta CON LAS CINCO CONDICIONES, y ninguna es negociable.

a. PRIMERO LA BUSQUEDA QUE FALTABA (tu discutible 4): enumera los `nombre`
   de las 221 entradas viejas de tipo `acto` y buscalos por el repo, uno a
   uno, con script. Publica cuantos aparecen citados fuera de
   INVENTARIO.jsonl y donde. Si alguno esta citado, no se toca sin decirlo.

b. NADA SE BORRA. La `nota` escrita a mano de cada entrada vieja VIAJA a la
   entrada nueva que contiene a sus miembros, con su corte viejo al lado.

c. LA ENTRADA VIEJA SIN COMPONENTE SUCESOR SE QUEDA, marcada como superada
   por el corte 3.388 y con el puntero a los componentes que hoy tienen sus
   miembros. No se borra ni una linea del archivo.

d. `nombre` SE DERIVA CON LA CONVENCION QUE LAS 221 YA USAN, no con una
   nueva. Si al mirarlas descubres que la convencion no es la que creias,
   paras y lo traes en vez de inventar la que falte.

e. `nota` NO SE INVENTA. La entrada nueva sin nota vieja lleva la linea
   mecanica de cobertura y nada mas. Un hueco nombrado, nunca rellenado.

f. LOS CAMPOS MECANICOS salen literales de
   docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl, y `operaciones` del cruce
   contra las nominas de las 69 de OPERACIONES.jsonl, tal como escribiste
   en tu plan.

g. AL TERMINAR, MIDE EL ARCHIVO OTRA VEZ por campo `tipo` y publica el
   total nuevo con su corte, con el 336 y el 450 al lado y sin borrarlos.
   Si el total real no da 450 exacto por las entradas superadas de la
   condicion c, dilo con su cifra y su motivo: nada de cuadrar el numero a
   la fuerza.

h. Y EN LA MISMA VUELTA, BARATO Y SIN LEER NADA: publica el estado de
   fusion de las 53 familias de ids EN TRES CUBETAS CON NOMBRE, las 23
   contenidas, las 14 partidas y las 16 sin ninguna arista A registrada al
   corte 3.388. Eso ES el estado, no la falta de estado. Lo que queda
   abierto (si una partida es de verdad dos familias) es materia de mesa y
   se deja escrito como tal, no como medicion pendiente.

Todo lo escrito va en una seccion nueva AL FINAL de
docs/plan/RECOMPUTO_3388.md, sin reescribir nada anterior, mas la nota de
OP-I-01 puesta al dia.

====================================================================
VERIFICACIONES FIJAS
====================================================================
- Toda declaracion de que algo falta, no existe o no esta leido se
  comprueba contra el archivo que acabas de citar, antes de escribirla.
- TODA CIFRA DE COBERTURA O DE CONTEO QUE COPIES DE UN ACTA, DE UN ENCARGO
  O DE UNA NOTA VIEJA SE REMIDE CONTRA EL ARCHIVO ANTES DE ESCRIBIRLA,
  AUNQUE TE LA BAJE EL AUDITOR. Una adjudicacion se obedece; una cifra se
  remide.
- NUEVA, y nace de tu caida de esta vuelta: UNA CIFRA NO SE DA POR
  VERIFICADA PORQUE EL INSTRUMENTO LA REPRODUZCA. Reproducir el numero
  viejo prueba de donde salio, no que siga vigente. La busqueda termina
  cuando se agotan las fuentes, no cuando cuadra el numero.
- dataset/ no se toca ni un byte. No se ejecuta ninguna operacion. No se
  crea la rama pasada-unica. No se crean operaciones nuevas. No se leen
  pares nuevos de la cola.
- Marca tus discutibles al final del reporte, como siempre: son lo primero
  que releo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
