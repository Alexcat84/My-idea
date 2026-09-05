### TAREA 1, LOS REGISTROS Y LA DEUDA DE LA 168 QUE SE CORTO

**Salidas:** `docs/loop/SALIDA_V169_APERTURA.txt` (el sello de apertura),
`docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt` (la bateria re corrida entera),
`docs/loop/SALIDA_V169_T1C_NOTAS_REPORTE_168.txt` (las tres notas) y
`docs/loop/SALIDA_V169_T1_REGISTRO_ACTA_168.txt` (el `R.38`).
**Instrumentos:** `scripts/loop/vuelta169_apertura.py`,
`scripts/loop/verificar_mutaciones_viejas.py`,
`scripts/loop/vuelta169_tarea1c_notas_al_reporte_168.py` y
`scripts/loop/vuelta169_tarea1_registrar_acta168.py`.

**LA APERTURA, SELLADA ANTES DE LA PRIMERA OPERACION** (`EJECUTOR.md` 1). Cifras
contadas de `docs/loop/SALIDA_V169_APERTURA.txt`, en la seccion que se nombra:

| lo que se midio | cifra | seccion de la salida |
|---|---|---|
| HEAD de apertura | `2ba08da7` | A |
| rama y remoto | `pasada-unica`, `origin/pasada-unica`, 0 adelante y 0 atras | B |
| lineas de `git status --porcelain` | **5** | C |
| `SALIDA_V168_T3_BATERIA_CIERRE.txt` | **0 bytes**, **NO ESTA EN EL ARBOL DE HEAD** | D y F |
| `_v168_cierre_tmp.py` | **3.220 bytes**, NO esta en el arbol | D y F |
| `master_graph.json` | modificado en `status` pero su diff mide **0 bytes**, tambien ignorando el CR | E |

**EL `master_graph.json` NO SE COMMITEO, Y SE DICE POR QUE:** `git status` lo daba
por modificado y su diff real mide **cero bytes**. Es suciedad de indice, no un
cambio. Commitearlo habria metido un fantasma en el arbol.

**(1.b) LA BATERIA, RE CORRIDA ENTERA, Y AHORA SU SALIDA NACE COMMITEADA.** Cifras
contadas de `docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt`, **15.212 bytes**,
commit `07446f2a`, comprobado con `git ls-tree -r HEAD` por el propio instrumento
de las notas antes de publicar ni una:

| lo que mide la bateria | cifra de HOY | lo que publico la tabla 3.c de la 168 |
|---|---:|---:|
| arneses cronometrados (la nomina) | **72** | 72 |
| ANCLA PERDIDA | **0** | 0 |
| NO MORDIO | **1** | 1 |
| NO REPRODUCIBLE | **0** | 0 |
| CASO DECLARADO | **2** | 2 |
| arneses posteriores FUERA de la nomina | **0** | 0 |
| entradas de la nomina invisibles al censo | **0** | 0 |
| RUIDO DE CONCURRENCIA | **0** | 0 |

**LAS OCHO CELDAS REPRODUCEN AL DIGITO, INCLUIDA LA QUE NO ERA UNA MEDICION.** La
primera fila es la de la caida `4.1`: el fichero commiteado de la 168
(`SALIDA_V168_BATERIA.txt`) decia **71**, y el **72** salia de contar la nomina de
hoy. **Era una prediccion correcta. Ahora es una medicion.** Tiempo por su propio
cronometro: **1.548,4 segundos, 25,8 minutos** (la corrida del auditor en la 168
tardo 19,1). **No se mato antes**, que es lo que el encargo pedia.

**EL ROJO SIGUE SIENDO UNO Y ES EL MISMO:** `vuelta166_tarea3_mutacion_retrato.py`,
exit 1, `NO MORDIO`. Esta corrida es la que PRUEBA que era ese y solo ese, y la
TAREA 2 lo re ancla.

