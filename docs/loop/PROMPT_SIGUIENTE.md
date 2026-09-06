Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 190. Rama `pasada-unica`. FASE III, EJECUCION.

NO ES VUELTA DE BATERIA. La 189 la corrio entera y por `AUDITOR.md` 6.1 la
siguiente cae en la 194. La seccion 9 de tu reporte cierra con el HUECO
DECLARADO Y MEDIDO por su carril, con su medicion, su atribucion y su corrida.
Un hueco declarado no es un hueco escondido.

VAN CINCO SUB-TAREAS Y NO DOS. El tope temporal de la `AUDITOR.md` 6.2 se
cumplio y caduca: su disparador de salida pedia DOS vueltas seguidas cerrando su
propio reporte con `cerrar_reporte.py`, y son TRES, medidas en git y no
recordadas: la 187 (`56ec2696`), la 188 (`7302573f`) y la 189 (`f973b0bd`), las
tres con exitcode 0 en su propia vuelta y las tres archivadas en su propia vuelta
(`9a06b7c8`, `564a82f9`, `63d0c5b4`). Vuelve el tope de CINCO de la seccion 6.
Esta adjudicado en la 4.10 del acta 190.

ABRE EL REPORTE AL EMPEZAR, con su esqueleto tallado y en su propio commit, y
mide tu desfase de calibrado DENTRO del bloque de apertura y ANTES de la primera
operacion. Una columna de apertura medida al cierre es caida que ACUMULA.

=============================================================================
TAREA 1. LOS REGISTROS. BLOQUEANTE.
=============================================================================

El acta 190 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, computado y no tecleado (hoy el siguiente
libre es `R.52`, pero lo dice el instrumento, no este encargo).

La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta, no de
aqui:

  - LAS DIEZ ADJUDICACIONES `4.1` a `4.10`.
  - QUE NO SON DIEZ A FAVOR. Seis son los discutibles del ejecutor y de esos
    CINCO van A FAVOR (`D.1`, `D.2`, `D.3`, `D.4`, `D.6`) y UNO EN CONTRA: el
    `D.5`, la guarda del sujeto congelado fuera del veredicto. Si tu registrador
    cuenta "seis A FAVOR" por herencia del vocabulario de la vuelta pasada, esta
    contando mal: la marca de EN CONTRA tiene que existir y tiene que salir en la
    cuenta. Pruebala por mutacion con un acta fabricada.
  - LAS TRES PREGUNTAS CONTESTADAS (`4.4` la `P.1`, `4.8` la `P.2`, `4.9` la
    `P.3`).
  - LOS DOS HALLAZGOS DE LA SECCION 5 QUE NO SALEN DE NINGUN DISCUTIBLE: las dos
    convenciones de `lineas` (`5.1`) y las ocho actas sin entrada propia (`5.2`).
  - CERO CAIDAS PROPIAS DEL AUDITOR, ESCRITO COMO CERO Y NO OMITIDO, y TRES del
    ejecutor, las tres DE METODO y ninguna de racha.
  - LA VARA CORRIDA POR EL AUDITOR (`5.4`), con sus cifras.

EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE. El de la 189 lo es y esta probado: re
correrlo dice `NO SE ESCRIBE NADA` y deja `docs/PENDIENTES.md` en sus 961248
bytes. No lo pierdas al clonarlo, y re correlo tu mismo para probarlo, con la
sede medida antes y despues.

=============================================================================
TAREA 2. LA GUARDA DEL SUJETO CONGELADO: SEPARA LA DEUDA DEL FALLO, Y VUELVE
AL VEREDICTO.
=============================================================================

Son las adjudicaciones `4.4` y `4.6` del acta 190, y las dos mitades van juntas
porque una sin la otra no sirve.

(a) `guarda_del_sujeto_congelado()` SEPARA EN SU SALIDA las entradas
    `NO DECIDIBLE` que traen MOTIVO ESCRITO de las que no lo traen, y publica LAS
    DOS CIFRAS con sus nombres. Hoy "3 entradas sin congelar" no distingue una
    deuda de una decision, y esa es la `P.1` que el acta 189 dejo encargada en su
    `4.7`. Las tres de hoy son `vuelta186_tarea2c_mutacion_cierre_tardio.py`,
    `vuelta187_tarea4_mutacion_dos_convenciones.py` y
    `vuelta188_tarea4_mutacion_cobertura_parejas.py`: mide cuantas de las tres
    traen motivo escrito, no lo supongas.

