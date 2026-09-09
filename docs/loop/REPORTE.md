# REPORTE DE LA VUELTA 219 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v219_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 218.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **LA OBLIGACION QUE ESTE REPORTE CUMPLIO 11 DE 11 EN LA VUELTA ANTERIOR Y TIENE
> QUE MANTENER.** Es el `6.6` del acta 210, que vive en la **linea 74203** de
> `docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero y no recordada: **toda cita
> de un acta anterior lleva SU NUMERO DE ACTA Y LA LINEA donde vive el texto
> citado, y la linea se lee del fichero**. El acta 218 la verifico una a una y
> dio **11 de 11** (acta 218, **linea 77463**). En este reporte **toda cita lleva
> su numero de acta y su linea**, y la linea se lee.
>
> **DOS TAREAS, Y LA 219 NO ES VUELTA DE BATERIA Y NO LA CORRE.** La 215 la
> corrio entera por sus once tramos. La cadencia de cinco de `AUDITOR.md` 6.1
> pone la siguiente en la **220**. La seccion 9 de este reporte cierra por tanto
> con el **HUECO DECLARADO Y MEDIDO**, con **el nombre, los bytes medidos y la
> atribucion, LAS TRES JUNTAS**, que es lo que la 6.1 manda en las vueltas
> intermedias.
>
> **EL TOPE DE SUB-TAREAS ES CINCO** (acta 212, adjudicacion `6.8`, **linea
> 75168** de `docs/loop/ACTA_AUDITOR.md`), y el encargo me da **DOS** porque lo
> que queda alcanzable por lectura cabe en dos, no porque el tope obligue.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las dos tareas son LECTURA, MEDICION y
> REGISTRO**, que es lo que la moratoria protege. Todo lo que esta vuelta escribe
> en el arbol scripts/loop (**sin comillas inversas, por la obligacion del `6.2`
> del acta 212**) son ficheros `_v219_*` **con prefijo de guion bajo, fuera del
> censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
>
> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL
> CAMPO DE ESTADO DE NINGUNA FICHA**, ni toca `docs/plan/08_VERIFICACION.md`, ni
> el inventario, ni el expediente, ni `docs/plan/07_ADUANA.md`, **cuya celda es
> sede del fundador**. Se lee, se mide, se publica y se dice. **No se escribe.**
> Los `sha256` se publican al entrar y al salir **por las dos convenciones**, y
> tienen que coincidir.
>
> **RIGE LA OBLIGACION DE LA PAREJA DE BYTES EN LA MISMA LINEA**, que es la caida
> `C.2` que mi propia guarda de `scripts/loop/cerrar_reporte.py` me canto en la
> 218 (acta 218, **linea 77664**): **cada ruta con sus dos convenciones EN SU
> MISMA LINEA**, los bytes exactos y nunca redondeados, y los KB solo entre
> parentesis y detras del byte.
>
> **RIGE LA OBLIGACION DE DICTADO DE LA CIFRA CON SU HUECO:** toda cifra de "lo
> que esta vuelta escribio" que se mida ANTES del cierre se publica **CON SU HUECO
> AL LADO, LAS DOS CIFRAS JUNTAS**, la medida y la que el propio cierre anade.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion `6.2`); una seccion suplementaria va detras de la que amplia y
> nunca detras de una mayor (hallazgo `7.1`); y el tallador de cabecera corrido en
> la apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V219_APERTURA.txt`,
> `docs/loop/SALIDA_V219_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y el remedio de la
> 215 se mantiene y no se afloja: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V219_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del
> fichero ausente y la del fichero de cero bytes.**
>
> **Y NO SE REPARA `scripts/loop/vuelta150_4_tabla_por_fase.py`.** Sigue saliendo
> con exitcode 1 y `AssertionError` porque la tabla no trae ocho filas, trae 11,
> y la moratoria `6.3` lo cubre por su propia letra. **Sube nombrado y sin
> reparar, otra vez** (acta 218, **linea 77674**).

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 219`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y ES BLOQUEANTE. Anotar que las SEIS adjudicaciones del acta 218 cayeron del lado del ejecutor y que NINGUNA mueve un veredicto, cada una con su rotulo, su numero de adjudicacion y SU LINEA LEIDA DEL FICHERO; volver a medir el recuento de las diecisiete clausulas con el mismo instrumento que el auditor reprodujo byte a byte, publicando LAS DOS CIFRAS JUNTAS, la que mido hoy y la que la 218 dejo; y anotar las SEIS cosas que suben nombradas a la auditoria integral con su cifra, sin resolver ninguna. Cero escrituras en el plan | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 2** | LAS DOS CLAUSULAS QUE TODAVIA SE PUEDEN MOVER LEYENDO, Y SON LECTURA, NO INSTRUMENTO NUEVO. En `01 FUENTES` idx 1, reproducir con mi propio instrumento las 7 menciones que aun declaran un segundo libro y contestar por cada una UNA sola pregunta, si el material de ese segundo libro vive hoy en algun nodo vivo del grafo o en ninguno, con el id que la declara, que material concreto es y donde vive hoy RESUELTO CON EL RESOLUTOR DELANTE; y en `05 SANEO` idx 1, localizar la anotacion del acta 120 y publicar SU LINEA leida del fichero, publicar por cada uno de los tres su id, si declara version de Incoterms hoy, cual y de donde sale, y dejar MARCADA COMO DISCUTIBLE la pregunta de frontera que decide la clausula. El recuento de las diecisiete se rehace AL CIERRE DE LA TAREA y la parada feliz solo se propone si las diecisiete quedan en CUBRE | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

