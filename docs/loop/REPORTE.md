# REPORTE VUELTA 135 (MODO AUSTERO)

HEAD sellado de apertura: `e12e4c36`
commit de nacimiento de las salidas de apertura: `a3b1bbb3`
HEAD sellado de cierre: `2deac539`
Los tres rotulos salen con hash distinto entre si (`tallar_identidad_reporte.py --vuelta 135`).

Cabecera (`tallar_cabecera_reporte.py --fase04 --vuelta 135`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e12e4c36` (asunto real leido de git log: 'ACTA DE LA VUELTA 134 DEL AUDITOR: el trabajo entrego entero y sin una sola caida suya; las tres de hoy son mias y la grande es mi exencion (iii), que deja al auditado apagar la guarda escribiendo tres palabras'), HEAD real de apertura `e12e4c36` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `2deac539` (leido de `SALIDA_V135_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

Cero REGIMEN B: NO se toco un solo nodo. Bateria 1.d
(`SALIDA_V135_BATERIAS_CMP.txt`): 8 IDENTICOS, MOTOR y WEB DISTINTOS solo
por duracion/Start at, diff pegado en `SALIDA_V135_1D_DIFF_MOTOR.txt` y
`_WEB.txt`. Conteo sube CERO aristas. 1.h/1.i VERDE
(`SALIDA_V135_1H_CIERRE_SELLADO.txt`, `_1H_CASOS_POSITIVOS.txt`,
`SALIDA_V135_1J_CITAS.txt`): cierre valido y distinto de la apertura, los
dos casos positivos caen en rojo, citas de este reporte VERDE.

1.e-1.g VERDE (`SALIDA_V135_1E_CITAS.txt`, `_1E_TITULOS.txt`,
`_1G_FUSION_OPS09.txt`, `_1G_ARISTAS_VIVAS.txt`, `_1G_HUERFANAS_LIVE.txt`):
citas y titulos cotejan (1 dup. cubierto), cifras del plan 0 pares
(`SALIDA_V135_1F_CIFRAS_PLAN.txt`), aristas vivas 7296==7296 PERDIDAS 0
NUEVAS 0, huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1 FABRICADAS 0.

TAREA 2, la puerta de servicio se tapia (acta 134, 4.1), REGIMEN de
codigo. 2.a (`SALIDA_V135_2A_DIAGNOSTICO.txt`): COBERTURA real de la 134
1 cotejadas / 3 exentas / 4 cifras; dos SI tenian instrumento cerca, una
NO. 2.b-2.d: la exencion (iii) ahora exige que la guarda compruebe SOLA,
en ventana amplia (+/-2 frases), que ningun SALIDA_V<N>_*.txt este
citado cerca; si lo esta, cae en rojo. Se suma la linea
`CIFRA <etiqueta>: <n> <unidad>` (cotejada por unidad canonica exacta).
2.e, tres mutaciones VERIFICADAS (`SALIDA_V135_2E_MUTACION_1.txt`,
`_2.txt`, `_3.txt`): 118->999 cae en rojo, 54->77 cae en rojo, caso
negativo (fichero citado + linea CIFRA + numero correcto) VERDE.

TAREA 3, registros por adicion (REGIMEN A puro, numstat 73/0, word-diff
CERO palabras borradas). 3.a: R.16 en `docs/PENDIENTES.md` con las cinco
cosas de la 134. 3.b: los dos predicados que separan de 117 a 118 grafias
(`SALIDA_V135_3B_CENSO_DOS_PREDICADOS.txt`). Grafia separadora `The
Field Guide to Understandin - Dekker, Sidney;` con 76 nodos
(`SALIDA_V135_3B_CENSO_DOS_PREDICADOS.txt`). 3.c: regla del singleton
anadida a la novena entrada de la ficha `fuente`, citando acta 134 3.2 y
`vuelta133_tabla_mapeo_propuesto.py:126,146`.

TAREA 4, la cola se extiende a `Caps?.` (adjudicada, acta 134, 3.3),
REGIMEN A estricto salvo el fichero unico autorizado, cero nodos. 4.a:
caso positivo (Cap. 9 entra a la familia Edwards) y negativo OK; peldano
localizador-con-Cap antes del prefijo, de 105 a 55 grupos
(`SALIDA_V135_4A_COLA_CON_CAP.txt`). 4.b: `OP_S_11_MAPEO_PROPUESTO.md`
rehecho con los seis peldanos historicos (111, 108, 106, 105, 104) mas el
peldano final de 54 grupos (`SALIDA_V135_4B_PELDANOS.txt`, 17 con 2+ / 92
en grupo, 37 solos, 3 SINTETICAS: Edwards et al., DeMarco y Lister,
Hubbard). 4.c: `verificar_cabecera_mapeo.py` extendido a los seis
peldanos, VERDE contra la tabla real; mutacion (borra el peldano 54)
VERIFICADA (`SALIDA_V135_4C_MUTACION.txt`). 4.d: la meta de 55 de
`05_SANEO.md` queda rebasada por uno (54 grupos, `SALIDA_V135_4B_PELDANOS.txt`);
`05_SANEO.md` no se toca, `OP-S-11` LISTA, `OP-S-12` no se abre.

DISCUTIBLE PARA LA CIEGA: la ventana AMPLIA (+/-2 frases) de 2.b es
definicion NUEVA de esta vuelta, no doctrina ya escrita: el cotejo normal
sigue FORWARD-only (MISMA doctrina que `verificar_cifras_del_plan.py`), y
no habria alcanzado la cita de 4.a desde la cifra de 118 (grafias sin
recortar, esta ANTES). La ensancho solo para la legalidad de la
exencion; no la resuelvo yo.

Correcciones declaradas de la 134: R.16 completo en `docs/PENDIENTES.md`.
Credito de CLASE y de CIFRA PUBLICADA: sigue en CERO. Tope de 1.k:
`wc -l docs/loop/REPORTE.md` da 80 lineas (<=80).
