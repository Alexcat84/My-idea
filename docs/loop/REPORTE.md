# REPORTE VUELTA 133 (MODO AUSTERO)

HEAD sellado de apertura: `b4fd942f`
commit de nacimiento de las salidas de apertura: `ccb4d351`
HEAD sellado de cierre: `606d4f99`
Los tres rotulos salen con hash distinto entre si (`tallar_identidad_reporte.py --vuelta 133`).

Cabecera (`tallar_cabecera_reporte.py --fase04 --vuelta 133`), pegada entera:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.184 / 669 | **3.853 / 3.184 / 669** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.198 / 9.180 / 18.378 / 9.833 | **9.198 / 9.180 / 18.378 / 9.833** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `b4fd942f` (asunto real leido de git log: 'ACTA DE LA VUELTA 132 DEL AUDITOR: el trabajo entrego bien (las 129 filas de la tabla cotejadas una por una contra mi propia regla, cero canonicas torcidas, la ciega reproduce 111/108/106 y el 104 del 3.d al digito), pero la linea de identidad publica un commit de nacimiento que ninguno de los once ficheros de apertura tiene, con el instrumento imprimiendo la cifra buena delante. La racha de reporte pasa a DOS y por eso la escalada de AUDITOR.md 1.2 queda ENCARGADA como TAREA 2 bloqueante de la 133.'), HEAD real de apertura `b4fd942f` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `606d4f99` (leido de `SALIDA_V133_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

Cero operacion de REGIMEN B esta vuelta: NO se toco un solo nodo. Bateria de
1.d reducida a APERTURA/CIERRE (`SALIDA_V133_BATERIAS_CMP.txt`): 8 familias
IDENTICOS, MOTOR y WEB DISTINTOS por duracion/Start at, diff entero pegado
en `SALIDA_V133_1D_DIFF_MOTOR.txt` y `_WEB.txt` (una sola clase de linea
cada uno). Conteo sube CERO aristas.

1.e-1.g VERDE: citas, titulos (1 dup. cubierto por excepcion vigente),
cifras del plan (0 pares), fusion_ops09, aristas vivas 7.296==7.296
PERDIDAS 0 NUEVAS 0, huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1 FABRICADAS
0 (`SALIDA_V133_1E_GUARDAS.txt`, `_1F_`, `_1G_`).

TAREA 2, la escalada (AUDITOR.md 1.2, racha en DOS): `tallar_identidad_
reporte.py` (2.a/2.b) reproduce la caida real de la 132 (nacimiento
`5eb04ca5` publicado, `3a5fd829` medido) y `--comparar` cae ROJO nombrando
ese rotulo; dos mutaciones VERIFICADAS (`SALIDA_V133_2C_MUTACION_A.txt`,
`SALIDA_V133_2C_MUTACION_B.txt`).
`verificar_cifras_del_reporte.py` (2.e) coteja pares (numero, unidad
cerrada) contra su `SALIDA_V<N>_*.txt`; mutacion VERIFICADA
(`SALIDA_V133_2E_MUTACION.txt`).

TAREA 3, REGIMEN A puro (`docs/PENDIENTES.md`, 155 lineas anadidas, 0
borradas): R.14 con las cinco cosas del encargo (identidad, "adjudica el
fundador", diff sin pegar, mi correccion de cifra remitida, las otras dos
caidas), ramales (xvi)/(xvii); UNDECIMA entrada de la ficha `fuente` con
la tabla de las 4 combinaciones del acta 132 (3.1).

TAREA 4, REGIMEN A puro + REGIMEN A CON LINEA VIEJA: 4.a cola +Apendice
(`SALIDA_V133_4A_COLA_CON_APENDICE.txt`) 106->105; 4.b prefijo sobre
recortada APLICADO, atado (`SALIDA_V133_4B_PREFIJO_APLICADO.txt`) 105->104,
familia Lindstrom 7 grafias/23 nodos, canonica `(J. Ross, 2014)`, NO
sintetica; 4.c SINTETICAS censo 1->0, regla NOVENA entrada VIGENTE Y SIN
CASO; 4.d tabla rehecha (word-diff `SALIDA_V133_4D_WORDDIFF.txt`), cifras
111/108/105/104, 14 grupos 2+ (39 grafias), 90 solos, faltan 49 colapsos
para 55. `OP-S-11` sigue LISTA, cero nodos tocados.

DISCUTIBLE MARCADO PARA LA CIEGA: `docs/PENDIENTES.md:3059` (citado en R.13
punto 1 para Reason) HOY no trae "Managing the Risks" (dice "La cobertura
al lado..."); la cita que si la trae, en la misma vecindad, es
`docs/PENDIENTES.md:1696`. Declarado en R.13(6), no resuelto por mi.

Correcciones declaradas de la 132 (auditor): R.14 completo, ver arriba.
Credito de CIFRA PUBLICADA: sigue en CERO (nada declarado como caida de
esta clase esta vuelta).

Tope de 1.k: `wc -l docs/loop/REPORTE.md` da 67 lineas (<=80).
