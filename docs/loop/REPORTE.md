# REPORTE VUELTA 117 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `15fa9d58` (`docs/loop/SALIDA_V117_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 117` VERDE EXIT 0, salida commiteada (`docs/loop/SALIDA_V117_APERTURA_SELLADA.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 117` (`docs/loop/SALIDA_V117_CABECERA_TALLADA.txt`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `15fa9d58` (asunto real leido de git log: 'ACTA DE LA VUELTA 116 DEL AUDITOR, mas el encargo de la 117.'), HEAD real de apertura `15fa9d58` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `ab062da2` (leido de `SALIDA_V117_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

sha256 identico en apertura y cierre (`f0e399396745...`, 8.391.653 bytes). Cero movimiento en `dataset/`, `web/`, `engine/` esta vuelta (`git diff --stat 15fa9d58..ab062da2 -- dataset/ web/ engine/` vacio).

**TAREA 1, LOS OCHO REGISTROS DEL ACTA 116.** D.1 a D.9 en `docs/PENDIENTES.md` (cinco CAIDA: D.1 a D.4 del ejecutor, D.5 del auditor; tres SIN_CAIDA: D.6, D.7, D.8), mas correccion declarada pegada debajo del C.5 viejo de la 116 (texto intacto). Composicion tallada (8 filas, 5/3, cotejo ninguno) en `docs/loop/SALIDA_V117_TAREA1_COMPOSICION.txt`, diff de fidelidad cero lineas.

**TAREA 2 BLOQUEANTE.** `vuelta117_guardas_cierre.py`: el INSTRUMENTO 1 (`tallar_veredictos_reporte.py` sobre el propio REPORTE.md) entra a `INSTRUMENTOS`; apertura y cierre imprimen `len(INSTRUMENTOS)` y `total_casos` con `%d`, ningun literal. Los 29 casos de la 116 siguen enteros. MUTACION BB (`docs/loop/SALIDA_V117_TAREA2_3_MUTACION_BB_ANTES.txt` dice 9, `_DESPUES.txt` dice 8; veredicto en `docs/loop/SALIDA_V117_TAREA2_3_MUTACION_BB_VEREDICTO.txt`: PASA EXIT 0). Absolutos de la Y, contra la cifra del auditor (16/5/59 union 73 crudo, 15/4/58 union 72 neto): re-medidos hoy sobre 636 `.py` de `scripts/loop` (633 mas los tres de esta tarea): **crudo 16/5/59 union 73, neto 15/4/58 union 72, IDENTICO, ningun absoluto bajo.**

**TAREA 3 (mide, no abre ni cierra fase).** (3.0) Techo re-corrido tal cual, IDENTICO byte a byte al de la 116 (`docs/loop/SALIDA_V117_TAREA3_0_TECHO.txt`). Techo nuevo: `OP_E_06_DIRECCION_V90.jsonl` 114 filas; `OP_E_07_DIRECCION_V9*` trae 4 ficheros, el ULTIMO es V94 con 84 filas (`docs/loop/SALIDA_V117_TAREA3_0_TECHO_DIRECCION.txt`). (3.1) Criterio de HECHO sobre las tres fuentes con el resolvedor de la casa replicado (`_resolver` de `run_phase1.py:989-1009`): OP-E-01 98/98 presentes, OP-E-06 114/114 (100 directo+14 alias), OP-E-07 84/84 (74+10), CERO rotas y CERO bidireccionales (`docs/loop/SALIDA_V117_TAREA3_1_CRITERIO_HECHO_TRES_FUENTES.txt`). (3.2) Registro de cierre en TRES superficies (nota, encabezado, frase "REGISTRO DE OPERACION HECHA"): las NUEVE de NUEVE dependencias de aguas arriba traen al menos una, citas re-medidas hoy (`docs/loop/SALIDA_V117_TAREA3_2_REGISTRO_CIERRE_TRES_SUPERFICIES.txt`). (3.3) Censo de ejecucion: OP-E-03/06/07 con ADDENDUM; OP-E-02 HECHA; OP-E-01 sin addendum pero 98/98 presentes; las cinco restantes sin addendum ni registro, con sus aristas propuestas mayormente ausentes (solo 1/4 de OP-E-05 presente) (`docs/loop/SALIDA_V117_TAREA3_3_CENSO_EJECUCION_FASE04.txt`). (3.4) Tres criterios de remision sobre las cinco (destino 4 a OP-M-01, 1 a OP-M-03; nomina 16; pregunta_pendiente NINGUNA; adjudicacion escrita en las cinco), tallador de la 116 corrido tal cual primero sobre las siete y acotado despues (`docs/loop/SALIDA_V117_TAREA3_4_CRITERIOS_REMISION_CINCO.txt`). (3.5) Cero aristas escritas o retiradas, cero cambios de `estado`, ninguna fase abierta ni cerrada.

**TAREA 4.** Registro aditivo en `docs/plan/04_ENLACES.md`: correccion declarada del registro de la vuelta 102 (OP-E-06/OP-E-07 salen de las "7 BLOQUEADAS" por la doctrina adjudicada, `estado` intacto), censo de cierre en dos mitades (destino cumplido: OP-E-02/03/06/07; remitidas: las cinco), y el limite explicito (no cierra la fase). Medido: `git diff --numstat` 94 lineas insertadas, 0 borradas; difflib confirma SOLO INSERCIONES = True (`docs/loop/SALIDA_V117_TAREA4_DIFF_NUMSTAT.txt`).

**GUARDAS DEL CIERRE.** `vuelta117_guardas_cierre.py` corrido AL CIERRE, con este REPORTE.md ya escrito: `docs/loop/SALIDA_V117_GUARDAS_CIERRE.txt`.

**DISCUTIBLES MARCADOS.** (a) El orden fijado esta vuelta para el ciclo (Gate0, luego `etiquetas_de_cara.py --aplicar` porque `run_phase1.py` revierte la curaduria en cada recompile, luego motor/web/tsc/censo/aristas/marcador/desfase, sync al final) es el que hizo correr verde `test_gate_alias.py` y el resto del ciclo; no es doctrina nueva, la nota de higiene ya lo anticipaba, pero esta vuelta lo dejo escrito en codigo por primera vez con esta secuencia exacta: si el orden correcto es otro, lo traigo aqui. (b) El resolvedor de alias de la TAREA 3.1/3.3 es una REPLICA declarada de `_resolver()` de `run_phase1.py` (no importable por ser funcion anidada): si existe una version realmente reutilizable que no localice, lo traigo aqui. (c) OP-E-01 queda sin categoria adjudicada en el censo de la TAREA 4.2 (no trae ADDENDUM pero sus 98/98 ya estan en el grafo): decision del auditor en la 118.

`wc -l docs/loop/REPORTE.md` AL CIERRE en `docs/loop/SALIDA_V117_WCL_CIERRE.txt`.
