# REPORTE DE LA VUELTA 193 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta193_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **NO ES VUELTA DE BATERIA, PERO ES LA ULTIMA ANTES.** `AUDITOR.md` 6.1: la
> bateria corre CADA CINCO VUELTAS, **la 189 la corrio entera**, y **la siguiente
> cae en la 194**. La seccion 9 cierra con el **HUECO DECLARADO Y MEDIDO** por el
> carril de `cerrar_reporte.py`, **con su nombre, sus bytes medidos y su
> atribucion, LAS TRES JUNTAS**. Y por eso **las dos bloqueantes son las que le
> llegan rotas a esa corrida**.
>
> **VAN CINCO SUB-TAREAS Y DOS SON BLOQUEANTES.** El tope de cinco esta ganado con
> holgura y **la cifra se conto del instrumento en esta vuelta**, no se heredo: el
> bloque `E` del sello de apertura corrio
> `scripts/loop/vuelta192_racha_de_cierres.py` sobre el inventario ENTERO.
>
> **EL DESFASE DE CALIBRADO SE MIDIO EN LA APERTURA**, dentro del bloque de
> apertura y **antes de la primera operacion**. Una columna de apertura medida al
> cierre es caida que ACUMULA.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina** (la opcion `c` que el fundador RECHAZO el
> 5 sep 2026: **la nomina sigue creciendo y nadie la poda sin el fundador**), ni la
> bateria, que cae en la 194. **Y siguen fuera, nombradas para que la 194 no las
> redescubra:** el desfase de `PATRONES_ACTA`, **que se encarga DESPUES de la 194**
> porque toca `tallar_cabecera_reporte.py` y cuatro entradas de la nomina lo
> nombran; `acumulan()` que lea la tabla o declare que no es la sede; el cotejo de
> clon declarado que separa sentencia de codigo de cambio de texto; la excepcion
> que publica siempre su lista; la medicion del censo de arneses con carril de
> mutacion sin fichero propio; las ocho actas sin entrada propia en la serie (173 a
> 180); el exitcode 2 propagado a `--componer`; y que el campo `evidencia` de
> `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE MUEVE: sigue en
> `LISTA`**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta193_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 192: `485c2f3e`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 192: LA 191 REPRODUJO ENTERA Y SIN UNA CIFRA FALSA NI UNA RUTA VACIA, Y LA PARADA QUE DECLARA ES CIERTA: LA CAIDA ERA MIA.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y DESDE ESTA VUELTA LLEVA SU
  FECHA DE CORTE.** La linea de arriba nombra el acta **192** porque
  `PATRONES_ACTA` pide la de `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la
  193**. Es el `D.2` del reporte de la 184, adjudicado a favor con reparacion
  encargada por la `5.2` del acta 185, **y el acta 193 lo deja expresamente DESPUES
  de la bateria de la 194**. Lo que si se puede contar: **4 reportes
  archivados traen el literal `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`), contados por
  `reportes_con_el_literal()` de este mismo fichero, **con FECHA DE CORTE
  2026-09-06** (banco `9.21`, TODA CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Esa
  fecha es la reparacion que el acta 193 encarga sobre la caida `5.5` del reporte
  de la 192**, que publico una cifra de este mismo inventario contradiciendo a su
  propia seccion 0: **un inventario que crece cada vuelta sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V193_HEAD_APERTURA.txt`: `5b921750`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `306c6fbb`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **192**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**PENDIENTE DE TALLAR AL CIERRE, Y SE DICE EN VEZ DE RELLENARLA.** La tabla sale
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 193`. **Esta
vuelta corrio el bloque de apertura entero ANTES de su primera operacion**, asi
que la mitad izquierda ya se puede leer: corrido aqui, el tallador dice **"ROJO, 23 celdas no se pudieron leer"**, y de las lineas de
rojo que imprima, **4 mencionan APERTURA**. Este hueco se rellena con la
tabla tallada entera cuando la vuelta cierre.
<!-- FIN CABECERA TALLADA -->

## 1. LAS CINCO TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 193 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado. Registra LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, las diez A FAVOR (siete son los discutibles `D.1` a `D.7` del reporte de la 192 y las tres restantes son las preguntas `P.1`, `P.2` y `P.3` contestadas), OTRA VEZ CERO EN CONTRA; LOS CUATRO HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` la cuarta puerta que no se puede usar desde el CLI, `5.2` el cotejo que convierte `"no"` en `si`, `5.3` el arnes que imprime su `mkdtemp` en la salida sellada, `5.4` el reporte que se contradice en la cuenta del `DESFASE DECLARADO`); UNA CAIDA DEL EJECUTOR, DE REPORTE, QUE NO ACUMULA (la seccion 5.5 publica 3 donde hay 4 y donde su propia seccion 0 dice 4: se registra con su nombre, dispara la relectura al doble y NO acumula por la letra del 27 ago 2026, RACHA DE REPORTE 0); UNA CAIDA PROPIA DEL AUDITOR, DE METODO (`C.1`, correr `run_phase1.py` sin `--reaplico-curaduria` y ensuciar `dataset/`); y LA METRICA DE CREDITO de la seccion 7 con la fila de puestos y su nota: 30 aislados y 30 cotejados, CERO quemados, SOLAPE TOTAL a proposito, o sea control y no cobertura nueva. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues | **CERRADA EN VERDE** | `SALIDA_V193_T1A_REGISTRO_R55.txt`, `SALIDA_V193_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, `SALIDA_V193_T1A_MUTACION_REGISTRADOR.txt` |
| **TAREA 2** | LOS TRES ARNESES QUE NO REPRODUCEN, ANTES DE LA BATERIA DE LA 194. BLOQUEANTE Y LA MAS URGENTE DE LA VUELTA. Es la adjudicacion `4.10` y el hallazgo `5.3` del acta 193, medido en `docs/loop/_auditor_v193_reproducibilidad.txt`: los tres REPRODUCEN entre dos corridas de hoy y NINGUNO contra su sellada. (a) LOS DOS PRIMEROS (`vuelta191_tarea3_mutacion_lineas.py` y `vuelta191_tarea6_mutacion_bloque_tallado.py`): CONGELAR SU SUJETO o DECLARAR EL CASO por el carril de los `CASO DECLARADO`, porque la `4.4` del acta 191 dice que `SUJETO VIVO` es FALLO y no deuda y la `4.10` cierra la salida que quedaba: una salida que no reproduce NO ES DEL MISMO CALIBRE, tenga o no tenga motivo escrito. (b) EL TERCERO (`guarda_de_entrada_a_la_nomina.py`): que su salida sellada NO lleve el nombre del directorio temporal; el directorio se sigue fabricando y se sigue retirando (`P.16`). (c) ARREGLAR LA GUARDA QUE NO LO VIO: `tempfile` y `mkdtemp` cuentan como huellas de CONGELADO y por eso da CONGELADO a un arnes cuya salida cambia en cada corrida; UNA HUELLA DE TEXTO NO PRUEBA REPRODUCCION. (d) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un arnes cuya salida no reproduce vuelve a salir CONGELADO. (e) NO SE TOCA LA NOMINA: la opcion `c` que el fundador RECHAZO el 5 sep 2026 sigue rechazada. (f) AL CERRAR, CORRER LOS TRES DOS VECES Y PUBLICAR SUS BYTES Y SUS `sha256`; si alguno sigue sin reproducir, SE PARA Y SE TRAE | **CERRADA EN VERDE, Y CON UN CUARTO CASO QUE EL ACTA NO TRAIA** | `SALIDA_V193_T2C_GUARDA_REPRODUCCION.txt`, `SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`, y los cuatro cortes viejos `_CORTE_191`/`_CORTE_192` |
| **TAREA 3** | LA VARA DE LAS CIEGAS PASA A SER LA DEL BANCO, Y EL DOBLE SE LEE CON ELLA. Es la adjudicacion `4.9` del acta 193, que contesta la `P.3` a favor. No es doctrina nueva: la vara ya esta escrita en `docs/BANCO_DE_TEXTOS.md` `9.6.1`, LA VARA DE LA RAMA CONTENIDO-MANDA: LA LINEA O EL PROCEDIMIENTO, propuesta y adoptada el 12 ago 2026. (a) ESCRIBIR EL CRITERIO DE LA CIEGA CITANDO `9.6.1` POR NUMERO, con la frase de la vara copiada LITERAL y no parafraseada (`9.5.0`), y que sea el criterio que se le pasa a `aislador_de_ciega.py` de aqui en adelante. (b) LA RELECTURA AL DOBLE DEL TRAMO DE LA 192, que es la deuda de credito de la tanda del auditor y la encarga el auditor, que es donde `AUDITOR.md` 1.2 la pone, CON MOTIVO TRIPLE: dos discrepancias cayeron fuera del marcado del auditor, las dos cayeron tambien fuera del marcado del ejecutor, y son el mismo par para los dos lectores. (c) EL TRAMO son los 30 puestos de `docs/loop/SALIDA_V192_T2_CIEGA.txt`, que son los mismos 30 de la ciega del auditor `docs/loop/_auditor_v193_ciega_blind.txt`. (d) AL DOBLE son sus 30 vecinos deterministas, con `vecinos()` IMPORTADA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y no copiada, con `evitar` cargado con TODO lo consumido, CONTADO DE SUS FICHEROS Y NO DEL ENCARGO, y con el solape contra el tramo y contra el universo en 0 y 0 POR CONSTRUCCION. (e) criterio escrito literal, ciega y destape en ficheros SEPARADOS, clases escritas y COMMITEADAS en su propio commit ANTES de abrir el destape, y dudosos NOMBRADOS DELANTE. (f) PUBLICAR LO QUE LA VARA NUEVA CAMBIA: cuantos dudosos y cuantas discrepancias habrian salido distinto con `9.6.1`, y si no cambia nada, DECIRLO. NO SE TOCA NINGUNA CLASE: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abre solo en lectura y su `sha256` LF abre y cierra en `0a77b5a35a962621` por las dos convenciones | **CERRADA, Y LA VARA NUEVA NO ALCANZA A LA MITAD DE MIS DISCREPANCIAS** | `SALIDA_V193_T3_AISLAMIENTO.txt`, `SALIDA_V193_T3_MIS_CLASES.txt` (commit b57aa7d6), `SALIDA_V193_T3_COTEJO.txt`, `SALIDA_V193_T3_COTEJO_SALIDA.txt`, `SALIDA_V193_T3F_QUE_CAMBIA_LA_VARA.txt` |
| **TAREA 4** | LA CUARTA PUERTA QUE SOBREVIVA AL PROCESO. Es el hallazgo `5.1` del acta 193, levantado por el auditor CONTRA EL FICHERO QUE LE PROTEGE Y QUE EL EJECUTOR ESCRIBIO PARA EL EN LA 192, y medido en `docs/loop/_auditor_v193_cuarta_puerta_prueba.txt`: `_BITACORA` y `_SELLADO` son estado de MODULO y mueren con el proceso, el auditor sella con el CLI, y en el proceso siguiente `puede_declarar_clases()` responde `NO: este turno no ha sellado` aunque el sello este en disco. Y LA MITAD MAS SERIA ES SOBRE LAS TRES PUERTAS VIEJAS: el docstring afirma que el sello no se pueda escribir despues, y un turno que toca `REPORTE.md` y arranca otro proceso vuelve a sellar con bitacora vacia porque `sellar()` SOBRESCRIBE. (a) QUE LA BITACORA Y EL SELLO SOBREVIVAN AL PROCESO, en un fichero del turno. (b) QUE `sellar()` CAIGA EN ROJO SI YA HAY SELLO EN DISCO PARA ESA VUELTA, en vez de sobrescribirlo. (c) QUE EL CLI PUEDA DECLARAR LAS CLASES, con su bandera, leyendo el sello de disco. (d) Y SI ALGO NO SE PUEDE, DECIRLO EN EL DOCSTRING en vez de afirmar lo contrario, que esa frase vive en sede de cifra publicada desde el 2 sep 2026. (e) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un sello se puede reescribir despues de tocar uno de los tres prohibidos en otro proceso. (f) NO SE CLONA EL FICHERO: `apertura_del_auditor.py` tiene nombre estable y se le anade. (g) RE CORRER SU ARNES DE LA NOMINA CON EL PARCHE PUESTO Y COMPROBAR QUE REPRODUCE BYTE A BYTE; hoy da 4282 bytes y `sha256` `4779fcd04bc5b2da` | **ABIERTA, SIN CERRAR** | (la fila se anexa al cerrarse la tarea) |
| **TAREA 5** | EL COTEJO QUE NO CONVIERTA `"no"` EN `si`. Es el hallazgo `5.2` del acta 193. `cuerpo_del_cotejo()` de `scripts/loop/cotejo_de_ciega.py` hace `bool(du)`, y `bool("no")` es `True`; el docstring especifica esa columna como `en dudosos` . `si` o `no`, que es justo la forma que revienta, y el instrumento publico al auditor `discrepancias FUERA de los dudosos: 0 (ninguna)` TENIENDO DOS. LA CIFRA PUBLICADA DEL EJECUTOR NO ESTA AFECTADA: `vuelta192_tarea2b_cotejo.py` linea 145 pasa `p in dudosos`, un booleano de verdad. IMPORTA MAS QUE UNA ERRATA porque la columna `en dudosos` es la unica del fichero de la que cuelga una regla de parada: `AUDITOR.md` 1.2 baja el credito y encarga el doble POR LO QUE CAE FUERA. (a) QUE `en_dudosos` SE NORMALICE O CAIGA, y no se resuelva en silencio, con la misma vara que el caso `G` de la mutacion ya le aplica a `veredicto_de`. (b) QUE LA GUARDA DE `escribir_cotejo()` MIRE ALGO MAS QUE EL DENOMINADOR, o que diga en su salida que no es la sede de esta comprobacion. (c) CON SU CASO POSITIVO POR MUTACION, que CAIGA si un `en_dudosos` no booleano se convierte en `si` sin avisar. (d) RE ESCRIBIR EL COTEJO DEL AUDITOR CON EL INSTRUMENTO ARREGLADO y comprobar que da lo que el publica a mano: 30 cotejados, 25 coinciden, 5 discrepan, 3 dentro y 2 fuera. (e) `cotejo_de_ciega.py` NACIO EN LA 192 Y ENTRA EN LA NOMINA POR LA REGLA DEL PROPIO FICHERO: tocarlo ahora es ANTES de que entre, y eso es a favor y no en contra | **CERRADA EN VERDE** | `SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt`, `SALIDA_V193_T5D_REHACER_COTEJO.txt`, `SALIDA_V193_T5D_COTEJO_AUDITOR_REHECHO.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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

### TAREA 2. LOS ARNESES QUE NO REPRODUCEN. **CERRADA EN VERDE, Y CON UN CUARTO CASO QUE EL ACTA NO TRAIA.**

**LO QUE ENCONTRE AL ENTRAR, ANTES DE TOCAR NADA** (bloque `F` del sello de
apertura): las tres selladas del acta 193 estaban INTACTAS y ninguna de cero
bytes, con los mismos bytes que el acta publica, **5836**, **4173** y **2433**
por LF, y los mismos `sha256` `bc8d7273baf30644`, `6de586c0e5c7a104` y
`d2c99c7e27f40183`.

**a) LOS DOS PRIMEROS: SUJETO CONGELADO, POR `git show` SOBRE UN COMMIT CLAVADO.**
Ninguno se declara como `CASO DECLARADO`: **los dos se congelan**, que es la
salida que el encargo pone primero.

| arnes | lo que leia VIVO | lo que lee ahora |
|---|---|---|
| `vuelta191_tarea3_mutacion_lineas.py` | el censo de `scripts/loop` del arbol, la lista de `vuelta191_*` del arbol, y `docs/plan/LECTURAS_DIRIGIDAS.md` | los tres, del arbol del commit `21ffca0c`, que es **el commit que ANADIO su salida sellada**, localizado con `git log --diff-filter=A` |
| `vuelta191_tarea6_mutacion_bloque_tallado.py` | `docs/loop/REPORTE.md`, que es un fichero distinto en cada vuelta por construccion | `docs/loop/reportes/REPORTE_V191.md` del commit `92a09bfa`, o sea **un reporte archivado, que no se reescribe, sacado de un commit, que no se mueve** |

**Y EL COMMIT CLAVADO DEL SEGUNDO NO ES EL DE SU PROPIA SELLADA, Y SE DICE POR
QUE:** se probo primero con `576fa467`, el commit que anadio su salida, y **en su
arbol el reporte de la 191 todavia NO estaba archivado**, porque el archivado
ocurre al cerrar la vuelta siguiente. **El arnes salio ROJO por sujeto vacio**,
que es la conducta correcta de una guarda que no puede pasar en verde sobre un
vacio, y de ahi salio el commit bueno.

**LO QUE ESTE CONGELADO CUESTA, DICHO Y NO CALLADO.** En el primero, **el censo
del arbol VIVO deja de correr dentro del arnes**; no se pierde, y se dice con su
nombre: vive en `scripts/loop/vuelta191_tarea3_censo.py`, que corre con
`--commit HEAD` y **no esta en la nomina**, que es donde tiene que vivir un
sujeto que se mueve. En el segundo, **el bloque `D` deja de lanzar
`tallar_cabecera_reporte.py --comparar`**, porque ese comando **RE TALLA leyendo
git en cada corrida** y su fila de identidad busca el asunto de un commit en una
ventana de `git log`: es sujeto vivo por dentro aunque el fichero comparado sea
fijo. **Tampoco se pierde:** el `--comparar` sobre el reporte VIVO sigue
corriendo cada vuelta en `cerrar_reporte.py`, que es su sede. **En su lugar el
bloque prueba algo mas estrecho y mas duro: que la comparacion es BYTE A BYTE,
mutando UN SOLO BYTE dentro de una linea sin cambiar ni el largo ni el numero de
lineas**, que es justo lo que una comparacion por lineas o por conteo no veria.

**b) EL TERCERO YA NO IMPRIME SU `mkdtemp`.** El directorio se sigue fabricando y
se sigue retirando (`P.16`), y se sigue comprobando que quedo retirado. Lo unico
que se calla es su nombre, **que es aleatorio por construccion y no prueba nada**.

**c) LA GUARDA QUE NO LO VIO, ARREGLADA, Y SIN AFLOJAR NADA.**
`guarda_de_entrada_a_la_nomina.py` gana el carril `--reproduccion`, que **corre
cada arnes reclamado DOS VECES y compara su salida sellada byte a byte**, mide
las selladas antes, y **restaura con `git checkout --` REMIDIENDO** antes de dar
nada por restaurado. **Y la corrida SIN esa bandera declara en su propia salida
que su columna de huella es UN INDICIO Y NO UN VEREDICTO DE REPRODUCCION**, con
la causa medida al lado. El carril es caro y por eso no corre por defecto: eso se
dice, no se esconde.

**LA VARA PARA LOCALIZAR LA SALIDA SELLADA VA EN DOS PASADAS, Y LA SEGUNDA NACIO
DE UNA MEDICION FALLIDA MIA.** Con la pasada del literal suelto, **los CUATRO
arneses reclamados salian `NO MEDIBLE`**, porque sus docstrings NOMBRAN otras
salidas de las que hablan. La pasada que manda mira **la asignacion de modulo
`SALIDA = os.path.join(LOOP, "...")`**, o sea la maquina y no la prosa. **Y la
sede por defecto del arnes iba mal**: buscaba en `docs/loop`, donde viven las
salidas, y los arneses viven donde `verificar_mutaciones_viejas.py` los busca.
Las dos correcciones van declaradas dentro del propio fichero.

**d) EL CASO POSITIVO POR MUTACION, Y CAE.** Se fabrican DOS arneses que **la
huella de texto ve EXACTAMENTE IGUAL** (los dos nombran `mkdtemp`) y que se
comportan al reves: uno escribe siempre lo mismo y el otro escribe una linea
distinta en cada corrida. **La huella dice `CONGELADO` de LOS DOS**, y la corrida
doble dice `reproduce=True` y `reproduce=False`. Mas la mutacion de que un arnes
que no nombre una sola salida sale `NO MEDIBLE` y **no se cuela como
reproducido**. Salida:
`docs/loop/SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA.txt`, **VEREDICTO: VERDE**.

**e) LA NOMINA NO SE TOCO.** Sigue en **127 entradas**, leidas de `VMV.VIEJAS` en
el bloque `H` del sello de apertura. No se poda, no se adelanta y no se le meten
entradas nuevas.

**UN CUARTO ARNES QUE NO REPRODUCIA, Y NO ESTABA EN EL ACTA. LO CAZO EL CARRIL
NUEVO EN SU PRIMERA CORRIDA DE VERDAD.** `vuelta191_tarea4_mutacion_veredicto.py`
imprimia **los bytes ABSOLUTOS de `cerrar_reporte.py`**, que crece cada vuelta.
Daba **6072 bytes las dos corridas y `sha256` DISTINTO**, porque las dos cifras
tienen el mismo numero de digitos: **una vara que solo mirase bytes lo habria
dado por bueno**. Su sujeto sigue vivo A PROPOSITO, porque lo que prueba es que
**la guarda de HOY** se puede quitar de una copia y que la copia compila. **La
reproduccion no se le exige al sujeto: se le exige a la SALIDA**, y lo que se
imprime ahora es la DIFERENCIA, que solo depende del trozo sustituido. Iba a
entrar en la bateria de la 194 exactamente igual que los otros tres.

**f) AL CERRAR, LOS CUATRO CORRIDOS DOS VECES, CON SUS BYTES Y SUS `sha256`.**
Tabla pegada de `docs/loop/SALIDA_V193_T2C_GUARDA_REPRODUCCION.txt` (4367 bytes),
que es el fichero del que sale y que existe y no esta vacio:

| arnes | sellada (LF, `sha256`) | corrida 1 | corrida 2 | reproduce | contra su sellada |
|---|---|---|---|---|---|
| `vuelta191_tarea3_mutacion_lineas.py` | 7246, `c053d5ebeee3afd2` | 7246, `c053d5ebeee3afd2` | 7246, `c053d5ebeee3afd2` | **True** | **True** |
| `vuelta191_tarea4_mutacion_veredicto.py` | 6426, `c7893936f11c7023` | 6426, `c7893936f11c7023` | 6426, `c7893936f11c7023` | **True** | **True** |
| `vuelta191_tarea6_mutacion_bloque_tallado.py` | 3976, `a5b846ea7deb3868` | 3976, `a5b846ea7deb3868` | 3976, `a5b846ea7deb3868` | **True** | **True** |
| `vuelta192_tarea4_mutacion_cuarta_puerta.py` | 4282, `4779fcd04bc5b2da` | 4282, `4779fcd04bc5b2da` | 4282, `4779fcd04bc5b2da` | **True** | **True** |

**CIFRA arneses medidos: 4. CIFRA NO MEDIBLES: 0. CIFRA QUE NO REPRODUCEN: 0.
CIFRA SIN RESTAURAR: 0. VEREDICTO DE REPRODUCCION: VERDE.** **NO HAY PARADA: la
194 no se abre con esto abierto.**

**LAS SELLADAS VIEJAS NO SE BORRAN, QUE UNA CORRECCION QUE TAPA LO QUE CORRIGE NO
SE PUEDE AUDITAR.** Los cuatro cortes anteriores quedan al lado con su nombre y
su vuelta: `SALIDA_V191_T3_MUTACION_LINEAS_CORTE_191.txt`,
`SALIDA_V191_T4_MUTACION_VEREDICTO_CORTE_191.txt`,
`SALIDA_V191_T6_MUTACION_BLOQUE_TALLADO_CORTE_191.txt` y
`SALIDA_V192_T3_MUTACION_ENTRADA_NOMINA_CORTE_192.txt`.

### TAREA 3. LA VARA DEL BANCO Y LA RELECTURA AL DOBLE. **CERRADA, Y LA VARA NUEVA NO ALCANZA A LA MITAD DE MIS DISCREPANCIAS.**

**a) EL CRITERIO, CITANDO `9.6.1` POR NUMERO Y CON LA FRASE COPIADA LITERAL.** Va
DENTRO del `CRITERIO` que se le pasa a `aislador_de_ciega.py`, o sea escrito en la
propia ciega y no en la cabeza del lector, y sale copiado en
`docs/loop/SALIDA_V193_T3_CIEGA.txt` (41185 bytes, `sha256` LF `fb9a9ed247ee550f`):

> **"Si lo que el hijo añade a lo que la madre ya dice CABE EN UNA LÍNEA, REPITE.
> Si trae un PROCEDIMIENTO que la madre no tiene, CONTINÚA."**

REPITE va a `A` y CONTINUA va a `D`, que es la lectura que la `4.9` adjudica. **No
se parafrasea** (`9.5.0`). **Y la vara vieja se nombra en vez de borrarse**: era el
solape de pasos, un literal privado que cada lector escribia por su cuenta.

**c) y d) EL TRAMO Y EL DOBLE, CONTADOS DE SUS FICHEROS.** De
`docs/loop/SALIDA_V193_T3_AISLAMIENTO.txt` (7653 bytes):

- **TRAMO: los 30 puestos de `docs/loop/SALIDA_V192_T2_CIEGA.txt`** (39850 bytes,
  `sha256` LF `da9b03300a305fbd`). **Y la ciega del auditor
  `docs/loop/_auditor_v193_ciega_blind.txt` trae los MISMOS 30**: no se creyo, se
  conto de su fichero, y el instrumento dice **ES EL MISMO CONJUNTO QUE EL TRAMO:
  SI**. **`1804` y `2833` estan los dos DENTRO del tramo.**
- **AL DOBLE: 30 vecinos deterministas**, con `vecinos()` **IMPORTADA** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`. **30 mas 30 son 60, el
  doble exacto.**
- **`evitar` cargado de OCHO ficheros, contados uno a uno y con sus nombres**, no
  de una lista tecleada: los seis de la 192 mas `_auditor_v192_ciega_blind.txt` y
  `SALIDA_V192_T2_CIEGA.txt`. **Universo consumido: 501 sin la tanda de la 192 y
  531 con ella.**
- **SOLAPE con el tramo: 0. SOLAPE con el universo: 0.** Los dos **POR
  CONSTRUCCION**: `evitar` va DENTRO de la llamada, no comprobado despues.

**e) EL ORDEN, QUE ES LA PRUEBA.** Criterio escrito literal; ciega y destape en
ficheros SEPARADOS; **mis 30 clases escritas y COMMITEADAS en su propio commit
`b57aa7d6` ANTES de abrir el destape**; y **mis OCHO dudosos NOMBRADOS DELANTE**
con el motivo de cada duda escrito: `203`, `718`, `967`, `2426` (donde digo `A` y
el otro lado podria traer procedimiento) y `132`, `972`, `1069`, `3171` (donde
digo `D` y lo que se anade podria caber en una linea).

