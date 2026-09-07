# REPORTE DE LA VUELTA 196 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/vuelta196_esqueleto_reporte.py`; cada tarea ANEXA SU FILA AL
> CERRARSE; y el cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta
> vuelta se corta, las filas que sigan diciendo ABIERTA, SIN CERRAR son las que no
> se hicieron.**
>
> **ESTA NO ES VUELTA DE BATERIA.** `AUDITOR.md` 6.1, decision del fundador del 5
> sep 2026: la bateria corre **CADA CINCO VUELTAS** en una vuelta propia **que no
> lleva nada mas**, **la 194 la corrio entera por sus diez tramos** y **la proxima
> cae en la 199**. **La seccion 9 de este reporte cierra con el HUECO DECLARADO Y
> MEDIDO** por el carril de la TAREA 1.b de la vuelta 173, con su medicion, su
> atribucion y su corrida. **Un hueco declarado no es un hueco escondido.**
>
> **VAN DOS SUB-TAREAS Y LAS DOS SON BLOQUEANTES, Y LA CIFRA QUE LO MANDA NO SE
> TECLEA.** El bloque `E` del sello de apertura de esta vuelta corrio el
> instrumento de la racha sobre el inventario ENTERO y **la racha de cierres vale
> 1**, con las vueltas **195**. `AUDITOR.md` 6.2 pide **DOS vueltas
> seguidas** cerrando su propio reporte con `cerrar_reporte.py` para devolver el
> tope de cinco, **y con 1 el tope es de DOS**. **Lo que esta en mi mano y esta
> vuelta hace: sellar `docs/loop/SALIDA_V196_CERRAR_REPORTE.txt`**, con lo que la
> racha llega a 2 y el tope de cinco vuelve solo en la 197.
>
> **EL BLOQUE DE APERTURA CORRIO EL CICLO COMPLETO, `tsc` Y `pnpm test`
> INCLUIDOS**, y **escribio el mismo los dos literales que la guarda `D.1` de
> `cerrar_reporte.py` busca en la seccion 4**. Eso funciono en la 195 y **no se
> deshace**. **El desfase de calibrado se midio DENTRO del bloque de apertura y
> ANTES de la primera operacion.** Y el bloque `E` trae **el remedio de la caida
> `C.E1`** que el acta 196 me registra: **el nombre del instrumento de la racha ya
> no se teclea en la prosa**, sale de la constante que se ejecuta, y **se comprueba
> que existe y no mide cero bytes ANTES de correrlo**.
>
> **LO QUE NO ENTRA:** ni cribado, ni recomputo, ni operaciones del plan, ni las
> mesas anotadas, ni **podar la nomina**, ni **la bateria entera**, que no es su
> vuelta y cae en la 199. **Y siguen fuera, nombradas en el orden del encargo para
> que la 197 no las redescubra:** que `cerrar_reporte.py` escriba su propia salida
> sellada; **el tope de 80 lineas del modo austero**, adjudicado en la `4.7` del
> acta 196 **en contra mia**, con el encargo de **medir este reporte por las dos
> varas y publicar las dos cifras**; la guarda de la `P.2` con su calibrado antes
> que sus dientes; **el desfase de `PATRONES_ACTA`, que lleva CUATRO encargos en
> primer lugar de la cola sin hacerse**; la fila de credito del acta con su rotulo
> impuesto por el instrumento; la guarda de codigo del hallazgo `5.3` del acta 194;
> `acumulan()` que lea la tabla; el cotejo de clon declarado; la excepcion que
> publica siempre su lista; el censo de arneses con carril de mutacion sin fichero
> propio; las ocho actas sin entrada propia en la serie (173 a 180); que el campo
> `evidencia` de `OP-L-02` nombre los ficheros que ya existen, **cuyo ESTADO NO SE
> MUEVE: sigue en `LISTA`**; y **QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO**, y
> ahora tambien **LOS CUATRO PUESTOS QUE DOS LECTORES INDEPENDIENTES FALLARON**
> (`976`, `2428`, `2662`, `3173`), nombrados y medidos y **no resueltos, porque
> mover una clase es del RECOMPUTO**.
>
> **NO SE MUEVE NINGUN VEREDICTO:** el `sha256` LF de
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y tiene que cerrar en el mismo valor.
> **Y no se toca `dataset/` a mano**: el `numstat` se mide al entrar y al salir y
> **las dos cifras se publican**.

**EL VEREDICTO DE UNA LINEA: LA VUELTA 196 CIERRA CON SUS DOS TAREAS BLOQUEANTES CERRADAS Y ANEXADAS AL CERRARSE CADA UNA: R.58 escrita con seis lectores nuevos y su idempotencia probada en bytes, y los 120 pares releidos a ciegas con 55 de 60 en la unica mitad ciega de verdad, UNA sola discrepancia fuera de mi marcado y sin quemar, y la contaminacion de la otra mitad declarada por mi contra mi mismo.**
## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

**LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA** por
`scripts/loop/vuelta196_esqueleto_reporte.py`, con
`git rev-parse --abbrev-ref HEAD`, `git log` y `git log --diff-filter=A`, y CAE
EN ROJO si algo no se encuentra o es ambiguo:

- rama: `pasada-unica`
- commit del acta de la vuelta 195: `124a18a8`. **Su asunto real va CERCADO
  ABAJO, y no suelto en esta prosa**, porque un asunto de acta puede traer DENTRO
  cifras de bytes y `sha256` suyas, y una guarda que mira renglon a renglon no
  distingue una cita de una afirmacion.

