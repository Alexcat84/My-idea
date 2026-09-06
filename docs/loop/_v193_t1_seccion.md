### TAREA 1. LOS REGISTROS. **CERRADA EN VERDE.**

**EL NUMERO NO SE TECLEO.** `scripts/loop/serie_de_registros.py`, corrido en el
bloque `G` de la apertura y otra vez dentro del registrador, da **`R.55`** como
siguiente libre, con **46 entradas, 0 colisiones y 0 huecos** antes de escribir.
El encargo adelantaba `R.55` y **CALZA**, y lo que manda es el instrumento.

**EL INSTRUMENTO ES NUEVO Y DICE POR QUE, PORQUE EL DE LA 192 NO SIRVE AQUI.**
`scripts/loop/vuelta193_tarea1a_registrar_acta193.py` **importa la maquina
generica** de `vuelta192_tarea1a_registrar_acta192.py` (acotar el acta, contar
claves, leer titulos, expandir rangos, leer filas de la tabla, la serie) y **solo
escribe lo que el acta 193 tiene distinto**. Las cuatro diferencias van medidas y
no supuestas:

| lo que cambia | la medicion que lo obliga |
|---|---|
| `MIA` en SINGULAR como lead del auditor | con `MARCAS_LEAD_AUDITOR = ("MIAS",)` el reparto sale **ejecutor 4, auditor 0**, y el acta declara **UNA** propia. Con la marca ensanchada a `MIA` sale **3 y 1, cero huerfanas** |
| dos marcas de estado nuevas (`NO LO CAMBIAN` de la `4.8`, `ADJUDICADO: SE CONGELAN` de la `4.10`) | con el vocabulario de la 192 y nada mas saldrian **2** adjudicaciones `SIN DECIR`, y el registrador **PARARIA** |
| la propia del auditor es **DE METODO** y NINGUNA es de cifra publicada | el registrador de la 192 PARABA si ninguna propia era `DE CIFRA PUBLICADA`. Aqui esa parada seria falsa: lo que se exige es que **cada propia DECLARE su especie**, y el reparto se publica salga lo que salga |
| las del ejecutor van por DOS filas y no por una | el acta **asigna** una (`C.1`, de REPORTE) y **cita** cuatro (`C.1` a `C.4` del reporte, de METODO). Contarlas juntas da **5**, que **no es el numeral de ninguna fila** de la tabla de credito |

**LAS CIFRAS, CONTADAS DEL CUERPO ACOTADO DEL ACTA (lineas 67926 a 68281 de
`docs/loop/ACTA_AUDITOR.md`) Y NINGUNA DEL ENCARGO**, en
`docs/loop/SALIDA_V193_T1A_REGISTRO_R55.txt` (11576 bytes):

- **10 adjudicaciones** `4.1` a `4.10`, cada una con **1** aparicion; patron
  entrecomillado **0**, patron suelto **10**, **las dos cifras publicadas**.
- **7 discutibles, los 7 A FAVOR; 3 preguntas contestadas** (`P.1` en la `4.8`,
  `P.3` en la `4.9`, `P.2` en la `4.10`). **CIFRA `EN CONTRA`: 0**, por tercera
  acta seguida, **y no se re fabrica su caso**: se cita
  `docs/loop/SALIDA_V191_T1A_MUTACION_REGISTRADOR.txt`, **6904 bytes en disco y
  6904 por LF**, `sha256` LF `795c0ec740bdd5cc`, veredicto leido del propio
  fichero `'VEREDICTO: VERDE'`.
- **4 hallazgos** `5.1` a `5.4`. **La fila de credito que los cuenta dice 6**, y
  **no se elige a ojo cual vale**: esa fila cuenta juntas discrepancias y
  hallazgos, y su celda lo escribe. **Por resta: 2 discrepancias fuera del
  marcado mas los 4 hallazgos.**
- **1 caida propia del auditor** (`C.1`, DE METODO) contra su fila **1**;
  **1 caida del ejecutor asignada** (`C.1`, DE REPORTE) contra su fila **1**;
  **4 citadas de metodo** contra su fila **4**. **LAS TRES CALZAN**, y si alguna
  no calzara el registrador PARARIA en vez de elegir la que conviene.
- **La fila de puestos con sus DOS notas, leidas y no parafraseadas:**
  `'solape TOTAL'` y `'cero quemados'`, con **30 aislados y 30 cotejados**.

**LA IDEMPOTENCIA NO SE AFIRMA: SE PROBO RE CORRIENDOLO, CON LA SEDE MEDIDA EN
BYTES ANTES Y DESPUES.** `docs/PENDIENTES.md` paso de **1020758 a 1029096 bytes**
al escribir la entrada (8337 bytes, 149 lineas por `count(NL)` y 150 por
`split`), y **el re corrido dejo la sede en 1029096, exactamente igual**, con la
salida `docs/loop/SALIDA_V193_T1A_RECORRIDO_SIN_ESCRIBIR.txt` (11720 bytes)
diciendo que el acta 193 ya aparece en **2 linea(s)**. Serie despues de escribir:
**47 entradas, 0 colisiones, 0 huecos, siguiente libre `R.56`**.

**Y CON SU CASO POSITIVO POR MUTACION**, en
`docs/loop/SALIDA_V193_T1A_MUTACION_REGISTRADOR.txt` (2262 bytes, **VEREDICTO:
VERDE**), corrido sobre texto FABRICADO y con el valor esperado sacado de como se
fabrico y no de una constante igual a la obtenida. **Las tres mutaciones CAEN:**
la marca vieja da **2/0** y la nueva **1/1** sobre la misma seccion fabricada;
juntar asignadas y citadas da **5** donde separadas dan **1 y 4**; y un titulo
mudo sale `SIN DECIR`, que es lo que hace PARAR al registrador. **La marca nueva
`MIA` tampoco rompe la forma en plural**, y ese caso corre.

**LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA: 8 actas sin entrada propia
(173 a 180)**, que **CALZA** con lo que el encargo dice y **se registra sin
arreglarse**, que es donde el encargo la deja.
