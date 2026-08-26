# Costuras internas: nodos con texto repetido DENTRO de si mismos

**ESTE INSTRUMENTO CITA, NO JUZGA.** Hermano chico de `scripts/gradiente_pares.py`. **Un nodo en esta lista es una cita para leer, no una costura probada.** El veredicto es **lectura textual** del auditor con visto del fundador.

La clase nacio de dos hallazgos del gradiente: `plan_mejora_procesos` (puesto 83) y `economia_circular_como_modelo_de_negocio` (puesto 97). **No son duplicados entre nodos: son un solo nodo al que le sobran pasos.**

## Las dos señales

| señal | que caza | umbral |
|---|---|---:|
| **pareja de pasos** | el paso repetido casi literal (`token_sort_ratio`) | **80** |
| **alineacion de bloques** | la secuencia que vuelve a empezar, y **donde** | **44** |

**Basta con que dispare cualquiera, y se reportan las dos siempre**, como en el hermano mayor: el auditor necesita ver por que entro cada nodo.

### Por que hacen falta las dos, medido

**Con la señal de pareja sola, y en cualquier umbral, la calibracion no entra.** La mejor pareja interna de `plan_mejora_procesos` es **60.0** y la de `economia_circular` **54.7**; bajar el umbral hasta ahi caza **856 nodos, el 24 por ciento del catalogo**.

> **Una baranda que caza lo correcto no es estricta, esta rota.**

El motivo es que esas dos costuras son **parafrasis con cola distinta**, no copias. La señal de bloques las pone en los **puestos 7 y 32 de 567** y **acierta el corte exacto en las dos**.

> **CORRECCION DECLARADA (15 ago 2026, vuelta 34).** Las cifras del parrafo de arriba **son las del dia en que se calibro y se quedan escritas**, pero **hoy no se reproducen**: esta misma campaña destejio los dos nodos, y medidos contra el grafo de hoy dan **pareja 47,1 y 54,3** con **cinco pasos cada uno**. La señal de bloque se recalibro (`MIN_BLOQUE` de 3 a 2, señal para todo nodo de cuatro pasos o mas, `NO APLICA` explicito por debajo), y **la puerta de calibracion se mudo a las señales para que toda importacion la herede**. Detalle entero, con el costo medido, en el encabezado de `scripts/costuras_internas.py`.

> **SEGUNDA CORRECCION DECLARADA (19 ago 2026, vuelta 40).** La puerta de arriba **quedo EN ROJO desde aquella recalibracion**: `plan_mejora_procesos` daba **43,1 contra 44** y el instrumento **no entregaba nada** (exit 1). **El roto no era el instrumento: era el fixture.** La propia campaña recorto ese nodo por una operacion legitima (`OP-F-04-HOR`, commit `2bd8dd76`), que es lo que lo dejo rancio. **La puerta se reparo cambiandole el fixture, con criterio escrito, y SIN TOCAR NI UN UMBRAL NI UN NODO**: el retirado se queda declarado abajo con su motivo. **Lo que la reparacion NO arregla y no se disfraza: la cola sigue en el 42,3 por ciento del catalogo**, que es el pendiente de doctrina del `MIN_BLOQUE = 2` y **lo decide el fundador**.

## La calibracion conocida

**Los nodos contra los que se comprueba que el instrumento sigue cazando la clase para la que se construyo. Tienen que entrar TODOS**, y si falta uno el instrumento no entrega nada. **El criterio de eleccion esta escrito arriba de la lista en `scripts/costuras_internas.py`.**

| fixture | pasos | pareja | bloque | corte | margen sobre el umbral |
|---|---:|---:|---:|---:|---:|
| **CAZADO** `fases_traccion_producto` | 7 | 76.3 | 72.6 | 4 | +28.6 |
| **CAZADO** `reglas_brainstorming` | 8 | 54.3 | 49.3 | 2 | +5.3 |
| **CAZADO** `economia_circular_como_modelo_de_negocio` | 5 | 54.3 | 44.2 | 3 | +0.2 |

> **AVISO DE BORDE: 1 fixture o mas esta a menos de 1.0 puntos del umbral** (`economia_circular_como_modelo_de_negocio`). **No es un fallo y no cambia nada hoy**, pero es el mismo sitio del que vino la averia de la vuelta 34: un fixture al borde cae con cualquier recorte legitimo del nodo. **Se dice para que la proxima se vea venir.**

### Los fixtures RETIRADOS, que no se borran

**No gobiernan la puerta, pero se siguen midiendo y publicando en cada corrida**: un fixture retirado en silencio es una calibracion que nadie puede auditar.

| fixture retirado | cuando | por que | commit de origen | como quedo hoy |
|---|---|---|---|---|
| `plan_mejora_procesos` | 19 ago 2026, vuelta 40 | fixture RANCIO: la propia campana recorto el nodo por una operacion legitima y dejo de disparar (bloque 43,1 contra umbral 44, por 0,9 puntos), con lo que el instrumento se nego a entregar entero desde la vuelta 34 | `2bd8dd76` (OP-F-04-HOR, que lo lleva en su nomina) | sigue sin disparar: 5 pasos, pareja 47.1, bloque 43.1 (corte tras 2) |

## Conteos

**1440 nodos** en la cola, sobre 3196 activos.

| dominio | nodos |
|---|---:|
| core | 631 |
| quality | 363 |
| health_safety | 112 |
| environmental | 84 |
| franquicias | 76 |
| exportacion | 70 |
| compras | 33 |
| seguridad_digital | 29 |
| entrega | 25 |
| risk_management | 17 |

## Distribucion, para calibrar

| percentil | mejor pareja interna | alineacion de bloques |
|---|---:|---:|
| p50 | 50.6 | 45.9 |
| p90 | 57.7 | 51.6 |
| p99 | 65.9 | 56.8 |
| maximo | 86.6 | 72.6 |

Nodos evaluados por bloques (4 pasos o mas): **2112**. Los de menos dan **NO APLICA**, que no es cero.

## La franja 44 a 45: lo que el umbral viejo dejaba fuera

**208 citas** entraron al bajar el umbral de bloque de 45 a 44. **Van juntas aqui a proposito**, para que la lectura del auditor las encuentre sin rastrearlas por la cola.

