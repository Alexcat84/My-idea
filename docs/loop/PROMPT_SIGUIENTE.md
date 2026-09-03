Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), en REGIMEN COMPLETO, con las
guardas obligatorias por operacion.

TU VUELTA ES LA 162. El acta que te abre es la 161. Va en la cabecera fija
por la adjudicacion 6.1 del acta 158, y no es cosmetico: las dos guardas
del cierre (tallar_cabecera_reporte.py y verificar_apertura_sellada.py)
localizan la apertura buscando el acta de la vuelta N menos 1, y el
invariante de la casa es ACTA N, VUELTA N MAS 1. Tus ficheros de esta
vuelta se llaman SALIDA_V162_*.

HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA: NINGUNO. No hay commit de
decision del fundador que admitir. Todo commit dentro del corredor es tuyo
y cuenta como intruso.

Y EL SELLO DE APERTURA VA EN EL PRIMER COMMIT DEL CORREDOR, NO EN EL
CIERRE. En la 161 lo hiciste bien: los diez SALIDA_V161_*_APERTURA.txt
nacieron todos en 4208b8fa, y lo verifique yo corriendo la guarda.
Repitelo igual.

LO PRIMERO, PORQUE TE AHORRA TRABAJO: LAS TRES COSAS QUE TRAJISTE SIN
ARREGLAR ESTAN ADJUDICADAS EN EL ACTA 161 Y NINGUNA SUBE AL FUNDADOR.
(1) Las dos paradas de frontera NO ERAN PARADA: 049 y 098 se quedan en C
por la adjudicacion 6.1, y el motivo es que el ejemplar 100 no excluye por
consumo sino por una direccion que falla, y su propia razon declara LIMPIA
la direccion que tu creias excluida. Hiciste bien en no tocarlas y traerlas.
(2) El rojo de OP-D-02 es DE LA VARA y lo dice tu propia ficha (6.4).
(3) La puerta del corredor queda ensanchada por la adjudicacion 6.5. Las
tres se ejecutan aqui abajo. LA VARA P.5.1 SIGUE CONGELADA Y NADIE LA
TOCA: ninguna vuelta la estrecha ni la ensancha sin correccion declarada
del fundador.

- TAREA 1, LOS REGISTROS, Y LLEVA DENTRO UNA CAIDA TUYA QUE HAY QUE
  CORREGIR ANTES DE ESCRIBIR NADA MAS.
  (1.a) LA R.29 QUE ESCRIBISTE YA EXISTIA, Y ES LA CAIDA DE LA VUELTA 161
  (acta 161, seccion 5.1). R.29 esta asignada desde la vuelta 150 y vive
  en docs/plan/CORRECCIONES_A_APLICAR.md:2127; y la prueba estaba en el
  mismo fichero que abriste, docs/PENDIENTES.md:10389, que dice literal
  que R.29 NO esta en esa pagina y que su fuente unica es la otra. Hoy
  docs/PENDIENTES.md se contradice a si mismo con 76 lineas de distancia.
  LA ENTRADA PASA A R.30 POR CORRECCION DECLARADA, sin borrar una sola
  linea: el titulo viejo queda TACHADO Y LEGIBLE con su motivo delante.
  Y ANTES DE ESCRIBIR, LA SERIE SE RECOMPUTA CON INSTRUMENTO DE LOS DOS
  FICHEROS (docs/PENDIENTES.md y docs/plan/CORRECCIONES_A_APLICAR.md),
  imprimiendo la serie entera con su sede fichero por fichero: la serie
  R.N es GLOBAL a los dos, y lo prueba la propia remision. EL NUMERO NO
  SE TECLEA NUNCA MAS, que es exactamente lo que fallo: tu instrumento
  llevaba "con la ultima escrita siendo R.28" escrito a mano y su
  idempotencia solo miraba un fichero. Arregla eso EN LA FUENTE, con
  CASO POSITIVO POR MUTACION sobre variable computada (mete una R.31 de
  mentira en el OTRO fichero y el instrumento tiene que verla).
  (1.b) LAS ADJUDICACIONES 6.1 A 6.8 DEL ACTA 161, registradas en la
  forma de la casa, en la sede que la serie recomputada diga.
  (1.c) LAS MARCAS DE MI CIEGA, EN EL REGISTRO, POR LA ADJUDICACION 6.7.
  Relei a ciegas las CATORCE en C (005, 038, 049, 052, 068, 081, 084,
  087, 088, 095, 098, 109, 110, 116) mas los dos ejemplares de exclusion
  (100 y 122), 16 de 16 coincidiendo, y esas lecturas hoy NO DEJAN MARCA
  CONTABLE, que es justo lo que P.5.2 denuncia. Escribe tu la marca por
  adicion en el campo razon de esas 16 filas, con la forma que P.5.2
  exige (que es RELECTURA y EN QUE VUELTA), citando la seccion 3 del acta
  161 y mi sello sha1 ffe1fa6f. No cambies ni una clase: las 16
  coinciden con la vigente. Y despues RECOMPUTA la cifra de P.5.2 y
  anadela debajo con su corte, sin borrar ni la de apertura ni la de
  cierre de la 161.

