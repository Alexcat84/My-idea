# REPORTE DE LA VUELTA 177 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta177_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA.** El acta 176, punto 7.8, reancla el contador a la vuelta que de
> verdad corrio la bateria y no a la que la tenia encargada: **la 175 no fue una
> vuelta de bateria porque murio sin producir una linea**, la corrio la 176, y
> desde ella se cuentan los cinco. **La proxima vuelta de bateria es la 181, no
> la 180.** Por eso la seccion 9 de este reporte cierra con el **HUECO DECLARADO
> Y MEDIDO** por el carril de la TAREA 1.b de la 173, con su medicion, su
> atribucion y su corrida. Un hueco declarado no es un hueco escondido.
>
> **EL TOPE DE ESTA VUELTA SIGUE EN DOS** (`AUDITOR.md` 6.2, regimen temporal
> vigente hasta que DOS vueltas seguidas cierren su propio reporte con
> `cerrar_reporte.py`), y el encargo trae exactamente dos. **LA 176 ES LA PRIMERA
> DE LAS DOS SEGUIDAS**, medido y no supuesto: cerro su reporte y lo archivo en su
> misma vuelta. **Si esta cierra el suyo, el tope vuelve a CINCO por la propia
> letra de la 6.2, sin que nadie tenga que decidirlo.**
>
> **Y ESTA VUELTA SI CORRIO SU BLOQUE DE APERTURA ANTES DE SU PRIMERA
> OPERACION**, que es lo que la 176 no hizo. Su lectura (que la 6.1 sacaba el
> aparato de abrir y cerrar la vuelta) **quedo corregida en el acta 176 punto
> 7.1**: la 6.1 saca el TRABAJO DE PLAN, no el aparato; si lo sacara, sacaria
> tambien el reporte y la 6.1 y la 6.2 se contradirian. Ademas esta vuelta no es
> de bateria, asi que la duda ni se plantea.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas coinciden, porque la
> 176 escribio su reporte, lo cerro y lo archivo; el fichero corre LAS DOS
> igualmente y publica lo que salga de cada una, porque una guarda que solo se
> mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta177_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 176: `f3087229`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 176: LA VUELTA PAGO LA DEUDA DE LA 175 ENTERA Y TODO LO QUE PUBLICA REPRODUCE BAJO MI MANO SALVO UNA FRASE. Recomputo verificado: bateria 88 de 88 con su doble corrida, 0 repetidas, 0 ajenas, 0 de la nomina sin correr, y los seis nombres que mi conteo vio de mas NO EXISTEN COMO FICHERO, son literales de prueba del propio arnes. Salida unica 60197 bytes en disco y 60197 normalizado a LF, 995 lineas, sha256 2f86d9e075d4e5ce, y sus 903 lineas no vacias estan LAS 903 dentro de la seccion 9: no es un hueco declarado, es la corrida. Los 18 numeros de los nueve tramos calzan uno a uno, el reloj suma 31.9, y las cinco cuentas de veredicto dan ANCLA PERDIDA 0, NO REPRODUCIBLE 0, RUIDO 0, CASO DECLARADO 2, NO MORDIO 1. GATE 0 VERDE EN SU CICLO ENTERO Y EN SU ORDEN, CORRIDO POR MI: numstat 0 filas, motor 25/25, tsc exit 0, web 82 y 1040. MARCADOR 3388 CON A 551 B 72 C 5 D 2760, puestos de 1 a 3388, CERO HUECOS Y CERO DUPLICADOS. LA CABECERA NO LA LEI, LA COTEJE: corri el tallador y las 11 filas salen IDENTICAS, 0 distintas y 0 ausentes. 13 commits en su orden, 39 rutas, y el grafo con 0 filas entre los dos sellos. LAS 55 RUTAS DEL REPORTE EXISTEN Y NINGUNA MIDE CERO BYTES. MI UNICA CAIDA CONTRA EL EJECUTOR ES DE REPORTE Y NO ACUMULA: el "diff del clon declarado sale VACIO" NO sale vacio, y lo medi hasta el fondo antes de acusar, porque el fondo le da la razon: de las 33 lineas de maquina que difieren, SENTENCIAS DE CODIGO 0 y LITERALES DE TEXTO 33, y en vuelta176_cierre.py la maquina sale VACIA de verdad. Vive en prosa del cuerpo, luego por la letra del 27 ago se registra y no acumula, y NO la meto en la cuarta sede de cifra publicada porque estirar cifra y ruta hasta un resultado de diff seria legislar, que es parada y no adjudicacion. LAS DOS RACHAS EN CERO Y LA ESCALADA NO SE DISPARA. CIEGA 7 DE 8, AISLADA DE UN SOLO TIRO ANTES DE GATE 0, DE LA VARA, DE LOS ARNESES Y DEL RECOMPUTO, Y EL QUE FALLO LO FALLE YO: el 491 lo di por gemelo leyendo el titulo cuando la prueba estaba en los pasos que tenia delante, la excepcion de rondas en uno y el term sheet en el otro. El archivo no fallo ninguna de las ocho. SIETE ADJUDICACIONES, TODAS CITANDO REGLA ESCRITA, y la mas gorda es la P.1: el arnes del rojo SE RE-COMPUTA EL ESPERADO, no se pasa a caso declarado ni se poda de la nomina. Le doy la razon al ejecutor en el D.6 y la culpa de la ambiguedad es mia, y reescribo la letra (f) en el encargo. La cadencia queda adjudicada: la proxima bateria es la 181, no la 180, porque la 175 no fue una vuelta de bateria, murio sin producir una linea. NO HAY PARADA: no escribo PARA_ALEXIS.md y el encargo de la 177 va completo, con dos sub-tareas, el remedio del rojo bloqueante y OP-L-03 desaplazada despues de siete vueltas.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V177_HEAD_APERTURA.txt`: `f3087229`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `1d18aa04`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **176**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 177`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
21 celdas no se pudieron leer"** y de esas lineas de rojo, **2
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE. Siete letras: (a) dejar constancia de la lectura del acta 176 nombrando sus adjudicaciones; (b) EL ARNES DEL ROJO, que es lo primero que se arregla, computando el esperado de la misma fuente viva en vez del `3` tecleado de la linea 175, SIN pasarlo a caso declarado, SIN re-anclarlo a sujeto congelado y SIN podar la nomina, con su caso positivo por mutacion que pruebe que el arnes SIGUE MORDIENDO; (c) la correccion declarada de la caida de reporte 1 del acta 176, el `diff` del clon que se publico como vacio y no lo es, en los DOS docstrings y sin borrar de que iban; (d) `scripts/loop/cotejar_clon_declarado.py`, el instrumento de nombre estable que hace innecesaria esa correccion a mano, con TRES veredictos separados y la clasificacion de SENTENCIAS DE CODIGO contra LITERALES DE TEXTO; (e) las dos correcciones chicas del acta, la salida del lanzador fuera de `docs/loop/` (`D.5`) y el tallador sellando su propio rechazo; (f) `D.3` y `P.3`, el tope de tramo POR MINUTOS computado del reloj medido dentro de `reparto_en_tramos()`, para que la 181 no lo decida a ojo; (g) contar en voz alta lo que NO entra en esta vuelta | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | `OP-L-03`, QUE LLEVA SIETE VUELTAS APLAZADA Y SE DESAPLAZA AQUI. La vara de hoy la sigue dando en LISTA sin ninguna prueba de ejecucion. Leer los ACTOS GRANDES primero, que es donde la lectura por acto cambia algo: el de SEIS miembros y los cuatro de CINCO. El criterio es `P.5` del banco del plan y se CITA, no se parafrasea: cada acto que vaya a fundirse se lee ENTERO despues de su destejido y antes de su fusion, y la decision es POR ACTO y no por pareja. Cada lectura se registra en JSONL y no se narra en prosa; ningun veredicto se mueve sin correccion declarada y recomputo; las 55 lecturas marcadas LECTURA DIRIGIDA no entran en la cola ni mueven su marcador; y el campo `estado` de la ficha NO SE TOCA aunque la operacion termine, porque la vara es `vuelta150_3_relectura_expediente.py` por decision del fundador del 4 sep 2026 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