| # | dominio | nodo | pasos | bloque | corte |
|---:|---|---|---:|---:|---:|
| 1 | core | `get_customers_funnel_webmobile` | 6 | 45.0 | 2 |
| 2 | core | `empathy_map` | 5 | 45.0 | 3 |
| 3 | exportacion | `financiamiento_sba_exportacion` | 6 | 45.0 | 3 |
| 4 | quality | `educacion_estadistica_para_la_calidad` | 5 | 45.0 | 3 |
| 5 | core | `test_card` | 6 | 45.0 | 4 |
| 6 | core | `diseno_para_sostenibilidad_cradle_to_cradle` | 4 | 45.0 | 2 |
| 7 | quality | `prepare_phase_roadmap` | 5 | 45.0 | 3 |
| 8 | core | `ecuacion_de_valor` | 4 | 45.0 | 2 |
| 9 | core | `strat_map_arenas_estrategicas` | 6 | 44.9 | 4 |
| 10 | health_safety | `sistemas_de_extincion_de_incendios` | 4 | 44.9 | 2 |
| 11 | core | `segmentos_de_clientes_problema_necesidad` | 6 | 44.9 | 3 |
| 12 | core | `framework_ones_and_twos` | 5 | 44.9 | 2 |
| 13 | compras | `prepara_posicion_agenda_antes_negociar` | 6 | 44.9 | 4 |
| 14 | health_safety | `materials_handling_safety` | 5 | 44.9 | 3 |
| 15 | core | `customer_validation_sell_phase` | 5 | 44.9 | 3 |
| 16 | core | `equipo_forma_t` | 4 | 44.9 | 2 |
| 17 | core | `diseno_sistemico_partes_interesadas` | 5 | 44.9 | 3 |
| 18 | core | `teatro_del_exito` | 4 | 44.9 | 2 |
| 19 | core | `identificar_high_value_jobs` | 4 | 44.9 | 2 |
| 20 | core | `fase_entendimiento_investigacion_mercado` | 6 | 44.9 | 4 |
| 21 | health_safety | `tripod_delta_general_failure_types` | 6 | 44.9 | 4 |
| 22 | core | `trade_off_responsividad_eficiencia` | 8 | 44.9 | 5 |
| 23 | core | `verificar_product_market_fit` | 5 | 44.9 | 3 |
| 24 | core | `customer_appreciation_pr` | 6 | 44.9 | 4 |
| 25 | core | `fase_acclimate_experiencia_cliente` | 5 | 44.9 | 3 |
| 26 | core | `experimentacion_iterativa_mercado_fisico` | 5 | 44.9 | 2 |
| 27 | franquicias | `decision_marca_comun_branding` | 4 | 44.9 | 2 |
| 28 | quality | `eliminacion_gestion_por_objetivos_y_numeros` | 4 | 44.9 | 2 |
| 29 | quality | `eliminar_trabajo_a_destajo` | 5 | 44.8 | 3 |
| 30 | environmental | `ubicacion_estrategica_ambiental` | 4 | 44.8 | 2 |
| 31 | quality | `identificacion_de_riesgos` | 6 | 44.8 | 3 |
| 32 | core | `embudo_get_keep_grow` | 8 | 44.8 | 3 |
| 33 | core | `realizar_pruebas_pasa_no_pasa` | 4 | 44.8 | 2 |
| 34 | quality | `muestreo_de_aceptacion` | 5 | 44.8 | 3 |
| 35 | quality | `conciencia_de_calidad_2` | 5 | 44.8 | 3 |
| 36 | core | `restricciones_extremas_como_innovacion` | 4 | 44.8 | 2 |
| 37 | core | `programa_referidos_exclusividad` | 4 | 44.8 | 2 |
| 38 | risk_management | `riesgo_del_negocio_o_del_proyecto` | 4 | 44.8 | 2 |
| 39 | exportacion | `piggyback_marketing` | 4 | 44.8 | 2 |
| 40 | core | `driver_produccion` | 4 | 44.8 | 2 |
| 41 | quality | `intercambio_de_roles_para_motivacion` | 6 | 44.7 | 3 |
| 42 | core | `mission_and_operations_planning` | 5 | 44.7 | 2 |
| 43 | core | `siete_razones_fracaso_productos` | 4 | 44.7 | 2 |
| 44 | quality | `revision_progreso` | 8 | 44.7 | 3 |
| 45 | quality | `superioridad_calidad_market_share` | 5 | 44.7 | 2 |
| 46 | entrega | `detectar_prioridad_cliente_entrega` | 5 | 44.7 | 3 |
| 47 | entrega | `medir_satisfaccion_real_del_cliente` | 5 | 44.7 | 2 |
| 48 | quality | `desplegar_metas_organizacion` | 5 | 44.7 | 2 |
| 49 | core | `preparar_contacto_clientes` | 6 | 44.7 | 2 |
| 50 | risk_management | `cultura_que_habla_del_riesgo_sin_miedo` | 4 | 44.7 | 2 |
| 51 | franquicias | `preparar_candidato_validacion` | 5 | 44.7 | 2 |
| 52 | core | `due_diligence_adquisiciones` | 6 | 44.7 | 4 |
| 53 | health_safety | `evaluacion_mejora_programa` | 6 | 44.7 | 4 |
| 54 | environmental | `alineacion_engagement_estrategia_general` | 4 | 44.7 | 2 |
| 55 | core | `work_breakdown_structure` | 5 | 44.7 | 3 |
| 56 | health_safety | `senalizacion_de_salidas` | 4 | 44.7 | 2 |
| 57 | quality | `eliminar_slogans_y_exhortaciones` | 5 | 44.7 | 2 |
| 58 | core | `personas_productos_ganancias_orden` | 4 | 44.7 | 2 |
| 59 | core | `sistema_captura_ideas` | 5 | 44.7 | 3 |
| 60 | core | `principios_lean_startup` | 5 | 44.7 | 2 |
| 61 | quality | `rol_del_equipo_de_trabajo_en_calidad` | 4 | 44.7 | 2 |
| 62 | core | `split_testing_experimentos_ab` | 5 | 44.7 | 3 |
| 63 | quality | `sostener_las_ganancias` | 6 | 44.7 | 4 |
| 64 | quality | `consejos_de_calidad` | 5 | 44.6 | 3 |
| 65 | quality | `graficos_control_atributos` | 5 | 44.6 | 3 |
| 66 | core | `original_issue_discount_oid` | 4 | 44.6 | 2 |
| 67 | quality | `necesidad_mantener_informado` | 4 | 44.6 | 2 |
| 68 | core | `dilema_riqueza_vs_control` | 6 | 44.6 | 4 |
| 69 | core | `lead_bullets_no_silver_bullets` | 5 | 44.6 | 3 |
| 70 | core | `gate2_second_screen` | 5 | 44.6 | 3 |
| 71 | risk_management | `correr_hacia_el_riesgo` | 5 | 44.6 | 2 |
| 72 | quality | `categorias_de_material_entrante` | 5 | 44.6 | 3 |
| 73 | core | `estilos_de_negociacion` | 4 | 44.6 | 2 |
| 74 | quality | `decision_aptitud_uso` | 6 | 44.6 | 3 |
| 75 | health_safety | `ergonomia_laboral` | 6 | 44.6 | 2 |
| 76 | environmental | `gestion_e_waste` | 5 | 44.6 | 3 |
| 77 | core | `gate4_go_to_testing` | 4 | 44.6 | 2 |
| 78 | quality | `mejora_continua_del_sistema` | 5 | 44.6 | 2 |
| 79 | core | `mapa_de_influencia` | 5 | 44.6 | 3 |
| 80 | quality | `metodologia_medicion_copq` | 5 | 44.6 | 3 |
| 81 | quality | `ciclo_shewhart_pdsa` | 5 | 44.5 | 2 |
| 82 | environmental | `plan_cambio_climatico` | 5 | 44.5 | 3 |
| 83 | exportacion | `desarrollo_plan_exportacion` | 6 | 44.5 | 3 |
| 84 | quality | `sistema_informacion_calidad` | 5 | 44.5 | 3 |
| 85 | quality | `mejora_de_proceso_como_via_a_productividad` | 5 | 44.5 | 3 |
| 86 | environmental | `alcance_profundo_cadena_suministro` | 4 | 44.5 | 2 |
| 87 | core | `amar_las_restricciones` | 4 | 44.5 | 2 |
| 88 | health_safety | `implementacion_controles` | 5 | 44.5 | 2 |
| 89 | quality | `circulos_de_calidad_para_mejora_operativa` | 5 | 44.5 | 3 |
| 90 | franquicias | `adaptabilidad_regional_concepto` | 5 | 44.5 | 3 |
| 91 | seguridad_digital | `csf_funcion_protect` | 7 | 44.5 | 5 |
| 92 | core | `customer_discovery` | 5 | 44.5 | 2 |
| 93 | entrega | `probar_empaque_antes_de_escalar_envios` | 5 | 44.5 | 2 |
| 94 | core | `plan_de_contingencia_b` | 5 | 44.5 | 2 |
| 95 | core | `test_rico_vs_rey` | 4 | 44.5 | 2 |
| 96 | core | `paradoja_responsabilidad_creatividad` | 5 | 44.5 | 3 |
| 97 | health_safety | `evitar_micro_matching` | 5 | 44.5 | 3 |
| 98 | exportacion | `marco_legal_comercio_electronico_internacional` | 6 | 44.5 | 3 |
| 99 | exportacion | `trade_fair_certification_program` | 5 | 44.5 | 3 |
| 100 | core | `starting_points_innovacion` | 4 | 44.5 | 2 |
| 101 | exportacion | `planificacion_itinerario_viaje_negocios` | 6 | 44.5 | 4 |
| 102 | environmental | `transicion_energia_diversa_renovable` | 4 | 44.5 | 2 |
| 103 | health_safety | `drift_hacia_el_fallo` | 4 | 44.5 | 2 |
| 104 | core | `determinar_monto_a_levantar` | 5 | 44.5 | 3 |
| 105 | core | `entrada_mercado_nuevo` | 5 | 44.5 | 3 |
| 106 | core | `buen_lugar_para_trabajar` | 4 | 44.5 | 2 |
| 107 | quality | `deteccion_de_lideres_y_rezagados` | 5 | 44.4 | 3 |
| 108 | core | `plan_gestion_comunicaciones` | 6 | 44.4 | 3 |
| 109 | quality | `diagrama_de_flujo_proceso_map` | 8 | 44.4 | 3 |
| 110 | compras | `registro_lecciones_aprendidas_compra` | 5 | 44.4 | 2 |
| 111 | core | `plan_gestion_recursos_humanos` | 5 | 44.4 | 2 |
| 112 | environmental | `marketing_verde_autentico` | 4 | 44.4 | 2 |
| 113 | core | `patrimonio_de_los_propietarios` | 4 | 44.4 | 2 |
| 114 | quality | `falacia_recompensa_loteria` | 6 | 44.4 | 3 |
| 115 | franquicias | `franquicia_unidad_individual` | 4 | 44.4 | 2 |
| 116 | core | `customer_insights_design` | 4 | 44.4 | 2 |
| 117 | core | `proteccion_organizacion_matriz_experimentos` | 5 | 44.4 | 2 |
| 118 | quality | `analisis_variacion_desempeno_servicio` | 5 | 44.4 | 2 |
| 119 | core | `optimizacion_embudo_get_customers` | 5 | 44.4 | 3 |
| 120 | quality | `rol_black_belt_six_sigma` | 6 | 44.4 | 3 |
| 121 | core | `genchi_gembutsu_salir_del_edificio` | 6 | 44.4 | 4 |
| 122 | quality | `lean_six_sigma_roadmap` | 5 | 44.4 | 3 |
| 123 | core | `gates_tempranos_flexibles` | 4 | 44.4 | 2 |
| 124 | environmental | `eficiencia_energetica_almacenes` | 4 | 44.4 | 2 |
| 125 | core | `transparencia_facturacion` | 4 | 44.4 | 2 |
| 126 | franquicias | `venta_primer_franquiciado` | 4 | 44.4 | 2 |
| 127 | core | `requirements_management_plan` | 5 | 44.4 | 3 |
| 128 | environmental | `metricas_impacto_ambiental` | 5 | 44.4 | 2 |
| 129 | core | `experiment_library` | 5 | 44.4 | 3 |
| 130 | core | `sintesis_hipotesis_modelo_negocio` | 5 | 44.3 | 3 |
| 131 | exportacion | `metodos_de_pago_internacional` | 4 | 44.3 | 2 |
| 132 | quality | `consejo_ejecutivo_calidad` | 5 | 44.3 | 2 |
| 133 | quality | `establecer_proyecto_y_metas_diseno` | 5 | 44.3 | 2 |
| 134 | health_safety | `enfoque_find_and_fix` | 4 | 44.3 | 2 |
| 135 | seguridad_digital | `que_es_cui` | 4 | 44.3 | 2 |
| 136 | core | `analisis_flujo_de_valor` | 6 | 44.3 | 4 |
| 137 | core | `gate_0_evaluacion_wishlist` | 5 | 44.3 | 3 |
| 138 | health_safety | `new_view_vs_old_view_de_error_humano` | 5 | 44.3 | 3 |
| 139 | exportacion | `documentacion_exportacion` | 6 | 44.3 | 4 |
| 140 | core | `gestion_equilibrio_familia_startup` | 4 | 44.3 | 2 |
| 141 | core | `seo_link_building` | 5 | 44.3 | 3 |
| 142 | core | `tipos_criterios_gate` | 5 | 44.3 | 2 |
| 143 | core | `contratar_cerrador_de_ventas` | 5 | 44.3 | 3 |
| 144 | health_safety | `equipos_alto_desempeno` | 4 | 44.3 | 2 |
| 145 | core | `linea_base_costos` | 4 | 44.3 | 2 |
| 146 | core | `option_pool_negociacion` | 4 | 44.3 | 2 |
| 147 | environmental | `energia_eolica_distribuida` | 4 | 44.3 | 2 |
| 148 | health_safety | `self_regulation_deregulation_tradeoffs` | 4 | 44.3 | 2 |
| 149 | quality | `mantenimiento_preventivo_orientado_al_cliente` | 5 | 44.3 | 3 |
| 150 | core | `plan_de_materiales_colaterales` | 5 | 44.3 | 3 |
| 151 | quality | `evaluacion_gestion_riesgos` | 6 | 44.3 | 4 |
| 152 | quality | `dmaic_fase_measure` | 7 | 44.3 | 4 |
| 153 | quality | `tipos_benchmarking_por_participante` | 4 | 44.2 | 2 |
| 154 | quality | `capacidad_proceso_concepto` | 6 | 44.2 | 2 |
| 155 | core | `economia_circular_como_modelo_de_negocio` | 5 | 44.2 | 3 |
| 156 | core | `traction_goal` | 7 | 44.2 | 4 |
| 157 | franquicias | `validacion_con_franquiciados` | 4 | 44.2 | 2 |
| 158 | core | `ways_to_grow_matrix` | 5 | 44.2 | 3 |
| 159 | core | `comprension_capacidades_limitaciones_ia` | 9 | 44.2 | 4 |
| 160 | franquicias | `contratar_abogado_franquicias` | 5 | 44.2 | 3 |
| 161 | quality | `diseno_implementacion_remedio` | 6 | 44.2 | 4 |
| 162 | franquicias | `desarrollo_value_proposition_usp` | 5 | 44.2 | 2 |
| 163 | health_safety | `organizaciones_alta_confiabilidad_hro` | 4 | 44.2 | 2 |
| 164 | core | `backlog_evolutivo_y_cronograma_flexible` | 5 | 44.2 | 2 |
| 165 | environmental | `evitar_greenwashing` | 5 | 44.2 | 2 |
| 166 | health_safety | `sesgo_retrospectivo` | 4 | 44.2 | 2 |
| 167 | health_safety | `reporte_casi_accidentes` | 4 | 44.2 | 2 |
| 168 | quality | `manejo_problemas` | 5 | 44.2 | 3 |
| 169 | exportacion | `international_partner_search` | 6 | 44.2 | 2 |
| 170 | environmental | `canales_comunicacion_estrategicos` | 4 | 44.2 | 2 |
| 171 | core | `gestion_de_las_cuatro_fases_del_negocio` | 4 | 44.2 | 2 |
| 172 | franquicias | `estrategia_redes_sociales_franquicias` | 5 | 44.2 | 2 |
| 173 | core | `mecanica_conversion_deuda` | 4 | 44.2 | 2 |
| 174 | risk_management | `anota_por_que_decidiste_asi` | 4 | 44.2 | 2 |
| 175 | environmental | `sistema_gestion_cumplimiento_ambiental` | 4 | 44.2 | 2 |
| 176 | franquicias | `metodologias_analisis_territorio` | 5 | 44.2 | 3 |
| 177 | core | `global_vs_local_maximum` | 4 | 44.1 | 2 |
| 178 | core | `activity_resource_requirements` | 4 | 44.1 | 2 |
| 179 | core | `calidad_de_ejecucion_proceso_innovacion` | 5 | 44.1 | 2 |
| 180 | environmental | `critica_del_pib_como_metrica_de_progreso` | 6 | 44.1 | 3 |
| 181 | quality | `gestion_resistencia_cultural_cambio` | 5 | 44.1 | 3 |
| 182 | quality | `reporte_gerencial_diagnostico_calidad` | 5 | 44.1 | 2 |
| 183 | seguridad_digital | `identify_mapeo_datos` | 5 | 44.1 | 3 |
| 184 | quality | `concepto_vs_tecnica` | 4 | 44.1 | 2 |
| 185 | franquicias | `consejo_asesor_franquiciados_fac` | 6 | 44.1 | 2 |
| 186 | core | `ciclo_construir_medir_aprender` | 4 | 44.1 | 2 |
| 187 | core | `pensamiento_visual_modelos_negocio` | 5 | 44.1 | 2 |
| 188 | core | `stage_gate_td_tecnologia` | 5 | 44.1 | 3 |
| 189 | quality | `organizacion_independiente_de_calidad` | 4 | 44.1 | 2 |
| 190 | core | `estrategia_crecimiento_clientes` | 6 | 44.1 | 3 |
| 191 | quality | `fomento_educacion_autoeducacion` | 4 | 44.1 | 2 |
| 192 | core | `customer_discovery_cuatro_fases` | 4 | 44.1 | 2 |
| 193 | core | `equity_crowdfunding` | 4 | 44.1 | 2 |
| 194 | core | `burn_rate_por_etapa` | 4 | 44.1 | 2 |
| 195 | franquicias | `decision_diy_vs_consultor_franquicia` | 5 | 44.1 | 2 |
| 196 | quality | `hojas_de_verificacion` | 5 | 44.0 | 2 |
| 197 | core | `vehiculos_autonomos_drones_supply_chain` | 5 | 44.0 | 3 |
| 198 | compras | `reconoce_las_tacticas_de_presion_y_urgencia_artificial_del_vendedor` | 5 | 44.0 | 2 |
| 199 | environmental | `nutrientes_biologicos` | 4 | 44.0 | 2 |
| 200 | core | `hoja_estimacion_costos` | 5 | 44.0 | 3 |
| 201 | quality | `caso_estudio_benchmarking_terminal` | 6 | 44.0 | 2 |
| 202 | core | `innovacion_abierta` | 8 | 44.0 | 6 |
| 203 | core | `term_sheet_disposiciones_vinculantes` | 5 | 44.0 | 3 |
| 204 | quality | `equipos_ruptura_vet` | 4 | 44.0 | 2 |
| 205 | quality | `estimacion_intervalos_confianza` | 5 | 44.0 | 3 |
| 206 | core | `pensar_en_grande_empezar_pequeno` | 4 | 44.0 | 2 |
| 207 | health_safety | `burocracia_de_seguridad` | 5 | 44.0 | 3 |
| 208 | core | `estrategia_multicanal_bienvenida` | 6 | 44.0 | 4 |

