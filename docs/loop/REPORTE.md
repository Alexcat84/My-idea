# REPORTE DE LA VUELTA 78 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 77. Cubre TAREA 1 (los registros y cinco
correcciones declaradas), TAREA 2 (la relectura al doble del tramo 3 por el
credito rebajado), TAREA 3 (la relectura conjunta de las once aristas que la
vara de los veredictos A toca, con el ensanche del filtro `P.9.1`) y TAREA 4
(el tramo 4 de `OP-E-01`) del encargo de `docs/loop/PROMPT_SIGUIENTE.md`,
escrito tras el acta de la vuelta 77 (`docs/loop/ACTA_AUDITOR.md`, linea
22077).

**SE MANTIENE "LA TABLA SE CUENTA DE SU FICHERO"**: toda tabla o cifra de
este reporte cita el fichero de salida del que sale y fue reconstruida
contando ese fichero antes de publicarse.

---

## 0. LA APERTURA, medida ANTES de la primera operacion

Commit de apertura: `57863182` (acta de la vuelta 77, rama `pasada-unica`,
arbol limpio, `origin/pasada-unica` igual a `HEAD` antes de empezar,
verificado con `git rev-parse HEAD` y `git rev-parse origin/pasada-unica`).

| | medido con |
|---|---|
| grafo: 3.853 nodos, 3.188 vivos, 665 deprecados | `python scripts/run_phase1.py --reaplico-curaduria`, corrida de apertura, ciclo de tres completo (`SALIDA_V78_GATE0_CMD1_APERTURA.txt`, `_CMD2_`, `_CMD3_`) |
| `nodos_siguientes` en `57863182` | **8.925**, contado con `python docs/loop/_auditor_v77_conteo.py 57863182` (`SALIDA_V78_CONTEO_APERTURA.txt`) |
| `nodos_previos` en `57863182` | **8.904** |
| suma | **17.829** |
| union dirigida unica | **9.548** |
| Gate 0 | OK (ciclo de tres, auto-aristas 0, duplicadas 0, divergentes 0) |
| motor | `python engine/run_all_tests.py`: **25/25** (`SALIDA_V78_MOTOR_APERTURA.txt`) |
| web | `npx vitest run` desde `web/`: **80 ficheros, 1.030 pasadas, 3 saltadas** (`SALIDA_V78_WEB_APERTURA.txt`) |
| tsc | `npx tsc --noEmit` desde `web/`: **exitcode 0, cero lineas** (`SALIDA_V78_TSC_APERTURA.txt`) |

**Declaro un tropiezo propio de esta vuelta, corregido antes de tocar el
grafo real:** al medir la apertura corri `python scripts/run_phase1.py
--reaplico-curaduria` una SEGUNDA vez sin haber corrido antes
`etiquetas_de_cara.py --aplicar`, y reproduje al digito el mismo tropiezo
que el reporte de la vuelta 77 declaro (**71 nodos divergentes**,
`GATE 0: FALLIDO`). Restaure el arbol con `git checkout --
dataset/metadata/master_graph.json dataset/metadata/phase1_run_log.json`
antes de medir nada, y repeti el ciclo de tres EN ORDEN (`run_phase1.py`
UNA vez, `etiquetas_de_cara.py --aplicar` UNA vez, `sync_assets_web.py` UNA
vez). Ninguna cifra de esta seccion sale de la corrida con el tropiezo.

---

## 1. TAREA 1: LOS REGISTROS Y CINCO CORRECCIONES

### 1.1. La caida de clase (dentro del marcado) y las dos caidas de reporte (fuera), registradas con su nombre

Las tres estan medidas y descritas en `docs/loop/ACTA_AUDITOR.md`
(vuelta 77, desde la linea 22077, secciones 3 y 4). Se registran aqui con
su nombre porque `EJECUTOR.md` regla 1 lo exige, **sin volver a
remedirlas** (ya vienen medidas por el auditor, citado como fuente):

1. **Caida de CLASE, DENTRO del marcado (acta 77, seccion 3, D5 segundo
   par).** El reporte de la vuelta 77, seccion 3.3, dejo sin escribir la
   arista `mejora_calidad_crosby -> programa_mejora_calidad_14_pasos` por
   una razon publicada: "los dos son miembros del mismo racimo declarado".
   El auditor midio que esa razon es **FALSA** contra
   `docs/RACIMOS_MIEMBROS.jsonl` (`mejora_calidad_crosby` no esta en
   ninguno de los 32 racimos) y que el par **SI tiene veredicto propio**,
   puesto_intra **2583**, clase **D**, cuyo texto dice que
   `mejora_calidad_crosby` "literalmente REMITE al de catorce pasos como
   su contenido". Corregida en 1.2 de este reporte.
