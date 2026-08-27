# REPORTE DE LA VUELTA 86 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 85. Apertura sellada ANTES de la primera operacion en
`docs/loop/SALIDA_V86_HEAD_APERTURA.txt`: `4cc090a2` (el acta de la vuelta 85).
Cierre recomputado AL CIERRE, con las suites y el grafo tal como quedan tras
escribir el tramo 11.

## CABECERA TALLADA (--fase04 --vuelta 86), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 86`
Salida completa en `docs/loop/_v86_cabecera_tallada.txt`, EXIT 0.

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.986 / 8.965 / 17.951 / 9.609 | **8.994 / 8.973 / 17.967 / 9.617** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+8 / +8 / +16 / +8** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 7 fila(s): `lienzo_proyecto_innovacion -> actividades_clave`, `estructura_equipos_innovacion_interna -> equipo_multifuncional_real`, `evaluacion_industria_cliente -> analisis_cadena_de_valor`, `diagrama_de_flujo_proceso_map -> analisis_flujo_proceso`, `stage_gate_system -> tipos_criterios_gate`, `waterfall_vs_agile_development -> customer_development_process`, `decidir_vender_solo_online_o_tambien_tienda_fisica -> ofrecer_puntos_recogida` | **8 fila(s): `determinacion_cuota_inicial -> analisis_competencia_franquicias`, `remover_barreras_orgullo_trabajo -> eliminar_slogans_y_exhortaciones`, `distribucion_poisson -> muestreo_de_aceptacion`, `personalizar_interacciones_cliente -> conexion_personal_emocional`, `customer_discovery_phase2_problem_test -> preparar_contacto_clientes`, `definicion_calidad_fitness_for_purpose -> descubrir_necesidades_del_cliente`, `definicion_y_concepto_de_aseguramiento_de_calidad -> trilogia_juran_qa_qc`, `motor_crecimiento_pago -> valor_de_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `4cc090a2` (ACTA DE LA VUELTA 85 DEL AUDITOR, leido de git log), HEAD real de apertura `4cc090a2` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `4cc090a2` (ACTA DE LA VUELTA 85 DEL AUDITOR, leido de git log), HEAD real de apertura `4cc090a2` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

La celda del desfase sale OBLIGATORIA por primera vez (TAREA 2.c): con el
fichero de apertura renombrado a un lado, el tallador cae en ROJO nombrando
la salida ausente (`docs/loop/SALIDA_V86_CASO_OBLIGATORIO_2C.txt`), y con el
fichero de vuelta a su sitio talla igual que antes.

El ciclo de tres (Gate 0, `etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`)
se corrio dos veces seguidas tras escribir las ocho aristas, y el `master_graph.json`
resultante da el MISMO hash sha256 las dos veces
(`03fbd62f5482e3208915592f549fe464f01e0372187d734c103c0aa2f214df01`): el ciclo es
estable sobre el arbol de hoy, aunque `etiquetas_de_cara.py` reporte "71 etiquetas
cambian" en cada corrida (recompila `master_graph.json` desde cero en el paso de
Gate 0 y vuelve a parchear las mismas 71 etiquetas: el hash final no cambia).

## 1. TAREA 1, los registros y la correccion declarada

**(1.1) La caida de reporte de la vuelta 85 queda registrada con su nombre**,
sin volver a medirla (viene medida en el acta 85, seccion 4.1): la frase *"en
los tramos 8 y 9, los pares con veredicto D coincidieron siempre con la
decision NO SE ENLAZA"*. Sube la racha de REPORTE de UNO a DOS; la parada pide
TRES y no se dispara, la escalada de `EJECUTOR.md` regla 1 pide DOS y SI se
dispara: es la TAREA 2 de esta vuelta (seccion 2 mas abajo).

**(1.2) CORRECCION DECLARADA**, con el texto viejo intacto delante: la frase
de la vuelta 85 decia *"en los tramos 8 y 9, los pares con veredicto D
coincidieron siempre con la decision NO SE ENLAZA"*. Eso es falso: en los
tramos 8 y 9 hay CUATRO pares con veredicto, los CUATRO clase D, y UNO de
ellos (`formulacion_teorias_causa -> diagrama_causa_efecto`, tramo 9, puesto
2.980) figura HOY como ESCRITA, porque la propia vuelta 85 lo corrigio en su
TAREA 2. La conclusion sobre el marcador (que mide semejanza global y no cita
literal de paso, asi que un D no predice la clase) NO cambia; la premisa
historica SI. Tallado hoy en `docs/loop/SALIDA_V86_TAREA4_VARA_TRAMO11.txt`,
seccion PATRON HISTORICO: tramo 8, 2 con veredicto, 2 clase D, 0 ESCRITA, 2 NO
SE ENLAZA; tramo 9, 2 con veredicto, 2 clase D, 1 ESCRITA, 1 NO SE ENLAZA.

**(1.3) Tres cosas que la vuelta 85 cerro, registradas por su nombre, sin
remedirlas** (acta 85, secciones 1.6, 1.13 y 5.1):
- El atasco del registro esta MUERTO: el reparto por tramo llego al 10 en la
  vuelta 85 y las 30 decisiones de esa vuelta quedaron dentro del registro
  commiteado (acta 85, seccion 1.6).
- Las dos filas talladas de `--fase04` de la vuelta 84 quedaron REMEDIADAS Y
  PROBADAS CON REGRESION: tallada la vuelta 84 con el instrumento nuevo, la
  fila da `+6 / +6 / +12 / +6`, y el desfase sobre el commit del acta 84 da 3
  filas, las mismas que el auditor conto a mano (acta 85, seccion 1.13).
- La ambiguedad de la vara del acta 84 quedo cerrada sin sustitucion callada:
  la guarda aprendio el estado ESCRITA (adjudicacion 5.1 del acta 85, TAREA
  2.a de esta vuelta).

**(1.4) Las diez adjudicaciones de la seccion 5 del acta 85, registradas por
su numero, sin remedirlas:**
- **5.1** La guarda aprende el estado ESCRITA: sin doctrina nueva, cuenta como
  decidida cualquier fila del registro. Ejecutada en la TAREA 2.a de esta
  vuelta.
- **5.2** La caida de reporte de la seccion 4 del acta 85 queda registrada con
  su nombre y se corrige con el texto viejo intacto delante. Ejecutada en
  1.1 y 1.2 de arriba.
- **5.3** La escalada de `EJECUTOR.md` regla 1 se dispara (racha de REPORTE en
  dos tandas): el instrumento de la vara gana la seccion PATRON HISTORICO.
  Ejecutada en la TAREA 2.b de esta vuelta.
- **5.4** La fila del desfase deja de ser opcional en `--fase04`. Ejecutada en
  la TAREA 2.c de esta vuelta.
- **5.5** Una comparacion sin cifra no se publica: esta vuelta no escribe
  ninguna frase que compare tramos o tandas sin un fichero que la sostenga
  (ver la seccion "LO QUE NO SE ESCRIBE" mas abajo).
- **5.6** La clase de las diez aristas de la vuelta 85 se ratifica: no afecta
  a esta vuelta directamente, solo se cita.
- **5.7** Los caveats de paso se anotan y el filtro gana el aviso del paso
  vecino con mas literalidad. Ejecutada en la TAREA 2.d de esta vuelta.
- **5.8** El credito de tanda sigue rebajado: se releyo el tramo 11 ENTERO (30
  de 30), no una muestra.
- **5.9** Lo que sigue sin escribirse (septima acta): `descubrir_necesidades_
  del_cliente -> customer_needs_spreadsheet` y `curva_caracteristica_
  operativa -> distribucion_poisson` siguen fuera de `PASO_NODO_CALIBRADO.
  jsonl`; no vueltas a verificar esta vuelta porque `OP-E-01` no decide fuera
  de su bolsa y esta vuelta no toco esas dos claves.
- **5.10** El final de `OP-E-01` ya se veia: tras el tramo 10 quedaban 34 sin
  decidir (30 para el tramo 11 y 4 de cola). Confirmado por esta vuelta: el
  filtro de hoy midio exactamente eso antes de leer (ver TAREA 3 mas abajo).

## 2. TAREA 2, EL INSTRUMENTO (BLOQUEANTE), commit `d13a951a`

Las cuatro piezas, todas commiteadas y pusheadas ANTES del filtro del tramo
11, porque la (2.a) cambia lo que el filtro y la guarda ven.

**(2.a) La guarda aprende el estado ESCRITA**
(`scripts/loop/vuelta83_guarda_decididas.py`): cuenta como decidida CUALQUIER
fila del registro, no solo `NO SE ENLAZA`, e imprime la decision al lado de
cada unidad del prefijo. Casos obligatorios, los dos corridos:
- **VERDE** sobre la bolsa V85 con el registro de 186 filas
  (`docs/loop/SALIDA_V86_CASO_2A_VERDE.txt`): prefijo 0 a 101 (102 unidades),
  primera sin decidir el indice 102, `determinacion_cuota_inicial ->
  analisis_competencia_franquicias` (paso 2, franquicias). Identico al
  contraste medido por el auditor en la adjudicacion 5.1 del acta 85.
- **ROJO inventado** (`docs/loop/SALIDA_V86_CASO_2A_ROJO.txt`), sobre una
  COPIA del registro (`docs/loop/_v86_registro_rojo_inventado.jsonl`, con la
  fila `principios_alineacion_empresarial -> desarrollar_estrategias_largo_
  plazo`, indice 50 de la bolsa, borrada del medio de la cabeza): EXIT 1,
  ROJO, nombrando la unidad. El registro real NUNCA se toco para este caso.

**(2.b) La tabla del PATRON HISTORICO**
(`scripts/loop/vuelta86_tarea4_vara_tramo11.py`, sucesor de `vuelta85_tarea5_
vara_tramo10.py`): para cada tramo con pares con veredicto, tallada de
`docs/plan/OP_E_01_DECIDIDAS.jsonl` y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`,
nunca de memoria. Caso obligatorio confirmado en
`docs/loop/SALIDA_V86_PATRON_HISTORICO.txt`: `formulacion_teorias_causa ->
diagrama_causa_efecto` sale tramo 9, clase D, decision ESCRITA, el hecho que
la prosa de la vuelta 85 nego. La tabla completa, corrida sobre los datos de
hoy (con el tramo 11 ya dentro), esta en la seccion 4 mas abajo, pegada de
`docs/loop/SALIDA_V86_TAREA4_VARA_TRAMO11.txt`.