**El motivo del cambio fue un FALSO NEGATIVO medido**: `nucleo/propuesta_gasto_capital`, con costura confirmada por lectura, quedaba fuera por **0,9 puntos** (bloque 44,1). **La señal si lo habia visto**: su corte propuesto es tras el paso 5, exactamente donde la lectura encontro la costura.

## EL LIMITE DECLARADO, que bajar el umbral NO cierra

**Bajar el umbral recupera a ESE falso negativo. No cierra el mecanismo que lo produjo.**

> **Un comparador de tokens no ve equivalencias semanticas, a ningun umbral.** En el nodo recuperado, el paso 3 dice *"calcular NPV usando el hurdle rate"* y el 11 dice *"calcular el valor presente neto (VPN)"*. **Son la misma cosa con la sigla en dos idiomas, y para este instrumento se parecen un 46,2.**

**Las redes que quedan debajo, y por eso el limite se declara en vez de taparse:**

| red | que caza que este instrumento no |
|---|---|
| **(a) los rebotes del gradiente** | ya cazaron **cuatro** costuras sin buscarlas, leyendo pares por otra razon |
| **(b) el barrido semantico intra-dominio** del final | los embeddings **si** ven que `NPV` y `VPN` viven juntos |
| **(c) la pasada unica** | relee **entero** cada nodo que toca antes de destejerlo |

