# REPORTE VUELTA 101 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `c6476cb7` (`docs/loop/SALIDA_V101_HEAD_APERTURA.txt`, ANTES
de la 1.a operacion, VERDE contra `scripts/loop/verificar_apertura_sellada.py
--vuelta 101`, `docs/loop/SALIDA_V101_TAREA1_2_MUTACION_APERTURA.txt`).
Cabecera tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 101`
(`docs/loop/SALIDA_V101_CABECERA_TALLADA.txt`):

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `c6476cb7` (ACTA DE LA VUELTA 100 DEL AUDITOR, leido de git log), HEAD real de apertura `c6476cb7` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `c6476cb7` (ACTA DE LA VUELTA 100 DEL AUDITOR, leido de git log), HEAD real de apertura `c6476cb7` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |

Cero movimiento en dataset/web/engine en toda la vuelta.

**TAREA 1 (bloqueante), dos guardas de codigo.** (1.1)
`prueba_mutacion_contar_cierre_efectivo.py` reescrita EN RELATIVO (ninguna
cifra congelada): remedia la CAIDA DE GUARDA ENVEJECIDA de la vuelta 100
(EXIT 1 contra literales viejos). Las 3 pasan contra 90/93 de hoy
(`SALIDA_V101_TAREA1_MUTACION.txt`). (1.2)
`scripts/loop/verificar_apertura_sellada.py`, nombre estable: comprueba con
git que los `SALIDA_V<N>_*_APERTURA.txt` nacen en el primer commit de la
vuelta. Mutacion: VERDE sobre la 101, ROJO sobre la 100 (8 ficheros nacidos
en el ultimo commit, caso negativo real). (1.3) usada sobre esta apertura:
VERDE. Arreglo de un minuto: `%d` sin interpolar en
`vuelta99_tarea3_prueba_mutacion.py:62`, sin re-correr el script.

**TAREA 2.** Registros del acta 100 en `PENDIENTES.md`: confirma 172 y 161
NO RESUELTA (la letra: mueve el par anadir genero, no desbordar paso); las
tres caidas del ejecutor nombradas; la correccion declarada de la TAREA 6
(15 CON cierre / 11 SIN, no 11/15); la caida de procedimiento del auditor.
Composicion tallada 1 nivel2/5 nivel3, caso positivo IDENTICO byte a byte
contra la vuelta 100.

**TAREA 3.** La fase 0 contra las TRES sedes mas la vara del codigo vivo
(`docs/loop/SALIDA_V101_TAREA3_FASE0_TRES_SEDES.md`). Las cuatro operaciones
que el auditor dejo "a verificar" (`OP-C-01`, `OP-C-02`, `OP-C-03`,
`OP-S-06`) SI tienen registro de cierre escrito, en una sede que el criterio
de la vuelta 100 no miraba: el COMMIT ("FASE 0, OP-X EJECUTADA", 14 ago
2026, en `pasada-unica`). Las seis (con `OP-C-04`/`OP-S-07`, ya cerradas en
acta) corren o estan aplicadas HOY, medido linea por linea contra el codigo
y el dato (citas en el fichero). **PREGUNTA PARA EL AUDITOR, NO RESUELTA
AQUI:** si un commit "EJECUTADA" sin frase de cierre en pagina ni en acta
cuenta como "registro de cierre escrito", la fase 04 pasa de 1/1/8 a 1/2/7
(solo bloqueada por las 4 mesas de fase 06). No se toco `estado` ni se abrio
fase; PENDIENTE DE DOCTRINA.

**LA CIFRA VIGENTE DE `OP-E-03`: 90 / 93 (50,8% NO RESUELTA)**, n=183, clase
A 3 B 2 C 1 D 177, invertidas 2 (pares 16, 114); sin movimiento esta vuelta.

**DISCUTIBLES MARCADOS:** ninguno nuevo esta vuelta (TAREA 3 es medicion de
fase 0, no lectura dirigida); 172 y 161 quedan CONFIRMADOS por el auditor
(2.1).

**PENDIENTE DE DOCTRINA:** si el commit cuenta como sede de "registro de
cierre escrito" para la fase 04 (TAREA 3, arriba).

`wc -l docs/loop/REPORTE.md` medido AL CIERRE, tras esta misma edicion (y
vuelto a correr una vez mas antes del commit, para no repetir la CAIDA DE
GUARDA ENVEJECIDA de la vuelta 100): **67**, bajo el tope de 80.