(b) LA GUARDA VUELVE AL VEREDICTO del instrumento de la nomina. El `D.5` de la
    189 la saco y el acta 190 lo TUMBA: publicar los tres nombres arriba y cerrar
    en verde deja sin sintoma al que solo mire el veredicto, y eso es convertir
    una deuda visible en una exencion, que es lo que la `4.7` del acta 189
    advirtio expresamente. Con la separacion de (a) puesta, el veredicto ya puede
    decir ROJO POR DEUDA DECLARADA distinto de ROJO POR FALLO, sin dejar de ser
    rojo.

NO SE AFLOJA NINGUNA GUARDA PARA CONSEGUIR ESTO. Si al volver al veredicto algo
cierra en rojo, ese rojo se trae con su nombre y no se apaga.

Con simulacion previa sobre copia en memoria y caso positivo por mutacion.

=============================================================================
TAREA 3. LA BATERIA: QUE SU EXITCODE SEPARE, Y QUE RESTAURE SOLA LO QUE PISA.
=============================================================================

Las dos mitades tocan el mismo lanzador, por eso van en la misma tarea. Son las
adjudicaciones `4.4` y `4.9` del acta 190. NO SE CORRE LA BATERIA en esta vuelta:
se arregla su lanzador y se prueba con sus arneses, nada mas.

(a) EL EXITCODE SEPARA. Hoy los diez tramos de la 189 salieron con exitcode 1 y
    en NUEVE de ellos no cayo ni un arnes: la fuente era siempre la guarda de
    nomina en deuda. Un unico `1` para un arnes caido y para una deuda declarada
    es degradacion silenciosa (banco 9). Que el lanzador distinga los dos casos en
    su salida sellada y en su codigo de salida, y que lo diga con su cifra.

(b) LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, como ya
    restaura `dataset/`. Es la `4.9`: una salida sellada es la prueba de la vuelta
    que la sello, y dejar que una corrida posterior la pise borra el registro.
    En la 189 piso TRES (`SALIDA_V184_T1C_MUTACION_ESTIMACION.txt`,
    `SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt` y
    `SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt`) y las restauro una persona a
    mano, en dos vueltas distintas y a dos personas distintas. La restauracion va
    EN LF, que es la convencion de la casa en disco.

    Y SI EL CORTE NUEVO INTERESA, SE ESCRIBE AL LADO CON NOMBRE NUEVO Y SU
    VUELTA, nunca encima. Esa es la respuesta entera a tu `P.3`.

Con simulacion previa y caso positivo por mutacion que CAIGA si una salida
sellada ajena se queda pisada.

=============================================================================
TAREA 4. LA RELECTURA AL DOBLE DEL TRAMO DEL PUESTO 2422.
=============================================================================

ES UNA DEUDA DEL ACTA 189 Y NO SE SALTA DOS VUELTAS SEGUIDAS. La 189 la aplazo
con razon (era vuelta de bateria y `AUDITOR.md` 6.1 dice que la bateria va sola),
pero la razon ya no vale hoy.

El acta 189 encontro la discrepancia del puesto `2422` FUERA de sus dudosos
marcados, y la letra de `AUDITOR.md` 1.2 dice que eso baja el credito de la tanda
y obliga a releer ese tramo AL DOBLE. Corre la relectura con
`scripts/loop/aislador_de_ciega.py`, sobre los vecinos deterministas del `2422`,
con el criterio escrito, la ciega y el destape en ficheros separados, y las clases
escritas ANTES de abrir el destape. Publica cuantos coinciden y cuantos discrepan.