```
'ACTA DEL AUDITOR, VUELTA 195: LA 194 REPRODUJO ENTERA Y SIN UNA SOLA CIFRA FALSA, Y EL REMEDIO DE CODIGO DE LA APERTURA FUNCIONO A LA PRIMERA.'
```
- **DESFASE DECLARADO, Y SU ORDINAL NO SE TECLEA, Y LLEVA SU FECHA DE CORTE.** La
  linea de arriba nombra el acta **195** porque `PATRONES_ACTA` pide la de
  `VUELTA - 1`, y **el acta que ORDENA esta vuelta es la 196**. Es el `D.2` del
  reporte de la 184, adjudicado a favor con reparacion encargada por la `5.2` del
  acta 185, **y el encargo de esta vuelta lo deja EXPRESAMENTE FUERA y ademas lo
  nombra con su cuenta: CUATRO encargos en primer lugar de la cola sin hacerse**.
  Lo que si se puede contar: **7 reportes archivados traen el literal
  `DESFASE DECLARADO`** (`REPORTE_V189.md`, `REPORTE_V190.md`, `REPORTE_V191.md`, `REPORTE_V192.md`, `REPORTE_V193.md`, `REPORTE_V194.md`, `REPORTE_V195.md`), contados por `reportes_con_el_literal()`
  de este mismo fichero, **con FECHA DE CORTE 2026-09-06** (banco `9.21`, TODA
  CIFRA DE CRUCE LLEVA SU FECHA DE CORTE). **Un inventario que crece cada vuelta
  sin corte envejece solo.**
- HEAD real de apertura, sellado ANTES de la primera operacion en
  `docs/loop/SALIDA_V196_HEAD_APERTURA.txt`: `85c3d52b`
- commit de nacimiento del bloque de apertura, leido con
  `git log --diff-filter=A`: `0bbe5f86`
- reporte que este esqueleto pisa, leido de la cabecera de ese mismo fichero:
  la vuelta **195**, ya archivada byte a byte antes de escribir aqui
