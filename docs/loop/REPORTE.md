# REPORTE DE LA VUELTA 192 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta192_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
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
> **VAN CINCO SUB-TAREAS Y DOS SON BLOQUEANTES. El tope de cinco no hace falta
> volver a ganarlo:** esta vigente desde la `4.10` del acta 190. **Y la cifra que
> lo sostiene se REMIDIO en esta vuelta en vez de heredarse**, tal como el encargo
> manda: el bloque **B.2** del sello de apertura busco en git los commits de
> cierre y midio sus ficheros `SALIDA_V<n>_CERRAR_REPORTE.txt` uno a uno, **y
> cuando vi que mi ventana estaba tecleada escribi un instrumento que cuenta del
> inventario ENTERO**, `scripts/loop/vuelta192_racha_de_cierres.py`. Las cifras
> que andan dando vueltas se publican JUNTAS en la seccion 0.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT.** Desde
> el segundo commit de esta vuelta ya hay reporte parcial en el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**), ni la bateria, que cae en
> la 194. **Y siguen fuera, nombradas para que la 193 no las redescubra:** el
> desfase de `PATRONES_ACTA`, **que se encarga DESPUES de la 194** porque toca
> `tallar_cabecera_reporte.py` y cuatro entradas de la nomina lo nombran;
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
`scripts/loop/vuelta192_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 191: `d21d5e8b`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer
  DENTRO cifras de bytes y `sha256` suyas, y una guarda que mira renglon a
  renglon no distingue una cita de una afirmacion. Cercarlo es decir lo que es:
  **una cita de la salida de un instrumento**.

```
'ACTA DEL AUDITOR, VUELTA 191: LA 190 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA NI UNA RUTA VACIA.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA.** La linea de arriba nombra el
  acta **191** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 192**. Es el `D.2` del reporte de la 184, adjudicado
  a favor con reparacion encargada por la `5.2` del acta 185, **y la `4.7` del
  acta 192 lo deja expresamente DESPUES de la bateria de la 194**. El reporte de
  la 191 se llama a si mismo **la SEPTIMA vuelta** del desfase; **esa palabra no
  sale de ningun instrumento, asi que aqui no se copia ni se le suma uno a ojo**:
  lo que si se puede contar es que **3 reportes archivados traen el
  literal `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`), contados por
  `reportes_con_el_literal()` de este mismo fichero. **LAS DOS CIFRAS SE PUBLICAN
  Y LA DISCREPANCIA SE DECLARA EN VEZ DE RESOLVERSE COPIANDO.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V192_HEAD_APERTURA.txt`: `485c2f3e`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `3470f651`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **191**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 192`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 19 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **0 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 192 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Con sus DIEZ adjudicaciones `4.1` a `4.10`, y las diez A FAVOR: siete son los discutibles del ejecutor (`D.1` a `D.7`, cuya numeracion en el reporte de la 191 va con el `D.7` escrito ANTES del `D.6`) y las tres restantes son las preguntas y los pendientes de doctrina contestados. OTRA VEZ CERO EN CONTRA, y si el arnes de la 191 ya cubre ese cero, SE DICE CON SU FICHERO en vez de re fabricarlo. Mas los TRES hallazgos de la seccion 5 que no salen de ningun discutible (los dos arneses `SUJETO VIVO` en `5.1`, la cuarta puerta del sello en `5.2`, y el segundo dato independiente sobre la marca contra la dificultad en `5.3`), DOS caidas propias del auditor escritas COMO DOS y ninguna omitida (la `C.1` es DE CIFRA PUBLICADA y va corregida por DECLARACION; la `C.2` es de metodo), CERO caidas del ejecutor que acumulen con las SEIS de metodo que el reporte de la 191 declara, y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos con su nota: 30 aislados y 28 cotejados, SOLAPE TOTAL a proposito. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada, y se prueba re corriendolo con la sede medida en bytes antes y despues | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DE LA 191. BLOQUEANTE. La encarga el AUDITOR, que es donde `AUDITOR.md` 1.2 la pone, y esta vez CON MOTIVO DOBLE: el puesto `2832` cayo FUERA de los dudosos marcados de DOS lectores independientes en DOS tandas seguidas, la del ejecutor en la 191 y la del auditor en la 192. EL TRAMO son los 30 puestos de `docs/loop/SALIDA_V191_T2_CIEGA.txt`, que el bloque `H.3` del sello de apertura midio como el MISMO conjunto que `docs/loop/_auditor_v192_ciega_blind.txt`. AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada: 30 mas 30 son 60, el doble exacto. EL SOLAPE SE LE EXIGE AL UNIVERSO Y NO AL TRAMO: a `vecinos()` se le pasa `evitar` con TODO lo consumido, contado de sus SEIS ficheros y no tecleado. Con `scripts/loop/aislador_de_ciega.py`, criterio escrito literal, ciega y destape en ficheros SEPARADOS, las clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y los dudosos NOMBRADOS DELANTE. Y SI EL TRAMO VUELVE A TUMBAR A LOS DOS LECTORES EN LOS MISMOS PUESTOS, SE DICE CON SUS NUMEROS. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en el mismo valor por las dos convenciones | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 3** | LOS DOS ARNESES `SUJETO VIVO` DE LA 191, ANTES DE QUE ENTREN EN LA NOMINA. BLOQUEANTE, Y LO ES POR LA BATERIA DE LA 194. Es el hallazgo `5.1` del acta 192, corrido con la guarda de la casa y medido en `docs/loop/_auditor_v192_sujeto_vivo.txt`. (a) CORRER LA GUARDA `guarda_del_sujeto_congelado_separada()` y publicar sus TRES listas sobre los doce arneses de la 191, con sus nombres: si la medicion no da 2 y 6, la del ejecutor manda y la del auditor se declara equivocada, que para eso se publica el comando. (b) ARREGLAR LOS DOS `SUJETO VIVO` para que su sujeto quede CONGELADO, o DECLARAR EL CASO por el carril de los `CASO DECLARADO` que la casa ya tiene: la `4.4` del acta 191 adjudico que `SUJETO VIVO` es FALLO y no deuda, asi que dejarlos como estan no es opcion. (c) LOS SEIS `sin_motivo` NO SON FALLO PERO SI SON DEUDA: nombrarlos y decir, por cada uno, si su sujeto esta vivo de verdad o si solo le falta escribir el motivo, sin arreglarlos a ciegas. (d) NO SE TOCA LA NOMINA: no se poda, no se adelanta y no se le meten entradas nuevas, que la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. (e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes con sujeto vivo vuelve a colarse hacia la nomina sin declararse | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 4** | LA CUARTA PUERTA DEL SELLO DE LA APERTURA DEL AUDITOR. Es el hallazgo `5.2` del acta 192, levantado por el auditor CONTRA SI MISMO. `scripts/loop/apertura_del_auditor.py` impide tocar `git log`, `git status` y `REPORTE.md` antes del sello, y eso FUNCIONO; pero EL SUJETO DE LA CIEGA NO VIVE EN NINGUNO DE LOS TRES: vive en las razones y las clases de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y por ahi se colo el auditor de la 192 con el sello ya escrito y sin romper ninguna guarda (los puestos 156 y 201 de su propia tanda). (a) AL SELLO SE LE ANADE LA CUARTA PUERTA: una funcion del propio fichero para leer el archivo que APUNTE SU TOQUE, y una comprobacion que CAIGA EN ROJO si el turno leyo `clase` o `razon` DE LOS PUESTOS SELLADOS antes de que las clases del auditor esten escritas. No se prohibe leer el archivo entero, que hace falta para el marcador: se prohibe destapar el sujeto. (b) DECIR EN EL PROPIO FICHERO LO QUE ESTA GUARDA NO PUEDE HACER, como su docstring ya hace con las otras tres. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si la cuarta puerta se quita. (d) NO SE CLONA EL FICHERO: `apertura_del_auditor.py` tiene nombre estable y sin numero de vuelta, y se le anade, no se le hace una version 2 | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | EL FORMATO UNICO DEL COTEJO DE CIEGA. Es el `P.2` del ejecutor, adjudicado A FAVOR en la `4.9` del acta 192. La TAREA 5 de la 191 midio que el universo se queda en 6 ficheros de 43, y tres cotejos de ciega DE VERDAD (los del 183, 184 y 190) quedan fuera POR FORMATO y no por fondo. ES UN FORMATO ANTES QUE UNA RE MEDICION: (a) ESCRIBIR EL FORMATO UNICO del cotejo de ciega, con nombre estable y sin numero de vuelta, que lleve como minimo y explicitos el puesto, la clase del lector, la clase del archivo, si el puesto estaba en los dudosos del lector, y el COINCIDE o DISCREPA, y que deje el DENOMINADOR RECUPERABLE, porque dos de los seis ficheros de hoy solo listan discrepancias. (b) UN LECTOR QUE LEA LOS FORMATOS VIEJOS y publique CUANTOS de los 43 pasa a recuperar, con sus nombres, y cuantos siguen fuera y por que, con la cifra de antes y la de despues LAS DOS JUNTAS. (c) NO SE RE MIDE LA MARCA CONTRA LA DIFICULTAD EN ESTA VUELTA: el universo nuevo se usa cuando este medido y declarado, no en el mismo acto en que se construye. (d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un cotejo del formato nuevo no permite recuperar el denominador | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