**(2.c) La fila del desfase deja de ser opcional en `--fase04`**
(`scripts/loop/tallar_cabecera_reporte.py`): se lee ahora con `leer()` (no con
`leer_opcional()`), asi que su ausencia es FALLO DECLARADO. El docstring de
`leer_opcional()` ya no dice que el marcador sea "la unica opcional". Caso
obligatorio corrido con el fichero de apertura renombrado
(`docs/loop/SALIDA_V86_CASO_OBLIGATORIO_2C.txt`): ROJO, 20 celdas no
legibles, la primera de la lista nombrando exactamente la salida ausente
(`no existe la salida SALIDA_V86_DESFASE_CALIBRADO_APERTURA.txt`); con el
fichero de vuelta a su sitio, la cabecera talla identica a la de arriba.

**(2.d) El filtro avisa del paso vecino con mas literalidad**
(`scripts/loop/vuelta86_aviso_paso_vecino.py`, wireado en
`scripts/loop/vuelta86_tramo11_filtrar.py`): cuando el filtro trae o aparta
una unidad, avisa si OTRO paso de la misma madre nombra al mismo hijo con MAS
literalidad (`rapidfuzz.token_set_ratio` del titulo del hijo contra cada paso
de la madre) que el paso que la unidad trae. No decide nada. Disparo en la
lectura de hoy: la unidad 100 (`conditions_precedent_financing -> entender_
term_sheet`, paso 3, ratio 74.3) trae el aviso de que el paso 1 de la misma
madre nombra al mismo hijo con mas literalidad (ratio 77.8); la lectura de
esta unidad (TAREA 3, discutible) considero el aviso y de todos modos decidio
NO SE ENLAZA por motivos de contenido, no de literalidad de paso (ver razon
completa abajo). **Heuristica declarada y sus falsos positivos, sin callarlos**
(docstring del modulo): compara solo `titulo_ratio` (si el paso NOMBRA al
hijo), no contencion de vocabulario ni familia de verbo; un paso puede nombrar
al hijo de pasada con un ratio alto sin ser el paso que realmente lo
desarrolla, asi que el aviso no distingue "nombra de pasada" de "desarrolla
de verdad": es informativo, el lector tiene que leer los dos pasos.