2. **Caida de REPORTE, FUERA del marcado (acta 77, seccion 4.1).** El
   reporte de la vuelta 77, seccion 3.3, publico *"4 de 30 tenian
   veredicto propio"* sin fichero de salida detras. El auditor conto **7**
   sin direccion (como lee el cribado) y **6** en direccion madre a hijo.
   Corregida en 1.3 de este reporte.
3. **Caida de REPORTE, FUERA del marcado (acta 77, seccion 4.2).** El
   reporte de la vuelta 77, seccion 3.2, publico que 15 candidatos se
   apartaban *"por las fusiones de fase 06"*. Las siete operaciones que
   apartan (`OP-M-01-FUSION`, `OP-M-02-PROG`, `OP-M-03-II`,
   `OP-M-03-III`, `OP-M-05-APERTURA`, `OP-M-05-EDIFICIO`,
   `OP-M-05-INDICE`) llevan **todas** `fase` = `03_FUSIONES` en su ficha
   (`docs/plan/OPERACIONES.jsonl`), y dos de ellas (`OP-M-02-PROG`,
   `OP-M-03-II`) ni siquiera estan entre las seis remitidas a la fase 06
   por `03_FUSIONES.md` linea 9246. El conteo de 15 SI es correcto; la
   etiqueta no. Corregida en 1.4 de este reporte.

**Con esta caida de clase registrada, la racha de clase o cifra publicada
queda en UNA** (tal como el acta 77 la deja) **y la racha de reporte queda
en UNA tanda**: ninguna de las dos dispara parada (piden dos y tres
seguidas respectivamente), pero el credito de la tanda queda REBAJADO
porque las dos caidas de reporte cayeron fuera del marcado, por lo que
`AUDITOR.md` seccion 1.2 obliga a releer el tramo 3 al doble (TAREA 2 de
este reporte).

### 1.2. Correccion declarada y arista escrita: `mejora_calidad_crosby -> programa_mejora_calidad_14_pasos`

**Verificado por corrida propia en esta vuelta, ANTES de escribir**
(script `scripts/loop/vuelta78_tarea12_arista_2583.py`, salida
`docs/loop/SALIDA_V78_TAREA12_ARISTA_2583.txt`):

- `mejora_calidad_crosby` en los 32 racimos de `docs/RACIMOS_MIEMBROS.jsonl`:
  **[] (cero coincidencias, busqueda negativa confirmada)**.
- Veredicto puesto_intra **2583**, dominio quality, clase **D**,
  `nodo_a=mejora_calidad_crosby`, `nodo_b=programa_mejora_calidad_14_pasos`.
- Los dos nodos vivos hoy, la arista no existia, cero escalera rota (el
  hijo no apuntaba a la madre).

**Texto viejo (reporte de la vuelta 77, seccion 3.3), citado sin
reescribir:** *"mejora_calidad_crosby -> programa_mejora_calidad_14_pasos:
mismo racimo 'Programa de catorce pasos de Crosby' [...] Extender esa
excepcion sin nueva adjudicacion a un segundo hijo del mismo racimo seria
adjudicar por acumulacion. No se enlaza."*

**CORRECCION DECLARADA (vuelta 78): la premisa era falsa** (la madre no
esta en ese racimo, solo el hijo) **y el par tenia veredicto D propio que
el cruce de la vuelta 77 no encontro.** Arista escrita en
`dataset/nodos/mejora_calidad_crosby.json`.

### 1.3. Correccion declarada y tabla re-tallada: "4 de 30"

**LA TABLA SE CUENTA DE SU FICHERO.** Script
`scripts/loop/vuelta78_tarea13_treinta.py`, que importa `PARES_SANOS` y
`PARES_DESCARTADOS` directo de `scripts/loop/vuelta77_tramo3_escribir.py`
(sin retranscribir la lista de 30 a mano). Salida completa en
`docs/loop/SALIDA_V78_TAREA13_TREINTA.txt`:

| forma de emparejar | cuantos de 30 (contado del fichero) |
|---|---:|
| **sin direccion (como lee el cribado)** | **7** |
| solo direccion madre a hijo | **6** |
| clase A entre los siete | **0** |

Los siete: puestos_intra **1369, 2464, 1951, 2826, 223, 1746 y 2583**,
**los siete clase D**: ninguna arista revertida por esta via. **Coincide
al digito con la medicion del auditor** (acta 77, seccion 4.1).

