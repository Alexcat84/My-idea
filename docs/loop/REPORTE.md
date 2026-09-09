# REPORTE DE LA VUELTA 215 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v215_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 214.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **CINCO TAREAS, Y LA 215 SI ES VUELTA DE BATERIA.** La cadencia de cinco de
> `AUDITOR.md` 6.1 pone la bateria aqui, y el acta 214 adjudica en su **linea
> 76149** que **son ONCE tramos y no nueve**: *"LA BATERIA SE DECLARA CORRIDA CON
> TODOS LOS TRAMOS DE SU REPARTO, Y HOY SON ONCE, NO NUEVE"*. **El tope de
> sub-tareas es CINCO** (acta 212, adjudicacion `6.8`, **linea 75168** de
> `docs/loop/ACTA_AUDITOR.md`, leida en esta vuelta), y **estas cinco lo agotan**.
> La bateria cabe al lado del cierre integral porque **el cierre integral NO es
> trabajo de plan, es VERIFICACION**: esta vuelta no escribe ni un nodo, ni un
> veredicto, ni una ficha.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las cinco tareas son BATERIA y VERIFICACION**, que
> es lo que la moratoria protege. Todo lo que esta vuelta escribe en el arbol
> scripts/loop (**sin comillas inversas, por la obligacion del `6.2` del acta
> 212**) son ficheros `_v215_*` **con prefijo de guion bajo, fuera del censo y
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
> `docs/loop/SALIDA_V215_APERTURA.txt`,
> `docs/loop/SALIDA_V215_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y esta vuelta anade
> el remedio del hallazgo `3.1` del acta 214: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca.** En la 214 esa consola NUNCA EXISTIO y la
> seccion 3.1 salio publicada VACIA.
>
> **Y LA APERTURA SELLA ADEMAS DE QUE VUELTA SON LOS SELLOS DE TRAMO QUE HAY EN EL
> ARBOL AL ENTRAR**, con su commit y su fecha leidos de `git log`, que es lo que
> la TAREA 2.a manda publicar ANTES de correr nada.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
PENDIENTE DE TALLAR AL CIERRE con
`scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 215`, y pegada entera
por `scripts/loop/cerrar_reporte.py`. **LA CELDA QUE NO SALGA DE UN INSTRUMENTO NO
SE ESCRIBE.**
<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS, Y VA PRIMERA PORQUE LAS DEMAS SE APOYAN EN ELLA. Leer el acta de la vuelta 214 en `docs/loop/ACTA_AUDITOR.md`, sus secciones 3 y 5, y REGISTRAR LAS NUEVE ADJUDICACIONES CON LA LINEA DE DONDE SALE CADA UNA, aplicando como orden las cinco que el encargo nombra; y registrar el hallazgo `3.1` del auditor contra el reporte de la 214, que es la unica caida no declarada y la unica que acumula | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 2** | LA BATERIA ENTERA, POR TRAMOS, Y SIN EL FALSO VERDE. Publicar ANTES de correr nada de que vuelta son los once sellos que hay en el arbol, con su commit y su fecha leidos de git log; NO usar el carril de la senal de arranque, que hoy publica un verde que no es de esta vuelta; y correr los ONCE tramos uno a uno con su doble corrida, su reloj y su salida sellada, commiteando cada salida al terminar su tramo | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 3** | EL CIERRE INTEGRAL, TODO LO QUE NO NECESITA CREDENCIAL: el ciclo entero de Gate 0 por los dos lados con su consola SELLADA y sus dieciocho salidas en disco; las tres suites con su exitcode y sus bytes; el inventario de las 71 fichas contra sus pruebas con el hash de la apertura; y el marcador y el censo recomputados, cada uno con su comando y con las cifras del auditor al lado para cotejar y NO para copiar | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 4** | LOS DOS PUNTOS QUE `OP-I-01` DEJO EN A MEDIAS, Y NO SE CIERRAN A OJO. El punto 3 por su NEGATIVA, que si se puede citar: se corre la busqueda y se publica su CERO con el comando delante. Y el punto 4 midiendo ANTES de decidir: buscar cual es el instrumento y cual el fichero que SI regeneran la vista humana, publicar la busqueda con su comando, y solo entonces decir si CUBRE, queda A MEDIAS o NO CUBRE. SIN mover el campo estado de ninguna ficha | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
| **TAREA 5** | EL REPORTE, Y SU SECCION 3.1 ESTA VEZ CON CIFRAS DENTRO. Sellar la consola del ciclo de Gate 0 por los dos lados en los nombres que el compositor busca, y sobre todo hacer que EL COMPOSITOR CAIGA EN ROJO SI NO LA ENCUENTRA: el de la 214 escribio una fila en blanco y siguio, que es degradacion silenciosa y es lo que el banco 9 prohibe. Y la seccion 9 cierra con LA BATERIA CORRIDA, no con hueco declarado, porque esta es su vuelta | **ABIERTA, SIN CERRAR** | (la fila la anexa `anexar_tarea_al_reporte.py` al cerrarse la tarea) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->
*(vacio: ninguna tarea ha cerrado todavia)*
<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**