**EL COTEJO, CON EL FORMATO UNICO YA ARREGLADO POR LA TAREA 5** y con `en dudosos`
pasado **COMO TEXTO** a proposito, o sea por el camino que reventaba. De
`docs/loop/SALIDA_V193_T3_COTEJO.txt` y su salida
`docs/loop/SALIDA_V193_T3_COTEJO_SALIDA.txt`:

| | cifra |
|---|---:|
| cotejados | **30** |
| coinciden | **23** |
| discrepan | **7** |
| dudosos marcados delante | **8** |
| discrepancias DENTRO de mis dudosos | **4** (`203`, `718`, `972`, `2426`) |
| discrepancias FUERA de mis dudosos | **3** (`158`, `612`, `651`) |
| reparto del lector | A 8, D 22 |
| reparto del archivo | A 6, B 3, D 21 |

**LAS TRES QUE CAEN FUERA DE MI MARCADO SE DECLARAN, Y CON ELLAS SE DISPARA LA
ESCALADA DE `AUDITOR.md` 1.2**: `158` (yo `A`, archivo `B`), `612` (yo `D`,
archivo `B`) y `651` (yo `D`, archivo `A`). **No las escondo tras el hecho de que
la vara sea nueva.**

**f) LO QUE LA VARA CAMBIA, MEDIDO Y NO AFIRMADO**, de
`docs/loop/SALIDA_V193_T3F_QUE_CAMBIA_LA_VARA.txt` (4168 bytes), contado de los
dos cotejos y no tecleado:

