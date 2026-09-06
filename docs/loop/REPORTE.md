# REPORTE DE LA VUELTA 182 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta182_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y ESO TAMBIEN ES LETRA.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO, en VUELTA PROPIA. **La 181 era la suya y se corto
> antes de lanzarla**, y su acta lo registra en el punto 7.5 sin contarlo como
> caida de reporte, porque el esqueleto por anexion dejo la fila diciendo ABIERTA,
> SIN CERRAR y no publico ninguna cifra de una corrida que no hubo. La decision
> del fundador del **5 sep 2026** (PREGUNTA 4 de
> `docs/loop/paradas/2026-09-05-cola-post-fusion-DECISION.md`) manda que corra
> **POR TRAMOS RESUMIBLES**, y la **TAREA 5** de este encargo la deja preparada y
> declarada para la **183**. **La seccion 9 de este reporte cierra con su HUECO
> DECLARADO Y MEDIDO**, que es lo que el regimen 6.1 manda para las vueltas
> intermedias: un hueco declarado no es un hueco escondido.
>
> **EL TOPE DE ESTA VUELTA ES CINCO SUB-TAREAS, Y TAMPOCO ES UNA GANA.** La
> adjudicacion **6.8 del acta 180** bajo el tope a DOS en la 181 porque era vuelta
> de bateria, y en la misma frase escribio: *"El tope vuelve a cinco en la 182"*.
> El encargo de esta vuelta trae **CINCO** y dice *"que es el tope. Ni una mas"*.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** no se relee
> ninguno de los 543 pares que la TAREA 4 mete en la cola (eso es justo lo que la
> decision del fundador evita al conceder la `b` y no la `c`), no se toca el
> marcador, no se cambia ningun veredicto del archivo, y **las `A` no ganan cola
> nueva** por la PREGUNTA 2 de la misma decision. **Y no se corre la bateria**: se
> prepara.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** El remedio se cableo en
> `vuelta177_apertura.py`, la 178 lo estreno, la 179 y la 180 lo repitieron y aqui
> vuelve a correr en su sitio. **Desde la 178, una columna de apertura medida al
> cierre es caida que ACUMULA.**
>
> **Y EL PASO 0 DE ESTE ESQUELETO PREGUNTA POR EL REPORTE QUE VA A PISAR, NO POR
> LA VUELTA ANTERIOR.** Esta vez las dos preguntas vuelven a coincidir, porque la
> 181 escribio su reporte, lo cerro y lo archivo EN SU MISMA VUELTA; el
> fichero corre LAS DOS igualmente y publica lo que salga de cada una, porque una
> guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta182_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 181: `b931019f`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 181, Y PARADA: UNA FUSION LE MOVIO LA EVIDENCIA A UN VEREDICTO CERRADO Y LA COLA QUE DEBIA RELEERLO EXCLUYE SU CLASE.'
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V182_HEAD_APERTURA.txt`: `326d7dc9`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `c85f0c4d`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **181**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 182`. **Esta
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
| **TAREA 1** | LOS REGISTROS Y LA DEUDA DE LECTURA. (a) El acta 181 y sus adjudicaciones entran en la serie de registros, con el numero que devuelve `scripts/loop/serie_de_registros.py` y no tecleado. (b) LOS DOS PENDIENTES DEL ACTA 180, que llevan una vuelta esperando y estan escritos en sus puntos `6.8` y `6.6`: el remedio del `E.1` sobre `scripts/loop/cerrar_reporte.py`, que es la rama que escribe la cabecera CORRIDA ENTERA Y SOLA sobre una seccion 9 cuyo cuerpo dice que nadie la corrio, y la `P.1`, el arnes `vuelta172_tarea1c_guarda_que_mordio.py`, que cae con exit 1 fallando 1 de 6 y esta fuera del censo: primero el esperado y despues el nombre, en ese orden, que es parte de la adjudicacion. (c) LA RELECTURA AL DOBLE del tramo de la ciega que el acta 181 encarga en su `7.2` por `AUDITOR.md` 1.2, sobre los 30 puestos que su seccion 8 lista | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA APERTURA DEL AUDITOR COMO CODIGO (decision del fundador del 5 sep 2026, PREGUNTA 3, opcion c, la mitad que quita el problema de raiz; la otra mitad, que ROMPER UN REMEDIO ESCRITO ACUMULE, ya esta escrita en `AUDITOR.md`). Fichero GEMELO del bloque de apertura del ejecutor: corre `scripts/loop/aislador_de_ciega.py` y SELLA SU SALIDA ANTES de que el turno pueda tocar `git log`, `git status` o `docs/loop/REPORTE.md`. Con CASO POR MUTACION SOBRE VARIABLE COMPUTADA, no sobre constante literal (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): si el sello se intenta DESPUES de tocar cualquiera de los tres, TIENE QUE CAER, y la prueba se corre cambiando el valor esperado para comprobar que el caso cae de verdad | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | EL INSTRUMENTO DEL DIFERENCIADOR MOVIDO (decision del fundador del 5 sep 2026, PREGUNTA 1, la `b`). Cruza LA RAZON ESCRITA de cada `D` contra LOS PASOS DE HOY del otro nodo, y SOLO las `D` con la lesion exacta vuelven a la cola. CASO POSITIVO OBLIGATORIO: EL PUESTO 2.464 TIENE QUE SALIR NOMBRADO; si no sale, el instrumento no sirve y se dice. Y EL CENSO POR ESTADO DE LAS `A` en el mismo instrumento: ejecutadas contra pendientes, con LAS PENDIENTES DE TEXTO MOVIDO MARCADAS RANCIAS POR `P.5`. Las `A` NO ganan cola nueva: la ejecutada es cosa consumada y la pendiente ya la cubre `P.5` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LAS `D` QUE EL INSTRUMENTO NOMBRE ENTRAN A LA COLA de relectura post fusion de `docs/plan/08_VERIFICACION.md`, y se releen POR TRAMOS en las vueltas siguientes. En esta vuelta SE ENTRA A LA COLA Y SE DECLARA EL TRAMO; no se releen 543 pares, que es justo lo que la decision del fundador evita al conceder la `b` y no la `c` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LA VUELTA DE BATERIA VA EN LA 183, POR TRAMOS RESUMIBLES (decision del fundador del 5 sep 2026, PREGUNTA 4, opcion `a`, con el precedente de los nueve tramos de la vuelta 176). Aqui SOLO se deja preparada y declarada: nueve tramos, cada uno se commitea CON SU SALIDA SELLADA al terminar, una vuelta cortada RETOMA EN EL TRAMO SIGUIENTE, y la bateria se declara corrida cuando LOS NUEVE tienen salida sellada DEL MISMO CALIBRE. En esta vuelta la seccion 9 del reporte cierra con su HUECO DECLARADO Y MEDIDO, como el regimen `6.1` manda | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
