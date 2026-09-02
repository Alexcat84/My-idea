# REPORTE DE LA VUELTA 140

**Rama `pasada-unica`. Fase III, EJECUCION, fase 06 MESAS. Regimen completo: el
modo austero sigue suspendido por su propio punto 5.** Corte de todas las cifras
de esta pagina: **2 sep 2026**, salvo donde se diga otra cosa.

**LA VUELTA ENTREGA LA 0, LA 1, LA 2 Y LA 4 ENTERAS, Y DE LA TAREA 3 ENTREGA TRES
DE LAS CINCO REMITIDAS Y TRAE DOS COMO PARADA.** Y lo que el encargo pedia
comprobar por encima de todo: **la fase 06 NO cierra hoy** (medido al cierre en
`SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt`, que deja sin cumplir a `OP-M-01`,
`OP-M-04` y `OP-E-04`), **y esta vez la frase no la escribe nadie: la computa un
instrumento.**

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 140 --fase04` da **VERDE
EXIT 0** y su tabla se pega entera, sin tocar una celda. Salida en
`SALIDA_V140_TALLADOR_CABECERA.txt`.

<!-- CABECERA TALLADA -->

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.171 / 682 | **3.853 / 3.171 / 682** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.226 / 9.200 / 18.426 / 9.901 | **9.231 / 9.205 / 18.436 / 9.906** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+5 / +5 / +10 / +5** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `6ec25c1d` (asunto real leido de git log: 'ACTA DE LA VUELTA 139 DEL AUDITOR: EL DISCUTIBLE 1 GANA CONTRA MI ACTA 138, PERO LA FASE 06 NO CIERRA: LAS CINCO REMITIDAS DE LA VUELTA 118 TIENEN ONCE ARISTAS SIN ESCRIBIR. RACHA DE REPORTE EN DOS Y ESCALADA ENCARGADA.'), HEAD real de apertura `6ec25c1d` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `2730d6af` (leido de `SALIDA_V140_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

**EL DESFASE DEL CALIBRADO NO SE MUEVE:** las mismas cuatro filas al abrir y al
cerrar. Las escrituras de esta vuelta no tocan ninguna fila del calibrado.

## 1. TAREA 0, EL BLOQUE DE APERTURA. ENTERA, CON LOS DIEZ.

Los **DIEZ** `SALIDA_V140_*_APERTURA.txt` en **UN SOLO COMMIT**, `2e2ad80b`, hijo
directo de `6ec25c1d`, el acta de la vuelta 139, y antes de la primera operacion.
`verificar_apertura_sellada.py --vuelta 140` da **VERDE EXIT 0** con los diez
dentro, al abrir (`SALIDA_V140_TAREA0D_APERTURA_SELLADA.txt`) y otra vez al
cerrar (`SALIDA_V140_CIERRE_APERTURA_SELLADA.txt`).
`verificar_cierre_sellado.py --vuelta 140`: **VERDE**
(`SALIDA_V140_CIERRE_SELLADO.txt`).

## 2. TAREA 1, LOS TRES REGISTROS. ENTERA, Y LOS TRES POR ADICION PURA.

| registro | fichero | numstat |
|---|---|---|
| **R.21** (las siete adjudicaciones del acta 139, las dos caidas del ejecutor, LAS TRES DEL AUDITOR y la racha en DOS con su escalada) | `docs/PENDIENTES.md` | **170 anadidas / 0 borradas** |
| **CORRECCION 11** (la cifra del propio auditor: TRES grupos contra CUATRO) | `docs/plan/CORRECCIONES_A_APLICAR.md` | **144 anadidas / 0 borradas, junto con la 12** |
| **CORRECCION 12** (la entrada de fase 04 de la perdida de nombre, con el remedio literal del banco 9.28 dentro) | `docs/plan/CORRECCIONES_A_APLICAR.md` | (en el mismo numstat) |

**Nada se sobreescribe y la cifra vieja no se borra:** la CORRECCION 11 publica
**TRES** (acta 138, corte 1 sep 2026) al lado de **CUATRO** (medicion del 2 sep
2026), dice que el proxy sintactico del que el acta se fio **no es ni necesario
ni suficiente**, y deja las dos con su autor y su corte.

## 3. TAREA 2, LA ESCALADA. ENTERA Y BLOQUEANTE, ANTES DE NINGUNA MESA.

