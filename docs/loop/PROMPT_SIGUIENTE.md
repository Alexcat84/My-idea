Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3): corre las fases seguidas sin
esperar acta, con las guardas obligatorias por operacion. dataset/ SI
se toca en esta fase, porque el texto de cada operacion lo ordena.
Cualquier guarda en rojo fuera de lo que 08_VERIFICACION.md declara
permitido, o cualquier operacion cuyo texto no alcance para ejecutarse
sin decidir, te detiene a ti y convoca al auditor.

EJECUTOR.md, regla 1, con sus tres renglones (LA CITA LLEVA SU LINEA;
EL ESTADO AL CIERRE SE MIDE AL CIERRE; LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION): mide la apertura de esta vuelta antes de tocar
nada, y remide cualquier cifra que tu propia vuelta pueda haber movido
antes de citarla en el cierre.

====================================================================
TAREA 1: registros
====================================================================
1. Corrige la fila de la tabla de costuras de docs/plan/08_VERIFICACION.md
   que dice "investigar y conexion_personal_emocional" (caida de cifra
   publicada contada en el acta de la vuelta 31, seccion 3): el id
   investigar NO existe en el grafo. El destino real de esa fila es
   conexion_personal_emocional a secas (un solo destino, no dos); la
   otra mitad del bloque partido ya tiene su propia fila bajo
   investigar_datos_cliente. Correccion declarada, con el texto viejo
   de la fila delante y tachado, no borrado.
2. Registra en la nota de OP-D-02 (docs/plan/OPERACIONES.jsonl) que la
   operacion queda readjudicada: su paso 1 (destejer voz_del_cliente_voc
   separando Cooper de Coleman) ya lo hizo OP-F-04-COL en la vuelta 31.
   Lo que le queda a la operacion es la fusion con enfoque_mercado_voc
   y las relecturas de los congelados 724, 755 y 827. Correccion
   declarada, texto viejo delante.
3. Cita, sin reescribirlas, las correcciones que este commit ya dejo
   hechas: la nomina de OP-F-04-HOR vuelve a 14 con
   principio_calidad_mvp reincorporado; el campo preservar de OP-D-01
   reescrito (preserva el objeto restante del nodo por lectura; el par
   494 se re-lee con la vara ordinaria sobre el nodo estable) y su nota
   corregida de Hugos a Horowitz; el registro de la pasada de forma
   unica para acentos en docs/plan/05_SANEO.md; y el registro de que
   HECHA no se estrena en docs/plan/00_INDICE.md.

====================================================================
TAREA 2: ejecutar en este orden, y seguir en modo continuo
====================================================================
1. Resuelve el 14vo de Horowitz DENTRO de OP-F-04-HOR, con sus guardas:
   el bloque de principio_calidad_mvp (pasos 6 a 10) por P.18 sobre la
   nomina de Horowitz vigente al dia, con P.19 disponible si la lectura
   da fundido con los pasos 1 a 5 (el objeto del MVP puede coincidir;
   decidelo con el texto delante, no de antemano). Si nace nodo propio,
   declaralo en INDICE_ROJO_DECLARADO.jsonl y corre el ciclo de Gate 0
   entero. Con este bloque resuelto, RE-CIERRA LA FASE 01: re-mide su
   saldo con el mismo instrumento de la vuelta 31 y confirma 14 de 14
   en OP-F-04-HOR.
2. Ejecuta OP-D-01 por su letra corregida: primero el destejido de
   producto_minimo_viable, despues el de principio_calidad_mvp (ya
   estable tras el paso 1 de esta tarea, sin segundo libro pendiente),
   y solo entonces decide si lo que queda se funde (par 494), leyendo
   el objeto restante del nodo con la vara ordinaria. Releé los
   congelados 592 y 830 contra el superviviente.
3. Ejecuta OP-D-02 por lo que le queda (la fusion con
   enfoque_mercado_voc y las relecturas 724, 755, 827), sin repetir el
   destejido que OP-F-04-COL ya hizo.
4. Con OP-D-01 y OP-D-02 hechas, SIGUE EN MODO CONTINUO el orden de la
   fase 02 (destejidos), con Gate 0 verde por el ciclo escrito y las
   suites en verde tras cada operacion, hasta que una guarda salga en
   rojo fuera de lo permitido o una operacion no alcance para
   ejecutarse sin decidir.

Las lecturas ya publicadas y verificadas (las diecisiete costuras de
OP-F-04-COL, los trece discutibles de la ciega del acta 31) NO se
rehacen: ejecuta sobre esa lectura.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
