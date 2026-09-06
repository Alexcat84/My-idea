# REPORTE DE LA VUELTA 190 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta190_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que **no lleva
> nada mas**. **La 189 la corrio entera** (sus diez tramos siguen sellados en
> disco y el bloque **H.5** del sello de apertura los remidio uno a uno antes de
> tocar nada), asi que **la siguiente cae en la 194**. El hueco va **con su
> medicion, su atribucion y su corrida, por el carril de `cerrar_reporte.py`**:
> un hueco declarado no es un hueco escondido.
>
> **Y VAN CINCO SUB-TAREAS Y NO DOS.** El tope temporal de la `AUDITOR.md` 6.2
> **se cumplio y caduca**: su disparador de salida pedia **DOS vueltas seguidas
> cerrando su propio reporte** con `cerrar_reporte.py`, y **son TRES**. El bloque
> **B.2** del sello de apertura las localizo **en git y no de memoria**, por el
> asunto de su commit, y midio ademas sus tres ficheros de cierre con
> `CIFRA piezas que faltan: 0` en los tres. **Vuelve el tope de CINCO** de la
> seccion 6 de `EJECUTOR.md`.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan que no sean la **busqueda** de la TAREA 5,
> ni las mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador
> RECHAZO el 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el
> fundador**). **Y no entran las SEIS que el encargo deja nombradas a proposito
> para que la 191 no las redescubra:** las dos convenciones de `lineas`,
> `acumulan()` contra la tabla, el cotejo de clon declarado que separa, la
> excepcion que publica siempre su lista, la medicion del censo de arneses sin
> fichero, y las ocho actas sin entrada propia en la serie. **Y no se corre la
> bateria.**
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y **las dos cifras se publican**.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta190_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 189: `bbeea713`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 189: LA 188 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA, ADJUDICO LOS SEIS DISCUTIBLES A FAVOR Y CONTESTO LAS TRES PREGUNTAS, DECLARO DOS CAIDAS PROPIAS MIAS Y CERO DEL EJECUTOR, Y CAZO QUE EL LANZADOR DE LA BATERIA YA REPARTE EN DIEZ TRAMOS Y SU --siguiente HABRIA CORRIDO OCHO ARNESES DE 125 DECLARANDOSE CORRIDO.'
- **DESFASE DECLARADO, SEXTA VUELTA:** la linea de arriba nombra el acta
  **189** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 190**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque no es ninguna de sus cinco tareas y el encargo nombra una a
  una las seis que quedan fuera. Se declara en vez de colarse.
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V190_HEAD_APERTURA.txt`: `b393347f`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `70d5662c`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **189**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 190`. **Esta
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
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 190 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus DIEZ adjudicaciones `4.1` a `4.10`, QUE NO SON DIEZ A FAVOR: seis son los discutibles del ejecutor y de esos CINCO van A FAVOR (`D.1`, `D.2`, `D.3`, `D.4`, `D.6`) y UNO EN CONTRA, el `D.5`, la guarda del sujeto congelado fuera del veredicto. La marca de EN CONTRA tiene que EXISTIR y tiene que SALIR EN LA CUENTA, probada por mutacion con un acta fabricada. Mas las TRES preguntas contestadas (`4.4` la `P.1`, `4.8` la `P.2`, `4.9` la `P.3`), los DOS hallazgos de la seccion 5 que no salen de ningun discutible (las dos convenciones de `lineas` en `5.1` y las ocho actas sin entrada propia en `5.2`), CERO caidas propias del auditor ESCRITO COMO CERO Y NO OMITIDO y TRES del ejecutor, las tres DE METODO y ninguna de racha, y LA VARA CORRIDA POR EL AUDITOR (`5.4`) con sus cifras. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido, no escribe nada, y se prueba re corriendolo con la sede medida antes y despues | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA GUARDA DEL SUJETO CONGELADO: SEPARA LA DEUDA DEL FALLO, Y VUELVE AL VEREDICTO. Son las adjudicaciones `4.4` y `4.6` del acta 190 y las dos mitades van juntas porque una sin la otra no sirve. (a) la guarda SEPARA EN SU SALIDA las entradas `NO DECIDIBLE` que traen MOTIVO ESCRITO de las que no lo traen, y publica LAS DOS CIFRAS CON SUS NOMBRES; hoy "3 entradas sin congelar" no distingue una deuda de una decision, y esa es la `P.1` que el acta 189 dejo encargada en su `4.7`. Las tres de hoy son `vuelta186_tarea2c_mutacion_cierre_tardio.py`, `vuelta187_tarea4_mutacion_dos_convenciones.py` y `vuelta188_tarea4_mutacion_cobertura_parejas.py`, y cuantas traen motivo escrito SE MIDE. (b) LA GUARDA VUELVE AL VEREDICTO del instrumento de la nomina: el `D.5` de la 189 la saco y el acta 190 lo TUMBA, porque publicar los tres nombres arriba y cerrar en verde deja sin sintoma al que solo mire el veredicto. Con la separacion de (a) puesta, el veredicto ya puede decir ROJO POR DEUDA DECLARADA distinto de ROJO POR FALLO sin dejar de ser rojo. NO SE AFLOJA NINGUNA GUARDA, y el rojo que salga se trae con su nombre. Con simulacion previa sobre copia en memoria y caso positivo por mutacion | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LA BATERIA: QUE SU EXITCODE SEPARE, Y QUE RESTAURE SOLA LO QUE PISA. Son las adjudicaciones `4.4` y `4.9` del acta 190, y NO SE CORRE LA BATERIA en esta vuelta: se arregla su lanzador y se prueba con sus arneses. (a) EL EXITCODE SEPARA: hoy los diez tramos de la 189 salieron con exitcode 1 y en NUEVE de ellos no cayo ni un arnes, porque la fuente era siempre la guarda de nomina en deuda, y un unico `1` para un arnes caido y para una deuda declarada es degradacion silenciosa (banco 9). Que el lanzador distinga los dos casos en su salida sellada y en su codigo de salida, y que lo diga con su cifra. (b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, como ya restaura `dataset/`: en la 189 piso TRES y las restauro una persona a mano, en dos vueltas distintas y a dos personas distintas. La restauracion va EN LF, y si el corte nuevo interesa se escribe AL LADO con nombre nuevo y su vuelta, nunca encima. Con simulacion previa y caso positivo por mutacion que CAIGA si una salida sellada ajena se queda pisada | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA RELECTURA AL DOBLE DEL TRAMO DEL PUESTO 2422. ES UNA DEUDA DEL ACTA 189 Y NO SE SALTA DOS VUELTAS SEGUIDAS: la 189 la aplazo con razon por ser vuelta de bateria, y esa razon ya no vale. El acta 189 encontro la discrepancia del puesto `2422` FUERA de sus dudosos marcados, y `AUDITOR.md` 1.2 dice que eso baja el credito de la tanda y obliga a releer ese tramo AL DOBLE. Corre la relectura con `scripts/loop/aislador_de_ciega.py`, sobre los vecinos deterministas del tramo del `2422`, con el criterio escrito, la ciega y el destape en ficheros separados, y las clases escritas ANTES de abrir el destape. Publica cuantos coinciden y cuantos discrepan. NO SE TOCA NINGUNA CLASE del archivo: si de la relectura sale una correccion se declara y se trae, y no se escribe sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en esta vuelta. El `sha256` LF del archivo abre y cierra en `0a77b5a35a962621` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LA SEDE DE `OP-L-02`: BUSCARLA, NO INVENTARLA. Es la `4.1` del acta 189 y la vara del acta 190 (`5.4`) la confirma medida: corrida con `--corte 63d0c5b4` da 71 fichas, 6 en LISTA sin ninguna prueba, 2 de ellas CONSUMIDAS por `OP-U-01` y 4 de TRABAJO REAL; de esas cuatro, tres son mesas cuyo producto documental SI existe en disco, y `OP-L-02` es LA UNICA SIN DOCUMENTO QUE MEDIR, con 0 menciones de fichero en su evidencia. Su `verificacion` habla de "las tres nominas afectadas" y de "cada grupo del backlog": BUSCA SI ESAS TRES NOMINAS TIENEN SEDE EN EL REPO, con comandos propios, y publica la busqueda entera (que se busco, donde, y que se encontro). Y EL LIMITE, ESCRITO PARA QUE NO SE CRUCE: si la busqueda no encuentra sede en ninguna parte, ESO ES EL RESULTADO Y SE PUBLICA COMO TAL. NO se le inventa una sede a la ficha, ni se declara HECHA, ni se mueve de estado: inventarle una sede es cambiar el alcance de la campana, y eso lo reserva el fundador | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