### 3.a. EL ESTADO DE UNA FASE SE COMPUTA: `tallar_estado_de_fase.py`

Instrumento nuevo, nombre estable y sin numero de vuelta. Lee el catalogo de una
fase de **su fichero**: las operaciones cuya `fase` es esa, mas las remitidas por
escrito, y los dos registros de remision se **parsean**, no se teclean
(`00_INDICE.md:261` para las seis de la fase 03, y la seccion
`SEGUNDA MITAD, LAS CINCO REMITIDAS A LAS MESAS DE LA FASE 06` de
`04_ENLACES.md` para las cinco de la vuelta 118).

**LAS TRES MUTACIONES** (`SALIDA_V140_2A_MUTACIONES.txt`):

| caso | que prueba | veredicto |
|---|---|---|
| **(i)** | se le quita al grafo en memoria una arista presente, **elegida por computo y no tecleada**: cumplido baja de 9 a 8 y `OP-M-01-ESLABONES` sale NOMBRADA. Contraprueba con copia sin mutar: la cifra no se mueve | **VERDE** |
| **(ii)** | una remitida de mentira que no existe en `OPERACIONES.jsonl`: ROJO nombrandola, y sin mutar hay cero fallos | **VERDE** |
| **(iii)** | caso positivo sobre sujeto congelado, la fase 05 en el commit `e4464be5` con los cuatro blobs cotejados por sha256 | **NO CALZA. SE DICE Y SE PARA ESTE CASO** |

**LA (iii) NO CALZA Y AQUI VA ENTERO EL PORQUE, COMPUTADO Y NO OPINADO.** El
encargo espera que la fase 05 salga con todo su catalogo cumplido salvo
`OP-S-12`. Sale **cumplido 1** (`OP-S-01`) y **9 sin cumplir**, las nueve por
falta de vara. **Y NO ES UN DEFECTO DEL INSTRUMENTO, ES UNA PROPIEDAD DEL
SUJETO:** el propio caso imprime que `OP-S-05`, `OP-S-08`, `OP-S-11` y `OP-S-12`
tienen **HUELLA DE GRAFO IDENTICA** (`nodos`, `superviviente`, `aristas_nuevas` y
`eliminar`, los cuatro campos con los que el grafo se mide, vacios en las
cuatro). **Ninguna vara de grafo puede separarlas.** Lo unico que separa a
`OP-S-11` de `OP-S-12` es el campo `estado`, y el encargo dice expresamente que
el destino se mide **contra el grafo y NO contra `estado`**. Lo digo y paro **ese
caso**, no la tarea: las mutaciones (i) y (ii) muerden, y el instrumento hace
sobre la fase 06 exactamente lo que la escalada pedia.

**LAS VARAS, Y UNA ES MIA:** `FUSION` y `ENLACE` las escribio el encargo. La
tercera, **`MESA`**, es **lectura mia** y va como **DISCUTIBLE 1**: una mesa
tiene destino cumplido cuando lo tienen todas sus hijas del catalogo, leidas de
su campo `bloquea_a`. La cuarta, **`SIN VARA ESCRITA`**, no mide: **cae en NO
COMPUTABLE, se cuenta entre las que no cumplen y se nombra aparte** (**DISCUTIBLE
2**).

### 3.b. LA GUARDA DE CIFRAS APRENDE A LEER LAS AFIRMACIONES DE CIERRE

Es la caida 4.1 del acta 139 puesta donde ocurrio. Vocabulario **CERRADO y
escrito dentro del codigo**, con su docstring diciendo que es cerrado: sujetos
`fase` y `catalogo`, y ocho verbos. La regla son **dos cosas, las dos
objetivas**, y la guarda **no intenta distinguir una afirmacion de una
negacion**, que seria leerle la mente al que escribe: **(1)** toda frase de la
familia CITA un fichero de `tallar_estado_de_fase.py` en su ventana, y sin cita
es ROJO; **(2)** si el fichero citado dice `sin cumplir: N` distinto de cero, la
ventana **tiene que NOMBRAR LAS N**, y si calla alguna es ROJO nombrandola.

