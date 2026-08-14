Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA, rama `bucle`. **FASE II, SEGUNDA VUELTA: EL PLAN SE REESCRIBE AL CORTE 3.388.**
MODO DE CIERRE: cero reparaciones de nodos. **`dataset/` NO SE TOCA NI UN BYTE.** Esta vuelta
sigue midiendo y registrando: la Fase III (mover nodos) va en la rama `pasada-unica` y todavia
no se abre.

ESTADO DEL CREDITO, leelo primero. **EL RECOMPUTO ESTA VERIFICADO ENTERO CON INSTRUMENTO
INDEPENDIENTE.** No use tu script: escribi el mio (resolutor desde `ids_alias`, componentes
conexas, criterio doble de `OP-U-01`) y sale identico. 391 alias; 583 A crudas y 583 pares
tras resolver, cero auto aristas; 854 nodos y 335 componentes con tu misma distribucion;
CERRADOS 280 sobre 600 y ABIERTOS 55 sobre 254 con tus mismos tamanos; las cuatro
comprobaciones dan lo mismo. **Y la prueba mas dura que ninguna de las cuatro: compare mis 335
componentes contra tu `RECOMPUTO_3388_COMPONENTES.jsonl` COMO CONJUNTOS DE CONJUNTOS, y son el
mismo conjunto, cero de un lado y cero del otro.** Tambien recompute `OP-E-03` sin correr tu
script: la tabla sale celda por celda igual y 477 = 2 + 88 + 387. Marcador, huecos, duplicados
y las dos correcciones de razon: verificados, dos lineas cambiadas y ninguna clase movida.

**TRES COSAS QUE HICISTE BIEN Y QUEDAN ESCRITAS CON TU NOMBRE:**
a) **Verificaste mi correccion antes de aplicarla y me corregiste a mi.** Los hubs de siete
   toques de `risk_management` son CINCO, no cuatro: lo conte yo mismo sobre los 106 pares y
   la distribucion no deja lugar a duda, y **no hay un sexto**. La cadena de listas cortadas
   cierra ahi. Yo corte una lista en un valor dejando fuera un empate, que es exactamente lo
   que le habia reprochado a tu vuelta 10.
b) **Declaraste el paso 2 NO CORRIDO en vez de reconstruir una nomina de memoria.** Es la
   conducta correcta y por eso el paso se puede rescatar hoy (ver TAREA 2.B).
c) **Publicaste el 387 sin forzar la baja que mi encargo te habia anunciado.** Hiciste bien: la
   baja era imposible y el error era mio (ver mi acta, seccion 2.c).

**DOS COSAS QUE DECLARASTE IMPOSIBLES Y SI SE PODIAN MEDIR. Las medi yo y hay que registrarlas:**
1. **El 401 contra 400 A vigentes al 2.117 esta RESUELTO PAR POR PAR.** El repo guarda el
   archivo al corte exacto (`c16a24f5`, 11 ago 2026, 2.117 lineas). Comparado clase a clase
   contra hoy en ese tramo, **cambio UNA sola clase: el puesto 2.078** (`elaboracion_fdd`
   contra `preparar_fdd`, `franquicias`), **D el 11 ago y A hoy por correccion posterior
   declarada**. El archivo viejo tiene exactamente 400 A. **No hay descuadre: hay una
   correccion declarada, y cada cifra es correcta en su corte.**
2. **El mapeo de los 48 actos abiertos SI se puede hacer 1 a 1**, porque la cola
   `docs/INTRA_DOMINIO_PARES.jsonl` **esta completa en 3.388 pares desde el 9 ago 2026**
   (`c442345a`) y no se ha tocado, asi que la medicion vieja se vuelve a correr sobre el mismo
   archivo con el corte viejo. Corriendola al 2.117 **excluyendo la correccion posterior del
   2.078** reproduzco la cifra publicada EXACTA: 221 componentes sobre 576 nodos, 173 cerrados
   sobre 371 (149 de dos, 23 de tres, uno de cuatro), 48 abiertos sobre 205, motivos 42 mas 6.
   **Y con esa membresia: de los 48 abiertos, CINCO CERRARON, 42 siguen abiertos identicos y
   UNO crecio sin cerrar. Ademas 114 actos de hoy no tienen ni un nodo de un acto del 2.117, y
   de esos 102 nacieron cerrados y 12 abiertos.** Las cuentas cierran: 173 + 5 + 102 = 280 y
   43 + 12 = 55. **Tu proxy de edad (221 / 1 / 113, con 101 y 12) difiere en una unidad y la
   unidad es el mismo 2.078**: su arista es vieja, pero en el corte viejo ese par era D.

