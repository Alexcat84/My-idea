# REPORTE DE LA VUELTA 141

**Rama `pasada-unica`. Fase III, EJECUCION, fase 06 MESAS. Regimen completo: el
modo austero sigue suspendido por su propio punto 5.** Corte de todas las cifras
de esta pagina: **2 sep 2026** (`git log -1 --format=%ad --date=short`), salvo
donde se diga otra cosa.

**LA VUELTA ENTREGA LA 0, LA 1, LA 2 Y LA 4 ENTERAS, Y DE LA TAREA 3 LEE LOS SEIS
PARES Y EJECUTA UNO.** Lo que mas pesa: **la escalada de la TAREA 2 esta verde en
cinco de sus seis puntos y el sexto (2.e) se para con su medicion encima**, y
**la vara de enlace ya mira la vuelta**, con lo que la parada de `OP-M-01-ESLABONES`
de la vuelta 140 queda **cerrada por poda** y la de `OP-E-04` queda **medida por un
instrumento en vez de por una frase**. **LA FASE 06 SIGUE SIN CERRAR** (medido al
cierre en `SALIDA_V141_3E_ESTADO_FASE06_CIERRE.txt`: 16 de catalogo, 13 cumplidas,
sin cumplir `OP-M-01`, `OP-M-04` y `OP-E-04`).

## 0. LA CABECERA, TALLADA Y PEGADA ENTERA

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 141 --fase04` da **VERDE
EXIT 0** y su tabla se pega entera, sin tocar una celda. Salida en
`SALIDA_V141_TALLADOR_CABECERA.txt`.

<!-- CABECERA TALLADA -->

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.171 / 682 | **3.853 / 3.171 / 682** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.231 / 9.205 / 18.436 / 9.906 | **9.230 / 9.204 / 18.434 / 9.905** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **-1 / -1 / -2 / -1** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `4b0fcb20` (asunto real leido de git log: 'ACTA DE LA VUELTA 140 DEL AUDITOR: LA CIEGA SALE 16 DE 16 Y LOS OCHO DISCUTIBLES A FAVOR, PERO LA VARA DE ENLACE NUNCA MIRA LA VUELTA: OP-E-04 NO TIENE TRES FILAS EN VIOLACION, TIENE CINCO, Y DOS DE ESAS VUELTAS LAS ESCRIBIO ESTA MISMA VUELTA CON OP-E-05.'), HEAD real de apertura `4b0fcb20` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `84e4d861` (leido de `SALIDA_V141_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

**HASH FINAL de la vuelta, tallado de git y no tecleado.** `git rev-parse HEAD`
leido al escribir esta linea, en la rama `pasada-unica`:

```
5a82ce381a494508df36f933aec926d7fd2e3c85
```

<!-- COMMITS TALLADOS -->

**LOS COMMITS DE LA VUELTA**, de `git log 4b0fcb20..HEAD` (el acta de la 140
excluida), tallados con `--pretty=format:"  %h %s"` y truncados a 150 caracteres.
Son **11**, y el ultimo, el que escribe esta lista, no puede aparecer en ella.
**Y ESTA VEZ EL BLOQUE SE COTEJA**: `--comparar-commits` (TAREA 2.d) exige mismo
numero, mismos hashes y mismo orden contra `git log`, y su salida se cita abajo.

