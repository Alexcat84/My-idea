# REPORTE VUELTA 134 (MODO AUSTERO)

HEAD sellado de apertura: `04e61206`
commit de nacimiento de las salidas de apertura: `feba8006`
HEAD sellado de cierre: `41f3e156`
Los tres rotulos salen con hash distinto entre si (`tallar_identidad_reporte.py --vuelta 134`).

Cabecera (`tallar_cabecera_reporte.py --fase04 --vuelta 134`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `04e61206` (asunto real leido de git log: 'ACTA DE LA VUELTA 133 DEL AUDITOR: el trabajo entrego bien y la escalada que encargue en la 132 aguanto tres mutaciones mias, dos de ellas que el ejecutor no probo'), HEAD real de apertura `04e61206` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `41f3e156` (leido de `SALIDA_V134_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

Cero REGIMEN B: NO se toco un solo nodo. Bateria 1.d
(`SALIDA_V134_BATERIAS_CMP.txt`, sin instrumento la cuenta de familias): 8
IDENTICOS, MOTOR y WEB DISTINTOS solo por duracion/Start at, diff pegado en
`SALIDA_V134_1D_DIFF_MOTOR.txt` y `_WEB.txt`. Conteo sube CERO aristas.

1.e-1.g VERDE (`SALIDA_V134_1E_CITAS.txt`, `_TITULOS.txt`,
`_1F_CIFRAS_PLAN.txt`, `_1G_FUSION_OPS09.txt`, `_1G_ARISTAS_VIVAS.txt`,
`_1G_HUERFANAS_LIVE.txt`, sin instrumento el detalle de cada cifra): citas
y titulos cotejan (1 dup. cubierto), cifras del plan 0 pares (sin instrumento),
fusion_ops09 dos autopruebas OK, aristas vivas 7.296==7.296 PERDIDAS 0
NUEVAS 0, huerfanas TOTAL 29 HEREDADAS 29 REPARADAS 1 FABRICADAS 0.

TAREA 2, guarda cegada (acta 133, 4.4), REGIMEN de codigo. 2.a
(`SALIDA_V134_2A_DIAGNOSTICO.txt`, sin instrumento el detalle): las siete
cifras sin fichero eran las siete motivo (A). 2.b/2.c: salida de
emergencia estrechada a tres exenciones cerradas en
`verificar_cifras_del_reporte.py`, COBERTURA publicada siempre. 2.d dos
mutaciones sobre el reporte REAL, las dos VERIFICADAS
(`SALIDA_V134_2D_MUTACION_1.txt`, `SALIDA_V134_2D_MUTACION_2.txt`). 2.f
guarda nueva verificar_cabecera_mapeo.py, mutacion VERIFICADA
(`SALIDA_V134_2F_MUTACION.txt`): 106 sin declarar antes de 3.c, VERDE
despues; efecto secundario propio (pisaba OP_S_11_MAPEO_PROPUESTO.md y dos
SALIDA_V133_* sellados) detectado y blindado con foto de bytes, md5 igual.

TAREA 3, registros por adicion (REGIMEN A puro salvo donde se dice otra
cosa). 3.a: R.15 en `docs/PENDIENTES.md` (sin instrumento el detalle),
correcciones de la 133. 3.b: par caducado `docs/PENDIENTES.md:3059` (FUE
VERDADERO en `5eb04ca5`, CADUCADO hoy, vive en `:3138`; `:1696` no era el
relevo), pegado al pie de BOLSA 2a y R.13(6). 3.c: peldano 106 repuesto por
adicion en `docs/plan/OP_S_11_MAPEO_PROPUESTO.md` (REGIMEN A CON LINEA
VIEJA, unico fichero viejo con contenido tocado; word-diff porcelain 0
lineas borradas, `SALIDA_V134_3C_VERIFICAR_CABECERA.txt` VERDE).

TAREA 4, cola `Cap.`, REGIMEN A estricto, cero nodos, solo medicion.
4.a (`SALIDA_V134_4A_CENSO_COLA.txt`, sin instrumento el detalle): mi
medicion 999 grafias (sin instrumento) sin recortar (encargo: 117), `Cap.`
48, `Waltzing` 5. 4.b (`SALIDA_V134_4B_EFECTO_CAP.txt`, sin instrumento el
detalle): cola extendida a `Caps?.` da 54 grupos (sin instrumento), 3
canonicas SINTETICAS de grupo multi miembro (Edwards et al., DeMarco y
Lister, Hubbard); encargo: 5 SINTETICAS.
4.c (`SALIDA_V134_4C_CONVIVENCIA.txt`, sin instrumento el detalle): 10
familias con localizador, CERO con las dos formas, 5 solo escrita/5 solo
abreviada, DISJUNTOS confirmado. 4.d (`SALIDA_V134_4D_SINTETICAS.txt`, sin
instrumento el detalle): 4 de 5 canonicas legibles, la quinta NO
(parentesis desbalanceado); acentos BIEN en bytes crudos y texto utf-8 de
`dataset/nodos/el_riesgo_eres_tu.json`, sin caracter de reemplazo (lo visto
en consola sin reconfigurar era artefacto de terminal).

DISCUTIBLE PARA LA CIEGA: 4.a y 4.b traen DOS discrepancias contra el
contraste del encargo (117 vs mis 118; 5 vs mis 3 SINTETICAS, por la
semantica de `calcular()`: solo marca SINTETICA un grupo de 2+ miembros
sin libro, y Cullinane mas la grafia malformada son singleton). Ninguna la
resuelvo yo. Por acta 133 4.1/4.7: la extension a `Cap.` NO se adjudica
esta vuelta, solo se mide (4.e).

Correcciones declaradas de la 133: R.15 completo en `docs/PENDIENTES.md`.
Credito de CLASE y de CIFRA PUBLICADA: sigue en CERO. Tope de 1.k:
`wc -l docs/loop/REPORTE.md` da 80 lineas (<=80).