## 3. TAREA 3, el tramo 11 de OP-E-01, leido POR LO NO DECIDIDO

**Bolsa recalibrada FRESCA** antes de leer: `python scripts/plan/paso_contra_
nodo_calibrado.py --umbral-titulo 72 --umbral-contencion 0.45 --min-tokens 4`
(`docs/loop/SALIDA_V86_RECALIBRADO.txt`), bolsa reducida 468 filas, 221 sin
arista (228 menos las 7 aristas que la vuelta 85 escribio).

**Filtro P.9.1 ensanchado + guarda del par no dirigido + vara de la cadena +
aviso del paso vecino** corridos ANTES de leer nada
(`scripts/loop/vuelta86_tramo11_filtrar.py` >
`docs/loop/SALIDA_V86_TRAMO11_FILTRO_P91_GUARDA_CADENA.txt`): 221 candidatos
sin arista, 92 apartados por P.9.1 ensanchado (35 solo por operacion, 57 con
motivo de la vara de los A), 129 limpios tras el filtro, 0 parejas del par no
dirigido, 129 unidades de lectura, escrito
`docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl` (129 filas). Registro de
decididas leido: 97 pares `NO SE ENLAZA`. **95 unidades ya decididas en la
cabeza, saltadas** (no se releen ni se re-derivan sus razones); **primera
unidad SIN DECIDIR el indice 95**, `determinacion_cuota_inicial ->
analisis_competencia_franquicias` (paso 2, franquicias); **30 frescas**
(indices 95 a 124); **4 unidades sin decidir restantes tras esta cabeza**
(indices 125 a 128).

**Las varas de contraste que el auditor midio hoy salen las CUATRO EXACTAS**:
bolsa filtrada 129, prefijo de decididas que sobrevive 95, primera sin
decidir el indice 95 (`determinacion_cuota_inicial -> analisis_competencia_
franquicias`, paso 2, franquicias), 34 sin decidir (30 frescas + 4 de cola).
Cero discrepancias que declarar.

Las 30 fichas de madre e hijo se volcaron ENTERAS antes de leer
(`docs/loop/_v86_volcado_tramo11.txt`, instrumento `scripts/loop/_v86_volcar_
tramo11.py`, 60 fichas). Credito de tanda REBAJADO por la caida de reporte de
la vuelta 85 (adjudicacion 5.8): se leyeron las 30 ENTERAS, no una muestra.

### Las 30 lecturas, con razon y discutibles marcados ANTES de saber si aciertan

La columna "cadena" es la tallada de `docs/loop/tallar_cabecera_reporte.py
--vuelta 86 --tramo-cadena 11` (seccion siguiente); no decide nada por si
sola (banco 9.6.1, caveat de la familia encadenada).

