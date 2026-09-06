# REPORTE DE LA VUELTA 184 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta184_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA VUELVE A SER DE BATERIA, Y RETOMA EN EL TRAMO 6.**
> `AUDITOR.md` 6.1: la bateria se declara corrida cuando **los NUEVE** tramos
> tienen salida sellada **del mismo calibre**, y el acta 184, punto 8, la midio
> en **CINCO**, con el siguiente en el **TRAMO 6**. **El TRAMO 5 se re-corre**
> porque su rojo es lo que la TAREA 1.b repara, y una salida sellada en rojo no
> es del mismo calibre que ocho en verde. **La seccion 9 de este reporte lleva la
> bateria entera dentro, no un hueco.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y LA CUENTA VOLVIO A CERO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. El acta 184,
> punto 8, lo remidio en git sobre `docs/loop/reportes/`: **la 182 SI cerro el
> suyo** y **la 183 NO**, asi que la racha **se rompe y arranca de cero**. **Van
> dos tareas y no hay una tercera.**
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ningun par de los 543 ni se toca la cola de `docs/plan/08_VERIFICACION.md` (su
> TRAMO 1 es el par **2.464** y se relee cuando haya vuelta de trabajo, no en la
> de bateria); no se cablea el instrumento de vigencia de las ocho `A` rancias por
> `P.5`; **no se vuelve a decidir ninguna clase** en la relectura al doble; no se
> toca el marcador, ni un veredicto, ni `dataset/`; y **no se poda la nomina de la
> bateria**, que es la opcion `c` que el fundador RECHAZO el 5 sep.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Las dos preguntas vuelven a coincidir en el numero, pero
> **no en el estado**: el reporte de la 183 **se quedo SIN CERRAR y SIN
> ARCHIVAR**, cosa que el bloque de apertura de hoy midio sin creerle al encargo
> (`docs/loop/SALIDA_V184_APERTURA.txt`, bloques H.1 y H.8). **Lo archiva el
> PASO 0 de este esqueleto, antes de escribir una sola linea encima**, y su
> salida se pega abajo con lo que salga. **Un reporte sin cerrar se archiva tal
> como quedo: taparlo con un cierre de hoy seria escribir en pasado lo que no
> paso.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta184_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 183: `d5862dcc`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 183: LA VUELTA SE CORTO EN EL TRAMO 2 DE 9 Y LO PUBLICADO REPRODUJO ENTERO, PERO LAS CUATRO SALIDAS SELLADAS DE ESA BATERIA DICEN QUE SON DE LA VUELTA 176.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V184_HEAD_APERTURA.txt`: `dc558582`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `c1ac7d59`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **183**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 184`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO,
19 celdas no se pudieron leer"** y de esas lineas de rojo, **0
mencionan APERTURA**. Este hueco se rellena con la tabla tallada entera cuando la
vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS Y LAS DOS REPARACIONES DE CODIGO, BLOQUEANTE Y ANTES DE TOCAR LA BATERIA. (a) El acta 184 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus siete adjudicaciones `5.1` a `5.7`, LA ADJUDICACION DEL PUNTO 6 contada aparte porque no lleva numeral `5.n`, las cero caidas propias del auditor DECLARADAS con todas las letras y la caida `E.1` del ejecutor, mas su caso positivo por mutacion con el esperado mutado cayendo, y la deuda de la serie REMEDIDA y no heredada del `R.45`. (b) LA REPARACION DEL ARNES QUE PARO LA BATERIA, que es la adjudicacion del punto 6 del acta 184: en `scripts/loop/vuelta165_tarea2_mutacion_censo.py`, `esperadas` deja de teclearse y se computa de la nomina real, los dos ficheros que el auditor de la 165 nombro NO se borran y el caso pasa a exigir que sigan DENTRO del conjunto invisible y no que sean TODO el conjunto, la cifra sale con su corte por banco `9.21`, y todos los casos del arnes tienen que CAER al mutar su esperado. (c) LA ESTIMACION DEL `--plan` SALE CON SU CORTE PEGADO, que es la escalada de la racha de reporte: funcion PURA y arnes propio que CAE si la linea sale sin su corte o si el corte no coincide con la nomina contada en esa corrida. (d) LA RELECTURA AL DOBLE del tramo de la ciega del acta 184, con el cotejo de `sha256` contra el sello ANTES de leer un solo puesto | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA BATERIA, DEL TRAMO 5 AL 9, Y EL CIERRE DEL REPORTE. El TRAMO 5 se re-corre primero, ya con (b) puesto, y despues los tramos 6, 7, 8 y 9 en orden; cual toca lo dice `--siguiente` y no la memoria. Cada tramo se commitea CON SU SALIDA SELLADA al terminar, antes de seguir; el reloj de cada tramo se mide al cerrarlo y se publica medido; una salida sellada que mide CERO BYTES no cuenta como hecha; `git diff --numstat -- dataset/` se mide AL ENTRAR y AL SALIR de cada tramo y las dos cifras se publican. Si otro arnes cae en rojo, el ejecutor se detiene ahi y lo trae con su salida entera, sin re-correrlo y sin arreglarlo. Cuando los nueve tramos tengan salida sellada del mismo calibre, `--componer` arma `docs/loop/SALIDA_V183_BATERIA.txt` y con esa pieza se cierra el reporte con `scripts/loop/cerrar_reporte.py`, que es lo que lleva dos vueltas sin conseguirse. El reporte, una vez cerrado, se archiva en su propia vuelta | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
