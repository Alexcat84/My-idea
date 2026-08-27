# REPORTE DE LA VUELTA 87 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 86. Apertura sellada ANTES de la primera operacion en
`docs/loop/SALIDA_V87_HEAD_APERTURA.txt`: `fe24bd71` (el acta de la vuelta 86).
Cierre recomputado AL CIERRE, con las suites y el grafo tal como quedan tras
escribir el tramo 12 (la cola de `OP-E-01`).

## CABECERA TALLADA (--fase04 --vuelta 87), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 87`
Salida completa en `docs/loop/_v87_cabecera_tallada.txt`, EXIT 0.

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.994 / 8.973 / 17.967 / 9.617 | **8.996 / 8.975 / 17.971 / 9.619** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+2 / +2 / +4 / +2** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 8 fila(s): `determinacion_cuota_inicial -> analisis_competencia_franquicias`, `remover_barreras_orgullo_trabajo -> eliminar_slogans_y_exhortaciones`, `distribucion_poisson -> muestreo_de_aceptacion`, `personalizar_interacciones_cliente -> conexion_personal_emocional`, `customer_discovery_phase2_problem_test -> preparar_contacto_clientes`, `definicion_calidad_fitness_for_purpose -> descubrir_necesidades_del_cliente`, `definicion_y_concepto_de_aseguramiento_de_calidad -> trilogia_juran_qa_qc`, `motor_crecimiento_pago -> valor_de_vida_del_cliente` | **2 fila(s): `juran_rcca_metodo -> diseno_implementacion_remedio`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `fe24bd71` (ACTA DE LA VUELTA 86 DEL AUDITOR, leido de git log), HEAD real de apertura `fe24bd71` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `fe24bd71` (ACTA DE LA VUELTA 86 DEL AUDITOR, leido de git log), HEAD real de apertura `fe24bd71` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

El desfase de la apertura (8 filas) son las ocho aristas que la vuelta 86
escribio, medidas contra la bolsa recalibrada de ESA vuelta; al recalibrar de
cero esta vuelta (TAREA 3, `SALIDA_V87_RECALIBRADO.txt`) esas ocho quedan
reflejadas en el calibrado y el desfase cae a cero por ese lado. Las DOS filas
del desfase de cierre son las dos aristas que ESTA vuelta escribio (tramo 12),
que la recalibracion de esta vuelta no pudo prever porque corrio ANTES de
escribirlas: es exactamente el patron declarado correcto por la adjudicacion
5.7 del acta 82 (el fichero se commitea "tal como quedo" tras una escritura
posterior a su propia recalibracion).

El ciclo de tres (Gate 0, `etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`)
se corrio dos veces seguidas tras escribir las dos aristas del tramo 12, y el
`master_graph.json` resultante da el MISMO hash sha256 las dos veces
(`6ea239641964f43a76d179721f6e5fc40b0422bf5e1ea3785fd2ee3987f2cd9f`): el ciclo
es estable sobre el arbol de hoy.

## 1. TAREA 1, los registros de la vuelta 86, sin remedirlos

**(1.1) El incumplimiento de encargo de la vuelta 86 queda registrado con su
nombre**, sin volver a medirlo (viene medido en el acta 86, seccion 4.1): el
horneado PRE FILTRO no se corrio esa vuelta, y el repaso punto por punto de
esa vuelta contesto "SI" a un punto que se corrio una sola vez. Dano medido
por el auditor: NINGUNO (las 186 filas de la apertura de la vuelta 86 eran
prefijo exacto de las 216 de esa misma vuelta). No tiene racha ni parada
asociada en `AUDITOR.md` seccion 4, y no me la invento: queda contada como el
primer incumplimiento de encargo de la campana (la cuenta se estrena en el
acta 86).

**(1.2) Las tres rachas quedan asi, sin remedirlas** (acta 86, seccion 7):
- **CLASE O CIFRA PUBLICADA: CERO** desde la vuelta 78. Van **nueve vueltas
  limpias** (78 a 86) de estas dos especies. La parada pide DOS SEGUIDAS: no
  se dispara.
- **REPORTE: CERO**, rota en la vuelta 86 (venia de DOS y quedaba a una de la
  parada). La parada vuelve a pedir TRES desde cero.
- **CREDITO DE TANDA: RESTAURADO** (adjudicacion 5.5 del acta 86): la rebaja
  de la vuelta 85 se levanta porque la 86 no tuvo caida de ninguna de las tres
  especies. Consecuencia escrita por el auditor: en esta vuelta 87 no estoy
  obligado a releer al doble, y aun asi las cuatro unidades de la cola se
  releyeron las cuatro (numero chico, no es la regla actuando).

**(1.3) Las diez adjudicaciones de la seccion 5 del acta 86 (5.1 a 5.10),
registradas por su numero, sin remedirlas:**
- **5.1** Las ocho aristas de la vuelta 86 y las treinta lecturas del tramo 11
  se ratifican: nada que corregir en el grafo.