**POR QUE ESA SEGUNDA, Y ES UNA REPARACION QUE ME HALLE A MI MISMO CORRIENDO LA
GUARDA CONTRA ESTE REPORTE.** Mi primera version exigia `sin cumplir: 0` a secas,
y con esa regla **el reporte que dice la verdad caia en ROJO**: escribir *"la
fase 06 NO cierra"* citando `SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt`, que deja
sin cumplir a `OP-M-01`, `OP-M-04` y `OP-E-04`, era tan rojo como escribir
*"cierra"* sin citar nada. Una guarda que castiga igual a quien miente y a quien informa del
estado real no empuja a la honestidad: **empuja a no hablar del asunto**, que es
la ceguera del ramal (xxi) por otra puerta. Y la caida 4.1 nunca fue decir
*"cierra"*: fue decirlo **callando las cinco remitidas**. Bajo la regla reparada
esa frase da ROJO nombrandolas una a una.

**LO QUE LA REGLA SIGUE PERMITIENDO, dicho para que nadie la lea de mas:** un
texto que escriba *"cierra"* Y ADEMAS nombre las que faltan pasaria. Es prosa que
se contradice sola y que salta a la vista; lo que la guarda impide es lo que
**no** salta a la vista.

**LAS CINCO MUTACIONES, VERDE** (`SALIDA_V140_2B_MUTACIONES.txt`), sobre sujeto
fabricado y **retirado por P.16**: (a) frase de cierre sin cita, ROJO; (b) con
cita a un fichero que dice `sin cumplir: 3` y sin nombrarlas, ROJO **nombrando
las tres, leidas del fichero y no tecleadas**; **(b bis) la misma frase
nombrandolas, VERDE, que es justo el caso que mi primera version tiraba**; (c)
sin la frase, VERDE; (c bis) con cita a un fichero que dice `sin cumplir: 0`,
VERDE y cotejada.

**Y LA PRUEBA DE QUE SIRVE, sobre el sujeto real que la motivo**
(`SALIDA_V140_2B_SOBRE_REPORTE_139.txt`): corrida contra el reporte de la vuelta
139 **caza la caida 4.1 en sus dos sitios**, la linea 8 (la cabecera) y la
linea 391 (la conclusion), y otras cuatro de la misma familia.

**LA ARIDAD DE `verificar()` NO SE TOCA**, y se dice por que: dos llamadores
sellados de otras vueltas desempaquetan cuatro valores
(`vuelta135_2a_diagnostico.py:30` y `vuelta139_2b_mutaciones.py:136`). Las
afirmaciones cotejadas salen por un parametro opcional de recogida.

### 3.c. EL ANCLA DE LA 2.b DEJA DE MOVERSE

El bloque (iii) de `vuelta139_2b_mutaciones.py` deja de resolver su sujeto con
*el ultimo commit que toca el reporte* y lo clava en `23bde6cd:docs/loop/REPORTE.md`
con su sha256 cotejado en cada corrida. **Reanclado da exactamente lo que el acta
139 re-midio a mano** (`SALIDA_V140_2C_V139_2B_REANCLADO.txt`): guarda vieja
**10**, guarda nueva **26**, la ceguera perdia **16**, y **75 filas** de tabla en
el reporte de la 138.

El script entra en la nomina de `verificar_mutaciones_viejas.py`, que pasa a
**CINCO** y da **ANCLA PERDIDA 0** (`SALIDA_V140_2C_MUTACIONES_VIEJAS.txt`). Y la
prueba de que eso sirve de algo, con su contraprueba
(`SALIDA_V140_2C_MUTACION_ANCLA.txt`): con el sha256 cambiado sobre una copia, la
bateria lo clasifica **ANCLA PERDIDA** y no verde; con la copia intacta, **OK**.

**Y UNA RECURSION QUE LA PROPIA 2.c CREO, HALLADA CORRIENDOLA Y NO LEYENDOLA:**
la bateria pasa a correr el script y el script ya corria la bateria. Cortada con
`LOOP_BATERIA_EN_CURSO`, y el sub-caso omitido **se declara como OMITIDO POR
RECURSION**, nunca como verde.

**TRES SALIDAS SELLADAS DE LA VUELTA 135 CAMBIAN Y SE DECLARA:**
`SALIDA_V135_2E_MUTACION_1/2/3.txt`. Lo unico que cambia es la linea `COBERTURA`,
que ahora dice ademas cuantas afirmaciones de cierre se cotejaron. **Ningun
veredicto se mueve.**

## 4. TAREA 3, LAS CINCO REMITIDAS. TRES ENTREGADAS Y DOS PARADAS.