| # | par (paso) | cadena | decision | DISCUTIBLE | razon |
|---:|---|---|---|:---:|---|
| 95 | `determinacion_cuota_inicial -> analisis_competencia_franquicias` (paso 2) | SIN CAMINO PREVIO | **SE ESCRIBE** | SI | El paso 2 de la madre ("analizar las cuotas iniciales de competidores directos comparables") nombra en una linea el tema que el hijo entero desarrolla: identificar competidores, revisar sus FDD, entrevistar a sus franquiciados y preguntar a los prospectos. La madre conserva material propio (costos, posicionamiento, barreras de entrada) que el hijo no toca. DISCUTIBLE porque el hijo es mas ancho (inteligencia competitiva completa) que la linea estricta de "cuotas iniciales" del paso 2. |
| 96 | `key_partners_hypothesis -> actualizar_business_model_canvas_tuneup` (paso 5) | ALCANZABLE (4 saltos) | NO SE ENLAZA | | El paso 5 ("actualiza el BMC con los socios identificados") es una linea sobre anadir SOCIOS al lienzo. El hijo es un procedimiento distinto: el "tune-up" del BMC completo TRAS cada ronda de Customer Discovery (revisar propuesta de valor, segmentos, hipotesis de ingresos), sin mencionar socios en ninguno de sus 4 pasos. El solape es el nombre "Business Model Canvas", no el contenido (9.6.3: el tamano del solape no decide, lo que importa es el resto). |
| 97 | `clasificacion_benchmarking -> consortium_benchmarking` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | SI | El paso 4 ("evaluar nivel de control, costo y tiempo del tipo elegido") es generico y no nombra "consorcio" en ningun momento; ningun paso de la madre lo hace. El hijo es una instancia especifica de benchmarking (por participantes) que ningun paso desarrolla literalmente. DISCUTIBLE: la madre ya enlaza a `generic_benchmarking`, otra instancia de tipo, sin que se sepa cuantos tipos-hermanos existen para aplicar 9.6.1 con seguridad. |
| 98 | `remover_barreras_orgullo_trabajo -> eliminar_slogans_y_exhortaciones` (paso 6) | ALCANZABLE (6 saltos) | **SE ESCRIBE** | | El paso 6 ("reemplazar carteles y exhortaciones por comunicacion real de avances") nombra EXACTO el tema del Punto 10 de Deming, que es el hijo entero: revisar los carteles, eliminar frases vacias, calcular que parte del error es del sistema, reemplazar por comunicacion clara, trabajar con proveedores. Es un procedimiento de 5 pasos, no una linea (9.6.1 continua-o-repite): CONTINUA. La madre conserva material propio (pasos 1 a 5, sobre barreras generales) que el hijo no toca. |
| 99 | `sujetos_de_control -> optimizacion_caracteristicas_diseno` (paso 3) | SIN CAMINO PREVIO | NO SE ENLAZA | | El paso 3 ("traducir la voz del cliente en KPC") es sobre TRADUCIR necesidades a caracteristicas; el hijo es sobre OPTIMIZAR caracteristicas ya elegidas (revision de diseno, equipos multifuncionales, negociacion). Son etapas distintas del ciclo de diseno. Ademas la madre ya enlaza a `key_process_product_characteristics`, que es el sibling que de verdad cubre la traduccion VOC-a-KPC del paso 3. |
| 100 | `conditions_precedent_financing -> entender_term_sheet` (paso 3) | ALCANZABLE (3 saltos) | NO SE ENLAZA | SI | El hijo es un nodo INTRODUCTORIO y mas general ("el arte del term sheet": el marco economia-vs-control) que una clausula especifica del term sheet (condiciones previas) no "desarrolla": la relacion natural es la inversa (entender_term_sheet es prerrequisito de conditions_precedent_financing, no su desarrollo). Trae el CAVEAT DE PASO de la TAREA 2.d (el paso 1 nombra al hijo con mas literalidad, ratio 77.8 contra 74.3 del paso 3); se leyeron los dos pasos y ninguno de los dos desarrolla el hijo en el sentido de 9.6.2 (que anade el HIJO a la MADRE), asi que el veredicto no cambia por el aviso. |
| 101 | `distribucion_poisson -> muestreo_de_aceptacion` (paso 4) | SIN CAMINO PREVIO | **SE ESCRIBE** | | El paso 4 ("usar el resultado para decisiones de aceptacion de lotes") nombra en una linea el tema entero del hijo: un procedimiento completo de muestreo de aceptacion (definir n y c, niveles de riesgo, elegir plan, documentar). La madre conserva material propio (cálculo de la distribucion, tabla np) que el hijo no toca. |
| 102 | `transformacion_calidad_compromiso_alta_direccion_japon -> planificacion_calidad_crosby` (paso 5) | SIN CAMINO PREVIO | NO SE ENLAZA | | La madre es el caso historico de Japon (JUSE, 1950-1970) sobre el compromiso de la alta direccion; el hijo es la filosofia de planificacion de Crosby (documentar toda actividad de calidad con una linea de accion). Proximidad tematica (ambos "compromiso con la calidad") pero ningun paso de la madre desarrolla el procedimiento de planificacion que el hijo trae. |
| 103 | `personalizar_interacciones_cliente -> conexion_personal_emocional` (paso 1) | SIN CAMINO PREVIO | **SE ESCRIBE** | | El paso 1 ("usa los datos personales o emocionales de cada cliente para crear mensajes personalizados") nombra literalmente el tema que el hijo entero desarrolla: clasificar datos personales/emocionales, priorizarlos, usar el nombre del cliente, crear rituales. La madre conserva material propio (honestidad, agrupacion por interes, eventos) que el hijo no toca. |
| 104 | `sistema_pull_push -> takt_time` (paso 3) | SIN CAMINO PREVIO | NO SE ENLAZA | SI | El paso 3 ("redisenar el flujo para que la produccion se autorice segun demanda real") es una descripcion abstracta del principio pull; ningun paso de la madre nombra "takt time" ni su calculo. El hijo es una herramienta especifica y mas ancha (formula, balanceo de linea, SMED) que no cabe entera en la linea del paso 3. Tematicamente muy cercano (el takt time es central en un sistema pull), por eso queda discutible. |
| 105 | `customer_discovery_phase2_problem_test -> preparar_contacto_clientes` (paso 2) | ALCANZABLE (5 saltos) | **SE ESCRIBE** | | El titulo del paso 2 ("prepararse para contactos y entrevistas con clientes") calca el titulo del hijo ("Preparacion de Contactos con Clientes Potenciales"). El hijo trae el procedimiento completo (lista de 50 clientes, historia de referencia, calendario) que el paso 2 solo nombra en una linea. La madre conserva material propio (pasos 1, 3, 4, 5) que el hijo no toca. |
| 106 | `formalizar_un_proceso_ad_hoc -> metricas_calidad` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | SI | `metricas_calidad` es un nodo generico y muy reusado (define atributo, metrica, metodo, ID) que calibro contra TRES madres distintas de este mismo tramo (106, 107, 108) por solape de vocabulario ("metrica", "medir", "definir"). Ninguna de las tres pasos menciona el rasgo que distingue al hijo (documentar en formato estandarizado CON ID UNICO), asi que se trata como colision de vocabulario en un nodo definicional generico y no como jerarquia real, en las tres. |
| 107 | `medir_lo_que_importa_no_solo_lo_facil -> metricas_calidad` (paso 1) | ALCANZABLE (5 saltos) | NO SE ENLAZA | SI | Mismo motivo que 106: ademas, el paso 1 es sobre AUDITAR que se mide hoy (listar metricas actuales), no sobre el procedimiento generico de DEFINIR una metrica que el hijo trae; son actividades distintas. |
| 108 | `plan_mejora_procesos -> metricas_calidad` (paso 3) | ALCANZABLE (5 saltos) | NO SE ENLAZA | SI | Mismo motivo que 106: el paso 3 bloque junto "metricas y limites de control", y el hijo no toca "limites de control" en ningun paso; solape parcial sobre un nodo generico ya sospechoso por el patron 106-108. |
| 109 | `sujetos_de_control -> establecer_metas_caracteristicas` (paso 3) | SIN CAMINO PREVIO | NO SE ENLAZA | | Mismo paso 3 que la unidad 99 ("traducir voz del cliente en KPC"), que ya tiene un sibling dedicado (`key_process_product_characteristics`). El hijo (fijar metas cuantificadas) es una etapa posterior a la que el paso 3 describe (todavia se esta traduciendo, no fijando metas numericas). |
| 110 | `escenarios_diseno_modelo_negocio -> escenarios_de_evolucion_de_la_ia` (paso 5) | ALCANZABLE (3 saltos) | NO SE ENLAZA | | El paso 5 citado ("evalua si un solo modelo sirve para todos los escenarios") no habla de IA; el paso que si se acercaria (6, "usa los escenarios de entorno futuro para anticipar como evolucionar") no es el que el calibrado trajo. Existe ademas una jerarquia sana ya cableada (madre -> `lienzo_modelo_negocio` -> `future_scenarios_planning` -> el hijo): un enlace directo saltaria ese nivel sin que el paso citado lo justifique. |
| 111 | `definicion_calidad_fitness_for_purpose -> descubrir_necesidades_del_cliente` (paso 2) | ALCANZABLE (4 saltos) | **SE ESCRIBE** | SI | El paso 2 ("determina las necesidades explicitas e implicitas de ese cliente") nombra exacto lo que el hijo entero desarrolla: declaradas vs reales vs percibidas vs culturales, metodos de recoleccion, priorizacion, traduccion. La madre conserva material propio (identificar cliente, traducir a caracteristicas, documentar fallas) que el hijo no toca. DISCUTIBLE: la madre tiene un titulo muy cercano a un sibling ya existente (`fitness_for_use_purpose`, que ya enlaza al mismo hijo por otra via); se anota la proximidad sin decidir fusion, que es operacion distinta a esta. |
| 112 | `inventario_conocimiento_estadistico_personal -> roi_proyectos_calidad` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | | El paso 4 ("integrar a este personal en proyectos de mejora") es sobre STAFFING; el hijo es sobre CALCULAR EL ROI financiero de esos proyectos. Distinto objeto pese a compartir "proyectos de mejora de calidad". |
| 113 | `reconocer_mercancia_peligrosa_disfrazada -> clasificar_tipo_paquete` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | | El paso 4 ("capacitate antes de despachar el primer envio de este tipo") es sobre CAPACITACION del propio despachador en mercancia peligrosa; el hijo es sobre clasificar el paquete por dimension y fragilidad, un eje totalmente distinto de la logistica de empaque. |
| 114 | `identificacion_proveedores_criticos -> validacion_externa_reportes` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | | El paso 4 ("revisa los reportes de sostenibilidad de tu COMPETENCIA para comparar") es benchmarking competitivo; el hijo es sobre conseguir validacion de terceros de TUS PROPIOS reportes. Direccion distinta del mismo tema "reportes de sostenibilidad". |
| 115 | `tipos_de_riesgo_invencion_vs_mercado -> fundadores_lideran_validacion` (paso 4) | ALCANZABLE (3 saltos) | NO SE ENLAZA | | El paso 4 ("si es ambos, combinar validacion tecnica con desarrollo de clientes") es una regla de decision entre metodologias; el hijo es sobre QUIEN debe liderar la validacion. La jerarquia ya esta sana: el paso 3 de esta misma madre ("aplicar el proceso de Customer Development") ya enlaza a `customer_development_modelo`, que encadena hasta el hijo; un enlace directo saltaria ese nivel. |
| 116 | `definicion_y_concepto_de_aseguramiento_de_calidad -> planificacion_inicial_calidad` (paso 1) | SIN CAMINO PREVIO | NO SE ENLAZA | | El paso 1 solo menciona "planificacion" como una de cuatro palabras de alcance (planificacion, control, mejora, revision) dentro de una definicion general de QA; el hijo es un procedimiento detallado y especifico de manufactura (KPC, diagrama de flujo por estacion, capacidad de proceso) que ese paso no desarrolla. Colision de vocabulario sobre la palabra "planificacion". |
| 117 | `definicion_y_concepto_de_aseguramiento_de_calidad -> trilogia_juran_qa_qc` (paso 3) | SIN CAMINO PREVIO | **SE ESCRIBE** | | El paso 3 ("diferencia el aseguramiento de calidad de otras tareas de calidad relacionadas") nombra exacto lo que el hijo entero desarrolla: la distincion QA contra QC, unificadas bajo ISO 8402. La madre conserva material propio (alcance, evidencias, comunicacion) que el hijo no toca. |
| 118 | `planificacion_recoleccion_datos -> analisis_pareto_proyectos_elefante` (paso 7) | SIN CAMINO PREVIO | NO SE ENLAZA | | El paso 7 ("evaluar supuestos del tamano de muestra y del analisis") es sobre metodologia estadistica de muestreo; el hijo es sobre subdividir proyectos demasiado grandes con Pareto. Sin relacion de contenido pese a compartir dominio quality. |
| 119 | `rol_director_calidad -> circulos_calidad_qc` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | SI | El paso 4 citado ("actuar como asesor estrategico en las decisiones de calidad") es sobre el rol de asesoria estrategica; el hijo (circulos de calidad, que el lider debe apoyar y sobre los que debe actuar) se acerca mas al paso 2 ("pasar actividades a quienes ejecutan el trabajo"), que no es el paso que el calibrado trajo. DISCUTIBLE por ese desfase de paso dentro de la misma madre. |
| 120 | `establecer_diseno_final_producto -> establecer_metas_caracteristicas` (paso 1) | SIN CAMINO PREVIO | NO SE ENLAZA | | Direccion invertida (9.6.2): la madre es la etapa FINAL (publicar el diseno ya autorizado); el hijo es fijar metas cuantificadas, que logicamente ocurre ANTES de publicar el diseno final, no despues. `establecer_metas_caracteristicas` tiene `nodos_siguientes` vacio hoy, consistente con ser un paso previo sin salida propia, no un desarrollo de esta madre. |
| 121 | `desarrollo_value_proposition_usp -> posicionamiento_vs_competidores` (paso 1) | SIN CAMINO PREVIO | NO SE ENLAZA | SI | El paso 1 ("identificar que hace unico al negocio frente a competidores") es analisis INTERNO durante el diseno de la oferta de franquicia; el hijo es una practica de conversacion con CANDIDATOS durante la venta, una etapa posterior y de otro proceso (venta de franquicias, no diseno de la propuesta). Proximidad tematica real (el hijo cita literalmente tener la USP "ya definida"), por eso queda discutible. |
| 122 | `motor_crecimiento_pago -> valor_de_vida_del_cliente` (paso 1) | ALCANZABLE (6 saltos) | **SE ESCRIBE** | | El paso 1 ("calcular el LTV despues de costos variables") nombra literal el tema entero del hijo: calcular, monitorear, mejorar el LTV con programas y retencion. La madre conserva material propio (CPA, margen, monetizacion, evitar tacticas puntuales) que el hijo no toca. |
| 123 | `constraint_management -> caso_estudio_benchmarking_terminal` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | | El paso 4 ("elevar el desempeno de la restriccion mediante inversion o mejora") es un paso generico de la Teoria de Restricciones; el hijo es un caso de estudio real de una terminal petrolera mejorada por benchmarking, sin mencion de restricciones en ninguno de sus pasos. |
| 124 | `ingenieria_calidad_proveedores -> desarrollar_estrategias_largo_plazo` (paso 4) | SIN CAMINO PREVIO | NO SE ENLAZA | | Colision de vocabulario en la frase "largo plazo": el paso 4 es sobre relaciones DE LARGO PLAZO CON PROVEEDORES especificamente; el hijo es sobre estrategia de negocio completa (5 areas: clientes, COPQ, cultura, procesos, competencia), sin mencionar proveedores en ninguno de sus 4 pasos. |

