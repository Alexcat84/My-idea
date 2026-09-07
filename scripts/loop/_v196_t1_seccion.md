### TAREA 1. LOS REGISTROS. **CERRADA.**

**EL ACTA 196 ENTRA COMO `R.58`, Y EL NUMERO NO SE TECLEA:** lo computa
`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes. El
bloque `G` del sello de apertura ya lo habia contado en **R.58** antes de la
primera operacion, y el registrador lo vuelve a contar al escribir: **49 entradas,
0 colisiones, 0 huecos**. **EL ENCARGO DE ESTA VUELTA NO ADELANTA NINGUN NUMERO**,
que es la diferencia con la 195.

**EL CUERPO SE ACOTO AQUI Y NO POR LA LINEA QUE EL ENCARGO CITA.** El encargo dice
que el acta empieza en la 69019 y manda recontarla porque el fichero puede haber
crecido. Recontada por `R92.cuerpo_del_acta` en esta vuelta: **lineas 69019 a
69340, 322 lineas**, sobre un `ACTA_AUDITOR.md` de **4577757 bytes**. La cifra del
encargo **CALZA**.

**LAS CIFRAS, TODAS CONTADAS DEL CUERPO ACOTADO** (fichero:
`docs/loop/SALIDA_V196_T1A_REGISTRO_R58.txt`, 14778 bytes):

| lo que se cuenta | del acta | lo que el encargo dice | |
|---|---:|---|---|
| adjudicaciones `4.1` a `4.14` | **14** | catorce | CALZA |
| de ellas EN CONTRA | **0** | cero, y sexta acta seguida | CALZA |
| discutibles `D.n`, todos A FAVOR | **7** | siete | CALZA |
| preguntas `P.1`, `P.2`, `P.3` | **3** | tres | CALZA |
| las que no son ni `D.n` ni `P.n` | **4** | las cuatro de su propia ciega | CALZA |
| hallazgos `5.1` a `5.3` | **3** | tres | CALZA |
| caidas del EJECUTOR en el cuerpo, de cifra publicada | **1** (`C.E1`) | una | CALZA |
| caidas propias del AUDITOR en el cuerpo | **1** (`C.A1`) | una, racha 2 | CALZA |
| racha de cifra publicada, leida de su celda | **1** | 1 | CALZA |
| racha de reporte, leida de su celda | **0** | (no la nombra) | medida |
| caidas de metodo del ejecutor, de su fila | **4** | `C.1` a `C.4` | CALZA |
| puestos: aislados, cotejados, quemados | **60, 60, 2** | 60, 60 y dos quemados | CALZA |
| actas 173 a 195 sin entrada propia | **8** | ocho (173 a 180) | CALZA |

**SEIS TROZOS NUEVOS, Y CADA UNO TRAE DELANTE LA CIFRA QUE LO OBLIGA.** El acta 196
escribe de formas que los lectores heredados no leen, y **ninguno se retira**:

1. **Las adjudicaciones vienen en DOS formas.** `4.1` a `4.7` son lead de parrafo;
   `4.8` a `4.14` son **clave sola en negrita dentro de UN SOLO parrafo**. Medido:
   `claves_entrecomilladas` da **7**, `claves_de_adjudicacion` da **0**, y
   `claves_en_negrita_sola()` da **7**. Union: **14**. Con el heredado y nada mas,
   el registro publicaria **7 donde el acta declara 14**.
2. **El estado puede vivir en el PARRAFO y no en el titulo.** Medido: con el titulo
   solo saldrian `SIN DECIR` **2** y el registrador **PARARIA**; **2** estados
   salieron del parrafo. **La tabla del registro publica de donde sale cada uno**,
   que es lo que impide que ensanchar la ventana sea aflojar la guarda: una muda en
   los dos sigue haciendo PARAR.
3. **Una marca de estado nueva, literal:** `VA CONTRA EL EJECUTOR`, que es como el
   acta contesta la `P.3`. El heredado dice `POR EXTENSION CITABLE` y el acta
   escribe *"CONTESTADA POR EXTENSION"*: saldria `SIN DECIR`.
4. **La familia sale de la PRIMERA clave que la adjudicacion nombra.** La `4.10`
   adjudica `D.3` y **cita** la `P.2`; el lector heredado da PREGUNTA. Medido: los
   dos discrepan en **1** de 14, y el heredado publicaria **una pregunta de mas y
   un discutible de menos**.
5. **Las caidas son titulares `###` con LETRA en la clave** (`C.E1`, `C.A1`).
   Medido: el lector heredado da **0** sobre esa seccion y el nuevo da **2**. Y la
   **parte sale de lo que cada titular dice de si mismo** (`DEL EJECUTOR` contra
   `MIA`), porque la seccion 3 guarda las de los dos lados bajo un titulo que no
   atribuye. **Una caida sin parte declarada hace PARAR.**
6. **El cotejo limpio no vive en la fila de puestos: vive en la seccion 2.** Con
   **2** quemados, el registrador de la 195 **PARARIA** aqui. Se busca en el acta
   entera (linea 69078, valor **58**) **y la exigencia se ENDURECE**: ya no basta
   con que el literal este, tiene que calzar con `cotejados - quemados`, que da
   **60 - 2 = 58**. **CALZA.** Eso la 195 no lo comprobaba.

**Y DONDE LA GUARDA SE ESTRECHA SE DICE, CON SU MEDICION:** la fila de caidas de
metodo del ejecutor **no nombra sus claves**, porque esas cuatro viven en el
reporte de la 195 y no en el cuerpo del acta. El cotejo heredado daria **0 contra
4**, o sea PARADA sobre un acta correcta. **La exigencia se hace condicional a que
la fila nombre alguna clave, y en esa rama sigue entera.** Lo que se estrecha es el
caso, no la guarda.

**EL CASO POSITIVO POR MUTACION, CORRIDO ANTES DE ESCRIBIR NADA**
(`docs/loop/SALIDA_V196_T1A_MUTACION_REGISTRADOR.txt`, 3800 bytes): **27 casos, los
27 pasan**. Los seis trozos son PUROS y corren sobre texto FABRICADO, con el
esperado sacado de como se fabrico el texto. **Cada uno lleva su mutacion medida al
lado**: el parrafo entero le daria a la `4.2` el `EN CONTRA` de la `4.3`; el
heredado llama PREGUNTA a la `4.10`; un cotejo limpio de 47 con 60 y 2 no calza;
una caida sin parte sale `SIN DECIR` y no se rellena sola.

**LA IDEMPOTENCIA NO SE AFIRMA: SE PRUEBA RE CORRIENDOLO, CON LA SEDE EN BYTES.**
`docs/PENDIENTES.md` paso de **1050189 a 1063803 bytes** al escribir la entrada.
Re corrido acto seguido: **sigue en 1063803**, exitcode 0, y su salida es
`docs/loop/SALIDA_V196_T1A_RECORRIDO_SIN_ESCRIBIR.txt`. **No se escribio nada y no
se consumio el `R.59`.** La serie recomputada despues de escribir: **50 entradas,
siguiente libre `R.59`, 0 colisiones, 0 huecos**.

**LA GUARDA DE LA ENTRADA, NUEVA Y CORRIDA SOBRE LA ENTRADA YA ARMADA:**
`entrada_publica_las_dos_partes()` exige que el registro publique **LOS DOS LADOS**.
Verde. Lo que se podia perder aqui no era media fila sino **un lado entero**: una
entrada que publicara solo las propias del auditor **borraria del registro la unica
caida de cifra publicada de la vuelta**, que es justo la que acumula.