**LA TABLA SALE DEL INSTRUMENTO**, `SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt`, que
al cierre deja sin cumplir a `OP-M-01`, `OP-M-04` y `OP-E-04`.

| # | operacion | que se hizo | destino medido al cierre |
|---|---|---|---|
| 1 | `OP-M-03-ENLACES` | las dos escritas | **CUMPLIDO** |
| 2 | `OP-M-01-ESLABONES` | verificada, **no se re-escribe nada** | **PARADA: su verificacion 0 cae** |
| 3 | `OP-M-01-SEXTO` | poda del solape mas la arista | **CUMPLIDO** |
| 4 | `OP-E-05` | las dos que faltaban, resueltas por alias | **CUMPLIDO** |
| 5 | `OP-E-04` | **cero escrituras** | **PARADA: su verificacion 0 no se puede cumplir** |

### 4.1. LO QUE SE ESCRIBIO, Y CON QUE GUARDAS

`vuelta140_3_escribir_aristas.py` **importa el parser de aristas del instrumento
que MIDE**, para que el que cuenta y el que escribe no partan la ficha de dos
maneras. Siete guardas por arista, la operacion se escribe entera o no se
escribe, y **mutacion negativa en las tres**, siempre con cero escrituras.

- **`OP-M-03-ENLACES`.** Los tres extremos vivos y directos, leidos contra
  `pivote_estrategico` **tal como quedo en la vuelta 139** y no contra la ficha
  del 12 ago 2026.
- **`OP-M-01-SEXTO`.** **La poda se leyo contra el nodo de hoy y calza mejor que
  contra la ficha:** las dos mitades de lo podado viven literales en el
  superviviente de 17 pasos. **El paso podado no se eligio por su numero:** se
  busco por su contenido, salio uno solo y cayo en la posicion que la ficha
  nombra. Las cuatro piezas propias de `preservar` siguen enteras despues.
- **`OP-E-05`.** **La resolucion por alias no lo convierte en otra cosa, y lo
  medi antes de escribir:** siguen siendo cuatro direcciones entre nodos vivos y
  distintos, y **las dos lineas que justifican el mutuo estan vivas**: el paso 5
  del absorbido vive hoy en el paso 10 del superviviente, medido.

### 4.2. LAS DOS PARADAS, Y SON LA MISMA ESPECIE

**Las dos salen del mismo sitio: la fusion `OP-M-01-FUSION`, ejecutada en la
vuelta anterior, dejo cinco destinos colapsados en un solo nodo, y con ellos
pares que antes eran distintos.**

