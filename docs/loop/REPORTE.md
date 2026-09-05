# REPORTE DE LA VUELTA 179 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta179_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA NO SE ELIGE AQUI: ESTA
> ADJUDICADA Y RECONFIRMADA DOS VECES.** El acta 176, punto 7.8, reanclo el
> contador a la vuelta que de verdad corrio la bateria y no a la que la tenia
> encargada; **el acta 178, punto 11, lo reconfirmo**; y el encargo de esta vuelta
> lo repite con todas las letras: **la proxima vuelta de bateria es la 181**, y la
> 179 y la 180 cierran su seccion 9 con el **HUECO DECLARADO Y MEDIDO**, con su
> nombre, sus bytes medidos y su atribucion, las tres juntas. Un hueco declarado
> no es un hueco escondido.
>
> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 LO
> CONFIRMO ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen temporal de
> dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su propio reporte**
> con `cerrar_reporte.py`, y eso se cumplio. **El regimen temporal queda CUMPLIDO
> Y CITABLE, no borrado**, y los cuatro commits que lo sostienen se localizan EN
> GIT en el bloque B.1 de `scripts/loop/vuelta179_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno y aqui se repite: el medidor corre
> dentro del bloque de apertura. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA**, y eso lo dice el encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 178 escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta179_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 178: `74cad47d`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 178: 29 DE 33 A CIEGAS Y LAS CUATRO QUE FALLARON LAS FALLE YO, PERO LA RACHA DE REPORTE LLEGA A DOS Y LA ESCALADA SE ENCARGA EN ESTE MISMO ACTA.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V179_HEAD_APERTURA.txt`: `74cad47d`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `02af60ee`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **178**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 179`. **Esta
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
| **TAREA 1** | LOS REGISTROS, LAS CORRECCIONES Y LA OPERACION DE CODIGO DE LA ESCALADA, Y ES BLOQUEANTE. Cuatro letras: (a) LA CORRECCION DECLARADA DE LA CAIDA DE LA 178, que publico en su 1.e `16 casos` donde su propio fichero `docs/loop/SALIDA_V178_T1E_MUTACION.txt` dice 18, con las TRES cifras al lado (la publicada, la del fichero y la de la re-corrida de hoy) y SIN retocar el reporte archivado, que dice lo que se publico; (b) LA OPERACION DE CODIGO DE LA ESCALADA, que es la pieza que manda: la guarda de LA PROSA QUE CITA UN FICHERO, dentro de `cerrar_reporte.py` y como funcion PURA junto a sus hermanas, que caza toda frase que publique una cifra de casos de un arnes Y nombre un `SALIDA_V*.txt` en la misma linea, lee la cifra propia de ese fichero y CAE EN ROJO nombrando la linea, la cifra publicada y la del fichero, con los bloques cercados fuera y con el fichero inexistente o de cero bytes tambien en ROJO; con su caso positivo por mutacion y CORRIDA SOBRE `REPORTE_V178.md` publicando lo que salga; (c) LOS DOS ARNESES DESTAPADOS ENTRAN EN LA NOMINA de `verificar_mutaciones_viejas.py`, mas todo arnes que esta vuelta escriba, con la cuenta entera y la resta comprobada, ANTES de la 181 para que el rojo que la 178 anuncio no llegue a existir; (d) EL CORTE DEL DENOMINADOR CABLEADO DONDE SE GENERA LA CIFRA y no en una frase, porque la 178 publico 15 de 92 siendo verdad y al cerrar eran 15 de 98 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | `OP-L-03`: SE LEEN LOS DIEZ PARES REALES DE LOS ACTOS SIN LEER. El backlog ya esta re-medido y `backlog_l03_resuelto.py` sale VERDE con los dos caminos calzando en los 40 actos: de los 73 pares que el instrumento da quedan 18 reales, 8 los leyo la 177 y quedan 10 en los 34 actos que nadie ha mirado. Los diez se leen con la vara del banco, par por par, y cada uno con su veredicto y su razon en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SOLO SI EL PAR TIENE PUESTO EN LA COLA; si no lo tiene NO SE INVENTA UN PUESTO y su clase y su razon van al registro de `OP-L-03` en el campo `clases_de_los_pares_por_leer`, que es donde la 177 las puso y donde son trazables. El marcador no se toca si no hay puesto, y si lo hay se recomputa del archivo con sus cuatro clases. Cada acto cierra con su forma escrita: la figura, su cobertura y lo que queda. Y la cifra va al lado, siempre las dos: pares del instrumento y pares reales | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LOS DIECISEIS TRIANGULOS SE PUBLICAN PARTIDOS POR SU FUENTE, y NINGUNA CLASE SE MUEVE. `vuelta178_tarea3_anotar_triangulos.py` publica la cifra PARTIDA y no solo el 16: cuantos descansan enteros en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y cuantos se apoyan en un lado de fuera, y NOMBRA aquellos en que el lado de fuera es el `D`, que es el lado que hace que el triangulo sea un triangulo. `docs/plan/OP_L_03_TRIANGULOS.jsonl` gana un campo por fila que diga si el triangulo es recomputable entero del archivo, y el campo `fuente_de_la_clase` por lado NO se toca. CERO VEREDICTOS MOVIDOS, comprobado por `sha256` antes y despues. Con su caso positivo por mutacion sobre un registro fabricado, donde un triangulo con sus tres lados en el archivo y otro con el `D` fuera caen en casillas distintas | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS QUINCE DEL SUJETO CONGELADO SE JUZGAN, UNA A UNA, Y NO SE CABLEA NADA TODAVIA. Primero se juzgan, despues se cablea, y no al reves. Por cada una de las quince, un veredicto escrito con su prueba: o el arnes de verdad ABRE un fichero vivo de la campana y hay que congelarle el sujeto, o LO NOMBRA SIN ABRIRLO y basta con que lo declare, o es un CASO DECLARADO legitimo y se anota por que. Registro propio y no prosa: `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, una fila por arnes, con el nombre, el veredicto, el fichero que abre y la evidencia (la linea del codigo). NO se arregla ningun arnes en esta vuelta y NO se cablea la guarda al rojo global de la bateria: el cableado se decide con los quince veredictos delante. NADA se borra de la nomina | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA. Ninguna de estas cinco se toca aqui, y las cinco se nombran CON SU MEDICION (existe, bytes en disco y normalizados a LF) para que no se caigan: la segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de `paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA ANTERIOR cuando la maquina pregunta por EL REPORTE QUE VA A PISAR; la guarda que falta en la dependencia del `D.4` de la 174, donde el esqueleto clona en vez de importar y nada avisa si el fichero del que se clono desaparece; el grano del tope de 10 minutos, que se mide EN LA 181 con el reloj de esa corrida y no se re-elige a ojo antes; y la convencion de bytes, que es del fundador, lleva seis actas subiendo y sube como PENDIENTE y no como problema, porque el remedio provisional de publicar siempre las dos ya es instrumento | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