**Texto viejo (reporte de la vuelta 77, seccion 3.3), citado sin
reescribir:** *"Cruzados los 30 [...] 4 de 30 tenian veredicto propio, los
4 clase D"*. **CORRECCION DECLARADA: son 7 sin direccion, 6 en direccion
madre-hijo, no 4.**

### 1.4. Correccion declarada: la etiqueta de "fusiones de fase 06"

**LA TABLA SE CUENTA DE SU FICHERO.** Verificado sobre
`docs/plan/OPERACIONES.jsonl` (`SALIDA_V78_TAREA14_FASE_OPS.txt`):

| operacion | `fase` en su ficha |
|---|---|
| `OP-M-01-FUSION` | `03_FUSIONES` |
| `OP-M-02-PROG` | `03_FUSIONES` |
| `OP-M-03-II` | `03_FUSIONES` |
| `OP-M-03-III` | `03_FUSIONES` |
| `OP-M-05-APERTURA` | `03_FUSIONES` |
| `OP-M-05-EDIFICIO` | `03_FUSIONES` |
| `OP-M-05-INDICE` | `03_FUSIONES` |

**Las siete llevan `fase` = `03_FUSIONES`.** Verificado tambien contra
`docs/plan/03_FUSIONES.md` linea 9246 ("SEIS FUSIONES ENRUTADAS a la fase
06": `OP-M-01-FUSION`, `OP-M-02-ACCLIMATE`, `OP-M-03-III`,
`OP-M-05-INDICE`, `OP-M-05-EDIFICIO`, `OP-M-05-APERTURA`): **`OP-M-02-PROG`
y `OP-M-03-II` no estan en esa lista de seis.**

**Texto viejo (reporte de la vuelta 77, seccion 3.2), citado sin
reescribir:** *"de esos, por las fusiones de fase 06 (via
eliminar/superviviente, filtro viejo) | 15"*. **CORRECCION DECLARADA: el
conteo de 15 es correcto; la etiqueta "fusiones de fase 06" no lo es para
las siete operaciones, que llevan fase 03_FUSIONES en su ficha, y dos de
ellas ni siquiera estan entre las seis remitidas a la fase 06.**

### 1.5. Tercer caso de EL TOQUE UNICO (banco 9.4): 2 ids de gates remitidos a `OP-M-01-FUSION`

**Medido por el auditor** (acta 77, seccion 5 punto 9) **y verificado de
nuevo por corrida propia** (script
`scripts/loop/vuelta78_tarea15_toque_unico.py`, salida
`docs/loop/SALIDA_V78_TAREA15_TOQUE_UNICO.txt`):

| | |
|---|---|
| overlap `OP-M-01-FUSION.eliminar` x `OP-S-09.nodos` | `estructura_de_gates`, `estructura_gates` |
| `OP-M-01-FUSION` | fase `03_FUSIONES`, orden **5** |
| `OP-S-09` | fase `05_SANEO`, orden **8** (corre despues) |

`OP-M-01-FUSION` corre antes: el mismo caso que `05_SANEO.md` ya aplica a
`OP-S-01` y `OP-S-04` (banco 9.4, EL TOQUE UNICO). **Declarado como tercer
caso** en `docs/plan/05_SANEO.md` (tabla de EL TOQUE UNICO y nota bajo la
seccion de `OP-S-09`, texto viejo intacto). Los dos ids forman por si
solos la familia `[PARTICULAS]` de la nomina de la vuelta 77: al
remitirlos, la familia desaparece entera.

**RE-MEDIDO, LA TABLA SE CUENTA DE SU FICHERO:**

| | vuelta 77 | vuelta 78, tras el toque unico |
|---|---:|---:|
| ids en `OP-S-09.nodos` | 69 | **67** |
| familias | 29 | **28** (la familia `[PARTICULAS]` desaparece entera) |

Escrito en `docs/plan/OPERACIONES.jsonl` (script
`scripts/loop/vuelta78_tarea15_escribir_toque_unico.py`, correccion
declarada anadida a `nota`, `adjudicacion` y `evidencia`, texto viejo
intacto).

---

## 2. TAREA 2: LA RELECTURA AL DOBLE DEL TRAMO 3 (credito rebajado)

**La vara**: cruzar las 28 aristas del tramo 3 (vuelta 77) contra
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y publicar, par a par, si el cribado
ya habia leido ese par y con que clase. Script
`scripts/loop/vuelta78_tarea2_relectura_doble_tramo3.py` (importa
`PARES_SANOS` directo de `scripts/loop/vuelta77_tramo3_escribir.py`, sin
retranscribir la lista). **LA TABLA SE CUENTA DE SU FICHERO**, salida
completa en `docs/loop/SALIDA_V78_TAREA2_RELECTURA_DOBLE_TRAMO3.txt`:

