# REPORTE DE LA VUELTA 178 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta178_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA Y RECONFIRMADA.** El acta 176, punto 7.8, reanclo el contador a la
> vuelta que de verdad corrio la bateria y no a la que la tenia encargada, y el
> encargo de esta vuelta lo repite con todas las letras: **la proxima vuelta de
> bateria es la 181**, y la 178, la 179 y la 180 cierran su seccion 9 con el
> **HUECO DECLARADO Y MEDIDO**, con su nombre, sus bytes medidos y su atribucion,
> las tres juntas. Un hueco declarado no es un hueco escondido.
>
> **EL TOPE VUELVE A CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA VUELTA
> ANTERIOR.** `AUDITOR.md` 6.2 dice que el regimen temporal de dos sub-tareas
> dura **hasta que DOS vueltas seguidas cierren su propio reporte** con
> `cerrar_reporte.py`. **La 176 y la 177 lo hicieron, cada una en su misma
> vuelta, y las dos archivaron ademas su reporte sin esperar a la siguiente.**
> El tope vuelve a CINCO por la propia letra de la 6.2, sin que nadie tenga que
> decidirlo, y este encargo trae cinco. **El regimen temporal queda CUMPLIDO Y
> CITABLE, no borrado**, y los cuatro commits que lo cumplen se localizan EN GIT
> en el bloque B.1 de `scripts/loop/vuelta178_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, QUE ES LA CAIDA
> PROPIA QUE LA 177 SE ANOTO.** El remedio quedo cableado en
> `vuelta177_apertura.py` y aqui se estrena de verdad: el medidor corre dentro
> del bloque de apertura, antes de la primera operacion. **Desde esta vuelta, una
> columna de apertura medida al cierre es caida que ACUMULA**, y eso lo dice el
> encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas coinciden, porque la
> 177 escribio su reporte, lo cerro y lo archivo; el fichero corre LAS DOS
> igualmente y publica lo que salga de cada una, porque una guarda que solo se
> mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta178_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 177: `77621a68`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 177: LAS DOS TAREAS ENTERAS Y TODO LO QUE PUBLICA REPRODUCE BAJO MI MANO SALVO UNA FRASE, Y EL TOPE VUELVE A CINCO PORQUE LA VUELTA LO DISPARO.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V178_HEAD_APERTURA.txt`: `77621a68`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `531efee1`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **177**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 178`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE. Cinco letras: (a) LA RELECTURA AL DOBLE DEL TRAMO DE LA CAIDA de conteo del acta 177, la cuenta de la nomina y del censo, publicada ENTERA en tabla y con la resta comprobada, porque una cuenta que no cierra consigo misma se caza sola si alguien la escribe entera; (b) `arneses_que_faltan()` SE ARREGLA en la funcion y no en la llamada, con la vara del censo EXPLICITA y con su motivo, sin podar la nomina, y con el caso positivo por mutacion que hoy CAE con la funcion vieja: dos arneses de la MISMA vuelta que la ultima de la nomina, uno dentro y otro fuera, y la funcion tiene que VER al de fuera; (c) EL CUARTO VEREDICTO de `cotejar_clon_declarado.py`, EL ARBOL DE SINTAXIS, sin tocar la clasificacion vieja, en rojo si un fichero no parsea, y con el caso que lo decide todo: dos ficheros que solo difieren en una coma final dan maquina DIFIERE y AST IDENTICO; (d) EL `--puestos` Y EL `--excluir` DEL AISLADOR DE CIEGA, componibles con los selectores que ya tiene, en rojo si un puesto pedido no existe, con la guarda de fuga intacta, y borrando despues la muleta `_auditor_v178_ciega.py` por `P.16`; (e) LAS DOS DE HIGIENE: que `cerrar_reporte.py` CAIGA EN ROJO si el reporte publica una cifra de bytes o un sha sin su pareja, y LA GUARDA DEL SUJETO CONGELADO, que lleva desde la vuelta 145 siendo una frase y no un instrumento | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | `OP-L-03`: SE RE-MIDE EL BACKLOG ENTERO ANTES DE LEER UN ACTO MAS. No se toca `backlog_l03_vuelta14.py`, que sostiene una cifra adjudicada en la vuelta 15; se escribe el filtro DELANTE, en `scripts/loop/backlog_l03_resuelto.py`, de nombre estable y sin numero de vuelta, que corre el instrumento viejo y le pasa el resolutor de `P.1` por encima publicando LAS DOS COLUMNAS AL LADO. Por acto y en total: miembros escritos, vivos por el resolutor, vivos por el campo `deprecado` del grafo, SI LOS DOS CAMINOS CALZAN, pares que el instrumento da, pares reales y pares disueltos. CAE EN ROJO si los dos caminos no calzan en algun acto, nombrandolo. Con su caso positivo por mutacion sobre un mapa de alias FABRICADO. Y publica la cifra que la 177 no pudo publicar: cuanto sobra en los 34 actos que no miro. EL ESTADO DE LA FICHA NO SE TOCA | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LOS CINCO TRIANGULOS `A` MAS `A` MAS `D`: SE ANOTAN CON SU REGLA, NO SE MUEVEN. La `P.3` de la 177 queda adjudicada como COSA JUZGADA en el acta 177 punto 7.9: las dos reglas que lo deciden ya estan escritas y RESULTAN COMPATIBLES. La `9.6.1` del banco dice que un nodo que es un paso de otro y NO TRAE PROCEDIMIENTO PROPIO, REPITE; la correccion declarada del 13 ago 2026 sobre los puestos 530 y 863 dice que la madre y su pieza de arenas se separan. La condicion que las concilia es la que la propia `9.6.1` escribe: SI LA PIEZA TRAE PROCEDIMIENTO PROPIO SE SEPARA, SI ES EL PASO DICHO OTRA VEZ, REPITE. Por cada uno de los cinco se anota EN EL JSONL cual de las dos reglas gobierna cada lado y CON QUE PRUEBA. CERO VEREDICTOS MOVIDOS | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA CEGUERA DE LA VARA, QUE LLEVA DOS VUELTAS CONTADA. `vuelta150_3_relectura_expediente.py` imprime SEIS fichas en LISTA sin prueba y dos de las seis estan CONSUMIDAS por otras, asi que el trabajo real son CUATRO. La vara es del fundador y su veredicto NO SE TOCA: lo que se anade es una COLUMNA, no una exclusion. Que siga imprimiendo las seis y que diga de cada una si esta CONSUMIDA por otra ficha y por cual. La cuenta final publica LAS DOS, nunca solo el cuatro. Con su caso positivo por mutacion sobre un expediente fabricado | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA COMO SIEMPRE: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`; la guarda que falta en la dependencia del `D.4` de la 174; y la medicion del grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes. Ninguna de las cuatro se toca aqui, y las cuatro se nombran para que no se caigan | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
