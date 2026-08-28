# REPORTE, VUELTA 99 (MODO AUSTERO, 27 ago 2026)

**CAIDA PROPIA DE PROCEDIMIENTO, DECLARADA:** la apertura NO se sello antes
de la 1.ª operacion. Remedio: `git diff --stat de4cc0e2 HEAD` excluyendo
`docs/plan`, `docs/loop`, `docs/PENDIENTES.md` y `scripts/loop` da VACIO, asi
que `dataset/`, `web/` y `engine/` son BYTE A BYTE IGUALES entre la apertura
real y ahora; las salidas de apertura del ciclo son copias declaradas de las
de cierre, no mediciones independientes.
## Cabecera, tallada y pegada entera (`scripts/loop/tallar_cabecera_reporte.py --vuelta 99 --fase04`)
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `de4cc0e2` (ACTA DE LA VUELTA 98 DEL AUDITOR, leido de git log), HEAD real de apertura `de4cc0e2` (sello RECONSTRUIDO DESPUES (commit 47d456e2), leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `de4cc0e2` (ACTA DE LA VUELTA 98 DEL AUDITOR, leido de git log), HEAD real de apertura `de4cc0e2` (sello RECONSTRUIDO DESPUES (commit 47d456e2), leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |
`--comparar docs/loop/REPORTE.md` da **CABECERA IDENTICA AL TALLADOR**
(`docs/loop/SALIDA_V99_COMPARAR_CIERRE.txt`).
## TAREA 1, acta 98 en `docs/PENDIENTES.md`
Siete adjudicaciones (3.1 a 3.7) por numero y linea de `ACTA_AUDITOR.md`
(35278 a 35395), tres caidas nombradas, correccion de cita 9.6.3 a 9.6.2 en
filas 147/148. Composicion tallada 7/3, 0 sobran/faltan; anadido 1 nivel 2 +
4 nivel 3, caso positivo reproduce 1/5 de la vuelta 98.
## TAREA 2, relectura conjunta del 147
`consortium_benchmarking` NO cabe entero en el paso 2 de
`clasificacion_benchmarking` (9.6.2). Se sostiene el auditor: AFIRMADA a NO
RESUELTA. Recomputado: **20/30/60,0% a 19/31/62,0%**. Correccion declarada
en el JSONL (`correccion_v99`, texto viejo intacto) y en `04_ENLACES.md`.
## TAREA 3, `OP-E-03` CIERRA, 183 de 183
33 filas nuevas (151 a 183): D las 33, direccion 13/20 (60,6% NO RESUELTA),
mediana `titulo_ratio` 73,2, confirma la prediccion del acta 98. Cierre
entero (4 ficheros de tramo, no 3 como decia el encargo, discrepancia
declarada): A 3, B 2, C 1 (par 111), D 177; direccion 95/88 (48,1%);
invertidas 2 (16, 114). Mutacion: 1 verde, 7 caen. Addendum simulado,
aplicado, idempotente (reaplicar EXIT 1). `estado` se queda en LISTA.
## TAREA 4, estado real de la fase 04 (medicion, nada tocado)
1 HECHA (`OP-E-02`), 2 ejecutables hoy sin dependencia externa viva
(`OP-E-01` sin dependencias; `OP-E-07` solo depende de `OP-E-06`, misma
fase), 7 esperan otra fase: 4 a `OP-M-01`/`FUSION` (fases 06/03), 1 a las
siete `OP-D` (fase 02). `OP-E-01` y `OP-E-03` tienen cierre citado en su
nota y siguen en LISTA por politica declarada (backlog 14 ago: "el estado
de verdad es el repo"). Detalle: `docs/loop/SALIDA_V99_TAREA4_ESTADO_FASE04.md`.
## DISCUTIBLES MARCADOS, para la relectura ciega
1. TAREA 2 (147): muevo mi propia lectura original a NO RESUELTA.
2. Puesto 152: NO RESUELTA por exceso del hijo; frontera fina con RESUELTA.
3. Puestos 156/157/158 (iman `metricas_calidad`): dos RESUELTA, una no.
4. Puesto 175 (`valor_de_vida_del_cliente`): RESUELTA por nombre literal,
   pero el hijo anade material fuera de la madre.
5. TAREA 4: "ejecutable hoy" de `OP-E-07` es formal, no practico.
## PENDIENTE DE DOCTRINA
Ninguno nuevo. "Tres ficheros de tramo" (encargo) contra "cuatro" (medido)
queda declarada en TAREA 3, no resuelta por mi.

**Lineas:** `wc -l docs/loop/REPORTE.md`, corrido tras escribirlo, da **58**.