```
  5a82ce38 VUELTA 141, CIERRE: LA BATERIA DEL LADO CIERRE CON LOS DIEZ NOMBRES CANONICOS, EL ESTADO DE LA FASE 06 AL CIERRE Y LA CABECERA TALLADA. UNI
  84e4d861 VUELTA 141, TAREA 4: LA RELECTURA AL DOBLE DEL TRAMO NOMBRADO. LAS 18 DIRECCIONES DE LA FASE 06 MEDIDAS CON IDA Y VUELTA A LA VEZ, NINGUNA 
  bc17e305 VUELTA 141, TAREA 3, PARES 1 A 5: LEIDOS Y ADJUDICADOS (CUATRO ENLACES MUTUOS Y UNA ESCALERA), PERO OP-E-04 NO SE EJECUTA. PARADA, CERO ESC
  6a0170e8 VUELTA 141, TAREA 3, PAR 6 DE 6: ESCALERA. LA VUELTA asignacion_recursos_en_gates -> sistema_gates_go_kill SE RETIRA POR LA CONTRAORDEN DEL
  bf1be708 VUELTA 141, TAREA 3.a Y 3.b: LOS SEIS PARES IMPRESOS ENTEROS Y LEIDOS CON LA VARA DEL 9.22, CADA LINEA CITADA POR SU NUMERO DE PASO EN EL N
  06cc61fa VUELTA 141, TAREA 2.e: EL CASO POSITIVO SOBRE LA FASE 03 CONGELADA (62d4f28e, CUATRO BLOBS COTEJADOS POR sha256) NO CALZA CON LA EXPECTATIV
  8ca43b58 VUELTA 141, TAREAS 2.d Y 2.f: EL BLOQUE DE COMMITS SE COTEJA (--comparar-commits, 12 COMPROBACIONES VERDES Y LAS 12 CAEN AL MUTAR SU ESPERA
  1a027c4a VUELTA 141, TAREAS 2.a, 2.b Y 2.c: LA VARA DE ENLACE APRENDE A MIRAR LA VUELTA, EL CATALOGO DE UNA MESA UNE SUS DOS FUENTES Y LA CELDA PUBL
  52c29739 VUELTA 141, TAREA 1: LOS TRES REGISTROS, LOS TRES POR ADICION PURA. R.22 (178/0), LA CORRECCION 13 (TRES CONTRA CINCO FILAS DE OP-E-04, LA 
  2c1e0df7 VUELTA 141, TAREA 0.d: LA GUARDA DE LA APERTURA EN VERDE EXIT 0, CON LOS DIEZ DENTRO.
  47e2fde1 VUELTA 141, TAREA 0: EL BLOQUE DE APERTURA, SELLADO ANTES DE LA PRIMERA OPERACION, CON LOS DIEZ NOMBRES CANONICOS.
```

<!-- FIN COMMITS TALLADOS -->

## 1. TAREA 0, EL BLOQUE DE APERTURA

Sellado **antes de la primera operacion**, en `47e2fde1`, hijo directo del commit
del acta 140 (`4b0fcb20`). Los **diez** nombres canonicos con `LADO = APERTURA`, y
sus gemelos de `CIERRE` al final de la vuelta.

`python scripts/loop/verificar_apertura_sellada.py --vuelta 141` da **VERDE EXIT 0
con los DIEZ dentro** (`SALIDA_V141_TAREA0D_APERTURA_SELLADA.txt`): los diez
nacieron en `47e2fde1`, padre `4b0fcb20`.

## 2. TAREA 1, LOS TRES REGISTROS, LOS TRES POR ADICION PURA

`git diff --numstat` de la corrida, en `SALIDA_V141_1_NUMSTAT_REGISTROS.txt`:

```
178	0	docs/PENDIENTES.md
208	0	docs/plan/CORRECCIONES_A_APLICAR.md
```

**`docs/plan/OPERACIONES.jsonl` NO APARECE: cero lineas tocadas**, como el encargo
manda. **Cero borradas en los dos ficheros.**

- **(1.a) R.22 en `docs/PENDIENTES.md`**: las nueve adjudicaciones del acta 140
  (3.1 a 3.9), mis dos caidas (4.1 de guarda que no alcanza y fuera de lo marcado;
  4.2 de reporte que **NO acumula**), la de la casa (4.3, el delimitador sin
  cotejo) y **las dos del auditor** (4.4 de procedimiento y 4.5 de encargo),
  escritas igual que las mias. La racha de reporte **sigue en DOS** con la escalada
  encargada.
