# REPORTE DE LA VUELTA 176 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta176_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA ES OTRA VEZ UNA VUELTA DE BATERIA, Y NO ES UN CAMBIO DE CADENCIA: ES LA
> DEUDA DE LA 175, QUE NO SE PAGO** (`AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026). La bateria corre CADA CINCO, en una vuelta propia QUE NO LLEVA NADA
> MAS, y la vuelta propia que le tocaba se murio antes de producir una linea. Aqui
> no hay trabajo de plan al lado, y `OP-L-03` no se toca: lleva SEIS vueltas
> aplazada y se cuenta en voz alta. **EL TOPE DE ESTA VUELTA NO ES CINCO SINO DOS**
> (`AUDITOR.md` 6.2, regimen temporal vigente hasta que DOS vueltas seguidas
> cierren su propio reporte), y el encargo trae exactamente dos. **La 174 fue la
> primera de esas dos, la 175 no cerro, y la racha VUELVE A EMPEZAR: esta es otra
> vez la primera.**
>
> **LO QUE SE PARTE ES EL BOCADO, NO LA BATERIA.** La 175 murio DENTRO de la
> corrida, y la causa esta medida y no supuesta: 87 entradas, cada una corrida DOS
> VECES, son un bloque indivisible de entre 57 y 75 minutos. Partirla en tramos
> DENTRO de esta misma vuelta no toca ninguna de las cuatro cosas que la letra del
> fundador fija (cadencia, soledad, integridad y la prohibicion de podar la
> nomina). **La nomina sigue en 87 y sigue creciendo.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 175 si escribio su reporte (ABIERTO Y SIN CERRAR, que es texto igual) y es el
> que hay en el arbol; el fichero corre LAS DOS igualmente y publica lo que salga
> de cada una, porque una guarda que solo se mira cuando difiere no se puede
> auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta176_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 175: `e8638442`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 175: LA VUELTA MURIO DENTRO DE LA BATERIA Y ME DEJO EL CATALOGO MUTADO, PERO NO PUBLICO NI UNA CIFRA FALSA Y SU REPORTE DECLARA SUS DOS TAREAS ABIERTAS. EL ARBOL ME LLEGO CON UNA ARISTA BIDIRECCIONAL QUE NADIE LEYO METIDA EN dataset/: vuelta154_tarea2d_mutacion_guarda.py metio un alias deprecado en las dos listas de ab_testing_optimizacion, run_phase1 la simetrizo, y su restauracion no corrio porque vive en un finally y a un finally lo mata quien mate al proceso. LA RESTAURE YO con git checkout sobre los cuatro ficheros y NADA MAS, dejando intacto el trabajo bueno de la nomina, y Gate 0 verde detras lo prueba. Y NO ME LO CREI: corri el arnes culpable entero, 3 de 3, y su CASO A demuestra que OP-C-05 SI muerde y nombra el par, o sea que la arista no podia entrar callada. EL AGUJERO ESTA UN PASO ANTES Y ES EL QUE ENCARGO: la primera linea de todo encargo commitea lo pendiente, y con el arbol asi eso mete la mutacion en la historia. EL ACTA ABRE CON MI PROPIO REMEDIO BLOQUEANTE Y CORRIGIENDO A MI ACTA ANTERIOR, QUE APLAZO SU DISPARADOR UNA VUELTA DE MAS: la racha de teclear de memoria llego a tres EN LA 174, asi que el acta que abre con el remedio es esta, y comprobe las nueve rutas con os.path.exists antes de nombrar una sola. CIEGA 8 DE 8, SIN UNA DISCREPANCIA Y DE UN SOLO TIRO SIN RE-TIRAR, con el 84 y el 828 que eran mis dos trampas del acta 174 en las dos direcciones. GATE 0 VERDE EN SU CICLO ENTERO Y CORRIDO POR MI: numstat 0 filas, motor 25/25, tsc 0, web 82 y 1040; MARCADOR 3388 CON A 551 B 72 C 5 D 2760 Y CERO HUECOS; las siete cifras del reporte y de sus dos commits reproducen todas, y de las 6 rutas que nombra la unica que no existe NO ES CAIDA porque se anuncia en futuro dentro de una fila declarada ABIERTA. MI CAIDA DE HOY ES MIA Y LA DIGO: dos veces me invente mi propia definicion en vez de correr el instrumento (union de aristas y censo de ficheros de bateria), y las dos el equivocado era yo. NO HAY PARADA: la bateria se puede partir en tramos sin tocar ninguna de las cuatro cosas que la letra del 5 sep fija, y esta medido por que hace falta, entre 57 y 75 minutos de bloque indivisible con la nomina en 87. LA 176 REPITE LA VUELTA DE BATERIA, EN TRAMOS, CON RESTAURACION AL ENTRAR Y CON LA GUARDA DEL COMMIT DELANTE'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V176_HEAD_APERTURA.txt`: `e8638442`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `2e00ad9e`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **175**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 176`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
37 celdas no se pudieron leer"** y de esas lineas de rojo, **18
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LA BATERIA DE MUTACIONES ENTERA, SOLA Y CON SU DOBLE CORRIDA, PERO PARTIDA EN TRAMOS QUE QUEPAN EN UNA SESION, porque la causa de que la 175 se la comiera entera esta MEDIDA: 87 entradas por dos corridas cada una son un bloque indivisible de entre 57 y 75 minutos. Se parte el BOCADO y no se afloja NADA de las cuatro cosas que la letra del fundador del 5 sep fija (cadencia, soledad, integridad y la prohibicion de podar la nomina): cada entrada sigue corriendo y sigue corriendo DOS VECES. Lleva dentro su GUARDA DEL COMMIT bloqueante y su RESTAURACION AL ENTRAR de cada tramo, cada tramo SELLA Y COMMITEA su propia salida, y al final la salida unica se COMPONE y se MIDE (bytes, lineas, sha256) antes de nombrarla en ningun sitio | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | ABRIR Y CERRAR ESTE MISMO REPORTE EN LA MISMA VUELTA. La 174 lo hizo entero, la 175 NO LLEGO (murio dentro de la bateria y dejo sus dos filas diciendo ABIERTA, SIN CERRAR), asi que la racha que `AUDITOR.md` 6.2 pide VUELVE A EMPEZAR y esta es OTRA VEZ la primera de las dos seguidas. Esqueleto al empezar, la fila de la TAREA 1 anexada al cerrarse CADA TRAMO y no al final, cierre con `scripts/loop/cerrar_reporte.py` en esta misma vuelta, y ARCHIVADO EN LA MISMA VUELTA sin esperar a la 177 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