> **Ninguna cola sustituye a leer el nodo.** Este instrumento ordena la lectura; no la reemplaza.

## Los veinte primeros

| # | dominio | nodo | pasos | pareja | bloque | corte | entro por |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | quality | `diseno_de_procesos_por_caracteristicas` | 5 | 86.6 | 0.0 |  | pareja |
| 2 | core | `ratios_eficiencia_inventario` | 4 | 85.1 | 46.3 | 2 | pareja y bloque |
| 3 | quality | `control_estadistico_metodo_medicion` | 6 | 80.9 | 46.4 | 2 | pareja y bloque |
| 4 | core | `customer_development_weekly_lessons_learned` | 6 | 76.4 | 60.8 | 4 | bloque |
| 5 | core | `fases_traccion_producto` | 7 | 76.3 | 72.6 | 4 | bloque |
| 6 | core | `producto_como_servicio_de_acceso` | 8 | 71.0 | 67.0 | 4 | bloque |
| 7 | core | `efecto_bullwhip` | 6 | 69.7 | 53.0 | 3 | bloque |
| 8 | core | `blue_ocean_four_actions` | 7 | 68.4 | 66.1 | 3 | bloque |
| 9 | quality | `smed_setup_reduction` | 5 | 67.9 | 54.0 | 3 | bloque |
| 10 | core | `reunion_conclusion_proyecto` | 13 | 67.8 | 54.2 | 11 | bloque |
| 11 | environmental | `reduccion_cargas_regulatorias` | 5 | 67.4 | 47.1 | 2 | bloque |
| 12 | core | `reporte_estado_miembro_equipo` | 6 | 67.2 | 57.8 | 4 | bloque |
| 13 | quality | `modelo_transformacion_juran` | 4 | 67.1 | 51.2 | 2 | bloque |
| 14 | core | `activity_attributes` | 5 | 66.7 | 58.1 | 3 | bloque |
| 15 | core | `ejecucion_incremental_transicion_tecnologica` | 16 | 66.7 | 55.9 | 7 | bloque |
| 16 | quality | `implementacion_monitoreo_controles` | 6 | 66.7 | 46.6 | 3 | bloque |
| 17 | quality | `product_design_spreadsheet` | 5 | 66.3 | 49.7 | 2 | bloque |
| 18 | core | `mantener_puntaje_innovacion` | 7 | 65.9 | 47.7 | 4 | bloque |
| 19 | quality | `mapa_satisfaccion_importancia` | 4 | 65.9 | 54.0 | 2 | bloque |
| 20 | core | `cultura_de_experiencia` | 8 | 65.8 | 54.7 | 5 | bloque |