**A FAVOR DE LA VARA.** De mis **10** discrepancias de la 192, **4 estan DENTRO de
su alcance** (`1068`, `1804`, `1814`, `2833`) y **la vara resuelve BIEN las 3 que
el acta adjudica**: `1068` (yo `D`, archivo `A`, vara `A`), `1804` y `2833` (yo
`A`, archivo `D`, vara `D`). **Las tres son las que el criterio viejo no resolvia,
y dos de ellas son las que cayeron fuera del marcado de LOS DOS lectores.**

**EN CONTRA DE LA VARA, Y ES MI DATO PROPIO DE ESTA VUELTA. `9.6.1` TIENE DOS
SALIDAS Y NO PUEDE EMITIR `B` NUNCA.** Leyendo la tanda de la 193 **entera** con
ella emiti **CERO `B`** sobre un tramo donde **el archivo tiene TRES** (`158`,
`612`, `718`). **Y 3 de mis 7 discrepancias son exactamente eso**: un par que el
archivo llama `B` y que la vara solo sabe empujar a `A` o a `D`. En la 192 el
mismo agujero ya estaba: **6 de mis 10 discrepancias eran pares que yo llame `B`**
(`874`, `906`, `965`, `971`, `2425`, `2659`), y **la vara no las toca**.

**LA CONCLUSION, DICHA CON SUS DOS MITADES JUNTAS: la vara arregla el eje `A`
contra `D`, que es donde nos tumbo a los dos lectores, y no dice nada sobre el eje
que mas discrepancias me produce a mi.** No es una adjudicacion floja: es una
adjudicacion **cuyo alcance acaba de quedar medido**.