**RESUMEN DE LA TANDA: 8 de 30 SE ESCRIBE, 22 de 30 NO SE ENLAZA, 10
DISCUTIBLES** (contados de la columna DISCUTIBLE de la tabla de arriba: 95,
97, 100, 104, 106, 107, 108, 111, 119, 121). La cuenta se tallo dos veces,
por `scripts/loop/vuelta86_medir_tramo11.py` (linea final de
`docs/loop/SALIDA_V86_TRAMO11_ESCRIBIR.txt`) y citada igual en
`docs/loop/SALIDA_V86_TAREA4_VARA_TRAMO11.txt`; las dos calzan con la tabla.

Aristas escritas esta tanda (`scripts/loop/vuelta86_tramo11_escribir.py` >
`docs/loop/SALIDA_V86_TRAMO11_ESCRIBIR.txt`, verificadas con instrumento
propio `scripts/loop/vuelta86_medir_tramo11.py`): **8 ARISTAS ESCRITAS, 0
ESCALERA ROTA, 0 INCONSISTENTES**, las ocho presentes en las DOS vistas
(`nodos_siguientes` de la madre Y `nodos_previos` del hijo), sin inversas.

**El horizonte de la vara de la cadena, recomputado con tope 30** sobre el
commit `d13a951a` (TAREA 2, antes de escribir las 8 aristas de esta vuelta),
instrumento propio (`docs/loop/SALIDA_V86_TRAMO11_HORIZONTE.txt`): de las 20
unidades SIN CAMINO PREVIO a 6 saltos, **15 SI tienen camino mas largo, de 7 a
17 saltos**, y **5 no lo tienen ni a 30 saltos**: `formalizar_un_proceso_ad_
hoc -> metricas_calidad`, `reconocer_mercancia_peligrosa_disfrazada ->
clasificar_tipo_paquete`, `definicion_y_concepto_de_aseguramiento_de_calidad
-> planificacion_inicial_calidad`, `definicion_y_concepto_de_aseguramiento_de
_calidad -> trilogia_juran_qa_qc`, `desarrollo_value_proposition_usp ->
posicionamiento_vs_competidores`.