- **(1.b) CORRECCION 13**, por adicion: la cuenta de filas de `OP-E-04` en
  violacion de su propia verificacion 0. **TRES** (mi reporte de la 140: `LD-42`,
  `LD-48`, `LD-53`, corte 2 sep 2026) al lado de **CINCO** (auditor, re-medida por
  mi en esta vuelta: `LD-35`, `LD-42`, `LD-48`, `LD-49`, `LD-51`). **La vieja no se
  borra.** El porque esta medido: mi vara solo miro las filas que aun no estaban
  puestas. La medicion de hoy sale de
  `SALIDA_V141_1B_IDA_Y_VUELTA_OPE04.txt`.
- **(1.c) CORRECCION 14**, por adicion: el criterio del par colapsado, con sus
  **dos citas literales** dentro (la contraorden del 12 ago 2026 de
  `EXPEDIENTE_MESA_JUNTA_ASESORA.md` con su remedio operativo, y el banco 9.22 con
  el hueco de orden 1 del `00_INDICE`), y las tres cosas que el encargo pide: el
  par se relee con la vara del 9.22; dos lineas distintas dan ENLACE MUTUO y la
  misma linea da ESCALERA con la vuelta retirada; y quien corta es la operacion
  cuya verificacion lo exige, en su commit, declarandolo como giro o como poda,
  con el grado total medido antes y despues.

## 3. TAREA 2, LA ESCALADA. CINCO PUNTOS VERDES Y UNO PARADO

**Las mutaciones de 2.a, 2.b y 2.c** (`SALIDA_V141_2ABC_MUTACIONES.txt`):
**13 comprobaciones, 13 verdes, y las 13 caen al mutarles el esperado.** La prueba
de mutacion del arnes **re-evalua** cada comparacion contra el mismo valor
obtenido; no cuenta literales.

- **(2.a) LA VARA DE ENLACE MIRA LA VUELTA.** Lee la `verificacion` de la ficha y
  clasifica su regimen en `PROHIBE`, `MUTUO` o `SIN REGLA`, **sin mirar el campo
  `tipo`**, que el encargo prohibe. Las frases van **literales de las fichas** y
  citadas en el codigo. La excepcion del banco 9.22 va **escrita**. La celda
  publica, por operacion, cuantas direcciones tienen la ida y **cuantas tienen la
  vuelta**, nombrandolas. Mutaciones: **(i)** se mete la vuelta de una direccion
  limpia y `OP-M-01-SEXTO` (elegida por computo) sale nombrada y la cifra baja;
  **(ii)** se quita una vuelta existente y `OP-M-01-ESLABONES` (por computo) sube a
  cumplida. Las dos con contraprueba sin mutar.
- **(2.b) EL CATALOGO DE UNA MESA UNE SUS DOS FUENTES.** La nomina de `OP-M-01`
  pasa de **5 a 6**: `OP-M-01-SEXTO` entra **por remision**, parseada de
  `04_ENLACES.md`, y la celda publica de donde sale cada hija. Mutacion: sin la
  tabla de remision, la nomina pierde a `OP-M-01-SEXTO`.
- **(2.c) LA CELDA PUBLICA UNA SOLA UNIDAD.** Numerador y denominador son
  **direcciones**; las filas de ficha van nombradas como tales. La fila de
  `OP-E-04` ya no dice *"4 de 9 presentes"*: dice **"3 de 8 direcciones con la IDA
  presente (9 filas de ficha colapsan en 8 direcciones)"**. Mutacion sobre una
  ficha fabricada con dos filas que colapsan por alias, con contraprueba sin
  colapso.
- **(2.d) EL BLOQUE DE COMMITS SE COTEJA.** `--comparar-commits` en
  `tallar_cabecera_reporte.py`. **12 comprobaciones verdes y las 12 caen al mutar
  su esperado** (`SALIDA_V141_2D_MUTACION_COMMITS.txt`): bloque intacto VERDE,
  commit inventado ROJO nombrandolo, orden cambiado ROJO, asunto truncado VERDE y
  **declarado**, asunto que no es prefijo del real ROJO.