**LO QUE SI MEJORO, Y TAMBIEN ES MEDICION:** mi tasa pasa de **20 de 30** en la
192 a **23 de 30** en la 193, y mis dudosos bajan de **15 de 30** a **8 de 30**,
con la misma cifra de discrepancias fuera del marcado (**3** en las dos). **Un
criterio escrito reduce a la mitad lo que el lector tiene que marcar como duda.**

**NO SE TOCO NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` se abrio
**solo en lectura** y su `sha256` LF **abre y cierra en `0a77b5a35a962621`** por
las dos convenciones, medido en el aislamiento y otra vez en el cotejo.

### TAREA 5. EL COTEJO QUE NO CONVIERTE `"no"` EN `si`. **CERRADA EN VERDE.**

**LA CAIDA, CONFIRMADA CORRIENDOLA Y NO LEYENDOLA.** `bool("no")` en Python es
`True`, y eso se imprime dentro de la propia mutacion en vez de afirmarse.
`cuerpo_del_cotejo()` hacia `bool(du)`, y el docstring del formato especifica esa
columna como *"`en dudosos` . `si` o `no`"*: **la forma que el formato invita a
usar era justo la que reventaba.**

**a) `en_dudosos` SE NORMALIZA O CAE.** `normalizar_en_dudosos()` admite el
booleano de verdad, `0`/`1`, y las formas literales `si`/`sí`/`true`/`1` y
`no`/`false`/`0`, con la caja y los espacios normalizados **y nada mas**.
**Cualquier otra cosa levanta `EnDudososIlegible`**, que es una excepcion con
nombre propio y con la causa medida escrita en su docstring. Es la misma vara que
el caso `G` de la mutacion ya le aplicaba a `veredicto_de`: **lo raro sale a la
vista en vez de resolverse en silencio.**

**b) LA GUARDA DE `escribir_cotejo()` YA NO MIRA SOLO EL DENOMINADOR, Y SE DICE
POR QUE.** Sobre el fichero del auditor, **con las dos discrepancias de fuera
silenciadas, el denominador calzaba PERFECTAMENTE y la guarda daba VERDE**: un
denominador correcto sobre una columna falsa sigue siendo un verde falso. Ahora la
guarda **relee la columna `en dudosos` del disco y la coteja contra la que se le
paso**, normalizada, y publica tres cifras nuevas: puestos torcidos al escribir,
puestos que no volvieron del disco, y el reparto `si`/`no` del fichero. **Si algo
no calza, CAE y nombra los puestos.**

**c) EL CASO POSITIVO POR MUTACION, Y CORRE LOS DOS CAMINOS.** En
`docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt` (4881 bytes, **VEREDICTO:
VERDE**), bloque `H`. Se fabrica un cotejo con `no` **en texto** en el puesto que
DISCREPA:

- **camino de hoy**: dudosos **1**, DENTRO `[]`, **FUERA `[2]`**;
- **camino viejo**, corrido aqui y no citado: `bool()` sobre `['si', 'no', 'no']`
  da **`[True, True, True]`**, o sea marca los TRES como dudosos y la discrepancia
  le sale DENTRO. **LA MUTACION CAE.**
- Mas la mutacion de los valores raros: `'quiza'`, `''`, `None`, `7` y `[]`
  **LEVANTAN**; `'SI '` y `'No'` **si se leen**, porque la caja y los espacios son
  lo unico que se normaliza.
- Mas la mutacion de que `cuerpo_del_cotejo()` **entero** cae si una fila trae un
  valor ilegible, **en vez de escribir un fichero con la columna inventada**.

**d) EL COTEJO DEL AUDITOR, RE ESCRITO CON EL INSTRUMENTO ARREGLADO.**
`scripts/loop/vuelta193_tarea5d_rehacer_cotejo_auditor.py`, salida en
`docs/loop/SALIDA_V193_T5D_REHACER_COTEJO.txt` (2463 bytes) y fichero en
`docs/loop/SALIDA_V193_T5D_COTEJO_AUDITOR_REHECHO.txt`. **Se le pasa `en dudosos`
COMO TEXTO a proposito**, que es el camino que reventaba. **Su fichero no se
toca.**

| | obtenido | lo que el auditor publica a mano | |
|---|---:|---:|---|
| cotejados | 30 | 30 | **CALZA** |
| coinciden | 25 | 25 | **CALZA** |
| discrepan | 5 | 5 | **CALZA** |
| DENTRO de sus dudosos | `965, 1068, 1814` | `965, 1068, 1814` | **CALZA** |
| FUERA de sus dudosos | `1804, 2833` | `1804, 2833` | **CALZA** |

**Y LA MEDICION QUE SEPARA LOS DOS CAMINOS, SOBRE SUS 30 FILAS DE VERDAD:** el
camino viejo lee **`si` en 30 de 30** (el fichero trae 13 `si` y 17 `no`) y publica
**0 discrepancias FUERA**; el de hoy publica **2** (`1804`, `2833`). **La regla de
parada de `AUDITOR.md` 1.2 cuelga de esa cifra, asi que el camino viejo publicaba
un VERDE donde habia una escalada.**

**e) `cotejo_de_ciega.py` NACIO EN LA 192 Y TODAVIA NO HA ENTRADO EN LA NOMINA.**
El carril `--reproduccion` de la TAREA 2, corrido en esta vuelta, mide que **los
arneses que el censo RECLAMA son cuatro** y **ninguno de ellos es este fichero**.
**Tocarlo ahora es ANTES de que entre, y eso es a favor y no en contra:** entrara
ya con el `bool(du)` arreglado, con su guarda ensanchada y con su mutacion
cubriendo la columna. **Lo digo aqui para que no se lea como que le meti mano a
una entrada de la nomina.**

**Y EL CORTE VIEJO NO SE BORRA:** queda en
`docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO_CORTE_192.txt`, con su nombre y
su vuelta.

<!-- FIN ANEXO DE TAREAS -->
