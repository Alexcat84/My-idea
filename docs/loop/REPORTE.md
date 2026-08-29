# REPORTE VUELTA 126 (MODO AUSTERO)

Identidad (git): rama `pasada-unica`, HEAD sellado de apertura `7150339f`
(acta 125), commit de nacimiento de las salidas de apertura `eb18f3d2`
(hijo directo del acta), HEAD sellado de cierre `ac22c1c5`
(`SALIDA_V126_HEAD_CIERRE.txt`). `verificar_apertura_sellada.py --vuelta 126`:
VERDE, 8/8 nacidos en el primer commit.
## Cabecera tallada (`tallar_cabecera_reporte.py --fase04 --vuelta 126`)
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.184 / 669 | **3.853 / 3.184 / 669** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.194 / 9.176 / 18.370 / 9.829 | **9.195 / 9.177 / 18.372 / 9.830** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+1 / +1 / +2 / +1** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 2 fila(s): `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **3 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `7150339f` (asunto real leido de git log: 'ACTA DE LA VUELTA 125 DEL AUDITOR: la vuelta hace bien todo lo que se le pidio, y mi propio codigo encuentra una arista vivo-vivo que la fusion corto y no declaro; OP-S-09 queda CERRABLE, no cerrada.'), HEAD real de apertura `7150339f` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `ac22c1c5` (leido de `SALIDA_V126_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

**Baterias cmp** (`SALIDA_V126_BATERIAS_CMP.txt`, 21 pares): GATE0_CMD1 y
MARCADOR apertura=cierre IDENTICOS (su salida no depende de aristas puntuales
ni de `condiciones_activacion`: GATE0 mide estructura/censo/dups, MARCADOR
dedup de titulo). TSC IDENTICO en las 4 etapas (no lee `dataset/`).
CONTEO/MOTOR/WEB/DESFASE DISTINTOS: escritura real de 3.a/3.d llegando,
timings de motor/web (avisado en 1.d, no es falla).
## TAREA 1.g, la (4) inalcanzable REEMPLAZADA (correccion de la caida 5.2)
Contrato nuevo en `verificar_fusion_ops09.py` (aristas heredadas del muerto,
resueltas con el resolutor de hoy). Autopruebas (a) alias y (b) arista
heredada VERDE (`SALIDA_V126_1G_AUTOPRUEBA_AB.txt`). Caso rojo real sobre
WORK, guarda NUEVA: ROJO nombrando `dia_cero_defectos_2 -> eliminacion_causas_error_4`
(`SALIDA_V126_1G_CASO_ROJO_WORK_NUEVA.txt`). Misma guarda VIEJA: VERDE
(`SALIDA_V126_1G_CASO_ROJO_WORK_VIEJA.txt`). Discrepancia: `--ref c9ac2fb8`
(literal del encargo) no aisla el caso, ninguna de las 4 fusiones existe a
ese ref (`SALIDA_V126_1G_REF_C9AC2FB8.txt`); WORK si reproduce el ejemplar.
## TAREA 1.h, guarda nueva `verificar_aristas_vivas.py`
Aristas vivo-vivo antes/despues proyectadas por el resolutor de hoy, autoprueba
VERDE. `--antes c9ac2fb8 --despues WORK` (antes de 3.a): 7293/7292, PERDIDAS 1.
## TAREA 3.a, reposicion REGIMEN B
`dia_cero_defectos_2 -> eliminacion_causas_error_4`, dos vistas. Simulacion:
VERDE (`SALIDA_V126_OPS09REP_SIMULACION.txt`). Mutacion negativa: ROJO
esperado (`SALIDA_V126_OPS09REP_MUTACION_NEGATIVA.txt`). 2.ª pasada: ROJO
con `git status --porcelain` pegado (`SALIDA_V126_OPS09REP_ROJO_SEGUNDA_PASADA.txt`).
Bateria OPS09REP verde; `verificar_aristas_vivas.py` PERDIDAS 1->0
(`SALIDA_V126_OPS09REP_ARISTAS_VIVAS_DESPUES.txt`).
## TAREA 3.b, cierre OP-S-09 (adjudicado, acta 125 secc. 4.2)
`estado` LISTA->HECHA. Nota recorre las 4 verificacion: 51 pares (47
CONTINUA+4 REPITE, `SALIDA_V126_OPS09_VERIFICACION1_51PARES.txt`); alias
VERDE; (4) nueva VERDE + PERDIDAS 0; sufijo numerico sin cambio (residuo
`eliminacion_causas_error_4` en ficha).
## TAREA 2, REGIMEN A
2.a: correccion en OP-S-09 (extremos ayer/hoy, 4 cifras, 3 varas). 2.b: R.8
en PENDIENTES.md (3 caidas del acta 125 + ramal vii). 2.c: ficha nueva
`aristas-huerfanas-por-fusion`, 32 medidas hoy, NO se tocan
(`SALIDA_V126_2C_ARISTAS_HUERFANAS_TOTALES.txt`).
## TAREA 3.c+3.d, OP-S-10
3.c (REGIMEN A): de 31, 28 vivos; 2 ya condicionan, 21 en ningun sitio, 4
solo resumen, 1 solo pasos (`obtencion_marca_registrada`, categoria nueva).
De los 8 "dentro de acto", 5 vivos, 3 ya deprecados. 3.d (REGIMEN B): 10
primeros vivos alfabeticos anteponen "Solo aplica si vendes o piensas vender
franquicias en Estados Unidos" (forma literal). 3 guardas verdes, PERDIDAS 0.
## Guardas 1.e/1.f/1.h finales
Citas (`SALIDA_V126_1H_CITAS_FINAL.txt`), titulos+autoprueba
(`SALIDA_V126_1H_TITULOS_FINAL.txt`) y sus 2 mutaciones
(`SALIDA_V126_1E_MUT_CITAS.txt`, `SALIDA_V126_1E_MUT_FILA_TABLA.txt`),
cifras del plan (`SALIDA_V126_1H_CIFRAS_FINAL.txt`, 0 pares, 2 filas
examinadas OP-S-09/OP-S-10), todas VERDE EXIT 0.
## PENDIENTE DE DOCTRINA
Aristas huerfanas totales: ejecutor mide 32, contraste del auditor era 39
("no para copiar"), metodo no cotejable sin su codigo; ver ficha.
## DISCUTIBLES MARCADOS PARA RELECTURA CIEGA
1. `--ref c9ac2fb8` en 1.g(ii) no reproduce el ejemplar literal (TAREA 1.g
   arriba); WORK si.
2. 32 vs 39 de aristas huerfanas totales (ver PENDIENTE DE DOCTRINA).
3. Forma de la condicion nueva de 3.d: literal del contramodelo en los 10,
   no adaptada por nodo (discutible ya marcado por el propio encargo).
4. Fase 05 SIGUE ABIERTA: con OP-S-09 HECHA quedan OP-S-10 (16 nodos sin
   tramo), OP-S-11, OP-S-12; no se declara cerrada (adjudica el auditor).
Racha de caidas de reporte: 0 (no toca escalada 1.2). Tope 80: `wc -l` da 80.
