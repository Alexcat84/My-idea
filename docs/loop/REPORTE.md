# REPORTE DE LA VUELTA 189 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta189_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE, no al final; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`.
> **Si esta vuelta se corta, lo que quede aqui es lo que de verdad se hizo, y las
> filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se hicieron.**
>
> **ESTA VUELTA SI ES DE BATERIA, Y POR ESO LLEVA DOS TAREAS Y LA SEGUNDA ES LA
> BATERIA SOLA.** `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la
> bateria de mutaciones **corre CADA CINCO VUELTAS**, en una vuelta propia que
> **no lleva nada mas**. **Cerro entera en la 184**, asi que la siguiente es
> esta. Su seccion 9 **no cierra con hueco declarado**: cierra con la bateria
> corrida, sus tramos sellados y su salida compuesta.
>
> **Y LA BATERIA DE ESTA VUELTA NO HEREDA NI UNA SALIDA SELLADA DE LA CORRIDA
> 183/184.** El acta 189, seccion 5, midio que
> `scripts/loop/vuelta183_bateria_por_tramos.py` **ya no reparte en nueve tramos
> sino en DIEZ** (la nomina paso de 121 a 125) y que su `--siguiente` dice hoy
> **"EL SIGUIENTE ES EL TRAMO 10"**: correrlo tal cual habria corrido **un tramo
> de diez** y se habria declarado corrido **habiendo corrido 8 arneses de 125**.
> El bloque **H.4** del sello de apertura de esta vuelta lo **reprodujo entero**
> antes de tocar nada. Por eso la bateria va con un **clon declarado**,
> `scripts/loop/vuelta189_bateria_por_tramos.py`, cuyo `--siguiente` **cuenta
> desde cero**. **Y no se borra nada:** las nueve salidas de la 183 se quedan
> donde estan.
>
> **DONDE SE TALLO ESTE ESQUELETO: EN LA APERTURA Y EN SU PROPIO COMMIT**, como
> hizo la 188. Desde el segundo commit de esta vuelta ya hay reporte parcial en
> el arbol.
>
> **LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE CUELE:** ni cribado, ni
> recomputo, ni operaciones del plan, ni las mesas anotadas, ni **podar la
> nomina** (la opcion `c` que el fundador RECHAZO el 5 sep 2026: **la nomina
> sigue creciendo y nadie la poda sin el fundador**). **No entran** la relectura
> al doble del tramo del puesto **2422**, la `P.1` en codigo, la `P.2` en codigo,
> la condicion del `D.4` ni la busqueda de la sede de `OP-L-02`: **las cinco van
> a la vuelta 190** y su encargo ya las lleva escritas. **Y no se mueve ningun
> veredicto**: el `sha256` LF del archivo abre y tiene que cerrar en el mismo
> valor. **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al
> salir y las dos cifras se publican.
>
> **Y ESTA VUELTA MIDE SU DESFASE DE CALIBRADO EN LA APERTURA, DENTRO DEL BLOQUE
> DE APERTURA Y ANTES DE LA PRIMERA OPERACION.** **Una columna de apertura medida
> al cierre es caida que ACUMULA.**

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando
haya de que hablar.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta189_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 188: `5aa9305d`, asunto real leido de git log:
  'ACTA DEL AUDITOR, VUELTA 188: LA 187 REPRODUJO ENTERA, EL PLAN SE MOVIO DE VERDAD (UNA FILA DE 3.388, EL PUESTO 2.464), ADJUDICO LOS SEIS DISCUTIBLES A FAVOR, Y LA PARADA QUE EL EJECUTOR DECLARA NO ES PARADA: LA RESUELVE SU PROPIO ENCARGO DE LA 187 Y SU REMEDIO VA BLOQUEANTE PORQUE LA BATERIA ES LA 189.'
- **DESFASE DECLARADO, QUINTA VUELTA:** la linea de arriba nombra el acta
  **188** porque `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que
  ORDENA esta vuelta es la 189**. Es el `D.2` del reporte de la 184, adjudicado a
  favor con reparacion encargada por la `5.2` del acta 185. **Esta vuelta no la
  ejecuta** porque su encargo dice con todas las letras *NADA MAS ENTRA EN ESTA
  VUELTA*. Se declara en vez de colarse.
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V189_HEAD_APERTURA.txt`: `bbeea713`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `b4f8b23c`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **188**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva**, porque ese commit se crea despues de escribirlo.

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 189`. **Esta
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
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 189 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, con sus DIEZ adjudicaciones `4.1` a `4.10` mas la adjudicacion de la seccion 5 (la bateria corre entera), las SEIS primeras (`4.1` a `4.6`) que son los seis discutibles del ejecutor y las seis A FAVOR, las TRES preguntas contestadas (`4.7`, `4.8`, `4.9`), DOS caidas propias del auditor (`C.1` y `C.2`) las dos DE METODO y NINGUNA DE RACHA, y CERO caidas del ejecutor REGISTRADAS COMO CERO Y NO OMITIDAS. Mas la correccion declarada del auditor sobre su propia sede (`4.9`: el acta 188 escribio "de `LD-01` hasta `LD-98`" y la cifra buena medida hoy es 68 etiquetas distintas con maximo `LD-154`), SIN BORRAR EL TEXTO VIEJO; y la racha de reporte CORTADA Y DE VUELTA A 0 por la `4.10`, con las DOS cifras, la vieja del acta 188 y la nueva. Con caso positivo por mutacion sobre un acta FABRICADA y su esperado mutado cayendo, y con la PARADA conservada entera. Y EL REGISTRADOR NACE IDEMPOTENTE, que es lo que sale de la `C.2` del acta: comprueba primero si el acta que se le pide YA TIENE ENTRADA, por su cabecera literal y no por el numero, y si la tiene SALE SIN ESCRIBIR Y LO DICE CON SU CIFRA, con su propio caso positivo por mutacion | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 2** | LA BATERIA DE MUTACIONES, ENTERA, POR TRAMOS Y SOLA. Primero el CLON, que es bloqueante: `scripts/loop/vuelta189_bateria_por_tramos.py`, clon declarado de `vuelta183_bateria_por_tramos.py`, cotejado con `scripts/loop/cotejar_clon_declarado.py` y con la salida del cotejo pegada, porque el de la 183 ya reparte en DIEZ tramos y su `--siguiente` diria hoy EL SIGUIENTE ES EL TRAMO 10: correrlo tal cual haria UN tramo de diez y declararia la bateria corrida habiendo corrido 8 arneses de 125. La bateria de esta vuelta CORRE ENTERA sobre la nomina de hoy y NO HEREDA NI UNA SALIDA SELLADA de la corrida 183/184, y no se borra ninguna de las nueve. Despues la bateria tramo a tramo: `--plan` con el reparto computado y no tecleado, cada tramo con `--tramo N` sellado y COMMITEADO antes del siguiente, doble corrida con cotejo de reproducibilidad, la exclusion de los arneses ya en rojo DICHA en su salida, el reloj con la estimacion del `--plan` y la medicion de verdad al cerrar cada tramo, y `--componer` al final. LA BATERIA SE DECLARA CORRIDA CUANDO LOS DIEZ TRAMOS TIENEN SALIDA SELLADA DEL MISMO CALIBRE, y una salida sellada de CERO BYTES no cuenta como hecha | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->