| | contado del fichero |
|---|---:|
| pares del tramo 3 | 28 |
| **LEIDOS por el cribado** | **6** |
| **NUNCA LEIDOS por el cribado** | **22** |
| clase D (de los leidos) | 6 |
| clase A (de los leidos) | **0** |
| **A REVERTIR (clase A y escrito como enlace)** | **0** |

Los 6 pares leidos: puestos_intra 2826, 2464, 223, 1369, 1746, 1951,
**todos clase D**. **Coincide al digito con la medicion del auditor** (acta
77, seccion 2: "TRAMO 3 (28 aristas de esta vuelta): 6 leidos por el
cribado, clase A 0"). **Cero reversiones: las 28 aristas del tramo 3 se
sostienen.**

---

## 3. TAREA 3: LA RELECTURA CONJUNTA DE LAS ONCE ARISTAS QUE LA VARA DE LOS VEREDICTOS A TOCA

### 3.1. El filtro `P.9.1` ensanchado con la vara de los veredictos A

**Adjudicado por el auditor por cita, sin doctrina nueva** (acta 77,
seccion 3 D4 y seccion 5 punto 5): `P.9` punto 1 (los enlaces corren
DESPUES de las fusiones que tocan sus destinos), `P.9` punto 2 (el id
escrito es el que estara vivo) y `AUDITOR.md` seccion 0 punto 3
(`INTRA_DOMINIO_VEREDICTOS.jsonl` es fuente de verdad). Un veredicto A es
una fusion que el plan aun no ha citado con una operacion.

Script `scripts/loop/vuelta78_filtro_p91_vara_a.py`: aparta el candidato
cuyo extremo (madre o hijo) participe en un veredicto clase A donde los
DOS nodos del par esten vivos hoy, ademas de lo que ya apartaba el filtro
de la vuelta 77 (`eliminar`, `superviviente`, `nodos` de
`RENOMBRE_CON_ALIAS`). **Caso positivo con datos SINTETICOS** (no tocan el
grafo real), salida en
`docs/loop/SALIDA_V78_FILTRO_P91_VARA_A_CASO_POSITIVO.txt`: confirma que
la vara aparta por madre y por hijo, en las dos direcciones, que un A con
un extremo ya deprecado NO aparta nada (ya resuelto por otra via), y que
el caso clasico de `FUSION` sigue apartando igual (no rompe lo viejo).

**Verificado contra el grafo real, mismo fichero de salida:**

| | |
|---|---:|
| veredictos clase A en el archivo | **551** |
| nodos VIVOS que participan en al menos un A con otro nodo VIVO | **187** |

**Coincide al digito con la medicion del auditor** (acta 77, seccion 3,
`_auditor_v77_guardaA.txt`). Correccion declarada equivalente en
`docs/plan/04_ENLACES.md` (bajo las notas de `P.9.1` de las vueltas 76 y
77, texto viejo intacto) y linea nueva anadida al array `verificacion` de
`OP-E-01` en `OPERACIONES.jsonl` (script
`scripts/loop/vuelta78_ensanchar_verificacion_ope01.py`, sin tocar ninguna
linea vieja).

### 3.2. Las once aristas, verificadas una a una y decididas par a par

Dossier completo (veredicto propio, cobertura por operacion, estado
vivo/deprecado de cada extremo y companero) en
`docs/loop/SALIDA_V78_TAREA3_DOSSIER_ONCE.txt`. **Criterio aplicado, uno
solo para las once, citado por `P.9` puntos 1 y 2, sin doctrina nueva**: si
el extremo ESCRITO en la arista (no su companero de A) esta condenado por
una operacion sin ser su superviviente, la arista SE MUEVE; si el extremo
escrito ES el superviviente declarado, o si ninguna operacion condena al
extremo escrito, la arista SE QUEDA con la razon puesta.

**LA TABLA SE CUENTA DE SU FICHERO**, decision completa en
`docs/loop/SALIDA_V78_TAREA32_DECISION_ONCE.txt`:

| # | arista | decision | razon corta |
|---:|---|:---:|---|
| 1 | `concepto_proyecto_breakthrough -> pocos_vitales_muchos_utiles` | **QUEDA** | ni madre ni hijo condenados; el propio cribado dice "el acto es POR ELEGIR" |
| 2 | `customer_validation -> mvp_alta_fidelidad` | **QUEDA** | la madre ES el `superviviente` declarado de `OP-M-05-APERTURA` (P.9 punto 2) |
| 3 | `customer_validation -> prueba_mvp_alta_fidelidad` | **QUEDA** | mismo caso: madre superviviente de `OP-M-05-APERTURA` |
| 4 | `earlyvangelists_ventas_tempranas -> value_proposition_startup` | **QUEDA** | ni madre ni hijo condenados; el companero condenado no es parte de esta arista |
| 5 | `ecuacion_de_valor_cliente -> preguntas_need_payoff` | **QUEDA** | los tres companeros de A sin operacion |
| 6 | `estrategia_de_innovacion_arenas -> product_roadmap_estrategico` | **QUEDA** | la madre no esta condenada; el cribado remite esta familia de 6 "a mesa", no a `OP-S-09` |
| 7 | `franquicia_unidad_individual -> programa_de_referidos_de_franquiciados` | **QUEDA** | ni madre ni hijo condenados |
| 8 | `funnel_get_customers_optimizacion -> disenar_tests_pass_fail` | **QUEDA** | ni madre ni hijo condenados |
| 9 | `screening_mercados_potenciales -> uso_del_us_commercial_service` | **QUEDA** | ni madre ni hijo condenados; un companero ya deprecado (A ya resuelta) |
| 10 | `testing_process_completo -> value_proposition_canvas` | **QUEDA** | ni madre ni hijo condenados; un companero ya deprecado |
| 11 | `waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development` | **SE MUEVE (revertida)** | el hijo tiene A vivo (puesto 1052) con `customer_development_modelo`, YA en la nomina de `OP-S-09`; el hijo mismo no esta en esa nomina (sinonimo puro no detectado) |

**RESULTADO: 10 se quedan, 1 se revierte.**

**TROPIEZO PROPIO, cazado y corregido antes de publicar cifra.** El primer
intento de revertir la arista 11 solo quito
`desarrollo_de_clientes_customer_development` de
`nodos_siguientes` de la madre. Tras correr el ciclo de Gate 0, la arista
**reaparecio sola**: `scripts/run_phase1.py` paso 5 (simetrizacion)
reciproca cualquier arista declarada por CUALQUIERA de los dos extremos, y
el hijo seguia declarandola en su propio `nodos_previos`. Corregido
quitando las DOS vistas a la vez (script
`scripts/loop/vuelta78_tarea32_decision_once.py`, version final); verificado
tras el ciclo de Gate 0 que la arista no vuelve (`SALIDA_V78_GATE0_CMD1_TRAS32.txt`
a `_CMD3_`).

### 3.3. Cuantas de la fase 04 quedan tocadas por la vara, tras la decision

**LA TABLA SE CUENTA DE SU FICHERO**, script
`scripts/loop/vuelta78_tarea33_fase04_tras_decision.py`, salida en
`docs/loop/SALIDA_V78_TAREA33_FASE04_TRAS_DECISION.txt`:

| | |
|---|---:|
| aristas de la fase 04 (HOY menos `62d4f28e`) | **79** |
| de esas, tocadas por la vara de los A (tras la decision de 3.2) | **10** |

Las diez son las que la tabla de 3.2 marca "QUEDA": se quedan tocadas
porque ninguna operacion condena a su extremo escrito, no porque el
hallazgo se ignore; quedan como observacion para cuando la operacion que
las cubra se escriba.

---

## 4. TAREA 4: EL TRAMO 4 DE `OP-E-01`

Corrido porque las TAREA 1, 2 y 3 cerraron en verde (Gate 0 OK, motor
25/25, web 1030/3, tsc limpio en cada tramo intermedio).

### 4.1. Bolsa recalibrada FRESCA (el grafo se movio con 1.2 y 3.2)

Corrida: `python scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo
72 --umbral-contencion 0.45 --min-tokens 4` (mismos umbrales, sin tocar,
corrida DESPUES de escribir la arista de 1.2 y de revertir la de 3.2).
**LA TABLA SE CUENTA DE SU FICHERO**, salida en
`docs/loop/SALIDA_V78_CALIBRADO_FRESCO.txt`:

| | vuelta 77, DESPUES del tramo 3 (283 sin arista, medido por el auditor en su acta seccion 1.5, "283 = 311 menos las 28 escritas") | **vuelta 78, esta vuelta** |
|---|---:|---:|
| candidatos brutos | 590 | **590** |
| bolsa reducida | 468 | **468** |
| **sin arista** | 283 | **283** |

**SIN CAMBIO, y verificado por que**: el par de TAREA 1.2
(`mejora_calidad_crosby -> programa_mejora_calidad_14_pasos`) SI estaba en
la bolsa del calibrador y al escribirlo salio de "sin arista" (-1); el par
de TAREA 3.2 (`waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development`)
tambien esta en la bolsa y al revertirlo volvio a "sin arista" (+1).
**Los dos movimientos se cancelan**, verificado contra
`docs/plan/PASO_NODO_CALIBRADO.jsonl` (campo `arista`: `True` para el
primer par, `False` para el segundo, tras la recalibracion de esta
vuelta): 283 sigue siendo 283. **CORRECCION DECLARADA sobre mi propio
primer borrador de esta seccion**: escribi una comparacion contra 311 (que
es la cifra ANTES del tramo 3, no despues) y una explicacion de "-28" que
no correspondia a esta vuelta; la cace releyendo el propio texto de la
acta 77 seccion 1.5 antes de publicar, y la corrijo aqui sin dejar la
cifra vieja circulando.

### 4.2. Filtro `P.9.1` ensanchado con la vara de los A, corrido ANTES de leer nada

Script `scripts/loop/vuelta78_tramo4_filtrar.py`. **LA TABLA SE CUENTA DE
SU FICHERO**, salida en `docs/loop/SALIDA_V78_TRAMO4_FILTRO_P91.txt`:

| | contado del fichero |
|---|---:|
| candidatos sin arista | 283 |
| **apartados por P.9.1 ensanchado (operaciones + vara de los A)** | **92** |
| de esos, SOLO por operacion (`eliminar`/`superviviente`/`nodos`) | 35 |
| de esos, con al menos un motivo de la vara de los A | 57 |
| **limpios tras el filtro** | **191** |

Bolsa filtrada completa en `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl`
(191 filas, orden de archivo, sin sorteo).

### 4.3. Lectura de los primeros 30, con el criterio adjudicado

**Criterio, sin cambio sobre tramos anteriores**: veredicto del cribado
PRIMERO; el sufijo numerico y el racimo solo opinan cuando NO hay
veredicto (y ya lo cubre el filtro); cuando el paso que el calibrador
senala no es el que calza, manda la lectura (adjudicado en el acta 77,
D1). Dossier completo (resumen, pasos, veredicto y racimo de cada uno de
los 30) en `docs/loop/SALIDA_V78_TRAMO4_DOSSIER30.txt`.

**DOS de los 30 tenian veredicto propio**: puesto_intra **3205**, clase
**D** (`sujetos_de_control -> key_process_product_characteristics`:
"ficha nombrada dentro del paso de otro nodo, figura reconocida") y
puesto_intra **637**, clase **B**
(`equipo_customer_development -> customer_development_team`: el archivo
dice, con estas palabras, *"Sin arista entre ellos"*). Los otros 28 sin
veredicto, decididos por 9.6.2 (contenido).

**LA TABLA SE CUENTA DE SU FICHERO**, salida en
`docs/loop/SALIDA_V78_TRAMO4_ESCRIBIR.txt`:

| clase | cuantos de 30 | que se hizo |
|---|---:|---|
| **JERARQUIA SANA (9.6.2)** | **24** | arista escrita en `nodos_siguientes` Y `nodos_previos` (las dos vistas a la vez, leccion de 3.2) |
| **NO ESCRITOS, con razon** | **6** | sin arista, razon citada abajo |

**Chequeo de escalera, exacto**, sobre las 24: cero de 24 (contado del
mismo fichero, seccion "ESCALERA ROTA").

**Los seis no escritos:**

- `equipo_customer_development -> customer_development_team`: **veredicto
  propio B, puesto 637**, y el archivo dice con estas palabras "Sin
  arista entre ellos": comparten el paso de liderar la conversacion con
  clientes pero cada uno se abre despues por un lado distinto. Se honra
  el mandato expreso del archivo.
- `clasificacion_tipos_activos -> tipos_de_pasivos`: el paso senalado
  clasifica ACTIVOS; el hijo entero es sobre PASIVOS, objeto financiero
  distinto con estructura de pasos parecida (mismo libro) pero sin
  relacion de procedimiento. Gemelo estructural falso.
- `proceso_llamada_inicial_venta -> proceso_venta_franquicias`: el hijo es
  el proceso de venta ENTERO, mas amplio que la llamada inicial; ningun
  paso del hijo elabora el paso 6 senalado. La relacion natural, si
  existe, es la inversa.
- `preparacion_preguntas_problema_precall -> preguntas_situacion`: dentro
  de SPIN, Preguntas de Problema y de Situacion son categorias hermanas,
  no madre e hijo; el paso senalado solo menciona minimizar la otra
  categoria como beneficio colateral.
- `timing_solicitud_referidos -> fase_adopt_ciclo_cliente`: el paso
  senalado nombra la fase Adopt solo como ejemplo parentetico; el
  contenido del hijo es la fase COMPLETA del ciclo de Coleman, mucho mas
  amplia que el momento de pedir un referido. Direccion de generalidad al
  reves.
- `requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level`:
  **DISCUTIBLE / PENDIENTE DE DOCTRINA.** El hijo (Crosby) es una CRITICA
  al uso del AQL que el paso de la madre (Juran) recomienda definir, no
  un procedimiento de como hacer ese paso: es un contrapunto de otro
  autor sobre el mismo termino. Ninguna regla escrita dice si una relacion
  "critica a" cuenta como 9.6.2; por `EJECUTOR.md` regla 5 no paro:
  registro el criterio mas conservador (no es jerarquia, no se enlaza) y
  sigo, marcado PENDIENTE DE DOCTRINA.

**Gate 0 el ciclo entero, tras las 24 escrituras**, salidas en
`docs/loop/SALIDA_V78_GATE0_CMD1_TRAMO4.txt` (comando 1), `_CMD2_`
(comando 2) y `_CMD3_` (comando 3): OK, **3.853/3.188/665** (censo
identico), **0 auto-aristas**, **0 duplicadas de titulo**, **0 nodos
divergentes**; motor **25/25**; web **80 ficheros, 1.030 pasadas, 3
saltadas**; tsc **exitcode 0, cero lineas**.

### 4.4. Discutibles de la lectura, marcados AQUI (antes de saber si aciertan)

1. **`diferencia_iso9001_iso9004 -> trilogia_de_juran`.** El paso 3 de la
   madre cita "incorporar metodos de planificacion, control y mejora en
   todos los procesos" y el hijo ES esos tres metodos (la Trilogia de
   Juran). A favor: el paso los nombra como la accion a tomar. En contra:
   la Trilogia es un marco mas fundamental y general que la comparacion
   de normas ISO que lo cita; podria ser la relacion inversa (la Trilogia
   es la base, la comparacion ISO una aplicacion). Se escribio igual,
   marcado para relectura de direccion.
