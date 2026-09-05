### TAREA 1. EL REPORTE. LA DEUDA DE LA 172 PAGADA Y EL DE LA 174 ABIERTO

**1.a EL REPORTE DE LA VUELTA 172 QUEDA CERRADO Y ARCHIVADO.** Y antes de
cerrarlo, la clausula de la `4.4`, porque archivar primero seria sellar la
afirmacion falsa en `docs/loop/reportes/REPORTE_V172.md` y corregir despues una
copia. **La eleccion del orden es mia y va escrita para que se pueda discutir**
(discutible `D.1`).

**LA CORRECCION DEL `4.4`, POR EL CARRIL DEL `9.10`.** Instrumento
`scripts/loop/vuelta174_tarea1a_corregir_44.py`, salida
`docs/loop/SALIDA_V174_T1A_CORREGIR_44.txt`. **Las dos rutas que la fila de la
TAREA 5 nombraba, MEDIDAS HOY en el disco con `os.path.getsize` y no creidas al
acta:**

| ruta que la fila publicaba como prueba | medido hoy |
|---|---|
| `docs/loop/SALIDA_V172_T5_MUTACION_CIERRE.txt` | 4921 bytes |
| `docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt` | **NO EXISTE** |

**CIFRA rutas de esa fila que apuntan a un vacio: 1.** El instrumento CAE EN
ROJO y no escribe nada si esa cifra no es exactamente 1: no corrige por lo que
dijo un acta, corrige por lo que mide el disco. El `CERRADA` viejo y la prueba
falsa quedan **enteros y tachados**, con el estado corregido al lado y la
correccion fechada debajo de la tabla. **13 comprobaciones de relectura, 0
fallan.** Su caso positivo por mutacion,
`scripts/loop/vuelta174_tarea1a_mutacion_44.py`, sobre **SUJETO CONGELADO**
(cero lecturas de disco y cero escrituras): **26 de 26**, once casos rojos que
caen cada uno por SU motivo nombrado y devolviendo el texto INTACTO, mas el caso
verde de catorce comprobaciones, mas la mutacion del propio arnes (se le pide un
motivo inventado y se comprueba que NO aparece).

**EL CIERRE.** `scripts/loop/cerrar_reporte.py --vuelta 172`, salida
`docs/loop/SALIDA_V174_T1A_CERRAR_REPORTE_172.txt`. **Las cuatro piezas, y
ninguna falta: `CIFRA piezas que faltan: 0`.** El reporte pasa de 33.434 a
**48.851 bytes** y de 536 a **761 saltos de linea**.

**LA SECCION 9 VA CON HUECO DECLARADO Y MEDIDO**, que es el carril que la TAREA
1.b de la vuelta 173 construyo. **Las dos cifras del hueco las midio el bloque
de apertura de esta vuelta, `H.3`, con `os.path.getsize`:**

| fichero de la bateria de la 172 | bytes medidos hoy |
|---|---:|
| `docs/loop/SALIDA_V172_BATERIA.txt` (ejecutor) | **0** |
| `docs/loop/SALIDA_V172_AUDITOR_BATERIA.txt` (auditor) | **0** |

**ATRIBUCION: NADIE la corrio**, y el auditor lo declara el mismo en su clausula
`4.3` (`docs/loop/ACTA_AUDITOR.md:58638`, leida hoy).

**LA CABECERA NO SE TECLEA Y ADEMAS SE COTEJA.**
`tallar_cabecera_reporte.py --vuelta 172 --fase04 --comparar docs/loop/REPORTE.md`
(`docs/loop/SALIDA_V174_T1A_COMPARAR_CABECERA_172.txt`) dice **`filas cotejadas:
9 | DISTINTAS: 0 | ausentes: 0`** y **`CABECERA: IDENTICA AL TALLADOR`**.
**ATRIBUCION DE LA CABECERA, y no es mia:** el fichero
`docs/loop/SALIDA_V172_TALLADOR_CABECERA.txt` nacio en el commit `0c287793`, que
es **el acta del auditor de la vuelta 172**, y es byte a byte identico a
`docs/loop/SALIDA_V172_AUD2_TALLADOR.txt`. La celda que se pego en el reporte de
la 172 la tallo **el auditor**, no el ejecutor (discutible `D.2`).