### La tabla de alcanzabilidad (vara de la cadena) del tramo 11

Comando: `python scripts/loop/tallar_cabecera_reporte.py --vuelta 86 --tramo-cadena 11`.
Salida completa en `docs/loop/_v86_tabla_cadena_tramo11.txt`, EXIT 0.

| # | par (paso) | alcanzable previo (vara de la cadena) |
|---:|---|---|
| 95 | `determinacion_cuota_inicial -> analisis_competencia_franquicias (paso 2)` | SIN CAMINO PREVIO |
| 96 | `key_partners_hypothesis -> actualizar_business_model_canvas_tuneup (paso 5)` | ALCANZABLE (4 saltos) |
| 97 | `clasificacion_benchmarking -> consortium_benchmarking (paso 4)` | SIN CAMINO PREVIO |
| 98 | `remover_barreras_orgullo_trabajo -> eliminar_slogans_y_exhortaciones (paso 6)` | ALCANZABLE (6 saltos) |
| 99 | `sujetos_de_control -> optimizacion_caracteristicas_diseno (paso 3)` | SIN CAMINO PREVIO |
| 100 | `conditions_precedent_financing -> entender_term_sheet (paso 3)` | ALCANZABLE (3 saltos) |
| 101 | `distribucion_poisson -> muestreo_de_aceptacion (paso 4)` | SIN CAMINO PREVIO |
| 102 | `transformacion_calidad_compromiso_alta_direccion_japon -> planificacion_calidad_crosby (paso 5)` | SIN CAMINO PREVIO |
| 103 | `personalizar_interacciones_cliente -> conexion_personal_emocional (paso 1)` | SIN CAMINO PREVIO |
| 104 | `sistema_pull_push -> takt_time (paso 3)` | SIN CAMINO PREVIO |
| 105 | `customer_discovery_phase2_problem_test -> preparar_contacto_clientes (paso 2)` | ALCANZABLE (5 saltos) |
| 106 | `formalizar_un_proceso_ad_hoc -> metricas_calidad (paso 4)` | SIN CAMINO PREVIO |
| 107 | `medir_lo_que_importa_no_solo_lo_facil -> metricas_calidad (paso 1)` | ALCANZABLE (5 saltos) |
| 108 | `plan_mejora_procesos -> metricas_calidad (paso 3)` | ALCANZABLE (5 saltos) |
| 109 | `sujetos_de_control -> establecer_metas_caracteristicas (paso 3)` | SIN CAMINO PREVIO |
| 110 | `escenarios_diseno_modelo_negocio -> escenarios_de_evolucion_de_la_ia (paso 5)` | ALCANZABLE (3 saltos) |
| 111 | `definicion_calidad_fitness_for_purpose -> descubrir_necesidades_del_cliente (paso 2)` | ALCANZABLE (4 saltos) |
| 112 | `inventario_conocimiento_estadistico_personal -> roi_proyectos_calidad (paso 4)` | SIN CAMINO PREVIO |
| 113 | `reconocer_mercancia_peligrosa_disfrazada -> clasificar_tipo_paquete (paso 4)` | SIN CAMINO PREVIO |
| 114 | `identificacion_proveedores_criticos -> validacion_externa_reportes (paso 4)` | SIN CAMINO PREVIO |
| 115 | `tipos_de_riesgo_invencion_vs_mercado -> fundadores_lideran_validacion (paso 4)` | ALCANZABLE (3 saltos) |
| 116 | `definicion_y_concepto_de_aseguramiento_de_calidad -> planificacion_inicial_calidad (paso 1)` | SIN CAMINO PREVIO |
| 117 | `definicion_y_concepto_de_aseguramiento_de_calidad -> trilogia_juran_qa_qc (paso 3)` | SIN CAMINO PREVIO |
| 118 | `planificacion_recoleccion_datos -> analisis_pareto_proyectos_elefante (paso 7)` | SIN CAMINO PREVIO |
| 119 | `rol_director_calidad -> circulos_calidad_qc (paso 4)` | SIN CAMINO PREVIO |
| 120 | `establecer_diseno_final_producto -> establecer_metas_caracteristicas (paso 1)` | SIN CAMINO PREVIO |
| 121 | `desarrollo_value_proposition_usp -> posicionamiento_vs_competidores (paso 1)` | SIN CAMINO PREVIO |
| 122 | `motor_crecimiento_pago -> valor_de_vida_del_cliente (paso 1)` | ALCANZABLE (6 saltos) |
| 123 | `constraint_management -> caso_estudio_benchmarking_terminal (paso 4)` | SIN CAMINO PREVIO |
| 124 | `ingenieria_calidad_proveedores -> desarrollar_estrategias_largo_plazo (paso 4)` | SIN CAMINO PREVIO |

