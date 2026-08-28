# REPORTE VUELTA 115 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `5b58a6c4` (`docs/loop/SALIDA_V115_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 115` VERDE EXIT 0 y su salida commiteada esta vez (`docs/loop/SALIDA_V115_APERTURA_SELLADA.txt`, cierra la observacion B.4 del acta 114).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 115` (`docs/loop/SALIDA_V115_CABECERA_TALLADA.txt`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `5b58a6c4` (asunto real leido de git log: 'ACTA DE LA VUELTA 114 DEL AUDITOR, mas el encargo de la 115.'), HEAD real de apertura `5b58a6c4` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `9420db0d` (leido de `SALIDA_V115_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

sha256 identico en apertura y cierre (`f0e399396745...`, 8.391.653 bytes). Nueve mediciones iguales: cero movimiento en `dataset/`, `web/`, `engine/` esta vuelta (`git diff --stat 73b72787..277d9b0a -- dataset/ web/ engine/` vacio).

**TAREA 1, LOS DOS BLOQUES.** Bloque A (registros del acta 113, heredados: A.1-A.3 CAIDA EJECUTOR, A.4-A.5 CAIDA AUDITOR, A.6 SIN_CAIDA, con A.1 y A.3 anadidos como CERRADOS en la 114 y A.2 abierta hacia la TAREA 2.3) y bloque B (registros del acta 114: B.1 y B.2 y B.4 SIN_CAIDA, B.3 CAIDA AUDITOR) en `docs/PENDIENTES.md`. Composicion tallada: 10 filas, 6 CAIDA / 4 SIN_CAIDA, cotejo SOBRAN/FALTAN NINGUNO (`docs/loop/SALIDA_V115_TAREA1_COMPOSICION.txt`). Fidelidad de extraccion CERO diferencias (`docs/loop/SALIDA_V115_TAREA1_DIFF_FIDELIDAD.txt`).

**TAREA 2 BLOQUEANTE.** Fichero nuevo `scripts/loop/vuelta115_guardas_cierre.py` (28 casos, historia de la 113 intacta) suma una capa de MOTIVO: cada caso lleva un `ESPERADO_BASE` fijo (anclado aparte de `CASOS`, no derivado de el) y, cuando el esperado de hoy difiere, la salida imprime `MOTIVO: ...` (si esta en `MOTIVOS`) o `ALERTA: ESPERADO CAMBIADO SIN MOTIVO DECLARADO` (si no, y ademas ROMPE la guarda). T arrastra su motivo desde la vuelta 113 (acta 113, 4.4): la caida A.2 ("la cita promete detalle y no lo tiene") queda CERRADA, el motivo vive ahora en la propia salida. MUTACION Z (`scripts/loop/vuelta115_tarea2_4_mutacion_z.py`): copia con el esperado de un caso de control (`Z_SONDA`) cambiado Y su comportamiento real mutado para que siga en `[CALZA]`, SIN anadirlo a `MOTIVOS`. ANTES (real, `docs/loop/SALIDA_V115_TAREA2_4_MUTACION_Z_ANTES.txt`): `[CALZA]` sin alerta, EXIT 1 (por T y por los dos instrumentos que dependian del reporte, ver abajo). DESPUES (mutada, `docs/loop/SALIDA_V115_TAREA2_4_MUTACION_Z_DESPUES.txt`, contra el ANTES de `docs/loop/SALIDA_V115_TAREA2_4_MUTACION_Z_ANTES.txt`): `Z_SONDA` sigue `[CALZA]` PERO imprime la ALERTA nombrandolo y la guarda cae a ROJO: no dice CALZA en silencio.

**TAREA 3, EL TERRITORIO DE LECTURA DE OP-E-03 SE ACABO.** (3.0) Techo re-corrido tal cual (`vuelta114_tarea3_0_techo.py`, historia, sin tocar), sellado en su propio commit ANTES de medir: **10 fase 04, 220 OP-E-01, 10 fase 05, 71 total**, identico a la 114 (`docs/loop/SALIDA_V115_TAREA3_0_TECHO.txt`). (3.1) Censo tallado de la fase 04 (`docs/loop/SALIDA_V115_TAREA3_1_CENSO_FASE04.txt`): diez operaciones, su tipo/estado/orden y sus dependencias con fase y estado, calza al digito con el contraste del auditor. (3.2) OP-E-01 contra el grafo de hoy (`docs/loop/SALIDA_V115_TAREA3_2_OPE01_VS_GRAFO.txt`): **220 filas, 98 ESCRITA / 122 NO SE ENLAZA, 98 presentes 0 ausentes** (criterio: hijo en `nodos_siguientes` de la madre O madre en `nodos_previos` del hijo; las 98 calzan en las DOS vistas). (3.3) Registro de cierre en `docs/plan/04_ENLACES.md`, apartado nuevo y aditivo (difflib: 0 borradas, 27 anadidas, `docs/loop/SALIDA_V115_TAREA3_3_DIFF_ADITIVIDAD.txt`): **109 = 80 + 8 + 21, cosecha CERO en las tres tandas**, cierre **74 / 109 (59,6%)** sin cambio (`docs/loop/SALIDA_V115_TAREA3_3_CIERRE_EFECTIVO.txt`), `estado` de OP-E-03 NO SE TOCA (sigue LISTA, acta 100 4.2). (3.4) Censo de la fase 05, SOLO MEDIR (`docs/loop/SALIDA_V115_TAREA3_4_CENSO_FASE05.txt`): diez operaciones en LISTA, nueve sin dependencia y OP-S-12 con nueve, `bloquea_a` de OP-S-11 (OP-A-01, OP-A-02) y OP-S-12 (OP-C-05) publicados, limite del campo `estado` declarado en la propia salida, sin adjudicar orden. (3.5) Cero aristas escritas o retiradas, cero cambios en `estado`, cero operaciones movidas de fase, ninguna fase abierta: `git diff --stat 73b72787..277d9b0a -- dataset/ web/ engine/` vacio.

**GUARDAS DEL CIERRE.** `vuelta115_guardas_cierre.py` corrido AL CIERRE, con `REPORTE.md` ya escrito: NUEVE instrumentos y VEINTIOCHO casos.

**DISCUTIBLES MARCADOS: NINGUNO.** El encargo de la 115 no trae lectura de nodos (TAREA 3 es censo y medicion, con 3.5 "cero aristas escritas o retiradas"): cero relecturas de unidad esta vuelta, casilla vacia en vez de inventada, mismo criterio que la 114 aplico por el mismo motivo (acta 81).

`tallar_veredictos_reporte.py` sobre este mismo reporte, `docs/loop/SALIDA_V115_GUARDAS_CIERRE.txt`.

`wc -l docs/loop/REPORTE.md` AL CIERRE en `docs/loop/SALIDA_V115_WCL_CIERRE.txt`.