La cola completa, con los dos pasos de cada pareja, en `COSTURAS_INTERNAS.jsonl`.
<!-- MANUAL -->

# INFORME DE CIERRE DEL INSTRUMENTO

**TODO LO QUE SIGUE A LA MARCA `<!-- MANUAL -->` LO CONSERVA EL SCRIPT.**
`scripts/costuras_internas.py` regenera lo de arriba y **copia esta cola tal cual**
en cada regeneracion. La marca y el codigo que la respeta se anadieron el 11 ago
2026, la misma solucion que ya lleva `scripts/intra_dominio.py`.

**Cerrado el 11 ago 2026. Toda cifra de este informe esta RECOMPUTADA del archivo**
cruzando `docs/COSTURAS_INTERNAS.jsonl` con los veredictos escritos en
`docs/FICHA_SUBFUSION_GRADIENTE.md`.

> **LA COLA CIERRA: 128 citas, 128 veredictos propios.** Ninguno heredado de otro
> informe, ninguno pendiente. **Veintidos tandas.**

---

## 1. LAS CIFRAS FINALES

| | |
|---|---:|
| citas del instrumento | **128** |
| **costuras CONFIRMADAS** | **46** |
| citas FALSAS | **82** |
| **precision de la cola** | **36%** |

**La serie de la precision, tanda a tanda**: 73% con 22 leidas, 68% con 28, 65%
con 34, 65% con 40, 61% con 46, 56% con 52, 53% con 58, 53% con 64, 54% con 70,
57% con 76, 55% con 82, 51% con 88, 48% con 94, 48% con 95, 46% con 101, 45% con
102, 43% con 108, 40% con 114, 38% con 121 y **36% con 128**.

