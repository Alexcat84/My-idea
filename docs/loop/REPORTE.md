# REPORTE DE LA VUELTA 77 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 76. Cubre TAREA 1 (los registros, cinco
correcciones declaradas de la parada del 26 ago 2026), TAREA 2 (la
relectura al doble del tramo 2 de `OP-E-01`) y TAREA 3 (el tramo 3 de
`OP-E-01`) del encargo de `docs/loop/PROMPT_SIGUIENTE.md`, escrito por el
fundador tras la parada de la vuelta 76
(`docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md`).

**ESTRENA EL RENGLON "LA TABLA SE CUENTA DE SU FICHERO"** (EJECUTOR.md
regla 1, quinto parrafo): toda tabla o cifra de este reporte cita el
fichero de salida del que sale y fue reconstruida contando ese fichero
antes de publicarse. Donde no hay fichero que contar, se dice.

---

## 0. LA APERTURA, medida ANTES de la primera operacion

Commit de apertura: `4f2e587a` (decision del fundador, rama `pasada-unica`,
arbol limpio, `origin/pasada-unica` igual a `HEAD` antes de empezar,
verificado con `git rev-parse HEAD` y `git rev-parse origin/pasada-unica`).

| | medido con |
|---|---|
| grafo: 3.853 nodos, 3.188 vivos, 665 deprecados | `python scripts/run_phase1.py --reaplico-curaduria`, corrida de apertura, ciclo de tres completo |
| `nodos_siguientes` en `4f2e587a` | **8.897**, contado sobre `git show 4f2e587a:dataset/metadata/master_graph.json` |
| `nodos_previos` en `4f2e587a` | **8.876** |
| suma | **17.773** |
| union dirigida unica | **9.520** |
| Gate 0 | OK (ciclo de tres: `run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`) |
| motor | `python engine/run_all_tests.py`: **25/25** |
| web | `npx vitest run` desde `web/`: **80 ficheros, 1.030 pasadas, 3 saltadas** |
| tsc | `npx tsc --noEmit` desde `web/`: **exitcode 0, cero lineas** |

**Declaro un tropiezo propio de esta vuelta, corregido antes de publicar
nada:** al correr `python scripts/run_phase1.py --reaplico-curaduria` una
SEGUNDA vez (para verificar el ciclo, sin haber corrido antes
`etiquetas_de_cara.py --aplicar`), el comando 1 por si solo dio **GATE 0:
FALLIDO, 71 nodos divergentes** entre `dataset/metadata/master_graph.json` y
`web/lib/assets/master_graph.json`. Esto NO es una caida del catalogo: es
que el paso 6 (compilacion) recalcula `etiqueta_arbol` desde las fuentes en
`dataset/nodos/`, y esa cifra vuelve a estar en su forma "sin editar" hasta
que `etiquetas_de_cara.py --aplicar` la reescribe. **El ciclo de tres es
`run_phase1.py` UNA VEZ, seguido de `etiquetas_de_cara.py --aplicar` UNA
VEZ, seguido de `sync_assets_web.py` UNA VEZ: correr `run_phase1.py` una
segunda vez DESPUES de `etiquetas_de_cara.py` deshace su correccion.**
Verificado con `git diff --stat -- dataset/metadata/master_graph.json`: tras
el tropiezo mostraba 72 lineas cambiadas contra HEAD; tras repetir
`etiquetas_de_cara.py --aplicar` volvio a diff vacio (bytes identicos salvo
el aviso de fin de linea LF/CRLF, que no es contenido). Ninguna cifra de
esta seccion se tomo de la corrida con el tropiezo.

---

## 1. TAREA 1: LOS REGISTROS Y SEIS CORRECCIONES

### 1.1. Las dos caidas de REPORTE de la vuelta 76 y la de la vuelta 75, registradas con su nombre

Las tres estan descritas y verificadas en
`docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md` (el acta de
la vuelta 76 del auditor). Se registran aqui con su nombre porque
`EJECUTOR.md` regla 1 lo exige, sin volver a remedirlas (ya vienen medidas
por el auditor en esa acta, citada como fuente):

1. **Caida de REPORTE, DENTRO del marcado (discutible 2 de la vuelta 76).**
   El reporte de la vuelta 76, seccion 4 discutible 2, afirmo que *"Ninguna
   de las dos aparece en ningun racimo de `RACIMOS_MIEMBROS.jsonl`"* sobre
   `rol_alta_direccion_calidad` y `consejo_de_calidad_y_rol_del_director`.
   Es falso para el segundo nodo: SI aparece, en el racimo "Consejo de
   calidad". Corregida en 1.2 de este reporte.
