# REPORTE DE LA VUELTA 214 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v214_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 213.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **TRES TAREAS, Y LA 214 NO ES VUELTA DE BATERIA.** La cadencia de cinco de
> `AUDITOR.md` 6.1 pone la bateria en la **215**, y la TAREA 3 de esta vuelta es
> justamente prepararla. **El tope de sub-tareas es CINCO** (acta 212,
> adjudicacion `6.8`, **linea 75168** de `docs/loop/ACTA_AUDITOR.md`, leida en
> esta vuelta), asi que las tres del encargo caben.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las tres tareas son trabajo de PLAN**, que
> es lo que la moratoria protege. Todo lo que esta vuelta escribe en el arbol
> scripts/loop (**sin comillas inversas, por la obligacion del `6.2` del acta
> 212**) son ficheros `_v214_*` **con prefijo de guion bajo, fuera del censo y
> fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se poda.
>
> **RIGE LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion `6.2`, **y es la `C.1` que esta vuelta no repite**); una seccion
> suplementaria va detras de la que amplia y nunca detras de una mayor (hallazgo
> `7.1`); y el tallador de cabecera corrido en la apertura escribe en un nombre
> con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V214_APERTURA.txt`,
> `docs/loop/SALIDA_V214_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 214`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LAS 95 SE DICEN, Y `OP-I-01` CIERRA (DECISION 1 del fundador). Marcar PROVISIONAL POR INSTRUMENTO, nunca a mano, exactamente las entradas de `docs/plan/INVENTARIO.jsonl` con forma N de M INCOMPLETA, con conteo ANTES y DESPUES; si el instrumento marca un numero distinto de 95, se PARA y se trae. Correccion DECLARADA citando el banco `9.26` y la decision del fundador POR SU RUTA. Y re-medir el punto 2 de `OP-I-01` a CUBRE, cerrando la ficha CON SU PRUEBA por la vara del expediente y su verificacion, SIN escribir el campo estado | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 2** | LA VARA DE LAS TRES FASES (DECISION 2 del fundador). La tabla del criterio de HECHO de `docs/plan/08_VERIFICACION.md` gana sus filas para las fases 08, 09 y 10, DERIVADAS de las clausulas de verificacion que las propias fichas traen y cada fila CON SU CITA, por correccion declarada. Y las CINCO fichas sin ejecutar se re-miden contra esas filas con el resultado escrito ficha por ficha (`OP-V-01`, `OP-L-01`, `OP-L-02`, `OP-L-03`, `OP-I-01`), con la `OP-V-01` llevando su prueba POR CITA de la corrida K ya escrita | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 3** | PREPARAR LA VUELTA 215, que es VUELTA DE BATERIA por la cadencia de cinco (`AUDITOR.md` 6.1) con la nomina CONGELADA EN 135 y por TRAMOS RESUMIBLES, y que lleva ademas el CIERRE INTEGRAL del bucle sin credencial: ciclo entero de Gate 0, las tres suites, el inventario de las 71 contra sus pruebas, y el marcador y el censo recomputados. La propuesta va EN ESTE REPORTE y no en la sede del auditor (doctrina de sedes del acta 203, ratificada por el fundador): el reparto de los tramos se COMPUTA con el lanzador y no se teclea, y la condicion de la PARA_ALEXIS.md de campaña consumada se deja escrita con su clausula de que NO se pide el merge | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