> **La precision baja de forma monotona desde la tanda 3 y eso NO es que el
> instrumento se degrade: es el orden de lectura.** La cola se leyo de mayor a
> menor senal, asi que lo bueno salio primero. **Un instrumento que ordena bien
> tiene que terminar con la precision cayendo.**

### Las 46 confirmadas, por forma

| forma | ejemplares | que le pasa al nodo |
|---|---:|---|
| **LA FORMA QUE PARTE** | **8** | un nodo lleva **dos temas**; la cirugia **separa** en dos nodos |
| **LA FORMA REPARTIDA** | **1** | un tema vive **partido en dos nodos**; la cirugia **reune** |
| **el resto** | **37** | **narraciones repetidas del mismo tema**; la cirugia **poda** |

> **La forma repartida es el espejo de la que parte, y nacio de una correccion
> mia**: el encargo daba por repetido el Bullseye en dos nodos y al verificarlo
> contra el grafo **cada nodo llevaba una mitad distinta**. **Cambiar el verbo,
> de podar a reunir, cambia la operacion entera.**

### Las 82 falsas, por clase

| clase | citas | por que no es costura |
|---|---:|---|
| **FALSO POSITIVO DE SECUENCIA LEGITIMA** | **74** | un procedimiento largo **que no se puede acortar ni reordenar**: cada paso necesita al anterior |
| **LARGO LEGITIMO** | **7** | checklists que el estandar de 3 a 6 pasos no contempla, y que **no estan repetidos: estan completos** |
| **DUO LEGITIMO** | **1** | **dos fuentes en secuencia temporal que no se solapan** |

> **LOS SIETE DEL LARGO LEGITIMO NO SE ARREGLAN UNO A UNO: son DECISION DE
> FUENTE.** Cuatro de los siete son formatos-lista del *Basic Guide*; el resto
> sale del mismo molde. **No se decide nodo por nodo si el checklist se parte: se
> decide una vez por libro y se aplica a todos sus nodos.**

---

## 2. LA HERENCIA PRINCIPAL: EL PREDICTOR DE FUENTES

> **CAVEAT DECLARADO, 12 ago 2026: CON EL CAMPO `fuente` SUCIO, ESTA CIFRA SOLO SIRVE
> PARA ORDENAR UNA COLA.**
>
> **El predictor separa por una propiedad del campo `fuente`: cuantos libros declara el
> nodo.** Y ese campo **no esta normalizado**. **MEDIDO HOY sobre el grafo: 128 grafias
> distintas en primera posicion para 55 libros canonicos**, y **140 si se cuentan todas
> las posiciones**. Hugos aparece con **dos** grafias y Horowitz con **tres**, varias
> truncadas a unos treinta caracteres.
>
> *(El encargo que trajo este caveat decia 129; medido hoy con el criterio de primera
> posicion son **128**. La diferencia es de una grafia y no mueve el argumento, pero se
> declara: **toda cifra lleva su criterio ademas de su corte**.)*
>
> **LA CONSECUENCIA ES DIRECTA SOBRE EL PREDICTOR Y NO SOBRE EL CENSO: un libro con dos
> grafias puede convertir un nodo de UN libro en uno de DOS**, que es exactamente la
> frontera por la que el predictor separa. **Un nodo que declare el mismo libro dos
> veces cae del lado del 91% sin serlo**, y hay al menos uno medido:
> `decision_de_vender_startup` lleva *The Hard Thing About Hard Thing* y *The Hard
> Thing About Hard Things* **en la misma linea**.
>
> **SU PRERREQUISITO TIENE NOMBRE: el campo `fuente` canonico.** **Hasta que eso corra,
> el 91 contra 4 ordena una cola y no prueba nada.**
>
> **Y ESTO NO CONTRADICE AL INFORME: LO CONFIRMA.** El propio informe ya declaro la
> deuda en su ultima linea, *auditar el campo `fuente` antes de fiarse del predictor
> para nada que no sea ordenar una cola*. **Este caveat solo pone la cifra de la averia
> al lado de la deuda, y le da dueno.**

**Es lo mas util que deja esta campana, y llego por un camino que no era el
previsto.**

| | citas leidas | confirmadas | tasa |
|---|---:|---:|---:|
| **nodos de DOS o mas libros** | **47** | **43** | **91%** |
| **nodos de UN solo libro** | **81** | **3** | **4%** |
| | **128** | **46** | 36% |

> **Veintitres veces mas probable.** Un nodo que declara dos libros confirma nueve
> de cada diez veces; uno que declara uno solo, cuatro de cada cien.
>
> **Y el reparto de la cola no explica el resultado**: 47 contra 81 no es un
> efecto de muestra pequena en ninguno de los dos lados.

**La racha final lo dice sin estadistica: CUARENTA Y CINCO citas de un solo libro
leidas seguidas, de la tanda 15 a la 22, sin UNA SOLA costura.** Las tres
confirmadas de un solo libro son todas anteriores a la tanda 15.

> **EL INSTRUMENTO SE CONSTRUYO SOBRE DOS SENALES DE TEXTO, el bloque y la
> pareja, y las dos resultaron ruidosas. La senal que si separa no estaba en el
> texto: estaba en el campo `fuente`, que nadie habia mirado.**

