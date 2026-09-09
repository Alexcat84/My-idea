# REPORTE DE LA VUELTA 216 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v216_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 215.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **CUATRO TAREAS, Y LA 216 NO ES VUELTA DE BATERIA Y NO LA CORRE.** La 215 la
> corrio entera y el auditor la declaro CORRIDA en su adjudicacion 5.1; la
> cadencia de cinco de `AUDITOR.md` 6.1 pone la siguiente en la **220**. La
> seccion 9 de este reporte cierra por tanto con el **HUECO DECLARADO Y MEDIDO**
> por el carril de la TAREA 1.b de la vuelta 173, que es lo que la 6.1 manda en
> las vueltas intermedias. **El tope de sub-tareas es CINCO** (acta 212,
> adjudicacion 6.8, **linea 75168** de `docs/loop/ACTA_AUDITOR.md`, leida en esta
> vuelta), y **estas cuatro no lo agotan porque el encargo dice que no hacen
> falta mas**.
>
> **ESTA VUELTA CORRE LA UNICA COSA QUE LE QUEDA AL PLAN, Y NO ES DEL AUDITOR: LA
> ORDENO EL FUNDADOR.** Su sede es
> `docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, DECISION 2, y su letra
> verbatim es *"las cinco fichas SIN EJECUTAR se re-miden contra esas filas
> (OP-V-01 con su prueba por cita de la corrida K ya escrita)"*. **La re-medicion
> es la TAREA 2 y es bloqueante.**
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las cuatro tareas son MEDICION y
> VERIFICACION**, que es lo que la moratoria protege. Todo lo que esta vuelta
> escribe en el arbol scripts/loop (**sin comillas inversas, por la obligacion del
> 6.2 del acta 212**) son ficheros `_v216_*` **con prefijo de guion bajo, fuera
> del censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se
> poda.
>
> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL
> CAMPO DE ESTADO DE NINGUNA FICHA.** La vara del trabajo pendiente es el
> instrumento y nunca ese campo (recuadro de `AUDITOR.md` 0, decision del fundador
> del 4 sep 2026). Se mide, se publica y se dice. **No se escribe.**
>
> **RIGE LA OBLIGACION DE DICTADO DEL 6.6 DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion 6.2); una seccion suplementaria va detras de la que amplia y nunca
> detras de una mayor (hallazgo 7.1); y el tallador de cabecera corrido en la
> apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V216_APERTURA.txt`,
> `docs/loop/SALIDA_V216_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y el remedio de la
> 215 se mantiene y no se afloja: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V216_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del
> fichero ausente y la del fichero de cero bytes.**

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 216`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA. Leer el acta de la vuelta 215 en `docs/loop/ACTA_AUDITOR.md`, sus secciones 3, 5 y 6, y REGISTRAR LAS OCHO ADJUDICACIONES DE LA 5.1 A LA 5.8 CON LA LINEA DE DONDE SALE CADA UNA, leida con un instrumento y no tecleada; las cuatro que obligan van con DOS COLUMNAS SEPARADAS, el titulo VERBATIM y la lectura mia. Y registrar las DOS CORRECCIONES DECLARADAS del auditor con su cifra, y su UNICA CIFRA MALA, que es suya y se escribe igual | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 2** | LA RE-MEDICION QUE EL FUNDADOR ORDENO EL 9 SEP 2026, Y ES EL CORAZON DE ESTA VUELTA Y ES BLOQUEANTE. Sacar CON UN INSTRUMENTO las clausulas de las CATORCE filas de derivacion de `docs/plan/08_VERIFICACION.md`, publicar cuantas filas se armaron y cuantas deberia haber EN LA MISMA LINEA, y medir cada una con su busqueda corrida y su cifra delante, incluidas las que dan cero. La ficha OP-V-01 tiene trato propio por la DECISION 2: su prueba va POR CITA DE LA CORRIDA K YA ESCRITA, y si no aparece, ESO TAMBIEN ES UN RESULTADO. Y el caso rojo se prueba POR MUTACION, en memoria y sin escribir en ninguna ficha | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 3** | LA CONSECUENCIA, MEDIDA Y SIN TOCAR UN SOLO CAMPO DE ESTADO. Publicar ficha por ficha cuantas clausulas quedan en CUBRE para las CINCO; volver a correr la vara `scripts/loop/vuelta150_3_relectura_expediente.py` con el hash de MI apertura y publicar MI cifra sin copiar la del auditor; PUBLICAR LAS DOS VARAS LADO A LADO sin maquillar que miden cosas distintas; y PROPONER, no declarar, si la campana queda consumada en lo que el bucle puede consumar | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 4** | EL CIERRE INTEGRAL Y EL REPORTE. El ciclo entero de Gate 0 por los dos lados con su consola SELLADA desde dentro del propio instrumento, manteniendo el remedio de la 215 y sin aflojarlo; las tres suites solas con su exitcode y sus bytes; marcador y censo recomputados cada uno con su comando; las rutas con `scripts/loop/vuelta186_rutas_del_reporte.py` corrido DESPUES de cerrar el reporte; la cabecera con su tallador y su comparacion; y el cierre con `scripts/loop/cerrar_reporte.py`, que con la 215 hacen dos seguidas | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

