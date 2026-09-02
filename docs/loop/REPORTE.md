# REPORTE DE LA VUELTA 139

**Rama `pasada-unica`. Fase III, EJECUCION, fase 06 MESAS. Regimen completo: el
modo austero sigue suspendido por su propio punto 5.** Corte de todas las cifras
de esta pagina: **2 sep 2026**, salvo donde se diga otra cosa.

**LA VUELTA ENTREGA LA 0, LA 1, LA 2 Y LA 4 ENTERAS Y LA TAREA 3 COMPLETA: LAS
CINCO FUSIONES QUE QUEDABAN. LA FASE 06 CIERRA SU CATALOGO.** Y trae una
discrepancia grande contra el acta 138, marcada abajo como **DISCUTIBLE 1**.

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 139 --fase04` da **VERDE
EXIT 0** y su tabla se pega entera. Salida en `SALIDA_V139_TALLADOR_CABECERA.txt`.
**SALE POR PRIMERA VEZ EN TRES VUELTAS**, y sale porque el bloque de apertura
llevo los **DIEZ** nombres y no nueve: es la reparacion de la caida 4.4 del acta
138.

<!-- CABECERA TALLADA -->

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.183 / 670 | **3.853 / 3.171 / 682** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.197 / 9.181 / 18.378 / 9.835 | **9.226 / 9.200 / 18.426 / 9.901** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+29 / +19 / +48 / +66** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e8cf1552` (asunto real leido de git log: 'ACTA DE LA VUELTA 138 DEL AUDITOR: EL PENDIENTE DE DOCTRINA LO CIERRA P.13 CITANDOLA, NO HAY PARADA, Y EL HUECO MUERDE EN TRES GRUPOS Y NO EN DOS.'), HEAD real de apertura `e8cf1552` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `9f473ce0` (leido de `SALIDA_V139_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

**EL DESFASE DEL CALIBRADO SUBE Y SE DICE POR QUE:** la fila nueva es
`customer_validation -> establecer_linea_base_mvp`, y la produce la fusion
`OP-M-05-APERTURA` de esta misma vuelta al redirigir una arista de un absorbido
al superviviente. Es la figura que la adjudicacion 5.7 del acta 82 llama desfase
ESPERADO Y CORRECTO: el calibrado se commiteo tal como quedo tras una escritura
posterior a su recalibracion.

**HASH FINAL de la vuelta, tallado de git y no tecleado.** `git rev-parse HEAD`
leido al escribir esta linea, en la rama `pasada-unica`:

```
effa0d8b25b97c252b4b4c00a78de2e30270336c
```

**LOS COMMITS DE LA VUELTA**, de `git log e8cf1552..HEAD` (el acta de la 138
excluida). Son **12**, y el ultimo, el que escribe esta lista, no puede
aparecer en ella: es el carril de la vuelta 64 que el acta 137 ya verifico.

```
  effa0d8b REPORTE DE LA VUELTA 139: LAS TAREAS 0, 1, 2 Y 4 ENTERAS Y LA 3 COMPLETA. LA FASE 06 CIERRA SU CATALOGO, Y LA CABECERA VUELVE A SALIR.
  9f473ce0 VUELTA 139, TAREA 3, CIERRE DE REGISTRO: CORRECCION 10, LAS CINCO FICHAS DE LA FASE 06 CONTRA SU PROPIA EJECUCION.
  6c976514 VUELTA 139, TAREA 3, FUSION 5 DE 5: OP-M-05-APERTURA. LA FASE 06 QUEDA COMPLETA, Y AQUI VA MI DISCREPANCIA CON EL ACTA 138.
  4f2e151b VUELTA 139, TAREA 3, FUSION 4 DE 5: OP-M-05-EDIFICIO. EL MARGEN CORTO NO VOLTEA, Y UNA LINEA DE preservar QUE NINGUNA MARCA PUEDE CUMPLIR.
  c351cc30 VUELTA 139, TAREA 3, FUSION 3 DE 5: OP-M-05-INDICE. LAS TRES LINEAS SIN ID, LEIDAS CON EL OJO Y ADJUDICADAS CON VEREDICTO COMPUTADO.
  495c140e VUELTA 139, TAREA 3, FUSION 2 DE 5: OP-M-03-III, EL ACTO III DEL PIVOTE. LA QUINTA MARCA, DOS VECES Y EN LAS DOS DIRECCIONES.
  3f249a03 VUELTA 139, TAREA 3, FUSION 1 DE 5: OP-M-01-FUSION, LA CAMARILLA DE CINCO. EL ESTRENO DE VIAJA_EN_EL_ACTO.
  5979e3f7 VUELTA 139, TAREA 2.b: LA GUARDA DE CIFRAS DEJA DE SER CIEGA A LAS TABLAS. 10 CIFRAS VISTAS PASAN A 26.
  11b1f0d6 VUELTA 139, TAREAS 2.a Y 2.c: LA QUINTA MARCA VIAJA_EN_EL_ACTO, Y LA CIFRA QUE MENTIA EN SU NOMBRE.
  5fb86415 VUELTA 139, TAREA 1: LOS DOS REGISTROS, LOS DOS POR ADICION PURA.
  bf00a6cc VUELTA 139, TAREA 0.d: LA GUARDA DE LA APERTURA EN VERDE EXIT 0, CON LOS DIEZ DENTRO.
  a4968cd4 VUELTA 139, TAREA 0: EL BLOQUE DE APERTURA, SELLADO ANTES DE LA PRIMERA OPERACION, Y ESTA VEZ SON DIEZ.
```

## 1. TAREA 0, EL BLOQUE DE APERTURA. ENTERA, Y CON LOS DIEZ.

Los **DIEZ** `SALIDA_V139_*_APERTURA.txt` en **UN SOLO COMMIT**, `a4968cd4`, hijo
directo de `e8cf1552`, el acta de la vuelta 138, y antes de la primera operacion.
El decimo es `SALIDA_V139_DESFASE_CALIBRADO_APERTURA.txt`, que es exactamente la
celda que impidio tallar la cabecera en la 137 y en la 138.

`verificar_apertura_sellada.py --vuelta 139` da **VERDE EXIT 0** con los diez
dentro, corrida al abrir (`SALIDA_V139_TAREA0D_APERTURA_SELLADA.txt`) y otra vez
al cerrar (`SALIDA_V139_CIERRE_APERTURA_SELLADA.txt`).
`verificar_cierre_sellado.py --vuelta 139`: **VERDE**, `9f473ce0` es un commit
valido, en la rama, descendiente del acta y distinto de la apertura.

## 2. TAREA 1, LOS DOS REGISTROS. ENTERA, Y LOS DOS POR ADICION PURA.

| registro | fichero | numstat |
|---|---|---|
| **R.20** (las siete adjudicaciones del acta 138, las dos caidas del ejecutor, LAS DOS DEL AUDITOR y la guarda cegada) | `docs/PENDIENTES.md` | **132 anadidas / 0 borradas** |
| **CORRECCION 9** (la ficha de `OP-M-02-ACCLIMATE` contra su ejecucion) | `docs/plan/CORRECCIONES_A_APLICAR.md` | **100 anadidas / 0 borradas** |
| **CORRECCION 10** (las cinco fichas de la fase 06 contra su ejecucion) | `docs/plan/CORRECCIONES_A_APLICAR.md` | **111 anadidas / 0 borradas** |

**Ninguna ficha se toca y ningun veredicto viejo se borra.** Los indices de linea
de la ficha de `OP-M-02-ACCLIMATE` se contaron **con codigo sobre el JSON, no a
ojo**: la cifra de las duplicadas esta en `verificacion[6]` y la del cableado en
`evidencia[3]`.

## 3. TAREA 2, LAS TRES OPERACIONES DE CODIGO. ENTERA Y BLOQUEANTE, ANTES DE
NINGUNA MESA.

### 3.a. LA QUINTA MARCA, `VIAJA_EN_EL_ACTO`

Toca `generar_plan_de_fusion_de_mesa.py` (la marca, `viaja_a()`,
`validar_viaja_en_el_acto()` y el reparto impreso) y `fundir_por_plan.py` (el
cuarto destino: **la pieza NO se injerta y se anota donde vive**). Las guardas se
muerden **en las dos**, al sellar y al ejecutar.

**LOS OCHO CASOS, todos VERDE** (`SALIDA_V139_2A_CASOS_BCDE.txt`), sobre banco
propio y congelado, con el temporal retirado por P.16 y **cero ids que pisen el
catalogo, comprobado antes de empezar**:

| caso | que prueba | veredicto |
|---|---|---|
| (B) | la cuenta de la pieza en el superviviente resultante: **1 con la marca, 2 al cambiarla por un segundo APPEND** | VERDE |
| (C) | cadena que no llega a viajar, nombrando el par | VERDE |
| (D.1) y (D.2) | absorbido destino inexistente y paso destino inexistente, **ROJO nombrando los dos** | VERDE |
| (iii) | auto referencia | VERDE |
| (v.1) y (v.2) | sin linea editorial, y linea que no dice cual redaccion viaja | VERDE |
| (E) | cero escritura tras los seis rojos | VERDE |

**La cuenta del caso (B) la computa el fundidor de verdad corrido sobre el banco,
no un literal.** Y las dos redacciones de la pieza **no son iguales byte a byte a
proposito**: si lo fueran, la guarda 3 (cero repetidos LITERALES) ya las cazaria y
el caso no probaria nada nuevo.

**CASO (A), el positivo, que no fabrique porque ya existia**
(`SALIDA_V139_2A_CASO_A_POSITIVO_63_64.txt`, **EXIT 0**): los tres planes de las
vueltas 63 y 64 regenerados con el generador de HOY salen **IDENTICOS salvo la
fecha**. Y sus tres mutaciones viejas siguen mordiendo
(`SALIDA_V139_2A_MUTACIONES_VIEJAS_138.txt`).

**UNA DECISION DECLARADA Y ESCRITA EN EL CODIGO:** `lineas_de_viaje` **NO va
siempre** en el acto, al reves que `perdidas`. Un campo nuevo presente siempre
moveria esos tres planes sellados y **romperia el caso (A)**: la marca nueva no
puede mover el camino viejo.

### 3.b. LA GUARDA DE CIFRAS DEJA DE SER CIEGA A LAS TABLAS

Es la caida 4.5 del acta 138, de la casa. La cabecera tallada se **delimita** con
dos marcas literales y la guarda quita **solo** lo delimitado; **sin las marcas no
quita nada y recorre todas las filas**; con una sola, ROJO ruidoso.

**LA CIFRA QUE EL ENCARGO PIDE, medida contra el reporte de la 138 tal como esta
en git** (`SALIDA_V139_2B_MUTACIONES.txt`):

| | cifras que la guarda VE | fuente |
|---|---:|---|
| guarda VIEJA (blob del acta 138) | **10** | `SALIDA_V139_2B_MUTACIONES.txt` |
| guarda NUEVA (arbol de hoy) | **26** | `SALIDA_V139_2B_MUTACIONES.txt` |
| **las que la ceguera perdia** | **16** | `SALIDA_V139_2B_MUTACIONES.txt` |

**Cuadra al digito con lo que el auditor midio.** La nueva da ROJO sobre ese
reporte, **y eso es el exito**: entre sus rojos estan las cinco cifras en `grupos`
de la tabla de la fase 06, **la de la caida 4.2 incluida**. Los rojos se citan
enteros en la salida; no se debilito la guarda ni se borro la tabla.

**LO QUE CAMBIA Y NO SE ESCONDE:** sobre el sujeto congelado el veredicto pasa de
exit 0 a exit 1, y **no por ver mas cifras** sino porque al dejar de borrar las
filas de tabla la ventana amplia de la exencion (iii) cambia de vecinos. Es el
ramal (xix) mordiendo mas, no menos. **Las cuatro mutaciones viejas siguen
mordiendo con la guarda reparada, exit 0 y ANCLA PERDIDA 0.**

### 3.c. EL RENOMBRE DE `deriva`

`deriva` pasa a ser `contar_distintas_por_posicion()`, y **al lado se imprime el
numstat de git del mismo par de blobs**. Medido hoy y cuadra al digito con el
auditor: `PLAN_V63_OPM02PROG.json` da **14** posicionales contra **7 anadidas y 1
borrada**. La mutacion (`SALIDA_V139_2C_MUTACION_CIFRAS_DERIVA.txt`, EXIT 0)
muerde sobre **las dos cifras computadas**: la posicional se mueve al insertar
una linea y el numstat no, y da 0/0 contra si mismo.

## 4. TAREA 3, LA FASE 06. LAS CINCO, EN SU ORDEN Y CON SUS GUARDAS COMPLETAS.

**TODA ESTA SECCION SALE DE UN INSTRUMENTO, NO DEL TECLADO.** Las tablas las
imprime `scripts/loop/vuelta139_tabla_fase06.py` leyendo los ficheros de salida
de cada fusion, y se pegan enteras de `SALIDA_V139_4_TABLA_FASE06.txt`. **Es la
TAREA 4 hecha estructura en vez de atencion:** el instrumento cuenta las
duplicadas nombradas y las coteja contra el `TOTAL NUEVAS` del mismo fichero, y
cae en ROJO si discrepan, que es exactamente la especie de la caida 4.2.

| operacion | P.5 | caso positivo | crecimiento del superviviente | delta deprecados |
|---|---|---|---|---|
| `OP-M-01-FUSION` | 10 pares leidos = 10 del acto, EXIT 0 (`SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt`) | LAS NUEVE MUERDEN | 6 a 17 pasos, 3 a 6 condiciones | +4 |
| `OP-M-03-III` | 3 pares leidos = 3 del acto, EXIT 0 (`SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt`) | LAS NUEVE MUERDEN | 5 a 9 pasos, 2 a 2 condiciones | +2 |
| `OP-M-05-INDICE` | 3 pares leidos = 3 del acto, EXIT 0 (`SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt`) | LAS NUEVE MUERDEN | 5 a 9 pasos, 2 a 5 condiciones | +2 |
| `OP-M-05-EDIFICIO` | 3 pares leidos = 3 del acto, EXIT 0 (`SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt`) | LAS NUEVE MUERDEN | 4 a 8 pasos, 2 a 2 condiciones | +2 |
| `OP-M-05-APERTURA` | 3 pares leidos = 3 del acto, EXIT 0 (`SALIDA_V139_3_P5_LECTURA_DE_ACTO.txt`) | LAS NUEVE MUERDEN | 5 a 11 pasos, 2 a 2 condiciones | +2 |

| operacion | piezas | enteras (APPEND) | ya dichas (CUBIERTO) | de INCISO | que ya viajan en el acto |
|---|---:|---:|---:|---:|---:|
| `OP-M-01-FUSION` | 26 | 14 | 9 | 1 | 2 |
| `OP-M-03-III` | 16 | 4 | 10 | 0 | 2 |
| `OP-M-05-INDICE` | 12 | 7 | 1 | 0 | 4 |
| `OP-M-05-EDIFICIO` | 12 | 4 | 7 | 0 | 1 |
| `OP-M-05-APERTURA` | 12 | 6 | 5 | 1 | 0 |
| **TOTAL de las cinco** | **78** | **35** | **32** | **2** | **9** |

| operacion | guarda A auto-aristas | guarda B duplicadas tras resolver | guarda C | guarda D | duplicadas de la simulacion |
|---|---|---|---|---|---:|
| `OP-M-01-FUSION` | OK (0) | OK (0) | 5 de 5 | OK | 5 |
| `OP-M-03-III` | OK (0) | OK (0) | 5 de 5 | OK | 2 |
| `OP-M-05-INDICE` | OK (0) | OK (0) | 5 de 5 | OK | 4 |
| `OP-M-05-EDIFICIO` | OK (0) | OK (0) | 5 de 5 | OK | 1 |
| `OP-M-05-APERTURA` | OK (0) | OK (0) | 5 de 5 | OK | 6 |

**En las cinco: cero auto aristas nuevas, cero aristas internas del acto que
sobrevivan, y CERO DUPLICADAS NUEVAS TRAS RESOLVER**, que es la cifra que de
verdad importa para el catalogo. **Cada fusion llevo su ciclo de Gate 0 con las
tres suites detras, y las cinco veces salio `GATE 0: OK`, motor 25/25, vitest
80 de 80 y tsc EXIT 0.**

### DONDE MUERDE EL HUECO, CON SUS PARES NOMBRADOS

| operacion | VIAJA_EN_EL_ACTO | los pares, del fichero del plan |
|---|---:|---|
| `OP-M-01-FUSION` | 2 | paso 2 de `requisitos_gates_con_dientes` viaja por el paso 1 de `estructura_de_gates`; paso 1 de `estructura_gates` viaja por el paso 1 de `estructura_de_gates` |
| `OP-M-03-III` | 2 | paso 2 de `pivote_startup` viaja por el paso 3 de `pivotes_e_iteraciones`; paso 4 de `pivotes_e_iteraciones` viaja por el paso 3 de `pivote_startup` |
| `OP-M-05-INDICE` | 4 | los cuatro pasos de `customer_discovery_overview` viajan por los cuatro de `customer_discovery_cuatro_fases`, uno a uno |
| `OP-M-05-EDIFICIO` | 1 | paso 2 de `manifiesto_regla1_hechos_fuera_del_edificio` viaja por el paso 2 de `get_out_of_the_building` |
| `OP-M-05-APERTURA` | 0 | NINGUNO |

**EL HUECO MUERDE EN CUATRO DE LAS CINCO, NOMBRADAS: `OP-M-01-FUSION`,
`OP-M-03-III`, `OP-M-05-INDICE` y `OP-M-05-EDIFICIO`. LA QUE NO, NOMBRADA:
`OP-M-05-APERTURA`.** El acta 138 la contaba como el tercer grupo donde muerde;
mi medicion dice que no. Va como **DISCUTIBLE 1**.

### LO QUE CADA MESA OBLIGO A DECIR

- **`OP-M-01-FUSION`.** Estreno de la marca y primera fusion de la campana con
  cuatro absorbidos. **Cual redaccion viaja NO lo decide el orden sino el
  texto:** viaja `estructura_de_gates` porque es la unica de las tres que trae
  **las plantillas**, y la linea 4 de `preservar` las exige literalmente.
  Comprobado sobre el nodo escrito: los entregables aparecen **una sola vez**, y
  las verificaciones [4] (la quinta salida) y [5] (el puente al portafolio) se
  cumplen literales.
- **`OP-M-03-III`.** La marca dos veces y **en las dos direcciones**, sin cadena:
  cada una apunta a un paso que lleva APPEND. **Una desviacion declarada contra
  la atribucion de la ficha:** su linea 1 atribuye la pieza a `pivote_startup` y
  viaja la redaccion de `pivotes_e_iteraciones`, porque solo esa nombra **el
  lienzo**, que es lo que `preservar` exige.
- **`OP-M-05-INDICE`.** Las tres lineas sin id, leidas con el ojo y **con
  veredicto computado**: la enumeracion es de `customer_discovery_cuatro_fases` y
  de nadie mas; las otras dos son de los dos absorbidos. **El indice viaja
  entero**, y las cuatro fases enumeradas estan en el texto final.
- **`OP-M-05-EDIFICIO`.** El margen corto **no voltea**: de 6 contra 5 pasa a 8
  contra 6. Y **una linea de `preservar` que ninguna marca puede cumplir** (10.c
  de la correccion): sellada como **PERDIDA DE NOMBRE**, enrutada a la fase 04, y
  comprobado que vive en `merged_originals` del superviviente.
- **`OP-M-05-APERTURA`.** El unico `CUBIERTO_COND` de la fase 06, el INCISO que
  la ficha manda con sus palabras (*"VIAJA SOLO EL MATIZ"*), y **tres relecturas
  que quedan pendientes y no se deciden por adelantado** (`earlyvangelists` y los
  puestos 781 y 245, todas por el banco 9.10).

**EL CAMPO `estado` NO SE TOCA en ninguna de las seis** (acta 138, adjudicacion
3.6): se resuelve en un solo pase adjudicado cuando la fase 06 cierre.
**`OP-S-12` sigue al final de la pasada entera** y esta vuelta no lo toca.

## 5. CORRECCIONES DECLARADAS

**Ninguna tapa lo que corrige.** Las de ficha estan en
`docs/plan/CORRECCIONES_A_APLICAR.md` (9 y 10) y no tocan ningun veredicto.
**El cableado de las cinco se movio y ninguna volteo un superviviente.** Las
duplicadas cuadran al digito y con sus nombres en `OP-M-03-III`,
`OP-M-05-INDICE` y `OP-M-05-EDIFICIO`; **no cuadran** en `OP-M-01-FUSION` (4 a 5)
ni en `OP-M-05-APERTURA` (3 a 6, y solo dos nombres coinciden). **El destino no
cambia en ninguna: todas a `OP-S-12`.**

**Y DOS CORRECCIONES DE MIS PROPIAS PRUEBAS, declaradas y arregladas en el codigo
y no en la frase:**

1. La verificacion de `OP-M-01-FUSION` dio 0 buscando `vision general` contra un
   texto que la lleva con tilde. Se rehizo **sin tildes en los dos lados**.
2. **Peor, y la digo entera:** la primera version de la lectura con el ojo de
   `OP-M-05-INDICE` imprimia el veredicto como **una frase tecleada**, y llego a
   decir *"ES DE LOS DOS ABSORBIDOS"* debajo de una medicion que decia que uno de
   los dos no la tenia. **Es la especie exacta de la caida 4.2.** No se cambio la
   frase: se cambio el codigo, y ahora **el veredicto lo computa** de las cifras
   que acaba de contar. Las dos quedan escritas en la cabecera de las salidas.

**Y UN FICHERO SELLADO DE OTRA VUELTA QUE SE TOCA, declarado como la regla de la
caida 4.2 del acta 137 manda:** `scripts/loop/vuelta138_2a_caso_positivo_63_64.py`
se modifica por encargo expreso (TAREA 2.c). `scripts/loop/caso_positivo_de_fusion_de_mesa.py`
tambien, y **no por encargo sino por necesidad medida**: su guarda paraba con *"el
sujeto tiene que ser un PAR"*, que **no era una regla sino un limite del
instrumento**, y con ella `OP-M-01-FUSION` habria quedado **sin caso positivo**.
Es la misma figura que la 2.a de la vuelta 138 hallo en el generador. **Ninguna de
las nueve pruebas cambia de sentido.**

## 6. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Todo lo de esta vuelta se resolvio con regla escrita: `P.5`,
`P.8`, `P.9`, `P.13`, `P.16`, banco 9, banco 9.10, `ESPECIES_DE_PERDIDA`,
`EJECUTOR.md` reglas 1, 2, 5 y 9, y las adjudicaciones 3.1, 3.3 y 3.6 del acta
138.

**LO QUE SI DEJO ESCRITO PARA EL AUDITOR, y no es doctrina nueva sino un limite
medido:** la verificacion 2 de la ficha de `OP-M-05-EDIFICIO`, **tal como esta
escrita, no se puede cumplir** con las cinco marcas de hoy, porque pide preservar
como frase en el texto final una formulacion que vive solo en `node_id` y en
`titulo_concepto`. Se sello como `PERDIDA DE NOMBRE` y se enruto a la fase 04.

## 7. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **EL GRANDE, Y ES CONTRA EL ACTA 138: `OP-M-05-APERTURA` NO ES UN GRUPO DONDE
   EL HUECO MUERDA.** El acta lo conto como el tercero. Medido pieza por pieza:
   la pieza de la linea 3 de `preservar` tiene tres partes y **las tres estan en
   `introduccion_validacion_clientes`**, una por paso; el paso 5 de
   `filosofia_customer_validation` **no contiene esa pieza**, contiene **las tres
   preguntas de escala**, que son la linea 1, y de las tres partes de la linea 3
   solo toca una, la repetibilidad, **y la toca como pregunta de puerta y no como
   prueba que se corre**. Los dos traen matices que el otro no trae, y la regla
   del propio auditor dice que entonces **cada uno es pieza propia**. Por eso los
   dos van de APPEND y **el solape se declara y se mide: la repetibilidad aparece
   dos veces en el texto final** (paso 6 como pregunta, paso 7 como prueba).
   **Puedo estar equivocado y esta es la lectura que sostengo.**
2. **Los supervivientes crecen mucho y ninguna regla lo prohibe.**
   `OP-M-01-FUSION` deja el suyo en 17 pasos y `OP-M-05-APERTURA` en 11. Es
   `preservar` como SUELO (acta 138, 3.3), pero los deja como **candidatos
   legitimos a la poda de la fase 04**, sobre todo `OP-M-05-INDICE`, donde las
   fases 2 y 3 **repiten sustancia que el superviviente ya tiene**.
3. **La atribucion de `preservar` contra la redaccion que sobrevive.** En
   `OP-M-03-III` la ficha atribuye la pieza a `pivote_startup` y viaja la del
   otro. Sostengo que manda el texto de `preservar` (el lienzo) y no su
   atribucion, pero **la ficha y el resultado no coinciden**.
4. **`CUBIERTO:1` contra `CUBIERTO:4` en el paso 1 de
   `requisitos_gates_con_dientes`.** Elegi el 1 porque el verbo es *definir*; el 4
   es defendible porque es el que hace del gate un momento real de go/kill. **La
   pieza se dice entre los dos pasos del superviviente y la marca solo admite
   uno.**
5. **Tres matices que no viajan y se declaran:** el `(Business Model Canvas)` en
   ingles de `customer_discovery_overview` (lo trato como glosa de terminologia y
   no como gesto); el *"empleados o consultores"* del manifiesto, **mas ancho**
   que el *"personal junior"* que sobrevive; y el *"y tu propuesta de valor"* del
   paso 3 de `overview`.
6. **La guarda (v) que anadi de mi cosecha:** exijo que la linea editorial
   **nombre al absorbido destino**. El encargo pedia que dijera cual redaccion
   viaja; convertirlo en una comprobacion de que el id aparece es **mi lectura**
   de la parte comprobable por maquina.
7. **`OP-M-05-INDICE`: los cuatro pasos del indice de APPEND y ninguno
   `CUBIERTO`.** La verificacion 3 manda comprobar las cuatro fases **enteras**, y
   un indice de tres rotulos no es un indice; pero las fases 2 y 3 repiten
   sustancia. Sostengo el indice entero y **marco el precio**.

## 8. VERIFICACION DEL CIERRE

| guarda | veredicto | salida |
|---|---|---|
| `verificar_apertura_sellada.py --vuelta 139` | **VERDE EXIT 0**, los diez | `SALIDA_V139_CIERRE_APERTURA_SELLADA.txt` |
| `verificar_cierre_sellado.py --vuelta 139` | **VERDE** | `SALIDA_V139_CIERRE_SELLADO.txt` |
| `verificar_mutaciones_viejas.py` | **VERDE**, las cuatro muerden, ANCLA PERDIDA 0 | `SALIDA_V139_CIERRE_MUTACIONES_VIEJAS.txt` |
| `tallar_cabecera_reporte.py --vuelta 139 --fase04` | **VERDE EXIT 0** | `SALIDA_V139_TALLADOR_CABECERA.txt` |
| `vuelta139_tabla_fase06.py` | **VERDE**, las cinco filas salen de sus ficheros | `SALIDA_V139_4_TABLA_FASE06.txt` |
| `vuelta139_baterias_cmp.py` | corrida, por familia | `SALIDA_V139_BATERIAS_CMP.txt` |
| `verificar_cifras_del_reporte.py` **reparada** | **VERDE EXIT 0** | `SALIDA_V139_CIERRE_GUARDA_CIFRAS.txt` |

**LA LINEA `COBERTURA`, ENTERA Y CON SU REPARTO** (condicion viva del acta 137,
3.1, y ahora tambien la del acta 138, 4.5):

```
COBERTURA: 5 cotejadas / 0 exentas / 5 cifras | reparto: 0 POR ETIQUETA, 5 POR CONJUNTO, 0 sin linea CIFRA | de las cotejadas, 5 viven en una FILA DE TABLA
```

**LAS CINCO VAN POR EL CAMINO DEBIL, `POR CONJUNTO`, Y SE NOMBRAN:** son las cinco
celdas de P.5 de la primera tabla de la fase 06, y van por el debil porque el
fichero de P.5 trae una linea `CIFRA` por operacion **con la misma etiqueta en las
cinco**, asi que la guarda no puede saber cual es cual y acepta que la escrita sea
cualquiera de las candidatas. **Y LAS CINCO VIVEN EN UNA FILA DE TABLA**, que es
justo lo que la guarda no veia hasta esta vuelta.

**Y LO QUE ESTA LINEA NO DICE, para que nadie la lea como cobertura llena, que es
la leccion entera de la caida 4.5:** el vocabulario de la guarda es CERRADO
(`fichero`, `par`, `grupo`, `grafia`, `colapso`, `nodo`, `linea`, `arista`).
**Las cifras de este reporte que no llevan una de esas ocho unidades (los pasos,
las condiciones, las piezas, las fusiones, los numstat) NO las mira nadie**, y no
por ceguera sino por contrato. Las tablas que las traen salen todas de
`SALIDA_V139_4_TABLA_FASE06.txt` y de la cabecera tallada, que son las dos cosas
que SI tienen instrumento propio.

## 9. PREGUNTAS PARA EL AUDITOR

1. **¿Acepta la lectura del DISCUTIBLE 1?** Su acta midio a mano que la linea 3
   de `preservar` de `OP-M-05-APERTURA` nombra dos absorbidos y concluyo que el
   hueco muerde ahi. Mi medicion dice que comparten **un tercio de una de las tres
   partes** de esa pieza, y con figuras distintas. Si acierto, el hueco muerde en
   **cuatro** de las seis mesas y no en tres.
2. **¿Como se cierra la linea 4 de `preservar` de `OP-M-05-EDIFICIO`?** Una
   formulacion que vive en el titulo no la puede mover ninguna de las cinco
   marcas. La selle como `PERDIDA DE NOMBRE` enrutada a la fase 04. **¿Es ese el
   carril, o hace falta una marca que mueva titulos?**
3. **¿Se toca ahora el `estado` de las seis?** La fase 06 tiene su catalogo
   completo: las seis mesas fundidas. La adjudicacion 3.6 dice que el pase va
   *"cuando la fase 06 cierre"*, y hoy cierra.

---

**Rutas tocadas en la vuelta:** `dataset/nodos/` (los nodos de las cinco
fusiones y sus citantes), `dataset/metadata/master_graph.json`,
`web/lib/assets/`, `docs/PENDIENTES.md`, `docs/plan/CORRECCIONES_A_APLICAR.md`,
`docs/loop/` y `scripts/loop/`. **`docs/plan/OPERACIONES.jsonl` NO se toca.**