### LA SALVEDAD, y sin ella el predictor se usa mal

> **El campo `fuente` tiene ruido medido, y esta medido en otra ficha**
> (`campos-sucios-dataset`, en `docs/PENDIENTES.md`): **1.314 nodos del catalogo,
> el 34,3%, declaran una fuente que no es el titulo de la obra** sino un nombre de
> archivo truncado o un codigo de documento. **Y once obras aparecen con dos o
> tres grafias distintas.**
>
> Ademas hay ruido de contenido: **`gestion_libro_abierto_obm` declara un libro
> cuyo material no aparece en ningun paso.**
>
> **El predictor es bueno y su base NO esta auditada.** Auditarla es del barrido.

### LA REGLA DE USO, que es la que impide el mal uso

> **EL PREDICTOR ORDENA LA LECTURA. NO DICTA EL VEREDICTO.**
>
> **Probado en los dos sentidos dentro de esta misma campana**:
> `manejo_empleados_en_adquisicion` declara dos libros, entro alto en la cola por
> eso, **y salio FALSA**. La senal acerto al ponerlo arriba; **el veredicto siguio
> siendo de la lectura**, como en las 128.
>
> **Lo que el predictor sirve para hacer**: decidir por donde empezar cuando hay
> mas cola que tiempo. **Lo que no sirve para hacer**: cerrar un nodo sin abrirlo.

### EL PUNTO CIEGO DEL INSTRUMENTO, declarado el 11 ago 2026

**Se anade a la herencia y NO toca ninguna cifra: las 128 siguen siendo 128 y el
cierre sigue cerrado.** Lo que se declara es **un limite del instrumento**, que
es informacion sobre lo que midio, no una medicion nueva.

> **LAS DOS SENALES MIDEN REPETICION. Un nodo que lleva DOS TEMAS PEGADOS SIN
> REPETIR NADA no dispara ninguna de las dos.**

**El ejemplar es `core/retention_metrics`**, hallado **despues del cierre** y por
el otro eje, en el puesto 522 del cribado intra-dominio. **Nueve pasos, dos
fuentes**, y el corte se ve en el vocabulario: del 1 al 5 se mide **lo que el
cliente hace**, del 6 al 9 **lo que el cliente cuesta**, con su propia jerga de
CAC, punto de equilibrio e impacto financiero. **Ninguno de los nueve pasos
repite a otro**, y por eso la cola no lo tenia.

> **Es LA FORMA QUE PARTE en estado puro.** Los ocho ejemplares que si entraron
> disparaban porque **ademas** repetian algo. **Esta es la forma sin su
> acompanamiento, y es invisible para este instrumento.**
>
> **LA RED QUE LO CUBRE ES EL EJE INTRA-DOMINIO, y lo cubre DE REBOTE**: un nodo
> con dos temas **se parece a los vecinos de cada uno de los dos**, asi que entra
> en la cola del otro eje por partida doble aunque no repita nada por dentro.
>
> **Los dos instrumentos no se solapan: se tapan los agujeros.** El de costuras
> mira dentro del nodo; el intra mira entre nodos; **y la forma que parte pura
> solo se ve desde fuera.**

**Lo que aparezca por esta via se anota en `COSTURAS FUERA DE COLA`**, en
`docs/FICHA_SUBFUSION_GRADIENTE.md`, **no aqui**: este informe dice lo que el
instrumento vio.

---

## 3. LAS REGLAS DE CORTE, con sus cifras finales

**El `corte` es donde el instrumento cree que empieza la segunda narracion. Se
midio si predice, y la respuesta es que no.**

| regla | cifra final | veredicto |
|---|---|---|
| **el corte 3 NO es evidencia** | **53 citas de corte 3, 4 confirmadas** | Cuarenta y nueve cayeron al abrir los pasos. **Un corte bajo es lo normal en un procedimiento corto.** |
| **la pareja como senal UNICA no cazo nada** | **4 citas de solo pareja, 0 confirmadas** | El eje de pareja sin el de bloque **no encontro ni una costura en toda la campana** |
| **corte 8 o mas predice costura, SALVO formato lista** | se cumple con la salvedad | La rompio `elementos_plan_exportacion_ejemplo`, corte 10 y FALSA, que es un formato lista |
| **mirar la pareja dentro del corte 3 no ayuda** | la pareja mas alta de ese grupo es de una FALSA | **La regla que se quiso escribir no se sostuvo con los datos** |

> **LO QUE EL EJE DE PAREJA SI ENSENA, y salio en la ultima tanda**: sus tres
> citas mas altas que no son copia **son las tres SIMETRIA DELIBERADA**, la
> comprobacion en los dos sentidos, los dos polos de una tecnica, el cruce
> completo de un estudio de medicion. **En su extremo superior, el eje de pareja
> caza al que escribe bien.**

> **PRECISION SOBRE EL CAMPO `pareja`, verificada en las 128 entradas**: son **dos
> indices de pasos DEL MISMO NODO**, no dos nodos. **Las dos senales del
> instrumento son internas las dos**, y por eso el cribado intra-dominio es otro
> eje y no un solapamiento.

---

## 4. LA ASIMETRIA NUCLEO-MUNDOS, final

| | |
|---|---:|
| confirmadas en nodos del **NUCLEO** | **45** |
| confirmadas en nodos de **MUNDO** | **1** |
| | **46** |

**La unica excepcion es `quality/planificacion_recoleccion_datos`.**

> **Cuarenta y cinco de cuarenta y seis.** La costura interna es **un fenomeno del
> nucleo**, y eso encaja con la vara del gradiente: **el nucleo se escribio
> primero, con mas fuentes y mas pasadas, y ahi es donde se apilaron las
> narraciones.**

---

## 5. LOS RACIMOS COSTURADOS TRANSVERSALES

**Dos racimos donde la costura interna y la duplicacion entre nodos son el mismo
problema, y por eso se destejen juntos.**

### Numero 1: la familia de la EXPERIENCIA del cliente

**Cinco vertices: tres costurados y dos sanos que son DESTINO del material que
sobra.** El destejido de los tres reparte hacia los dos, en vez de podar y tirar.

