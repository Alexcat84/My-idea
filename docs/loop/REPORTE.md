# REPORTE DE LA VUELTA 180 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta180_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA Y LA SIGUIENTE SI, Y LA CADENCIA NO SE ELIGE
> AQUI: ESTA ADJUDICADA Y RECONFIRMADA TRES VECES.** El acta 176, punto 7.8,
> reanclo el contador a la vuelta que de verdad corrio la bateria y no a la que la
> tenia encargada; **el acta 178, punto 11, y el acta 179, punto 11, lo
> reconfirmaron**; y el encargo de esta vuelta lo repite con todas las letras:
> **la proxima vuelta de bateria es la 181**. Esta es **LA ULTIMA VUELTA QUE
> DECLARA EL HUECO**: la seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** y
> sus TRES piezas juntas, el nombre del fichero, sus bytes por las dos
> convenciones y la atribucion. Un hueco declarado no es un hueco escondido, y
> **la 181 lo corre**.
>
> **EL TOPE SIGUE EN CINCO, Y NO LO DECIDE NADIE: LO DISPARO LA 177 Y LA 178 Y LA
> 179 LO CONFIRMARON ENTREGANDO CINCO.** `AUDITOR.md` 6.2 dice que el regimen
> temporal de dos sub-tareas dura **hasta que DOS vueltas seguidas cierren su
> propio reporte** con `cerrar_reporte.py`, y eso se cumplio. **El regimen
> temporal queda CUMPLIDO Y CITABLE, no borrado**, y los cuatro commits que lo
> sostienen se localizan EN GIT en el bloque B.1 de
> `scripts/loop/vuelta180_apertura.py`, no se teclean.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 lo repitio y aqui vuelve a
> correr en su sitio. **Desde la 178, una columna de apertura medida al cierre es
> caida que ACUMULA**, y eso lo dice el encargo, no este reporte.
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 179 escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.
> **Y LA TAREA 4.a DE ESTA VUELTA FABRICA EL DIA EN QUE DIFIEREN**, que es lo que
> a esta guarda le faltaba desde la 174: hasta hoy nadie la habia visto responder
> a la pregunta buena cuando las dos preguntas dan cosas distintas.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta180_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 179: `d3240915`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 179: NI UNA CAIDA CONTRA EL EJECUTOR, LA ESCALADA QUE ENCARGUE CAZA LA CAIDA DE LA 178 BAJO MI MANO, Y LA RACHA DE REPORTE VUELVE A CERO.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V180_HEAD_APERTURA.txt`: `d3240915`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `122ca81f`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **179**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 180`. **Esta
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
| **TAREA 1** | LOS REGISTROS Y LA ETIQUETA DE FUENTE, Y ES BLOQUEANTE. (a) El acta del auditor de la vuelta 179 vive en `docs/loop/ACTA_AUDITOR.md` y NO levanta ninguna caida contra la 179: la racha de reporte vuelve a CERO, la de cifra publicada sigue en CERO y no hay correccion declarada que arrastrar. (b) LA ETIQUETA DE FUENTE, ARREGLADA, y eso LEVANTA LA PARADA DE LA 3.f DE LA 179: `clases_por_par()` LEE LA VUELTA DE LA FILA DEL REGISTRO en vez del literal `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` clavado, con `sha256` de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y de `docs/plan/OP_L_03_LECTURAS.jsonl` ANTES y DESPUES dentro del propio instrumento y los CUATRO publicados, con `vuelta179_tarea3_etiqueta_de_fuente.py` re-corrido y las DOS mediciones al lado (la de antes y la de despues, y la de despues en CERO falsos o se para), con `vuelta178_tarea3_anotar_triangulos.py` re-corrido y el total de triangulos y de lados sin moverse, y con su caso positivo por mutacion sobre un registro fabricado de dos vueltas distintas | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | EL SUJETO CONGELADO, RESUELTO Y CABLEADO, Y ES LA QUE LIMPIA LA PISTA DE LA 181. El orden es: los trece declaran, los cuatro congelan, y SOLO ENTONCES se cablea. (a) LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO, once `LO NOMBRA SIN ABRIRLO` y dos `ABRE UN SUJETO YA CLAVADO`, una linea por arnes con el literal que la guarda busca y NINGUNA otra linea tocada, comprobado con `git diff --numstat` sobre `scripts/loop/` publicando las lineas anadidas por fichero. (b) LOS CUATRO QUE SI ABREN, CONGELADOS DE VERDAD, cada uno con que abria, que abre ahora y la prueba de que su resultado ya no se mueve. (c) Y SOLO ENTONCES EL CABLEADO al rojo global de la bateria, con la cifra de antes y su corte pegado y la de despues, que TIENE QUE DAR 0 o no se cablea. (d) NADA SE PODA DE LA NOMINA: todo arnes que esta vuelta escriba entra en `verificar_mutaciones_viejas.py` con la cuenta entera y la resta comprobada, antes de la 181 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | EL CORTE, CABLEADO DONDE TODAVIA FALTA. El hallazgo es del fundador y esta medido en la seccion 6 del acta 179: la tabla de tramos de la 2.a de la 179 esta contada de su fichero y sus cifras eran verdad, pero LE FALTA EL CORTE, y sin corte no hay manera de saber cual mira que. Se cablea el sello de `sello_de_corte()` DONDE SE GENERA LA TABLA DE TRAMOS de `backlog_l03_resuelto.py`, no en una frase del reporte, por `banco 9.21` y el punto 7.2 del acta 178. Y SE BARRE EL RESTO: la lista de toda cifra de ese instrumento y de `vuelta179_tarea2_cobertura_final.py` que pueda moverse dentro de una vuelta, diciendo cuales llevan corte y cuales no, y las que no lo lleven lo llevan al terminar. Con su caso positivo por mutacion: dos cortes distintos con la misma cifra no se confunden, y la misma cifra con dos cortes distintos tampoco | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS DOS PENDIENTES BARATAS QUE YA LLEVAN VUELTAS SUBIENDO, LAS DOS TEXTO QUE MIENTE SOBRE SU PROPIA MAQUINA. (a) EL DOCSTRING DE `scripts/loop/paso0_archivar_anterior.py`, que sigue hablando de LA VUELTA ANTERIOR cuando la maquina ya pregunta por EL REPORTE QUE VA A PISAR: se arregla, se publican la linea vieja y la nueva sin borrar la vieja del reporte, y SE ESCRIBE LA GUARDA QUE HACE VISIBLE LA DIFERENCIA, un caso fabricado donde las dos preguntas NO coinciden y que demuestra que la maquina responde a la buena. (b) LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL `D.4` DE LA 174: el esqueleto CLONA `vuelta_del_reporte_del_arbol()` en vez de importarla y nada avisa si el fichero del que se clono desaparece; la guarda CAE EN ROJO nombrandolo, con su caso positivo por mutacion sobre una ruta fabricada que no existe | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | EL BACKLOG DE `OP-L-02`, MEDIDO Y NO LEIDO, CON LA MISMA VARA RESUELTA QUE CERRO `OP-L-03`. Se corre el instrumento viejo de `OP-L-02` por dentro y sin citarlo de memoria y se publican LOS PARES QUE DA; se le pone encima el resolutor de `P.1` y se publican LOS PARES REALES, o sea los que no estan ya en el archivo tras resolver a nodo vivo; LAS DOS COLUMNAS VAN LAS DOS Y LA VIEJA NO SE BORRA (`banco 9.10`); el reparto por tramo va CON SU CORTE PEGADO por la TAREA 3 de este mismo encargo; y LOS DOS CAMINOS TIENEN QUE CALZAR en todos los actos medidos o se publica donde y se para. LO QUE NO SE HACE: no se lee ningun par, no se escribe ningun veredicto, no se toca el marcador, no se toca el estado de ninguna ficha (`EJECUTOR.md` 4, modo de cierre) y NO SE TOCAN LOS CINCO PARES DE SALES ROADMAP, que `docs/plan/LECTURAS_DIRIGIDAS.md` deja como decision revocable del fundador: se nombran y se dejan | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
