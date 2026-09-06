# REPORTE DE LA VUELTA 191 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta191_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA NO ES DE BATERIA, Y SU SECCION 9 CIERRA CON EL HUECO DECLARADO Y
> MEDIDO.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria de
> mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que **no lleva
> nada mas**. **La 189 la corrio entera**, asi que **la siguiente cae en la 194**.
> El hueco va **con su nombre, sus bytes medidos y su atribucion, LAS TRES
> JUNTAS**, por el carril de `cerrar_reporte.py`: **un hueco declarado no es un
> hueco escondido.**
>
> **VAN CINCO SUB-TAREAS, Y EL TOPE DE CINCO NO HACE FALTA VOLVER A GANARLO:**
> esta vigente desde la `4.10` del acta 190. **Y la cifra que lo sostiene se
> remidio en esta vuelta en vez de heredarse:** el bloque **B.2** del sello de
> apertura busco en git los commits de cierre y midio sus ficheros
> `SALIDA_V<n>_CERRAR_REPORTE.txt` uno a uno, y publica lo que salga.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**), ni la bateria, que cae en
> la 194. **Y siguen fuera, nombradas para que la 192 no las redescubra:**
> `acumulan()` que lea la tabla o declare que no es la sede; el cotejo de clon
> declarado que separa sentencia de codigo de cambio de texto; la excepcion que
> publica siempre su lista; la medicion del censo de arneses con carril de
> mutacion sin fichero propio; las ocho actas sin entrada propia en la serie (173
> a 180); el exitcode 2 propagado a `--componer`; y que el campo `evidencia` de
> `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue
> en `LISTA`**.
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
`scripts/loop/vuelta191_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 190: `b393347f`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 190: LA 189 REPRODUJO ENTERA Y LA BATERIA CORRIO DE VERDAD, PERO TUMBO UNO DE LOS SEIS DISCUTIBLES. Gate 0 verde entero corrido por mi, marcador recomputado del archivo (3.388, A 551, B 72, C 5, D 2.760, 0 huecos, 0 duplicados, sha256 LF 0a77b5a35a962621) y cabecera recomputada (3.853/3.169/684, aristas 8.780/8.740/17.520/9.914). Los DIEZ tramos de la bateria sellados, ninguno de cero bytes, 125 entradas cada una una sola vez, y el rojo que declara REPRODUCE bajo mi mano: vuelta172_tarea5_mutacion_cierre.py exit 1, fallos=2. La idempotencia del registrador, que es el remedio de mi propia C.2 de ayer, la probe re corriendola: no escribe nada y PENDIENTES.md se queda en 961248 bytes. 230 rutas barridas, CERO de cero bytes; 12 parejas de bytes, las 12 calzan.'
- **DESFASE DECLARADO, SEPTIMA VUELTA:** la linea de arriba nombra el acta
  **190** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 191**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque no es ninguna de sus cinco tareas y el encargo nombra una a
  una las que quedan fuera. Se declara en vez de colarse.
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V191_HEAD_APERTURA.txt`: `d21d5e8b`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `df038ec9`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **190**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 191`. **Esta
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
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 191 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus NUEVE adjudicaciones `4.1` a `4.9`, QUE ESTA VEZ SI SON NUEVE A FAVOR: seis son los discutibles del ejecutor (`D.1` a `D.6`) y los seis van A FAVOR, y las tres restantes (`4.7`, `4.8`, `4.9`) son las tres preguntas contestadas. EL CERO DE `EN CONTRA` TIENE QUE SALIR SIN QUE LA MAQUINA SE ROMPA POR NO ENCONTRAR NINGUNA, y se prueba por mutacion con un acta fabricada que SI lleve una. Mas los TRES hallazgos de la seccion 5 que no salen de ningun discutible (la marca `DISCUTIBLE MARCADO` contra la dificultad medida en `5.1`, la etiqueta del veredicto duplicada en `5.2`, y `git checkout --` que no restaura byte a byte en `5.3`), UNA caida propia del auditor de metodo ESCRITA COMO UNA Y NO OMITIDA, CERO caidas del ejecutor que acumulen con las TRES de metodo que el reporte de la 190 declara, y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos con su nota de SOLAPE TOTAL a proposito. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido, no escribe nada, y se prueba re corriendolo con la sede medida en bytes antes y despues | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DEL 3182. BLOQUEANTE. Es la deuda de credito que la TAREA 4 de la 190 dejo medida y que no se auto encargo, adjudicada A FAVOR en la `4.5` del acta 191 y encargada ahi mismo: quien encarga el doble es el auditor. EL TRAMO es la tanda de 30 puestos de `docs/loop/SALIDA_V190_T4_CIEGA.txt`, donde la discrepancia del `3182` cayo FUERA de los dudosos marcados. AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada: 30 mas 30 son 60, el doble exacto. EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO: a `vecinos()` se le pasa `evitar` con TODO lo consumido, contado de sus ficheros y no tecleado. Con `scripts/loop/aislador_de_ciega.py`, criterio escrito literal, ciega y destape en ficheros SEPARADOS, las clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y los dudosos NOMBRADOS DELANTE. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en el mismo valor por las dos convenciones | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LAS DOS CONVENCIONES DE `lineas`, QUE LLEVAN DOS VUELTAS ESPERANDO. Es la `5.1` del acta 190 y no se ha tocado. Hay instrumentos de la cadena que cuentan lineas con `len(texto.split(NL))`, que suma un elemento vacio final que no es una linea, y otros que cuentan con `texto.count(NL)`, que si calza con `wc -l`. ES UNA MEDICION ANTES QUE UN ARREGLO: (a) MIDE PRIMERO cuantos ficheros de `scripts/loop/` cuentan lineas por cada una de las dos convenciones, nombralos y publica la cifra, porque sin esa cifra el arreglo no se sabe de que tamano es; (b) DESPUES ARREGLA con la vara de las dos convenciones de BYTES que esta casa ya construyo: o se publica la pareja, o se publica la que calza con `wc -l` diciendo cual es; (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un instrumento vuelve a publicar una sola cifra de lineas por la convencion que no calza. NO SE TOCAN LOS NUMEROS YA PUBLICADOS EN REPORTES CERRADOS | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA GUARDA DEL VEREDICTO DUPLICADO EN `cerrar_reporte.py`. Es el hallazgo `5.2` del acta 191. La linea 50 del reporte de la 190 dice `**EL VEREDICTO DE UNA LINEA: **EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS...`, y la causa esta medida: `cerrar_reporte.py` en su linea 1817 compone la etiqueta y su propia salida prueba que el veredicto que se le paso YA la traia. (a) QUE `cerrar_reporte.py` CAIGA EN ROJO si el `--veredicto` que recibe ya trae la etiqueta o los asteriscos, en vez de pegarla dos veces, y que diga QUE RECIBIO y QUE ESPERABA: fallar ruidoso, sin limpiarla en silencio, porque limpiar en silencio es la otra mitad de la misma enfermedad. (b) CASO POSITIVO POR MUTACION que CAIGA si la guarda se quita. (c) EL REPORTE DE LA 190 NO SE REESCRIBE: esta cerrado y archivado byte a byte, y su etiqueta doble se queda donde esta con la explicacion al lado | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | LA MARCA `DISCUTIBLE MARCADO` CONTRA LA DIFICULTAD MEDIDA. SOLO MEDIR, Y NO TOCA NI UNA RAZON DEL ARCHIVO. Es el hallazgo `5.1` del acta 191: sobre su tanda de treinta, dos lectores independientes discrepan del archivo en los MISMOS OCHO puestos, `DISCUTIBLE MARCADO` aparece en 427 de las 3.388 filas y en CERO de esos ocho. TREINTA CASOS NO SON UNA LEY, y por eso esto es una medicion. (a) DI PRIMERO CUAL ES TU UNIVERSO Y COMO LO CONSTRUYES antes de contar nada: que ficheros de cotejo de ciega existen, de que vueltas, y cuales quedan fuera por no ser legibles con una regla unica, con la cifra de los que entran y de los que no y con sus nombres, porque un universo elegido despues de ver el resultado no sirve. (b) CUENTA sobre ese universo cuantos puestos han tumbado alguna vez a un lector, cuantos de esos llevan la marca, y cual es la tasa de la marca en el archivo entero: las tres cifras juntas o ninguna. (c) NO SAQUES LA CONCLUSION SI LA CUENTA NO LA SOSTIENE: si el universo sale pequeno, dilo y publica el tamano. (d) NO SE ESCRIBE NI UNA FILA DEL ARCHIVO | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