- **5.2** El horneado se fija por escrito: desde esta vuelta 87, "hornear dos
  veces" significa DOS CORRIDAS DENTRO DE LA MISMA VUELTA, cada una con su
  fichero propio. Ejecutada en la TAREA 2.b de esta vuelta.
- **5.3** La cuenta de unidades nuevas por recalibracion pasa a ser una celda
  tallada por el filtro. Ejecutada en la TAREA 2.a de esta vuelta.
- **5.4** La marca de discutible sigue siendo senal del ejecutor y se pide mas
  suelta todavia (con la unidad 120 de la vuelta 86 nombrada como ejemplo de
  lo que se marca). No es doctrina nueva, es descriptiva: cuando la razon del
  NO sea la DIRECCION y no la literalidad, y el paso nombre el sustantivo del
  hijo, la marca corresponde.
- **5.5** El credito de tanda se restaura (ver 1.2 arriba).
- **5.6** El caveat del paso vecino queda anotado y no adjudicado: no
  ensancharlo esta vuelta, es trabajo nuevo que no bloquea nada.
- **5.7** Lo que sigue sin escribirse (octava acta consecutiva, ver TAREA 3
  mas abajo, siguen fuera de la bolsa).
- **5.8** `OP-E-01` se consume en esta vuelta 87 y su cierre se mide, no se
  anuncia. Ejecutado en las TAREAS 3 y 4 de esta vuelta.
- **5.9** Lo que viene despues de `OP-E-01` se mide antes de tocarlo, y no se
  teclea. Ejecutado en la TAREA 5 de esta vuelta.
- **5.10** El campo `estado` de `OPERACIONES.jsonl` NO MIDE NADA desde el 15
  ago 2026 (00_INDICE.md linea 111): la vara buena es el campo `nota` mas las
  paginas de fase. Aplicado en la TAREA 5.

## 2. TAREA 2, EL INSTRUMENTO (BLOQUEANTE), commit `c3642f7f`

Las dos piezas, commiteadas y pusheadas ANTES del filtro de la cola de
`OP-E-01`.

**(2.a) La cuenta de unidades nuevas por recalibracion pasa a ser una celda
tallada** (`scripts/loop/vuelta87_unidades_nuevas_recalibracion.py`, wireado
en `scripts/loop/vuelta87_tramo12_filtrar.py`): compara la bolsa filtrada de
HOY contra la de la vuelta ANTERIOR y cuenta cuantos pares (madre, hijo) de la
bolsa de hoy no estaban en la anterior, nombrandolos si son pocos (10 o
menos). Casos obligatorios, los dos corridos:
- **VERDE**, caso obligatorio del encargo: `PASO_NODO_CALIBRADO_FILTRADO_
  V86.jsonl` (129 filas) contra `PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl` (136
  filas) da **CERO nuevas**
  (`docs/loop/SALIDA_V87_CASO_2A_VERDE_UNIDADES_NUEVAS.txt`), identico a lo
  que el auditor midio a mano en `docs/loop/_auditor_v86_nuevas_por_vuelta.txt`.
- **ROJO inventado**, sobre una COPIA de la bolsa V86 con una fila falsa
  anadida (`docs/loop/_v87_copia_bolsa_rojo_inventado.jsonl`, NUNCA los
  ficheros reales): **1 nueva**, nombrada
  (`docs/loop/SALIDA_V87_CASO_2A_ROJO_UNIDADES_NUEVAS.txt`). Prueba que la
  celda no esta clavada en cero.

Wireada en el filtro del tramo 12 de esta misma vuelta: **0 unidades nuevas**
en la bolsa filtrada V87 (121 filas) respecto de la V86 (129 filas), medido
en la corrida real (TAREA 3 mas abajo).

**(2.b) El horneado PRE FILTRO vuelve, con su fichero propio**
(`scripts/loop/vuelta85_hornear_decididas.py`, sin cambio de maquina, solo de
CUANDO corre): corrido ANTES del filtro de esta vuelta, salida en
`docs/loop/SALIDA_V87_HORNEAR_PRE_FILTRO.txt`: **216 filas (97 ESCRITA, 119
NO SE ENLAZA)**, **8 ascendidas y 4 degradadas**, identico a la vara de
contraste que el auditor midio hoy (acta 86). NO MUEVE NINGUN DATO:
`git status --porcelain -- docs/plan/OP_E_01_DECIDIDAS.jsonl` dio cero lineas
tras esta corrida. Corrido otra vez AL CIERRE, DESPUES de escribir el tramo
12 (`docs/loop/SALIDA_V87_HORNEAR_CIERRE.txt`), ver seccion 5 mas abajo.

Sello del HEAD de apertura antes de la primera operacion:
`docs/loop/SALIDA_V87_HEAD_APERTURA.txt` = `fe24bd71` (acta de la vuelta 86).

## 3. TAREA 3, la cola de `OP-E-01` (tramo 12), leida POR LO NO DECIDIDO