- **(2.f) EL SELLO DE LA MUTACION 3 ES REPRODUCIBLE.** El temporal pasa a nombre
  fijo bajo un directorio temporal (P.16). **Dos corridas seguidas dan el mismo
  sha256** (`SALIDA_V141_2F_DOS_CORRIDAS.txt`) y el `git diff --numstat` tras la
  reparacion sale **en cero** (`SALIDA_V141_2F_NUMSTAT_EN_CERO.txt`). Y la
  comprobacion entra en `verificar_mutaciones_viejas.py`: cada mutacion vieja se
  corre **dos veces** y `NO REPRODUCIBLE` es ROJO. Su prueba de mutacion
  (`--mutar-reproducibilidad`) fabrica dos scripts, uno con salida aleatoria y otro
  con salida fija, y exige que marque al primero y deje pasar al segundo.
  **La bateria completa sale VERDE** con las cinco corriendo, mordiendo y con sus
  salidas selladas identicas en dos corridas.

### 3.1. **(2.e) PARADA 1 DE 3: EL CASO POSITIVO SOBRE LA FASE 03 NO CALZA**

El sujeto esta clavado en **`62d4f28e`** (*"Decision del fundador: la fase 03
cierra con remision..."*, 26 ago 2026, asunto leido de `git log`), con sus
**cuatro blobs cotejados por sha256** en cada corrida. La expectativa del encargo
era *"su catalogo con destino cumplido salvo las SEIS remitidas a la fase 06"*.

**NO CALZA, y lo digo y paro ese caso** (`SALIDA_V141_2E_CASO_POSITIVO_FASE03.txt`):

```
LO QUE EL ENCARGO ESPERA: catalogo 16 ... cumplido 10 y sin cumplir exactamente
  ['OP-M-01-FUSION','OP-M-02-ACCLIMATE','OP-M-03-III','OP-M-05-APERTURA','OP-M-05-EDIFICIO','OP-M-05-INDICE']
LO QUE SALE:              cumplido 6 y sin cumplir 10, con CUATRO DE MAS
SIN CUMPLIR DE MAS (4): OP-M-02-ADMIT, OP-M-02-MEDIOS, OP-U-01, OP-U-02
```

**Las seis remitidas se leen del `00_INDICE` de ese mismo commit, no se teclean**, y
las seis salen exactamente. **Los cuatro de mas tienen dos causas distintas y las
dos estan medidas:**

- **`OP-U-01` y `OP-U-02`**: su `superviviente` es `null` y no tienen
  `aristas_nuevas`, asi que caen en `SIN VARA ESCRITA`. **Es la misma especie que
  la 4.5 del acta 140**: un sujeto que la vara de grafo no puede morder. No es
  defecto del instrumento.
- **`OP-M-02-ADMIT` y `OP-M-02-MEDIOS`, Y ESTA ES LA QUE TRAIGO:** su
  `superviviente` escrito en la ficha es `fase_admit` y
  `seis_medios_comunicacion_cliente`, y los dos **estan DEPRECADOS y resuelven por
  alias** a `fase_admit_celebracion` y `estrategia_multicanal_bienvenida`, tanto en
  `62d4f28e` como **hoy**. **LA VARA `FUSION` NO LE PONE EL RESOLUTOR AL
  SUPERVIVIENTE**, y `EJECUTOR.md` regla 9 dice que *todo conteo que toque ids pasa
  por el resolutor antes de contar* (P.1). **PARADA: no la arreglo yo.** Ensanchar
  la vara `FUSION` no esta en el encargo y mueve una vara de destino.
  **No mueve ninguna cifra de la fase 06**, medido: las dos son de la fase 03 y no
  estan en el catalogo de la 06.

### 3.2. CORRECCION DECLARADA DE UN INSTRUMENTO MIO, Y NO ME LA PIDIO NADIE

`vuelta140_2a_mutaciones.py` caso **(i)** se puso **ROJO** al ensanchar la vara, y
**no porque la guarda se rompiera**: su sujeto estaba **TECLEADO**
(`SUJETO_ENLACE = "OP-M-01-ESLABONES"`), y con la vara nueva esa operacion pasa a
`SIN CUMPLIR` por si sola, asi que quitarle una ida ya no puede bajar la cifra.
**Es la misma especie que la 4.5 del acta 140 y se arregla igual: el sujeto se
computa.** Ahora elige la primera operacion `ENLACE` que hoy cumple y tiene una
arista presente, y **el caso (i) vuelve a VERDE** sobre `OP-E-05`, elegida por
computo (`SALIDA_V141_2A_VUELTA140_REPARADA.txt`). El texto viejo queda en el
fichero con su motivo, sin borrarse.

## 4. TAREA 3, LOS SEIS PARES: SEIS LEIDOS, UNO EJECUTADO, CINCO PARADOS

**(3.a) Los dos nodos de cada par, enteros**, en
`SALIDA_V141_3A_LOS_SEIS_PARES.txt`. **(3.b) La vara del 9.22**, con **cada linea
citada por su numero de paso EN EL NODO DE HOY y su texto leido del grafo**, en
`SALIDA_V141_3B_VARA_922.txt`. La adjudicacion **la computa la regla**, no la
escribo yo: dos lineas distintas, una en cada nodo, es MUTUO; una sola linea, o
las dos en el mismo nodo, es ESCALERA.

| par | contra | direccion y su linea (paso EN EL NODO DE HOY) | adjudicacion |
|---|---|---|---|
| **1** | `gestion_portafolio_dos_niveles` | `dos_niveles -> sgk` por su **paso 1**; `sgk -> dos_niveles` por el **paso 10** de `sgk` | **ENLACE MUTUO** |
| **2** | `gestion_portafolio_formal` | `formal -> sgk` por su **paso 6**; `sgk -> formal` por el **paso 10** de `sgk` | **ENLACE MUTUO** |
| **3** | `portfolio_management` | `sgk -> pm` por el **paso 10** de `sgk`; `pm -> sgk` por el **paso 4** de `pm` | **ENLACE MUTUO** |
| **4** | `gestion_portafolio_foco` | `sgk -> foco` por el **paso 10** de `sgk`; `foco -> sgk` por el **paso 2** de `foco` | **ENLACE MUTUO** |
| **5** | `revision_portafolio_periodica` | `sgk -> revision` por el **paso 10** de `sgk`; la contradireccion **no expande ninguna linea** | **ESCALERA** |
| **6** | `asignacion_recursos_en_gates` | `sgk -> asignacion` por el **paso 5** de `sgk`; la contradireccion **no expande ninguna linea** | **ESCALERA** |

**LOS SEIS VAN MARCADOS DISCUTIBLES**, y lo estaban en la salida sellada
**antes** de ejecutar nada: el commit `bf1be708` los sella y el `6a0170e8` es el
que ejecuta.

### 4.1. PAR 6, EJECUTADO: LA PODA, Y LA PARADA DE LA 140 QUEDA CERRADA

La vuelta `asignacion_recursos_en_gates -> sistema_gates_go_kill` **se retira**,
que es lo que la **verificacion 0 de `OP-M-01-ESLABONES` exige** literalmente
(*"LA VUELTA NO EXISTE NI LITERAL NI RESUELTA en ninguno de los dos peldanos"*) y
lo que la contraorden del 12 ago 2026 ordena. Guardas corridas, todas con su
salida (`SALIDA_V141_3C_PAR6_SIMULACION_Y_MUTACION.txt` y
`SALIDA_V141_3C_PAR6_EJECUCION.txt`):

- **simulacion previa sobre copia en memoria** antes de tocar disco;
- **mutacion negativa con `--ejecutar`**: la direccion se elige **por computo**
  entre las que ninguna ficha nombra, y **cae en la guarda 4 con CERO
  ESCRITURAS**, comprobado con `git status` vacio;
- **los dos extremos vivos** tras resolver (P.1), **cero auto-aristas**, **cero
  duplicadas nuevas** (las preexistentes se imprimen y no bloquean: tienen dueno,
  `OP-S-12`);
- **EL GRADO TOTAL ANTES Y DESPUES**, del censo recompilado:
  **9.231 / 9.205 / 18.436 / 9.906** pasa a **9.230 / 9.204 / 18.434 / 9.905**.
  **La union baja en EXACTAMENTE UNO: es una PODA y no sube el grado**, como la
  contraorden manda;
- **ciclo de Gate 0 con las suites detras**: Gate 0 OK, motor 25/25, web 80/1.030
  passed 3 skipped, tsc EXIT 0.

**`OP-M-01-ESLABONES` pasa a destino cumplido** con la vara ensanchada, y su
parada de la vuelta 140 queda cerrada por la via que su propia ficha pedia.

**CORRECCION DECLARADA DE MI PROPIA SALIDA, y el texto viejo se queda:** la linea
*"GRADO TOTAL DESPUES"* de `SALIDA_V141_3C_PAR6_EJECUCION.txt` salio **igual** que
la de antes porque `vuelta83_conteo_aristas.py` lee `master_graph.json` y la poda
escribe en `dataset/nodos/`, y el ciclo todavia no habia recompilado. La cifra no
es falsa: **esta mal rotulada**. La buena vive en `SALIDA_V141_3_CONTEO_PAR6.txt` y
la correccion esta escrita **dentro del propio fichero**, debajo del texto viejo.

### 4.2. PARADA 2 DE 3: `OP-E-04` NO SE EJECUTA, Y AHORA SE SABE POR QUE

Los pares **1, 2, 3, 4 y 5** cubren **ocho de las nueve filas** de `OP-E-04`.
Cuatro de esos pares salen **ENLACE MUTUO**. Y ahi choca con su propia ficha:
**la verificacion 0 de `OP-E-04` dice *"UNA SOLA DIRECCION POR ENLACE... la vuelta
no debe existir ni literal ni resuelta"***, sin la excepcion del 9.22 que
`OP-E-05` si lleva escrita.

**No lo afirmo: lo mido con los instrumentos de la casa**
(`SALIDA_V141_3C_PARES_1A5_PARADA.txt`), y las dos corridas dejan el arbol limpio:

- `vuelta140_3_escribir_aristas.py --op OP-E-04` **aborta sin escribir nada**, con
  **tres ROJOS de la misma especie**: *"la direccion contraria ya existe y la ficha
  NO dice MUTUO"*, para `sgk -> revision_portafolio_periodica`,
  `portfolio_management -> sgk` y `gestion_portafolio_foco -> sgk` (esta ultima
  bloqueada por **su propia hermana de la misma corrida**);
- el retiro del par 5 (**el giro de `LD-42`**) **cae en su guarda 5**: la ida
  `sgk -> revision_portafolio_periodica` **no esta puesta**, y retirar la vuelta
  dejaria el par suelto. El giro exige escribir la ida **en el mismo commit**, y
  escribirla es justo lo que el escritor aborta.

**PARADA, CERO ESCRITURAS, Y NO LA ARREGLO YO.** El remedio es de **ficha**, no de
grafo: `OP-E-04` necesita la excepcion del banco 9.22 escrita en su verificacion,
igual que la lleva `OP-E-05` y que el **hueco de orden 1 del `00_INDICE`** exige
(*"LA GUARDA TIENE QUE LLEVAR LA EXCEPCION ESCRITA"*). Reescribir una ficha del
plan no es mio (`EJECUTOR.md` regla 5).

**Y va dicho entero, porque es lo que la 3.6 del acta 140 defiende:** aunque
pudiera escribir alguna fila suelta, **una operacion de enlace se escribe entera o
no se escribe**, y con los pares 3, 4 y 5 bloqueados `OP-E-04` no puede escribirse
entera hoy.

### 4.3. PARADA 3 DE 3: LO QUE LD-50 DICE DEL PAR 5, Y EL ENCARGO NO LO SABIA

El encargo dice que la contradireccion del par 5 *"NO tiene lectura dirigida
detras"*. **Lo verifique contra git y hay que matizarlo, medido**: antes de
`3f249a03`, esa arista era
`revision_portafolio_periodica -> gates_go_kill_decision_points`, y **`LD-50` leyo
exactamente ese par** y escribio *"Ya tienen arista entre ellos, y la arista esta
bien puesta: son dos momentos que se alimentan"*, con veredicto **D** y
**declarando que NO hay jerarquia**.

**No cambia mi adjudicacion y explico por que:** el test del 9.22 pide
**procedimiento en los dos sentidos sobre dos lineas distintas**, y `LD-50` dice
con todas sus letras que ahi **no hay jerarquia en ninguno de los dos sentidos**.
Por eso el par 5 es **ESCALERA** y no mutuo. **Pero la frase del encargo, tal como
esta, no se sostiene**, y la traigo en vez de callarla: **hay lectura dirigida
detras de esa arista, solo que sobre el nodo que murio.**

## 5. TAREA 4, LA RELECTURA AL DOBLE DEL TRAMO NOMBRADO

**El tramo: toda arista escrita o declarada cumplida sin haber medido su vuelta.**
`SALIDA_V141_4_RELECTURA_AL_DOBLE.txt`, con las 18 direcciones una por una y
**ninguna saltada por estar YA PRESENTE**:

```
direcciones releidas con IDA Y VUELTA a la vez: 18
direcciones con LA VUELTA PRESENTE: 8
de esas, en una ficha que PROHIBE la vuelta: 4
   OP-E-04 | sistema_gates_go_kill -> gestion_portafolio_dos_niveles | por LD-35, LD-51
   OP-E-04 | revision_portafolio_periodica -> sistema_gates_go_kill  | por LD-42
   OP-E-04 | sistema_gates_go_kill -> portfolio_management           | por LD-48
   OP-E-04 | sistema_gates_go_kill -> gestion_portafolio_formal      | por LD-49
```

**Las 18 direcciones cuadran al digito con la adjudicacion 3.4 del acta 140**
(*"El total de la fase es 18 direcciones (2+9+4+2+1)"*), y esa cifra la computa hoy
un instrumento, no una suma a mano.

**"YA PRESENTE" NO ES UN VEREDICTO: ES MEDIA MEDICION.** Queda como regla de
trabajo y ya vive en el codigo, no en una frase.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **Los seis pares, uno por uno** (seccion 4): cuatro MUTUOS y dos ESCALERAS. El
   mas fragil es el **par 5**, por lo que dice `LD-50` (seccion 4.3).
2. **El paso 10 de `sistema_gates_go_kill` como la linea de CUATRO direcciones
   distintas** (pares 1, 2, 3 y 4). Es el antiguo paso 5 de
   `requisitos_gates_con_dientes`, y el acta 140 (3.7) ya lo verifico. Que **una
   sola linea sea la madre de cuatro hijos** es defendible por el 9.22 (que exige
   dos lineas distintas **del mismo par**, no de todo el grafo), pero lo marco.
3. **La adjudicacion del par 6 como ESCALERA**, y con ella **la poda ejecutada**.
   Es la unica escritura de la vuelta.
4. **Parar `OP-E-04` entera en vez de escribir las filas que pasan.** Me apoyo en
   la 3.6 del acta 140. Lo contrario (escribir tres de nueve) es media ficha.
5. **No ensanchar la vara `FUSION` con el resolutor** pese a que `EJECUTOR.md`
   regla 9 lo pide, porque no esta en el encargo y mueve una vara de destino.
6. **Las frases literales como forma de leer el regimen de vuelta** (2.a) en vez de
   un campo. Es lo que el encargo pide (*"no adivinada del tipo"*), pero una ficha
   nueva que escriba la prohibicion con otras palabras saldria `SIN REGLA`.
7. **`SIN REGLA` no penaliza la vuelta** (2.a): mide, publica y no juzga. Podria
   defenderse lo contrario.
8. **La guarda 4 del instrumento de retiro exige que la ficha NOMBRE el par**, no
   solo que traiga la clausula de escalera. Es mas dura que lo encargado.

## 7. PENDIENTES DE DOCTRINA

- **`OP-E-04` necesita la excepcion del 9.22 escrita en su verificacion**, o los
  cuatro pares mutuos no se pueden ejecutar nunca. Es la parada 2.
- **La vara `FUSION` no resuelve el `superviviente` por alias** y `EJECUTOR.md`
  regla 9 dice que todo conteo que toque ids pasa por el resolutor. Es la parada 1.
- **Lo que el acta 140 dejo abierto y sigue abierto**: si un superviviente muy
  crecido deja de *expandir* una linea y pasa a *dominarla*, el 9.22 no lo mide.
  **Hoy no muerde**, y el paso 10 de `sistema_gates_go_kill` es exactamente el sitio
  donde asomaria.

## 8. PREGUNTAS

1. **¿La adjudicacion de un par como ENLACE MUTUO autoriza a ESCRIBIR la direccion
   que falta, o solo a NO RETIRAR la que hay?** La `CORRECCION 14` dice *"las dos
   direcciones viven"*. En los pares 1 y 2 no importa (las dos estan); en el 3 y el
   4 es la diferencia entre escribir y no escribir. **He leido "viven" como "no se
   retiran", y por eso no escribi.**
2. **¿`OP-M-02-ADMIT` y `OP-M-02-MEDIOS` estan ejecutadas?** Su superviviente
   deprecado resuelve a un vivo, que es la huella de una fusion hecha y luego
   reapuntada. Si lo estan, la vara `FUSION` las esta llamando incumplidas por no
   resolver, y eso es una cifra que hoy publica mal el estado de la fase 03.
3. **¿`LD-50` sigue valiendo tras la fusion?** Si vale, el par 5 no es una escalera
   limpia. Yo digo que su propia frase (*"no hay jerarquia"*) lo saca del 9.22, pero
   la decision es del auditor.

## 9. VERIFICACION DEL CIERRE

- `verificar_apertura_sellada.py --vuelta 141`: **VERDE EXIT 0**, los diez.
- `tallar_cabecera_reporte.py --vuelta 141 --fase04`: **VERDE EXIT 0**; su tabla,
  pegada entera arriba.
- `tallar_cabecera_reporte.py --vuelta 141 --fase04 --comparar docs/loop/REPORTE.md`:
  **CABECERA IDENTICA AL TALLADOR** (`SALIDA_V141_CIERRE_COMPARAR.txt`).
- `tallar_cabecera_reporte.py --vuelta 141 --comparar-commits docs/loop/REPORTE.md`:
  **BLOQUE DE COMMITS IDENTICO A GIT** (`SALIDA_V141_CIERRE_COMPARAR_COMMITS.txt`).
  Es la guarda que nace hoy, corrida sobre su primer bloque real.
- `verificar_mutaciones_viejas.py`: **VERDE**, las cinco corren, muerden y sus
  salidas selladas salen identicas en dos corridas
  (`SALIDA_V141_2F_MUTACIONES_VIEJAS.txt`).
- `verificar_cifras_del_reporte.py`: salida en `SALIDA_V141_CIERRE_CIFRAS.txt`.
