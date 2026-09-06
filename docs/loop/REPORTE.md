# REPORTE DE LA VUELTA 185 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta185_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que no lleva nada
> mas. **Cerro entera en la 184**, con sus nueve tramos sellados, asi que **la
> siguiente vuelta de bateria es la 189**. En las vueltas intermedias la seccion 9
> se cierra igual, con el **nombre del fichero, sus bytes medidos y su
> atribucion**, las tres juntas o no vale.
>
> **EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y LA CUENTA SIGUE EN CERO.** El
> regimen `AUDITOR.md` 6.2 devuelve el tope a cinco cuando **dos vueltas seguidas
> cierren su propio reporte** con `scripts/loop/cerrar_reporte.py`. **La 184 no
> cerro el suyo** (`cerrar_reporte.py` exitcode 1, salida pegada entera en su
> reporte), asi que la cuenta **sigue en cero**. **Van dos tareas y no hay una
> tercera.**
>
> **EL TRABAJO DE ESTA VUELTA ES DESATASCAR EL CIERRE DEL REPORTE**, que lleva
> CUATRO vueltas sin conseguirse (181, 182, 183 y 184), y que es el mismo atasco
> por el que el fundador puso el regimen 6.2 el 5 sep.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee el
> par **2.464** ni ningun otro de la cola post fusion (encabeza el encargo de la
> **186**); no se cablea el instrumento de vigencia de las `A` rancias por `P.5`;
> **no se vuelve a decidir ninguna clase** en la relectura al doble; no se toca el
> marcador, ni un veredicto, ni `dataset/`; **no se poda la nomina de la bateria**,
> que es la opcion `c` que el fundador RECHAZO el 5 sep; y **no se repara el
> desfase del acta `VUELTA - 1`** de la `5.2`, que queda encargado y sin ejecutar
> porque el tope son dos sub-tareas.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py` y desde la 178 vuelve a correr en su sitio. **Una
> columna de apertura medida al cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO YA NO TIENE REPORTE AJENO QUE ARCHIVAR, PORQUE
> LA TAREA 2.a LO ARCHIVO ANTES.** El orden de esta vuelta no es el de siempre y
> el motivo se dice: si el esqueleto corriera primero, su PASO 0 archivaria el
> reporte de la 184 **sin cerrar**, y la reparacion de la TAREA 1.c llegaria tarde
> para el unico reporte al que le sirve. **El PASO 0 se corre igual y su salida se
> pega con lo que salga**, diga lo que diga, en vez de dejar la fila muda.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta185_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 184: `dc558582`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 184: LA CONTINUACION DE LA 183 REPRODUJO ENTERA, LOS SIETE DISCUTIBLES VAN A FAVOR, Y ADJUDICO LA REPARACION DEL ARNES QUE PARO LA BATERIA.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V185_HEAD_APERTURA.txt`: `5834632b`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `2c72d81d`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **184**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 185`. **Esta
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
| **TAREA 1** | LOS REGISTROS Y LAS TRES REPARACIONES DE CODIGO. BLOQUEANTE. (a) El acta 185 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus siete adjudicaciones `5.1` a `5.7` todas a favor, los CUATRO pendientes de doctrina de la seccion 6 con su estado leido del titulo (`PD.2`, `PD.3` y `PD.4` CERRADAS por cita y `PD.1` ABIERTA con sus cinco puestos leidos del acta y no copiados del encargo), la caida propia del auditor `A.1` y la caida de reporte del ejecutor `R.1`, mas su caso positivo por mutacion sobre un acta FABRICADA con el esperado mutado cayendo, y la deuda de la serie REMEDIDA y no heredada del `R.46`. (b) LA SALIDA SELLADA DEL ARNES QUE PARO LA BATERIA DEJA DE CAMBIAR SOLA: funcion PURA `sin_temporal(linea, tmp)` aplicada ANTES del recorte, sin tocar lo que el arnes prueba, con arnes propio de DOS MITADES que fallan por separado. (c) LA GUARDA DE LA BATERIA CONTINUADA, que es la adjudicacion `6.2` del acta 185: `vuelta_que_sello()` y `tramos_por_vuelta()` nuevas, `rama_de_la_seccion9()` con un cuarto parametro que por defecto se comporta EXACTAMENTE como hoy, y una rama nueva que EXIGE MAS que la vieja con CUATRO condiciones a la vez, con la evidencia computada de git y sin ninguna bandera. (d) LA ESCALADA DE `AUDITOR.md` 1.2: la columna `quien lo sello` se computa en vez de teclearse, y el cotejo de las NUEVE celdas contra las que el reporte de la 184 ya lleva es la prueba. (e) LA RELECTURA AL DOBLE del tramo de la ciega del acta 185, con el cotejo de `sha256` contra el sello `V185b` ANTES de leer un solo puesto | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | EL CIERRE DE DOS REPORTES: EL DE LA 184 Y EL DE LA 185. (a) El reporte de la 184 se cierra con la guarda ya reparada por la 1.c, DESPUES de cotejar sus tres piezas por `sha256` y por bytes contra lo que la 184 midio, con el veredicto de una linea TALLADO y no tecleado, y se archiva. (b) El reporte de la 185 se abre en su esqueleto, cada tarea anexa su fila al cerrarse, la cabecera se talla y `--comparar` tiene que dar CABECERA IDENTICA AL TALLADOR, y su SECCION 9 CIERRA CON EL HUECO DECLARADO Y MEDIDO por el carril de `cerrar_reporte.py`: nombre del fichero, bytes medidos y atribucion, las tres juntas o no vale | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