> **Y tiene un quinto vertice que hay que fabricar**: el destejido conjunto tiene
> que mirar a `fase_affirm_buyers_remorse` como destino aunque hoy no exista con
> ese contenido.

### Numero 2: el BULLSEYE partido en dos

**Es el ejemplar unico de LA FORMA REPARTIDA**, y su regla no es *decidir cual es
la copia* sino **decidir donde vive el original**.

---

## 6. LOS PATRONES DE FUENTE

> **CORRECCION DECLARADA, 12 ago 2026: la cuenta de DIECIOCHO es de 31 con la clase
> entera, y la nomina de Hugos que el plan usa es de 21 y no de 11. Ver la nota de la
> seccion 7, punto 1. Lo que NO cambia es la decision: siguen siendo TRES decisiones
> de fuente y no una lista de arreglos sueltos.**

> **CORRECCION DECLARADA ADITIVA, 14 ago 2026 (vuelta 26), al ejecutar `OP-F-01` en la
> pasada unica, y la de arriba se queda entera: son ~~31~~ TREINTA.** La clase LARGO
> LEGITIMO paso de SIETE a SEIS miembros por decision del fundador del 14 ago 2026 y la
> regla `P.17` del banco del plan (*la lectura vence al metadato*):
> `background_startup_vs_corporativo` estaba clasificado dos veces, aqui como formato
> lista por su metadato de fuente y en `OP-F-04-HOR` como injerto de Horowitz **leido y
> confirmado contra sus pasos con frontera escrita (1 a 4 de Wasserman, 5 a 9 de
> Horowitz)**, y gana la lectura. **6 mas 3 mas 21 = 30**, contado hoy sobre el campo
> `nodos` de las tres operaciones con `scripts/loop/vuelta26_medir.py`. **La fila de la
> tabla de abajo que dice *4 de los 7 LARGO LEGITIMO* se lee hoy como 4 de los 6.**

**Tres decisiones de fuente en la pasada unica, en vez de dieciocho arreglos de
nodo. Es la misma economia de la mesa de racimos.**

| patron | como se manifiesta | nodos |
|---|---|---:|
| **los formatos lista del `Basic Guide` y de Juran** | checklists largos que el estandar de 3 a 6 pasos no contempla, y que salen **FALSOS** | 4 de los 7 LARGO LEGITIMO |
| **la tanda de Mollick** | el metodo de taller rehecho con IA como segundo bloque, **CONFIRMADO** las tres veces | 3 |
| **el pegado de Hugos** | material de cadena de suministro adosado a nodos de otro tema, **CONFIRMADO** | 11 de las 46 |

> **El de Mollick sale mas raro de lo que parece, y la medicion lo agrava**: **51
> nodos declaran a Mollick y 48 son de tema IA por su propio id.** O sea que la
> tanda entro **dos veces y de dos maneras**: como familia propia de 48 nodos, que
> es lo correcto, **y ademas como injerto en 3 nodos de taller que ya existian**.
> **El material de IA ya tenia adonde ir: los injertos no se hicieron por falta de
> sitio.**

---

## 7. EL ESTADO, dicho sin adorno

> **NADA ESTA REPARADO. NINGUN NODO SE TOCO EN TODA LA CAMPANA.**
>
> **Las 46 costuras confirmadas, las 8 de la forma que parte, la repartida, los
> dos racimos transversales y los tres patrones de fuente PASAN ENTEROS AL PLAN DE
> LA PASADA UNICA.** Este instrumento **citaba y medía**; **no arregla.**

**Lo que el plan de la pasada unica recibe de aqui, en orden de coste:**

1. **Tres decisiones de fuente** que cubren dieciocho nodos.
   > **RECOMPUTADA CON SU CORTE, 12 ago 2026, tras la adjudicacion de que MANDA LA
   > CLASE y no la cuenta.** La cuenta de 18 tomaba **cuatro** miembros de la clase
   > LARGO LEGITIMO, los del *Basic Guide*, y dejaba fuera **tres** que estan en la
   > misma clase: dos de *Juran's Quality Handbook* y uno de `core`. **Con la clase
   > entera, el alcance de las tres decisiones es de 7 mas 3 mas 21 = 31 nodos**, no 18.
   >
   > **CORRECCION DECLARADA ADITIVA, 14 ago 2026 (vuelta 26), al ejecutar `OP-F-01`, y el
   > parrafo de arriba se queda entero: hoy son 6 mas 3 mas 21 = ~~31~~ 30 nodos.** El
   > uno de `core` que la correccion del 12 ago sumaba a la clase,
   > `background_startup_vs_corporativo`, **salio de ella el 14 ago 2026** por decision
   > del fundador y la regla `P.17` (*la lectura vence al metadato*): el mismo nodo estaba
   > LEIDO Y CONFIRMADO como injerto de Horowitz en `OP-F-04-HOR`, con su frontera de paso
   > publicada, y la pertenencia leida vence a la argumentada por metadato de fuente.
   > **El nodo no se pierde: se desteje por `OP-F-04-HOR`.** Medido hoy con
   > `scripts/loop/vuelta26_medir.py` sobre el campo `nodos` de las tres operaciones.
   >
   > **Y EL SALTO GRANDE NO ES ESE:** la nomina de Hugos, publicada como **11 de las 46
   > confirmadas**, se midio en **21 nodos vivos que declaran Hugos junto a otra
   > fuente**. **Los dos numeros conviven porque cuentan cosas distintas**: 11 son
   > costuras confirmadas con pegado de Hugos, 21 son todos los nodos con la firma del
   > injerto. **La cifra que el plan usa es la de 21, por adjudicacion.**
2. **Dos racimos transversales** que se destejen juntos, con reparto en vez de poda.
3. **Nueve cirugias de forma**: ocho que parten, una que reune.
4. **Treinta y siete podas** de narracion repetida, la primera de ellas
   `producto_minimo_viable`, elegida **no por ser la mayor sino por ser la mas
   barata**: su material sobrante ya esta localizado paso por paso, asi que el
   destejido deja de ser un juicio y pasa a ser una lista de borrados.

> **Y la deuda que este informe deja abierta y no cierra**: **auditar el campo
> `fuente`** antes de fiarse del predictor para nada que no sea ordenar una cola.
