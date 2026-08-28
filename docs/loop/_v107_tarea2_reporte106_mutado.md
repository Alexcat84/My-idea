# REPORTE VUELTA 106 (MODO AUSTERO, tope 80 lineas)

Apertura sellada `fc504151` (`docs/loop/SALIDA_V106_HEAD_APERTURA.txt`, ANTES de la 1.a operacion). PRE-TAREA hallada al sellar: `verificar_apertura_sellada.py --vuelta 106` daba ROJO porque el acta de la vuelta 105 (`fc504151`) titula su commit distinto del patron literal vigente desde la vuelta 92 ("ACTA DE LA VUELTA N DEL AUDITOR"); las dos funciones que leen ese patron (`verificar_apertura_sellada.py`, `tallar_cabecera_reporte.py`) ahora aceptan las dos formas, probado por mutacion (VERDE en 106, ROJO sin cambio en el caso real 100, VERDE sin cambio en 101). Guarda VERDE EXIT 0 (`docs/loop/SALIDA_V106_APERTURA_SELLADA_VERDE.txt`).

**CABECERA, tallada con `tallar_cabecera_reporte.py --fase04 --vuelta 106` (VERDE EXIT 0, `docs/loop/SALIDA_V106_CABECERA_TALLADA.txt`), pegada entera:**

| | apertura | cierre |
|---|---:|---:|
| censo | 3.854/3.188/665 | **3.853/3.188/665** |
| Gate 0 | OK (auto-aristas 0, dup 0, diverg 0) | **OK (auto-aristas 0, dup 0, diverg 0)** |
| aristas | 9.190/9.169/18.359/9.813 | **9.190/9.169/18.359/9.813** |
| motor | 25/25 | **25/25** |
| web | 80(80)/1.030+3 skipped | **80(80)/1.030+3 skipped** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| marcador | A551/B72/C5/D2760, n 3.388 | **A551/B72/C5/D2760, n 3.388** |
| aristas movidas | no aplica | **+0/+0/+0/+0** |
| desfase calibrado | 1 fila (`ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`) | **1 fila (idem)** |
| identidad | rama `pasada-unica`, acta `fc504151` (asunto real leido de git log: "ACTA DEL AUDITOR, VUELTA 105, mas el encargo de la 106..."), arboles `dataset/` coinciden | **HEAD de cierre `d2aa753c`, leido de `SALIDA_V106_HEAD_CIERRE.txt`** |

sha256 identico en apertura, cierre y HEAD. `git diff --stat -- dataset/ web/lib/assets/` VACIO. Nueve mediciones iguales en apertura y cierre.

**TAREA 2 (bloqueante).** `lado_fase04()` leia el marcador legado con el formato viejo tipo diccionario; los cinco regex pasan al formato vigente desde la vuelta 53 (el mismo que ya usaba `lado()`), y `n` se lee de la misma salida de marcador. Caso positivo (V105, A551/B72/C5/D2760) y caso rojo por mutacion (A551 mutado a A999, la celda cambia): VERDE GENERAL, `docs/loop/SALIDA_V106_TAREA2_2_3_CASO_POSITIVO_Y_MUTACION.txt`. La celda de HEAD deja de repetir la de apertura: `leer_head_cierre()` remedia la caida 1.1 del acta 105 (talla la V105 en `275cb46c`, no `ba261321`).

**TAREA 3 (bloqueante).** El ensanche a oraciones siguientes pasa de un solo paso a una CADENA: avanza mientras ninguna oracion traiga veredicto propio, para en la primera que lo traiga. Mutacion E (cita dos oraciones despues, con una neutra de por medio) ahora da ROJO EXIT 1, antes daba EXIT 0 sin hallazgo, `docs/loop/SALIDA_V106_TAREA3_2_MUT_E_ANTES_DESPUES.txt`. Las mutaciones A, B y F, la mutacion D y el reporte 102 (el griton) no cambian de resultado: VERDE GENERAL, `docs/loop/SALIDA_V106_TAREA3_3_LAS_CINCO_QUE_NO_SE_MUEVEN.txt`. Cobertura republicada sin cambio sobre 102, 104 y 105 (3/17, 2/6, 3/8), `docs/loop/SALIDA_V106_TAREA3_5_COBERTURA_REPUBLICADA.txt`.

**TAREA 4.** (4.1) Censo propio del lote de tramos 3+4 (`docs/loop/SALIDA_V106_TAREA4_1_CENSO.txt`): **28 RESUELTA, 27 sin correccion ni relectura, no 26**; DISCREPANCIA declarada contra el encargo (el 147 ya NO es RESUELTA desde `correccion_v99`; el 110 si pertenece y no estaba en la lista del encargo). (4.2) Guarda del paso mal casado en los cuatro tramos: 2 puestos (46, 147), sin cifra viva que tocar. (4.3) Pregunta de tres vias sobre los 27 (`docs/loop/SALIDA_V106_TAREA4_3_TRES_VIAS.txt`): 24 OBJETO, 3 SATELITE (123, 145, 154), 0 NO_OBJETO. (4.4, DISCUTIBLE) Lectura entera a ciegas de los 3 SATELITE (`docs/loop/SALIDA_V106_TAREA4_4_LECTURA_ENTERA.md`): **123 SOSTIENE** (entregables confirman, patron del 2.215); **145 SE MUEVE** (el paso propio del hijo tensiona con la tesis de la madre); **154 SOSTIENE** (el paso casado por si solo contiene entero al hijo). `correccion_v106` en el 145. (4.5) **CIERRE DE LA BOLSA: NO SON TODAS.** Faltan 2, ambos en tramo1 (puestos 3 y 16), fuera del alcance de este encargo.

**CIFRA FINAL `OP-E-03`: 73 / 110 (60,1% NO RESUELTA)**, de 74/109 (59,6%) en la apertura. Recomputo en los tres sitios aditivos tras la correccion.

**TAREA 1.** Registros del acta 105 en `PENDIENTES.md`, 7 subapartados (1.1 a 1.7), composicion tallada 1 nivel2/7 nivel3, cotejo limpio (`docs/loop/SALIDA_V106_TAREA1_COMPOSICION.txt`).

**DISCUTIBLES MARCADOS, para la relectura ciega del auditor:** las DOS direcciones de juicio de esta vuelta: **145** (SE MUEVE, tension con la tesis de la madre) y **154** (SOSTIENE, entregable agregado de la madre distinto del entregable del paso casado). Ninguna otra.

**PENDIENTE, no de doctrina, de cobertura:** los puestos 3 y 16 (tramo1), RESUELTA y nunca releidos por ningun barrido, quedan fuera del alcance de esta vuelta (el encargo pedia solo tramos 3 y 4); van a la siguiente vuelta que cierre tramo1, registrados en `04_ENLACES.md` y `PENDIENTES.md`.

Guardas del cierre, corridas tras la ultima edicion: `tallar_veredictos_reporte.py` sobre este mismo reporte (`docs/loop/SALIDA_V106_GUARDAS_CIERRE.txt`); `tallar_nombre_de_operacion.py OP-E-03` EXIT 0 (`docs/loop/SALIDA_V106_TALLAR_NOMBRE_OP.txt`); `verificar_apertura_sellada.py --vuelta 106` VERDE EXIT 0 (arriba). Tres de tres VERDE.

`wc -l docs/loop/REPORTE.md` AL CIERRE, tras esta misma edicion, en `docs/loop/SALIDA_V106_WCL_CIERRE.txt`.
