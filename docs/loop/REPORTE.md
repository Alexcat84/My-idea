# REPORTE VUELTA 100 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `c8827ef7` (`docs/loop/SALIDA_V100_HEAD_APERTURA.txt`, leida
ANTES de la 1.a operacion). Cabecera tallada con
`tallar_cabecera_reporte.py --fase04 --vuelta 100`:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `c8827ef7` (ACTA DE LA VUELTA 99 DEL AUDITOR, leido de git log), HEAD real de apertura `c8827ef7` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `c8827ef7` (ACTA DE LA VUELTA 99 DEL AUDITOR, leido de git log), HEAD real de apertura `c8827ef7` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |

Cero movimiento en dataset/web/engine en toda la vuelta: LECTURA DIRIGIDA y
medicion, no cirugia (`EJECUTOR.md` 4).

**TAREA 1 (bloqueante).** `scripts/loop/contar_cierre_efectivo.py`: aplica
`correccion_vNN` por fila, cae ROJO si un `campo_corregido` es desconocido.
Mutacion en verde las 3 (control, quitar 147, campo inventado),
`SALIDA_V100_TAREA1_MUTACION.txt`.

**TAREA 2.** Registros del acta 99 en `PENDIENTES.md`, composicion tallada
1 nivel2/5 nivel3, caso positivo verde contra la vuelta 99.

**TAREA 3.** Relectura conjunta 174 y 175: SE SOSTIENE el caso del auditor
en las dos (NO RESUELTA), `correccion_v100`. Tramo4 60,6% a 66,7%.

**TAREA 4.** Cifra de cierre corregida en `04_ENLACES.md`, `OPERACIONES.jsonl`
y `PENDIENTES.md`: 95/88 (48,1%) crudo -> 92/91 (49,7%) tras TAREA 3. Bug de
anclaje de tabla detectado y corregido en el mismo paso.

**TAREA 5.** Relectura al doble, dos flancos (5 afirmadas menor
`titulo_ratio`, 5 no resueltas mayor). 8 sostenidas. **2 discutibles NUEVOS,
sin marcar antes** (172 `desarrollo_en_espiral->protocepto`, 161
`seis_herramientas_comunicacion_celebracion->celebracion_automatizada_de_hitos`),
las dos NO RESUELTA por exceso de genero del 9.6.2. Recomputado OTRA VEZ en
vivo para no repetir la caida de la vuelta 99: **92/91 -> 90/93 (50,8%)**.

**TAREA 6.** `docs/loop/SALIDA_V100_TAREA6_FASE04_CONTRA_EVIDENCIA.md`: 26
dependencias transitivas unicas de las 10 ops de fase 04 (BFS,
`vuelta100_tarea6_transitivas_fase04.py`), 11 con registro de cierre escrito
y 15 sin el, cada una citada fichero:linea. Cuenta: **1 HECHA, 1 EJECUTABLE
(`OP-E-01`), 8 BLOQUEADAS**. Coincide en TOTAL con la 4.7 del acta 99, pero
la COMPOSICION diverge (el campo `estado` marcaba bloqueante lo que ya
tenia cierre escrito: 11 de las 26). Declarado, sin tocar `estado`, sin
abrir fase nueva.

**LA CIFRA VIGENTE DE `OP-E-03`: 90 / 93 (50,8% NO RESUELTA), n=183**, clase
A 3 B 2 C 1 D 177, invertidas 2 (pares 16, 114).

**DISCUTIBLES MARCADOS para la relectura ciega del auditor:** el **172** y
el **161** (TAREA 5), unica fuente de direccion la lectura del ejecutor
contra el grafo, sin auditor con quien contrastar en vivo esta vuelta.

**PENDIENTE DE DOCTRINA:** ninguno nuevo esta vuelta.

**NOTA DE INSTRUMENTO:** `vuelta99_tarea3_addendum_cierre_opE03.py` sigue
imprimiendo `FILAS DE PARTIDA: %d.` sin interpolar (acta 99, 1.11); no se
toco por regla 1.4 de `vuelta99_tarea3_addendum_cierre_opE03.py` NO
reescribirse.

`wc -l docs/loop/REPORTE.md` medido tras la penultima edicion: **65**, bajo
el tope de 80 del austero.