2. **Caida de REPORTE, FUERA del marcado.** El reporte de la vuelta 76
   publico que la vara 9.6.1 dio **13 CONFIRMA y 12 DEJA IGUAL** en el tramo
   1, cuando el script que la produjo no filtraba `deprecado` en ninguna
   linea (contradiciendo su propio docstring, que decia "vivos"). Corregida
   en 1.3 de este reporte.
3. **Caida de REPORTE de la vuelta 75 (acta del auditor de esa vuelta,
   citada en la parada).** El auditor escribio en su acta de la vuelta 75
   que los dos `medicion_servicios` eran "gemelos" sin haber consultado que
   el cribado ya habia leido ese par exacto (puesto 2493) y lo habia fallado
   **D**. La disposicion final (no enlazar, esperar a `OP-S-09`) se sostiene
   por otra via, asi que no movio dato, pero la palabra "gemelos" se publico
   sin consultar el veredicto de archivo.

**Con esta tercera caida registrada, la racha de reporte queda en TRES
caidas documentadas (dos de la vuelta 76, una de la vuelta 75) y vuelve a
CERO al relanzar esta vuelta**, tal como fija la decision del fundador del
26 ago 2026. Cero caidas de clase o de cifra publicada en la tanda 74-76,
sin cambio (asi lo cerro el acta del auditor).

### 1.2. Correccion declarada: el discutible 2 de la vuelta 76 sobre `RACIMOS_MIEMBROS.jsonl`

**Texto viejo (reporte de la vuelta 76, seccion 4, discutible 2), citado sin
reescribir:** *"Posible gemelo de MADRES no catalogado: `rol_alta_direccion_calidad`
(madre de dos pares escritos, `alineacion_estrategica_despliegue` y
`consejo_ejecutivo_calidad`) y `consejo_de_calidad_y_rol_del_director`
(madre del D3) tienen estructuras de pasos casi identicas del mismo libro
(Juran) [...]. Ninguna de las dos aparece en ningun racimo de
`RACIMOS_MIEMBROS.jsonl` ni lleva sufijo numerico, asi que ninguna regla
escrita obliga a pararse por esto."*

**CORRECCION DECLARADA (vuelta 77): la frase subrayada es FALSA para uno de
los dos nodos.** Verificado por corrida propia sobre
`docs/RACIMOS_MIEMBROS.jsonl`, campo `miembros[].node_id`:
`consejo_de_calidad_y_rol_del_director` SI aparece, en el racimo "Consejo de
calidad" (quality, 3 miembros, junto a `consejo_calidad_2` y
`consejo_de_calidad`), que es exactamente la fila de la seccion 1.4 del
reporte de la vuelta 76 ("Consejo de calidad | quality | 3 | 3 | DECISION
1"). `rol_alta_direccion_calidad` SI queda sin racimo (busqueda negativa
confirmada, cero coincidencias). El propio reporte de la vuelta 76 se
contradecia entre su seccion 1.4 (que media bien este nodo) y su seccion 4
(que lo afirmaba al reves).

### 1.3. Correccion declarada y tabla re-tallada: `vuelta76_relectura_9_6_1.py`

**El bug, con nombre.** La linea vieja del script
(`scripts/loop/vuelta76_relectura_9_6_1.py`) era:
```
siguientes = [s for s in (madre.get("nodos_siguientes") or [])]
```
Contaba TODOS los `nodos_siguientes` de la madre, vivos o no, mientras el
docstring y el reporte de la vuelta 76 publicaban la cifra como si fuera
solo de hijos VIVOS. **Se eligio filtrar `deprecado` de verdad** (no bajar
el docstring): se anadio la funcion `cargar_siguientes_vivos()`, que carga
cada hijo de `nodos_siguientes` y descarta los que tengan `deprecado` en
`True`. El texto viejo del docstring no se borro: la correccion esta
anadida como parrafo nuevo en el propio script.

**LA TABLA SE CUENTA DE SU FICHERO.** Re-corrido el script sobre las mismas
25 aristas del tramo 1, salida completa en
`docs/loop/SALIDA_V77_RELECTURA_9_6_1_TRAMO1_CORREGIDA.txt`, contada con
`grep -c` sobre ese mismo fichero:

