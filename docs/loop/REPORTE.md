# REPORTE VUELTA 120 (MODO AUSTERO, tope 80 lineas)

Apertura sellada en vivo: `SALIDA_V120_HEAD_APERTURA.txt` = `5bf5f786`, primer
commit de la vuelta `bac06ba5` (hijo directo), `verificar_apertura_sellada.py
--vuelta 120` VERDE (8 ficheros, todos nacidos en `bac06ba5`).

**CABECERA**, tallada con `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 120`:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `5bf5f786` (asunto real leido de git log: 'ACTA DE LA VUELTA 119 DEL AUDITOR: dato impecable, guardas perdidas, y un universal mio que era falso.'), HEAD real de apertura `5bf5f786` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `32a03035` (leido de `SALIDA_V120_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

Pegada entera desde `python scripts/loop/tallar_cabecera_reporte.py --fase04
--vuelta 120`, sin editar ninguna celda.

**TAREA 1.** Sello de apertura en vivo (guarda perdida en la 119, ahora VERDE)
y siete salidas con nombre canonico. Ciclo de tres corrido dos veces (apertura
y cierre): `run_phase1.py --reaplico-curaduria` revierte 71 etiquetas y NUNCA
se dejo asi, siempre seguido de `etiquetas_de_cara.py --aplicar` y
`sync_assets_web.py`; `git diff --numstat` sobre `dataset/web/engine` en cero
las dos veces. Commit `bac06ba5`.

**TAREA 2.** Tres registros aditivos en `docs/PENDIENTES.md` (88/0, `git diff
--numstat`, `grep -c "^-[^-]"` en 0). R.1: el "SIEMPRE" de la `M` espuria
(acta 118 seccion 4.2, heredado por reporte 119 y docstring de
`vuelta119_tarea1_guarda_op_c05_contenido.py`) es FALSO como universal,
reverificado hoy: `--caso-rojo` de la guarda vieja EXIT 0, `git status
--porcelain -- dataset/` vacio antes y despues. Se corrige el diagnostico, no
el arreglo; ningun codigo se reescribe. R.2: quinta entrada de la ficha
`vigencia-del-marco-internacional`: el superviviente de `OP-S-01` sigue
diciendo NAFTA en `resumen_teorico`/`pasos_accionables` pese al titulo ya
corregido; anotado, nodo sin tocar. R.3: caso positivo que faltaba de las
guardas de `OP-S-01`, corridas hoy: ambas EXIT 1 limpio (titulo: "no se pisa
un estado distinto al medido"; operaciones: `ValueError` sin capturar en
`verif.index(PUNTO4_VIEJO)`, ya fuera de lista tras la 119). Ninguna escribio
nada. Commit `02c734ba`.

**TAREA 3.a.** `OP-S-02` (Incoterms) **CERRADA con nomina remapeada**.
Remedida contra el grafo de hoy: de los tres nodos de la nomina (11 ago 2026),
DOS estan deprecados. `terminos_de_venta_incoterms` resuelve por alias a
`incoterms_reglas_comerciales_internacionales`: la cita viaja.
`seguro_de_carga_transporte` resuelve a `seguro_exportacion`: la cita **NO**
viaja completa (el superviviente perdio la palabra "Incoterms" de su paso 1 en
una fusion anterior). Version "Incoterms 2020" (`docs/PENDIENTES.md`, ficha
`vigencia-del-marco-internacional`) escrita en
`incoterms_reglas_comerciales_internacionales.resumen_teorico`, unico campo
tocado, con ancla-guarda + simulacion + mutacion negativa pegadas
(`SALIDA_V120_TAREA3A_SIMULACION.txt`, `..._MUTACION_NEGATIVA.txt`,
`..._ESCRITURA.txt`). Ciclo de tres corrido, `git diff --numstat` 1/1 en los
dos `master_graph.json` y en el nodo; Gate 0 y las tres suites verdes
despues. `OPERACIONES.jsonl`: `OP-S-02` LISTA a HECHA, punto 1 de
`verificacion` acotado por correccion declarada citando el remapeo, `nota`
ampliada sin borrar texto viejo (guardas: `..._OPS_SIMULACION.txt`,
`..._OPS_MUTACION_NEGATIVA.txt`, `..._OPS_ESCRITURA.txt`). `seguro_exportacion`
**NO TOCADO**: restituir la palabra perdida es decision de contenido distinta
a "anadir version a una cita que ya existe". Commit `32a03035`.

**3.b.** `OP-S-03` en adelante **NO SE ABRIO**: `OP-S-02` sola llevo
simulacion, mutacion negativa, dos ciclos de Gate 0 mas suites, y cierre de
registro con guarda propia; `OP-S-03` exige la misma relectura entera. Limite
de alcance, no parada; a diferencia de la 119, esta vuelta si entrego trabajo
de fase 05 ejecutado (operacion real cerrada), no solo registro.

**DISCUTIBLES MARCADOS.** (a) La quinta entrada de la ficha (TAREA 2, R.2) es
adjudicacion del auditor por extension, no encargo literal del fundador sobre
ese texto especifico. (b) `seguro_de_carga_transporte`/`seguro_exportacion`
queda fuera de `OP-S-02` por lectura de alcance del ejecutor (restituir
palabra perdida != anadir version), no por regla escrita; PENDIENTE DE
DOCTRINA. (c) `OP-S-03` en adelante no se abrio (3.b).

Commits de la vuelta: TAREA1 `bac06ba5`, TAREA2 `02c734ba`, TAREA3.a `32a03035`.