**Bolsa recalibrada FRESCA** antes de leer: `python scripts/plan/paso_contra_
nodo_calibrado.py --umbral-titulo 72 --umbral-contencion 0.45 --min-tokens 4`
(`docs/loop/SALIDA_V87_RECALIBRADO.txt`), bolsa reducida 468 filas, 213 sin
arista (221 menos las 8 aristas que la vuelta 86 escribio).

**Filtro P.9.1 ensanchado + guarda del par no dirigido + vara de la cadena +
aviso del paso vecino + celda tallada de unidades nuevas (TAREA 2.a)**
corridos ANTES de leer nada (`scripts/loop/vuelta87_tramo12_filtrar.py` >
`docs/loop/SALIDA_V87_TRAMO12_FILTRO_P91_GUARDA_CADENA.txt`): 213 candidatos
sin arista, 92 apartados por P.9.1 ensanchado (35 solo por operacion, 57 con
motivo de la vara de los A), 121 limpios tras el filtro, 0 parejas del par no
dirigido, 121 unidades de lectura, escrito
`docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V87.jsonl` (121 filas). **UNIDADES
NUEVAS RESPECTO DE LA BOLSA V86: CERO** (celda tallada, TAREA 2.a).

Registro de decididas leido (horneado PRE FILTRO de esta vuelta): 119 pares
`NO SE ENLAZA`. **117 unidades ya decididas en la cabeza, saltadas** (no se
releen ni se re-derivan sus razones); **primera unidad SIN DECIDIR el indice
117**, `juran_rcca_metodo -> diseno_implementacion_remedio` (paso 3, quality);
**4 frescas** (indices 117 a 120); **0 unidades sin decidir restantes tras
esta cabeza**: es la cola entera de `OP-E-01`.

**Las cuatro varas de contraste que el encargo publico salen las CUATRO
EXACTAS**: bolsa filtrada 121, prefijo de decididas que sobrevive 117,
primera sin decidir el indice 117 (`juran_rcca_metodo ->
diseno_implementacion_remedio`, paso 3, quality), y las cuatro sin decidir
nombradas identicas a las del encargo. Cero discrepancias que declarar.

Las 8 fichas (madre e hijo de las 4 unidades) se volcaron ENTERAS antes de
leer (`docs/loop/_v87_volcado_tramo12.txt`, instrumento
`scripts/loop/_v87_volcar_tramo12.py`). Credito de tanda RESTAURADO
(adjudicacion 5.5 del acta 86): no estoy obligado a releer al doble, y aun
asi se leyeron las 4 ENTERAS, porque cuatro es un numero chico.

### Las 4 lecturas, con razon y discutibles marcados ANTES de saber si aciertan

La columna "cadena" es la tallada de `docs/loop/tallar_cabecera_reporte.py
--vuelta 87 --tramo-cadena 12` (seccion siguiente); no decide nada por si
sola (banco 9.6.1, caveat de la familia encadenada). La columna "es la
cadena propia de la madre" es una decision de LECTURA (adjudicacion 6.1 del
acta 83, no de longitud): para cada unidad ALCANZABLE, si el camino recorre
los propios pasos enumerados de la madre, en su propio orden.