| resultado | cuantos de 25 (contado del fichero) |
|---|---:|
| 9.6.1 CONFIRMA (mayoria establecida) | **12** |
| 9.6.1 DEJA IGUAL (mitad o menos, manda 9.6.2 ya leida) | **13** |
| ESCALERA ROTA (ciclo de dos) | **0** |

**Esta es la tercera cuenta que la parada del 26 ago 2026 predijo** (el
`13/12` publicado, el `14/11` del fichero sin filtrar, y este `12/13` con el
filtro real aplicado): coincide al digito con lo que el auditor midio
corriendo la misma vara con el criterio declarado. Ninguna de las 25
aristas se mueve: 9.6.1 sigue siendo un respaldo o un silencio, nunca un
veto en solitario contra 9.6.2 ya leida linea a linea (banco 9.6.1). Cero
correcciones de arista salen de esta tabla.

### 1.4. Correccion declarada: la etiqueta del instrumento de `OP-E-02`

**El bug.** `scripts/loop/vuelta75_op_e02_racimos.py` publicaba `"TOTAL
miembros vivos hoy: {total_vivos}"` sin decir que "vivos" significa "nodo
vivo TRAS RESOLVER ALIAS", no "nodo cuyo propio fichero no esta deprecado".
**Verificado por corrida propia**: de los 171 miembros censados, **133 son
vivos directos** (su propio nodo no esta deprecado) y **38 estan deprecados
en su propio fichero y solo llegan a "vivos" porque `resolver()` los
redirige a un id distinto que si esta vivo** (133 + 38 = 171).

**Correccion aplicada** (texto viejo no borrado, la etiqueta se ANADE su
definicion): la linea ahora dice `"TOTAL miembros vivos hoy (nodo vivo TRAS
RESOLVER ALIAS): {total_vivos}"`. **LA TABLA SE CUENTA DE SU FICHERO**:
re-corrido, salida en `docs/loop/SALIDA_V77_OPE02_RACIMOS.txt`:

| medido HOY, contado de `SALIDA_V77_OPE02_RACIMOS.txt` | |
|---|---:|
| racimos censados | 32 |
| miembros vivos (nodo vivo TRAS RESOLVER ALIAS) | **171 de 171** |
| muertos/fundidos desde el censo | **0** |
| racimos con miembro ajeno tras normalizar NUCLEO=core | **0** |

Sin cambio de cifra frente a la vuelta 76: la correccion es de etiqueta, no
de dato.

### 1.5. `OP-S-09`: la nomina llevada a su ficha, por instrumento, con delta declarado

**Donde vivia el agujero.** `OP-S-09` (tipo `RENOMBRE_CON_ALIAS`, fase
`05_SANEO`) tenia `nodos: []`, `eliminar: []`, `superviviente: null`: sus 53
familias y 125 nodos vivos (medidos el 11 ago 2026) vivian solo en prosa
(`docs/plan/05_SANEO.md`), asi que el filtro `P.9.1` nunca podia verla.

**El recomputo, script `scripts/loop/vuelta77_op_s09_nomina.py`.** Metodo
declarado en el propio script (docstring): universo = nodos VIVOS hoy; se
agrupan por clave normalizada (sufijo numerico retirado, particulas
retiradas, tokens restantes ordenados alfabeticamente); toda clave
compartida por 2 o mas ids vivos es una familia. Causa de la familia
(sufijo numerico / particulas / orden de palabras) asignada por el patron
de los tokens. Sinonimo puro declarado en 0 (no detectable por este metodo
lexico, igual que el recomputo de 11 ago 2026). Excepcion de
`nafta_free_trade_agreements` (ya cubierta por `OP-S-01`) excluida por
nombre.

**LA TABLA SE CUENTA DE SU FICHERO**, salida completa en
`docs/loop/SALIDA_V77_OP_S09_NOMINA.txt`:

| | medido HOY (26 ago 2026), contado del fichero | medido el 11 ago 2026 (05_SANEO.md) |
|---|---:|---:|
| familias | **29** | 53 |
| nodos vivos en familia | **69** | 125 |
| por sufijo numerico | 16 familias, 37 nodos | 35 familias |
| por particulas | 11 familias, 26 nodos | 12 familias |
| por orden de palabras | 2 familias, 6 nodos | 6 familias |
| por sinonimo puro | 0 (no detectable por este metodo) | 0 |

