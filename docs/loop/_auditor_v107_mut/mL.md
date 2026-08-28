# REPORTE VUELTA 107 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `9e8017db` (`docs/loop/SALIDA_V107_HEAD_APERTURA.txt`, ANTES de la 1.a operacion), `verificar_apertura_sellada.py --vuelta 107` VERDE EXIT 0 en la apertura (`docs/loop/SALIDA_V107_APERTURA_SELLADA_VERDE.txt`) y re-corrida al cierre sin cambio (`docs/loop/SALIDA_V107_APERTURA_SELLADA_VERDE_CIERRE.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 107` (`docs/loop/SALIDA_V107_CABECERA_TALLADA.txt`), condensada del tallador (3 etiquetas acortadas de 10 filas, ningun valor tocado, confirmado por la guarda de la TAREA 2 abajo):

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| motor | 25/25 | **25/25** |
| marcador del cribado `A` / `B` / `C` / `D`, `n` | 551 / 72 / 5 / 2.760, n 3.388 | **551 / 72 / 5 / 2.760, n 3.388** |
| aristas movidas en la vuelta | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad | rama `pasada-unica`, acta `9e8017db` (asunto real: "ACTA DE LA VUELTA 106 DEL AUDITOR, mas el encargo de la 107."), arboles `dataset/` IGUALES | **HEAD de cierre `a40130ed`** |

sha256 identico en apertura, cierre y HEAD (`f0e3993967457ed2b7a0`, 8.391.653 bytes). `git diff --stat -- dataset/ web/lib/assets/ engine/` VACIO. Nueve mediciones iguales en apertura y cierre. CORRECCION DE ARTEFACTO: `SALIDA_V107_TSC_APERTURA/CIERRE.txt` nacieron con una linea `EXIT=0` anadida por costumbre, que rompia la convencion de fichero vacio == exito; corregidas a vacias antes de tallar (la MEDICION no cambio, tsc siempre dio EXIT 0 sin salida).

**TAREA 3.** Relectura conjunta del discutible 145 (acta 106). CEDO ante el caso del auditor: la madre (`poder_a_traves_de_la_accion`) hace, en su resumen y su paso 3, la MISMA advertencia que el paso 4 del hijo tensiona segun `correccion_v106`; no es material ajeno. Acta 98 3.5 manda sobre este puesto (caveat fuera de la linea casada, referencia mal citada pero doctrina vigente). `correccion_v107` revierte `correccion_v106` sin borrarla: cierre de 73/110 (60,1%) a 74/109 (59,6%). DISCUTIBLE otra vez.

**TAREA 4.** El 109 confirmado SATELITE por grafica ("socios" vive en el complemento instrumental, no en el objeto "el canvas inicial"); lectura entera: el contra-caso gana (paso 6 del hijo PLANEA, no ejecuta; patron 9.6.2 igual que 123/127; paso 5 es entrega de vuelta, patron 2.215). SOSTIENE. Tramo 3 al doble, formato de tres campos (`docs/loop/SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md`): DISCREPANCIA contra el encargo (citaba 18; contadas hoy, tras la reversion del 145, son 19): 18 OBJETO, 1 SATELITE (el propio 109), 0 NO_OBJETO. Cero satelites nuevos ademas del 109.

**TAREA 5, CIERRE DE LA BOLSA.** Recuento propio: DISCREPANCIA de procedimiento (el 148 ya paso por tres vias en la TAREA 4.3; lote vigente DIEZ, no once: 3, 5, 7, 10, 13, 16, 19, 27, 30, 33). Guarda del paso mal casado: los mismos dos (46, 147). Tres vias sobre los diez (`docs/loop/SALIDA_V107_TAREA5_3_TRAMO1_TRES_VIAS.md`): 10 OBJETO, 0 SATELITE. **CIFRA FINAL, LAS DOS DEFINICIONES:** de 74 RESUELTA vivas, 74 pasaron por la pregunta de tres vias (74/74), 0 sin ningun instrumento (0/74). **LA BOLSA QUEDA CERRADA.**

**CIFRA FINAL `OP-E-03`: 74 / 109 (59,6% NO RESUELTA)**, de 73/110 (60,1%) en la apertura.

**TAREA 2 (guarda nueva).** `verificar_cabecera_pegada_o_condensada.py`: coteja la cabecera POR POSICION (no por etiqueta) contra el tallador, distingue PEGADA ENTERA de CONDENSADA, rojo solo si cambia N de filas, alguna cifra no calza, o el reporte miente sobre cual de las dos es. Caso positivo sobre el REPORTE.md real de la 106: CONDENSADA, 8 de 10 filas retecleadas (DISCREPANCIA: el acta dice "9 de 11"; la tabla real de ese reporte tiene 10 filas, no 11) mas ROJO por la promesa falsa de "pegada entera", la caida real. Caso rojo por mutacion (censo alterado a 3.854): la guarda senala esa celda exacta. Corrida sobre la cabecera de ESTE reporte, arriba: ver guardas del cierre.

**TAREA 1.** Registros del acta 106 en `PENDIENTES.md`, 8 subapartados (1.1 a 1.8) como el encargo, composicion tallada 1 nivel2/8 nivel3, cotejo limpio. Insercion pura: 147 lineas anadidas, 0 borradas.

**DISCUTIBLES MARCADOS:** **145** (CEDE, vuelve a DIRECCION AFIRMADA). Ninguna otra.

**PENDIENTES DE PROCEDIMIENTO (no de doctrina):** encargo dice "SIETE mutaciones" pero nombra ocho (A-H); se corrieron las ocho. Cifras de cobertura de tramo3/tramo1 recontadas al dia, no copiadas del encargo (ver TAREA 4 y 5 arriba).

Guardas del cierre, corridas tras la ultima edicion, detalle completo en `docs/loop/SALIDA_V107_GUARDAS_CIERRE_MUTACIONES.txt`: `tallar_nombre_de_operacion.py OP-E-03` VERDE EXIT 0 (`docs/loop/SALIDA_V107_TALLAR_NOMBRE_OP.txt`); `verificar_cabecera_pegada_o_condensada.py --vuelta 107` VERDE (`docs/loop/SALIDA_V107_TAREA2_5_ESTE_REPORTE.txt`); de las ocho mutaciones mas el griton, seis caen y dos mas el griton se sostienen, los nueve calzando con lo publicado en la vuelta 106. `tallar_veredictos_reporte.py` corrido sobre este mismo reporte al final, su propia salida sin autocitarse (para no encerrarse en un espejo) en `docs/loop/SALIDA_V107_GUARDAS_CIERRE.txt`.

`wc -l docs/loop/REPORTE.md` AL CIERRE, tras esta misma edicion, en `docs/loop/SALIDA_V107_WCL_CIERRE.txt`.