2. **`conformidad_comercio_internacional -> sistema_gestion_calidad`.**
   Mismo patron: el paso 4 de la madre dice "unificar el sistema de
   gestion de calidad", y el hijo ES ese sistema (`sistema_gestion_calidad`)
   de forma generica y amplia, mas fundamental que la conformidad de
   comercio internacional que lo nombra. Se escribio igual, marcado para
   relectura de direccion.
3. **Los cuatro candidatos hacia `value_proposition_startup`**
   (`actualizar_business_model_canvas_tuneup`, `etapa_build_business_case`,
   `extraer_priorizar_hipotesis`, `ventaja_competitiva_producto`).
   `value_proposition_startup` ya tenia **17 madres y 26 hijos** en el
   grafo ANTES de esta vuelta (verificado contra
   `dataset/metadata/master_graph.json`): es un nodo concepto ampliamente
   citado, y cada una de las cuatro madres nueva menciona "propuesta de
   valor" en el paso senalado, aunque ninguna dedica el paso ENTERO solo
   a eso (viene junto a otros elementos: feedback loop, business case,
   hipotesis, ventaja competitiva). A favor: el patron ya esta establecido
   en el grafo para este mismo nodo. En contra: es la primera vez en esta
   campana que CUATRO candidatos de un solo tramo convergen en el mismo
   hijo hub; vale la pena que el auditor confirme que no es sobre-conexion
   por termino generico.