**DELTA DECLARADO, no forzado, con verificacion propia de la causa.** El
recomputo de hoy NO da 53/125. Para las cuatro familias mayores que
`05_SANEO.md` cita por nombre (`accion_correctiva` x5, "el consejo de
calidad" x5, "el programa Make Certain" x4, `definiciones_operacionales`
x4), verifique uno a uno el estado de sus miembros contra
`dataset/metadata/master_graph.json`:

| id | estaba en la nomina de 11 ago | estado HOY |
|---|---|---|
| `accion_correctiva_5` | si | **deprecado** |
| `accion_correctiva_6` | si | **deprecado** |
| `consejo_calidad` | si | **deprecado** |
| `consejo_calidad_2` | si | **deprecado** |
| `definiciones_operacionales_4` | si | **deprecado** |
| `make_certain_programa`, `programa_make_certain`, `_2`, `_3` | si (los 4) | **vivos los 4** (familia identica a la de 11 ago, "orden de palabras", confirma el metodo) |

**Los cinco ids que faltan de las cuatro familias mayores estan TODOS
deprecados hoy**: otras operaciones de fusion (fase 03) ya los absorbieron
por otra via desde el 11 ago 2026, quince dias de campana antes de esta
vuelta. La familia Make Certain, en cambio, sale identica a la de 11 ago
(los cuatro miembros siguen vivos), lo que confirma que el metodo
reproduce bien cuando el grafo no se movio. **El delta es real movimiento
del grafo, no un fallo del metodo**, pero se declara sin forzar la cifra:
si el recomputo no fuera a dar los 53/125 aunque el grafo no se hubiera
movido, seria una discrepancia de metodo, y no hay forma de distinguir las
dos causas sin la nomina original (que nunca se escribio).

**Donde se escribio.** Por instrucción del encargo: `OP-S-09` es
`RENOMBRE_CON_ALIAS` (sus nodos no se eliminan, se renombran conservando
alias), asi que la nomina de 69 ids va al campo **`nodos`** de
`docs/plan/OPERACIONES.jsonl` (antes vacio), NO a `eliminar`. Script
`scripts/loop/vuelta77_op_s09_escribir_nomina.py`: escribe `nodos`, y ANADE
(sin borrar el texto viejo) una correccion declarada al final de `nota` y
de `adjudicacion`, mas una entrada nueva en `evidencia`. Correccion
declarada equivalente, con el mismo delta, anadida en
`docs/plan/05_SANEO.md` bajo la seccion de `OP-S-09` (texto viejo intacto).

**El filtro `P.9.1`, ENSANCHADO.** El filtro de la vuelta 76 solo cruzaba
`eliminar` y `superviviente`: nunca podia ver a `OP-S-09` aunque su nomina
estuviera escrita, porque sus ids viven en `nodos`. Script nuevo
`scripts/loop/vuelta77_filtro_p91_ensanchado.py`: cruza tambien `nodos` de
toda operacion NO EJECUTADA de tipo `RENOMBRE_CON_ALIAS`, en las DOS
direcciones (madre o hijo del candidato). **Caso positivo, con datos
sinteticos** (no tocan el grafo real), salida en
`docs/loop/SALIDA_V77_FILTRO_P91_ENSANCHADO_CASO_POSITIVO.txt`: confirma que
el filtro aparta un candidato cuando la MADRE esta en `nodos` de una
`RENOMBRE_CON_ALIAS`, y otro cuando es el HIJO el que esta, sin romper el
caso clasico (`FUSION` con `eliminar`, que sigue apartando igual). Verificado
tambien contra el grafo real: **de los 69 ids de la nomina de `OP-S-09`, el
filtro ensanchado ve los 69** (mismo fichero de salida).

Correccion declarada equivalente en `docs/plan/04_ENLACES.md` (bajo la nota
de `P.9.1` de la vuelta 76, texto viejo intacto) y linea nueva anadida al
array `verificacion` de `OP-E-01` en `OPERACIONES.jsonl` (script
`scripts/loop/vuelta77_ensanchar_verificacion_ope01.py`, sin tocar ninguna
linea vieja del array).

### 1.6. El renglon "LA TABLA SE CUENTA DE SU FICHERO", estrenado

Cada tabla de este reporte con una cifra medida hoy trae, en su propia
seccion, el fichero de salida del que sale, y fue reconstruida contando ese
fichero (con `grep -c`, con el propio script sumando, o leyendo el bloque
`NOMINA_IDS_JSON_START`/`END`) antes de publicarse. Donde una cifra viene de
un acta o reporte anterior, se cita como tal y no como medicion de hoy
(seccion 1.1).