## 4. TAREA 4, la vara del tramo 11, instrumento propio

Comando: `python scripts/loop/vuelta86_tarea4_vara_tramo11.py` >
`docs/loop/SALIDA_V86_TAREA4_VARA_TRAMO11.txt`. Pares LEIDOS del fichero del
filtro, no tecleados. Alcance de la adjudicacion 6.5 del acta 84: (4.a) las 30
frescas contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` SIN direccion; (4.b) las
mismas contra `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl` buscando la
reciproca; (4.c) la tabla del PATRON HISTORICO de la TAREA 2.b, pegada
entera.

Cifras del auditor, confirmadas al digito: **3.388 veredictos, 3.388 pares no
dirigidos unicos, 136 unidades en la bolsa filtrada V85.** Sin discrepancia.

**RESUMEN 4.a/4.b: 4 de 30 con veredicto (98, 103, 104, 117, todos clase D), 0
de 30 con reciproca contra la bolsa filtrada V84... V85** (la reciproca se
busca contra la bolsa de la vuelta ANTERIOR, que es la V85, tal como manda la
adjudicacion 6.5 del acta 84). De los 4 con veredicto D, 3 se decidieron
ESCRITA (98, 103, 117) y 1 NO SE ENLAZA (104): cifra de ESTA tanda, sin
compararla contra ninguna otra (adjudicacion 5.5, ver seccion siguiente).

**(4.c) La tabla del PATRON HISTORICO, pegada entera de
`docs/loop/SALIDA_V86_TAREA4_VARA_TRAMO11.txt`:**

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

**RESUMEN POR TRAMO, tallado (pares con veredicto | clase D | ESCRITA | NO SE
ENLAZA):** tramo 3: 7\|7\|7\|0. Tramo 4: 2\|1\|1\|1. Tramo 5: 3\|3\|1\|2.
Tramo 6: 1\|1\|0\|1. Tramo 7: 1\|1\|0\|1. Tramo 8: 2\|2\|0\|2. Tramo 9: 2\|2\|1\|1.
Tramo 10: 3\|3\|2\|1. **Tramo 11: 4\|4\|3\|1.**

**CASO OBLIGATORIO confirmado**: `formulacion_teorias_causa ->
diagrama_causa_efecto` (tramo 9, clase D) sale ESCRITA, el hecho exacto que la
prosa de la vuelta 85 nego.

## LO QUE NO SE ESCRIBE EN PROSA ESTA VUELTA (adjudicacion 5.5)

Ninguna frase de esta vuelta compara el tramo 11 contra "el promedio de
tramos anteriores" ni expresiones parecidas: la marca de discutible no vive
en ningun fichero (salvo la tabla de este mismo reporte, que no es un
instrumento corrido por separado), asi que ese promedio no se puede tallar.
Se publica solo la cifra de esta tanda (8 de 30 SE ESCRIBE, 10 discutibles
segun la tabla) y nada mas.

## 5. La guarda, corrida DESPUES del horneado de cierre, con la definicion nueva

Registro horneado DOS VECES (adjudicacion 6.3 del acta 84): el fichero ya
traia 186 filas con el tramo 10 dentro (horneado de cierre de la vuelta 85),
y el segundo horneado de esta vuelta (`docs/loop/SALIDA_V86_TAREA3_HORNEAR_
CIERRE.txt`, `python scripts/loop/vuelta85_hornear_decididas.py`, maquina sin
cambios, descubre por patron) anade el tramo 11: **216 filas (97 ESCRITA, 119
NO SE ENLAZA)**, 8 filas ASCENDIDAS y 4 DEGRADADAS, las mismas de siempre
(ningun cambio nuevo esta vuelta: las 8 aristas de esta tanda calzan con el
grafo sin ascenso ni degradacion).

Guarda corrida DESPUES de este horneado, con la definicion nueva (TAREA 2.a):
`python scripts/loop/vuelta83_guarda_decididas.py --bolsa docs/plan/PASO_NODO
_CALIBRADO_FILTRADO_V86.jsonl` (`docs/loop/SALIDA_V86_GUARDA_CIERRE.txt`):
**VERDE**, prefijo 0 a 124 (125 unidades), primera unidad SIN DECIDIR el
indice 125, `juran_rcca_metodo -> diseno_implementacion_remedio` (paso 3,
quality). Es exactamente la cabeza del tramo 12: la adjudicacion 6.3 del acta
84 vuelve a cumplirse, esta vez con la definicion que SI reconoce el estado
ESCRITA.

## EL FINAL DE OP-E-01, medido y no descubierto a mitad

Tras el tramo 11 quedan **4 unidades sin decidir** en la bolsa V86 (indices
125 a 128 de `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl`), listadas
por nombre por la guarda de cierre. Salvo que la recalibracion abra unidades
nuevas (cosa que no ha pasado en las tres ultimas vueltas), `OP-E-01` se
consume en la vuelta 87.

## PENDIENTES DE DOCTRINA

Ninguno esta vuelta. Las cuatro piezas de la TAREA 2 estaban las cuatro
adjudicadas por el acta 85 sin doctrina nueva, y la lectura del tramo 11 no
encontro ninguna pregunta que la doctrina vigente (banco 9.6, 9.6.1, 9.6.2,
9.6.3, 9.8, 9.9) no contestara.

## REPASO PUNTO POR PUNTO DEL ENCARGO, antes de cerrar

- Commitear y pushear lo pendiente antes de tocar nada: SI, working tree
  estaba limpio al abrir (verificado con `git status`).
- TAREA 1, registros y correccion declarada: SI, seccion 1.
- TAREA 2, el instrumento, BLOQUEANTE, cuatro piezas, commit propio ANTES del
  filtro: SI, commit `d13a951a`, pusheado antes de correr el filtro del
  tramo 11.
- TAREA 3, tramo 11 leido POR LO NO DECIDIDO, bolsa fresca, filtro/guarda/
  cadena ANTES de leer, 30 unidades, discutibles marcados, varas de contraste
  del auditor confirmadas: SI, seccion 3.
- TAREA 4, vara del tramo 11 con instrumento propio, pares leidos del
  fichero del filtro, alcance 6.5 del acta 84, cifras del auditor
  confirmadas: SI, seccion 4.
- Lo que no se escribe en prosa (comparaciones sin cifra): SI, respetado.
- Cabecera tallada con `--fase04 --vuelta 86`, pegada entera, `--comparar`
  contra este mismo reporte antes del commit de cierre: pendiente de correr
  tras escribir este fichero (se corre a continuacion y su salida se cita).
- `--comparar` del tramo 11 contra este reporte, cabecera y tabla de la
  cadena identicas, EXIT 0: pendiente de correr tras escribir este fichero
  (se corre a continuacion y su salida se cita).
- Sello del HEAD de apertura antes de la primera operacion: SI,
  `docs/loop/SALIDA_V86_HEAD_APERTURA.txt`.
- Hornear el registro dos veces, guarda corrida despues del segundo con la
  definicion nueva: SI, secciones 3 y 5.
- Cero guiones largos ni medios: repasado a mano en este fichero.

## DISCUTIBLES, listados para la relectura ciega del auditor

Contados de la columna DISCUTIBLE de la tabla de la seccion 3, DIEZ:
**95, 97, 100, 104, 106, 107, 108, 111, 119, 121.**