- TAREA 2, LAS DOS GUARDAS QUE EL ROJO DEJO ABIERTAS. ES BLOQUEANTE: LA
  APERTURA DE ESTA VUELTA NO SE DA POR BUENA HASTA QUE LA 2.a ESTE VERDE.
  (2.a) LA PUERTA DEL CORREDOR DESPUES DE UNA PARADA (adjudicacion 6.5
  del acta 161, que es MIA y por eso la ensancho yo). En
  verificar_apertura_sellada.py: CUANDO, Y SOLO CUANDO, el commit del
  acta trae docs/loop/PROMPT_SIGUIENTE.md VACIO y docs/loop/PARA_ALEXIS.md
  escrito (la firma de una parada, que tu no puedes fabricar porque el
  acta es mia), el encargo se lee del PRIMER commit posterior al acta que
  escriba PROMPT_SIGUIENTE.md. EL MECANISMO DEL ROTULO NO CAMBIA EN NADA:
  sin el literal HASHES ADMITIDOS EN EL CORREDOR DE ESTA VUELTA: no entra
  nada, y un hash citado de paso sigue sin entrar. SI HUBIERA MAS DE UN
  COMMIT ASI, ROJO. Con CASO POSITIVO POR MUTACION sobre encargo
  fabricado en memoria (la funcion ya es pura a proposito), y con la
  prueba de que NINGUN VEREDICTO VIEJO SE MUEVE: corre la guarda vieja
  contra la nueva sobre las vueltas 156, 158, 159 y 160 y coteja. Al
  terminar, verificar_apertura_sellada.py --vuelta 161 TIENE QUE DAR
  VERDE, y --vuelta 162 tambien.
  (2.b) LA VARA DE LOS DESTEJIDOS Y OP-D-02 (adjudicacion 6.4). El
  tallador toma como absorbidos todo el campo nodos menos el
  superviviente, y la ficha de OP-D-02 dice con sus palabras que
  homework_frontend_loading y voice_of_customer_homework NO ENTRAN EN LA
  FUSION y que el campo nodos NO es la lista de lo que se funde. LA VARA
  ES MAS ANCHA QUE LA FICHA. Se arregla con TABLA DE EXCEPCIONES QUE CITA
  SU ADJUDICACION, que es el patron que la casa ya usa en la lista blanca
  de OP-C-05 (cada entrada cita su lectura): una excepcion sin cita es un
  agujero. CASO POSITIVO POR MUTACION: una operacion cuyos absorbidos de
  verdad esten pendientes TIENE que seguir saliendo roja, y si pasa, la
  excepcion esta abierta de mas. Recomputa la fase 02 despues y publica
  las dos cifras, antes y despues, sin borrar la de antes.

- TAREA 3, LA GUARDA QUE SE QUEDO CIEGA Y SIGUE DANDO VERDE (adjudicacion
  6.6, acta 161 seccion 5.2). verificar_cifras_del_reporte.py cotejo
  CINCO afirmaciones de cierre sobre el reporte de la vuelta 160 y CERO
  sobre el tuyo, y salio VERDE las dos veces: tus ocho cifras de fase se
  mudaron de la prosa a una tabla y la guarda dejo de verlas. Esta medido
  y se reproduce con git show aa6bb622:docs/loop/REPORTE.md. NO SE AFLOJA
  NADA Y NO SE PROHIBE LA TABLA: la guarda tiene que cotejar tambien las
  afirmaciones de cierre que vivan en una FILA DE TABLA, y lo que no
  pueda cotejar lo tiene que DECIR con su cifra en un AVISO visible, que
  es la regla de fallar ruidoso del banco 9. VARA DE ACEPTACION, y es
  dura: sobre tu reporte de la 161 tiene que cotejar las OCHO filas de
  fase del cierre, sobre el de la 160 tiene que SEGUIR DANDO 5, y ningun
  veredicto viejo puede moverse. Con su caso por mutacion.

- TAREA 4, UNA MEDICION QUE NO ARREGLA NADA Y SE DECLARA (acta 161,
  seccion 5.3). Hay UN par de nodos vivos con el mismo titulo normalizado,
  sistema_responsabilidad_gerencial y sistema_responsabilidad_gerencial_2,
  y el Gate 0 no se equivoca al decir cero duplicadas porque su vara es el
  titulo EXACTO. Mide el universo entero de colisiones de titulo
  NORMALIZADO entre vivos, publica la nomina con su cifra, y PARA AHI:
  NO FUNDAS NADA Y NO PROPONGAS FUSION, que eso es alcance de campaña y
  es del fundador. Es una medicion, no una operacion.

- TAREA 5, SEGUIR EL ORDEN ESCRITO EN MODO CONTINUO, hasta el MURO
  CONOCIDO Y YA ADJUDICADO (acta 149, seccion 3.10): la fase 08 NO CIERRA
  sin una SESION CON CREDENCIAL Y CON EL FUNDADOR DELANTE, porque el .env
  esta fuera del repo mientras el bucle corre y eso esta bien. Lo corri yo
  hoy y da exit 2. Al llegar ahi SE PARA Y SE DICE. EL MERGE NO SE PIDE NI
  SE HACE: es del fundador y solo suyo, ni ahora ni al final.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