**VERIFICACION FIJA NUEVA, y nace de lo de arriba:** junto a la de discutibles y a la de las
fracciones (que cumpliste, y las tres se quedan), **toda declaracion de "no se puede medir" o
"no se puede saber" lleva al lado EL INTENTO QUE SI CORRISTE y por que no alcanzo.** Dos de tus
tres declaraciones de esta vuelta se podian medir con lo que ya estaba en el repo.

====================================================================
TAREA 1: registros, ninguno toca el marcador ni una sola clase
====================================================================
1. **En `docs/plan/RECOMPUTO_3388.md`, con CORRECCION DECLARADA y sin borrar el texto viejo
   (tachado), cierra las dos preguntas de arriba:**
   a) la del 401 contra 400, con el hash `c16a24f5`, el puesto 2.078 nombrado y la frase de que
      cada cifra es correcta en su corte (banco 9.21);
   b) la de los 48, sustituyendo el "no se puede decir con certeza" por **las cifras medidas
      (5 cerraron, 42 identicos abiertos, 1 crecio; 114 nuevos, 102 nacidos cerrados y 12
      abiertos)**, con el metodo escrito (re correr la medicion vieja al corte viejo excluyendo
      la correccion del 2.078) y **con la condicion que lo hace valido declarada al lado: la
      cola esta completa en 3.388 desde `c442345a`**. **VERIFICALO TU con tu propio instrumento
      antes de escribirlo; si tu cuenta no da lo mismo que la mia, NO la escribas: dilo y
      traelo.**
   c) la del 387 que no bajo: anade la razon decisiva (el script compara contra la UNION de
      `INTRA_DOMINIO_PARES.jsonl` mas `INTRA_DOMINIO_VEREDICTOS.jsonl`, y la primera esta
      completa desde el 9 ago), **dejando escrito que la expectativa de baja fue un error del
      auditor, no tuyo.**
2. **Registra en `docs/INTRA_DOMINIO_INFORME.md` (seccion 101.e, nueva) mi adjudicacion de la
   relectura:** cuando el acto de quince de `health_safety` se ejecute, **el superviviente
   conserva el CONTRASTE DE SEIS EJES de `vieja_vision_vs_nueva_vision_seguridad`** (personas
   como problema o recurso, actitudes o condiciones, ausencia de eventos o presencia de
   capacidades, staff o linea, reglas o contexto, hacer imposible el error o dar espacio para
   hacer lo correcto). Ese nodo repite cuatro veces contra cuatro supervivientes distintos y
   muere en todas; su tabla es catalogo. **Misma regla que la 101.c: una fusion que se lleve
   solo un lado es perdida de catalogo no declarada.**
3. **LO VERIFICADO Y EN VERDE, no lo reabras:** el marcador entero al 3.388 y las diez tasas;
   el retrato de las A; las 335 componentes y sus miembros; los 280 CERRADOS y los 55 ABIERTOS;
   las cuatro comprobaciones; la tabla entera de `OP-E-03` con su aritmetica; los cinco hubs de
   siete toques; los once de once que citan el entregable. Siguen aprobados
   `scripts/recomputar_marcador.py`, `scripts/_registrar_lote.py`, `scripts/volcar_pares.py`,
   `scripts/corregir_veredicto.py`, `scripts/plan/recomputo_3388.py` y
   `scripts/plan/diferencia_contra_cola.py`.

====================================================================
TAREA 2.A: EL PLAN SE REESCRIBE AL CORTE 3.388 (autorizado: las cuatro
comprobaciones estan verificadas por el auditor)
====================================================================
**Ahora si se edita `docs/plan/OPERACIONES.jsonl`**, y solo lo que esta aqui:
1. **`OP-U-02` pasa de DECISION PENDIENTE a LISTA**, con `fecha_corte` 2026-08-13 y su
   evidencia reescrita con las cifras del recomputo (335 actos, 280 cerrados sobre 600 nodos,
   55 abiertos sobre 254), **conservando la linea vieja del corte 2.117 con su fecha**, no
   borrandola (banco 9.21).
2. **`OP-U-01`**: reescribe sus cifras al corte 3.388 (los cerrados pasan de 173 sobre 371 a
   280 sobre 600; el desglose por tamano 2: 244, 3: 32, 4: 4), **con la cifra vieja y su corte
   al lado**, y anade en la nota **cuales de los 48 cerraron (los cinco)**. La verificacion
   "NINGUN acto de la lista de abiertos se ejecuta antes del recomputo" se actualiza a la lista
   nueva de 55.
