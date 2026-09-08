# REPORTE DE LA VUELTA 208 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v208_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no se
> hicieron.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, Y ESO ES EL REMIENDO DE MI
> `C.1` DE LA 207.** Aquella vuelta tallo su esqueleto sin la marca de apertura de
> la tabla de tareas, sin la del anexo y sin sus dos cierres, y hubo que ponerselas
> a mano despues con `_v207_marcas_anexo.py`. **Aqui no se teclean: se IMPORTAN de
> `anexar_tarea_al_reporte.py`**, que es el instrumento que las lee, y se comprueba
> ANTES de tallar que es lo que ese instrumento exige. **Las cuatro no se citan
> literalmente en esta prosa a proposito**: la guarda las cuenta sobre el fichero
> entero, y una cita en prosa las duplicaria. Es lo que esta corrida cazo en su
> primer intento, en rojo, y por eso la prosa las nombra en vez de copiarlas.
>
> **EL REPORTE DE LA 207 TAMPOCO ESTABA ARCHIVADO AL ENTRAR, Y ESO SE DECLARA EN
> VEZ DE COPIARSE** (`EJECUTOR.md` 2, EL INSTRUMENTO MANDA). Mi sello de apertura,
> `docs/loop/SALIDA_V208_APERTURA.txt`, escrito **antes de la primera operacion**,
> publica `CIFRA docs/loop/reportes/REPORTE_V207.md existe al entrar: NO`. Lo
> archiva el PASO 0, que es su sitio, y su salida va sellada en
> `docs/loop/SALIDA_V208_PASO0_ARCHIVAR.txt`.
>
> **TRES SUB-TAREAS.** El tope volvio a CINCO (`AUDITOR.md` 6.2, adjudicacion `6.5`
> del acta 207: la 206 y la 207 cerraron las dos su propio reporte con
> `cerrar_reporte.py`), y el encargo pone TRES y no cinco porque la TAREA 2 toca una
> sede sellada del banco.
>
> **ESTA NO ES VUELTA DE BATERIA, Y ESO NO ES UNA OMISION SINO LA CADENCIA**
> (`AUDITOR.md` 6.1, adjudicacion `6.7` del acta 207). La ultima fue la **205** y
> la siguiente es la **210**. La **seccion 9 cierra igual**, con el **HUECO
> DECLARADO Y MEDIDO** y sus **tres piezas juntas**: el nombre del fichero, los
> bytes medidos **distinguiendo el cero de ausencia del cero de fichero vacio**, y
> la atribucion.
>
> **Y RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Todo lo que esta vuelta
> escribe son ficheros `_v208_*` **con prefijo de guion bajo, fuera del censo y
> fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda. **EL
> TRABAJO ES EL PLAN**, y por eso las TAREAS 2 y 3 son mesas del plan.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 208`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TRES TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS DE LA VUELTA 207. Leer el acta 207 entera y REMEDIR sus cifras de crecimiento; escribir `R.72` en `docs/PENDIENTES.md` **por adicion pura y en su sede**, con el numero COMPUTADO por `scripts/loop/serie_de_registros.py` y las dos puntas publicadas; registrar **las ocho adjudicaciones** `6.1` a `6.8` por su numero y su linea, con la vara del `4.1` del acta 202 corrida por mi; y CORREGIR LA CAIDA `4.1` DEL AUDITOR CONTRA MI en el reporte ARCHIVADO de la 207, por CORRECCION DECLARADA y con el texto viejo entero encima | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 2** | LA `TABLA VIVA DE LOS PUROS` DE `docs/BANCO_DE_TEXTOS.md`, PUESTA AL DIA POR EL CARRIL DEL BANCO `9.10`. **Primero el DENOMINADOR** de las dos nominas, recomputado de su nomina de miembros y no de la tabla; despues las dos filas escritas por CORRECCION DECLARADA con el texto viejo entero encima; y la `V.3` de la vara de `OP-L-01` dejada MEDIDA con su cita. **NO SE CIERRA `OP-L-01` Y NO SE TOCA SU CAMPO `estado`** | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 3** | LA MESA `OP-L-03`, MEDIDA CONTRA LOS DOCUMENTOS QUE SU FICHA NOMBRA, POR EL MISMO METODO QUE LA `OP-L-01` DE LA 207. La vara SELLADA EN SU PROPIO COMMIT antes de abrir ningun documento, con cada cita comprobada VERBATIM y el reparto documental sellado antes de mirar; el cotejo punto por punto con CUBRE, A MEDIAS o NO CUBRE **y su cita de fichero y linea**; la cobertura MEDIDA y no narrada. **NO SE CIERRA LA FICHA Y NO SE TOCA SU CAMPO `estado`** | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