**(1.c) LAS TRES NOTAS AL REPORTE DE LA 168, TODAS POR ADICION.** El fichero pasa
de **26.577 a 31.263 bytes** y de **456 a 530 lineas**: solo crece. El instrumento
comprueba, antes de escribir, que las cuatro anclas aparezcan **exactamente una
vez** cada una, y que cuatro trozos de texto viejo sigan dentro despues (los
cuatro siguen). **Las once cifras que la nota de la `6.1` publica se comprobaron
contra el fichero de salida Y contra `git ls-tree`** antes de escribirse, y el
instrumento PARA si alguna no cuadra: **11 de 11**. Es la relectura al doble que
el acta 168 ordeno en su metrica de credito, ejecutada dentro del instrumento y
no prometida en prosa.

**LO QUE DICE CADA UNA, Y NINGUNA BORRA UNA PALABRA:**

| nota | que adosa | que NO toca |
|---|---|---|
| `6.1`, al pie de la 3.c | que la tabla se publico antes que su fuente (`fdc46ad2` a las 18:03:30, fichero nacido a las 18:04 con 0 bytes), que la celda `72` era prediccion y no medicion, y que hoy la fuente existe | ni una celda de la tabla, que resulto correcta entera |
| `6.3`, a "LA CAUSA, MEDIDA" | que el arnes **nacio rojo en su propio commit `33fe1380`**, de la vuelta 166, y que la 167 **no movio esa fila**: trece tachadas antes y trece despues | la tabla de los tres casos que caen, correcta al digito |
| `6.9`, a la traza | la subida que faltaba (`78ea7799` 334, **`801c59f9` 335**, `c8c4e0b3` 334) y `~~trazada commit a commit~~` **tachada y visible** | la conclusion, que no se mueve |

**(1.a) EL `R.38`.** Cifras contadas de
`docs/loop/SALIDA_V169_T1_REGISTRO_ACTA_168.txt`:

| lo que se midio | cifra | seccion |
|---|---:|---|
| cuerpo del acta 168 acotado | lineas **56.059 a 56.701** | A |
| adjudicaciones `6.n` | **10** (6.1 a 6.10) | B |
| caidas propias del auditor | **2** | C |
| entradas de la serie ANTES de escribir | **29** | E |
| colisiones y huecos | **0 y 0** | E y K |
| numero libre, computado y no tecleado | **`R.38`** | E |
| entradas de la serie DESPUES | **30**, y la serie VE la entrada en `docs/PENDIENTES.md:12081` | K |
| reparto por via | EJECUTADA **7**; SIN TOCAR NADA **3** | I |

**EL BORDE QUE NINGUNA VUELTA ANTERIOR HABIA TOCADO:** el acta 168 es **la
primera que llega a `6.10`**, y el barrido tiene que contarla sin confundirla con
`6.1`. Lo impide el espacio final del patron, y el conteo salio **10**. El
encargo dice "6.1 a 6.10", o sea diez: **coincide, y se cita como contraste, no
como fuente.**

**EL `_v168_cierre_tmp.py` SE RESUELVE POR LA PRIMERA VIA DEL ENCARGO Y ADEMAS SE
MIDE.** Pasa a `scripts/loop/vuelta168_cierre.py`, que es el nombre que su propio
docstring ya se daba, y queda commiteado. **Y SE DECLARA QUE NO CORRIO, medido y
no supuesto:** los **diez** ficheros que ese script escribe
(`SALIDA_V168_HEAD_CIERRE.txt` y sus nueve hermanos) **no existen, ni en el arbol
ni en disco**, y su paso 1 escribe el primero de ellos. **No corrio ni un paso.**
Y de paso queda probado algo que nadie habia dicho: **el fichero de cero bytes NO
lo escribio ese script**, porque `SALIDA_V168_T3_BATERIA_CIERRE.txt` no esta entre
los diez nombres que produce.
