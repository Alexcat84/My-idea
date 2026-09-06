# REPORTE DE LA VUELTA 183 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta183_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA SI ES DE BATERIA, Y ESO MANDA SOBRE TODO LO DEMAS.**
> `AUDITOR.md` 6.1: la bateria corre CADA CINCO, en **VUELTA PROPIA**, y esa
> vuelta **no lleva trabajo de plan al lado**. **La 181 era la suya y se corto
> antes de lanzarla.** La decision del fundador del **5 sep 2026** (PREGUNTA 4 de
> `docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) la manda **por
> tramos resumibles**, y su lanzador,
> `scripts/loop/vuelta183_bateria_por_tramos.py`, esta escrito desde la 182 y sin
> correr. **La seccion 9 de este reporte lleva la bateria entera dentro, no un
> hueco: esta vez si es su vuelta.**
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES INERCIA: ESTA MEDIDO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. El acta 182,
> punto 8, lo midio: **la 181 NO cerro el suyo** y **la 182 SI**, asi que la
> cuenta va por **UNA**. **Si la 183 cierra el suyo, seran dos seguidas y el tope
> vuelve a cinco en la 184.**
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ningun par de los 543 ni se toca la cola de `docs/plan/08_VERIFICACION.md` (su
> TRAMO 1 es el par **2.464** y se relee cuando haya vuelta de trabajo, no en la
> de bateria); no se cablea el instrumento de vigencia de las ocho `A` rancias por
> `P.5`; no se toca el marcador, ni un veredicto, ni `dataset/`; y **no se poda la
> nomina de la bateria**, que es la opcion `c` que el fundador RECHAZO el 5 sep.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Las dos preguntas vuelven a coincidir en el numero, pero
> **no en el estado**: la 182 **cerro su reporte con `cerrar_reporte.py` y NO
> lo archivo en su misma vuelta**, cosa que el bloque de apertura de hoy midio
> (`docs/loop/SALIDA_V183_APERTURA.txt`, bloque H.4: `REPORTE_V182.md
> archivado: NO`). **Lo archiva el PASO 0 de este esqueleto, antes de escribir
> una sola linea encima**, y su salida se pega abajo con lo que salga.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta183_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 182: `0ef74748`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 182: LA APERTURA SELLADA CUMPLIO EN SU ESTRENO, Y EL VEREDICTO DE UNA LINEA SE CONTRADICE CON SU PROPIA SECCION 8.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V183_HEAD_APERTURA.txt`: `0ef74748`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `f3593671`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **182**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 183`. **Esta
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
| **TAREA 1** | LOS REGISTROS Y LA ESCALADA, BLOQUEANTE Y ANTES DE LA BATERIA. (a) El acta 182 entra en la serie de registros con el numero que devuelve `scripts/loop/serie_de_registros.py` y no tecleado, con sus adjudicaciones `5.D.1` a `5.D.7` y `7.1` a `7.5`, su caida propia del auditor y las dos del ejecutor, y su caso por mutacion. (b) LA DEUDA DE OCHO REGISTROS SE DOCUMENTA COMO SALTO Y NO SE RELLENA: una sola linea de constancia en la serie, en su sitio, con la cifra contada por el instrumento. (c) LA ESCALADA DE `AUDITOR.md` 1.2, que es la operacion de codigo de esta vuelta: `scripts/loop/cerrar_reporte.py` gana una funcion PURA con arnes propio que coteja los numerales del veredicto de una linea contra lo que el cuerpo permite contar (caidas propias `C.n` de la seccion 8 y filas de la tabla de tareas), lee los numerales TAMBIEN escritos con letra, y CAE EN ROJO sin escribir nada si no calzan. Con caso positivo POR MUTACION SOBRE VARIABLE COMPUTADA. (d) EL HUECO DE LA SECCION 9 TIENE QUE DECIR SI EL FICHERO NO EXISTE O SI MIDE CERO, que hoy los confunde en un `max(tam, 0)`, sin tocar las tres piezas que el hueco ya exige. (e) LA RELECTURA AL DOBLE del tramo de la ciega: los 30 puestos de la seccion 9 del acta 182 y sus 30 vecinos deterministas, mecanica y con la vara, sin volver a decidir la clase de ningun par | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA BATERIA DE MUTACIONES, ENTERA Y POR TRAMOS. `scripts/loop/vuelta183_bateria_por_tramos.py`, escrito y medido en la 182 y sin correr. Cada tramo se commitea CON SU SALIDA SELLADA al terminar, antes de seguir; una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE y cual toca lo dice `--siguiente`; la bateria se declara corrida cuando LOS NUEVE tienen salida sellada DEL MISMO CALIBRE; una salida sellada que mide CERO BYTES no cuenta como hecha; la doble corrida y todas las demas guardas siguen enteras, y lo unico que cambio es la cadencia. El reloj de cada tramo se mide al cerrarlo y se publica medido: la estimacion del `--plan` es estimacion y se dice como tal. Si un arnes cae en rojo, el ejecutor se detiene ahi y lo trae con su salida entera | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