**EL ARCHIVADO.** `scripts/loop/archivar_reporte.py --vuelta 172`
(`docs/loop/SALIDA_V174_T1A_ARCHIVAR_172.txt`), leido de git y no del arbol:
`docs/loop/reportes/REPORTE_V172.md`, **48.851 bytes, 761 lineas, sha256
`d29e45527ea302a0`**, commit de origen `23d5743c`. **La cadena de archivados ya
no tiene hueco: 168, 169, 170, 171 y 172.**

**1.b EL REPORTE DE LA 174 SE ABRE Y SE CIERRA EN LA MISMA VUELTA.** Esqueleto
por `scripts/loop/vuelta174_esqueleto_reporte.py`
(`docs/loop/SALIDA_V174_T1B_ESQUELETO.txt`): **4.547 bytes, 65 lineas, 2 filas
de tarea abiertas.**

**Y TRAE EL UNICO CAMBIO DE MAQUINA DE LA VUELTA, QUE ES UN ENDURECIMIENTO.** El
paso 0 de todos los clones anteriores preguntaba por `VUELTA - 1`. **La vuelta
173 no escribio ningun reporte**, asi que ese sujeto ya no sirve. Corrido tal
cual, y publicado salga lo que salga, el paso 0 sobre la **173** da **ROJO por su
clausula (b)**: *"no existe el archivo `docs/loop/reportes/REPORTE_V173.md`"*.
**Eso es cierto y no es la pregunta.** La pregunta del paso 0 es *"lo que voy a
destruir, esta guardado?"*, y aqui el numero **se lee de la cabecera del fichero
que se va a pisar** con la funcion pura `vuelta_del_reporte_del_arbol()`, no se
teclea. Sobre la **172**, que es el reporte que de verdad estaba en el arbol, el
paso 0 da **VERDE con los dos sha256 calzando** (`d29e45527ea302a0`). **Ninguna
de sus cuatro clausulas se afloja: se le da el sujeto correcto.**

**Y NO SE PUBLICA SIN SU MUTACION.**
`scripts/loop/vuelta174_tarea1b_mutacion_esqueleto.py`
(`docs/loop/SALIDA_V174_T1B_MUTACION_ESQUELETO.txt`): **19 de 19**, con los
ficheros de mentira en un temporal que se borra al terminar y **el repo sin
tocar**. Ocho casos sobre la funcion pura (devuelve el numero cuando lo hay y
`None` cuando no, sin adivinar ninguno), ocho sobre las clausulas `(b)`, `(c)` y
`(d)` de la guarda (incluida la caida por **un solo byte** de diferencia y la
vuelta al verde al restaurar, que es lo que prueba que no es un rojo
permanente), y **el caso que prueba el cambio de esta vuelta: el sujeto TECLEADO
da ROJO y el LEIDO da VERDE**.

**LA IDENTIDAD, LEIDA DE GIT Y NO TECLEADA:** el commit del acta 173 se localizo
por **busqueda NO ANCLADA** (su asunto lleva arrobas sueltas delante, como paso
con el de la 170), con **exactamente 1 acierto**: `ee3be26a`. El HEAD de
apertura, `9445cd21`, salio del sello
`docs/loop/SALIDA_V174_HEAD_APERTURA.txt`, y el nacimiento de ese sello,
`f7284a6b`, de `git log --diff-filter=A`.

**EL CIERRE DE ESTA MISMA 1.b ES EL ULTIMO ACTO DE LA VUELTA Y TODAVIA NO HA
CORRIDO AL ESCRIBIR ESTA LINEA.** Se dice asi a proposito: la caida `4.4` que
esta misma tarea acaba de corregir fue exactamente una fila que dijo `CERRADA`
nombrando una prueba que aun no existia. **Aqui no se nombra ninguna ruta del
cierre**, porque por la regla del 5 sep 2026 una ruta a un fichero inexistente
ya es caida de cifra. Cuando el cierre corra, **la celda de estado de esta fila
la sella `scripts/loop/vuelta174_sellar_fila_cerrada.py`, que MIDE el fichero
antes de nombrarlo y se niega a sellar si no existe o mide cero bytes.**