| # | par (paso) | cadena | es la cadena propia de la madre | decision | DISCUTIBLE | razon |
|---:|---|---|---|---|:---:|---|
| 117 | `juran_rcca_metodo -> diseno_implementacion_remedio` (paso 3, quality) | ALCANZABLE (6 saltos): `juran_rcca_metodo -> definicion_problema_moms_2 -> analisis_sintomas -> formulacion_teorias_causa -> prueba_teorias_causa_raiz -> evaluacion_alternativas_solucion -> diseno_implementacion_remedio` | **SI**: arranca del hijo del paso 1 de la madre (`definicion_problema_moms_2`) y AVANZA en orden creciente por sus propios pasos 2 (analizar y diagnosticar: sintomas, teorias, prueba) y 3 (mejorar: evaluar alternativas, disenar el remedio) del metodo RCCA | **SE ESCRIBE** | SI | El paso 3 ("Mejorar: disenar e implementar el remedio") nombra literal el titulo entero del hijo ("Diseno e Implementacion del Remedio"). La madre conserva material propio (pasos 1, 2 y 4: definir el problema, analizar y diagnosticar, controlar) que el hijo no toca. DISCUTIBLE: la madre ya enlaza a `viaje_diagnostico_remedial`, un nodo hermano que tambien describe a nivel general el diseno de remedios (uno de sus 8 pasos es "Disenar remedios para eliminar las causas"); por 9.6.3 el tamano del solape no decide por si solo, se pesa el resto, y el resto de cada nodo es distinto (el hermano es la metodologia dual completa, el hijo es el procedimiento detallado de 6 pasos para UN remedio ya elegido). |
| 118 | `valor_intangible_sostenibilidad -> alineacion_engagement_estrategia_general` (paso 1, environmental) | SIN CAMINO PREVIO | (no aplica, sin camino) | NO SE ENLAZA | SI | El paso 1 de la madre ("incorpora metricas de sostenibilidad en tu seguimiento del negocio") es sobre INCORPORAR METRICAS de medicion; el hijo es una lista de verificacion de liderazgo (10 recomendaciones, 4 pasos volcados: verificar coherencia, mostrar con hechos, elegir lideres con credibilidad, dar seguimiento) para ALINEAR el compromiso del equipo, una actividad distinta. DISCUTIBLE: el paso 3 de la misma madre ("alinea tu cultura de trabajo y proposito de sostenibilidad con la marca que quieres proyectar como empleador") se acerca mas en tema que el paso 1 que el calibrado trajo, sin que ninguno de los dos desarrolle el procedimiento completo del hijo; el aviso automatico del paso vecino (TAREA 2.d de la vuelta 86) no disparo para esta unidad. |
| 119 | `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` (paso 4, core) | ALCANZABLE (5 saltos): `ganar_comprension_del_cliente -> actualizar_modelo_de_negocio_pivot_o_proceed -> leap_of_faith_assumptions -> genchi_gembutsu_salir_del_edificio -> arquetipos_de_cliente -> dia_en_la_vida_del_cliente` | **NO**: el primer salto (`actualizar_modelo_de_negocio_pivot_o_proceed`) no corresponde a ninguno de los 6 pasos enumerados de la madre, y el camino transita por temas de Customer Development (hipotesis de fe, salir del edificio, arquetipos) ajenos a esos pasos | **SE ESCRIBE** | | El paso 4 de la madre ("Pasa un dia haciendo lo que hace tu cliente... y asiste a sus eventos") nombra literal el titulo entero del hijo ("Un Dia en la Vida del Cliente"). La madre conserva material propio (pasos 1, 2, 3, 5 y 6: investigar flujo de trabajo, preguntar por otras soluciones, explorar que cambiaria el comportamiento de compra, identificar publicaciones, documentar hallazgos) que el hijo no toca. |
| 120 | `no_shop_agreement -> dividends_terms` (paso 2, core) | ALCANZABLE (4 saltos): `no_shop_agreement -> term_sheet_negociacion -> conversion_rights -> automatic_conversion -> dividends_terms` | **NO**: transita por un nodo hub generico de negociacion del term sheet y clausulas de conversion, ajenas a los 4 pasos propios de `no_shop_agreement` (definir plazo, bindingness, obligacion de aviso, que pasa si no cierra) | NO SE ENLAZA | | El paso 2 de la madre ("esta clausula es vinculante desde que firmas el term sheet") es sobre la BINDINGNESS de la exclusividad; el hijo es sobre clausulas de DIVIDENDOS (acumulativo o no, aprobacion del consejo, pago en efectivo o acciones), sin relacion de contenido. Colision de dominio: las dos son clausulas de term sheet de financiamiento, y nada mas. |

**RESUMEN DE LA TANDA: 2 de 4 SE ESCRIBE, 2 de 4 NO SE ENLAZA, 2
DISCUTIBLES** (117, 118), contado de `docs/loop/SALIDA_V87_TRAMO12_
ESCRIBIR.txt`.

Aristas escritas esta tanda (`scripts/loop/vuelta87_tramo12_escribir.py`,
verificadas con `scripts/loop/vuelta87_medir_tramo12.py` >
`docs/loop/SALIDA_V87_TRAMO12_ESCRIBIR.txt`): **2 ARISTAS ESCRITAS, 0
ESCALERA ROTA, 0 INCONSISTENTES**, las dos presentes en las DOS vistas
(`nodos_siguientes` de la madre Y `nodos_previos` del hijo), sin inversas.

### La tabla de alcanzabilidad (vara de la cadena) del tramo 12

Comando: `python scripts/loop/tallar_cabecera_reporte.py --vuelta 87 --tramo-cadena 12`.
Salida completa en `docs/loop/_v87_tabla_cadena_tramo12.txt`, EXIT 0.

| # | par (paso) | alcanzable previo (vara de la cadena) |
|---:|---|---|
| 117 | `juran_rcca_metodo -> diseno_implementacion_remedio (paso 3)` | ALCANZABLE (6 saltos) |
| 118 | `valor_intangible_sostenibilidad -> alineacion_engagement_estrategia_general (paso 1)` | SIN CAMINO PREVIO |
| 119 | `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente (paso 4)` | ALCANZABLE (5 saltos) |
| 120 | `no_shop_agreement -> dividends_terms (paso 2)` | ALCANZABLE (4 saltos) |

## 4. TAREA 4, la vara del tramo 12 y el cierre medido de `OP-E-01`

Comando: `python scripts/loop/vuelta87_tarea4_vara_tramo12.py` >
`docs/loop/SALIDA_V87_TAREA4_VARA_TRAMO12.txt`. Pares LEIDOS del fichero del
filtro, no tecleados. Alcance de la adjudicacion 6.5 del acta 84: (4.a) las 4
frescas contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SIN direccion; (4.b) las
mismas contra `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl` buscando la
reciproca; (4.c) la tabla del PATRON HISTORICO, pegada entera.