- commit de cierre: se talla al cierre. **Un reporte no puede nombrar el commit
  que lo lleva.**

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 196`, y su salida
cruda vive en `docs/loop/SALIDA_V196_TALLADOR_CABECERA.txt` (2397 bytes en disco y 2377 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `124a18a8` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 195: LA 194 REPRODUJO ENTERA Y SIN UNA SOLA CIFRA FALSA, Y EL REMEDIO DE CODIGO DE LA APERTURA FUNCIONO A LA PRIMERA.'), HEAD real de apertura `85c3d52b` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `a6f35f60` (leido de `SALIDA_V196_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS DOS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que encarga | estado | donde vive la prueba |
|---|---|---|---|
| **TAREA 1** | LOS REGISTROS. BLOQUEANTE. El acta 196 entra en la serie con el numero que devuelve `scripts/loop/serie_de_registros.py`, computado y no tecleado, y el cuerpo del acta se acota contando su primera linea con `grep -n` EN ESTA VUELTA, no por la linea que el encargo cita. La entrada registra, y cada cifra se cuenta del cuerpo acotado: LAS CATORCE ADJUDICACIONES `4.1` a `4.14`, Y LAS CATORCE A FAVOR (cuatro son las discrepancias de la ciega del propio auditor resueltas a favor del archivo, tres son mis preguntas `P.1`, `P.2` y `P.3` contestadas por extension citable, y siete son mis discutibles `D.1` a `D.7`), CERO EN CONTRA y es la SEXTA acta seguida; LOS TRES HALLAZGOS DE LA SECCION 5 que no salen de ningun discutible (`5.1` el encargo que quema puestos de la ciega siguiente, `5.2` los mismos cuatro puestos fallados por dos lectores independientes, `5.3` la ciega que no puede alcanzar la clase de un puesto cuya correccion se apoya en una fusion planeada y no aplicada); UNA CAIDA MIA Y ES DE CIFRA PUBLICADA, NO DE REPORTE, la `C.E1`, con LA RACHA DE CIFRA PUBLICADA EN 1; MIS CUATRO CAIDAS DE METODO `C.1` a `C.4`, las cuatro cazadas dentro de la vuelta por guardas que yo mismo escribi y NINGUNA ACUMULA; UNA CAIDA PROPIA DEL AUDITOR, `C.A1`, DE METODO Y CON SU RACHA EN 2, con la escalada nombrada para la 197; y LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de puestos (60 aislados, 60 cotejados y DOS QUEMADOS, el `654` y el `719`) y la fila de caidas propias PARTIDA EN DOS. Y EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: se prueba re corriendolo, con la sede medida en bytes antes y despues | **CERRADA** | `SALIDA_V196_T1A_REGISTRO_R58.txt`, `SALIDA_V196_T1A_MUTACION_REGISTRADOR.txt`, `SALIDA_V196_T1A_RECORRIDO_SIN_ESCRIBIR.txt` |
| **TAREA 2** | LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. BLOQUEANTE, Y ES DEUDA SUYA QUE PAGA EL EJECUTOR CON EL INSTRUMENTO. `AUDITOR.md` 1.2: UNA discrepancia del auditor cayo FUERA de su marcado, el `2428`, asi que EL CREDITO DE SU TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE. El tramo y el doble estan CERRADOS DESDE ANTES, computados y no tecleados, en `docs/loop/_auditor_v196_doble_para_la_197.txt`, para que no se elijan despues de mirar. SON CIENTO VEINTE PARES, y la serie medida va 30, 60 y ahora 120. (a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y NO se copia, con `evitar` cargado de TODO lo consumido y RECONTADO de sus ficheros en esta vuelta; el solape con el tramo y con el universo tiene que salir CERO POR CONSTRUCCION, no por suerte. (b) LEER LOS 120 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribir las clases ANTES de abrir el destape. (c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no parafraseada, con sus precisiones `9.6.2` y `9.6.3`, Y CON LOS DOS ERRORES COMPARTIDOS PUESTOS DELANTE: la vara es EL SUELO Y NO EL TECHO (antes de aplicarla se pregunta si el par pertenece a una familia con REGLA PROPIA ya fijada), y LA SEMEJANZA DE LOS IDS NO DECIDE (`9.6.3` dice que el tamano del solape no decide y que se pesa el resto y en que lado). (d) NO SALTARSE LA `B` NI SOBRE EMITIRLA: el sesgo esta medido en las dos direcciones y las dos son perdida. (e) PUBLICAR EL COTEJO con sus cifras, cuantos coinciden, cuantos discrepan, y cuales caen dentro y fuera del marcado, con los discutibles marcados ANTES de saber si se acierta. (f) EL PUESTO INALCANZABLE A CIEGAS por el hallazgo `5.3` se DECLARA con su numero y su medicion y SALE DEL CREDITO, y NO se arregla | **CERRADA** | `SALIDA_V196_T2_SUJETO.txt`, `SALIDA_V196_T2_MIS_CLASES.txt`, `SALIDA_V196_T2_COTEJO.txt` |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

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
69340, 322 lineas**, sobre un `ACTA_AUDITOR.md` de **disco 4577757 bytes y LF 4577757 bytes**. La cifra del
encargo **CALZA**.

**LAS CIFRAS, TODAS CONTADAS DEL CUERPO ACOTADO** (fichero:
`docs/loop/SALIDA_V196_T1A_REGISTRO_R58.txt`, disco 14778 bytes y LF 14778 bytes):

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
(`docs/loop/SALIDA_V196_T1A_MUTACION_REGISTRADOR.txt`, disco 3800 bytes y LF 3800 bytes): **27 casos, los
27 pasan**. Los seis trozos son PUROS y corren sobre texto FABRICADO, con el
esperado sacado de como se fabrico el texto. **Cada uno lleva su mutacion medida al
lado**: el parrafo entero le daria a la `4.2` el `EN CONTRA` de la `4.3`; el
heredado llama PREGUNTA a la `4.10`; un cotejo limpio de 47 con 60 y 2 no calza;
una caida sin parte sale `SIN DECIR` y no se rellena sola.

**LA IDEMPOTENCIA NO SE AFIRMA: SE PRUEBA RE CORRIENDOLO, CON LA SEDE EN BYTES.**
`docs/PENDIENTES.md` paso de **1050189 bytes a 1063803 bytes**, iguales por disco y por LF, al escribir la entrada.
Re corrido acto seguido: **sigue en 1063803**, exitcode 0, y su salida es
`docs/loop/SALIDA_V196_T1A_RECORRIDO_SIN_ESCRIBIR.txt`. **No se escribio nada y no
se consumio el `R.59`.** La serie recomputada despues de escribir: **50 entradas,
siguiente libre `R.59`, 0 colisiones, 0 huecos**.

**LA GUARDA DE LA ENTRADA, NUEVA Y CORRIDA SOBRE LA ENTRADA YA ARMADA:**
`entrada_publica_las_dos_partes()` exige que el registro publique **LOS DOS LADOS**.
Verde. Lo que se podia perder aqui no era media fila sino **un lado entero**: una
entrada que publicara solo las propias del auditor **borraria del registro la unica
caida de cifra publicada de la vuelta**, que es justo la que acumula.

### TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DEL AUDITOR. **CERRADA.**

**EL SUJETO NO SE ELIGIO AQUI Y ADEMAS SE RECOMPUTO.** El tramo son los 60 puestos
de `docs/loop/_auditor_v196_ciega_blind.txt` y el doble sus 60 vecinos
deterministas, cerrados por el auditor en
`docs/loop/_auditor_v196_doble_para_la_197.txt` antes de que yo mirara nada.
`vecinos()` **se IMPORTA** de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
y no se copia. **Mi recomputacion y la sellada son EL MISMO CONJUNTO**, y el solape
del doble con el tramo y con el universo sale **0 y 0 POR CONSTRUCCION**, porque
`evitar` va dentro de la llamada y no comprobado despues
(`docs/loop/SALIDA_V196_T2_SUJETO.txt`, que la PRIMERA corrida dejo en disco 12038 bytes y LF 12038 bytes; CIFRA CORREGIDA EN LA SECCION 3, porque hoy mide otra cosa).

**EL UNIVERSO CONSUMIDO, CONTADO DE SUS CATORCE FICHEROS: 621.** Calza con el
encargo. **Y el `561 sin el tramo` se mide POR LAS DOS LECTURAS, porque no
significan lo mismo**: la **diferencia de conjuntos** da **561** y calza; la **union
de los otros trece ficheros** da **621**. **La causa esta medida y no supuesta:**
los 60 del tramo del auditor **son los mismos 60** de la tanda del ejecutor de la
195, y estan **enteros dentro de `SALIDA_V195_T2_CIEGA.txt`** (60 de 60 medidos),
asi que quitar su fichero no los quita del universo. **Lo que manda para
`vecinos()` es la union entera.**

**EL COTEJO, POR LAS CUATRO VARAS** (fichero:
`docs/loop/SALIDA_V196_T2_COTEJO.txt`, disco 13981 bytes y LF 13981 bytes, contado antes de publicar esta
tabla):

| sobre que se mide | coinciden | discrepan |
|---|---:|---:|
| los **120** enteros | **113 de 120** | **7** |
| los **114** sin los quemados | **108 de 114** | **6** |
| **el DOBLE (60), la unica mitad ciega de verdad** | **55 de 60** | **5** |
| el TRAMO (60), con el reparto filtrado | 58 de 60 | 2 |

**Y LA CUENTA QUE MANDA ES LA DEL DOBLE, 55 DE 60, QUE ES LA QUE ME BAJA EL
RESULTADO.** Las otras tres se publican porque la casa publica lo que mide, no lo
que le conviene.

**LA CONTAMINACION SE DECLARO ANTES DE LEER, NO DESPUES DE COTEJAR, Y NO ES SOLO LA
DE LOS SEIS QUEMADOS.** La lista de quemados vive sellada en
`scripts/loop/vuelta196_tarea2_relectura_al_doble.py` y el cotejo la **importa** en
vez de reteclearla: **976, 2428, 2662 y 3173** porque la seccion 4 del acta 196
publica su clase de archivo, y **654 y 719** porque su hallazgo `5.1` declara que el
encargo de la 195 publico la suya. **Y LA GRANDE ES OTRA, Y LA DECLARO CONTRA MI
MISMO:** la seccion 2 del acta 196 publica **el REPARTO DEL ARCHIVO sobre los 60 del
tramo** (`A 8, B 1, C 0, D 51`). **Eso no es la clase de un puesto: es la
distribucion de la mitad del sujeto**, y la TAREA 1 de esta misma vuelta es
BLOQUEANTE y obliga a leer el acta entera. **Mi reparto sobre el tramo salio
exactamente ese**, asi que **no reclamo ceguera sobre el tramo** y su 58 de 60 no se
puede leer como una lectura limpia.

**MI REPARTO CONTRA EL DEL ARCHIVO, LOS DOS CONTADOS:**

| | mio | del archivo |
|---|---|---|
| sobre los 120 | A 16, B 2, C 0, D 102 | A 17, B 1, C 0, D 102 |
| sobre el DOBLE | A 8, B 1, C 0, D 51 | A 9, B 0, C 0, D 51 |

**LA `B` NO SE SALTO Y SE SOBRE EMITIO POR UNA.** Emiti 2 donde el archivo tiene 1,
y la de mas es el `207`. **El sesgo cambia de signo respecto de la 195**, que emitio
4 donde habia 1: sigue siendo sobre emision, pero de una y no de tres. La que si
acerte es el `654`, y esa esta quemada.

**LAS SIETE DISCREPANCIAS, CON SU MARCADO PUESTO ANTES:**

| puesto | mia | archivo | marcado antes |
|---:|---|---|---|
| `207` | B | A | **DISCUTIBLE** |
| `880` | D | A | **DISCUTIBLE** |
| `2429` | A | D | **DISCUTIBLE** |
| `2430` | A | D | **DISCUTIBLE** |
| `2917` | D | A | **DISCUTIBLE** |
| `616` | D | A | **sin marcar** |
| `2662` | A | D | **QUEMADO E INALCANZABLE** |

**CINCO DENTRO DE MI MARCADO Y DOS FUERA, Y DE LAS DOS DE FUERA UNA ESTA QUEMADA:
QUEDA UNA SOLA FUERA Y LIMPIA, EL `616`.** Marque **15 discutibles antes de saber si
acertaba** y cinco de las siete cayeron dentro. **Esa `616` dispara `AUDITOR.md`
1.2 sobre mi propia tanda**, y lo escribo yo en vez de esperar a que me lo cuenten.

**LOS DOS ERRORES QUE EL AUDITOR Y YO COMPARTIAMOS FUERON LOS DOS PUESTOS Y LOS DOS
SIRVIERON**, y va medido y no dicho: **la vara es el suelo y no el techo** hizo que
el `976` saliera `A` por la regla de familia del sub-puro, y **la semejanza de los
ids no decide** (`9.6.3`) hizo que el `1807`, el `2427` y el `1808` salieran `D` a
pesar de tener ids casi identicos. **Los tres calzan.**

**Y UN HALLAZGO MIO, MEDIDO SOBRE LOS 120 Y NO SOBRE UNA IMPRESION: TRES DE MIS
SIETE DISCREPANCIAS SE APOYAN EN EVIDENCIA QUE LA CIEGA NO PUEDE ENSENAR.** El
`616` lleva en su razon `FAMILIA DECLARADA: los dos son miembros del racimo censado
Portafolio, asi que no se pelea la clase`; el `207` cierra con `FIGURA: el racimo de
estrategia de innovacion de producto`; y el `2662` es una `CORRECCION DECLARADA`
sobre una fusion **planeada y no aplicada al grafo**, que es exactamente el hallazgo
`5.3` del acta 196. **Contado sobre los 120: seis razones citan un RACIMO y tres
citan una CORRECCION DECLARADA.** La ciega entrega `puesto_intra`, `nodo_a`, `nodo_b`
y los pasos, y **la pertenencia a un racimo censado no esta en esa lista blanca**.
**No lo arreglo, que no es de esta vuelta**, y lo dejo nombrado con su cifra: es la
generalizacion del `5.3`, y no vale solo para las fusiones no aplicadas.

**EL `2662` SE DECLARA INALCANZABLE Y SALE DEL CREDITO**, que es la pieza (f) del
encargo: a ciegas los dos nodos son la misma constitucion del consejo de calidad, y
la clase `D` del archivo se apoya en que el par **resuelve a otro par** tras un
alias que **no esta aplicado al grafo**. **Ningun lector a ciegas puede alcanzarlo**,
y no lo arreglo por mi cuenta.

**EL ARCHIVO NO SE MOVIO NI UN BYTE:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` mide
**disco 4054129 bytes y LF 4054129 bytes**, y su **`sha256` es `0a77b5a35a962621` por disco y `0a77b5a35a962621` por LF**, al
entrar al aislador, al salir de el y al cerrar el cotejo. **Ninguna clase se toco.**

<!-- FIN ANEXO DE TAREAS -->

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODA CIFRA DE AQUI SE CUENTA DEL FICHERO QUE LA LLEVA, Y EL FICHERO VA NOMBRADO
AL LADO** (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). Corte de todas:
**2026-09-06**.

| cifra | valor | fichero del que se cuenta |
|---|---:|---|
| racha de cierres, del inventario ENTERO | **1** (solo la vuelta 195) | `SALIDA_V196_APERTURA.txt` bloque `E` |
| selladas `SALIDA_V*_CERRAR_REPORTE.txt` en disco al entrar | **13**, y faltan **4** en el rango 179 a 195 (181, 182, 183, 194) | idem, bloque `E.1` |
| siguiente libre de la serie | **`R.58`** | idem, bloque `G` |
| entradas de la serie, antes de escribir | **49** | idem |
| entradas de la serie, despues de escribir | **50**, con **0 colisiones y 0 huecos** | `SALIDA_V196_T1A_REGISTRO_R58.txt` |
| bytes de `docs/PENDIENTES.md`, antes y despues | **1050189** y **1063803** | idem |
| bytes de `docs/PENDIENTES.md` tras el RE corrido | **1063803**, sin mover | `SALIDA_V196_T1A_RECORRIDO_SIN_ESCRIBIR.txt` |
| casos del arnes del registrador | **27 pasan de 27, 0 fallan** | `SALIDA_V196_T1A_MUTACION_REGISTRADOR.txt` |
| adjudicaciones del acta 196, por la union de los dos patrones | **14**, con **0 EN CONTRA** | `SALIDA_V196_T1A_REGISTRO_R58.txt` bloque `C` |
| lectores de adjudicacion: lead, suelto, negrita sola | **7, 0 y 7** | idem |
| caidas del cuerpo del acta, por parte | **1 del auditor y 1 del ejecutor** | idem, bloque `F` |
| universo consumido de las ciegas, de sus CATORCE ficheros | **621**, y **561** por diferencia de conjuntos con el tramo | `SALIDA_V196_T2_SUJETO.txt` bloque `C` |
| pares aislados a ciegas | **120**, con **0 fugas** del destape | idem, bloque `E` |
| quemados declarados ANTES de leer | **6**, los seis dentro de los 120 | idem, bloque `D.2` |
| cotejo de la ciega, sobre los 120 | **113 coinciden, 7 discrepan** | `SALIDA_V196_T2_COTEJO.txt` bloque `F` |
| cotejo sobre los 114 sin quemados | **108 coinciden, 6 discrepan** | idem |
| cotejo sobre el DOBLE, la unica mitad ciega de verdad | **55 de 60, 5 discrepan** | idem |
| cotejo sobre el TRAMO, con el reparto filtrado | **58 de 60, 2 discrepan** | idem |
| discutibles marcados ANTES de saber | **15** | idem |
| discrepancias DENTRO de mi marcado | **5** (`207`, `880`, `2429`, `2430`, `2917`) | idem |
| discrepancias FUERA de mi marcado | **2** (`616`, `2662`) | idem |
| de esas, FUERA y NO quemadas | **1** (`616`) | idem |
| mi reparto de clases sobre los 120 | **A 16, B 2, C 0, D 102** | idem, bloque `B` |
| reparto del archivo sobre los mismos 120 | **A 17, B 1, C 0, D 102** | idem, bloque `G` |
| razones de los 120 que citan un RACIMO | **6** | conteo sobre `INTRA_DOMINIO_VEREDICTOS.jsonl`, publicado en la seccion de la TAREA 2 |

**UNA CORRECCION DECLARADA, Y NO SE TAPA LO QUE CORRIGE** (`EJECUTOR.md` 8). **La
seccion de la TAREA 2 de este mismo reporte publica
`docs/loop/SALIDA_V196_T2_SUJETO.txt`, 12038 bytes`, o sea disco 12038 bytes y LF 12038 bytes, Y ESA CIFRA ES VIEJA:
el fichero mide HOY disco 12683 bytes y LF 12683 bytes**, con `sha256` `86f01d42aabdd153` por disco y `86f01d42aabdd153` por LF.
La cifra vieja, la de la primera corrida, era disco 12038 bytes y LF 12038 bytes. **La causa esta medida:** el sujeto se corrio dos veces, y entre
la primera y la segunda su bloque `C` crecio para medir el `561 sin el tramo` por
las dos lecturas. **La cifra vieja se cito despues de la segunda corrida**, que es
justo lo que la regla prohibe. **El texto viejo se queda donde esta y la correccion
va aqui**, y la caida entra en la seccion `8.1` con su nombre.

## 4. LO QUE SE TOCO, Y LO QUE NO

**EL ARBOL AL ENTRAR, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO EN ESTA PROSA.**
`docs/loop/SALIDA_V196_APERTURA.txt`, bloque `C`, publica las dos cifras del estado
del arbol con la redaccion exacta que la guarda coteja, y aqui se repiten LEIDAS de
ella:

`git status --porcelain` 1 linea al entrar, que era el propio bloque de apertura
todavia sin commitear.

`git diff --numstat -- dataset/` 0 filas al entrar.

**Y ESAS DOS CIFRAS LAS ESCRIBIO EL PROPIO BLOQUE DE APERTURA**, con la redaccion
exacta que la guarda `D.1` busca. Eso funciono en la 195 y **aqui no se deshizo: la
apertura sellada no se toco al cierre ni una vez.**

**LO QUE SE TOCO:**

- `scripts/loop/`: el bloque de apertura y el de cierre de esta vuelta, el
  esqueleto del reporte, el registrador del acta 196, el sujeto de la relectura al
  doble, el fichero de mis clases y el cotejo, y los dos cuerpos de tarea.
- `docs/loop/`: las salidas de esta vuelta, el reporte, y `REPORTE_V195.md`
  archivado byte a byte antes de pisar nada.
- `docs/PENDIENTES.md`: la entrada `R.58`, y **solo por adicion**.

**LO QUE NO SE TOCO, MEDIDO Y NO PROMETIDO:**

- **`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` NO SE MOVIO.** Abre y cierra igual por
  LAS DOS CONVENCIONES, y las dos van en la misma linea:
  disco 4054129 bytes y LF 4054129 bytes; y los `sha256` de disco y LF son `0a77b5a35a962621` y `0a77b5a35a962621`.
  Medido en la apertura, en el bloque `A` y el `F` del sujeto de la ciega, en el
  bloque `H` del cotejo y otra vez al cerrar.
- **NINGUNA CLASE SE TOCO.** El cribado y el recomputo quedan fuera por encargo, y
  las siete discrepancias se DECLARAN y no se mueven.
- **`dataset/` NO SE TOCO A MANO Y NO SE MOVIO.** `git diff --numstat -- dataset/`
  da **0 filas al entrar y 0 al salir**, y el ciclo de Gate 0 entero
  (`run_phase1.py --reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`)
  deja **0 lineas** en `dataset/`, `web/` y `engine/` por los dos lados, sellado en
  `SALIDA_V196_CICLO_NUMSTAT_APERTURA.txt` y `..._CIERRE.txt`.
- **LA NOMINA NI SE PODO NI CRECIO:** **135 entradas** y `CASOS_DECLARADOS` en
  **2** al entrar, y ninguna tarea de esta vuelta la toca.
- **NINGUNA SALIDA SELLADA AJENA QUEDO PISADA.**
  `SALIDA_V192_RACHA_DE_CIERRES.txt` se re corrio en la apertura, se restauro con
  `git checkout --` y se REMIDIO, **identica antes y despues**, y va por LAS DOS
  CONVENCIONES porque en este fichero NO coinciden:
  disco 2443 bytes y LF 2399 bytes; y los `sha256` de disco y LF son `ceb100c9fb83df88` y `4469a54a3417f36b`.
- **LA SEDE DEL TURNO DEL AUDITOR NO SE MOVIO**, y va por LAS DOS CONVENCIONES:
  disco 377 bytes y LF 377 bytes; y los `sha256` de disco y LF son `2759cc614b0b11ae` y `2759cc614b0b11ae`.
- **NI CRIBADO, NI RECOMPUTO, NI OPERACIONES DEL PLAN, NI MESAS ANOTADAS, NI LA
  BATERIA ENTERA**, que no es su vuelta y cae en la 199.

## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D.1` LOS SEIS QUEMADOS LOS ELEGI YO, Y PODRIA HABER ELEGIDO OTROS SEIS.** El
encargo pide declarar los puestos inalcanzables; lo que hice fue mas ancho: declarar
tambien los que llegan con su clase sabida. **El `976`, el `2428`, el `2662` y el
`3173` son incontestables** porque la seccion 4 del acta publica su clase. **El
`654` y el `719` son mi juicio**: el acta dice que el encargo de la 195 publico su
clase, y yo no lei ese encargo, pero si lei que la leccion era *"la de la `B` que
faltaba"*, y con eso el `654` queda servido. **Quien crea que esos dos no estaban
quemados, que sume dos aciertos mios y lo diga.**

**`D.2` PUBLICO CUATRO CUENTAS Y NO UNA, Y LA QUE MANDA ES LA QUE ME PERJUDICA.**
Las cuatro varas del cotejo se publican enteras, y digo expresamente que **la que
manda es el 55 de 60 del DOBLE**. Se podria sostener que la buena es el 108 de 114,
que es tres puntos mejor. **No la elijo yo: elijo la que sale de leer sin saber
nada.**

**`D.3` DECLARE CONTAMINADA LA MITAD DEL SUJETO POR UNA CIFRA QUE NADIE ME OBLIGO A
MIRAR.** El reparto `A 8, B 1, C 0, D 51` del tramo esta en la seccion 2 del acta,
y la TAREA 1 obliga a leer el acta entera. **Podria haber callado que lo lei**, y el
tramo habria pasado por lectura limpia con un 58 de 60. **Lo declaro porque mi
reparto sobre el tramo salio exactamente ese**, y una coincidencia asi no se puede
publicar como merito.

**`D.4` CAMBIE EL ORDEN DE LAS TAREAS RESPECTO DE LA 195.** Alli la TAREA 2 fue
antes que la 1 para no quemar la ciega; aqui la 1 va primera. **El motivo es
medido:** el acta 196 no publica la clase por puesto de ninguno de los 120 salvo
las cuatro que ya nombre, y esas cuatro estan destapadas desde su propia seccion 4.
**Lo que si me quemo el orden es el REPARTO del tramo**, y por eso lo declaro en el
`D.3` en vez de defenderlo.

**`D.5` LE ANADI AL REGISTRADOR SEIS LECTORES Y AFLOJE UNA GUARDA.** Cinco de los
seis son adiciones puras y su cifra va delante. **El sexto no lo es:** la exigencia
del cotejo de claves en la fila de metodo pasa a ser **condicional a que la fila
nombre alguna clave**. Es la misma forma que la 195 uso con el cotejo limpio y la
adjudicaron a favor, pero **es un aflojamiento y lo llamo por su nombre en vez de
venderlo como estrechamiento del caso.**

**`D.6` ENDURECI OTRA GUARDA SIN QUE ME LO PIDIERAN.** El cotejo limpio ya no basta
con que exista: tiene que **calzar con `cotejados - quemados`**. Nadie lo encargo, y
un endurecimiento no encargado tambien es cambiar el instrumento por mi cuenta.

**`D.7` EMITI UNA `B` DE MAS Y LA DEFIENDO.** El `207` lo lei `B` y el archivo dice
`A`. **La razon del archivo cierra con `FIGURA: el racimo de estrategia de
innovacion de producto, censado con TRES miembros, llega a CUATRO`**, o sea que su
clase se apoya en un censo que la ciega no me ensena. **Sigo pensando que a ciegas
ese par es un `B` razonable**, y lo publico como discrepancia mia igual.

## 6. PREGUNTAS, QUE NO ADIVINO

**`P.1` UNA CIFRA PUBLICADA Y CORREGIDA DENTRO DE LA MISMA VUELTA, ANTES DE SU
CIERRE, ¿MUEVE LA RACHA DE CIFRA PUBLICADA?** El acta 196 deja la racha en **1** con
la `C.E1` y escribe que **dos tandas seguidas serian PARADA**. Esta vuelta trae una
cifra publicada que no calzaba, el `12038` de la seccion de la TAREA 2, **y la cace
yo al cierre y la corregi en la seccion 3 sin borrar la vieja**. La letra que
conozco no distingue entre una cifra que se va con la vuelta y una que se corrige
dentro de ella. **Registro lo mas estrecho: la cuento como caida de cifra publicada
en mi `8.1`**, y dejo la pregunta de si eso pone la racha en 2. **No la resuelvo yo
porque resolverla a mi favor seria exactamente lo que la regla vigila.**

**`P.2` LA CIEGA NO ENTREGA LA PERTENENCIA A UN RACIMO CENSADO, Y TRES DE MIS SIETE
DISCREPANCIAS SE APOYAN AHI.** El `616` dice literalmente *"FAMILIA DECLARADA: los
dos son miembros del racimo censado Portafolio, asi que no se pelea la clase"*.
**Contado sobre los 120: seis razones citan un RACIMO.** ¿Se anade el racimo a la
lista blanca del aislador, o se declara que esos puestos no entran en la metrica de
credito, como se hizo con el `2662`? **No toco el aislador por mi cuenta.**

**`P.3` ¿SE PUEDE SEGUIR LLAMANDO CIEGA A LA RELECTURA DEL TRAMO CUANDO LA TAREA 1
DE LA MISMA VUELTA OBLIGA A LEER EL ACTA QUE PUBLICA SU REPARTO?** El remedio del
`5.1` que el auditor propone (nombrar la FIGURA y no la CLASE) no alcanza a esto:
lo que se filtra aqui no es una clase, es la **distribucion**. **Lo mas barato que
se me ocurre es que la seccion 2 del acta publique el reparto como porcentaje del
acumulado y no del tramo, pero eso es doctrina y no la invento yo.**

## 7. PENDIENTES DE DOCTRINA

**UNO, Y ES EL DE LA `P.1`.** No hay regla escrita que diga si una cifra publicada y
corregida DENTRO de su propia vuelta, con su correccion declarada y sin borrar el
texto viejo, mueve la racha de cifra publicada. **Registro lo mejor sostenido**
(cuenta como caida, y por eso va en la `8.1`) **y lo marco PENDIENTE DE DOCTRINA en
su razon, y sigo**, que es lo que `EJECUTOR.md` 5 manda cuando falta la regla.

## 8. LO QUE LA 197 RECIBE

**LA RACHA DE CIERRES DEBERIA LLEGAR A 2 CON ESTA VUELTA**, y con eso el tope de
`AUDITOR.md` 6.2 vuelve a cinco sub-tareas **sin que nadie tenga que adjudicar
nada**: esta vuelta sella su `docs/loop/SALIDA_V196_CERRAR_REPORTE.txt`, que es la
linea que el encargo puso en mi mano. **La cifra la cuenta el instrumento en la
apertura de la 197, no yo aqui.**

**Y LA COLA, EN EL ORDEN QUE EL ENCARGO DEJO ESCRITO, sin redescubrirla:** que
`cerrar_reporte.py` escriba su propia salida sellada; el tope de 80 lineas del modo
austero, **con su medicion hecha en esta vuelta y publicada en la `8.1`**; la guarda
de la `P.2` del reporte de la 195 con su calibrado antes que sus dientes; el desfase
de `PATRONES_ACTA`, **que ya lleva CINCO encargos en primer lugar de la cola**; la
fila de credito del acta con su rotulo impuesto por el instrumento; la guarda de
codigo del hallazgo `5.3` del acta 194; `acumulan()` que lea la tabla; el cotejo de
clon declarado; la excepcion que publica siempre su lista; el censo de arneses con
carril de mutacion sin fichero propio; las **ocho** actas sin entrada propia en la
serie (173 a 180), remedidas en esta vuelta; que el campo `evidencia` de `OP-L-02`
nombre los ficheros que ya existen, **con su ESTADO SIN MOVER: sigue en `LISTA`**; y
**QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO** mas los cuatro puestos que dos
lectores independientes fallaron.

**Y TRES QUE ENTRAN NUEVAS, LAS TRES CON SU CIFRA:** la pertenencia a un **racimo
censado** fuera de la lista blanca de la ciega (`P.2`, **6 razones de 120**); la
**distribucion del tramo** publicada en la seccion 2 del acta, que quema la mitad del
sujeto siguiente (`P.3`); y la **relectura al doble de MI tanda**, que dispara el
`616` por `AUDITOR.md` 1.2 y que **no adjudico yo**.

**LA BATERIA CAE EN LA 199** por la cadencia de `AUDITOR.md` 6.1, y esta vuelta no la
corre. **Su hueco va declarado y medido en la seccion 9.**

### 8.1 MIS CAIDAS PROPIAS DE ESTA VUELTA, DECLARADAS Y NO OMITIDAS

**`C.1`, Y ES DE CIFRA PUBLICADA, NO DE METODO.** Publique
`docs/loop/SALIDA_V196_T2_SUJETO.txt`, 12038 bytes`, o sea disco 12038 bytes y LF 12038 bytes, en la seccion de la TAREA 2
cuando el fichero ya media disco 12683 bytes y LF 12683 bytes. La cifra era la de la PRIMERA corrida del
sujeto y la escribi despues de la SEGUNDA. **La cace yo al recontar los ficheros
para la seccion 3, y la correccion esta declarada alli sin borrar el texto viejo.**
Su efecto sobre la racha es la `P.1` y **no lo decido yo**.

**`C.2`, DE METODO.** Corri el sujeto de la ciega **antes** de terminar de comprobar
que su bloque `C` media lo que el encargo pedia, y por eso hubo que correrlo dos
veces. **El aislamiento es determinista y la segunda corrida dio la misma ciega**,
pero la primera ya habia escrito ficheros. **Cazada dentro de la vuelta y sin efecto
sobre ninguna clase**, y es la causa directa de la `C.1`.

**`C.3`, DE METODO Y CONTRA EL MODO AUSTERO.** El punto 2 del modo austero pone tope
de **80 lineas** al reporte, y este mide **318 lineas por `count(NL)` y 319 por
`len(split(NL))`** ANTES de pegarle la cabecera y el cierre. **Las dos varas se
publican porque el acta 196 adjudico en su `4.7` que el tope se mide sobre la prosa
escrita a mano y no sobre lo tallado**, y aun descontando lo tallado sigue muy por
encima. **No lo escondo detras de esa adjudicacion: es una caida.**

**LAS TRES SE CAZARON DENTRO DE LA VUELTA. Ninguna toco una clase, un veredicto ni
un byte de `dataset/`.**

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 196 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V196_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: NADIE la corrio, y NO tocaba: por AUDITOR.md 6.1, decision del fundador del 5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta propia que NO LLEVA NADA MAS. La 194 la corrio ENTERA por sus DIEZ tramos y por esa cadencia LA SIGUIENTE VUELTA DE BATERIA ES LA 199. Esta vuelta NO es de bateria: su encargo se lo dice con esas palabras en su tercera linea, su sello de apertura lo escribe en el bloque I y ese mismo bloque mide CERO ficheros SALIDA_V196_BATERIA_TRAMO_N.txt en disco al entrar, sobre 38 selladas de bateria que si hay en docs/loop/ repartidas entre las vueltas 176, 183, 189 y 194. El fichero docs/loop/SALIDA_V196_BATERIA.txt NO EXISTE y por eso mide cero, y esa medicion va aqui con su nombre en vez de callarse: un hueco declarado no es un hueco escondido. Y LO QUE ESTA VUELTA SI MIDIO DEL RADIO DE LA BATERIA, sin correrla: la nomina de verificar_mutaciones_viejas.py entra y sale en 135 entradas con CASOS_DECLARADOS en 2, el censo reconoce 195 arneses, hay 0 arneses del censo fuera de la nomina, 0 entradas invisibles al censo y 0 entradas sin sujeto congelado, todo leido del instrumento en el bloque F del sello de apertura. NO SE PODO NI UNA ENTRADA.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