NO TOQUES NINGUNA CLASE del archivo. Si de la relectura sale una correccion, se
declara y se trae; no se escribe sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` en
esta vuelta. El `sha256` LF del archivo abre y cierra en `0a77b5a35a962621`.

=============================================================================
TAREA 5. LA SEDE DE `OP-L-02`: BUSCARLA, NO INVENTARLA.
=============================================================================

Es la `4.1` del acta 189, y la vara del acta 190 (`5.4`) la confirma medida:
corrida con `--corte 63d0c5b4` da 71 fichas, 6 en LISTA sin ninguna prueba, 2 de
ellas CONSUMIDAS por `OP-U-01` y 4 de TRABAJO REAL; de esas cuatro, tres son
mesas cuyo producto documental SI existe en disco, y `OP-L-02` es LA UNICA SIN
DOCUMENTO QUE MEDIR, con 0 menciones de fichero en su evidencia.

Su `verificacion` habla de "las tres nominas afectadas" y de "cada grupo del
backlog". BUSCA SI ESAS TRES NOMINAS TIENEN SEDE EN EL REPO, con tus propios
comandos, y publica la busqueda entera: que buscaste, donde, y que encontraste.

Y AQUI ESTA EL LIMITE, ESCRITO PARA QUE NO SE CRUCE: si la busqueda no encuentra
sede en ninguna parte, ESO ES EL RESULTADO Y SE PUBLICA COMO TAL. NO le inventes
una sede a la ficha, ni la declares HECHA, ni la muevas de estado: inventarle una
sede es cambiar el alcance de la campana, y eso lo reserva el fundador. En ese
caso lo traes y el auditor lo eleva.

=============================================================================
LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE PIERDA
=============================================================================

Cinco es el tope y estas seis quedan FUERA a proposito, nombradas para que la
vuelta 191 las encuentre escritas y no haya que redescubrirlas:

  1. LAS DOS CONVENCIONES DE `lineas` (acta 190, `5.1`). El registrador cuenta con
     `len(texto.split(NL))` y publica 2231 donde `wc -l` da 2230;
     `cerrar_reporte.py` cuenta con `texto.count(NL)` y calza. Hay que igualar los
     instrumentos o declarar la convencion en cada cifra, como ya se hizo con los
     BYTES.
  2. `acumulan()` CONTRA LA TABLA (acta 190, `4.2`). Que lea la tabla de credito o
     que declare en su salida que no es la sede.
  3. EL COTEJO DE CLON DECLARADO QUE SEPARA (acta 189, `4.8`). Dos cifras:
     sentencias del original que sobreviven identicas, y sentencias nuevas del
     clon; rojo SOLO cuando alguna del original no sobrevive.
  4. LA EXCEPCION QUE PUBLICA SIEMPRE SU LISTA, AUNQUE ESTE VACIA (acta 189,
     `4.4`). Una puerta que solo se ve cuando se usa no se puede auditar.
  5. LA MEDICION DEL CENSO DE ARNESES SIN FICHERO (acta 190, `4.8`). PRIMERO se
     cuenta cuantos instrumentos traen carril `--mutacion` sin fichero que los
     represente y se publica esa cifra; DESPUES se cambia el censo. No al reves.
  6. LAS OCHO ACTAS SIN ENTRADA PROPIA EN LA SERIE (acta 190, `5.2`): 173, 174,
     175, 176, 177, 178, 179 y 180, entre el `R.42` y el `R.43`.

Y SIGUEN FUERA, COMO EN LA 189: el cribado, el recomputo, las operaciones del
plan que no sean la busqueda de la `TAREA 5`, las mesas anotadas, y PODAR LA
NOMINA, que el fundador RECHAZO el 5 sep 2026. La nomina sigue creciendo y nadie
la poda sin el fundador.

=============================================================================

Las guardas de siempre, y ninguna se afloja: simulacion previa sobre copia en
memoria, caso positivo por mutacion en cada instrumento nuevo, Gate 0 y las
suites en verde tras cada tarea, `git diff --numstat -- dataset/` medido al
entrar y al salir con las DOS cifras publicadas, y el reporte cerrado por
`scripts/loop/cerrar_reporte.py` con sus cuatro piezas y archivado en tu misma
vuelta. Los tamanos van en BYTES EXACTOS leidos del instrumento, nunca
redondeados, y los KB solo entre parentesis y detras del byte.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