4. **La decision completa de TAREA 3.2** (10 quedan, 1 se revierte),
   primera vez que esta vuelta revierte una arista por la vara de los A en
   vez de solo apartar candidatos nuevos. El criterio ("extremo escrito
   condenado sin ser superviviente") es nuevo en su aplicacion practica,
   aunque se apoya en reglas ya citadas (`P.9` puntos 1 y 2). Vale relectura
   completa, no solo del par revertido.
5. **`requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level`,
   no escrita, PENDIENTE DE DOCTRINA** (seccion 4.3): la tension entre un
   paso que recomienda una practica y un hijo que la critica desde otro
   autor no tiene regla escrita. Se aplico el criterio conservador (no es
   jerarquia).

---

## 5. EL CIERRE, medido AL CIERRE

Commit de esta vuelta que cierra TAREA 1 a 4: `2e040cb6` (rama
`pasada-unica`, push confirmado a `origin/pasada-unica`); este reporte se
cierra en un commit posterior que solo anade este mismo fichero, sin tocar
dato ni cifra.

| | medido con |
|---|---|
| grafo: 3.853 nodos, 3.188 vivos, 665 deprecados (sin cambio: la fase 04 no muda ids) | `python scripts/run_phase1.py --reaplico-curaduria`, corrida de cierre (`SALIDA_V78_GATE0_CMD1_CIERRE.txt` a `_CMD3_`) |
| `nodos_siguientes` | **8.949** (apertura 8.925, mas 1 de TAREA 1.2, menos 1 de TAREA 3.2, mas 24 de TAREA 4: 8.925 + 1 - 1 + 24 = 8.949) |
| `nodos_previos` | **8.928** (misma aritmetica: 8.904 + 24) |
| suma | **17.877** |
| union dirigida unica | **9.572** |
| Gate 0 | OK, ciclo de tres, auto-aristas 0, duplicadas 0, divergentes 0 |
| motor | 25/25 (`SALIDA_V78_MOTOR_CIERRE.txt`) |
| web (corrido desde `web/`) | 80 ficheros, 1.030 pasadas, 3 saltadas (`SALIDA_V78_WEB_CIERRE.txt`) |
| tsc (corrido desde `web/`) | EXITCODE 0, cero lineas (`SALIDA_V78_TSC_CIERRE.txt`) |
| marcador del cribado | A 551, B 72, C 5, D 2.760, n 3.388 (sin cambio, `SALIDA_V78_MARCADOR_CIERRE.txt`) |
| aristas nuevas escritas esta vuelta | 25 (1 de TAREA 1.2, 24 de TAREA 4) |
| aristas revertidas esta vuelta | 1 (TAREA 3.2: `waterfall_vs_agile_development -> desarrollo_de_clientes_customer_development`) |
| pares leidos y no enlazados esta vuelta (tramo 4, con razon) | 6 |
| operaciones cerradas esta vuelta | 0 |
| correcciones declaradas esta vuelta | 5 (1.2, 1.3, 1.4, 1.5, y la reversion de 3.2) |
| bolsa de `OP-E-01` restante sin leer (filtrada por `P.9.1` ensanchado con la vara de los A, esta vuelta) | **161 de 191** (191 filtrados menos los 30 leidos: 24 escritas mas 6 no escritas) |

Verificado con `python docs/loop/_auditor_v77_conteo.py 2e040cb6` que las
cifras de arriba coinciden con el estado del arbol de trabajo tras el
cierre (`SALIDA_V78_CONTEO_CIERRE.txt`).

---

## 6. LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Los cinco discutibles de la seccion 4.4 (arriba) son los que esta vuelta
trae para relectura ciega. Los seis discutibles de la vuelta 77 (seccion
3.4 de su reporte) ya fueron auditados y adjudicados en el acta 77
(D1 a D6, todos A FAVOR o resueltos), no se repiten aqui.

---

## 7. PENDIENTES DE DOCTRINA

**Uno nuevo**, seccion 4.3: ninguna regla escrita dice si una relacion
"el hijo critica la practica que el paso de la madre recomienda" (distinto
autor, mismo termino, postura opuesta) cuenta como jerarquia 9.6.2.
Ejemplar: `requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level`.
Aplique el criterio conservador (no se enlaza) y lo registro en vez de
pararme, por `EJECUTOR.md` regla 5.

---

## 8. LO QUE QUEDA PENDIENTE PARA LA VUELTA SIGUIENTE

- Continuar `OP-E-01` con un TRAMO 5, recalibrando la bolsa antes de leer
  (regla EL INSTRUMENTO MANDA: no reusar
  `PASO_NODO_CALIBRADO_FILTRADO_V78.jsonl`, el grafo ya se habra movido
  otra vez con las 24 aristas de este tramo).
- El par `PENDIENTE DE DOCTRINA` de 4.3 (seccion 7) espera adjudicacion.
- Los cinco discutibles de 4.4 esperan la relectura ciega del auditor,
  especialmente la decision completa de TAREA 3.2 (unica reversion de
  arista por la vara de los A hecha hasta ahora).
- Las diez aristas de la fase 04 que la vara de los A sigue tocando
  (3.3) quedan como observacion, no como parada: ninguna operacion las
  condena hoy.
- `OP-E-02` sigue CERRADO (vuelta 76), sin cambio.
- `OP-E-03` sigue esperando a que `OP-E-01` termine entero.
- `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y
  `OP-M-01-SEXTO` siguen esperando a la fase 06 (remision escrita, no se
  tocan).
- `OP-E-06` y `OP-E-07` siguen libres de bloqueo de dependencia pero
  esperan su turno en el orden escrito.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada (esta
vuelta: hecho al cierre de este mismo reporte). Cero guiones largos y cero
guiones medios. El hook corrio en el commit sin saltarse. No se adivino
nada que no se pudiera medir.