Cifras que el acta 86 publico como medidas hoy por el auditor, confirmadas al
digito: **3.388 veredictos, 3.388 pares no dirigidos unicos, 129 unidades en
la bolsa filtrada V86.** Sin discrepancia.

**RESUMEN 4.a/4.b: 1 de 4 con veredicto (119, clase D, puesto 1.358, core), 0
de 4 con reciproca contra la bolsa filtrada V86.** La unidad 119 se decidio
ESCRITA esta tanda (dato de esta tanda, sin compararlo contra ninguna otra:
adjudicacion 5.5 del acta 85, seccion "LO QUE NO SE ESCRIBE" mas abajo).

**(4.c) La tabla del PATRON HISTORICO, pegada entera de
`docs/loop/SALIDA_V87_TAREA4_VARA_TRAMO12.txt`:**

| tramo | par | clase | puesto | dominio | decision (registro de hoy) |
|---:|---|:---:|---:|---|---|
| 3 | `fees_y_breakup_fee_adquisicion -> breakup_fee_evaluation` | D | 223 | core | ESCRITA |
| 3 | `analisis_de_ratios_financieros -> retorno_sobre_capital` | D | 1369 | core | ESCRITA |
| 3 | `identificar_si_tu_producto_necesita_proteccion_especial -> probar_empaque_antes_de_escalar_envios` | D | 1746 | entrega | ESCRITA |
| 3 | `control_exportaciones_bis -> licencia_exportacion_regulaciones` | D | 1951 | exportacion | ESCRITA |
| 3 | `cero_defectos -> zero_defects_concepto` | D | 2464 | quality | ESCRITA |
| 3 | `mejora_calidad_crosby -> programa_mejora_calidad_14_pasos` | D | 2583 | quality | ESCRITA |
| 3 | `estadistica_basica_calidad -> medidas_tendencia_dispersion` | D | 2826 | quality | ESCRITA |
| 4 | `equipo_customer_development -> customer_development_team` | B | 637 | core | NO SE ENLAZA |
| 4 | `sujetos_de_control -> key_process_product_characteristics` | D | 3205 | quality | ESCRITA |
| 5 | `mvp_catalogo_tecnicas -> mvp_tipo_video` | D | 384 | core | NO SE ENLAZA |
| 5 | `posicionamiento_vs_competidores -> analisis_competencia_franquicias` | D | 2097 | franquicias | NO SE ENLAZA |
| 5 | `identificacion_evaluacion_peligros -> investigacion_incidentes` | D | 2324 | health_safety | ESCRITA |
| 6 | `abolir_inspeccion_masiva -> eliminacion_inspeccion_masiva_por_control_estadistico` | D | 2560 | quality | NO SE ENLAZA |
| 7 | `estructura_reporte_dual_estadistico -> organizacion_liderazgo_estadistico` | D | 3121 | quality | NO SE ENLAZA |
| 8 | `term_sheet_negociacion -> entender_term_sheet` | D | 554 | core | NO SE ENLAZA |
| 8 | `clasificacion_caracteristicas_calidad -> key_process_product_characteristics` | D | 2959 | quality | NO SE ENLAZA |
| 9 | `formulacion_teorias_causa -> diagrama_causa_efecto` | D | 2980 | quality | ESCRITA |
| 9 | `control_calidad_definicion -> plan_de_control` | D | 3056 | quality | NO SE ENLAZA |
| 10 | `customer_discovery_phase2_problem_test -> ganar_comprension_del_cliente` | D | 1397 | core | NO SE ENLAZA |
| 10 | `estructura_equipos_innovacion_interna -> equipo_multifuncional_real` | D | 1401 | core | ESCRITA |
| 10 | `diagrama_de_flujo_proceso_map -> analisis_flujo_proceso` | D | 2728 | quality | ESCRITA |
| 11 | `personalizar_interacciones_cliente -> conexion_personal_emocional` | D | 1396 | core | ESCRITA |
| 11 | `definicion_y_concepto_de_aseguramiento_de_calidad -> trilogia_juran_qa_qc` | D | 2765 | quality | ESCRITA |
| 11 | `remover_barreras_orgullo_trabajo -> eliminar_slogans_y_exhortaciones` | D | 3174 | quality | ESCRITA |
| 11 | `sistema_pull_push -> takt_time` | D | 3231 | quality | NO SE ENLAZA |
| 12 | `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | D | 1358 | core | ESCRITA |

**RESUMEN POR TRAMO, tallado (pares con veredicto | clase D | ESCRITA | NO SE
ENLAZA):** tramo 3: 7\|7\|7\|0. Tramo 4: 2\|1\|1\|1. Tramo 5: 3\|3\|1\|2.
Tramo 6: 1\|1\|0\|1. Tramo 7: 1\|1\|0\|1. Tramo 8: 2\|2\|0\|2. Tramo 9: 2\|2\|1\|1.
Tramo 10: 3\|3\|2\|1. Tramo 11: 4\|4\|3\|1. **Tramo 12: 1\|1\|1\|0.**

**CASO OBLIGATORIO confirmado**: `formulacion_teorias_causa ->
diagrama_causa_efecto` (tramo 9, clase D) sale ESCRITA, igual que en la vuelta
86.

### 4.d EL CIERRE MEDIDO DE `OP-E-01` (adjudicacion 5.8 del acta 86)

No se anuncia: se talla.

**La cifra final de la operacion**, leida de `docs/plan/OP_E_01_DECIDIDAS.jsonl`
(nunca de la suma de reportes viejos): **220 unidades leidas en total, 99
ESCRITA, 121 NO SE ENLAZA**, reparto por tramo `{3: 30, 4: 30, 5: 23, 6: 10,
7: 3, 8: 30, 9: 30, 10: 30, 11: 30, 12: 4}`.

**La guarda, corrida DESPUES del horneado de cierre** (ver seccion 5 mas
abajo), con la bolsa filtrada V87
(`scripts/loop/vuelta83_guarda_decididas.py --bolsa docs/plan/PASO_NODO_
CALIBRADO_FILTRADO_V87.jsonl`, `docs/loop/SALIDA_V87_GUARDA_CIERRE.txt`):
**VERDE**, con el mensaje **TODA LA BOLSA ESTA DECIDIDA**, sobre las 121
unidades de la bolsa filtrada V87. Ninguna unidad queda sin decision.

**El cierre se declara COMO MANDA EL 00_INDICE LINEA 111**: el campo `estado`
de `OPERACIONES.jsonl` NO SE TOCA (`OP-E-01` sigue en `LISTA`), la ejecucion
se declara en el campo `nota` de `OP-E-01` con esta misma cifra dentro, y el
cierre se escribe en `docs/plan/04_ENLACES.md`, apartado nuevo `## OP-E-01,
CIERRE MEDIDO (27 ago 2026, vuelta 87)`, con la misma cifra.

**`OP-E-01` CIERRA SIN BOLSA A MEDIAS.**

## LO QUE NO SE ESCRIBE EN PROSA ESTA VUELTA (adjudicacion 5.5 del acta 85)

Ninguna frase de esta vuelta compara el tramo 12 contra "el promedio de
tramos anteriores" ni expresiones parecidas sin el fichero que la sostenga.
La unica comparacion entre tandas que esta vuelta publica es la que la celda
tallada de la TAREA 2.a produce (0 unidades nuevas respecto de la V86), y
viene con su fichero citado al lado.

## 5. El horneado de cierre y la guarda, DESPUES de escribir el tramo 12

Registro horneado DOS VECES DENTRO DE ESTA MISMA VUELTA (adjudicacion 5.2 del
acta 86, la definicion que queda fijada desde hoy): PRE FILTRO (seccion 2
arriba, `docs/loop/SALIDA_V87_HORNEAR_PRE_FILTRO.txt`, 216 filas) y AL CIERRE,
DESPUES de escribir el tramo 12
(`docs/loop/SALIDA_V87_HORNEAR_CIERRE.txt`, `python scripts/loop/
vuelta85_hornear_decididas.py`, maquina sin cambios, descubre por patron):
**220 filas (99 ESCRITA, 121 NO SE ENLAZA)**, **8 ascendidas y 4 degradadas**,
las mismas de siempre: el tramo 12 no ascendio ni degrado ninguna fila
historica.

Guarda corrida DESPUES de este segundo horneado, con la bolsa filtrada V87:
**VERDE, TODA LA BOLSA ESTA DECIDIDA** (ver 4.d arriba). Es la primera vez
que la guarda imprime ese mensaje en vez de nombrar la cabeza del tramo
siguiente: no hay tramo siguiente, `OP-E-01` se acabo.

## TAREA 5, LO QUE VIENE DESPUES, TALLADO Y NO TECLEADO (adjudicaciones 5.9 y 5.10)

Instrumento propio: `scripts/loop/vuelta87_tarea5_desbloqueo_fase04.py` >
`docs/loop/SALIDA_V87_TAREA5_DESBLOQUEO_FASE04.txt`, EXIT 0. El criterio para
leer "EJECUTADA" esta escrito completo en el docstring del script (no se
resume aqui para no parafrasearlo, banco 9.5.0): en corto, marcas negativas
por PROXIMIDAD LITERAL a cada mencion del id en la pagina de fase (nunca la
seccion entera, que puede hablar de otra cosa a mitad de camino) mas marcas
positivas dentro de las secciones que nombran al id (cabecera CERRADA,
SELLADA o CIERRE; la frase `REGISTRO DE OPERACION HECHA`; o un registro de
fusion con censo antes/despues medido). El campo `estado` de
`OPERACIONES.jsonl` NUNCA se lee (adjudicacion 5.10 del acta 86: ese campo no
mide nada desde el 15 ago 2026).

**LA TABLA, pegada entera:**

| id_op | orden | depende_de | DESBLOQUEADA |
|---|---:|---|---|
| `OP-E-01` | 1 | (ninguna) | SI (sin dependencias; esta misma vuelta la cierra) |
| `OP-E-02` | 2 | (ninguna) | SI (sin dependencias; ya HECHA desde antes) |
| `OP-E-03` | 3 | `OP-E-01`, `OP-U-02` | **NO** (`OP-U-02` pendiente del cierre del cribado) |
| `OP-M-03-ENLACES` | 4 | `OP-M-03-I`, `OP-M-03-II`, `OP-M-03-III` | **NO** (`OP-M-03-III` enrutada a la fase 06) |
| `OP-E-04` | 5 | `OP-M-01`, `OP-M-01-FUSION` | **NO** (`OP-M-01` DECISION PENDIENTE; `OP-M-01-FUSION` enrutada a la fase 06) |
| `OP-E-05` | 6 | `OP-M-01`, `OP-M-01-FUSION` | **NO** (idem) |
| `OP-M-01-ESLABONES` | 7 | `OP-M-01`, `OP-M-01-FUSION` | **NO** (idem) |
| `OP-M-01-SEXTO` | 8 | `OP-M-01`, `OP-M-01-FUSION` | **NO** (idem) |
| **`OP-E-06`** | **9** | `OP-D-01` a `OP-D-07` | **SI**: las siete dependencias estan las siete EJECUTADAS |
| `OP-E-07` | 10 | `OP-E-06` | NO SE PUEDE DECIR (`OP-E-06` no se ha ejecutado todavia: ni cerrada ni declarada pendiente, simplemente no ha corrido) |

**`OP-E-06` (orden 9) es la UNICA operacion de la fase 04 que queda
desbloqueada ademas de `OP-E-01`**, confirmando por medicion (no por la vara
cruda del acta 86) lo que el auditor sospechaba. Las siete dependencias
(`OP-D-01` a `OP-D-07`) estan cerradas segun `docs/plan/02_DESTEJIDOS.md`
linea 4470 ("EL CIERRE DE LA FASE 02, DECLARADO MIDIENDO"), que las lista las
nueve (incluidas `OP-D-08` y `OP-D-09`, fuera del `depende_de` de `OP-E-06`)
con su registro de cierre citado por linea.

**DOS FALSOS NEGATIVOS DEL INSTRUMENTO EN SU PRIMERA CORRIDA, citados y
corregidos, sin callarlos** (ver el docstring del script para el detalle
completo): (a) `OP-M-03-I`, `OP-M-03-II` y `OP-M-01-FUSION` salian NO
EJECUTADA porque la cabecera de apertura de `03_FUSIONES.md` se leia entera
para cualquier id de esa pagina, y esa cabecera declara a OTRA operacion
(`OP-U-02`) "pendiente del cierre del cribado"; se corrigio restringiendo la
cabecera de apertura a los casos en que de verdad nombra al id que se esta
midiendo. (b) `OP-D-01` seguia saliendo NO EJECUTADA por una frase sobre un
umbral sin relacion (`MIN_BLOQUE`) que comparte oracion con una mencion de
`OP-D-01` en `02_DESTEJIDOS.md` linea 3580; este caso persistio tras el
arreglo de (a) porque la proximidad literal (220 caracteres) todavia alcanza
esa oracion multiclausula, y queda **CORREGIDO A MANO Y CITADO** en el propio
script (`CORRECCIONES_MANUALES`), contra la fuente autoritativa de la linea
4470 arriba citada.

**NO SE ABRE `OP-E-06` ESTA VUELTA.** Se leyo su texto entero
(`docs/plan/OPERACIONES.jsonl`, campos `verificacion`, `evidencia`,
`adjudicacion` y `nota`) para contestar la pregunta del encargo: **su texto
NO ALCANZA para ejecutarse sin decidir.** Motivos, medidos:

1. La evidencia citada (`docs/plan/COSECHA_RAZONES_D.jsonl`, 397 filas,
   generado por `scripts/plan/barrido_razones_d.py`) guarda `nodo_a` y
   `nodo_b` **sin direccion resuelta** (cual es madre, cual es hijo): el
   campo `senales` solo marca que PATRON de la razon disparo (por ejemplo
   "madre e hijo"), no cual nodo es cual. Verificado leyendo el codigo del
   script (`scripts/plan/barrido_razones_d.py`, funcion `main()`): no calcula
   ni imprime ninguna cifra de "192 con direccion explicita", que es la que
   la ficha de `OP-E-06` cita como la parte ejecutable. Esa cifra no se puede
   reproducir con lo que hay en el repositorio hoy.
2. Aunque se reprodujera, resolver la direccion de cada una de las 293 filas
   "nuevas" exige LEER la `frase` de cada razon (prosa) y decidir cual nodo
   se llama madre y cual hijo: es el mismo tipo de trabajo de lectura que
   `OP-E-01` hizo par a par en sus doce tramos, no una operacion mecanica.
3. La evidencia tiene fecha de corte **12 ago 2026**, mas de setenta vueltas
   de antiguedad: el grafo se ha movido con fusiones, destejidos y renombres
   desde entonces, y ninguna de las cuatro dedupes que la propia
   `verificacion` de `OP-E-06` exige (contra la bolsa de la fase 04, contra
   aristas ya escritas, contra la cola de relectura post fusion, y contra
   pares que ya tienen arista resolviendo alias) se ha vuelto a correr sobre
   el grafo de hoy.

**ESTO ES PARADA por `AUDITOR.md` seccion 3** ("una operacion cuyo texto no
alcance para ejecutarse sin decidir es PARADA, no una improvisacion"; modo de
ejecucion continua: "cualquier operacion cuyo texto no alcance para
ejecutarse sin decidir [...] convoca al auditor en la vuelta siguiente"). NO
es la parada de `AUDITOR.md` seccion 4 (no se escribe `PARA_ALEXIS.md`, la
campana no esta consumada): es la parada especifica de esta operacion, que
se trae aqui escrita para que el auditor decida el remedio (por ejemplo,
ensanchar `barrido_razones_d.py` para que resuelva direccion y re-correr
sobre el grafo de hoy) en vez de que yo la improvise.

## PENDIENTES DE DOCTRINA

Ninguno esta vuelta. Las dos piezas de la TAREA 2 estaban adjudicadas por el
acta 86 sin doctrina nueva, y la lectura del tramo 12 no encontro ninguna
pregunta que la doctrina vigente (banco 9.6, 9.6.1, 9.6.2, 9.6.3, 9.8, 9.9) no
contestara.

## REPASO PUNTO POR PUNTO DEL ENCARGO, antes de cerrar

- Commitear y pushear lo pendiente antes de tocar nada: SI, working tree
  estaba limpio al abrir (verificado con `git status`).
- TAREA 1, los registros: SI, seccion 1.
- TAREA 2, el instrumento, BLOQUEANTE, dos piezas, commit propio ANTES del
  filtro: SI, commit `c3642f7f`, pusheado antes de correr el filtro del
  tramo 12.
- TAREA 3, la cola de `OP-E-01` leida POR LO NO DECIDIDO, bolsa fresca,
  filtro/guarda/cadena ANTES de leer, 4 unidades, discutibles marcados,
  varas de contraste del encargo confirmadas: SI, seccion 3, commit
  `7398b308`.
- TAREA 4, la vara del tramo 12 con instrumento propio, cifras del acta 86
  confirmadas, Y el cierre medido de `OP-E-01` (4.d), con `estado` intacto y
  `nota` mas `04_ENLACES.md` escritos con la cifra final: SI, seccion 4,
  commit `4087f8f6`.
- TAREA 5, instrumento propio de lo que viene despues, campo `estado` nunca
  leido, tabla publicada, `OP-E-06` identificada y NO abierta, pregunta de
  si su texto alcanza contestada con PARADA escrita: SI, seccion "TAREA 5"
  arriba, commit `dd8546dc`.
- Lo que no se escribe en prosa (comparaciones sin cifra): SI, respetado.
- Cabecera tallada con `--fase04 --vuelta 87`, pegada entera: SI, corrida
  DESPUES de escribir este fichero, con `--comparar` contra este mismo
  reporte antes del commit de cierre (resultado citado abajo).
- `--comparar` del tramo 12 contra este reporte, cabecera y tabla de la
  cadena identicas, EXIT 0: corrido tras escribir este fichero (resultado
  citado abajo).
- Sello del HEAD de apertura antes de la primera operacion: SI,
  `docs/loop/SALIDA_V87_HEAD_APERTURA.txt` = `fe24bd71`.
- Hornear el registro dos veces DENTRO de esta vuelta, con fichero propio
  cada corrida, guarda corrida despues del segundo con la definicion nueva:
  SI, secciones 2 y 5.
- Cero guiones largos ni medios: repasado a mano en este fichero.

## `--comparar`, corridos DESPUES de escribir este fichero

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 87
--comparar docs/loop/REPORTE.md`:

```
filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0
CABECERA: IDENTICA AL TALLADOR
```

`python scripts/loop/tallar_cabecera_reporte.py --vuelta 87 --tramo-cadena 12
--comparar docs/loop/REPORTE.md`:

```
UNIDADES NO PUBLICADAS EN ESA TABLA: 0

filas cotejadas: 4 | DISTINTAS: 0 | ausentes (no rojo): 0 | inventadas (ROJO): 0
TABLA DE LA CADENA: IDENTICA AL TALLADOR (las ausentes listadas no son rojo)
```

## DISCUTIBLES, listados para la relectura ciega del auditor

Contados de la columna DISCUTIBLE de la tabla de la seccion 3, DOS:
**117, 118.**