**PARADA 1, `OP-M-01-ESLABONES`** (`SALIDA_V140_3_PARADA_OPM01ESLABONES.txt`).
Sus dos aristas estan presentes, cada una una sola vez tras resolver y con el id
vivo escrito. Pero su verificacion 0 dice *"LA VUELTA NO EXISTE NI LITERAL NI
RESUELTA"* y **la vuelta existe**: `asignacion_recursos_en_gates ->
sistema_gates_go_kill`, medida contra git, la fabrico la redireccion de
`3f249a03` sobre una entrada que antes era `estructura_de_gates`.

**PARADA 2, `OP-E-04`** (`SALIDA_V140_3_PARADA_OPE04.txt`). Sus nueve pares
colapsan en ocho aristas distintas tras resolver. Cuatro ya estan, dos pasarian,
y **tres quedan bloqueadas porque su vuelta existe**: LD-42 (la fabrico la
fusion), LD-48 (su vuelta es LD-40 de su propia ficha) y LD-53 (su vuelta es
LD-45 de su propia ficha). **No escribo ni las dos que pasan**, porque LD-45 es
justamente la vuelta de LD-53 y escribirla sola seria elegir cual direccion
sobrevive.

**NINGUNA DE LAS DOS LA ARREGLO YO:** la ficha dice que la vuelta no debe
existir, pero no dice **quien la quita** ni si la regla de la escalera manda
sobre la redireccion de una fusion (`EJECUTOR.md` regla 5).

## 5. TAREA 4, LA RELECTURA AL DOBLE: TODA AFIRMACION DE CIERRE

**LA FASE 06 NO CIERRA, Y NO LO DIGO YO, LO DICE EL INSTRUMENTO**, corrido al
cierre y pegado de `SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt`, que deja sin cumplir
a `OP-M-01`, `OP-M-04` y `OP-E-04`:

```
CIFRA: operaciones del catalogo: 16 | con destino cumplido: 13 | sin cumplir: 3 | de ellas, sin vara escrita: 1
SIN CUMPLIR (3): OP-M-01, OP-M-04, OP-E-04
SIN VARA ESCRITA (1): OP-M-04
```

**LAS TRES QUE FALTAN, NOMBRADAS Y CON SU MOTIVO:** `OP-E-04` por su parada;
`OP-M-01` porque `OP-E-04` es hija suya; y `OP-M-04` porque **ninguna de sus
hijas esta en el catalogo de esta fase** (`bloquea_a` nombra `OP-S-12`, de la
fase 05, y `OP-U-01`, de la fase 03). Al abrir la vuelta eran **siete**; al
cerrar son **tres**.

**EL CAMPO `estado` SIGUE SIN TOCARSE** en las once (acta 139, adjudicacion 3.6).
**`OP-S-12` sigue al final de la pasada entera** por la atadura 2, y esta vuelta
no lo toca.

## 6. CORRECCIONES DECLARADAS

**Ninguna tapa lo que corrige.** Ademas de la 11 y la 12 de la TAREA 1, **tres de
mis propios instrumentos, las tres halladas CORRIENDOLOS y no leyendolos**:

1. **La guarda 6 del escritor media el TOTAL de duplicadas y no el DELTA**, y
   caia en ROJO por una duplicada **que ya estaba** en
   `pivote_estrategico.nodos_previos` (`mvp_concierge` y `concierge_mvp`
   resuelven al mismo destino), fabricada por una fusion anterior y con dueno
   escrito en `OP-S-12`. Una guarda que castiga a quien no lo hizo no es una
   guarda: es un bloqueo. Ahora mide el delta e **imprime las preexistentes**.
2. **Peor, y era un caso rojo que no podia caer:** la mutacion negativa del
   escritor elegia *un deprecado cualquiera*, y el primero por orden alfabetico
   (`6s_lugar_trabajo`) **es alias de un vivo**, asi que el resolutor lo revivia
   y la guarda pasaba con razon. Ahora elige, computandolo, uno que **sigue
   muerto tras resolver**.
3. **Un rotulo que afirmaba de mas:** el escritor imprimia *"los dos ids son
   VIVOS y directos"* cuando lo unico que habia comprobado era que no habia alias
   que resolver. Corregido a *"los dos ids son DIRECTOS"*.

**Y UNA DISCREPANCIA DE CONTEO CONTRA EL ACTA 139, DECLARADA Y NO COPIADA:** el
acta mide `OP-E-05` como **1 de 2** contando **cadenas** de `aristas_nuevas`; yo
cuento **pares dirigidos** y da **2 de 4**. Las dos son correctas sobre unidades
distintas, y el registro de la vuelta 117 en `04_ENLACES.md` ya usaba la mia
(*"1 de 4"*). El total de la fase pasa de dieciseis cadenas a
dieciocho direcciones por el mismo motivo. Va como **DISCUTIBLE 4**.

## 7. PENDIENTES DE DOCTRINA

**UNO, Y ES EL DE LAS DOS PARADAS.** No existe regla escrita para **una arista de
una sola direccion cuya vuelta nace de la redireccion de una fusion**. La regla
de la escalera dice que la vuelta es una instruccion falsa; la redireccion de una
fusion dice que una arista del absorbido pasa al superviviente. Cuando chocan,
**nadie ha escrito cual manda ni quien corta**. Queda **PENDIENTE DE DOCTRINA** y
es lo que las dos paradas piden.

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **LA VARA `MESA` ES MIA Y NO DEL ENCARGO.** El encargo escribio dos varas,
   fusion y enlace. Yo anadi que una mesa tiene destino cumplido cuando lo tienen
   sus hijas del catalogo, leidas de `bloquea_a`, apoyandome en la fila 6 del
   `00_INDICE` (*"sus operaciones hijas viven en las fases 3 y 4"*). Sin esa vara
   las cinco mesas caerian en el saco de las no medibles.
2. **`NO COMPUTABLE` CUENTA COMO `SIN CUMPLIR`.** Sostengo que *destino cumplido*
   es una afirmacion y que lo no medible no esta demostrado. Meterlo con las
   cumplidas seria la degradacion silenciosa del banco 9. El desglose se publica
   al lado para que nadie confunda **no cumplida** con **no medible**.
3. **PARE EL CASO (iii) Y NO LA TAREA 2.** El encargo dice *"si sale otra cosa,
   lo dices y paras"*. Pare **ese caso** y segui, porque su expectativa es
   inalcanzable por una propiedad del sujeto que el propio caso imprime, y parar
   la vuelta entera por eso habria dejado las remitidas otra vuelta mas sin
   tocar. **Puedo estar equivocado.**
4. **PARES DIRIGIDOS CONTRA CADENAS DE `aristas_nuevas`.** Ver la seccion 6.
5. **LA GUARDA DE CIERRE DISPARA DE MAS, Y A PROPOSITO.** Con el vocabulario
   cerrado caen tambien frases condicionales y asuntos de commit. Sostengo que el
   coste de un disparo de mas es una cita y el de un disparo de menos fue la
   caida 4.1. **El remedio de un rojo de esta clase es CITAR, jamas reescribir la
   prosa** (ramal (xxi)).
6. **LAS DOS PARADAS PODRIAN LEERSE COMO EXCESO DE CELO.** En `OP-E-04` dos de
   los nueve pares pasan todas las guardas y no los escribi. Sostengo que
   escribir LD-45 sin LD-53 es elegir direccion, pero **es defendible entregar
   LD-55, que no choca con nada**.
7. **MI LECTURA DE QUE `OP-E-05` SIGUE SIENDO EL MUTUO DE LA FICHA** pese a que
   un extremo es hoy un nodo fundido de 17 pasos. Me apoyo en su verificacion 2
   (*"los ids se escriben resueltos"*) y en que las dos lineas que lo justifican
   siguen vivas. **Un extremo mucho mas gordo cambia el peso del enlace, y eso no
   lo mide nadie.**
8. **MI PROPIO INSTRUMENTO DA `OP-M-01-ESLABONES` POR CUMPLIDA Y SU FICHA DICE
   QUE NO.** La vara que el encargo le escribio cuenta `aristas_nuevas`
   presentes; la ficha ademas exige que la vuelta no exista. **Hoy discrepan, y
   lo dejo discrepando en vez de ensanchar la vara por mi cuenta.**

## 9. PREGUNTAS PARA EL AUDITOR

1. **¿Quien corta la vuelta de las dos paradas, y que regla manda?** Es el
   pendiente de doctrina de la seccion 7, y por el sigue sin cerrar la fase 06,
   con las tres que `SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt` nombra todavia sin
   cumplir: `OP-E-04`, `OP-M-01` y `OP-M-04`.
2. **¿Debe `tallar_estado_de_fase.py` mirar tambien las `verificacion` de cada
   ficha, y no solo sus `aristas_nuevas`?** Hoy `OP-M-01-ESLABONES` sale cumplida
   con su ficha cayendo. No lo ensanche yo porque el encargo fijo la vara.
3. **¿Donde vive el destino de `OP-M-04`?** Sus hijas escritas viven fuera de la
   fase 06 (`OP-U-01`, de la fase 03, sigue `LISTA`). Mientras eso siga asi, la
   fase 06 no puede cerrar aunque `OP-E-04` se resuelva.

## 10. VERIFICACION DEL CIERRE

| guarda | veredicto | salida |
|---|---|---|
| `verificar_apertura_sellada.py --vuelta 140` | **VERDE EXIT 0**, los diez | `SALIDA_V140_CIERRE_APERTURA_SELLADA.txt` |
| `verificar_cierre_sellado.py --vuelta 140` | **VERDE** | `SALIDA_V140_CIERRE_SELLADO.txt` |
| `verificar_mutaciones_viejas.py` | **VERDE**, las cinco muerden, ANCLA PERDIDA 0 | `SALIDA_V140_CIERRE_MUTACIONES_VIEJAS.txt` |
| `tallar_cabecera_reporte.py --vuelta 140 --fase04` | **VERDE EXIT 0** | `SALIDA_V140_TALLADOR_CABECERA.txt` |
| `tallar_cabecera_reporte.py --comparar docs/loop/REPORTE.md` | **CABECERA IDENTICA AL TALLADOR**, nueve filas cotejadas, cero distintas, cero ausentes | `SALIDA_V140_CABECERA_COMPARADA.txt` |
| `verificar_cifras_del_reporte.py` **ampliada** | **VERDE EXIT 0** | `SALIDA_V140_CIERRE_GUARDA_CIFRAS.txt` |
| `tallar_estado_de_fase.py --fase 06_MESAS` | corrido al abrir y al cerrar | `SALIDA_V140_2A_ESTADO_FASE06_ANTES.txt`, `SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt` |

**LAS DOS CORRIDAS DEL INSTRUMENTO, CON SUS NOMBRES:** al abrir quedaban siete sin cumplir, `OP-M-01`, `OP-M-03`, `OP-M-04`, `OP-E-04`, `OP-E-05`, `OP-M-01-SEXTO` y `OP-M-03-ENLACES`, y al cerrar quedan tres, `OP-M-01`, `OP-M-04` y `OP-E-04`.

**LA LINEA `COBERTURA`, ENTERA Y CON SU LECTURA HONESTA:**

```
COBERTURA: 0 cotejadas / 0 exentas / 0 cifras | reparto: 0 POR ETIQUETA, 0 POR CONJUNTO, 0 sin linea CIFRA | de las cotejadas, 0 viven en una FILA DE TABLA | afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase.py: 13
```

Esa linea sale de `SALIDA_V140_CIERRE_GUARDA_CIFRAS.txt` y las afirmaciones que cuenta van todas contra `SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt`, que deja sin cumplir a `OP-M-01`, `OP-M-04` y `OP-E-04`.

**Y COMO SE ESCRIBIO ESA LINEA, porque tiene una trampa que declaro:** esa cifra
**mide al propio reporte**, asi que escribirla lo mueve. No se teclea: se corre
la guarda, se pega su linea entera y su palabra de recuento, y **se repite hasta
PUNTO FIJO**, que llego en la segunda iteracion. Si no hubiera convergido, la
regla que me di es decirlo y no publicar la cifra.

**UN CERO DE COBERTURA NO ES UN VERDE, ES UN PLATO VACIO** (ramal (xxi) del acta
136), y por eso lo explico en vez de publicarlo a secas: **el cuerpo de este
reporte, fuera de la cabecera delimitada, no trae ni un par numero-mas-unidad del
vocabulario cerrado de la guarda** (`fichero`, `par`, `grupo`, `grafia`,
`colapso`, `nodo`, `linea`, `arista`). **No lo evite a proposito**, y lo digo
expresamente porque esa es justamente la caida 4.1 del acta 136: las cifras de
esta vuelta son operaciones, aristas de una ficha, pasos y direcciones, y de esas
unidades solo `arista` esta en el vocabulario, en frases donde va sin numero
delante. **Las dos cifras que si lo traian se reescribieron cuando la guarda las
canto, y las dos veces por motivo declarado**: una era **el numero de una vuelta
leido como si fuera un recuento de colapsos**, un falso positivo del patron; la
otra contaba **direcciones y las llamaba pares**, que **no es la unidad
correcta** para una arista dirigida, y ademas no tenia fichero que la contara.

**LO QUE SI SE COTEJO, Y ES LO QUE ESTA VUELTA ANADE: TRECE AFIRMACIONES DE
CIERRE**, contra `SALIDA_V140_4_ESTADO_FASE06_CIERRE.txt` y contra
`SALIDA_V140_2A_ESTADO_FASE06_ANTES.txt`, que dejan sin cumplir a `OP-M-01`,
`OP-M-04`, `OP-E-04`, `OP-M-03`, `OP-E-05`, `OP-M-01-SEXTO` y `OP-M-03-ENLACES`,
y cada una publicando **lo que su fichero dice, computado y no tecleado**. La primera
version de ese rotulo imprimia *"todas contra un fichero que dice sin cumplir:
0"*, que **era falso** en cuanto una pasaba por nombrar las que faltan: es la
especie exacta de la correccion 2 de la vuelta 139, y se arreglo **en el codigo y
no en la frase**.

---

**Rutas tocadas:** `dataset/nodos/` (seis nodos), `dataset/metadata/master_graph.json`,
`web/lib/assets/`, `docs/PENDIENTES.md`, `docs/plan/CORRECCIONES_A_APLICAR.md`,
`docs/loop/` y `scripts/loop/`. **`docs/plan/OPERACIONES.jsonl` NO se toca.**
