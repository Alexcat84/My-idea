# Cola intra-dominio: pares del mismo dominio para leer

**ESTE INSTRUMENTO EMPAREJA, NO JUZGA.** El veredicto de cada par es **lectura textual** del auditor con visto del fundador. **Un par en esta lista es una cita para leer, no un duplicado.**

Es el otro eje del mismo trabajo: `scripts/gradiente_pares.py` empareja **mundo contra nucleo**, y este empareja **cada dominio contra si mismo**, que es donde viven los racimos. Los conteos de pasos **solo ordenan la cola**; la profundidad y la duplicacion se adjudican leyendo, jamas contando.

## Como se emparejo

Dos senales independientes, y basta con que dispare **cualquiera**:

- **titulo**: `token_sort_ratio` de rapidfuzz, umbral **80**
- **semantica**: coseno sobre `semantic_index.json`, umbral **0.78**

Cada par reporta **las dos**, aunque solo una haya disparado.

**El umbral semantico es 0.78 y no el 0,75 del gradiente a proposito.** Dentro de un dominio la vecindad tematica es **la norma, no la senal**: dos nodos de `quality` hablan de calidad por definicion. La distribucion por dominio esta mas abajo **para que el umbral se pueda recalibrar con datos antes de leer**, no despues.

## La calibracion conocida

**CAZADO.** El par `descubrir_necesidades_cliente` contra `descubrir_necesidades_del_cliente` (los dos en `quality`) esta en la cola: similitud de titulo **87.8**, semantica **0.8102** (disparo por titulo: True, por semantica: True).

## Conteos

**3388 pares** en la cola, sobre **3521 nodos activos** repartidos en **10 dominios**.

| dominio | nodos | pares posibles | en la cola | % de los posibles |
|---|---:|---:|---:|---:|
| compras | 46 | 1035 | **155** | 14.98% |
| core | 1618 | 1308153 | **1445** | 0.11% |
| entrega | 47 | 1081 | **171** | 15.82% |
| environmental | 289 | 41616 | **170** | 0.41% |
| exportacion | 141 | 9870 | **130** | 1.32% |
| franquicias | 195 | 18915 | **148** | 0.78% |
| health_safety | 283 | 39903 | **192** | 0.48% |
| quality | 792 | 313236 | **844** | 0.27% |
| risk_management | 55 | 1485 | **106** | 7.14% |
| seguridad_digital | 55 | 1485 | **27** | 1.82% |

## Nuevos contra re-avistados

**El instrumento conoce el trabajo hecho.** Nada se excluye por estar ya visto: se MARCA, con su fuente, y la cola dice que es nuevo y que no.

| estado | pares | que significa |
|---|---:|---|
| **nuevo** | **2669** | ni el par ni sus dos nodos aparecen en lo ya escrito |
| nodo ya avistado | 506 | alguno de los dos nodos ya fue leido en otro par; **el par en si es nuevo** |
| re-avistado | 213 | **el par exacto** ya esta adjudicado o censado |

Fuentes de las marcas, con lo que aporto cada una:

| fuente | entradas |
|---|---:|
| `racimos_miembros_32_nominas` | 32 racimos, 569 parejas |
| `informe_4_4_ids_casi_identicos` | 19 |
| `informe_4_3_base_mas_2` | 9 |
| `informe_4_2_crosby_duplicados` | 7 |
| `ficha_36_parejas_de_sufijo` | 36 |
| `ficha_citas_intra_dominio_nodos` | 67 |

> **HUECO CERRADO.** En la primera corrida solo dos de los 32 racimos tenian nomina escrita y el resumen declaraba la columna de re-avistados como subestimada. **Ya no**: `docs/RACIMOS_MIEMBROS.jsonl` tiene **las 32 nominas completas**, reconstruidas de las razones de los veredictos del cribado, y **las 32 cuadran con su tamano censado**. Cada par cuyos dos nodos pertenecen al mismo racimo entra ya como re-avistado.

## Recall contra lo declarado, que es el dato duro de calibracion

**Las parejas ya escritas en los documentos son la unica verdad conocida que existe para este eje.** Si el instrumento no las caza, la cola tiene agujeros, y eso hay que saberlo ANTES de leerla, no despues.

| | |
|---|---:|
| parejas declaradas que son **intra-dominio** | **596** |
| de esas, **cazadas** por la cola | **213** |
| **perdidas** | **383** |
| **recall** | **36%** |

(22 parejas declaradas mas **cruzan dominio** y por definicion no le tocan a este instrumento: `activacion_lista_positiva` con `diseno_para_sostenibilidad_cradle_to_cradle`, `analisis_flujo_de_valor` con `lean_manufacturing`, `analisis_flujo_de_valor` con `mapeo_flujo_valor`, `analisis_flujo_de_valor` con `ocho_desperdicios_lean`, `analisis_flujo_de_valor` con `value_stream_mapping_ambiental`, `brainstorming` con `brainstorming_divergente`, `brainstorming` con `brainstorming_efectivo`, `brainstorming` con `reglas_brainstorming`, `cradle_to_cradle_concepto` con `diseno_para_sostenibilidad_cradle_to_cradle`, `critica_eco_eficiencia` con `diseno_para_sostenibilidad_cradle_to_cradle`, `desperdicio_es_alimento` con `diseno_para_sostenibilidad_cradle_to_cradle`, `diseno_para_sostenibilidad_cradle_to_cradle` con `eco_efectividad`, `diseno_para_sostenibilidad_cradle_to_cradle` con `eco_efectividad_2`, `diseno_para_sostenibilidad_cradle_to_cradle` con `eco_efectividad_re_evolucion_industrial`, `diseno_para_sostenibilidad_cradle_to_cradle` con `materiales_ciclicos_infinitamente_reciclables`, `diseno_para_sostenibilidad_cradle_to_cradle` con `modelo_cradle_to_grave`, `diseno_para_sostenibilidad_cradle_to_cradle` con `nutrientes_biologicos`, `lean_manufacturing` con `value_stream_mapping_ambiental`, `mapeo_flujo_valor` con `value_stream_mapping_ambiental`, `ocho_desperdicios_lean` con `value_stream_mapping_ambiental`, `proteccion_propiedad_intelectual` con `proteccion_propiedad_intelectual_2`, `seleccion_canal_distribucion` con `seleccion_canales_distribucion`.)

**Las 383 perdidas, con sus dos senales**, para que se vea cuanto falta y no cuanto se cree que falta:

| dominio | pareja | titulo | semantica | de donde viene la marca |
|---|---|---:|---:|---|
| quality | `control_mantener_ganancias` con `matriz_de_control_de_proceso` | 44.4 | 0.7797 | racimo censado: Plan y matriz de control (cribado) |
| quality | `design_for_six_sigma_dmadv` con `design_for_six_sigma_dmadv_2` | 61.1 | 0.7795 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `desajuste_tarea_persona` con `enfoque_situacional_vs_personal` | 40.4 | 0.7794 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_comunes_especiales` con `mejora_del_sistema_responsabilidad_gerencial` | 36.0 | 0.779 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| core | `curse_cinco_culpas` con `five_whys_inversion_proporcional` | 35.1 | 0.7785 | racimo censado: Los cinco porques (cribado) |
| franquicias | `velocidad_crecimiento_franquicia` con `velocidad_crecimiento_franquicia_2` | 43.9 | 0.7783 | ficha, las 36 parejas de sufijo vivo |
| core | `encuadre_desafio_diseno` con `how_might_we_hmw` | 28.8 | 0.7778 | racimo censado: Encuadre del problema (How Might We) (cribado) |
| quality | `benchmarking_proceso` con `rol_alta_direccion_benchmarking` | 48.6 | 0.7773 | racimo censado: Benchmarking (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `new_view_human_error` | 37.5 | 0.7773 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `human_error_como_sintoma` | 30.4 | 0.7772 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `desperdicio_es_alimento` con `nutrientes_biologicos` | 33.3 | 0.7772 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `human_error_como_sintoma` con `principios_gestion_error` | 35.8 | 0.7772 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `establecer_estandares_desempeno` con `establecer_metas_de_calidad_basadas_en_mercado` | 43.2 | 0.7762 | racimo censado: Metas de calidad (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `human_error_como_sintoma` | 28.6 | 0.776 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `accion_correctiva_2` con `accion_correctiva_crosby` | 57.5 | 0.7759 | racimo censado: Accion correctiva (cribado) |
| health_safety | `ciclo_de_culpa` con `responsabilidad_sistemica` | 41.1 | 0.7758 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `customer_development_modelo` con `customer_discovery_phase2_problem_test` | 41.4 | 0.7758 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| quality | `causas_comunes_vs_especiales` con `sistema_estable_causas_comunes` | 46.6 | 0.7754 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `estructura_competencias_six_sigma_lean` con `rol_black_belt_six_sigma` | 40.3 | 0.7744 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `gestion_efectiva_benchmarking` con `monitoreo_continuo_benchmarking` | 47.1 | 0.774 | racimo censado: Benchmarking (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `new_view_human_error` | 36.6 | 0.7739 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `responsabilidad_prospectiva` | 36.4 | 0.7737 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `responsabilidad_gerencial_causas_comunes` con `sistema_estable_responsabilidad_gerencial` | 40.3 | 0.7737 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `principios_auditoria_calidad` con `programa_auditoria_calidad` | 62.7 | 0.7736 | racimo censado: Auditoria de calidad (cribado) |
| quality | `monitoreo_continuo_benchmarking` con `rol_alta_direccion_benchmarking` | 49.2 | 0.7731 | racimo censado: Benchmarking (cribado) |
| quality | `distincion_causas_comunes_especiales` con `moral_y_sistema_no_individuo` | 34.3 | 0.773 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| core | `pivotar_o_perseverar` con `reunion_pivotar_o_perseverar` | 72.6 | 0.7728 | racimo censado: Pivotar o proceder (cribado) |
| core | `how_might_we_briefs` con `how_might_we_framing` | 48.6 | 0.7718 | racimo censado: Encuadre del problema (How Might We) (cribado) |
| quality | `distincion_causas_especiales_comunes` con `mejora_del_sistema_responsabilidad_gerencial` | 39.3 | 0.7714 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `principios_gestion_error` | 33.7 | 0.7714 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `ciclo_de_culpa` | 43.2 | 0.7713 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `moral_y_sistema_no_individuo` con `responsabilidad_gerencial_causas_comunes` | 37.1 | 0.7712 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `distincion_causas_especiales_comunes` con `responsabilidad_gerencial_causas_comunes` | 47.1 | 0.7701 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `analisis_causa_raiz_diagnostico` con `juran_rcca_metodo` | 60.0 | 0.77 | racimo censado: Analisis de causa raiz (cribado) |
| health_safety | `new_view_human_error` con `responsabilidad_sistemica` | 31.3 | 0.7697 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `auditoria_calidad` con `principios_auditoria_calidad` | 61.8 | 0.7694 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `falla_sistemica_vs_error_individual` | 35.9 | 0.7691 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `falla_sistemica_vs_error_individual` | 39.6 | 0.7689 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `programa_make_certain` con `programa_make_certain_2` | 47.5 | 0.7679 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `bad_apple_theory` con `errores_como_consecuencia` | 29.5 | 0.7676 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_comunes_especiales_2` con `politica_no_culpar_trabajador` | 35.6 | 0.7674 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `distincion_causas_especiales_comunes` con `sistema_estable_causas_comunes` | 42.0 | 0.7674 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| core | `pivotar_o_perseverar` con `pivotar_o_proceder` | 68.9 | 0.7667 | racimo censado: Pivotar o proceder (cribado) |
| quality | `estructura_competencias_six_sigma_lean` con `rol_black_belt` | 49.6 | 0.7664 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `sistema_estable_responsabilidad_gerencial` con `sistema_responsabilidad_gerencial` | 39.6 | 0.7663 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `causas_comunes_vs_especiales` con `mejora_del_sistema_responsabilidad_gerencial` | 37.4 | 0.7654 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `politica_no_culpar_trabajador` con `sistema_responsabilidad_gerencial_2` | 41.5 | 0.7654 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `analisis_diagnostico_causa` con `juran_rcca_metodo` | 66.7 | 0.7622 | racimo censado: Analisis de causa raiz (cribado) |
| health_safety | `bad_apple_theory` con `enfoque_situacional_vs_personal` | 34.6 | 0.762 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `causas_comunes_vs_especiales` con `sistema_responsabilidad_gerencial` | 32.5 | 0.7619 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| core | `objetivos_de_llamada_orientados_a_avance` con `obtencion_de_compromiso` | 38.8 | 0.7613 | racimo censado: El avance y el compromiso en la venta (cribado) |
| health_safety | `errores_como_consecuencia` con `revision_de_aprendizaje` | 28.9 | 0.7612 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `lean_manufacturing` con `ocho_desperdicios_lean` | 37.2 | 0.7603 | racimo censado: Mapeo del flujo de valor (cribado) |
| environmental | `diversidad_en_diseno` con `respeto_a_la_diversidad` | 57.5 | 0.7601 | racimo censado: Diversidad en el diseno (cribado) |
| core | `gestion_de_portafolio_gates_go_kill` con `pruning_portafolio` | 46.9 | 0.7599 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| quality | `definiciones_operacionales` con `definiciones_operacionales_3` | 61.0 | 0.7592 | ficha, las 36 parejas de sufijo vivo |
| environmental | `critica_eco_eficiencia` con `eco_efectividad_2` | 25.6 | 0.7591 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `bad_apple_theory` con `responsabilidad_sistemica` | 38.1 | 0.7586 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `errores_como_consecuencia` | 32.2 | 0.7585 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `customer_discovery_cuatro_fases` con `customer_discovery_get_out_of_building` | 40.0 | 0.7585 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `responsabilidad_sistemica` | 41.2 | 0.7585 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `principios_gestion_error` con `revision_de_aprendizaje` | 38.4 | 0.7584 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `rol_black_belt` con `rol_green_belt_six_sigma` | 41.3 | 0.7579 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `abandonar_arreglos_rapidos` con `bad_apple_theory` | 44.2 | 0.7576 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `cradle_to_cradle_concepto` con `eco_efectividad` | 32.9 | 0.7569 | racimo censado: Cradle to cradle (cribado) |
| quality | `validacion_sistema_medicion` con `validacion_sistema_medicion_2` | 65.0 | 0.756 | ficha, las 36 parejas de sufijo vivo |
| quality | `accion_correctiva_2` con `accion_correctiva_sistematica` | 52.5 | 0.7558 | racimo censado: Accion correctiva (cribado) |
| health_safety | `responsabilidad_prospectiva` con `responsabilizacion_del_trabajador` | 52.3 | 0.7547 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `responsabilidad_sistemica` | 41.2 | 0.7545 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `how_might_we_brief_social` con `how_might_we_hmw` | 33.3 | 0.7543 | racimo censado: Encuadre del problema (How Might We) (cribado) |
| quality | `accion_correctiva` con `accion_correctiva_2` | 54.3 | 0.7542 | racimo censado: Accion correctiva (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `new_view_human_error` | 34.4 | 0.754 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `responsabilidad_sistemica` | 45.2 | 0.754 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_especiales_comunes` con `politica_no_culpar_trabajador` | 33.3 | 0.7536 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `responsabilidad_prospectiva` | 35.0 | 0.7533 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `falla_sistemica_vs_error_individual` | 30.2 | 0.7533 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `mejora_del_sistema_responsabilidad_gerencial` con `politica_no_culpar_trabajador` | 45.2 | 0.7533 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `analisis_causa_raiz_defectos` con `analisis_causa_raiz_diagnostico` | 55.0 | 0.7527 | racimo censado: Analisis de causa raiz (cribado) |
| environmental | `cradle_to_cradle_concepto` con `modelo_cradle_to_grave` | 36.1 | 0.7525 | racimo censado: Cradle to cradle (cribado) |
| core | `curse_cinco_culpas` con `regla_simplificada_tolerancia_errores` | 41.1 | 0.7524 | racimo censado: Los cinco porques (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `preguntar_que_no_quien` | 41.6 | 0.7522 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `critica_eco_eficiencia` con `eco_efectividad` | 33.6 | 0.7511 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `revision_de_aprendizaje` | 39.6 | 0.7507 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `pruning_portafolio` con `revision_portafolio_periodica` | 39.6 | 0.7505 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| quality | `estructura_competencias_six_sigma_lean` con `rol_green_belt_six_sigma` | 36.4 | 0.7502 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `entrenamiento_para_breakthrough` con `rol_black_belt_six_sigma` | 43.0 | 0.75 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `new_view_investigation` con `responsabilidad_sistemica` | 31.8 | 0.7494 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `ciclo_de_mejora_continua_helix` con `ciclo_shewhart_pdsa` | 60.0 | 0.749 | racimo censado: Ciclo de mejora PDCA / PDSA (cribado) |
| quality | `causas_comunes_vs_especiales` con `politica_no_culpar_trabajador` | 40.8 | 0.7478 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `responsabilidad_sistemica` con `responsabilizacion_del_trabajador` | 39.2 | 0.7477 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `portfolio_management` con `revision_portafolio_periodica` | 56.5 | 0.747 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| quality | `distincion_causas_comunes_especiales_2` con `sistema_responsabilidad_gerencial_2` | 31.3 | 0.7467 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `desarrollo_expertos_capaces` con `entrenamiento_para_breakthrough` | 38.2 | 0.7464 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `distincion_causas_comunes_especiales_2` con `sistema_estable_causas_comunes` | 43.4 | 0.7464 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `human_error_como_sintoma` | 25.3 | 0.7454 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `objetivos_de_llamada_orientados_a_avance` con `obtencion_compromiso_venta` | 39.7 | 0.7453 | racimo censado: El avance y el compromiso en la venta (cribado) |
| health_safety | `human_error_como_sintoma` con `new_view_investigation` | 21.3 | 0.7451 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `preguntar_que_no_quien` | 31.3 | 0.7448 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `desajuste_tarea_persona` | 40.4 | 0.7448 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `benchmarking_proceso` con `gestion_efectiva_benchmarking` | 54.3 | 0.7443 | racimo censado: Benchmarking (cribado) |
| health_safety | `ciclo_de_culpa` con `errores_como_consecuencia` | 35.1 | 0.7436 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `activacion_lista_positiva` con `materiales_ciclicos_infinitamente_reciclables` | 37.4 | 0.7433 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `new_view_human_error` con `revision_de_aprendizaje` | 29.7 | 0.7433 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_especiales_comunes` con `sistema_estable_responsabilidad_gerencial` | 36.4 | 0.7431 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `principios_gestion_error` | 42.7 | 0.7421 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `errores_como_consecuencia` con `responsabilizacion_del_trabajador` | 34.6 | 0.7419 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `responsabilizacion_del_trabajador` | 38.8 | 0.7416 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `desperdicio_es_alimento` con `eco_efectividad` | 29.3 | 0.7415 | racimo censado: Cradle to cradle (cribado) |
| core | `objetivos_de_llamada_orientados_a_avance` con `obtencion_compromiso` | 34.4 | 0.7415 | racimo censado: El avance y el compromiso en la venta (cribado) |
| health_safety | `ciclo_de_culpa` con `revision_de_aprendizaje` | 38.8 | 0.7414 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `preguntar_que_no_quien` con `principios_gestion_error` | 27.7 | 0.7412 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `auditoria_calidad` con `estructuracion_programa_auditoria` | 41.4 | 0.7411 | racimo censado: Auditoria de calidad (cribado) |
| quality | `clasificacion_caracteristicas_calidad` con `clasificacion_de_seriedad_de_defectos` | 52.6 | 0.7411 | racimo censado: Clasificacion de defectos (cribado) |
| core | `advances_vs_continuations` con `obtencion_compromiso` | 32.7 | 0.7403 | racimo censado: El avance y el compromiso en la venta (cribado) |
| core | `encuadre_desafio_diseno` con `how_might_we_briefs` | 38.0 | 0.7401 | racimo censado: Encuadre del problema (How Might We) (cribado) |
| health_safety | `principios_gestion_error` con `responsabilidad_prospectiva` | 31.6 | 0.7394 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `estructuracion_programa_auditoria` con `principios_auditoria_calidad` | 32.7 | 0.7389 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `responsabilizacion_del_trabajador` | 35.2 | 0.7383 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `estructuracion_programa_auditoria` con `programa_auditoria_calidad` | 45.5 | 0.738 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `human_error_como_sintoma` con `revision_de_aprendizaje` | 27.7 | 0.738 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `politica_no_culpar_trabajador` con `sistema_estable_causas_comunes` | 43.8 | 0.7366 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `cultura_justa` con `cultura_justa_3` | 50.6 | 0.7365 | ficha, las 36 parejas de sufijo vivo |
| quality | `desarrollar_caracteristicas_proceso` con `desarrollar_caracteristicas_proceso_2` | 44.0 | 0.7365 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `new_view_human_error` con `preguntar_que_no_quien` | 29.0 | 0.7365 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `regla_simplificada_tolerancia_errores` con `tecnica_cinco_porques` | 22.7 | 0.736 | racimo censado: Los cinco porques (cribado) |
| environmental | `activacion_lista_positiva` con `desperdicio_es_alimento` | 35.7 | 0.7357 | racimo censado: Cradle to cradle (cribado) |
| core | `advances_vs_continuations` con `obtencion_compromiso_venta` | 45.7 | 0.7357 | racimo censado: El avance y el compromiso en la venta (cribado) |
| health_safety | `errores_como_consecuencia` con `responsabilidad_sistemica` | 28.3 | 0.7357 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `rol_black_belt` con `rol_facilitador_black_belt` | 44.6 | 0.7356 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| core | `customer_discovery_get_out_of_building` con `customer_discovery_phase2_problem_test` | 57.4 | 0.7352 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `new_view_investigation` | 26.1 | 0.7347 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `activacion_lista_positiva` con `eco_efectividad` | 35.3 | 0.7344 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `bad_apple_theory` con `principios_gestion_error` | 41.2 | 0.7342 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `gestion_portafolio_dos_niveles` con `pruning_portafolio` | 48.8 | 0.7338 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| core | `how_might_we_brief_social` con `how_might_we_framing` | 36.0 | 0.7337 | racimo censado: Encuadre del problema (How Might We) (cribado) |
| health_safety | `defensas_en_profundidad` con `defensas_en_profundidad_3` | 61.0 | 0.7335 | ficha, las 36 parejas de sufijo vivo |
| core | `gestion_de_portafolio_gates_go_kill` con `gestion_portafolio_dos_niveles` | 63.5 | 0.7333 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| quality | `mapeo_flujo_valor` con `ocho_desperdicios_lean` | 36.0 | 0.7333 | racimo censado: Mapeo del flujo de valor (cribado) |
| core | `decision_pivotar_o_proceder` con `pivotar_o_perseverar` | 34.1 | 0.7329 | racimo censado: Pivotar o proceder (cribado) |
| core | `customer_discovery` con `customer_discovery_get_out_of_building` | 62.1 | 0.7324 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| environmental | `desperdicio_es_alimento` con `materiales_ciclicos_infinitamente_reciclables` | 35.0 | 0.7314 | racimo censado: Cradle to cradle (cribado) |
| core | `actualizar_modelo_de_negocio_pivot_o_proceed` con `reunion_pivotar_o_perseverar` | 41.6 | 0.7311 | racimo censado: Pivotar o proceder (cribado) |
| quality | `entrenamiento_para_breakthrough` con `estructura_competencias_six_sigma_lean` | 42.5 | 0.7306 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| environmental | `desperdicio_es_alimento` con `eco_efectividad_re_evolucion_industrial` | 28.9 | 0.729 | racimo censado: Cradle to cradle (cribado) |
| environmental | `cradle_to_cradle_concepto` con `materiales_ciclicos_infinitamente_reciclables` | 29.8 | 0.7279 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `human_error_como_sintoma` con `preguntar_que_no_quien` | 24.7 | 0.7276 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `principios_gestion_error` con `responsabilizacion_del_trabajador` | 32.6 | 0.7275 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `preguntar_que_no_quien` con `responsabilizacion_del_trabajador` | 31.0 | 0.7271 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `errores_como_consecuencia` | 28.9 | 0.7265 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `decision_pivotar_o_proceder` con `reunion_pivotar_o_perseverar` | 29.4 | 0.7263 | racimo censado: Pivotar o proceder (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `rendicion_cuentas_prospectiva` | 31.3 | 0.7261 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `gestion_de_errores` con `new_view_human_error` | 41.8 | 0.7256 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `rendicion_cuentas_prospectiva` con `responsabilizacion_del_trabajador` | 39.8 | 0.7254 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `falla_sistemica_vs_error_individual` | 31.8 | 0.725 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `responsabilidad_prospectiva` | 46.7 | 0.7242 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `entrenamiento_para_breakthrough` con `rol_black_belt` | 53.2 | 0.724 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `causas_comunes_vs_especiales` con `sistema_responsabilidad_gerencial_2` | 32.5 | 0.7238 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| core | `gestion_de_portafolio_gates_go_kill` con `revision_portafolio_periodica` | 34.9 | 0.7233 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| quality | `benchmarking_7_pasos_juran` con `rol_alta_direccion_benchmarking` | 58.5 | 0.7232 | racimo censado: Benchmarking (cribado) |
| health_safety | `desajuste_tarea_persona` con `responsabilizacion_del_trabajador` | 29.9 | 0.7231 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_comunes_especiales_2` con `sistema_estable_responsabilidad_gerencial` | 30.8 | 0.7229 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `certificacion_belts_six_sigma` con `entrenamiento_para_breakthrough` | 33.0 | 0.7227 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| core | `customer_development_vs_business_plan` con `customer_discovery_cuatro_fases` | 37.5 | 0.7221 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| quality | `accion_correctiva_2` con `accion_correctiva_4` | 49.4 | 0.7218 | racimo censado: Accion correctiva (cribado) |
| core | `encuadre_desafio_diseno` con `how_might_we_brief_social` | 41.5 | 0.7218 | racimo censado: Encuadre del problema (How Might We) (cribado) |
| quality | `accion_correctiva` con `accion_correctiva_4` | 62.7 | 0.7215 | racimo censado: Accion correctiva (cribado) |
| quality | `politica_no_culpar_trabajador` con `sistema_responsabilidad_gerencial` | 39.0 | 0.7209 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `auditoria_calidad` con `reporte_auditoria` | 53.9 | 0.7207 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `desajuste_tarea_persona` con `principios_gestion_error` | 32.6 | 0.7207 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `curse_cinco_culpas` con `tecnica_cinco_porques` | 41.5 | 0.72 | racimo censado: Los cinco porques (cribado) |
| core | `customer_development_modelo` con `customer_development_vs_business_plan` | 35.5 | 0.72 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| health_safety | `errores_como_consecuencia` con `new_view_investigation` | 25.6 | 0.7197 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `gestion_portafolio_dos_niveles` con `gestion_portafolio_foco` | 61.9 | 0.7194 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| quality | `distincion_causas_comunes_especiales` con `sistema_responsabilidad_gerencial` | 31.5 | 0.7191 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| environmental | `critica_eco_eficiencia` con `desperdicio_es_alimento` | 32.5 | 0.7187 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `gestion_de_errores` con `responsabilidad_prospectiva` | 32.1 | 0.7183 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `principios_gestion_error` | 36.4 | 0.7182 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `adopcion_liderazgo` con `eliminar_slogans_metas` | 41.2 | 0.718 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| health_safety | `ciclo_de_culpa` con `responsabilidad_prospectiva` | 42.5 | 0.718 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `advances_vs_continuations` con `obtencion_de_compromiso` | 45.6 | 0.7175 | racimo censado: El avance y el compromiso en la venta (cribado) |
| health_safety | `new_view_investigation` con `preguntar_que_no_quien` | 32.4 | 0.717 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `cultura_justa` con `cultura_justa_2` | 40.4 | 0.7169 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `human_error_como_sintoma` con `responsabilidad_sistemica` | 31.1 | 0.7166 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_comunes_especiales` con `sistema_responsabilidad_gerencial_2` | 31.5 | 0.7164 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `distincion_causas_comunes_especiales_2` con `sistema_responsabilidad_gerencial` | 36.1 | 0.7155 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `gestion_de_errores` con `human_error_como_sintoma` | 34.5 | 0.7155 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `causas_comunes_vs_especiales` con `sistema_estable_responsabilidad_gerencial` | 31.5 | 0.7152 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| environmental | `critica_eco_eficiencia` con `eco_efectividad_re_evolucion_industrial` | 38.3 | 0.7152 | racimo censado: Cradle to cradle (cribado) |
| core | `actualizar_modelo_de_negocio_pivot_o_proceed` con `decision_pivotar_o_proceder` | 22.9 | 0.715 | racimo censado: Pivotar o proceder (cribado) |
| health_safety | `principios_gestion_error` con `responsabilidad_sistemica` | 38.9 | 0.7137 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `enfoque_situacional_vs_personal` | 39.6 | 0.7132 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `estructuracion_programa_auditoria` con `reporte_auditoria` | 40.0 | 0.7132 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `errores_como_consecuencia` con `gestion_de_errores` | 31.1 | 0.7127 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `desajuste_autoridad_responsabilidad` | 36.6 | 0.7126 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `responsabilizacion_del_trabajador` con `revision_de_aprendizaje` | 31.3 | 0.7126 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_especiales_comunes` con `sistema_responsabilidad_gerencial_2` | 29.2 | 0.7118 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `ciclo_de_mejora_continua_helix` con `pdsa_shewhart_cycle` | 26.8 | 0.7109 | racimo censado: Ciclo de mejora PDCA / PDSA (cribado) |
| quality | `fomento_educacion_autoeducacion` con `institucionalizar_capacitacion` | 57.8 | 0.7105 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| environmental | `activacion_lista_positiva` con `eco_efectividad_2` | 32.1 | 0.7101 | racimo censado: Cradle to cradle (cribado) |
| quality | `benchmarking_7_pasos_juran` con `gestion_efectiva_benchmarking` | 53.9 | 0.7101 | racimo censado: Benchmarking (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `enfoque_situacional_vs_personal` | 42.0 | 0.7101 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `principios_gestion_error` | 32.3 | 0.709 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `definiciones_operacionales` con `definiciones_operacionales_4` | 42.1 | 0.7087 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `responsabilidad_sistemica` con `revision_de_aprendizaje` | 35.5 | 0.7083 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `mejora_del_sistema_responsabilidad_gerencial` con `moral_y_sistema_no_individuo` | 37.6 | 0.7082 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `preguntar_que_no_quien` | 32.3 | 0.7079 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `rendicion_cuentas_prospectiva` | 36.8 | 0.7069 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `new_view_human_error` | 32.4 | 0.7063 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `distincion_causas_comunes_especiales_2` con `moral_y_sistema_no_individuo` | 34.4 | 0.7063 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `adopcion_liderazgo` con `institucionalizar_capacitacion` | 62.3 | 0.7062 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `politica_no_culpar_trabajador` con `sistema_estable_responsabilidad_gerencial` | 29.5 | 0.7052 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `rol_facilitador_black_belt` con `roles_six_sigma` | 34.8 | 0.705 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| core | `cinco_porques_master` con `five_whys_inversion_proporcional` | 57.1 | 0.7044 | racimo censado: Los cinco porques (cribado) |
| health_safety | `new_view_investigation` con `principios_gestion_error` | 32.5 | 0.7041 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `principios_auditoria_calidad` con `reporte_auditoria` | 52.8 | 0.704 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `new_view_human_error` con `responsabilizacion_del_trabajador` | 25.5 | 0.7037 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `gestion_de_errores` | 29.6 | 0.7033 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `rendicion_cuentas_prospectiva` | 33.6 | 0.7028 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `preguntar_que_no_quien` | 34.9 | 0.7026 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `entrenamiento_para_breakthrough` con `roles_six_sigma` | 36.5 | 0.7026 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `distincion_causas_especiales_comunes` con `sistema_responsabilidad_gerencial` | 33.3 | 0.7025 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `falla_sistemica_vs_error_individual` | 24.7 | 0.7006 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `desajuste_tarea_persona` | 27.2 | 0.7002 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `human_error_como_sintoma` con `responsabilizacion_del_trabajador` | 32.3 | 0.7001 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `responsabilidad_prospectiva` con `responsabilidad_sistemica` | 49.2 | 0.6997 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `errores_como_consecuencia` con `responsabilidad_prospectiva` | 28.6 | 0.6996 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `gestion_de_errores` | 34.6 | 0.6994 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `revision_de_aprendizaje` | 34.1 | 0.6993 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `gestion_portafolio_foco` con `gestion_portafolio_formal` | 62.0 | 0.6988 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| environmental | `cradle_to_cradle_concepto` con `critica_eco_eficiencia` | 29.6 | 0.6984 | racimo censado: Cradle to cradle (cribado) |
| quality | `distincion_causas_especiales_comunes` con `moral_y_sistema_no_individuo` | 35.8 | 0.6976 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `responsabilidad_sistemica` | 42.0 | 0.6975 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `new_view_investigation` | 28.6 | 0.6974 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `responsabilizacion_del_trabajador` | 33.9 | 0.697 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `new_view_investigation` | 35.4 | 0.6967 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `new_view_investigation` | 36.8 | 0.6954 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `cradle_to_cradle_concepto` con `eco_efectividad_re_evolucion_industrial` | 32.1 | 0.6948 | racimo censado: Cradle to cradle (cribado) |
| core | `cinco_porques_master` con `curse_cinco_culpas` | 40.9 | 0.6931 | racimo censado: Los cinco porques (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `rendicion_cuentas_prospectiva` | 36.1 | 0.6924 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `errores_como_consecuencia` | 26.4 | 0.6919 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `adopcion_liderazgo` con `eliminar_miedo` | 55.1 | 0.6894 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `moral_y_sistema_no_individuo` con `sistema_estable_responsabilidad_gerencial` | 34.7 | 0.6891 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| quality | `certificacion_belts_six_sigma` con `rol_green_belt_six_sigma` | 40.4 | 0.6888 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `ciclo_de_culpa` con `human_error_como_sintoma` | 34.0 | 0.6886 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `materiales_ciclicos_infinitamente_reciclables` con `nutrientes_biologicos` | 35.6 | 0.6886 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `new_view_human_error` con `responsabilidad_prospectiva` | 27.0 | 0.6884 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `new_view_investigation` con `rendicion_cuentas_prospectiva` | 26.4 | 0.6881 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `preguntar_que_no_quien` | 30.8 | 0.6877 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `causas_comunes_vs_especiales` con `moral_y_sistema_no_individuo` | 33.3 | 0.6865 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `preguntar_que_no_quien` | 32.2 | 0.686 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `gestion_portafolio_foco` con `revision_portafolio_periodica` | 38.9 | 0.6848 | racimo censado: Portafolio: revisar, podar, reasignar (cribado) |
| environmental | `critica_eco_eficiencia` con `modelo_cradle_to_grave` | 39.3 | 0.6841 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `rendicion_cuentas_prospectiva` con `responsabilidad_sistemica` | 29.9 | 0.684 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `desarrollo_expertos_capaces` con `estructura_competencias_six_sigma_lean` | 36.4 | 0.6836 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `concepto_de_auditoria_de_calidad` con `principios_auditoria_calidad` | 65.5 | 0.6835 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `desajuste_tarea_persona` con `responsabilidad_prospectiva` | 39.6 | 0.6834 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `cradle_to_cradle_concepto` con `nutrientes_biologicos` | 32.1 | 0.6831 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `new_view_investigation` con `process_tracing_methods` | 33.3 | 0.6826 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `eco_efectividad_2` con `modelo_cradle_to_grave` | 16.4 | 0.6824 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `preguntar_que_no_quien` | 24.1 | 0.682 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `gestion_de_errores` con `revision_de_aprendizaje` | 35.2 | 0.682 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `eco_efectividad` con `modelo_cradle_to_grave` | 31.7 | 0.6813 | racimo censado: Cradle to cradle (cribado) |
| environmental | `materiales_ciclicos_infinitamente_reciclables` con `modelo_cradle_to_grave` | 31.1 | 0.6809 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `bad_apple_theory` con `gestion_de_errores` | 31.5 | 0.68 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `new_view_human_error` con `rendicion_cuentas_prospectiva` | 23.8 | 0.6799 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `gestion_de_errores` | 40.5 | 0.6787 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `actualizar_modelo_de_negocio_pivot_o_proceed` con `pivotar_o_perseverar` | 41.0 | 0.678 | racimo censado: Pivotar o proceder (cribado) |
| quality | `certificacion_belts_six_sigma` con `desarrollo_expertos_capaces` | 31.3 | 0.677 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `programa_auditoria_calidad` con `reporte_auditoria` | 61.8 | 0.676 | racimo censado: Auditoria de calidad (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `responsabilizacion_del_trabajador` | 32.3 | 0.6757 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `new_view_investigation` con `responsabilidad_prospectiva` | 27.7 | 0.6753 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `human_error_como_sintoma` con `responsabilidad_prospectiva` | 27.5 | 0.675 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `mejora_continua_del_sistema` con `plan_de_accion_transformacion` | 45.5 | 0.6747 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `ciclo_de_mejora_continua_helix` con `ciclo_pdca_pdsa` | 23.5 | 0.6742 | racimo censado: Ciclo de mejora PDCA / PDSA (cribado) |
| health_safety | `preguntar_que_no_quien` con `responsabilidad_sistemica` | 27.5 | 0.674 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `principios_gestion_error` con `rendicion_cuentas_prospectiva` | 31.7 | 0.6737 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `desajuste_tarea_persona` | 63.5 | 0.6724 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `moral_y_sistema_no_individuo` con `sistema_estable_causas_comunes` | 37.1 | 0.6715 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `bad_apple_theory` con `responsabilizacion_del_trabajador` | 36.4 | 0.6707 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `ciclo_de_culpa` | 39.6 | 0.67 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `gestion_de_errores` con `responsabilidad_sistemica` | 36.0 | 0.6696 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `eco_efectividad_2` con `materiales_ciclicos_infinitamente_reciclables` | 22.2 | 0.669 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `ciclo_de_culpa` con `desajuste_autoridad_responsabilidad` | 32.6 | 0.6688 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `gestion_de_errores` con `new_view_investigation` | 27.8 | 0.6688 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `gestion_de_errores` | 35.2 | 0.6683 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `revision_de_aprendizaje` | 35.2 | 0.6679 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `certificacion_belts_six_sigma` con `estructura_competencias_six_sigma_lean` | 62.8 | 0.6677 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| core | `cinco_porques_master` con `regla_simplificada_tolerancia_errores` | 32.3 | 0.6673 | racimo censado: Los cinco porques (cribado) |
| quality | `eliminar_miedo` con `eliminar_slogans_metas` | 52.9 | 0.6669 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| health_safety | `desajuste_autoridad_responsabilidad` con `responsabilidad_sistemica` | 51.5 | 0.6661 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `errores_como_consecuencia` con `rendicion_cuentas_prospectiva` | 33.9 | 0.665 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `estructura_competencias_six_sigma_lean` con `rol_facilitador_black_belt` | 39.6 | 0.6637 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `rol_black_belt_six_sigma` con `rol_facilitador_black_belt` | 43.9 | 0.6635 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `desajuste_tarea_persona` con `new_view_human_error` | 23.9 | 0.6633 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `certificacion_belts_six_sigma` con `rol_black_belt_six_sigma` | 46.3 | 0.6616 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `desajuste_tarea_persona` con `rendicion_cuentas_prospectiva` | 33.9 | 0.6602 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `moral_y_sistema_no_individuo` con `sistema_responsabilidad_gerencial_2` | 35.1 | 0.6587 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `gestion_de_errores` con `preguntar_que_no_quien` | 25.6 | 0.6572 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `revision_de_aprendizaje` | 41.3 | 0.6564 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `certificacion_belts_six_sigma` con `rol_black_belt` | 49.5 | 0.6536 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| environmental | `modelo_cradle_to_grave` con `nutrientes_biologicos` | 26.7 | 0.6534 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `new_view_human_error` | 26.5 | 0.653 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `analisis_causa_raiz_defectos` con `analisis_diagnostico_causa` | 60.2 | 0.6524 | racimo censado: Analisis de causa raiz (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `human_error_como_sintoma` | 29.5 | 0.6523 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `eliminar_slogans_metas` con `mejora_continua_del_sistema` | 41.5 | 0.652 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| health_safety | `ciclo_de_culpa` con `desajuste_tarea_persona` | 35.2 | 0.6501 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `eco_efectividad` con `nutrientes_biologicos` | 30.0 | 0.6491 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `desajuste_tarea_persona` con `new_view_investigation` | 27.8 | 0.6466 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `eco_efectividad_re_evolucion_industrial` con `modelo_cradle_to_grave` | 28.9 | 0.646 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `bad_apple_theory` con `responsabilidad_prospectiva` | 34.2 | 0.645 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `eco_efectividad_2` con `nutrientes_biologicos` | 20.3 | 0.6445 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `responsabilidad_prospectiva` | 27.2 | 0.6444 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `falla_sistemica_vs_error_individual` | 31.7 | 0.6437 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `eliminar_slogans_metas` con `institucionalizar_capacitacion` | 46.3 | 0.6417 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `analisis_causa_raiz_defectos` con `juran_rcca_metodo` | 56.6 | 0.6411 | racimo censado: Analisis de causa raiz (cribado) |
| quality | `moral_y_sistema_no_individuo` con `sistema_responsabilidad_gerencial` | 35.1 | 0.6411 | racimo censado: Causas comunes y responsabilidad del sistema (cribado) |
| health_safety | `gestion_de_errores` con `rendicion_cuentas_prospectiva` | 28.8 | 0.64 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `activacion_lista_positiva` con `nutrientes_biologicos` | 34.5 | 0.639 | racimo censado: Cradle to cradle (cribado) |
| environmental | `activacion_lista_positiva` con `critica_eco_eficiencia` | 39.4 | 0.6386 | racimo censado: Cradle to cradle (cribado) |
| quality | `desarrollo_expertos_capaces` con `rol_green_belt_six_sigma` | 29.9 | 0.6375 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `gestion_de_errores` con `responsabilizacion_del_trabajador` | 29.9 | 0.6375 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `cinco_porques_master` con `tecnica_cinco_porques` | 49.3 | 0.6354 | racimo censado: Los cinco porques (cribado) |
| health_safety | `human_error_como_sintoma` con `rendicion_cuentas_prospectiva` | 34.7 | 0.6349 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `new_view_investigation` con `responsabilizacion_del_trabajador` | 26.1 | 0.6346 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `customer_development_process` con `customer_development_vs_business_plan` | 41.2 | 0.6331 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| environmental | `activacion_lista_positiva` con `eco_efectividad_re_evolucion_industrial` | 36.4 | 0.6317 | racimo censado: Cradle to cradle (cribado) |
| core | `customer_development_vs_business_plan` con `customer_discovery` | 43.4 | 0.6298 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| health_safety | `bad_apple_theory` con `revision_de_aprendizaje` | 37.5 | 0.6296 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| environmental | `critica_eco_eficiencia` con `materiales_ciclicos_infinitamente_reciclables` | 35.9 | 0.6286 | racimo censado: Cradle to cradle (cribado) |
| quality | `institucionalizar_capacitacion` con `mejora_continua_del_sistema` | 41.8 | 0.6274 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| environmental | `responsabilidad_extendida_productor` con `responsabilidad_extendida_productor_2` | 44.2 | 0.6268 | ficha, las 36 parejas de sufijo vivo |
| health_safety | `process_tracing_methods` con `revision_de_aprendizaje` | 37.1 | 0.6261 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `certificacion_belts_six_sigma` con `roles_six_sigma` | 44.2 | 0.6254 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `errores_como_consecuencia` con `process_tracing_methods` | 29.2 | 0.6253 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_autoridad_responsabilidad` con `gestion_de_errores` | 35.3 | 0.6235 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `desarrollo_expertos_capaces` con `rol_black_belt` | 38.2 | 0.6235 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| environmental | `activacion_lista_positiva` con `modelo_cradle_to_grave` | 35.7 | 0.6232 | racimo censado: Cradle to cradle (cribado) |
| quality | `desarrollo_expertos_capaces` con `rol_black_belt_six_sigma` | 29.8 | 0.6226 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `institucionalizar_capacitacion` con `plan_de_accion_transformacion` | 50.6 | 0.6221 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `eliminar_miedo` con `fomento_educacion_autoeducacion` | 45.3 | 0.6206 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| environmental | `eco_efectividad_re_evolucion_industrial` con `materiales_ciclicos_infinitamente_reciclables` | 35.6 | 0.6194 | racimo censado: Cradle to cradle (cribado) |
| quality | `concepto_de_auditoria_de_calidad` con `reporte_auditoria` | 60.5 | 0.6193 | racimo censado: Auditoria de calidad (cribado) |
| quality | `entrenamiento_para_breakthrough` con `rol_facilitador_black_belt` | 42.9 | 0.6184 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `preguntar_que_no_quien` con `process_tracing_methods` | 32.6 | 0.6179 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `rol_facilitador_black_belt` con `rol_green_belt_six_sigma` | 36.7 | 0.6166 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `planificacion_estrategica_despliegue` con `planificacion_estrategica_despliegue_2` | 39.2 | 0.615 | informe 4.3 base mas _2 calcados; ficha, las 36 parejas de sufijo vivo |
| health_safety | `bad_apple_theory` con `rendicion_cuentas_prospectiva` | 35.8 | 0.6137 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| core | `customer_development_vs_business_plan` con `customer_discovery_get_out_of_building` | 37.0 | 0.6123 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| health_safety | `abandonar_arreglos_rapidos` con `process_tracing_methods` | 34.5 | 0.6115 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `new_view_human_error` con `process_tracing_methods` | 35.6 | 0.6091 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `eliminar_miedo` con `institucionalizar_capacitacion` | 51.6 | 0.6078 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `desarrollo_expertos_capaces` con `rol_facilitador_black_belt` | 40.8 | 0.6065 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| core | `customer_development_vs_business_plan` con `customer_discovery_phase2_problem_test` | 34.6 | 0.6049 | racimo censado: Customer discovery: salir a hablar con el cliente (cribado) |
| quality | `concepto_de_auditoria_de_calidad` con `estructuracion_programa_auditoria` | 37.8 | 0.6043 | racimo censado: Auditoria de calidad (cribado) |
| environmental | `eco_efectividad_re_evolucion_industrial` con `nutrientes_biologicos` | 29.5 | 0.6037 | racimo censado: Cradle to cradle (cribado) |
| quality | `adopcion_liderazgo` con `plan_de_accion_transformacion` | 44.4 | 0.6022 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| health_safety | `falla_sistemica_vs_error_individual` con `rendicion_cuentas_prospectiva` | 31.3 | 0.5949 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `process_tracing_methods` con `responsabilidad_sistemica` | 41.5 | 0.5934 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `enfoque_situacional_vs_personal` con `process_tracing_methods` | 38.1 | 0.5907 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `falla_sistemica_vs_error_individual` con `process_tracing_methods` | 25.3 | 0.5901 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `desajuste_autoridad_responsabilidad` | 33.3 | 0.5858 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `ciclo_de_culpa` con `process_tracing_methods` | 39.2 | 0.5831 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `bad_apple_theory` con `process_tracing_methods` | 35.8 | 0.5821 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `human_error_como_sintoma` con `process_tracing_methods` | 30.1 | 0.5814 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `desarrollo_expertos_capaces` con `roles_six_sigma` | 37.8 | 0.5792 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| quality | `adopcion_liderazgo` con `mejora_continua_del_sistema` | 44.4 | 0.5787 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `adopcion_liderazgo` con `fomento_educacion_autoeducacion` | 44.4 | 0.5786 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `fomento_educacion_autoeducacion` con `plan_de_accion_transformacion` | 58.3 | 0.5785 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| health_safety | `desajuste_autoridad_responsabilidad` con `new_view_investigation` | 27.4 | 0.5711 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `principios_gestion_error` con `process_tracing_methods` | 44.9 | 0.5679 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `eliminar_slogans_metas` con `plan_de_accion_transformacion` | 48.1 | 0.5662 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| environmental | `critica_eco_eficiencia` con `nutrientes_biologicos` | 34.8 | 0.5641 | racimo censado: Cradle to cradle (cribado) |
| health_safety | `process_tracing_methods` con `rendicion_cuentas_prospectiva` | 33.9 | 0.5629 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `gestion_de_errores` con `process_tracing_methods` | 42.2 | 0.5458 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| health_safety | `desajuste_tarea_persona` con `process_tracing_methods` | 42.2 | 0.5358 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `fomento_educacion_autoeducacion` con `mejora_continua_del_sistema` | 47.2 | 0.5255 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `eliminar_slogans_metas` con `fomento_educacion_autoeducacion` | 51.9 | 0.5205 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| health_safety | `process_tracing_methods` con `responsabilidad_prospectiva` | 33.9 | 0.5164 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `eliminar_miedo` con `mejora_continua_del_sistema` | 37.3 | 0.5035 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| quality | `eliminar_miedo` con `plan_de_accion_transformacion` | 45.3 | 0.4957 | racimo censado: Los puntos de Deming en el titulo (muestra-D) |
| health_safety | `process_tracing_methods` con `responsabilizacion_del_trabajador` | 31.6 | 0.4724 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |
| quality | `certificacion_belts_six_sigma` con `rol_facilitador_black_belt` | 44.7 | 0.472 | racimo censado: La estructura de cinturones de Six Sigma (muestra-D) |
| health_safety | `desajuste_autoridad_responsabilidad` con `process_tracing_methods` | 33.0 | 0.4588 | racimo censado: No culpar a la persona, arreglar el sistema (cribado) |

**Lo que estas perdidas dicen, y es lo mas util de este resumen:**

- **La familia de ids no la cazan estas dos senales.** Casi todas las perdidas son parejas de **sufijo `_N`**: se llaman parecido pero no lo bastante para el umbral de titulo, y hablan de lo mismo pero por debajo del umbral semantico. **Su detector no es este: es la regla del sufijo**, que este mismo instrumento ya computa y publica arriba con sus 36 parejas.
- **Bajar el umbral no las rescata gratis.** La perdida mas alta esta en **0.7797** de semantica; bajar el corte hasta ahi ensancharia la cola en todos los dominios a la vez. La distribucion de abajo dice cuanto.
- **Hay perdidas que NO son de sufijo, y esas si duelen**: `abandonar_arreglos_rapidos` con `bad_apple_theory`, `abandonar_arreglos_rapidos` con `ciclo_de_culpa`, `abandonar_arreglos_rapidos` con `desajuste_autoridad_responsabilidad`, `abandonar_arreglos_rapidos` con `desajuste_tarea_persona`, `abandonar_arreglos_rapidos` con `errores_como_consecuencia`, `abandonar_arreglos_rapidos` con `falla_sistemica_vs_error_individual`, `abandonar_arreglos_rapidos` con `gestion_de_errores`, `abandonar_arreglos_rapidos` con `human_error_como_sintoma`, `abandonar_arreglos_rapidos` con `new_view_human_error`, `abandonar_arreglos_rapidos` con `preguntar_que_no_quien`, `abandonar_arreglos_rapidos` con `principios_gestion_error`, `abandonar_arreglos_rapidos` con `process_tracing_methods`, `abandonar_arreglos_rapidos` con `rendicion_cuentas_prospectiva`, `abandonar_arreglos_rapidos` con `responsabilidad_prospectiva`, `abandonar_arreglos_rapidos` con `responsabilidad_sistemica`, `abandonar_arreglos_rapidos` con `responsabilizacion_del_trabajador`, `accion_correctiva_2` con `accion_correctiva_4`, `accion_correctiva_2` con `accion_correctiva_crosby`, `accion_correctiva_2` con `accion_correctiva_sistematica`, `activacion_lista_positiva` con `critica_eco_eficiencia`, `activacion_lista_positiva` con `desperdicio_es_alimento`, `activacion_lista_positiva` con `eco_efectividad`, `activacion_lista_positiva` con `eco_efectividad_2`, `activacion_lista_positiva` con `eco_efectividad_re_evolucion_industrial`, `activacion_lista_positiva` con `materiales_ciclicos_infinitamente_reciclables`, `activacion_lista_positiva` con `modelo_cradle_to_grave`, `activacion_lista_positiva` con `nutrientes_biologicos`, `actualizar_modelo_de_negocio_pivot_o_proceed` con `decision_pivotar_o_proceder`, `actualizar_modelo_de_negocio_pivot_o_proceed` con `pivotar_o_perseverar`, `actualizar_modelo_de_negocio_pivot_o_proceed` con `reunion_pivotar_o_perseverar`, `adopcion_liderazgo` con `eliminar_miedo`, `adopcion_liderazgo` con `eliminar_slogans_metas`, `adopcion_liderazgo` con `fomento_educacion_autoeducacion`, `adopcion_liderazgo` con `institucionalizar_capacitacion`, `adopcion_liderazgo` con `mejora_continua_del_sistema`, `adopcion_liderazgo` con `plan_de_accion_transformacion`, `advances_vs_continuations` con `obtencion_compromiso`, `advances_vs_continuations` con `obtencion_compromiso_venta`, `advances_vs_continuations` con `obtencion_de_compromiso`, `analisis_causa_raiz_defectos` con `analisis_causa_raiz_diagnostico`, `analisis_causa_raiz_defectos` con `analisis_diagnostico_causa`, `analisis_causa_raiz_defectos` con `juran_rcca_metodo`, `analisis_causa_raiz_diagnostico` con `juran_rcca_metodo`, `analisis_diagnostico_causa` con `juran_rcca_metodo`, `auditoria_calidad` con `estructuracion_programa_auditoria`, `auditoria_calidad` con `principios_auditoria_calidad`, `auditoria_calidad` con `reporte_auditoria`, `bad_apple_theory` con `ciclo_de_culpa`, `bad_apple_theory` con `desajuste_autoridad_responsabilidad`, `bad_apple_theory` con `desajuste_tarea_persona`, `bad_apple_theory` con `enfoque_situacional_vs_personal`, `bad_apple_theory` con `errores_como_consecuencia`, `bad_apple_theory` con `falla_sistemica_vs_error_individual`, `bad_apple_theory` con `gestion_de_errores`, `bad_apple_theory` con `human_error_como_sintoma`, `bad_apple_theory` con `new_view_investigation`, `bad_apple_theory` con `preguntar_que_no_quien`, `bad_apple_theory` con `principios_gestion_error`, `bad_apple_theory` con `process_tracing_methods`, `bad_apple_theory` con `rendicion_cuentas_prospectiva`, `bad_apple_theory` con `responsabilidad_prospectiva`, `bad_apple_theory` con `responsabilidad_sistemica`, `bad_apple_theory` con `responsabilizacion_del_trabajador`, `bad_apple_theory` con `revision_de_aprendizaje`, `benchmarking_7_pasos_juran` con `gestion_efectiva_benchmarking`, `benchmarking_7_pasos_juran` con `rol_alta_direccion_benchmarking`, `benchmarking_proceso` con `gestion_efectiva_benchmarking`, `benchmarking_proceso` con `rol_alta_direccion_benchmarking`, `causas_comunes_vs_especiales` con `mejora_del_sistema_responsabilidad_gerencial`, `causas_comunes_vs_especiales` con `moral_y_sistema_no_individuo`, `causas_comunes_vs_especiales` con `politica_no_culpar_trabajador`, `causas_comunes_vs_especiales` con `sistema_estable_causas_comunes`, `causas_comunes_vs_especiales` con `sistema_estable_responsabilidad_gerencial`, `causas_comunes_vs_especiales` con `sistema_responsabilidad_gerencial`, `causas_comunes_vs_especiales` con `sistema_responsabilidad_gerencial_2`, `certificacion_belts_six_sigma` con `desarrollo_expertos_capaces`, `certificacion_belts_six_sigma` con `entrenamiento_para_breakthrough`, `certificacion_belts_six_sigma` con `estructura_competencias_six_sigma_lean`, `certificacion_belts_six_sigma` con `rol_black_belt`, `certificacion_belts_six_sigma` con `rol_black_belt_six_sigma`, `certificacion_belts_six_sigma` con `rol_facilitador_black_belt`, `certificacion_belts_six_sigma` con `rol_green_belt_six_sigma`, `certificacion_belts_six_sigma` con `roles_six_sigma`, `ciclo_de_culpa` con `desajuste_autoridad_responsabilidad`, `ciclo_de_culpa` con `desajuste_tarea_persona`, `ciclo_de_culpa` con `enfoque_situacional_vs_personal`, `ciclo_de_culpa` con `errores_como_consecuencia`, `ciclo_de_culpa` con `falla_sistemica_vs_error_individual`, `ciclo_de_culpa` con `gestion_de_errores`, `ciclo_de_culpa` con `human_error_como_sintoma`, `ciclo_de_culpa` con `new_view_human_error`, `ciclo_de_culpa` con `new_view_investigation`, `ciclo_de_culpa` con `preguntar_que_no_quien`, `ciclo_de_culpa` con `principios_gestion_error`, `ciclo_de_culpa` con `process_tracing_methods`, `ciclo_de_culpa` con `rendicion_cuentas_prospectiva`, `ciclo_de_culpa` con `responsabilidad_prospectiva`, `ciclo_de_culpa` con `responsabilidad_sistemica`, `ciclo_de_culpa` con `responsabilizacion_del_trabajador`, `ciclo_de_culpa` con `revision_de_aprendizaje`, `ciclo_de_mejora_continua_helix` con `ciclo_pdca_pdsa`, `ciclo_de_mejora_continua_helix` con `ciclo_shewhart_pdsa`, `ciclo_de_mejora_continua_helix` con `pdsa_shewhart_cycle`, `cinco_porques_master` con `curse_cinco_culpas`, `cinco_porques_master` con `five_whys_inversion_proporcional`, `cinco_porques_master` con `regla_simplificada_tolerancia_errores`, `cinco_porques_master` con `tecnica_cinco_porques`, `clasificacion_caracteristicas_calidad` con `clasificacion_de_seriedad_de_defectos`, `concepto_de_auditoria_de_calidad` con `estructuracion_programa_auditoria`, `concepto_de_auditoria_de_calidad` con `principios_auditoria_calidad`, `concepto_de_auditoria_de_calidad` con `reporte_auditoria`, `control_mantener_ganancias` con `matriz_de_control_de_proceso`, `cradle_to_cradle_concepto` con `critica_eco_eficiencia`, `cradle_to_cradle_concepto` con `eco_efectividad`, `cradle_to_cradle_concepto` con `eco_efectividad_re_evolucion_industrial`, `cradle_to_cradle_concepto` con `materiales_ciclicos_infinitamente_reciclables`, `cradle_to_cradle_concepto` con `modelo_cradle_to_grave`, `cradle_to_cradle_concepto` con `nutrientes_biologicos`, `critica_eco_eficiencia` con `desperdicio_es_alimento`, `critica_eco_eficiencia` con `eco_efectividad`, `critica_eco_eficiencia` con `eco_efectividad_2`, `critica_eco_eficiencia` con `eco_efectividad_re_evolucion_industrial`, `critica_eco_eficiencia` con `materiales_ciclicos_infinitamente_reciclables`, `critica_eco_eficiencia` con `modelo_cradle_to_grave`, `critica_eco_eficiencia` con `nutrientes_biologicos`, `curse_cinco_culpas` con `five_whys_inversion_proporcional`, `curse_cinco_culpas` con `regla_simplificada_tolerancia_errores`, `curse_cinco_culpas` con `tecnica_cinco_porques`, `customer_development_modelo` con `customer_development_vs_business_plan`, `customer_development_modelo` con `customer_discovery_phase2_problem_test`, `customer_development_process` con `customer_development_vs_business_plan`, `customer_development_vs_business_plan` con `customer_discovery`, `customer_development_vs_business_plan` con `customer_discovery_cuatro_fases`, `customer_development_vs_business_plan` con `customer_discovery_get_out_of_building`, `customer_development_vs_business_plan` con `customer_discovery_phase2_problem_test`, `customer_discovery` con `customer_discovery_get_out_of_building`, `customer_discovery_cuatro_fases` con `customer_discovery_get_out_of_building`, `customer_discovery_get_out_of_building` con `customer_discovery_phase2_problem_test`, `decision_pivotar_o_proceder` con `pivotar_o_perseverar`, `decision_pivotar_o_proceder` con `reunion_pivotar_o_perseverar`, `desajuste_autoridad_responsabilidad` con `desajuste_tarea_persona`, `desajuste_autoridad_responsabilidad` con `enfoque_situacional_vs_personal`, `desajuste_autoridad_responsabilidad` con `errores_como_consecuencia`, `desajuste_autoridad_responsabilidad` con `falla_sistemica_vs_error_individual`, `desajuste_autoridad_responsabilidad` con `gestion_de_errores`, `desajuste_autoridad_responsabilidad` con `human_error_como_sintoma`, `desajuste_autoridad_responsabilidad` con `new_view_human_error`, `desajuste_autoridad_responsabilidad` con `new_view_investigation`, `desajuste_autoridad_responsabilidad` con `preguntar_que_no_quien`, `desajuste_autoridad_responsabilidad` con `principios_gestion_error`, `desajuste_autoridad_responsabilidad` con `process_tracing_methods`, `desajuste_autoridad_responsabilidad` con `rendicion_cuentas_prospectiva`, `desajuste_autoridad_responsabilidad` con `responsabilidad_prospectiva`, `desajuste_autoridad_responsabilidad` con `responsabilidad_sistemica`, `desajuste_autoridad_responsabilidad` con `revision_de_aprendizaje`, `desajuste_tarea_persona` con `enfoque_situacional_vs_personal`, `desajuste_tarea_persona` con `errores_como_consecuencia`, `desajuste_tarea_persona` con `falla_sistemica_vs_error_individual`, `desajuste_tarea_persona` con `gestion_de_errores`, `desajuste_tarea_persona` con `human_error_como_sintoma`, `desajuste_tarea_persona` con `new_view_human_error`, `desajuste_tarea_persona` con `new_view_investigation`, `desajuste_tarea_persona` con `preguntar_que_no_quien`, `desajuste_tarea_persona` con `principios_gestion_error`, `desajuste_tarea_persona` con `process_tracing_methods`, `desajuste_tarea_persona` con `rendicion_cuentas_prospectiva`, `desajuste_tarea_persona` con `responsabilidad_prospectiva`, `desajuste_tarea_persona` con `responsabilidad_sistemica`, `desajuste_tarea_persona` con `responsabilizacion_del_trabajador`, `desajuste_tarea_persona` con `revision_de_aprendizaje`, `desarrollo_expertos_capaces` con `entrenamiento_para_breakthrough`, `desarrollo_expertos_capaces` con `estructura_competencias_six_sigma_lean`, `desarrollo_expertos_capaces` con `rol_black_belt`, `desarrollo_expertos_capaces` con `rol_black_belt_six_sigma`, `desarrollo_expertos_capaces` con `rol_facilitador_black_belt`, `desarrollo_expertos_capaces` con `rol_green_belt_six_sigma`, `desarrollo_expertos_capaces` con `roles_six_sigma`, `desperdicio_es_alimento` con `eco_efectividad`, `desperdicio_es_alimento` con `eco_efectividad_re_evolucion_industrial`, `desperdicio_es_alimento` con `materiales_ciclicos_infinitamente_reciclables`, `desperdicio_es_alimento` con `nutrientes_biologicos`, `distincion_causas_comunes_especiales` con `mejora_del_sistema_responsabilidad_gerencial`, `distincion_causas_comunes_especiales` con `moral_y_sistema_no_individuo`, `distincion_causas_comunes_especiales` con `sistema_responsabilidad_gerencial`, `distincion_causas_comunes_especiales` con `sistema_responsabilidad_gerencial_2`, `distincion_causas_comunes_especiales_2` con `moral_y_sistema_no_individuo`, `distincion_causas_comunes_especiales_2` con `politica_no_culpar_trabajador`, `distincion_causas_comunes_especiales_2` con `sistema_estable_causas_comunes`, `distincion_causas_comunes_especiales_2` con `sistema_estable_responsabilidad_gerencial`, `distincion_causas_comunes_especiales_2` con `sistema_responsabilidad_gerencial`, `distincion_causas_comunes_especiales_2` con `sistema_responsabilidad_gerencial_2`, `distincion_causas_especiales_comunes` con `mejora_del_sistema_responsabilidad_gerencial`, `distincion_causas_especiales_comunes` con `moral_y_sistema_no_individuo`, `distincion_causas_especiales_comunes` con `politica_no_culpar_trabajador`, `distincion_causas_especiales_comunes` con `responsabilidad_gerencial_causas_comunes`, `distincion_causas_especiales_comunes` con `sistema_estable_causas_comunes`, `distincion_causas_especiales_comunes` con `sistema_estable_responsabilidad_gerencial`, `distincion_causas_especiales_comunes` con `sistema_responsabilidad_gerencial`, `distincion_causas_especiales_comunes` con `sistema_responsabilidad_gerencial_2`, `diversidad_en_diseno` con `respeto_a_la_diversidad`, `eco_efectividad` con `modelo_cradle_to_grave`, `eco_efectividad` con `nutrientes_biologicos`, `eco_efectividad_2` con `materiales_ciclicos_infinitamente_reciclables`, `eco_efectividad_2` con `modelo_cradle_to_grave`, `eco_efectividad_2` con `nutrientes_biologicos`, `eco_efectividad_re_evolucion_industrial` con `materiales_ciclicos_infinitamente_reciclables`, `eco_efectividad_re_evolucion_industrial` con `modelo_cradle_to_grave`, `eco_efectividad_re_evolucion_industrial` con `nutrientes_biologicos`, `eliminar_miedo` con `eliminar_slogans_metas`, `eliminar_miedo` con `fomento_educacion_autoeducacion`, `eliminar_miedo` con `institucionalizar_capacitacion`, `eliminar_miedo` con `mejora_continua_del_sistema`, `eliminar_miedo` con `plan_de_accion_transformacion`, `eliminar_slogans_metas` con `fomento_educacion_autoeducacion`, `eliminar_slogans_metas` con `institucionalizar_capacitacion`, `eliminar_slogans_metas` con `mejora_continua_del_sistema`, `eliminar_slogans_metas` con `plan_de_accion_transformacion`, `encuadre_desafio_diseno` con `how_might_we_brief_social`, `encuadre_desafio_diseno` con `how_might_we_briefs`, `encuadre_desafio_diseno` con `how_might_we_hmw`, `enfoque_situacional_vs_personal` con `falla_sistemica_vs_error_individual`, `enfoque_situacional_vs_personal` con `new_view_human_error`, `enfoque_situacional_vs_personal` con `new_view_investigation`, `enfoque_situacional_vs_personal` con `preguntar_que_no_quien`, `enfoque_situacional_vs_personal` con `process_tracing_methods`, `enfoque_situacional_vs_personal` con `rendicion_cuentas_prospectiva`, `enfoque_situacional_vs_personal` con `responsabilidad_prospectiva`, `enfoque_situacional_vs_personal` con `responsabilidad_sistemica`, `enfoque_situacional_vs_personal` con `responsabilizacion_del_trabajador`, `enfoque_situacional_vs_personal` con `revision_de_aprendizaje`, `entrenamiento_para_breakthrough` con `estructura_competencias_six_sigma_lean`, `entrenamiento_para_breakthrough` con `rol_black_belt`, `entrenamiento_para_breakthrough` con `rol_black_belt_six_sigma`, `entrenamiento_para_breakthrough` con `rol_facilitador_black_belt`, `entrenamiento_para_breakthrough` con `roles_six_sigma`, `errores_como_consecuencia` con `gestion_de_errores`, `errores_como_consecuencia` con `new_view_investigation`, `errores_como_consecuencia` con `process_tracing_methods`, `errores_como_consecuencia` con `rendicion_cuentas_prospectiva`, `errores_como_consecuencia` con `responsabilidad_prospectiva`, `errores_como_consecuencia` con `responsabilidad_sistemica`, `errores_como_consecuencia` con `responsabilizacion_del_trabajador`, `errores_como_consecuencia` con `revision_de_aprendizaje`, `establecer_estandares_desempeno` con `establecer_metas_de_calidad_basadas_en_mercado`, `estructura_competencias_six_sigma_lean` con `rol_black_belt`, `estructura_competencias_six_sigma_lean` con `rol_black_belt_six_sigma`, `estructura_competencias_six_sigma_lean` con `rol_facilitador_black_belt`, `estructura_competencias_six_sigma_lean` con `rol_green_belt_six_sigma`, `estructuracion_programa_auditoria` con `principios_auditoria_calidad`, `estructuracion_programa_auditoria` con `programa_auditoria_calidad`, `estructuracion_programa_auditoria` con `reporte_auditoria`, `falla_sistemica_vs_error_individual` con `gestion_de_errores`, `falla_sistemica_vs_error_individual` con `new_view_human_error`, `falla_sistemica_vs_error_individual` con `new_view_investigation`, `falla_sistemica_vs_error_individual` con `preguntar_que_no_quien`, `falla_sistemica_vs_error_individual` con `principios_gestion_error`, `falla_sistemica_vs_error_individual` con `process_tracing_methods`, `falla_sistemica_vs_error_individual` con `rendicion_cuentas_prospectiva`, `falla_sistemica_vs_error_individual` con `responsabilidad_prospectiva`, `falla_sistemica_vs_error_individual` con `responsabilidad_sistemica`, `falla_sistemica_vs_error_individual` con `responsabilizacion_del_trabajador`, `falla_sistemica_vs_error_individual` con `revision_de_aprendizaje`, `fomento_educacion_autoeducacion` con `institucionalizar_capacitacion`, `fomento_educacion_autoeducacion` con `mejora_continua_del_sistema`, `fomento_educacion_autoeducacion` con `plan_de_accion_transformacion`, `gestion_de_errores` con `human_error_como_sintoma`, `gestion_de_errores` con `new_view_human_error`, `gestion_de_errores` con `new_view_investigation`, `gestion_de_errores` con `preguntar_que_no_quien`, `gestion_de_errores` con `process_tracing_methods`, `gestion_de_errores` con `rendicion_cuentas_prospectiva`, `gestion_de_errores` con `responsabilidad_prospectiva`, `gestion_de_errores` con `responsabilidad_sistemica`, `gestion_de_errores` con `responsabilizacion_del_trabajador`, `gestion_de_errores` con `revision_de_aprendizaje`, `gestion_de_portafolio_gates_go_kill` con `gestion_portafolio_dos_niveles`, `gestion_de_portafolio_gates_go_kill` con `pruning_portafolio`, `gestion_de_portafolio_gates_go_kill` con `revision_portafolio_periodica`, `gestion_efectiva_benchmarking` con `monitoreo_continuo_benchmarking`, `gestion_portafolio_dos_niveles` con `gestion_portafolio_foco`, `gestion_portafolio_dos_niveles` con `pruning_portafolio`, `gestion_portafolio_foco` con `gestion_portafolio_formal`, `gestion_portafolio_foco` con `revision_portafolio_periodica`, `how_might_we_brief_social` con `how_might_we_framing`, `how_might_we_brief_social` con `how_might_we_hmw`, `how_might_we_briefs` con `how_might_we_framing`, `human_error_como_sintoma` con `new_view_investigation`, `human_error_como_sintoma` con `preguntar_que_no_quien`, `human_error_como_sintoma` con `principios_gestion_error`, `human_error_como_sintoma` con `process_tracing_methods`, `human_error_como_sintoma` con `rendicion_cuentas_prospectiva`, `human_error_como_sintoma` con `responsabilidad_prospectiva`, `human_error_como_sintoma` con `responsabilidad_sistemica`, `human_error_como_sintoma` con `responsabilizacion_del_trabajador`, `human_error_como_sintoma` con `revision_de_aprendizaje`, `institucionalizar_capacitacion` con `mejora_continua_del_sistema`, `institucionalizar_capacitacion` con `plan_de_accion_transformacion`, `lean_manufacturing` con `ocho_desperdicios_lean`, `mapeo_flujo_valor` con `ocho_desperdicios_lean`, `materiales_ciclicos_infinitamente_reciclables` con `modelo_cradle_to_grave`, `materiales_ciclicos_infinitamente_reciclables` con `nutrientes_biologicos`, `mejora_continua_del_sistema` con `plan_de_accion_transformacion`, `mejora_del_sistema_responsabilidad_gerencial` con `moral_y_sistema_no_individuo`, `mejora_del_sistema_responsabilidad_gerencial` con `politica_no_culpar_trabajador`, `modelo_cradle_to_grave` con `nutrientes_biologicos`, `monitoreo_continuo_benchmarking` con `rol_alta_direccion_benchmarking`, `moral_y_sistema_no_individuo` con `responsabilidad_gerencial_causas_comunes`, `moral_y_sistema_no_individuo` con `sistema_estable_causas_comunes`, `moral_y_sistema_no_individuo` con `sistema_estable_responsabilidad_gerencial`, `moral_y_sistema_no_individuo` con `sistema_responsabilidad_gerencial`, `moral_y_sistema_no_individuo` con `sistema_responsabilidad_gerencial_2`, `new_view_human_error` con `preguntar_que_no_quien`, `new_view_human_error` con `process_tracing_methods`, `new_view_human_error` con `rendicion_cuentas_prospectiva`, `new_view_human_error` con `responsabilidad_prospectiva`, `new_view_human_error` con `responsabilidad_sistemica`, `new_view_human_error` con `responsabilizacion_del_trabajador`, `new_view_human_error` con `revision_de_aprendizaje`, `new_view_investigation` con `preguntar_que_no_quien`, `new_view_investigation` con `principios_gestion_error`, `new_view_investigation` con `process_tracing_methods`, `new_view_investigation` con `rendicion_cuentas_prospectiva`, `new_view_investigation` con `responsabilidad_prospectiva`, `new_view_investigation` con `responsabilidad_sistemica`, `new_view_investigation` con `responsabilizacion_del_trabajador`, `objetivos_de_llamada_orientados_a_avance` con `obtencion_compromiso`, `objetivos_de_llamada_orientados_a_avance` con `obtencion_compromiso_venta`, `objetivos_de_llamada_orientados_a_avance` con `obtencion_de_compromiso`, `pivotar_o_perseverar` con `pivotar_o_proceder`, `pivotar_o_perseverar` con `reunion_pivotar_o_perseverar`, `politica_no_culpar_trabajador` con `sistema_estable_causas_comunes`, `politica_no_culpar_trabajador` con `sistema_estable_responsabilidad_gerencial`, `politica_no_culpar_trabajador` con `sistema_responsabilidad_gerencial`, `politica_no_culpar_trabajador` con `sistema_responsabilidad_gerencial_2`, `portfolio_management` con `revision_portafolio_periodica`, `preguntar_que_no_quien` con `principios_gestion_error`, `preguntar_que_no_quien` con `process_tracing_methods`, `preguntar_que_no_quien` con `responsabilidad_sistemica`, `preguntar_que_no_quien` con `responsabilizacion_del_trabajador`, `principios_auditoria_calidad` con `programa_auditoria_calidad`, `principios_auditoria_calidad` con `reporte_auditoria`, `principios_gestion_error` con `process_tracing_methods`, `principios_gestion_error` con `rendicion_cuentas_prospectiva`, `principios_gestion_error` con `responsabilidad_prospectiva`, `principios_gestion_error` con `responsabilidad_sistemica`, `principios_gestion_error` con `responsabilizacion_del_trabajador`, `principios_gestion_error` con `revision_de_aprendizaje`, `process_tracing_methods` con `rendicion_cuentas_prospectiva`, `process_tracing_methods` con `responsabilidad_prospectiva`, `process_tracing_methods` con `responsabilidad_sistemica`, `process_tracing_methods` con `responsabilizacion_del_trabajador`, `process_tracing_methods` con `revision_de_aprendizaje`, `programa_auditoria_calidad` con `reporte_auditoria`, `pruning_portafolio` con `revision_portafolio_periodica`, `regla_simplificada_tolerancia_errores` con `tecnica_cinco_porques`, `rendicion_cuentas_prospectiva` con `responsabilidad_sistemica`, `rendicion_cuentas_prospectiva` con `responsabilizacion_del_trabajador`, `responsabilidad_gerencial_causas_comunes` con `sistema_estable_responsabilidad_gerencial`, `responsabilidad_prospectiva` con `responsabilidad_sistemica`, `responsabilidad_prospectiva` con `responsabilizacion_del_trabajador`, `responsabilidad_sistemica` con `responsabilizacion_del_trabajador`, `responsabilidad_sistemica` con `revision_de_aprendizaje`, `responsabilizacion_del_trabajador` con `revision_de_aprendizaje`, `rol_black_belt` con `rol_facilitador_black_belt`, `rol_black_belt` con `rol_green_belt_six_sigma`, `rol_black_belt_six_sigma` con `rol_facilitador_black_belt`, `rol_facilitador_black_belt` con `rol_green_belt_six_sigma`, `rol_facilitador_black_belt` con `roles_six_sigma`, `sistema_estable_responsabilidad_gerencial` con `sistema_responsabilidad_gerencial`. **Son parejas ya adjudicadas que estas dos senales no ven**, y son el argumento para no leer esta cola como si fuera exhaustiva.

## Distribucion de la similitud semantica, por dominio

**Esta es la tabla para recalibrar el umbral antes de leer.** Si un dominio tiene el p99 por encima del umbral, ese dominio va a inundar la cola de vecinos legitimos y conviene subirle el corte.

| dominio | comparaciones | media | p50 | p90 | p99 | p99.9 | maximo | sobre el umbral |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| compras | 1035 | 0.6732 | 0.6739 | 0.8000 | 0.8646 | 0.8868 | 0.8877 | 155 |
| core | 1308153 | 0.4381 | 0.4323 | 0.5614 | 0.6845 | 0.7842 | 0.9334 | 1436 |
| entrega | 1081 | 0.6711 | 0.6630 | 0.8073 | 0.8839 | 0.9089 | 0.9283 | 171 |
| environmental | 41616 | 0.5253 | 0.5236 | 0.6405 | 0.7464 | 0.8294 | 0.9022 | 170 |
| exportacion | 9870 | 0.5623 | 0.5571 | 0.6759 | 0.7936 | 0.8724 | 0.9432 | 130 |
| franquicias | 18915 | 0.5870 | 0.5917 | 0.6898 | 0.7717 | 0.8709 | 0.9309 | 147 |
| health_safety | 39903 | 0.5210 | 0.5205 | 0.6443 | 0.7504 | 0.8295 | 0.9058 | 190 |
| quality | 313236 | 0.5071 | 0.5059 | 0.6253 | 0.7294 | 0.8174 | 0.9629 | 838 |
| risk_management | 1485 | 0.6756 | 0.6829 | 0.7684 | 0.8353 | 0.8843 | 0.9042 | 106 |
| seguridad_digital | 1485 | 0.6052 | 0.6057 | 0.7125 | 0.8096 | 0.8840 | 0.9136 | 26 |

## La banda 0,78 a 0,80, YA DENTRO de la cola

**Pares que entraron por la rebaja del umbral**: semantica por debajo de **0,80** y titulo por debajo de **80**, o sea que con el umbral anterior no entraban por ninguna de las dos senales. **Estan en `INTRA_DOMINIO_PARES.jsonl` con el campo `banda_078_080` en true**, para poder contar su rendimiento aparte y no mezclarlo con el de la cola original.

| dominio | de la banda | del resto de la cola | total | la banda es |
|---|---:|---:|---:|---:|
| compras | **51** | 104 | 155 | 33% |
| core | **564** | 881 | 1445 | 39% |
| entrega | **44** | 127 | 171 | 26% |
| environmental | **67** | 103 | 170 | 39% |
| exportacion | **43** | 87 | 130 | 33% |
| franquicias | **67** | 81 | 148 | 45% |
| health_safety | **84** | 108 | 192 | 44% |
| quality | **347** | 497 | 844 | 41% |
| risk_management | **50** | 56 | 106 | 47% |
| seguridad_digital | **8** | 19 | 27 | 30% |
| **total** | **1325** | **2063** | **3388** | **39%** |

**La banda se lee, no se descarta, y el motivo esta medido**: las dos parejas ya adjudicadas que la corrida anterior perdia viven dentro de ella. **Su rendimiento se cuenta aparte** (cuantas A, B y C aporta contra su costo de lectura), que es la unica forma de saber si la rebaja del umbral valio la pena.

**Verificacion de las dos perdidas conocidas**, que es lo que hace util a la banda:

| pareja | semantica | titulo | cae en la banda |
|---|---:|---:|:--:|
| `accion_correctiva_4` con `accion_correctiva_sistematica` | 0.7890 | 67.6 | **NO** |
| `cadencia_seguimiento_prospectos` con `gestion_seguimiento_prospectos` | 0.7887 | 41.7 | **NO** |

**Las dos son parejas ya adjudicadas que las senales actuales no ven** (el recall de arriba). Si caen dentro, la banda **es exactamente el sitio donde vive lo que esta cola se pierde**, y eso es lo que hay que pesar al decidir si se lee.

## Los treinta pares de similitud mas alta

Ordenados por la senal MAS FUERTE de las dos, normalizando el titulo a 0 a 1. Por eso hay filas con semantica baja y titulo alto: entraron por el titulo.

| # | dominio | nodo a | nodo b | titulo | semantica | pasos a/b | estado |
|---:|---|---|---|---:|---:|---:|---|
| 1 | quality | `capacidad_de_proceso` | `capacidad_del_proceso` | 97.6 | 0.7876 | 4/4 | nuevo |
| 2 | quality | `control_estadistico_de_procesos` | `control_estadistico_del_proceso` | 97.3 | 0.8809 | 10/4 | nuevo |
| 3 | exportacion | `carta_de_credito_letter_of_credit` | `letters_of_credit` | 97.2 | 0.8993 | 5/6 | nuevo |
| 4 | quality | `programa_de_mejora_de_calidad` | `programa_mejora_calidad_14_pasos` | 69.7 | 0.9629 | 6/7 | nodo ya avistado |
| 5 | quality | `planificacion_de_la_inspeccion` | `planificacion_inspeccion` | 94.7 | 0.8749 | 5/4 | re-avistado |
| 6 | exportacion | `export_administration_regulations` | `regulaciones_exportacion_ear` | 64.5 | 0.9432 | 6/4 | nuevo |
| 7 | core | `customer_discovery_cuatro_fases` | `customer_discovery_overview` | 80.7 | 0.9334 | 4/4 | nodo ya avistado |
| 8 | core | `cumplimiento_magnuson_moss` | `regla_disponibilidad_previa_venta` | 31.7 | 0.9324 | 4/3 | nuevo |
| 9 | franquicias | `gestion_terminacion_franquiciado` | `terminacion_franquiciado_causas` | 57.1 | 0.9309 | 5/4 | nuevo |
| 10 | quality | `eliminacion_causas_error` | `eliminacion_causas_error_2` | 93.0 | 0.8119 | 4/6 | re-avistado |
| 11 | entrega | `calcular_peso_dimensional_antes_cotizar` | `medir_paquete_redondeando_hacia_arriba` | 37.2 | 0.9283 | 5/5 | nuevo |
| 12 | core | `contratos_de_servicio_garantia` | `diferenciacion_garantia_contrato_servicio` | 48.7 | 0.9258 | 3/4 | nuevo |
| 13 | exportacion | `export_administration_regulations` | `licencia_exportacion_regulaciones` | 38.9 | 0.9231 | 6/6 | nuevo |
| 14 | quality | `mantener_las_ganancias` | `sostener_las_ganancias` | 92.3 | 0.8886 | 5/5 | re-avistado |
| 15 | core | `clasificacion_garantia_full_limited` | `cumplimiento_magnuson_moss` | 35.9 | 0.9179 | 4/4 | nuevo |
| 16 | core | `gestion_sindicato_inversores` | `manejo_syndicate_inversion` | 58.4 | 0.9174 | 4/4 | nuevo |
| 17 | core | `asignacion_agil_de_recursos` | `presupuesto_agil_innovacion` | 40.7 | 0.916 | 4/4 | nuevo |
| 18 | core | `cumplimiento_magnuson_moss` | `evitar_terminos_enganosos_garantia` | 35.7 | 0.9154 | 4/3 | nuevo |
| 19 | core | `producto_unico_superior` | `ventaja_competitiva_producto` | 36.5 | 0.9143 | 8/4 | nuevo |
| 20 | seguridad_digital | `csf_funcion_recover` | `funcion_recover_restauracion` | 59.3 | 0.9136 | 6/4 | nuevo |
| 21 | quality | `accion_correctiva_5` | `accion_correctiva_6` | 45.4 | 0.9127 | 6/4 | re-avistado |
| 22 | core | `cumplimiento_magnuson_moss` | `regla_divulgacion_garantia` | 34.0 | 0.9124 | 4/3 | nuevo |
| 23 | quality | `desarrollar_controles_transferir_operaciones` | `desarrollo_de_controles_de_proceso` | 91.1 | 0.8442 | 5/6 | nuevo |
| 24 | franquicias | `deteccion_franquicia_inadvertida` | `prevenir_franquicias_inadvertidas` | 37.4 | 0.9099 | 4/4 | nuevo |
| 25 | entrega | `calcular_peso_dimensional_antes_cotizar` | `conocer_limites_peso_tamano_courier` | 47.3 | 0.9091 | 5/5 | nuevo |
| 26 | core | `seleccion_canal_distribucion` | `seleccion_canal_fisico` | 90.7 | 0.7111 | 5/4 | nuevo |
| 27 | quality | `innovacion_tipo_ii` | `tipos_innovacion_i_ii` | 51.5 | 0.9069 | 5/6 | nodo ya avistado |
| 28 | entrega | `acolchado_segun_forma` | `adaptar_empaque_segun_tipo_de_articulo` | 50.0 | 0.9068 | 5/5 | nuevo |
| 29 | quality | `relacion_largo_plazo_proveedor_unico` | `relaciones_largo_plazo_con_proveedores` | 46.3 | 0.9063 | 4/4 | re-avistado |
| 30 | quality | `sistema_responsabilidad_gerencial` | `sistema_responsabilidad_gerencial_2` | 90.6 | 0.8677 | 5/5 | re-avistado |

La cola completa, con los titulos de los dos lados y las marcas de procedencia, en `INTRA_DOMINIO_PARES.jsonl`.

## Que hacer con el tamano de esta cola

**Si la cola sale grande, no es un fallo del instrumento: es el tamano del problema.** El paso de lectura lo deciden el auditor y el fundador, como se hizo con la franja bajo el umbral. Las palancas, en orden de menor a mayor perdida de cobertura: **subir el umbral semantico** (la distribucion de arriba dice cuanto), **leer por dominio** en vez de por cola global, y **ordenar por senal** dejando la cola larga para tandas posteriores. **Lo que no se puede hacer es podarla en silencio**: si se corta, se escribe donde se corto y cuanto quedo sin mirar.

---

<!-- MANUAL -->

# ANOTACIONES A MANO

**TODO LO QUE SIGUE A LA MARCA `<!-- MANUAL -->` LO CONSERVA EL SCRIPT.**
`scripts/intra_dominio.py` regenera todo lo de arriba y **copia esta cola tal
cual** en cada regeneracion.

> **Por que existe esta marca, y la fecha importa.** Estas anotaciones se
> escribieron el 11 ago 2026 **dentro de un archivo generado**, con un aviso de
> procedencia que decia que una regeneracion las borraria. **Eso no es un aviso:
> es una averia esperando.** El mismo dia se mudaron aqui y se le anadio al
> script el codigo que respeta la marca. **Ahora el aviso sobra porque el
> problema no existe.**
>
> **Como se anade algo**: se escribe debajo de la marca. **Como se pierde**:
> borrando la marca. Nada mas.

---

## La calibracion del eje de titulo

**Escrita a mano el 11 ago 2026, y mudada el 11 ago 2026 a esta cola.** Ya no
corre peligro: vive debajo de la marca `<!-- MANUAL -->` y el script la preserva.

### El falso positivo conocido: PLANTILLA DE ID

**Los puestos 427 y 428 del cribado dispararon por titulo y salieron sanos los
dos**, y no por casualidad: **los dos son el mismo molde.**

| puesto | el par | titulo | semantica |
|---:|---|---:|---:|
| 427 | `key_partners_hypothesis` contra `key_resources_hypothesis` | **84,6** | **0,6992** |
| 428 | `plan_gestion_calidad` contra `plan_gestion_cambios` | **84,6** | **0,7077** |

> **El molde es `X_hypothesis` y `plan_gestion_X`**: dos ids construidos con la
> misma plantilla sobre contenidos que no se parecen. **La semantica de los dos
> esta muy por debajo del umbral de 0,78** y acerto; **el titulo se dejo enganar
> por la plantilla.**
>
> **Y en el 427 el propio nodo desmiente el par**: el paso 4 de
> `key_partners_hypothesis` manda *distinguir con claridad entre socios y
> recursos clave*.

### LA DECISION DEL AUDITOR, y sus tres partes

> **1. El umbral NO se toca a mitad de corrida.** Subir el umbral de titulo con
> 449 pares ya leidos partiria la cola en dos poblaciones distintas y ningun
> conteo posterior seria comparable con los anteriores. **La cola se lee entera
> con el instrumento con el que empezo.**
>
> **2. PLANTILLA DE ID queda registrado como falso positivo CONOCIDO**, y el
> cribador **lo despacha en la razon del veredicto** en vez de tratarlo como
> hallazgo nuevo cada vez. Basta con nombrarlo y seguir.
>
> **3. La leccion viaja al diseno del proximo instrumento**, no a este: **un eje
> de titulo que compare ids deberia descontar el prefijo o el sufijo comun de
> plantilla antes de puntuar**, o exigir que el titulo dispare acompanado de una
> semantica minima. **Aqui no se cambia nada; alli no se repite.**

**Lo que esto NO significa**: el eje de titulo no queda desacreditado. Sigue
siendo el que caza los pares de id casi identico que la semantica no siempre
sube, que es justo para lo que se puso. **Lo que queda medido es su modo de
fallo, y ahora tiene nombre.**