3. **`OP-L-02`, las cinco mesas (`OP-M-01` a `OP-M-05` y sus sub operaciones) y las seis
   `OP-D-01` a `OP-D-06`**: para CADA UNA, comprueba si alguna cifra suya cambia con el corte
   nuevo. **Si cambia, la reescribes con los dos cortes; si NO cambia, lo dices explicitamente
   en el reporte con la cifra que verificaste.** No basta con dejarlas quietas: la regla es que
   **ninguna cifra publicada queda sin recomputar con su corte nuevo**, y una cifra que se
   confirma igual tambien es un resultado.
4. **CADA edicion lleva su comando al lado en el reporte.** Y al terminar, **una comprobacion de
   integridad del propio archivo**: 69 operaciones antes y 69 despues, ningun `id_op` duplicado,
   ningun `depende_de` apuntando a un id que no existe. Escribela con su cifra.
5. **NO se ejecuta ninguna operacion. NO se toca `dataset/`. NO se crea la rama `pasada-unica`.**

====================================================================
TAREA 2.B: EL PASO 2 DEL RECOMPUTO, POR LA VIA ACOTADA (adjudicacion
del auditor: se puede correr sin inventar nomina)
====================================================================
**Tu busqueda de la nomina fue correcta pero se quedo en los `.md`. El instrumento dejo su
propia salida: `docs/COSTURAS_INTERNAS.jsonl`, 128 filas con `node_id`, `dominio`, `pasos`,
`corte`, `disparo_bloque` y `disparo_pareja`. NO trae el veredicto, por eso la nomina de las 46
confirmadas no esta como dato. Pero el paso 2 no necesita la nomina entera: solo necesita saber
que citas caen dentro del retrato de las A.**

1. **Cruza las 128 citas (resolviendo por alias, P.1) contra los 854 nodos con al menos una A.**
   **Medido por mi: la interseccion es de TREINTA Y SEIS nodos.** Publica tu cuenta; si no te da
   36, para y dilo antes de seguir.
2. **Para esos treinta y seis, y solo esos, busca el veredicto YA ESCRITO** en
   `docs/FICHA_SUBFUSION_GRADIENTE.md` y `docs/COSTURAS_INTERNAS_RESUMEN.md`. **Cita archivo y
   linea de cada veredicto que encuentres.** El que no tenga veredicto escrito se declara **SIN
   VEREDICTO ESCRITO** y **NO SE ADIVINA NI SE DEDUCE DEL TEXTO DEL NODO**: leer el nodo para
   decidir si tiene costura es reabrir el otro eje, y eso no es esta campana.
3. **Los que salgan CONFIRMADA son las CURAS ACOPLADAS**: destejido y fusion en el mismo acto,
   por el toque unico del banco 9.4. **La ficha ya tiene siete ejemplares escritos de esta misma
   pregunta** (la serie SANO POR DENTRO, GEMELO POR FUERA y LA CURA ACOPLADA): empieza por
   comprobar cuales de tus resultados ya estan ahi y cuales son nuevos. **Un ejemplar que ya
   este escrito no se reescribe: se cita.**
4. **Publica el resultado en `docs/plan/RECOMPUTO_3388.md`, en el hueco del paso 2**, con la
   correccion declarada de que el paso pasa de NO CORRIDO a corrido por la via acotada, y con
   **la fraccion al lado** (cuantos de los 36 tienen veredicto escrito, cuantos CONFIRMADA,
   cuantos FALSA, cuantos sin veredicto).

**Si el presupuesto no alcanza para la TAREA 2.B completa, NO LA CORRAS A MEDIAS: dejala sin
correr y declaralo con esa frase.** La TAREA 2.A tiene prioridad sobre la 2.B.

LO QUE NO ENTRA EN ESTA VUELTA, para que no lo adelantes: el lote de cinco lecturas del sales
roadmap, la cola de relectura post fusion, el criterio del forastero, las lecturas de acto
entero de P.5, y las 387 filas de LECTURAS DIRIGIDAS. **Cada una tiene su encargo y su orden.**
Si terminas con presupuesto de sobra, gastalo **midiendo, sin escribir nada en el plan, cuantas
de las 55 componentes ABIERTAS lo estan por pares que nunca entraron a la cola y cuantas por
otra razon**, y declara la cuenta: eso alimenta el encargo siguiente.

REPORTE en `docs/loop/REPORTE.md`, que reescribes entero: hash y rutas, la TAREA 1 con sus tres
correcciones declaradas, la TAREA 2.A operacion por operacion (incluidas las que NO cambiaron,
con su cifra confirmada) y su comprobacion de integridad, la TAREA 2.B con sus fracciones, y
**la lista explicita de lo que NO mediste, cada linea con el intento que si corriste al lado**.
Los hallazgos que no puedan esperar, al mensaje del commit. Commitea por bloques para no perder
trabajo si la sesion se corta.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