---

## 2. TAREA 2: LA RELECTURA AL DOBLE DEL TRAMO 2, CONTRA EL CRIBADO

**La vara que la parada del 26 ago 2026 encontro**: cruzar las 26 aristas
del tramo 2 (vuelta 76) contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
(fuente de verdad por `AUDITOR.md` seccion 0) y publicar, par a par, si el
cribado ya habia leido ese par y con que clase. Script
`scripts/loop/vuelta77_tarea2_relectura_tramo2.py` (importa `PARES_SANOS`
directo de `scripts/loop/vuelta76_op_e01_tramo2_escribir.py`, sin
retranscribir la lista a mano). **LA TABLA SE CUENTA DE SU FICHERO**, salida
completa en `docs/loop/SALIDA_V77_TAREA2_RELECTURA_TRAMO2.txt`:

| | contado del fichero |
|---|---:|
| pares del tramo 2 | 26 |
| **LEIDOS por el cribado** | **4** |
| **NUNCA LEIDOS por el cribado** | **22** |
| clase D (de los leidos) | 4 |
| clase A (de los leidos) | **0** |
| **A REVERTIR (clase A y escrito como enlace)** | **0** |

Los 4 pares que el cribado ya habia leido:

| par | puesto | clase |
|---|---:|:---:|
| `analisis_capacidad_proceso -> capacidad_de_proceso_2` | 3086 | D |
| `planificacion_de_la_inspeccion -> clasificacion_caracteristicas_calidad` | 2462 | D |
| `principio_correspondencia_contable -> contabilidad_caja_vs_devengo` | 859 | D |
| `mejora_calidad_crosby -> concepto_programa_catorce_pasos` | 2868 | D |

**Ningun par del tramo 2 fue fallado A por el cribado: cero reversiones.**
Las 26 aristas del tramo 2 se sostienen. Esta vara, corrida sobre esta
tanda, no encuentra el patron que encontro en la vuelta 76 (donde el
`13/12` sin tallar si escondia un problema): aqui las cuatro coincidencias
son todas D, coherentes con las lecturas de contenido que las escribieron.

---

## 3. TAREA 3: EL TRAMO 3 DE `OP-E-01`

### 3.1. Bolsa recalibrada FRESCA (el grafo se movio con el tramo 2)

Corrida: `python scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo
72 --umbral-contencion 0.45 --min-tokens 4` (mismos umbrales, sin tocar).
**LA TABLA SE CUENTA DE SU FICHERO**, salida en
`docs/loop/SALIDA_V77_CALIBRADO_FRESCO.txt`:

| | vuelta 76 (tras tramo 2, 337 sin arista) | **vuelta 77, esta vuelta** |
|---|---:|---:|
| candidatos brutos | 590 | **590** |
| bolsa reducida | 468 | **468** |
| **sin arista** | 337 | **311** |

**El -26 es exactamente las 26 aristas que el tramo 2 escribio**, que ya no
aparecen como "sin arista": confirma que la recalibracion capturo el
movimiento de la vuelta anterior.

### 3.2. Filtro `P.9.1` ENSANCHADO, corrido ANTES de leer nada

Script `scripts/loop/vuelta77_tramo3_filtrar.py`. **LA TABLA SE CUENTA DE SU
FICHERO**, salida en `docs/loop/SALIDA_V77_TRAMO3_FILTRO_P91.txt`:

| | contado del fichero |
|---|---:|
| candidatos sin arista | 311 |
| **apartados por P.9.1 ensanchado** | **61** |
| de esos, por `OP-S-09` (via campo `nodos`, filtro nuevo) | **46** |
| de esos, por las fusiones de fase 06 (via `eliminar`/`superviviente`, filtro viejo) | 15 |
| **limpios tras el filtro** | **250** |

**El salto de 10 apartados (vuelta 76) a 61 (esta vuelta) es el efecto
medido del ensanche del filtro**: 46 candidatos que la vuelta 76 habria
dejado pasar (porque sus ids viven en `nodos` de `OP-S-09`, no en
`eliminar`) quedan apartados desde esta vuelta. Bolsa filtrada completa en
`docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V77.jsonl` (250 filas, orden de
archivo, sin sorteo).

### 3.3. Lectura de los primeros 30, con el criterio adjudicado

