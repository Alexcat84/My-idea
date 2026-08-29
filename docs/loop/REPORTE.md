# REPORTE, VUELTA 124

Identidad (git): rama `pasada-unica`, HEAD apertura `6d512a0d` (acta 123, sellado antes de la 1.ª operacion), HEAD cierre `b46e6d92` (`SALIDA_V124_HEAD_CIERRE.txt`). `verificar_apertura_sellada.py --vuelta 124`: VERDE, 8/8 nacidos en el primer commit.

Cabecera tallada (`tallar_cabecera_reporte.py --fase04 --vuelta 124`), pegada entera:

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `6d512a0d` (asunto real leido de git log: 'ACTA DE LA VUELTA 123 DEL AUDITOR: la parada no se dispara, el trabajo del ejecutor aguanta al digito, y las dos caidas de la vuelta son mias.'), HEAD real de apertura `6d512a0d` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `b46e6d92` (leido de `SALIDA_V124_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

Baterias (`SALIDA_V124_BATERIAS_CMP.txt`, `cmp -s`): **IDENTICOS** GATE0_CMD1, CONTEO, TSC, DESFASE_CALIBRADO, MARCADOR. **DISTINTOS** MOTOR y WEB (solo tiempos). Determinismo LEGITIMO: `git diff --numstat -- dataset/ web/ engine/` en CERO toda la vuelta salvo dos reconvergencias del ciclo (ver TAREA 1.c/1.a, caida propia corregida en vivo, igual que la 123); nada se escribio en esos arboles.

**TAREA 1.** 1.e: las dos mutaciones (`docs/loop/SALIDA_V124_TAREA1E_MUTACION_122.txt`, `docs/loop/SALIDA_V124_TAREA1E_MUTACION_123.txt`) siguen cayendo en rojo, sin tocar la guarda. 1.f: `scripts/loop/verificar_cifras_del_plan.py` ensanchado a ventana de 3 frases con normalizacion de `web/` y rojo por ambiguo; `docs/loop/SALIDA_V124_TAREA1F_CASO_POSITIVO.txt` verificado (rojo 99/27 en la copia, VERDE 27==27 en `docs/loop/SALIDA_V124_TAREA1F_VERDE_2727.txt`, rojo 32/27 del caso viejo de la 123 en `docs/loop/SALIDA_V124_TAREA1F_CASO_POSITIVO_VIEJO.txt`). 1.g: `scripts/loop/verificar_titulos_normalizados.py` nuevo, VERDE en `docs/loop/SALIDA_V124_TAREA1G_VERDE.txt` (3.188 vivos, 0 exactos, 1 normalizado, igual a la medicion del auditor sin copiarla), autoprueba de mutacion en rojo verificada en `docs/loop/SALIDA_V124_TAREA1G_AUTOPRUEBA.txt`, excepcion unica declarada (`sistema_responsabilidad_gerencial`/`_2`).

**TAREA 2.** 2.a: nota de OP-S-09 corregida (39 consecutivos vs 51 totales del racimo, caida del auditor acta123 4.2); numstat 1/1, word-diff porcelain solo borra la comilla vieja (remision pura). 2.b: `PENDIENTES.md` R.6, las tres caidas de la 123 (dos del auditor, una del ejecutor). 2.c: ficha `campos-sucios-dataset`, SEPTIMA entrada, punto ciego de titulos. `PENDIENTES.md` numstat total 106/0, cero borrados.

**TAREA 3.a, EL SUELO: CUMPLIDO.** 51/51 pares del racimo leidos y registrados (`vuelta124_verificar_51_pares_completos.py`, VERDE). Los 12 que faltaban (`SALIDA_V124_OPS09_LECTURA_RESTO.jsonl`): 11 CONTINUA, 1 REPITE (`estrategia_de_innovacion_de_producto`<->`estrategia_innovacion_producto`, superviviente el primero) que DISCREPA del aviso del auditor (contenido empatado, no lo salva la fase distinta).

**TAREA 3.b, NO CABE ESTA VUELTA: ENTREGA COMPLETA, no limite de alcance** (letra del encargo). Guardas de escritura consumidas: CERO, ningun instrumento toco `dataset/`. **DISCUTIBLE MAYOR:** la `verificacion` de OP-S-09 exige "ningun id vivo lleva sufijo numerico de duplicado", lo que implica RENOMBRAR ~61 nodos vivos ademas de las 3 fusiones REPITE ya leidas y registradas en `SALIDA_V123_OPS09_LECTURA.jsonl` y `SALIDA_V124_OPS09_LECTURA_RESTO.jsonl` (`eliminacion_causas_error` a `_4`, `dia_cero_defectos_3` a `_2`, y la pareja del marco de producto leida hoy). Elegir el id nuevo de cada uno es juicio editorial sin regla escrita que lo derive mecanicamente (EJECUTOR.md regla 11, no adivinar). Paso el par a la 125 con este caso escrito: se ejecuta con una regla de nomenclatura explicita del auditor, o el auditor confirma que el alcance de "renombre" es otro.

**TAREA 3.c: NO CORRE.** Condicionada a que OP-S-09 cierre entera; no cerro.

`tallar_cabecera_reporte.py --fase04 --vuelta 124 --comparar docs/loop/REPORTE.md`: pendiente de correr tras este commit (se cita en el commit). `verificar_citas_del_reporte.py`, `verificar_cifras_del_plan.py`, `verificar_titulos_normalizados.py`: VERDE los tres (salidas arriba).

`wc -l docs/loop/REPORTE.md`: **34**, dentro del tope de 80 del austero.