**Criterio del encargo**: veredicto del cribado PRIMERO; el sufijo numerico
solo opina cuando NO hay veredicto (y ese caso ya lo cubre el filtro
`P.9.1` via `OP-S-09`, asi que en la practica no quedaba ningun candidato
"solo con sufijo" en esta cabeza). Cruzados los 30 contra
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` ANTES de leer el contenido: **4 de 30
tenian veredicto propio, los 4 clase D** (ninguno A, nada que temer por esa
via); los otros 26 sin veredicto, decididos por 9.6.2 (contenido).

**Verificacion nueva de esta vuelta, no pedida por el encargo pero hallada
al leer**: crucé los 30 pares contra `docs/RACIMOS_MIEMBROS.jsonl` para ver
si madre e hijo caian en el MISMO racimo declarado (la misma trampa que la
parada del 26 ago 2026 nombro para `OP-S-09`, pero para racimos SIN
sufijo numerico, que ningun filtro escrito cubre). Resultado: **2 de 30**.
Ninguna regla vigente dice que hacer con un candidato asi, asi que por
`EJECUTOR.md` regla 5 no pare: registro el criterio aplicado (no se enlaza
dentro de un racimo declarado sin que su propia mesa lo adjudique primero)
y sigo, marcado **PENDIENTE DE DOCTRINA**.

**LA TABLA SE CUENTA DE SU FICHERO**, salida en
`docs/loop/SALIDA_V77_TRAMO3_ESCRIBIR.txt`:

| clase | cuantos de 30 | que se hizo |
|---|---:|---|
| **JERARQUIA SANA (9.6.2)** | **28** | arista escrita en `nodos_siguientes` |
| **PENDIENTE DE DOCTRINA (mismo racimo declarado sin adjudicar)** | **2** | sin arista, razon citada |

**Los dos no escritos:**

- `human_error_como_sintoma -> preguntar_que_no_quien`: los dos son
  miembros del racimo "No culpar a la persona, arreglar el sistema"
  (health_safety, 20 miembros, DECISION 2, verificado contra
  `docs/RACIMOS_MIEMBROS.jsonl`, sin operacion ejecutada que lo toque).
  Enlazarlos como jerarquia madre-hijo adjudicaria por la puerta de enlaces
  una pregunta que pertenece a la mesa de DECISION 2 ("continua o repite,
  par a par, dentro del racimo"). No se enlaza.
- `mejora_calidad_crosby -> programa_mejora_calidad_14_pasos`: mismo racimo
  "Programa de catorce pasos de Crosby" (quality, 3 miembros, sin
  operacion) que el D2 YA ESCRITO en el tramo 2
  (`mejora_calidad_crosby -> concepto_programa_catorce_pasos`, adjudicado
  por el auditor UNA VEZ, para ESE par). Extender esa excepcion sin nueva
  adjudicacion a un segundo hijo del mismo racimo seria adjudicar por
  acumulacion. No se enlaza.

**Chequeo de escalera, exacto**, sobre las 28: ¿el hijo ya apuntaba a la
madre antes de la arista? **CERO de 28**, contado del mismo fichero
(`SALIDA_V77_TRAMO3_ESCRIBIR.txt`, seccion "ESCALERA ROTA").

**Gate 0 el ciclo entero, tras las 28 escrituras**, salidas en
`docs/loop/SALIDA_V77_GATE0_CMD1.txt` (comando 1), `SALIDA_V77_GATE0_CMD2.txt`
(comando 2) y `SALIDA_V77_GATE0_CMD3.txt` (comando 3):

| verificacion | resultado |
|---|---|
| Gate 0, comando 1 | OK, **3.853/3.188/665** (censo identico, no se crean ni deprecan nodos), **0 auto-aristas**, **0 duplicadas de titulo**, **0 nodos divergentes** |
| Gate 0, comando 2 (`etiquetas_de_cara.py --aplicar`) | 71 etiquetas reaplicadas |
| Gate 0, comando 3 (`sync_assets_web.py`) | corrido (la operacion cambio el grafo), 6 assets sincronizados |
| Gate 0, comando 4 (`plan_readiness.py`) | NO corrido: censo identico, no se dispara la regla condicional |
| motor | `python engine/run_all_tests.py`: **25/25** |
| web (`npx vitest run`, corrido desde `web/`) | **80 ficheros, 1.030 pasadas, 3 saltadas** |
| tsc (`npx tsc --noEmit`, desde `web/`) | **EXITCODE 0, cero lineas** |

### 3.4. Discutibles de la lectura, marcados AQUI (antes de saber si aciertan)

1. **`lean_launchpad_web_startup_process -> construir_mvp_baja_fidelidad`,
   ESCRITA CON EL PASO CORREGIDO.** El calibrador senalo el paso 9 de la
   madre, que habla de **ALTA** fidelidad ("Construir una version de alta
   fidelidad para probar la 'solucion'"), y el hijo es sobre **BAJA**
   fidelidad: no calzan. El paso que si calza, leido por mi, es el 5
   ("Construir un sitio web de baja fidelidad, splash page, formularios de
   pre-orden"). Se escribio la arista igual (no lleva indice de paso, solo
   madre-hijo), pero con el paso corregido en la razon. A favor: el
   contenido del hijo (crear pagina simple, accion clara, sumar
   videos/encuestas, probar variantes, publicar rapido) SI elabora el paso
   5. En contra: es la primera vez en esta campana que el paso citado por el
   calibrador no es el que realmente calza, y no hay regla escrita sobre
   cuando eso es aceptable.
2. **`cero_defectos -> zero_defects_concepto`, veredicto D del cribado
   (puesto 2464) pero titulo y tema muy cercanos.** Los dos son sobre el
   mismo estandar Cero Defectos de Crosby. A favor: el cribado ya la leyo y
   dio D; el hijo trae contenido propio (poner el compromiso por escrito con
   quien te ayuda, enfoque explicito de negocio pequeno) que la madre no
   tiene. En contra: es el mismo perfil que el discutible 2 de la vuelta 76
   (madres con estructura casi identica del mismo autor): aqui ademas madre
   e hijo comparten CASI el mismo tema, no solo estructura.
3. **`capacidad_proceso_concepto -> control_estadistico_de_procesos`,
   titulo con 97,3% de similitud (Gate 0) contra `control_estadistico_del_proceso`
   (que SI esta en la nomina de `OP-S-09` de esta vuelta; este hijo NO).**
   A favor: el contenido de este hijo es la metodologia SPC general de 10
   pasos, distinta de lo que trae `control_estadistico_del_proceso` (no leido
   en esta vuelta, pero ya enlazado en tramos anteriores). En contra: mi
   propio recomputo de `OP-S-09` declara que su metodo lexico (sufijo,
   particulas, orden de palabras) NO agrupa singular/plural
   (`procesos`/`proceso`), asi que no puedo descartar que sea un cuarto
   miembro de esa familia que el metodo simplemente no vio.
4. **`waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development`,
   posible sinonimo puro no detectado por el recomputo de `OP-S-09`.** El
   titulo del hijo ("El Modelo de Desarrollo de Clientes") se parece al de
   dos ids YA en la nomina de `OP-S-09` de esta vuelta
   (`customer_development_modelo`, `modelo_customer_development`), pero mi
   metodo lexico no los agrupo porque este tercer id usa palabras en
   espanol ("desarrollo_de_clientes") en vez de las mismas palabras en
   ingles. Es exactamente el hueco que la seccion 1.5 declara ("sinonimo
   puro: 0, no detectable por este metodo"): aqui podria haber uno de
   verdad. A favor: el contenido leido (metodologia Customer Development
   general, "get out of the building", ejemplos IMVU/Webvan) no repite lo
   que ya se sabe de los otros dos ids (no releidos en esta vuelta). En
   contra: la sospecha de familia queda sin resolver.
5. **Los dos pares del mismo racimo, no escritos (3.3), son la primera vez
   en la campana que se aplica el criterio "no enlazar dentro de un racimo
   declarado sin adjudicar".** Es `PENDIENTE DE DOCTRINA`, no una regla
   escrita: si el auditor o el fundador deciden que un racimo SIN sufijo
   numerico y SIN operacion NO bloquea el enlace (el mismo argumento que
   dejo pasar al D2 en el tramo 2), estos dos pares se leerian otra vez con
   ese criterio.
6. **La medicion de 9.6.1 sigue usando el proxy declarado en la vuelta 76**
   (`L` = `nodos_siguientes` vivos de la madre HOY, no "hijos con nodo propio
   en el grafo, esten o no ya ligados"), ahora con el filtro de `deprecado`
   corregido (1.3). El proxy en si mismo no se corrigio de fondo, solo el
   bug de conteo.

---

## 4. EL CIERRE, medido AL CIERRE

Commit final de esta vuelta: `122bcc77` (contiene todo lo de TAREA 1, 2 y 3;
el segundo commit de esta vuelta solo anade este hash al propio reporte, sin
tocar dato ni cifra). Push a `origin/pasada-unica`.

| | medido con |
|---|---|
| grafo: 3.853 nodos, 3.188 vivos, 665 deprecados (sin cambio: la fase 04 no muda ids) | `python scripts/run_phase1.py --reaplico-curaduria`, corrida de cierre |
| `nodos_siguientes` | **8.925** (apertura 8.897 mas 28 del tramo 3) |
| `nodos_previos` | **8.904** (apertura 8.876 mas 28) |
| suma | **17.829** |
| union dirigida unica | **9.548** |
| Gate 0 | OK, ciclo de tres, auto-aristas 0, duplicadas 0, divergentes 0 |
| motor | 25/25 |
| web (corrido desde `web/`) | 80 ficheros, 1.030 pasadas, 3 saltadas |
| tsc (corrido desde `web/`) | EXITCODE 0, cero lineas |
| aristas revertidas esta vuelta | 0 (TAREA 2 no encontro ninguna A del cribado escrita) |
| aristas nuevas escritas esta vuelta (tramo 3) | 28 |
| pares leidos y no enlazados esta vuelta (tramo 3, PENDIENTE DE DOCTRINA) | 2 |
| operaciones cerradas esta vuelta | 0 |
| correcciones declaradas esta vuelta | 6 (1.2, 1.3, 1.4, 1.5 x2 (nomina + filtro), y la de `OP-E-01.verificacion`) |
| bolsa de `OP-E-01` restante sin leer (filtrada por `P.9.1` ensanchado, esta vuelta) | **220 de 250** (250 menos los 30 leidos: 28 escritas mas 2 PENDIENTE DE DOCTRINA) |

---

## 5. LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Los seis discutibles de la seccion 3.4 (arriba), mas los cinco heredados de
la vuelta 76 (`docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md`
y el reporte anterior, no repetidos aqui porque ya fueron auditados y
adjudicados: PENDIENTE 1 y 2 cerrados, D2 decidido, y el resto queda como
observacion sin parada). Los seis nuevos son los unicos que esta vuelta trae
para relectura ciega.

---

## 6. PENDIENTES DE DOCTRINA

**Uno nuevo, con dos ejemplares esta vuelta (3.3, discutible 5).** Ninguna
regla escrita dice que hacer con un candidato de enlace cuyos dos nodos
(madre e hijo) son miembros del MISMO racimo declarado en
`docs/RACIMOS_MIEMBROS.jsonl`, cuando ese racimo NO tiene sufijo numerico
(asi que `P.9.1` no lo aparta) y NO tiene operacion que lo nombre. Aplique
el criterio mas conservador (no enlazar sin que la mesa del racimo
adjudique primero) y lo registro en vez de pararme, por `EJECUTOR.md` regla
5. Los dos ejemplares (3.3) esperan esa doctrina o una adjudicacion del
auditor.

---

## 7. LO QUE QUEDA PENDIENTE PARA LA VUELTA SIGUIENTE

- Continuar `OP-E-01` con un TRAMO 4, recalibrando la bolsa antes de leer
  (regla EL INSTRUMENTO MANDA: no reusar
  `PASO_NODO_CALIBRADO_FILTRADO_V77.jsonl`, el grafo ya se habra movido
  otra vez con las 28 aristas de este tramo).
- Los dos pares `PENDIENTE DE DOCTRINA` de 3.3 esperan adjudicacion.
- Los seis discutibles de 3.4 esperan la relectura ciega del auditor.
- `OP-E-02` sigue CERRADO (vuelta 76), sin cambio.
- `OP-E-03` sigue esperando a que `OP-E-01` termine entero.
- `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y
  `OP-M-01-SEXTO` siguen esperando a la fase 06 (remision escrita, no se
  tocan).
- `OP-E-06` y `OP-E-07` siguen libres de bloqueo de dependencia pero esperan
  su turno en el orden escrito.
- La escalada automatica del tallador a las fases mecanicas (opcion b de la
  decision del fundador) SOLO se dispara si la racha de reporte vuelve a
  DOS: esta vuelta la deja en CERO.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada (esta
vuelta: hecho al cierre de este mismo reporte). Cero guiones largos y cero
guiones medios. El hook corrio en el commit sin saltarse. No se adivino
nada que no se pudiera medir.
