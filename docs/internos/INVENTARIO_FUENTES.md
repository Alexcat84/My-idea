# Inventario interno de fuentes por nodo

INTERNO. Decisiones del fundador del 27 sep 2026, puntos 1 y 4: cada nodo vivo con la lista COMPLETA de sus fuentes, la suya mas las de todos los nodos que absorbio por cualquier fusion y en cadena, sin limite. Lo genera `python scripts/fuentes_internas.py` (no se edita a mano) y es el mismo contenido que el campo interno `fuentes_internas` de cada nodo. El campo `fuente` no se toca. Nada de esto llega al cliente: ni a la web, ni a un documento, ni a un correo, ni a una respuesta de la IA (REGLA ESTRICTA del 26 sep 2026).

## Resumen

- Nodos vivos: 3634
- Con mas de un libro (fusiones entre libros distintos): 54
- Nodos que absorbieron a otros: 722 (1165 ids absorbidos)
- Fuentes distintas: 59
- Ids absorbidos sin fuente registrada en ningun sitio (referencias que nunca fueron nodo): 333

## Nodos con mas de un libro

| nodo | fuentes | absorbio |
|---|---|---|
| analisis_de_cohortes | The Startup Owner's Manual - Blank, Steve<br>The Lean Startup - Eric Ries | cohort_analysis_retencion, metricas_cohortes |
| arquetipos_de_cliente | The Startup Owner's Manual - Blank, Steve<br>The Lean Startup - Eric Ries | arquetipo_cliente, customer_archetypes |
| capacitacion_educacion_seguridad | OSHA3886<br>OSHA3885 | capacitacion_conciencia_programa, educacion_entrenamiento_seguridad |
| caracterizacion_priorizacion_peligros | OSHA3886<br>OSHA3885 | priorizacion_caracterizacion_peligros |
| ciclo_shewhart_pdsa | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev<br>Juran's Quality Handbook_ The C - Joseph A. Defeo | ciclo_pdsa, pdsa_shewhart_cycle |
| coeficiente_viral | The Startup Owner's Manual - Blank, Steve<br>Traction - Gabriel Weinberg |  |
| composicion_board_directors | Venture Deals - Brad Feld<br>The Founder's Dilemmas - Wasserman, Noam | board_composition_investors, board_directores_composicion, board_directores_formacion, board_of_directors_composition, composicion_del_consejo_board_composition, composicion_junta_directiva, gestion_de_board_de_directores |
| control_estadistico_de_procesos | Juran's Quality Handbook_ The C - Joseph A. Defeo<br>Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | control_estadistico_de_procesos_2 |
| coordinacion_sitios_multiempleador | OSHA3886<br>OSHA3885 | comunicacion_coordinacion_multiempleador, comunicacion_coordinacion_multiempleador_2, coordinacion_empleadores_multiples, coordinacion_multiempleador, establecer_comunicacion_efectiva_contratistas, establecer_comunicacion_efectiva_hostempleador, establecer_coordinacion_efectiva_contratistas, establecer_coordinacion_efectiva_hostempleador |
| costo_de_mala_calidad_copq | Juran's Quality Handbook_ The C - Joseph A. Defeo<br>Quality is free _ the art of making quality certain -- Philip B_ Crosby<br>Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | categorias_copq, categorias_costo_de_calidad, categorias_costos_calidad, concepto_costo_de_calidad, costo_de_calidad_5, costo_de_calidad_6, costo_de_la_calidad, costo_de_la_calidad_coq, costo_de_la_mala_calidad, costo_de_la_no_calidad, costo_de_mala_calidad, costo_de_mala_calidad_2, costo_de_mala_calidad_3, costo_de_mala_calidad_copq_2, costo_de_mala_calidad_copq_3, costo_de_mala_calidad_copq_4, costo_mala_calidad_copq, costo_pobre_calidad, costos_de_calidad_cuatro_categorias, costos_ocultos_calidad, cuatro_costos_de_calidad, impacto_calidad_en_costos |
| customer_retention_tactics | The Startup Owner's Manual - Blank, Steve<br>Never Lose a Customer Again - Joey Coleman | customer_retention_strategy, retencion_de_talento |
| decision_de_vender_startup | The Founder's Dilemmas - Wasserman, Noam<br>The Hard Thing About Hard Things - Ben Horowitz | board_decision_exit, estrategia_de_salida, estrategia_de_salida_exit, exit_strategy |
| division_trabajo_humano_ia | Essentials of Supply Chain Management - Michael H. Hugos<br>Co-Intelligence_ Living and Wor - Ethan Mollick | automatizacion_tareas_aburridas, descomposicion_tareas_trabajo, framework_tareas_ia_humano |
| embudo_secuencial_de_inversores | The Founder's Dilemmas - Wasserman, Noam<br>Venture Deals - Brad Feld | seleccion_etapa_fondo_vc |
| encuadre_desafio_diseno | The field guide to human-centered design<br>Change by Design, Revised and U - Tim Brown | how_might_we_brief_social, how_might_we_briefs, how_might_we_framing, how_might_we_hmw |
| evaluacion_mejora_programa | OSHA3885<br>OSHA3886 | correccion_deficiencias_programa_sst, evaluacion_mejora_programa_2, evaluacion_mejora_programa_3, evaluacion_periodica_programa_seguridad, verificacion_implementacion_programa_sst |
| funcion_protect_politica_seguridad | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC)<br>Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses | protect_medidas_tecnicas |
| funcion_respond_plan_incidentes | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC)<br>NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide | csf_funcion_respond |
| future_scenarios_planning | Business Model Generation - Osterwalder, Alexander<br>Winning at New Products - Robert G. Cooper | escenarios_futuros, planificacion_de_salida |
| get_visual | The field guide to human-centered design<br>Change by Design, Revised and U - Tim Brown | pensamiento_sistemico, pensamiento_visual |
| grafico_de_corrida_run_chart | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev<br>Juran's Quality Handbook_ The C - Joseph A. Defeo | run_chart_datos_temporales |
| identificacion_evaluacion_peligros | OSHA3885<br>OSHA3886 | identificacion_evaluacion_peligros_2 |
| identificacion_peligros_salud | OSHA3885<br>OSHA3886 | identificacion_peligros_salud_2 |
| identificacion_recopilacion_informacion_peligros | OSHA3885<br>OSHA3886 | recopilacion_informacion_peligros |
| identificar_earlyvangelists | The Startup Owner's Manual - Blank, Steve<br>Traction - Gabriel Weinberg | earlyvangelists, earlyvangelists_identificacion, identificacion_de_fallo_o_sintoma |
| implementacion_controles | OSHA3885<br>OSHA3886 | implementacion_controles_2 |
| inspeccion_lugar_trabajo_peligros | OSHA3885<br>OSHA3886 | inspeccion_sitio_peligros |
| intellectual_property_strategy | The Startup Owner's Manual - Blank, Steve<br>Venture Deals - Brad Feld | proteccion_propiedad_intelectual |
| investigacion_etnografica_ideacion | Winning at New Products - Robert G. Cooper<br>Change by Design, Revised and U - Tim Brown | etnografia_aplicada_en_equipos_multidisciplinarios, etnografia_de_proyecto, etnografia_investigacion_usuario, gobernanza_etica_proyecto, investigacion_de_usuario_ideo, observacion_etnografica_ideo |
| investigacion_incidentes | OSHA3885<br>OSHA3886 | investigacion_incidentes_2 |
| keep_customers_strategy | The Startup Owner's Manual - Blank, Steve<br>Never Lose a Customer Again - Joey Coleman | optimizacion_keep_retencion |
| key_resources_hypothesis | The Startup Owner's Manual - Blank, Steve<br>Business Model Generation - Osterwalder, Alexander | recursos_clave |
| liderazgo_gerencial_seguridad | OSHA3885<br>OSHA3886 | compromiso_gerencial_seguridad |
| lienzo_modelo_negocio | Business Model Generation - Osterwalder, Alexander<br>The field guide to human-centered design<br>Value Proposition Design | business_model_canvas_hcd, business_model_canvas_ideo, business_model_canvas_refresher, business_model_execution, business_model_generation:propuesta_valor, business_model_generation_lienzo, diseño_centrado_en_sistemas, mapa_ecosistema_business_model_generation, metricas_clave_modelo_negocio, modelo_negocio_sostenible_social, patrones_modelo_negocio, scaling_business_model |
| modelo_spin_preguntas | SPIN Selling - Neil Rackham<br>Traction - Gabriel Weinberg | framework_spin_selling, modelo_spin, modelo_spin_2, modelo_spin_secuencia_preguntas |
| normalizacion_de_la_desviacion | Managing the Risks of Organizat - Reason, J. T_<br>The Field Guide to Understandin - Dekker, Sidney | drift_hacia_el_fallo_2, regulador_fallas_sistemicas |
| nueve_pasos_iniciar_programa | OSHA3886<br>OSHA3885 | diez_pasos_iniciales_programa |
| participacion_trabajadores | OSHA3885<br>OSHA3886 | participacion_trabajadores_2 |
| peligros_emergencias_no_rutinarias | OSHA3885<br>OSHA3886 | peligros_emergencias_no_rutinarias_2 |
| pensamiento_convergente_divergente | Change by Design, Revised and U - Tim Brown<br>Business Model Generation - Osterwalder, Alexander | design_attitude_vs_decision_attitude, generar_multiples_opciones |
| pivote_estrategico | The Lean Startup - Eric Ries<br>The Startup Owner's Manual - Blank, Steve | manifiesto_regla4_iteraciones_pivotes, pivote_startup, pivotes_e_iteraciones |
| practica_de_observacion_atenta | Assembling Tomorrow: A Guide to Designing a Thriving Future<br>Change by Design, Revised and U - Tim Brown | field_observations_ideo, observacion_de_campo, observar_lo_ordinario |
| preferencia_de_liquidacion | Venture Deals - Brad Feld<br>The Founder's Dilemmas - Wasserman, Noam | liquidacion_preferencia_participante, liquidation_preference, liquidation_preference_basica, terminos_liquidacion_preferencia |
| prevencion_control_peligros | OSHA3885<br>OSHA3886 | jerarquia_controles, jerarquia_controles_2, prevencion_control_peligros_2 |
| principio_calidad_mvp | The Lean Startup - Eric Ries<br>The Hard Thing About Hard Things - Ben Horowitz |  |
| producto_minimo_viable | The Lean Startup - Eric Ries<br>The Startup Owner's Manual - Blank, Steve | minimum_viable_product_discovery, minimum_viable_product_mvp, mvp, mvp_minimo_viable, producto_minimo_viable_mvp |
| programa_seguridad_salud_ocupacional | OSHA3885<br>SMALL_BUSINESS | programa_seguridad_salud_ocupacional_2 |
| punto_equilibrio_calidad_inspeccion | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev<br>Juran's Quality Handbook_ The C - Joseph A. Defeo | economia_de_la_inspeccion, punto_equilibrio_calidad, regla_todo_o_nada_inspeccion |
| reglas_brainstorming | Business Model Generation - Osterwalder, Alexander<br>Change by Design, Revised and U - Tim Brown | brainstorm, brainstorming_divergente, brainstorming_efectivo, brainstorming_estructurado, brainstorming_ideacion, brainstorming_ideacion_ideo, brainstorming_ideo, construir_sobre_ideas_ajenas, generacion_ideas_brainstorming, generacion_ideas_brainstormings |
| search_for_business_model | The Startup Owner's Manual - Blank, Steve<br>Value Proposition Design<br>The Lean Startup - Eric Ries | busqueda_vs_ejecucion, customer_development_vs_business_plan, definicion_de_brief, definicion_de_pov_ideo, definicion_del_problema_de_diseño, definicion_del_problema_ideo, definicion_hipotesis_negocio, definicion_problema_diseno, definicion_problema_inicial, definicion_problema_sistemico, definicion_problema_social, definicion_startup, definicion_startup_busqueda_modelo_negocio, definicion_startup_incertidumbre, ideacion_busqueda_oportunidades, startup_como_busqueda_vs_ejecucion, startup_definition, the_lean_startup:experimentacion_validada |
| seguimiento_efectividad_controles | OSHA3885<br>OSHA3886 | seguimiento_efectividad_controles_2 |
| sesgo_retrospectivo_hindsight_2 | The Field Guide to Understandin - Dekker, Sidney<br>Managing the Risks of Organizat - Reason, J. T_ | sesgo_retrospectivo_hindsight |
| vesting_acciones_fundadores | Venture Deals - Brad Feld<br>The Founder's Dilemmas - Wasserman, Noam | eleccion_estructura_vesting_founder, emision_founders_stock, estructura_de_equity_fundadores, single_double_trigger_acceleration, stock_vesting_founders_employees, vesting_de_acciones_y_aceleracion, vesting_de_equity, vesting_golden_handcuffs |
| viral_loop_marketing | The Startup Owner's Manual - Blank, Steve<br>Never Lose a Customer Again - Joey Coleman<br>Traction - Gabriel Weinberg |  |

## Todos los nodos vivos

| nodo | n | fuentes |
|---|---:|---|
| ab_testing_optimizacion | 1 | The Startup Owner's Manual - Blank, Steve |
| abandonar_arreglos_rapidos | 1 | The Field Guide to Understandin - Dekker, Sidney |
| abastecer_flujo_candidatos | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| abolir_inspeccion_masiva | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| abordar_cinco_efes_venta | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| abrazar_incomodidad_arrancar_critica_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| abrazar_incomodidad_silencio_contar_seis | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| abrazar_la_incomodidad | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| abrazar_los_bordes_de_la_conciencia | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| abrir_debate_humor_explicar_proposito | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| abrir_discusion_notas_adhesivas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| acceptance_control | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| accident_proneness_fallacy | 1 | The Field Guide to Understandin - Dekker, Sidney |
| accidentes_individuales_vs_organizacionales | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| accidentes_organizacionales_por_mantenimiento | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| accion_correctiva | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| accion_correctiva_2 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| accion_correctiva_4 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| accion_correctiva_crosby | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| accion_correctiva_sistematica | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| accruals_y_activos_prepagados | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| aceleracion_de_gates | 1 | Winning at New Products - Robert G. Cooper |
| aceptacion_bienes_comprados | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| aceptacion_de_fallas_como_inevitables | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| aceptar_la_imperfeccion_del_diseno | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| acolchado_segun_forma | 1 | Guia de empaque para envios (FedEx) |
| acompaniar_mejores_equipo_socio | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| acordar_plan_conjunto_jefe | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| acquisicion_viral_engineering | 1 | The Startup Owner's Manual - Blank, Steve |
| acreditacion_organismos_certificadores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| actitud_de_experimentacion_organizacional | 1 | Change by Design, Revised and U - Tim Brown |
| activacion_lista_positiva | 1 | Cradle to Cradle - Michael Braungart |
| actividades_clave | 1 | Business Model Generation - Osterwalder, Alexander |
| activity_attributes | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| activity_duration_estimates | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| activity_list | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| activity_resource_requirements | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| activos_intangibles_amortizacion | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| actualizacion_hvac | 1 | The Green to Gold Business Play - Daniel C. Esty |
| actualizacion_iluminacion | 1 | The Green to Gold Business Play - Daniel C. Esty |
| actualizacion_manual_operaciones | 1 | Franchise Your Business - Mark Siebert |
| actualizacion_posiciones_existentes | 1 | The Founder's Dilemmas - Wasserman, Noam |
| actualizar_business_model_canvas_tuneup | 1 | The Startup Owner's Manual - Blank, Steve |
| actualizar_modelo_de_negocio_pivot_o_proceed | 1 | The Startup Owner's Manual - Blank, Steve |
| actuar_conducta_contraria_valores | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| acuerdo_de_co_venta_y_votacion | 1 | Venture Deals - Brad Feld |
| acuerdo_representante_servicio | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| acumulacion_capital_previo_fundacion | 1 | The Founder's Dilemmas - Wasserman, Noam |
| acumular_asuntos_importantes_fichero_espera | 1 | High Output Management - Andrew S. Grove |
| ad_tracking | 1 | Value Proposition Design |
| adaptabilidad_regional_concepto | 1 | Franchise Your Business - Mark Siebert |
| adaptacion_14_puntos_servicio_medico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| adaptacion_cultural_negocios_internacionales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| adaptacion_producto_estandares_tecnicos | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| adaptacion_producto_mercado_exterior | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| adaptacion_teorica_del_lean_startup | 1 | The Lean Startup - Eric Ries |
| adaptaciones_procedimentales | 1 | The Field Guide to Understandin - Dekker, Sidney |
| adaptaciones_sectoriales_iso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| adaptar_empaque_segun_tipo_de_articulo | 1 | Guia visual de empaque |
| adaptar_escucha_cultura_ajena | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| adherence_loop_diseno_temporal | 1 | Change by Design, Revised and U - Tim Brown |
| administracion_de_inspeccion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| admitir_errores_areas_mejora_propias | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| admitir_pronto_mal_desempenio_cuatro_razones | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| adn_de_innovacion_organizacional | 1 | Change by Design, Revised and U - Tim Brown |
| adopcion_liderazgo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| adopciones_industria_especifica_iso9000 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| adoptar_co_inteligencia_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| adoptar_nueva_filosofia | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| adquisicion_estrategica_resolver_crisis | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| advocacy_customer_journey | 1 | Never Lose a Customer Again - Joey Coleman |
| afinar_frente_difuso_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| afinar_motor_crecimiento | 1 | The Lean Startup - Eric Ries |
| agendar_cuidados_propios_cumplirlos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| agrupar_interrupciones_subordinados_reuniones_regulares | 1 | High Output Management - Andrew S. Grove |
| agrupar_tareas_semejantes_aprovechar_preparacion | 1 | High Output Management - Andrew S. Grove |
| ai_como_coach_personalizado | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| aim_of_leadership | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| ajustar_franqueza_oido_oyente | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| ajustar_plan_fuerzas_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| ajuste_iterativo_plan_franquicia | 1 | Franchise Your Business - Mark Siebert |
| alcance_profundo_cadena_suministro | 1 | The Green to Gold Business Play - Daniel C. Esty |
| alentar_asuntos_corazon_vigilar_final_reunion | 1 | High Output Management - Andrew S. Grove |
| alfabetizacion_en_materiales_maliciosos | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| alianzas_cross_industry | 1 | The Green to Gold Business Play - Daniel C. Esty |
| alineacion_bd_metricas_core | 1 | Traction - Gabriel Weinberg |
| alineacion_con_canvas | 1 | Value Proposition Design |
| alineacion_de_objetivos_en_sistemas | 1 | Change by Design, Revised and U - Tim Brown |
| alineacion_engagement_estrategia_general | 1 | The Green to Gold Business Play - Daniel C. Esty |
| alineacion_estrategica_despliegue | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| alineacion_etica_ia_negocio | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| alineacion_incentivos_desempeno | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| alineacion_stakeholders_ma | 1 | Venture Deals - Brad Feld |
| alineacion_ti_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| alinear_comunicar_tarjeta_puntuacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| alinear_equipo_proposito_comun | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| alinear_prioridades_reporte_directivo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| almacenamiento_liquidos_inflamables | 1 | SMALL_BUSINESS |
| alternativa_agency_relationship | 1 | Franchise Your Business - Mark Siebert |
| alternativa_business_opportunity_licensing | 1 | Franchise Your Business - Mark Siebert |
| alternativa_dealership_distributorship | 1 | Franchise Your Business - Mark Siebert |
| alternativa_joint_venture | 1 | Franchise Your Business - Mark Siebert |
| alternativa_operaciones_propias | 1 | Franchise Your Business - Mark Siebert |
| alternativa_trademark_licensing | 1 | Franchise Your Business - Mark Siebert |
| amar_las_restricciones | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| amara_law_expectativas_tecnologia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| amenaza_y_oportunidad | 1 | Edwards et al., Managing Project Risks |
| amortizacion_y_periodo_de_gracia | 1 | Venture Deals - Brad Feld |
| analisis_antiguedad_cuentas_por_cobrar | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| analisis_beneficio_costo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_cadena_de_valor | 1 | Winning at New Products - Robert G. Cooper |
| analisis_capacidad_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_capacidad_procesos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_causa_efecto_indicadores_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| analisis_causa_raiz_defectos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| analisis_causa_raiz_despido_ejecutivo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| analisis_competencia_franquicias | 1 | Franchise Your Business - Mark Siebert |
| analisis_competitivo | 1 | Winning at New Products - Robert G. Cooper |
| analisis_competitivo_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_competitivo_deconstruccion | 1 | Winning at New Products - Robert G. Cooper |
| analisis_conversacional | 1 | The Field Guide to Understandin - Dekker, Sidney |
| analisis_costo_entrada_mercado | 1 | The Startup Owner's Manual - Blank, Steve |
| analisis_datos_atributos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_datos_reporte_estatus | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| analisis_de_capacidad_de_recursos | 1 | Winning at New Products - Robert G. Cooper |
| analisis_de_cohortes | 2 | The Startup Owner's Manual - Blank, Steve<br>The Lean Startup - Eric Ries |
| analisis_de_gastos_de_capital | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| analisis_de_ratios_financieros | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| analisis_de_sensibilidad_riesgo | 1 | Winning at New Products - Robert G. Cooper |
| analisis_de_sistemas_de_medicion_msa | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_del_extremo_organizacional | 1 | The Field Guide to Understandin - Dekker, Sidney |
| analisis_distribucion_poisson_para_capacidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| analisis_factores_distales_proximales | 1 | The Field Guide to Understandin - Dekker, Sidney |
| analisis_flujo_de_valor | 1 | Winning at New Products - Robert G. Cooper |
| analisis_flujo_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_flujo_proceso_servicio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_identificacion_mejores_practicas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_licitaciones_no_ganadas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_motivaciones_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| analisis_pareto_de_proveedores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_pareto_proyectos_elefante | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_porcentual_estados_financieros | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| analisis_regresion_correlacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_reporte_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_sintomas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_tco_roi_b2b | 1 | The Startup Owner's Manual - Blank, Steve |
| analisis_trafico_competitivo | 1 | The Startup Owner's Manual - Blank, Steve |
| analisis_valor | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_variacion_desempeno_servicio | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| analisis_varianza_financiera | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| analisis_vendibilidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| analisis_y_sintesis | 1 | Change by Design, Revised and U - Tim Brown |
| analogos_antilogos | 1 | The Lean Startup - Eric Ries |
| anatomia_proceso_arbol_ensamble | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| anillo_interior_explotar_el_canal_nucleo | 1 | Traction - Gabriel Weinberg |
| anota_por_que_decidiste_asi | 1 | Edwards et al., Managing Project Risks |
| antiboycott_regulations | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| anticipacion_riesgos_fundacionales | 1 | The Founder's Dilemmas - Wasserman, Noam |
| antidilucion_provisiones | 1 | Venture Deals - Brad Feld |
| antidilution_carve_outs | 1 | Venture Deals - Brad Feld |
| antidilution_weighted_average_broad_narrow | 1 | Venture Deals - Brad Feld |
| antigoals_framework | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| anunciar_decision_inesperada_reconvocar_reunion | 1 | High Output Management - Andrew S. Grove |
| apalancamiento_de_competencias_centrales | 1 | Winning at New Products - Robert G. Cooper |
| apalancamiento_personal_franquicia | 1 | Franchise Your Business - Mark Siebert |
| apertura_llamada_venta_grande | 1 | SPIN Selling - Neil Rackham |
| aplica_modelo_ackerman | 1 | Chris Voss, Rompe la barrera del no |
| aplicar_cinco_pasos_proceso_contratacion | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| aplicar_consecuencias_nota_apoyar_fuerzas_persona | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| aplicar_ejercicio_codigo_genetico_control | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| aplicar_metodo_ghsmart_contratacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| aplicar_metodo_promocion_sucesion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| aplicar_ocho_reglas_juego_personas | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| aplicar_regla_fija_de_colchon_de_relleno | 1 | Requisitos de empaque de los couriers |
| aplicar_seis_pasos_sistema_venta | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| aplicar_tacticas_maestras_entrevista | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| apoyar_una_causa | 1 | The Green to Gold Business Play - Daniel C. Esty |
| aprender_desde_el_amor_empatia | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| aprender_haciendo_dfe | 1 | The Green to Gold Business Play - Daniel C. Esty |
| aprender_resultados_vencer_dos_presiones | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| aprendizaje_institucionalizado_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| aprendizaje_organizacional_desde_incidentes | 1 | The Field Guide to Understandin - Dekker, Sidney |
| aprendizaje_validado | 1 | The Lean Startup - Eric Ries |
| aprobacion_alta_direccion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| arbol_decision_culpabilidad | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| archivar_indicadores_resolver_problemas | 1 | High Output Management - Andrew S. Grove |
| armar_plan_anual_crecimiento_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| arquetipos_de_cliente | 2 | The Startup Owner's Manual - Blank, Steve<br>The Lean Startup - Eric Ries |
| arquitectura_tecnica_modular | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| arrendamiento_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| arte_de_las_finanzas | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| articular_etica_valores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| asegurar_opinion_llega_persona | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| asignacion_agil_de_recursos | 1 | Change by Design, Revised and U - Tim Brown |
| asignacion_recursos_en_gates | 1 | Winning at New Products - Robert G. Cooper |
| asignar_entrevistas_enfocadas_equipo | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| asignar_responsable_unico_evolucion_planificada | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| asistencia_agencias_minoritarias_mbda | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| asistencia_apertura_franquicia | 1 | Franchise Your Business - Mark Siebert |
| asistencia_embajadas_consulados_comerciales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| asociacion_de_ideas | 1 | The Art of Thought - Wallas, Graham |
| asociaciones_clave | 1 | Business Model Generation - Osterwalder, Alexander |
| aspectos_legales_eticos_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| asset_deal_vs_stock_deal | 1 | Venture Deals - Brad Feld |
| assumption_constraint_log | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| asuncion_stock_options_adquisicion | 1 | Venture Deals - Brad Feld |
| asuntos_consumidor | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| ata_el_pago_al_cumplimiento_real_del_servicio | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| atacar_mercados_establecidos_con_problema | 1 | Winning at New Products - Robert G. Cooper |
| atencion_franquiciados_top | 1 | Franchise Your Business - Mark Siebert |
| atender_modo_supervivencia_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| atestiguar_sin_prejuicios | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| atribucion_retrospectiva_del_error | 1 | The Field Guide to Understandin - Dekker, Sidney |
| atributos_liderazgo_ceo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| atributos_mercado_chopra_meindl | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| audacia_del_cero | 1 | The Lean Startup - Eric Ries |
| audio_analysis_framework | 1 | The Green to Gold Business Play - Daniel C. Esty |
| auditar_calendario_reuniones_semana | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| auditar_formacion_premios_ultima_fila | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| auditoria_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| auditoria_calidad_proveedores | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| auditoria_de_posicionamiento | 1 | The Startup Owner's Manual - Blank, Steve |
| auditoria_de_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditoria_de_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditoria_de_producto_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditoria_energetica_sistematica | 1 | The Green to Gold Business Play - Daniel C. Esty |
| auditoria_negocio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditoria_presidente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditoria_responsabilidad | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| auditoria_sistema_control_calidad_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditoria_ti_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| auditorias_calidad_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditorias_gerenciales_periodicas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditorias_primera_segunda_tercera_parte | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auditorias_proveedores | 1 | The Green to Gold Business Play - Daniel C. Esty |
| auditorias_vigilancia_certificacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| auftragssystem_supervision_autonoma | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| ausencia_valor_verdadero | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| autenticidad_del_liderazgo_de_campo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| auto_inspeccion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| autoacusacion_antes_mala_noticia | 1 | Chris Voss, Rompe la barrera del no |
| autocertificacion_del_exportador | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| autocontrol_empoderamiento | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| autocontrol_planificacion_servicio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| autocontrol_y_controlabilidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| autoinspeccion_lugar_de_trabajo | 1 | SMALL_BUSINESS |
| automatic_conversion | 1 | Venture Deals - Brad Feld |
| automatizacion_software_gestion_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| autonomia_dependencia_regulatoria | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| autonomia_maestria_proposito | 1 | The Field Guide to Understandin - Dekker, Sidney |
| autoresponders_drip_campaigns | 1 | Franchise Your Business - Mark Siebert |
| autorizar_sistema | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| autorregulacion_seguridad | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| autoservicio_y_autosanacion_del_producto | 1 | Never Lose a Customer Again - Joey Coleman |
| avisar_organizador_reunion_prescindible | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| avisar_pronto_incumplimiento_expectativas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| ayudar_personas_jugar_fortalezas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| background_startup_vs_corporativo | 1 | The Founder's Dilemmas - Wasserman, Noam |
| backlog_evolutivo_y_cronograma_flexible | 1 | Winning at New Products - Robert G. Cooper |
| bad_apple_theory | 1 | The Field Guide to Understandin - Dekker, Sidney |
| bajar_detalle_organizacion_fuente_hechos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| balance_estructura_libertad_aprendizaje | 1 | The Art of Thought - Wallas, Graham |
| barreras_comerciales_no_arancelarias | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| barreras_entrada_competencia | 1 | Franchise Your Business - Mark Siebert |
| batna_definicion | 1 | Venture Deals - Brad Feld |
| bd_bajo_contacto_escalable | 1 | Traction - Gabriel Weinberg |
| benchmark_auditoria_energetica | 1 | The Green to Gold Business Play - Daniel C. Esty |
| benchmark_inversion_rd_industria | 1 | Winning at New Products - Robert G. Cooper |
| benchmarking_7_pasos_juran | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| benchmarking_desempeno_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| benchmarking_estrategia | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| benchmarking_prioritizacion_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| benchmarking_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| benchmarking_prospectivo_futuro | 1 | The Green to Gold Business Play - Daniel C. Esty |
| benchmarking_trilogia_juran | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| biblioteca_experimentos_validacion | 1 | Value Proposition Design |
| big_data_ia_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| biomimicry_conexiones_naturales | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| biomimicry_diseno | 1 | The Green to Gold Business Play - Daniel C. Esty |
| bioremediacion_living_machines | 1 | Cradle to Cradle - Michael Braungart |
| bloquear_tiempo_pensar_calendario | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| blue_ocean_four_actions | 1 | Business Model Generation - Osterwalder, Alexander |
| board_control_etapas_tardias | 1 | Venture Deals - Brad Feld |
| board_gridlock_y_directores_independientes | 1 | The Founder's Dilemmas - Wasserman, Noam |
| board_management_buyin | 1 | The Startup Owner's Manual - Blank, Steve |
| boxplot_resumen_datos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| bpm_gestion_excepciones | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| brainstorming | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| branding_etiquetado_empaque_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| breakthrough_cultural | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| breakup_fee_evaluation | 1 | Venture Deals - Brad Feld |
| brecha_capital_humano_founder | 1 | The Founder's Dilemmas - Wasserman, Noam |
| brecha_de_calidad_cuatro_gaps | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| brecha_entre_trabajo_prescrito_y_real | 1 | The Field Guide to Understandin - Dekker, Sidney |
| brief_competitivo | 1 | The Startup Owner's Manual - Blank, Steve |
| brief_de_diseno | 1 | Change by Design, Revised and U - Tim Brown |
| brokers_lead_referral_networks | 1 | Franchise Your Business - Mark Siebert |
| bucle_retroalimentacion_autoajustable | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| bucle_retroalimentacion_control | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| buen_lugar_para_trabajar | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| buenas_practicas_manufactura_cgmp | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| buggy_inert_knowledge | 1 | The Field Guide to Understandin - Dekker, Sidney |
| build_measure_learn | 1 | Value Proposition Design |
| bullseye_framework | 1 | Traction - Gabriel Weinberg |
| bundle_ideas | 1 | The field guide to human-centered design |
| burn_rate_por_etapa | 1 | The Startup Owner's Manual - Blank, Steve |
| burocracia_de_seguridad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| busca_el_riesgo_antes_de_que_te_busque | 1 | Edwards et al., Managing Project Risks |
| buscar_actividad_alta_palanca_tres_vias | 1 | High Output Management - Andrew S. Grove |
| buscar_armonia_diseno | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| buscar_recomendaciones_confianza | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| buscar_regularidad_bloques_iguales_trabajo_mando | 1 | High Output Management - Andrew S. Grove |
| business_excellence_models | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| business_materiality_assessment | 1 | The Green to Gold Business Play - Daniel C. Esty |
| business_model_canvas_scorecard | 1 | The Startup Owner's Manual - Blank, Steve |
| business_model_environment_mapping | 1 | Business Model Generation - Osterwalder, Alexander |
| business_plan_cinco_secciones | 1 | Business Model Generation - Osterwalder, Alexander |
| busqueda_ceo_sucesor_externo | 1 | The Founder's Dilemmas - Wasserman, Noam |
| busqueda_cofundador_complementario | 1 | The Founder's Dilemmas - Wasserman, Noam |
| butterfly_test_convergencia | 1 | Change by Design, Revised and U - Tim Brown |
| buy_a_feature_game | 1 | Value Proposition Design |
| buyer_rating_system | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| buyin_customer_development | 1 | The Startup Owner's Manual - Blank, Steve |
| cadena_reaccion_calidad_productividad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| cadena_suministro_respuesta_desastres | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| cadencia_seguimiento_prospectos | 1 | Franchise Your Business - Mark Siebert |
| calcula_costo_de_mantener_contra_costo_de_reponer | 1 | Max Muller, Essentials of Inventory Management |
| calcular_embudo_reclutamiento_propio | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| calcular_peso_dimensional_antes_cotizar | 1 | Guia de empaque para envios (FedEx) |
| calculo_contenido_valor_regional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| calculo_de_aranceles_importacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| calculo_ebitda | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| calculo_roi | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| calculo_roi_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| calculo_roi_franquiciado_2 | 1 | Franchise Your Business - Mark Siebert |
| calibra_tu_propio_ojo | 1 | Hubbard, The Failure of Risk Management |
| calibracion_intensidad_celebracion | 1 | Never Lose a Customer Again - Joey Coleman |
| calibrar_ascensos_evitar_politica | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| calibrar_decision_despido_documentarla | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| calibrar_normalidad_preguntas_jefe | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| calibrar_notas_reunion_jefes_pares | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| calibrar_vision_propia_opinion_ajena | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| calidad_de_diseno_vs_produccion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| calidad_de_ejecucion_proceso_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| calidad_del_servicio | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| calificacion_de_calidad_de_proveedores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| calificacion_de_proveedores_por_capacidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| calificacion_productos_procesos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| calificacion_prospectos_award | 1 | Franchise Your Business - Mark Siebert |
| calificacion_prospectos_marketing | 1 | Franchise Your Business - Mark Siebert |
| calificar_tarjeta_puntuacion_habilidad_voluntad | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| call_to_action_cta | 1 | Value Proposition Design |
| cambiar_forma_trabajar_conservar_plantilla | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| cambiar_formato_reunion_favorecer_participacion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| cambiar_mentalidad_fija_crecimiento | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| cambiar_posicion_hechos_explicar_cambio | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| cambiar_potencial_trayectoria_crecimiento | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| cambiar_saludo_cliente_dos_ramas | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| cambio_comportamiento_consumidor | 1 | The Green to Gold Business Play - Daniel C. Esty |
| canales_comunicacion_estrategicos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| canales_de_traccion_19 | 1 | Traction - Gabriel Weinberg |
| canales_distribucion | 1 | Business Model Generation - Osterwalder, Alexander |
| canales_link_sharing | 1 | Traction - Gabriel Weinberg |
| canalizar_interrupciones_cartel_hora_oficina | 1 | High Output Management - Andrew S. Grove |
| cap_table_basico | 1 | Venture Deals - Brad Feld |
| capacidad_de_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| capacidad_de_proceso_2 | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| capacidad_de_respuesta_responsable | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| capacidad_del_proceso | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| capacidad_proceso_concepto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| capacitacion_de_distribuidores | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| capacitacion_educacion_seguridad | 2 | OSHA3886<br>OSHA3885 |
| capacitacion_identificacion_peligros | 1 | OSHA3885 |
| capacitacion_roles_gerencia | 1 | OSHA3885 |
| capital_calls_lp | 1 | Venture Deals - Brad Feld |
| capital_financiero_cushion | 1 | The Founder's Dilemmas - Wasserman, Noam |
| capital_social_de_inversores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| capital_social_founder | 1 | The Founder's Dilemmas - Wasserman, Noam |
| capitalizacion_adecuada_del_franquiciador | 1 | Franchise Your Business - Mark Siebert |
| captura_conocimiento_mercado | 1 | The Startup Owner's Manual - Blank, Steve |
| capturar_conocimiento_de_mercado | 1 | The Startup Owner's Manual - Blank, Steve |
| caracteristicas_tareas_propensas_omision | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| caracterizacion_priorizacion_peligros | 2 | OSHA3886<br>OSHA3885 |
| card_sort | 1 | The field guide to human-centered design |
| cargos_extraordinarios_bandera_amarilla | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| carryover_fallas_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| carta_de_control_shewhart | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| carta_de_credito_letter_of_credit | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| carta_de_intencion_loi | 1 | Venture Deals - Brad Feld |
| carta_proyecto_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| casar_flujo_fabricacion_flujo_ventas | 1 | High Output Management - Andrew S. Grove |
| case_study_sistema_servicio_completo | 1 | The field guide to human-centered design |
| cash_burn_calculation | 1 | The Startup Owner's Manual - Blank, Steve |
| cash_in_advance | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| caso_estudio_benchmarking_terminal | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| caso_grietas_pequenas_mantenimiento_aeronaves | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| caso_taobao_evolucion_modelo | 1 | Value Proposition Design |
| catalogo_pivotes | 1 | The Lean Startup - Eric Ries |
| catch_ball_comunicacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| categorias_de_material_entrante | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| categorias_entusiasmo_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| categorizacion_ranking_proyectos_cubetas | 1 | Winning at New Products - Robert G. Cooper |
| causas_comunes_vs_especiales | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| causas_especiales_y_comunes_variacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| caza_las_oportunidades_no_solo_amenazas | 1 | Edwards et al., Managing Project Risks |
| ceder_autoridad_unilateral_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| ceder_control_reforzar_competencia_claridad | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| celebracion_automatizada_de_hitos | 1 | Never Lose a Customer Again - Joey Coleman |
| celebracion_hitos_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| celebrar_aceptacion_primer_dia | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| celebrar_logros_planificar_cambio | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| celebrar_pequenias_victorias | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| centaur_cyborg_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| centrar_debate_ideas_fuera_egos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| centro_asesoria_advocacy_center | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| ceo_de_guerra_vs_paz | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| ceo_equity_premium | 1 | The Founder's Dilemmas - Wasserman, Noam |
| ceo_puente_interino | 1 | The Founder's Dilemmas - Wasserman, Noam |
| cero_defectos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| cerrar_brecha_dos_preguntas_estrategia | 1 | High Output Management - Andrew S. Grove |
| cerrar_reunion_pasos_siguientes | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| certificacion_belts_six_sigma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| certificacion_cradle_to_cradle | 1 | The Green to Gold Business Play - Daniel C. Esty |
| certificacion_de_proveedores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| certificacion_leed_energy_star | 1 | The Green to Gold Business Play - Daniel C. Esty |
| certificacion_origen_producto | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| certificacion_profesional_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| certificacion_registro_sistema_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| certificaciones_ecoetiquetas | 1 | The Green to Gold Business Play - Daniel C. Esty |
| certificado_de_origen_coo | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| certificado_de_origen_tratados_libre_comercio | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| certificados_genericos_de_origen | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| change_log | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| channels_hypothesis_physical | 1 | The Startup Owner's Manual - Blank, Steve |
| channels_hypothesis_web_mobile | 1 | The Startup Owner's Manual - Blank, Steve |
| checklist_estandares_auditoria | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| checklist_mejores_apuestas_modelo_negocio | 1 | The Startup Owner's Manual - Blank, Steve |
| checklist_sistema_stage_gate_primera_clase | 1 | Winning at New Products - Robert G. Cooper |
| checkpoints_validacion | 1 | The Startup Owner's Manual - Blank, Steve |
| chief_sustainability_officer | 1 | The Green to Gold Business Play - Daniel C. Esty |
| ciclo_adaptativo_inteligencia | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| ciclo_circunstancias_sentimientos_ideas | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| ciclo_construir_medir_aprender | 1 | The Lean Startup - Eric Ries |
| ciclo_crear_medir_aprender | 1 | The Lean Startup - Eric Ries |
| ciclo_de_conversion_de_efectivo | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| ciclo_de_culpa_2 | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| ciclo_de_mejora_continua_helix | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| ciclo_pdca_pdsa | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| ciclo_shewhart_pdsa | 2 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev<br>Juran's Quality Handbook_ The C - Joseph A. Defeo |
| ciclo_ventas_calidad_franquicia | 1 | Franchise Your Business - Mark Siebert |
| ciclo_ventas_calidad_franquicia_2 | 1 | Franchise Your Business - Mark Siebert |
| ciclo_virtuoso_datos_electronicos | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| cierre_de_ciclos_industriales | 1 | The Green to Gold Business Play - Daniel C. Esty |
| cierre_satisfaccion_postventa | 1 | SPIN Selling - Neil Rackham |
| cierre_segun_complejidad_venta | 1 | SPIN Selling - Neil Rackham |
| cierre_term_sheet | 1 | Venture Deals - Brad Feld |
| cinco_artefactos_stage_gate | 1 | Winning at New Products - Robert G. Cooper |
| cinco_pasos_eco_efectividad | 1 | Cradle to Cradle - Michael Braungart |
| cinco_pasos_enfoque_restricciones | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| cinco_porques_master | 1 | The Lean Startup - Eric Ries |
| cinco_principios_guia_transformacion | 1 | Cradle to Cradle - Michael Braungart |
| cinco_suposiciones_erroneas_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| circulos_busqueda_cofundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| circulos_calidad_qc | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| circulos_de_calidad_para_mejora_operativa | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| circulos_de_calidad_qc_circles | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| claridad_especificaciones_instrucciones | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| clases_de_medidas_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| clasifica_tu_inventario | 1 | Max Muller, Essentials of Inventory Management |
| clasificacion_abc_prospectos | 1 | Franchise Your Business - Mark Siebert |
| clasificacion_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| clasificacion_caracteristicas_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| clasificacion_consultores_empleados | 1 | Venture Deals - Brad Feld |
| clasificacion_de_seriedad_de_defectos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| clasificacion_de_seriedad_de_defectos_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| clasificacion_garantia_full_limited | 1 | Businessperson's Guide to Federal Warranty Law |
| clasificacion_leads_abc | 1 | Traction - Gabriel Weinberg |
| clasificacion_riesgos_por_dominio | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| clasificacion_seriedad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| clasificacion_seriedad_defectos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| clasificacion_sistemas_por_nivel_seguridad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| clasificacion_tipos_activos | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| clasificar_tipo_paquete | 1 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria |
| clasificar_trabajo_proceso_montaje_prueba | 1 | High Output Management - Andrew S. Grove |
| clausula_antidesviacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| clausula_deber_general_osha | 1 | SMALL_BUSINESS |
| clausula_escape_contrato_representante | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| clausula_no_shop_adquisicion | 1 | Venture Deals - Brad Feld |
| clausula_personas_clave_banker | 1 | Venture Deals - Brad Feld |
| cliente_disena_producto | 1 | Winning at New Products - Robert G. Cooper |
| clonacion_replicacion_breakthrough | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| cloud_computing_supply_chain | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| co_creacion_estrategia_engagement | 1 | The Green to Gold Business Play - Daniel C. Esty |
| co_creation_session | 1 | The field guide to human-centered design |
| co_sale_drag_along_agreements | 1 | Venture Deals - Brad Feld |
| cobertura_de_intereses | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| codigo_conducta_orientado_cliente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| codigo_conducta_proveedores | 1 | The Green to Gold Business Play - Daniel C. Esty |
| coeficiente_viral | 2 | The Startup Owner's Manual - Blank, Steve<br>Traction - Gabriel Weinberg |
| cofundar_con_amigos_familia_riesgos | 1 | The Founder's Dilemmas - Wasserman, Noam |
| cognisance_organizacional | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| colaboracion_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| colaboracion_creador_consumidor | 1 | Change by Design, Revised and U - Tim Brown |
| colaboracion_industria_gobierno_estandares | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| colaboracion_transporte_ctm | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| collaboration_enablers | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| collaboration_roadblocks | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| colocar_etiquetas_de_manejo_correctamente | 1 | Guia de empaque para envios (FedEx) |
| combinacion_humano_ia_decision | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| comercio_electronico_fundamentos | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| comite_cero_defectos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| communicate_transparencia | 1 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses |
| community_building_estrategia | 1 | Traction - Gabriel Weinberg |
| commuting_teletrabajo_sostenible | 1 | The Green to Gold Business Play - Daniel C. Esty |
| como_ganan_dinero_los_vc | 1 | Venture Deals - Brad Feld |
| como_sabes_que_tu_metodo_sirve | 1 | Hubbard, The Failure of Risk Management |
| company_building | 1 | The Startup Owner's Manual - Blank, Steve |
| comparacion_metodos_inspeccion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| comparacion_metodos_inversion | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| comparar_motivacion_resultado_papel | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| compartir_datos_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| compartir_lecciones_aprendidas | 1 | The Green to Gold Business Play - Daniel C. Esty |
| compartir_logica_mostrar_razonamiento | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| compartir_opinion_conductual_regularidad | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| compatibilidad_de_visualizacion | 1 | The Field Guide to Understandin - Dekker, Sidney |
| compatibilidad_motivaciones_riqueza_control | 1 | The Founder's Dilemmas - Wasserman, Noam |
| compensacion_de_riesgo | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| compensacion_fundadores_cash_vs_equity | 1 | The Founder's Dilemmas - Wasserman, Noam |
| compensacion_service_providers | 1 | Venture Deals - Brad Feld |
| competencias_director_calidad_bloom | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| competencias_ingeniero_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| complejidad_acorde_capacidad_organizacional | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| composicion_board_directors | 2 | Venture Deals - Brad Feld<br>The Founder's Dilemmas - Wasserman, Noam |
| compra_energia_limpia | 1 | The Green to Gold Business Play - Daniel C. Esty |
| compra_equipos_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| compra_offsets_carbono | 1 | The Green to Gold Business Play - Daniel C. Esty |
| compra_por_precio_mas_bajo_como_error | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| comprender_alineacion_etica_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| comprender_definicion_legal_franquicia | 1 | Franchise Your Business - Mark Siebert |
| comprender_ia_como_tecnologia_de_proposito_general | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| comprension_brechas_desempeno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| comprension_capacidades_limitaciones_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| comprobar_confianza_persona_cargo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| comprobar_criticas_hombre_mujeres_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| comprobar_equipo_ejecuta_bien | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| comprobar_gusto_trato_personas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| comprobar_opinion_produce_mejora | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| compromiso_cliente_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| compromiso_gerencial_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| compromiso_linea_tiempo_cliente | 1 | Traction - Gabriel Weinberg |
| compromiso_organismico_en_la_accion | 1 | The Art of Thought - Wallas, Graham |
| computacion_en_la_nube | 1 | The Green to Gold Business Play - Daniel C. Esty |
| comunicacion_a_toda_la_empresa | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| comunicacion_aprendizaje_continuo | 1 | The Startup Owner's Manual - Blank, Steve |
| comunicacion_de_riesgos_quimicos | 1 | SMALL_BUSINESS |
| comunicacion_del_riesgo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| comunicacion_efectiva_con_franquiciados | 1 | Franchise Your Business - Mark Siebert |
| comunicacion_honesta_en_crisis_al_equipo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| comunicacion_interna_empleados | 1 | The Green to Gold Business Play - Daniel C. Esty |
| comunicacion_interna_post_despido_ejecutivo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| comunicacion_proactiva_puntos_estres | 1 | Never Lose a Customer Again - Joey Coleman |
| comunicacion_reporte_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| comunicacion_transparente_en_crisis | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| comunicar_politicas_organizacionales | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| comunicar_valores_diez_formas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| comunicar_vision_jugadores_organizacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| comunidad_como_activo_estrategico | 1 | Traction - Gabriel Weinberg |
| concepcion_hormica_del_pensamiento | 1 | The Art of Thought - Wallas, Graham |
| concepto_cuatro_pilares_programa_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| concepto_de_advances | 1 | Franchise Your Business - Mark Siebert |
| concepto_de_auditoria_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| concepto_de_crecimiento_regenerativo | 1 | Cradle to Cradle - Michael Braungart |
| concepto_de_dominancia | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| concepto_haciendo_la_calidad_cierta | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| concepto_patrimonio_equity | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| concepto_producto_plus | 1 | Cradle to Cradle - Michael Braungart |
| concepto_programa_catorce_pasos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| concepto_proyecto_breakthrough | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| concepto_quality_is_free | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| concepto_reconocimiento_ring_of_quality | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| concepto_variacion_estadistica | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| concepto_vs_tecnica | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| conciencia_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| conciencia_de_calidad_2 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| concientizacion_entrenamiento_cui | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| concierge_mvp | 1 | The Lean Startup - Eric Ries |
| concurrent_engineering | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| condiciones_de_cierre_adquisicion | 1 | Venture Deals - Brad Feld |
| condiciones_latentes_largo_plazo | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| condiciones_latentes_organizacionales | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| condiciones_latentes_riesgo_universal | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| conditions_precedent_financing | 1 | Venture Deals - Brad Feld |
| conducir_entrevista_cronologica_trayectoria | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| conducir_etapas_modelo_ideal_decision | 1 | High Output Management - Andrew S. Grove |
| conducir_llamadas_referencia | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| conducir_reunion_equipo_agenda_tres_bloques | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| conducir_reunion_individual_telefono_distancia | 1 | High Output Management - Andrew S. Grove |
| conducir_reuniones_salto_nivel_diez_reglas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| conexion_comportamiento_proceso | 1 | The Field Guide to Understandin - Dekker, Sidney |
| conexion_flujos_energia_natural | 1 | Cradle to Cradle - Michael Braungart |
| conexion_personal_emocional | 1 | Never Lose a Customer Again - Joey Coleman |
| confianza_mutua_fundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| confidencialidad_nda_adquisicion | 1 | Venture Deals - Brad Feld |
| conflicto_de_objetivos_en_organismos_reguladores | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| conformidad_comercio_internacional | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| conformidad_especificacion_aptitud_uso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| confusion_de_modos_automatizacion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| conoce_insumos_vitales | 1 | Max Muller, Essentials of Inventory Management |
| conocer_fuerzas_valores_sesgos_propios | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| conocer_limites_peso_tamano_courier | 1 | Guia visual de empaque |
| conocimiento_detallado_y_justicia | 1 | The Field Guide to Understandin - Dekker, Sidney |
| conocimiento_local_colaboracion | 1 | Change by Design, Revised and U - Tim Brown |
| consecuencias_no_intencionadas_sistemicas | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| consejo_asesor_franquiciados_fac | 1 | Franchise Your Business - Mark Siebert |
| consejo_calidad_informacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| consejo_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| consejo_de_calidad_2 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| consejo_de_calidad_3 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| consejo_de_calidad_y_rol_del_director | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| consejo_ejecutivo_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| consejos_de_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| consideraciones_instalacion_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| consignment | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| consistencia_decisiones_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| consolidacion_cargas_backhaul | 1 | The Green to Gold Business Play - Daniel C. Esty |
| consortium_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| constancia_de_proposito | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| constraint_management | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| construccion_capacidad_empleados | 1 | The Green to Gold Business Play - Daniel C. Esty |
| construccion_de_causas | 1 | The Field Guide to Understandin - Dekker, Sidney |
| construccion_de_leverage | 1 | Venture Deals - Brad Feld |
| construccion_de_valor_percibido | 1 | SPIN Selling - Neil Rackham |
| construccion_equipo_financiero | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| construccion_equipo_franquicia | 1 | Franchise Your Business - Mark Siebert |
| construccion_experticia_era_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| construccion_linea_tiempo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| construccion_red_profesional_integrada | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| construccion_relaciones_internacionales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| construccion_timeline_resolucion | 1 | The Field Guide to Understandin - Dekker, Sidney |
| construccion_tribu_de_marca | 1 | Never Lose a Customer Again - Joey Coleman |
| construccion_verde_nueva | 1 | The Green to Gold Business Play - Daniel C. Esty |
| construir_apoyo_equipo_directivo_metodo | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| construir_capacidad_evaluacion_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| construir_confianza_equipo_tiempo_solas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| construir_empresa_plantilla_vision_diaria | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| construir_equipo_perspectivas_diversas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| construir_estrategia_gente_cuatro_componentes | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| construir_flujo_produccion_paso_limitante | 1 | High Output Management - Andrew S. Grove |
| construir_fortalezas_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| construir_grafico_escalonado_pronosticos | 1 | High Output Management - Andrew S. Grove |
| construir_indicador_linealidad_alerta_temprana | 1 | High Output Management - Andrew S. Grove |
| construir_indicador_tendencia_patron | 1 | High Output Management - Andrew S. Grove |
| construir_mvp_baja_fidelidad | 1 | The Startup Owner's Manual - Blank, Steve |
| consultores_comercio_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| consumidor_como_eje_de_produccion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| contabilidad_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| contabilidad_basada_actividades | 1 | The Green to Gold Business Play - Daniel C. Esty |
| contabilidad_caja_vs_devengo | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| contabilidad_flujo_materiales | 1 | The Green to Gold Business Play - Daniel C. Esty |
| contabilidad_innovacion | 1 | The Lean Startup - Eric Ries |
| contabilidad_innovacion_largo_plazo | 1 | The Lean Startup - Eric Ries |
| contabilidad_innovacion_pivote | 1 | The Lean Startup - Eric Ries |
| contactar_despedido_mes_despues | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| contacto_con_el_cliente | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| contacto_evaluacion_representantes_extranjeros | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| contar_cuatro_historias_propias_ver_hueco_intencion | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| contar_firmas_cadena_tramite_parado | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| contar_historias_propias_explicar_franqueza_radical | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| content_marketing_blog | 1 | Traction - Gabriel Weinberg |
| contestar_dos_preguntas_direccion_objetivos | 1 | High Output Management - Andrew S. Grove |
| contextualizacion_datos_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| contract_close_out | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| contractor_status_report | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| contrarrestar_argumento_mercado | 1 | Venture Deals - Brad Feld |
| contrastar_cultura_actual_aspirada | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| contrastar_motivos_querer_gestionar | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| contratacion_acelerada_hipercrecimiento | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| contratacion_experiencia_vs_potencial | 1 | The Founder's Dilemmas - Wasserman, Noam |
| contratar_abogado_franquicias | 1 | Franchise Your Business - Mark Siebert |
| contratar_ambicion_correcta | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| contratar_cerrador_de_ventas | 1 | The Startup Owner's Manual - Blank, Steve |
| contratar_investigadores_reclutamiento | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| contratar_personas_capaces_mas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| contratar_por_fortaleza | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| contratar_reclutadores_externos | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| contratar_vendedor_franquicia | 1 | Franchise Your Business - Mark Siebert |
| contratos_de_servicio_garantia | 1 | Businessperson's Guide to Federal Warranty Law |
| contratos_desempeno_energetico_esco | 1 | The Green to Gold Business Play - Daniel C. Esty |
| contribucion_por_unidad_desventaja | 1 | Franchise Your Business - Mark Siebert |
| control_acceso_least_privilege | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| control_calidad_definicion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| control_calidad_operaciones_servicio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| control_charts_shewhart | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| control_del_board_startup | 1 | The Founder's Dilemmas - Wasserman, Noam |
| control_del_proceso_del_proveedor | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| control_estadistico_de_inventario_en_transito | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| control_estadistico_de_procesos | 2 | Juran's Quality Handbook_ The C - Joseph A. Defeo<br>Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| control_estadistico_de_procesos_en_tiempo_real | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| control_estadistico_del_proceso | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| control_estadistico_metodo_medicion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| control_estadistico_proceso | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| control_exportaciones_bis | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| control_minimizacion_datos | 1 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses |
| control_proceso_variables | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| control_responsabilidad_manual | 1 | Franchise Your Business - Mark Siebert |
| controles_no_rutinarias_emergencias | 1 | OSHA3886 |
| conversacion_emocional_postcompra | 1 | Never Lose a Customer Again - Joey Coleman |
| conversar_historia_vida_descubrir_motivadores | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| conversar_suenios_cruzar_habilidades | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| conversion_datos_co2e | 1 | The Green to Gold Business Play - Daniel C. Esty |
| conversion_rights | 1 | Venture Deals - Brad Feld |
| conversion_venta_empresa | 1 | Venture Deals - Brad Feld |
| convertible_debt_fundamentos | 1 | Venture Deals - Brad Feld |
| convertir_cualquiera_mentor | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| convertir_necesidad_en_demanda | 1 | Change by Design, Revised and U - Tim Brown |
| convertir_unknown_unknowns_en_known_unknowns | 1 | The Founder's Dilemmas - Wasserman, Noam |
| coordinacion_colaboracion_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| coordinacion_control_vs_cambio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| coordinacion_organica_de_elementos_independientes | 1 | The Art of Thought - Wallas, Graham |
| coordinacion_sitios_multiempleador | 2 | OSHA3886<br>OSHA3885 |
| copy_testing | 1 | The Startup Owner's Manual - Blank, Steve |
| coraje_decision_ceo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| coraje_en_decisiones_dificiles | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| coraje_para_pivotar | 1 | The Lean Startup - Eric Ries |
| correlacion_cero_muestra_remanente | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| correr_hacia_el_riesgo | 1 | DeMarco y Lister, Waltzing with Bears |
| correr_semana_arreglo_averias_gestion | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| cortar_discusion_libre_momento_justo | 1 | High Output Management - Andrew S. Grove |
| cortar_efecto_divisor_persona_brillante | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| coshh_procedimiento_rolling | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cost_management_plan | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| costeo_ciclo_de_vida | 1 | The Green to Gold Business Play - Daniel C. Esty |
| costo_de_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| costo_de_calidad_3 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| costo_de_calidad_diagnostico | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| costo_de_capital | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| costo_de_mala_calidad_copq | 3 | Juran's Quality Handbook_ The C - Joseph A. Defeo<br>Quality is free _ the art of making quality certain -- Philip B_ Crosby<br>Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| costo_de_oportunidad | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| costo_de_uso_life_cycle | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| costos_agencia_asimetria_informacion | 1 | Venture Deals - Brad Feld |
| costos_ocultos_accidentes_iceberg | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| costos_personal_franquicia | 1 | Franchise Your Business - Mark Siebert |
| costos_preparacion_franquicia | 1 | Franchise Your Business - Mark Siebert |
| costos_transaccion | 1 | Venture Deals - Brad Feld |
| covenants_control_terms | 1 | Venture Deals - Brad Feld |
| cradle_to_cradle_concepto | 1 | Cradle to Cradle - Michael Braungart |
| craft_positioning_statement | 1 | The Startup Owner's Manual - Blank, Steve |
| creacion_contenido_compartible | 1 | Traction - Gabriel Weinberg |
| creacion_data_warehouse | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| creacion_estrategia_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| creacion_option_pool | 1 | The Founder's Dilemmas - Wasserman, Noam |
| creacion_roles_c_level | 1 | The Founder's Dilemmas - Wasserman, Noam |
| creacion_valor_cliente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| crear_cultura_escucha_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| crear_espacio_seguro_madurar_ideas_nuevas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| crear_infraestructura_producto | 1 | The Green to Gold Business Play - Daniel C. Esty |
| crear_manuales_jugadas_repetibles | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| crear_obligacion_disentir_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| crear_pitch | 1 | The field guide to human-centered design |
| crear_plan_creible_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| crear_sistema_captura_seguimiento_candidatos | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| crear_tarjeta_puntuacion_puesto | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| create_a_concept | 1 | The field guide to human-centered design |
| crecimiento_desde_franquiciados_existentes | 1 | Franchise Your Business - Mark Siebert |
| crecimiento_ingresos_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| cribado_de_datos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| cribado_prueba_barata | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| cribar_candidatos_entrevista_telefonica | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| criterio_bazooka_peashooter | 1 | Franchise Your Business - Mark Siebert |
| criterios_baldrige_excelencia | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| criterios_de_exito_gate | 1 | Winning at New Products - Robert G. Cooper |
| criterios_diseno_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| criterios_equity_split | 1 | The Founder's Dilemmas - Wasserman, Noam |
| criterios_seleccion_proveedores | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| criterios_seleccion_proyectos_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| critica_acceptable_quality_level | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| critica_behavior_based_safety | 1 | The Field Guide to Understandin - Dekker, Sidney |
| critica_del_pib_como_metrica_de_progreso | 1 | Cradle to Cradle - Michael Braungart |
| critica_del_plan_con_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| critica_eco_eficiencia | 1 | Cradle to Cradle - Michael Braungart |
| critica_ground_truth_investigacion | 1 | The Field Guide to Understandin - Dekker, Sidney |
| critica_revolucion_industrial | 1 | Cradle to Cradle - Michael Braungart |
| critical_path | 1 | Traction - Gabriel Weinberg |
| criticar_trabajo_evitar_desanimo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| cronograma_proyecto | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| crosby_creatividad_gerencial | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| crosby_habilidad_transmision | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| crosby_implementacion_gerencial | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| crosby_liderazgo_abierto | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| crosby_programa_14_pasos_introduccion | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| crossdocking | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| crowdfunding_de_producto | 1 | Venture Deals - Brad Feld |
| crowdfunding_legal_exemptions_jobs_act | 1 | Venture Deals - Brad Feld |
| csf_funcion_detect | 1 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide |
| csf_funcion_govern | 1 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide |
| csf_funcion_identify | 1 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide |
| csf_funcion_protect | 1 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide |
| csf_funcion_recover | 1 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide |
| csf_perfiles_organizacionales | 1 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide |
| ctq_caracteristicas_criticas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| cual_es_tu_mayor_riesgo | 1 | Hubbard, The Failure of Risk Management |
| cuan_probable_y_cuanto_doleria | 1 | Edwards et al., Managing Project Risks |
| cuando_el_riesgo_se_vuelve_realidad | 1 | Edwards et al., Managing Project Risks |
| cuantificar_impacto_innovacion_6_pasos | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| cuanto_sabes_y_cuanto_solo_crees | 1 | Hubbard, The Failure of Risk Management |
| cuantos_cofundadores_agregar | 1 | The Founder's Dilemmas - Wasserman, Noam |
| cuatro_caminos_ante_un_riesgo | 1 | Edwards et al., Managing Project Risks |
| cuatro_etapas_del_pensamiento_creativo | 1 | The Art of Thought - Wallas, Graham |
| cuatro_etapas_llamada_de_ventas | 1 | SPIN Selling - Neil Rackham |
| cubrir_indicadores_problemas_reunion_individual | 1 | High Output Management - Andrew S. Grove |
| cuestionar_historia_irracional_cabeza | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| cuestionar_supuestos_financieros | 1 | The Green to Gold Business Play - Daniel C. Esty |
| cuestionar_vision_zero | 1 | The Field Guide to Understandin - Dekker, Sidney |
| cuestionario_autoevaluacion_gerencial_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| cuidado_con_la_falsa_precision | 1 | Hubbard, The Failure of Risk Management |
| cuidar_persona_completa_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| cuidarse_agotamiento_centro_rueda | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| cultivar_relacion_talento_largo_plazo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| cultivo_estimulo_emocional_pensamiento_propio | 1 | The Art of Thought - Wallas, Graham |
| cultura_climatica_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| cultura_como_mecanismo_descentralizacion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_de_aprendizaje | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_de_buena_empresa | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| cultura_de_experiencia | 1 | Change by Design, Revised and U - Tim Brown |
| cultura_de_experimentacion_continua | 1 | Change by Design, Revised and U - Tim Brown |
| cultura_de_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| cultura_de_innovacion_y_juego_serio | 1 | Change by Design, Revised and U - Tim Brown |
| cultura_de_optimismo | 1 | Change by Design, Revised and U - Tim Brown |
| cultura_de_reporte | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_de_seguridad_componentes | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_de_seguridad_interpretivista_funcionalista | 1 | The Field Guide to Understandin - Dekker, Sidney |
| cultura_de_transparencia_financiera | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| cultura_feedback_alta_frecuencia | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| cultura_flexible | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_flexible_organizacional | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_generativa_westrum | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_justa | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_justa_2 | 1 | The Field Guide to Understandin - Dekker, Sidney |
| cultura_justa_3 | 1 | The Field Guide to Understandin - Dekker, Sidney |
| cultura_narrativas_variedad_requerida | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| cultura_organizacional_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| cultura_que_habla_del_riesgo_sin_miedo | 1 | Edwards et al., Managing Project Risks |
| cultura_reduce_reuse_recycle | 1 | The Green to Gold Business Play - Daniel C. Esty |
| cultura_transparencia_organizacional | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| cumplimiento_acuerdos_comerciales_tanc | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| cumplimiento_can_spam | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| cumplimiento_ftc_rule_436 | 1 | Franchise Your Business - Mark Siebert |
| cumplimiento_inversionistas_acreditados | 1 | Venture Deals - Brad Feld |
| cumplimiento_magnuson_moss | 1 | Businessperson's Guide to Federal Warranty Law |
| cumplimiento_normativo_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| cumplimiento_sarbanes_oxley | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| cumplimiento_vs_violacion | 1 | The Field Guide to Understandin - Dekker, Sidney |
| cumplir_leyes_estatales_franquicia | 1 | Franchise Your Business - Mark Siebert |
| curse_cinco_culpas | 1 | The Lean Startup - Eric Ries |
| curva_atricion_optima | 1 | Winning at New Products - Robert G. Cooper |
| curva_banera_periodos_fallo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| curva_caracteristica_operativa | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| customer_activation_tactics | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_appreciation_pr | 1 | Traction - Gabriel Weinberg |
| customer_creation | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_development_agile_pairing | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_development_modelo | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_development_process | 1 | Value Proposition Design |
| customer_development_team | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_development_weekly_lessons_learned | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_discovery | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_discovery_get_out_of_building | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_discovery_introduccion | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_discovery_phase2_problem_test | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_gains | 1 | Value Proposition Design |
| customer_insights_design | 1 | Business Model Generation - Osterwalder, Alexander |
| customer_jobs | 1 | Value Proposition Design |
| customer_journey_mapping | 1 | Change by Design, Revised and U - Tim Brown |
| customer_needs_spreadsheet | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| customer_pains | 1 | Value Proposition Design |
| customer_profile | 1 | Value Proposition Design |
| customer_retention_tactics | 2 | The Startup Owner's Manual - Blank, Steve<br>Never Lose a Customer Again - Joey Coleman |
| customer_validation | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_validation_sales_roadmap | 1 | The Startup Owner's Manual - Blank, Steve |
| customer_validation_sell_phase | 1 | The Startup Owner's Manual - Blank, Steve |
| customs_bonded_warehouses | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| cycle_time | 1 | Value Proposition Design |
| dar_critica_inmediata_ayuda_tangible | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| dar_elogio_disciplina_igual_critica | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| dar_estabilidad_situacion_emocional | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dar_forma_politica_climatica | 1 | The Green to Gold Business Play - Daniel C. Esty |
| dar_guia_acto_seis_consejos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| dar_guia_humilde_tres_tecnicas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| dar_guia_util_cuatro_recordatorios | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| dar_mala_noticia_decision_tomada | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dar_opinion_critica_directa_desapasionada | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dar_opinion_especifica_tarea | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dar_opinion_frecuencia_suficiente | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dar_valor_constante_cuatro_publicos | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| data_integrity_forecasting | 1 | Winning at New Products - Robert G. Cooper |
| data_transmission_edi_xml | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| deadlines_como_herramienta_convergencia | 1 | Change by Design, Revised and U - Tim Brown |
| debatir_decidir_asuntos_cultura_evitar_delegar | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| debriefing_participantes | 1 | The Field Guide to Understandin - Dekker, Sidney |
| decide_criterio_eleccion_proveedor | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| decide_phase_roadmap | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| decide_si_lo_compras_o_lo_haces_tu | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| decidir_aceptar_rechazar_material_defectuoso | 1 | High Output Management - Andrew S. Grove |
| decidir_amistad_subordinado_prueba_revision_dificil | 1 | High Output Management - Andrew S. Grove |
| decidir_cobro_velocidad_ventana_entrega | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| decidir_contratacion_final | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| decidir_directivo_no_encaja_papel | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| decidir_empacar_tu_mismo_o_subcontratar | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| decidir_momento_despedir_persona | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| decidir_nivel_competente_inferior | 1 | High Output Management - Andrew S. Grove |
| decidir_poner_nota_comunicar_proposito_limites | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| decidir_quien_comunica_cada_cuanto | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| decidir_vender_solo_online_o_tambien_tienda_fisica | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| decir_no_trabajo_excede_capacidad | 1 | High Output Management - Andrew S. Grove |
| decir_normas_participacion_voz_alta | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| decision_aptitud_uso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| decision_autofinanciamiento_vs_inversion | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decision_comunicacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| decision_conformidad_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| decision_consciente_de_crecimiento | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| decision_cuando_fundar | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decision_de_salir_a_bolsa | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decision_de_vender_startup | 2 | The Founder's Dilemmas - Wasserman, Noam<br>The Hard Thing About Hard Things - Ben Horowitz |
| decision_diy_vs_consultor_franquicia | 1 | Franchise Your Business - Mark Siebert |
| decision_egalitaria_vs_jerarquica | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decision_estrategica_exportar | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| decision_factory_mentality | 1 | Winning at New Products - Robert G. Cooper |
| decision_fpr | 1 | Franchise Your Business - Mark Siebert |
| decision_franquiciar_vs_expansion_propia | 1 | Franchise Your Business - Mark Siebert |
| decision_fundador_solo_vs_equipo | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decision_hire_investment_banker | 1 | Venture Deals - Brad Feld |
| decision_intensidad_capital | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decision_log | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| decision_marca_comun_branding | 1 | Franchise Your Business - Mark Siebert |
| decision_momento_fundacion | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decision_pivotar_o_proceder | 1 | The Startup Owner's Manual - Blank, Steve |
| decision_royalties_vs_venta_producto | 1 | Franchise Your Business - Mark Siebert |
| decision_segunda_unidad_operativa | 1 | Franchise Your Business - Mark Siebert |
| decisiones_de_financiamiento_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| decisiones_por_diseno_no_por_default | 1 | The Founder's Dilemmas - Wasserman, Noam |
| decisiones_reversibles_irreversibles | 1 | The Startup Owner's Manual - Blank, Steve |
| declarar_intencion_reemplazar_peticion_permiso | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| deep_dive_workshop | 1 | Change by Design, Revised and U - Tim Brown |
| defensas_en_profundidad_3 | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| defensas_peligrosas_paradojas | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| define_punto_maximo_de_stock | 1 | Max Muller, Essentials of Inventory Management |
| definicion_alineacion_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| definicion_calidad_conformidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| definicion_calidad_fitness_for_purpose | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| definicion_calidad_segun_agente | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| definicion_estable_producto | 1 | Winning at New Products - Robert G. Cooper |
| definicion_gatekeepers | 1 | Winning at New Products - Robert G. Cooper |
| definicion_metas_engagement | 1 | The Green to Gold Business Play - Daniel C. Esty |
| definicion_objetivos_proyecto_sistema | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| definicion_problema_moms_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| definicion_producto_proyecto | 1 | Winning at New Products - Robert G. Cooper |
| definicion_sistema_calidad_proveedor | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| definicion_sprint_terminado_fisico | 1 | Winning at New Products - Robert G. Cooper |
| definicion_tipos_nuevo_producto | 1 | Winning at New Products - Robert G. Cooper |
| definicion_y_concepto_de_aseguramiento_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| definiciones_operacionales | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| definiciones_operacionales_2 | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| definiciones_operacionales_3 | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| definiciones_operacionales_de_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| definiciones_operacionales_defectos | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| definir_entorno_grupo_clientes_proveedores_competidores | 1 | High Output Management - Andrew S. Grove |
| definir_limites_huella_carbono | 1 | The Green to Gold Business Play - Daniel C. Esty |
| definir_meta_a_5_anos_antes_de_franquiciar | 1 | Franchise Your Business - Mark Siebert |
| definir_metas_smart_de_proyecto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| definir_mision_organizacional | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| definir_que_cuenta_como_dano_antes_de_probar_empaque | 1 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria |
| definir_quien_responde_cada_cosa | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| definir_receta_propia_mantenerse_centrado | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| definir_resultados_tarjeta_puntuacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| definir_tesoro_con_perspectiva_temporal | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| definir_tu_propio_pedido_perfecto | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| definir_vision_larga_trabajar_atras | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| deja_de_ignorar_el_riesgo | 1 | DeMarco y Lister, Waltzing with Bears |
| deja_que_el_proveedor_diga_el_precio_primero | 1 | Chris Voss, Rompe la barrera del no |
| del_caos_al_metodo_madurez_de_riesgo | 1 | Edwards et al., Managing Project Risks |
| delegar_tarea_base_comun_seguimiento | 1 | High Output Management - Andrew S. Grove |
| delimitar_franqueza_radical_cinco_noes | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| demand_curve_pricing | 1 | The Startup Owner's Manual - Blank, Steve |
| demo_prototipo_inversion | 1 | Venture Deals - Brad Feld |
| democratizacion_de_herramientas_creativas | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| demostrar_apertura_visiones_distintas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| dependency_analysis | 1 | The Startup Owner's Manual - Blank, Steve |
| depreciacion_y_amortizacion | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| depura_proveedores_sin_respuesta | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| derecho_rechazo_trabajo_peligroso | 1 | SMALL_BUSINESS |
| derechos_de_registro | 1 | Venture Deals - Brad Feld |
| deriva_deliberada | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| deriva_hacia_el_fallo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| desafios_implementacion_ia | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| desajuste_autoridad_responsabilidad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| desajuste_tarea_persona | 1 | The Field Guide to Understandin - Dekker, Sidney |
| desarrollar_caracteristicas_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollar_caracteristicas_proceso_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollar_caracteristicas_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollar_controles_transferir_operaciones | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollar_estrategia_busqueda_candidatos | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| desarrollar_estrategias_largo_plazo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollar_manual_operaciones | 1 | Franchise Your Business - Mark Siebert |
| desarrollar_metas_anuales | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollar_posicionamiento_empresa | 1 | The Startup Owner's Manual - Blank, Steve |
| desarrollar_primer_curso_entrenamiento | 1 | High Output Management - Andrew S. Grove |
| desarrollo_attack_plans | 1 | Winning at New Products - Robert G. Cooper |
| desarrollo_capacidades_expertos_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollo_caracteristicas_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollo_de_clientes_customer_development | 1 | The Startup Owner's Manual - Blank, Steve |
| desarrollo_de_controles_de_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollo_en_espiral | 1 | Winning at New Products - Robert G. Cooper |
| desarrollo_expertos_capaces | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desarrollo_plan_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| desarrollo_posicionamiento_producto | 1 | The Startup Owner's Manual - Blank, Steve |
| desarrollo_presentacion_problema | 1 | The Startup Owner's Manual - Blank, Steve |
| desarrollo_value_proposition_usp | 1 | Franchise Your Business - Mark Siebert |
| descomponer_tiempo_ciclo_pedido | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| desconexion_ventas_experiencia | 1 | Never Lose a Customer Again - Joey Coleman |
| describir_candidato_ideal_precision | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| descubrir_motivacion_sentido_persona | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| descubrir_necesidades_del_cliente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| descubrir_valor_inesperado_cliente | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| descuento_aceptaciones_bancarias | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| design_for_assembly | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| design_for_environment | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| design_for_manufacture | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| design_for_six_sigma_dfss | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| design_principles | 1 | The field guide to human-centered design |
| design_scorecard | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| design_test_repeat | 1 | Value Proposition Design |
| design_thinking_fundamentos | 1 | Change by Design, Revised and U - Tim Brown |
| design_thinking_proceso | 1 | Winning at New Products - Robert G. Cooper |
| desirability_feasibility_viability | 1 | Change by Design, Revised and U - Tim Brown |
| desmaterializacion_producto_servicio | 1 | The Green to Gold Business Play - Daniel C. Esty |
| desmitificacion_barreras_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| despedir_persona_franqueza_radical | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| despedir_persona_respeto_franqueza | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| desperdicio_cronico_vs_esporadico | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desperdicio_es_alimento | 1 | Cradle to Cradle - Michael Braungart |
| desplegar_estrategia_tarjeta_puntuacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| desplegar_marco_franqueza_radical | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| desplegar_metas_organizacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| desplegar_plan_orden_operaciones_franqueza_radical | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| desplegar_tres_conversaciones_carrera | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| despliegue_continuo | 1 | The Lean Startup - Eric Ries |
| despliegue_metas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| destraba_una_negociacion_que_se_quedo_estancada | 1 | Chris Voss, Rompe la barrera del no |
| deteccion_de_lideres_y_rezagados | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| deteccion_de_mentiras_organizacionales | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| deteccion_defectos_raros_control_estadistico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| deteccion_efecto_hawthorne | 1 | SPIN Selling - Neil Rackham |
| deteccion_franquicia_inadvertida | 1 | Franchise Your Business - Mark Siebert |
| deteccion_ineficiencias_ti | 1 | The Green to Gold Business Play - Daniel C. Esty |
| deteccion_temprana_regulatoria | 1 | The Green to Gold Business Play - Daniel C. Esty |
| detectar_arreglar_fallo_etapa_menor_valor | 1 | High Output Management - Andrew S. Grove |
| detectar_empaque_poco_rigido | 1 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria |
| detectar_metodos_vudu_contratacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| detectar_palanca_negativa_actividad_mando | 1 | High Output Management - Andrew S. Grove |
| detectar_prioridad_cliente_entrega | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| determinacion_cuota_inicial | 1 | Franchise Your Business - Mark Siebert |
| determinacion_regalias | 1 | Franchise Your Business - Mark Siebert |
| determinacion_tamano_cubetas | 1 | Winning at New Products - Robert G. Cooper |
| determinacion_tamano_muestra | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| determinacion_territorio | 1 | Franchise Your Business - Mark Siebert |
| determinar_alcance_cui | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| determinar_estado_presente_capacidades_proyectos_merma | 1 | High Output Management - Andrew S. Grove |
| determinar_monto_a_levantar | 1 | Venture Deals - Brad Feld |
| determinar_tipo_de_mercado | 1 | The Startup Owner's Manual - Blank, Steve |
| determine_what_to_prototype | 1 | The field guide to human-centered design |
| deuda_de_gestion | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| dia_cero_defectos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| dia_cero_defectos_2 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| dia_en_la_vida_del_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| diagnosticar_capacidad_motivacion_prueba_vida | 1 | High Output Management - Andrew S. Grove |
| diagnosticar_falta_motivacion_habilidad | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| diagnostico_antes_remedio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diagnostico_de_productos_crudos | 1 | Cradle to Cradle - Michael Braungart |
| diagnostico_efecto_latigo | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| diagnostico_motivacion_para_contrataciones_inversores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| diagnostico_sintoma_vs_causa_ventas | 1 | SPIN Selling - Neil Rackham |
| diagrama_afinidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diagrama_arbol_despliegue | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diagrama_barreras_ayudas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diagrama_causa_efecto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diagrama_de_flujo_proceso_map | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diagrama_eames_interseccion_posibilidad | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diagrama_flujo_cui | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| diagrama_riesgo_recompensa | 1 | Winning at New Products - Robert G. Cooper |
| dialogo_con_stakeholders | 1 | The Green to Gold Business Play - Daniel C. Esty |
| dialogo_proveedores | 1 | The Green to Gold Business Play - Daniel C. Esty |
| dialogo_stakeholders | 1 | The Green to Gold Business Play - Daniel C. Esty |
| diamante_de_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| diamante_decision_tres_partes | 1 | Winning at New Products - Robert G. Cooper |
| dictar_ritmo_crecimiento_preguntas_escritas | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| diez_derechos_servicio_cliente | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| diez_principios_prototipado | 1 | Value Proposition Design |
| diez_principios_testing | 1 | Value Proposition Design |
| diferencia_ganancia_flujo_caja | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| diferencia_iso9001_iso9004 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diferencia_planeacion_mejora | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diferenciacion_de_marca_contraintuitiva | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| diferenciacion_garantia_contrato_servicio | 1 | Businessperson's Guide to Federal Warranty Law |
| dilema_riqueza_vs_control | 1 | The Founder's Dilemmas - Wasserman, Noam |
| dilucion_propiedad_por_ronda | 1 | The Founder's Dilemmas - Wasserman, Noam |
| dimensionar_inventario_materia_prima_reposicion | 1 | High Output Management - Andrew S. Grove |
| dimensionar_numero_subordinados_medio_dia_semanal | 1 | High Output Management - Andrew S. Grove |
| dimensionar_plantilla_administrativa_pronostico | 1 | High Output Management - Andrew S. Grove |
| dirigir_reunion_decision | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dirigir_reunion_generar_ideas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dirigir_reunion_individual_semanal | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dirigir_reunion_informativa | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dirigir_reunion_reforzar_relaciones | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| dirigir_reunion_revision_trabajo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| disciplina_atencion_dirigida | 1 | The Art of Thought - Wallas, Graham |
| disciplina_rigurosa_proceso_ventas | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| discovery_day_estrategico | 1 | Franchise Your Business - Mark Siebert |
| disenar_empaque_logistica | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| disenar_entorno_rendir_mejor | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| disenar_equipo_plan_anual | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| disenar_incorporacion_cien_dias | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| disenar_los_detalles_no_lo_inevitable | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| disenar_para_sanacion | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| disenar_prompts_efectivos_para_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| disenar_tests_pass_fail | 1 | The Startup Owner's Manual - Blank, Steve |
| disenar_verbos_no_sustantivos | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| disenio_en_turbulencia | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_activismo_social | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_basado_en_comportamientos_existentes | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_biomimetico_de_edificios | 1 | Cradle to Cradle - Michael Braungart |
| diseno_como_plataforma_expansiva | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_conceptual_sistema | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| diseno_consecuencias_no_intencionadas | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_controles_proceso_mejorado | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_dashboards | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| diseno_de_calidad_desde_planificacion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| diseno_de_comportamiento_sostenible | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_de_desafios_de_innovacion | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_de_eucatastrofe_organizacional | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| diseno_de_flujos_pace_layers | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_de_ia_antropomorfica_para_producto | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| diseno_de_mejoras_para_clientes | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_de_metodos_de_recoleccion_de_datos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_de_procesos_por_caracteristicas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_de_sistemas_institucionales | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_departamento_seguridad_efectivo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| diseno_edificio_como_arbol | 1 | Cradle to Cradle - Michael Braungart |
| diseno_embudo_ventas_cliente | 1 | Traction - Gabriel Weinberg |
| diseno_en_la_cuarta_dimension | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_estrategico_vs_tactico | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_estructura_recompensas_roles | 1 | The Founder's Dilemmas - Wasserman, Noam |
| diseno_etico_de_privacidad | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_experimentos_doe_mejora | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_experimentos_hipotesis | 1 | The Startup Owner's Manual - Blank, Steve |
| diseno_experimentos_pass_fail | 1 | The Startup Owner's Manual - Blank, Steve |
| diseno_imperfeccion_intencional | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_implementacion_remedio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_intencional_etica | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_landing_page | 1 | The Startup Owner's Manual - Blank, Steve |
| diseno_mas_alla_del_individuo | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_mensaje_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| diseno_metricas_lideres_rezagados | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| diseno_no_neutral_interfaces | 1 | The Field Guide to Understandin - Dekker, Sidney |
| diseno_organizacional | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| diseno_para_el_ciclo_completo | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_para_el_medio_ambiente | 1 | The Green to Gold Business Play - Daniel C. Esty |
| diseno_para_factores_criticos_y_error_humano | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_para_ia_centrada_en_humano | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_para_reuso_responsable | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_para_sostenibilidad_cradle_to_cradle | 1 | Change by Design, Revised and U - Tim Brown |
| diseno_por_sustraccion | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_producto_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| diseno_programa_capacitacion_franquicia | 1 | Franchise Your Business - Mark Siebert |
| diseno_recordatorios_efectivos_2 | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| diseno_servicio_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| diseno_sistemico_partes_interesadas | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| diseno_universal_talla_unica | 1 | Cradle to Cradle - Michael Braungart |
| disponibilidad_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| disposicion_producto_no_conforme | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| disruptores_endocrinos_y_salud_industrial | 1 | Cradle to Cradle - Michael Braungart |
| distincion_cogs_gastos_operativos | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| distincion_esfuerzo_energia | 1 | The Art of Thought - Wallas, Graham |
| distincion_gasto_vs_capital_expenditure | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| distinguir_empuje_tiron_salidas_laborales | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| distinguir_tres_tipos_sistemas_negocio | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| distorsion_muestreo_mecanico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| distribucion_binomial | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| distribucion_normal_probabilidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| distribucion_poisson | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| distribucion_weibull | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| distribucion_weibull_confiabilidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| distribuciones_probabilidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| divergencia_de_motivaciones_en_exit | 1 | The Founder's Dilemmas - Wasserman, Noam |
| diversidad_activa | 1 | Cradle to Cradle - Michael Braungart |
| diversidad_en_diseno | 1 | Cradle to Cradle - Michael Braungart |
| dividends_terms | 1 | Venture Deals - Brad Feld |
| division_de_labor_vs_roles_superpuestos | 1 | The Founder's Dilemmas - Wasserman, Noam |
| division_trabajo_humano_ia | 2 | Essentials of Supply Chain Management - Michael H. Hugos<br>Co-Intelligence_ Living and Wor - Ethan Mollick |
| dmadv_fase_diseno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| dmadv_fase_verificacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| dmaic_fase_analyze | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| dmaic_fase_define | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| dmaic_fase_improve | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| dmaic_fase_measure | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| dmaic_fase_select | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| doble_significado_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| documenta_el_ahorro_real_de_cada_compra | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| documenta_lo_que_no_incluye_tu_compra | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| documentacion_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| documentacion_mantenimiento_linea_base | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| documentacion_sistemas_operativos | 1 | Franchise Your Business - Mark Siebert |
| documentacion_viaje_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| documentar_trabajo_manual_operaciones | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| documento_alcance_servicio | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| documento_quien_es_quien_equipo | 1 | Never Lose a Customer Again - Joey Coleman |
| domina_lo_que_compras | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| dominar_arte_socializar_trabajo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| dominar_reacciones_emociones_ajenas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| downcycling_problema | 1 | Cradle to Cradle - Michael Braungart |
| draft_plan_accion_climatico | 1 | The Green to Gold Business Play - Daniel C. Esty |
| drag_along_agreement | 1 | Venture Deals - Brad Feld |
| drift_hacia_el_fallo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| driver_de_inventario | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| driver_produccion | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| driver_transporte | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| driver_ubicacion | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| drum_buffer_rope | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| due_diligence_adquisiciones | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| duos_vs_trios_fundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| duration_estimating_worksheet | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| earlyvangelists_ventas_tempranas | 1 | The Startup Owner's Manual - Blank, Steve |
| earned_value_status | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| earned_vs_paid_media | 1 | The Startup Owner's Manual - Blank, Steve |
| eco_advantage | 1 | The Green to Gold Business Play - Daniel C. Esty |
| eco_efectividad | 1 | Cradle to Cradle - Michael Braungart |
| eco_efectividad_2 | 1 | Cradle to Cradle - Michael Braungart |
| eco_eficiencia | 1 | The Green to Gold Business Play - Daniel C. Esty |
| economia_circular_como_modelo_de_negocio | 1 | Change by Design, Revised and U - Tim Brown |
| economia_circular_de_la_imaginacion | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| economia_de_la_experiencia | 1 | Change by Design, Revised and U - Tim Brown |
| economia_subensambles_inspeccion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| ecosistema_global_emprendimiento_gee | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| ecuacion_de_valor | 1 | SPIN Selling - Neil Rackham |
| ecuacion_de_valor_cliente | 1 | SPIN Selling - Neil Rackham |
| ecuacion_de_valor_venta | 1 | SPIN Selling - Neil Rackham |
| educacion_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| educacion_estadistica_para_la_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| efecto_bullwhip | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| efecto_palo_hockey | 1 | Franchise Your Business - Mark Siebert |
| efectos_recompensa_castigo | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| eficiencia_energetica_almacenes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| eficiencia_flota_vehicular | 1 | The Green to Gold Business Play - Daniel C. Esty |
| eficiencia_hidrica_edificios_2 | 1 | The Green to Gold Business Play - Daniel C. Esty |
| ejecucion_auditoria | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| ejecucion_de_touchpoints | 1 | Change by Design, Revised and U - Tim Brown |
| ejecucion_incremental_transicion_tecnologica | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| ejecucion_rapida_de_despidos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| ejecutar_ciclos_cortos_aprender | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| ejecutar_embudo_reclutamiento_escala | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| ejercer_poder_posicion_etapa_decision_clara | 1 | High Output Management - Andrew S. Grove |
| ejercicio_retrospectivo_proyecto | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| el_pre_mortem_imagina_el_fracaso | 1 | Edwards et al., Managing Project Risks |
| el_riesgo_cambia_con_el_tiempo | 1 | Edwards et al., Managing Project Risks |
| el_riesgo_del_entorno_que_no_controlas | 1 | Edwards et al., Managing Project Risks |
| el_riesgo_eres_tu | 1 | Síntesis del método aplicado al emprendedor individual (riesgo de rotación, Waltzing with Bears, Cap. 13, llevado a un proyecto de una sola persona) |
| el_riesgo_nunca_se_acaba_se_administra | 1 | Síntesis de tono de DeMarco y Lister, Waltzing with Bears (nodo ancla del pack) |
| el_valor_tambien_es_incierto | 1 | DeMarco y Lister, Waltzing with Bears |
| elaboracion_pro_forma_invoice | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| eleccion_83b | 1 | Venture Deals - Brad Feld |
| eleccion_abogado_franquicias | 1 | Franchise Your Business - Mark Siebert |
| eleccion_del_lenguaje_para_pensar | 1 | The Art of Thought - Wallas, Graham |
| eleccion_ritmo_crecimiento | 1 | The Founder's Dilemmas - Wasserman, Noam |
| elegir_caja_correcta | 1 | Requisitos de empaque de los couriers |
| elegir_categorias_nota_palabras_propias_empresa | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| elegir_cinco_indicadores_diarios_fabrica | 1 | High Output Management - Andrew S. Grove |
| elegir_estilo_direccion_madurez_relevante_tarea | 1 | High Output Management - Andrew S. Grove |
| elegir_fabricar_pedido_pronostico | 1 | High Output Management - Andrew S. Grove |
| elegir_forma_inspirar_cambio_conducta | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| elegir_indicador_salida_trabajo_administrativo | 1 | High Output Management - Andrew S. Grove |
| elegir_inspeccion_barrera_monitorizacion | 1 | High Output Management - Andrew S. Grove |
| elegir_material_de_relleno_segun_producto | 1 | Guia de empaque para transporte |
| elegir_medio_dar_guia_jerarquia_modos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| elegir_modo_control_motivacion_factor_cua | 1 | High Output Management - Andrew S. Grove |
| elegir_modo_transporte_volumen_distancia | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| elegir_momento_actividad_palanca_maxima | 1 | High Output Management - Andrew S. Grove |
| elegir_palabras_nota_definirlas_empresa_entera | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| elegir_pregunta_recurrente_pedir_critica | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| elegir_recolocar_despedir_persona | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| elegir_resistencia_caja_peso | 1 | DHL Express, Guia de empaque |
| elegir_sobre_o_caja_tamano | 1 | Guia de empaque para envios (FedEx) |
| elementos_contrato_legal | 1 | The Founder's Dilemmas - Wasserman, Noam |
| elementos_creadores_valor | 1 | Business Model Generation - Osterwalder, Alexander |
| elementos_plan_exportacion_ejemplo | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| elevated_surfaces_fall_protection | 1 | SMALL_BUSINESS |
| elevator_pitch_inversion | 1 | Venture Deals - Brad Feld |
| eliminacion_causas_error_4 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| eliminacion_desperdicio_lean_green | 1 | The Green to Gold Business Play - Daniel C. Esty |
| eliminacion_estandares_trabajo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminacion_firmas_redundantes | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminacion_gestion_por_objetivos_y_numeros | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminacion_inspeccion_masiva_por_control_estadistico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminacion_planes_muestreo_estandar | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminar_barreras_departamentales | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminar_cuotas_numericas_trabajadores | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminar_desperdicio_organizacional | 1 | The Lean Startup - Eric Ries |
| eliminar_metas_numericas_gerencia | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminar_miedo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminar_seguimiento_descendente_responsabilizar_dueno | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| eliminar_slogans_y_exhortaciones | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| eliminar_trabajo_a_destajo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| elogiar_publico_criticar_privado_sus_tres_matices | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| elogiar_trabajo_especifico_contexto | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| email_marketing_activacion | 1 | Traction - Gabriel Weinberg |
| email_marketing_para_captacion | 1 | Traction - Gabriel Weinberg |
| email_marketing_retencion | 1 | Traction - Gabriel Weinberg |
| embalaje_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| embrace_the_struggle_liderazgo_autentico | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| embudo_atricion_nuevos_productos | 1 | Winning at New Products - Robert G. Cooper |
| embudo_get_keep_grow | 1 | The Startup Owner's Manual - Blank, Steve |
| embudo_secuencial_de_inversores | 2 | The Founder's Dilemmas - Wasserman, Noam<br>Venture Deals - Brad Feld |
| embudo_ventas_franquicia | 1 | Franchise Your Business - Mark Siebert |
| emocion_como_motor_pensamiento | 1 | The Art of Thought - Wallas, Graham |
| emocion_e_imagen_en_el_pensamiento | 1 | The Art of Thought - Wallas, Graham |
| empacar_flores_plantas_sin_agua | 1 | Guia de empaque para envios (FedEx) |
| empacar_liquidos_doble_barrera | 1 | Requisitos de empaque de los couriers |
| empaque_ecoeficiente | 1 | The Green to Gold Business Play - Daniel C. Esty |
| emparejar_indicadores_efecto_contraefecto | 1 | High Output Management - Andrew S. Grove |
| empathy_map | 1 | Business Model Generation - Osterwalder, Alexander |
| empatia_capas_de_comprension | 1 | Change by Design, Revised and U - Tim Brown |
| empezar_cultura_franqueza_radical | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| empieza_con_lo_que_ya_funciona | 1 | Hubbard, The Failure of Risk Management |
| employee_mobilization_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| employee_pool_esop | 1 | Venture Deals - Brad Feld |
| empoderamiento_de_participantes | 1 | Change by Design, Revised and U - Tim Brown |
| empoderamiento_empleados | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| empoderamiento_personal_frontline | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| emprendedor_como_puesto_de_trabajo | 1 | The Lean Startup - Eric Ries |
| emprendimiento_como_disciplina_de_gestion | 1 | The Lean Startup - Eric Ries |
| emprendimiento_serial | 1 | The Founder's Dilemmas - Wasserman, Noam |
| empujar_persona_reunion_direccion_preferida | 1 | High Output Management - Andrew S. Grove |
| encaje_organizacional | 1 | Franchise Your Business - Mark Siebert |
| encargar_meta_especifica_dejar_libre_metodo | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| encontrar_el_golpe_mental | 1 | The Art of Thought - Wallas, Graham |
| encontrar_lead_vc | 1 | Venture Deals - Brad Feld |
| encontrar_vc_adecuado | 1 | Venture Deals - Brad Feld |
| encuadre_desafio_diseno | 2 | The field guide to human-centered design<br>Change by Design, Revised and U - Tim Brown |
| encuestar_al_cliente_para_saber_que_valora | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| energia_eolica_distribuida | 1 | Cradle to Cradle - Michael Braungart |
| energia_fuentes_limpias | 1 | The Green to Gold Business Play - Daniel C. Esty |
| enfasis_en_utilidades_corto_plazo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| enfermedades_mortales_gestion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| enfoque_centrado_humano_organizacional | 1 | Change by Design, Revised and U - Tim Brown |
| enfoque_en_procesos_no_en_problemas | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| enfoque_en_superfans | 1 | Never Lose a Customer Again - Joey Coleman |
| enfoque_etapa_investigacion | 1 | SPIN Selling - Neil Rackham |
| enfoque_find_and_fix | 1 | OSHA3886 |
| enfoque_integrado_marketing_franquicia | 1 | Franchise Your Business - Mark Siebert |
| enfoque_motor_unico_crecimiento | 1 | The Lean Startup - Eric Ries |
| enfoque_paso_a_paso_investigacion_mercado | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| enfoque_portafolio_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| enfoque_proyecto_por_proyecto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| enfoque_situacional_vs_personal | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| enfoques_definicion_riesgo_aceptable | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| enfoques_generales_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| enfoques_gurus_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| engineering_as_marketing | 1 | Traction - Gabriel Weinberg |
| ensenanza_deficiente_metodos_estadisticos | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| entender_term_sheet | 1 | Venture Deals - Brad Feld |
| entrada_mercado_nuevo | 1 | The Startup Owner's Manual - Blank, Steve |
| entrega_por_partes_para_exponer_el_riesgo | 1 | DeMarco y Lister, Waltzing with Bears |
| entregar_evaluacion_desempeno_tres_claves | 1 | High Output Management - Andrew S. Grove |
| entregar_evaluacion_formal_desempenio_nueve_consejos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| entregar_experiencia_entrevista_excelente | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| entregar_problema_dificil_reporte | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| entrenamiento_continuo | 1 | Franchise Your Business - Mark Siebert |
| entrenamiento_de_gerentes_para_despidos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| entrenamiento_en_sitio | 1 | Franchise Your Business - Mark Siebert |
| entrenamiento_funcional_empleados | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| entrenamiento_gerencial | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| entrenamiento_oficina_central | 1 | Franchise Your Business - Mark Siebert |
| entrenamiento_para_breakthrough | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| entrenamiento_supervisores | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| entrenamiento_supervisores_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| entrenamiento_y_control_estadistico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| entrenar_franquiciados_validacion | 1 | Franchise Your Business - Mark Siebert |
| epc_condiciones_productoras_error | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| epicentros_innovacion_modelo_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| equilibrar_capacidad_personal_inventario_plazo | 1 | High Output Management - Andrew S. Grove |
| equilibrar_corto_largo_plazo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| equilibrar_elogio_critica_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| equilibrar_microdireccion_ausencia | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| equilibrio_confianza_verificacion | 1 | Franchise Your Business - Mark Siebert |
| equipo_conjunto_de_mejora_con_proveedores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| equipo_customer_development | 1 | The Startup Owner's Manual - Blank, Steve |
| equipo_de_gestion_de_crisis | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| equipo_dedicado_continuo | 1 | Winning at New Products - Robert G. Cooper |
| equipo_diverso_ideacion | 1 | Business Model Generation - Osterwalder, Alexander |
| equipo_forma_t | 1 | Change by Design, Revised and U - Tim Brown |
| equipo_interdepartamental_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| equipo_mejora_calidad_2 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| equipo_multifuncional_real | 1 | Winning at New Products - Robert G. Cooper |
| equipos_alto_desempeno | 1 | The Field Guide to Understandin - Dekker, Sidney |
| equipos_autodirigidos_servicio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| equipos_blitz | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| equipos_conjuntos_diseno_proveedor | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| equipos_dedicados_de_proyecto | 1 | Winning at New Products - Robert G. Cooper |
| equipos_multifuncionales_dfe | 1 | The Green to Gold Business Play - Daniel C. Esty |
| equipos_pequenos_vs_grandes | 1 | Change by Design, Revised and U - Tim Brown |
| equipos_ruptura_vet | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| equipos_visita_cliente | 1 | Winning at New Products - Robert G. Cooper |
| equity_crowdfunding | 1 | Venture Deals - Brad Feld |
| equity_crowdfunding_terminos | 1 | Venture Deals - Brad Feld |
| ergonomia_laboral | 1 | SMALL_BUSINESS |
| erosion_de_defensas_por_ausencia_de_accidentes | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| erp_systems | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| error_humano_vs_falla_mecanica | 1 | The Field Guide to Understandin - Dekker, Sidney |
| error_proofing_servicio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| error_proofing_six_sigma_lean | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| errores_como_consecuencia | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| errores_comunes_fundraising | 1 | Venture Deals - Brad Feld |
| escala_actitud_cierre | 1 | SPIN Selling - Neil Rackham |
| escaleras_fijas_seguridad | 1 | SMALL_BUSINESS |
| escaleras_portatiles_seguridad | 1 | SMALL_BUSINESS |
| escalonar_complejidad_puesto_empleado_nuevo | 1 | High Output Management - Andrew S. Grove |
| escalonar_fuentes_informacion_gerencial | 1 | High Output Management - Andrew S. Grove |
| escape_trampa_proveedor_pasivo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| escenarios_de_evolucion_de_la_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| escenarios_diseno_modelo_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| escepticismo_sano_ante_el_riesgo | 1 | Hubbard, The Failure of Risk Management |
| escribir_apuntes_sala_estudio_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| escribir_escaleras_puesto_evitar_dos_extremos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| escrow_en_adquisiciones | 1 | Venture Deals - Brad Feld |
| escucha_activa_requisitos | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| escuchar_callado_equipo_tranquilizar_incomodo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| escuchar_entender_critica_dominar_defensa | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| escuchar_ruidoso_opinion_fuerte_pedir_agujeros | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| esfuerzo_voluntario_vs_urge_espontaneo | 1 | The Art of Thought - Wallas, Graham |
| esfuerzo_y_energia_intelectual | 1 | The Art of Thought - Wallas, Graham |
| espacio_de_seguridad | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| espacios_de_diseno_superpuestos | 1 | Change by Design, Revised and U - Tim Brown |
| espacios_fisicos_de_innovacion | 1 | Change by Design, Revised and U - Tim Brown |
| especificacion_requisitos_proveedores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| especificacion_vehiculos_eficientes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| espiral_mortal_lotes_grandes | 1 | The Lean Startup - Eric Ries |
| espiral_muerte_lotes_grandes | 1 | The Lean Startup - Eric Ries |
| esposas_doradas_carrera | 1 | The Founder's Dilemmas - Wasserman, Noam |
| esposas_familiares_founder | 1 | The Founder's Dilemmas - Wasserman, Noam |
| establecer_capacidad_del_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_credibilidad_pericia_humildad | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| establecer_dinamica_nueva_antiguos_pares | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| establecer_diseno_final_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_equipo_multifuncional | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_estandar_alto_desempeno | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| establecer_estandares_desempeno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_limites_cuidado_personal | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| establecer_linea_base_mvp | 1 | The Lean Startup - Eric Ries |
| establecer_metas_caracteristicas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_metas_de_calidad_basadas_en_mercado | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_metas_reduccion_emisiones | 1 | The Green to Gold Business Play - Daniel C. Esty |
| establecer_politicas_de_nuevo_producto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_proyecto_mejora | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_proyecto_y_metas_diseno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_vision_organizacional | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecer_vision_organizacional_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecimiento_capacidad_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecimiento_de_niveles_de_calidad_aql_dpm | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecimiento_metas_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| establecimiento_metas_publicas | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estacionalidad_marketing_franquicia | 1 | Franchise Your Business - Mark Siebert |
| estadistica_basica_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estadisticas_comerciales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| estado_flujo_de_caja_tres_categorias | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| estandar_gtin_epc | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| estandares_voluntarios | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| estandarizacion_codigos_producto_epc | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| estandarizacion_industrial_voluntaria | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| estandarizar_metodologia_lca | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estar_listo_para_ser_publica | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| estatus_fundador_simbolico | 1 | The Founder's Dilemmas - Wasserman, Noam |
| estilo_gerencial_ballet_vs_hockey | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| estilo_gerencial_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| estilos_de_negociacion | 1 | Venture Deals - Brad Feld |
| estilos_pensamiento_intuitivo_vs_logico | 1 | The Art of Thought - Wallas, Graham |
| estimacion_costos_actividad | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| estimacion_intervalos_confianza | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estimacion_inversion_inicial_franquiciador | 1 | Franchise Your Business - Mark Siebert |
| estimate_at_completion_eac | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| estrategia_captura_mercado_crecimiento | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| estrategia_circular_y_mecanismo_de_retorno | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| estrategia_competencia_vcs | 1 | Venture Deals - Brad Feld |
| estrategia_comunicacion_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estrategia_crecimiento_clientes | 1 | The Startup Owner's Manual - Blank, Steve |
| estrategia_de_innovacion_arenas | 1 | Winning at New Products - Robert G. Cooper |
| estrategia_de_innovacion_producto | 1 | Winning at New Products - Robert G. Cooper |
| estrategia_de_innovacion_y_tecnologia | 1 | Winning at New Products - Robert G. Cooper |
| estrategia_de_tragedia_vs_estrategia_de_cambio | 1 | Cradle to Cradle - Michael Braungart |
| estrategia_de_ventas | 1 | The Startup Owner's Manual - Blank, Steve |
| estrategia_eco_advantage | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estrategia_edificios_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estrategia_expansion_centros_distribucion | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| estrategia_ferias_comerciales | 1 | Traction - Gabriel Weinberg |
| estrategia_gestion_riesgo_tolerancia | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| estrategia_hibrida_control_riqueza | 1 | The Founder's Dilemmas - Wasserman, Noam |
| estrategia_innovacion_producto | 1 | Winning at New Products - Robert G. Cooper |
| estrategia_marca_segun_tamano | 1 | Franchise Your Business - Mark Siebert |
| estrategia_mercados_geograficos | 1 | Franchise Your Business - Mark Siebert |
| estrategia_multicanal_bienvenida | 1 | Never Lose a Customer Again - Joey Coleman |
| estrategia_plataformas_existentes | 1 | Traction - Gabriel Weinberg |
| estrategia_proactiva_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estrategia_producto_global_glocal | 1 | Winning at New Products - Robert G. Cooper |
| estrategia_recoleccion_datos_carbono | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estrategia_redes_sociales_franquicias | 1 | Franchise Your Business - Mark Siebert |
| estrategia_ti_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| estrategia_ventas_diy | 1 | Franchise Your Business - Mark Siebert |
| estrategia_ventas_enterprise | 1 | Traction - Gabriel Weinberg |
| estrategias_de_alfabetizacion_financiera | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| estrategias_de_crecimiento_empresarial | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| estrategias_estimacion_costos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estrategias_seleccion_preferencial | 1 | Cradle to Cradle - Michael Braungart |
| estratificacion_datos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estructura_competencias_six_sigma_lean | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estructura_de_costos | 1 | Business Model Generation - Osterwalder, Alexander |
| estructura_de_la_venta | 1 | The Founder's Dilemmas - Wasserman, Noam |
| estructura_equipos_innovacion_interna | 1 | The Lean Startup - Eric Ries |
| estructura_estado_resultados | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| estructura_fondo_vc | 1 | Venture Deals - Brad Feld |
| estructura_global_oficina_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estructura_organizacional_funcional_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estructura_plan_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| estructura_precio_adquisicion | 1 | Venture Deals - Brad Feld |
| estructura_proveedores_aprobados_designados | 1 | Franchise Your Business - Mark Siebert |
| estructura_reporte_dual_estadistico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| estructura_sp800171 | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| estructuracion_programa_auditoria | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estudio_desempeno_run_charts_servicios | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| estudio_lealtad_cliente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estudio_mercado_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| estudio_mezclas_multiples_fuentes | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| etapa_build_business_case | 1 | Winning at New Products - Robert G. Cooper |
| etapa_development | 1 | Winning at New Products - Robert G. Cooper |
| etapa_discovery_ideacion | 1 | Winning at New Products - Robert G. Cooper |
| etapa_pruebas_necesaria | 1 | Winning at New Products - Robert G. Cooper |
| etapa_scoping | 1 | Winning at New Products - Robert G. Cooper |
| etapa_testing_validation | 1 | Winning at New Products - Robert G. Cooper |
| etapas_de_control_operativo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| etiqueta_duplicada_dentro_del_paquete | 1 | Guia visual de empaque |
| etiqueta_lo_que_piensa_el_proveedor | 1 | Chris Voss, Rompe la barrera del no |
| etiquetado_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| evalua_la_gravedad_sin_autoengano | 1 | Edwards et al., Managing Project Risks |
| evaluacion_actitudes_empleados | 1 | The Green to Gold Business Play - Daniel C. Esty |
| evaluacion_alternativas_solucion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_amazon_case | 1 | Business Model Generation - Osterwalder, Alexander |
| evaluacion_balanceada_de_ejecutivos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| evaluacion_capacidades_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_capital_humano | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_capital_para_cofundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_competencia_franquiciados | 1 | Franchise Your Business - Mark Siebert |
| evaluacion_competencias_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_competencias_centrales | 1 | Winning at New Products - Robert G. Cooper |
| evaluacion_conocimiento_industria | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_cultura_seguridad_completa | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| evaluacion_de_atractivo_de_mercado | 1 | Winning at New Products - Robert G. Cooper |
| evaluacion_de_desempeno_merito | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| evaluacion_de_factores_de_riesgo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_desempeno_junta_directiva | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_desempeno_proyectos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_disimilitud_sucesor | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_dispassionate_idea | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_encuesta_calidad_proveedor | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_etica_trabajo | 1 | Franchise Your Business - Mark Siebert |
| evaluacion_fit_cultural | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_gestion_riesgos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_industria_cliente | 1 | Winning at New Products - Robert G. Cooper |
| evaluacion_megatendencias | 1 | Winning at New Products - Robert G. Cooper |
| evaluacion_mejora_programa | 2 | OSHA3885<br>OSHA3886 |
| evaluacion_mercados_objetivo | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| evaluacion_necesidad_franquiciar | 1 | Franchise Your Business - Mark Siebert |
| evaluacion_potencial_exportador_producto | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| evaluacion_preparacion_empresa_exportar | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| evaluacion_preparacion_tecnologica | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| evaluacion_riesgo_calidad_organizacional | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evaluacion_riesgo_mercado_dinero_gestion | 1 | Franchise Your Business - Mark Siebert |
| evaluacion_riesgos_legales_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| evaluacion_salud_financiera_empresa | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| evaluacion_tecnologias_disruptivas | 1 | Winning at New Products - Robert G. Cooper |
| evaluacion_temperamento_franquiciador | 1 | Franchise Your Business - Mark Siebert |
| evaluacion_tipos_inversores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_ventana_mercado | 1 | The Founder's Dilemmas - Wasserman, Noam |
| evaluacion_vp_ventas | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| evaluar_controles | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| evaluar_cultura_empresa_adjetivos | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| evaluar_desempenio_dos_veces_anio | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| evaluar_directivo_resultados_fortaleza | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| evaluar_huella_hidrica | 1 | The Green to Gold Business Play - Daniel C. Esty |
| evaluar_ia_predictiva_vs_generativa_para_negocio | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| evaluar_impacto_ecosistemas_biodiversidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| evaluar_proceso_completo_no_cada_metrica | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| eventos_kaizen_rie | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| eventos_offline_como_canal_traccion | 1 | Traction - Gabriel Weinberg |
| eventos_reuniones_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| evitacion_del_riesgo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| evitar_cherry_picking | 1 | The Field Guide to Understandin - Dekker, Sidney |
| evitar_copia_estructura_competencia | 1 | Franchise Your Business - Mark Siebert |
| evitar_doble_impuesto_malestar | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| evitar_greenwashing | 1 | The Green to Gold Business Play - Daniel C. Esty |
| evitar_lenguaje_juzgador | 1 | The Field Guide to Understandin - Dekker, Sidney |
| evitar_materiales_blandos_contenedor_final | 1 | Guia de empaque para envios (FedEx) |
| evitar_micro_matching | 1 | The Field Guide to Understandin - Dekker, Sidney |
| evitar_o_asumir_decide_a_conciencia | 1 | Edwards et al., Managing Project Risks |
| evitar_obsesion_ascenso_estatus | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| evitar_paralisis_por_analisis | 1 | The Lean Startup - Eric Ries |
| evitar_perdida_situacion_awareness | 1 | The Field Guide to Understandin - Dekker, Sidney |
| evitar_personalizar_guia_aceptar_personal | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| evitar_preguntas_ilegales_entrevista | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| evitar_presion_social_actos_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| evitar_pseudociencia_producto | 1 | The Lean Startup - Eric Ries |
| evitar_terminos_enganosos_garantia | 1 | Businessperson's Guide to Federal Warranty Law |
| evitar_uso_complacencia | 1 | The Field Guide to Understandin - Dekker, Sidney |
| examinar_demanda_entorno_dos_marcos_temporales | 1 | High Output Management - Andrew S. Grove |
| examinar_entorno_expectativas_tecnologia_proveedores_grupos | 1 | High Output Management - Andrew S. Grove |
| examinar_trabajo_pasado_candidato | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| exclusividad_territorial_representante | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| executive_summary_inversion | 1 | Venture Deals - Brad Feld |
| exenciones_legales_franquicia | 1 | Franchise Your Business - Mark Siebert |
| exercise_period_opciones | 1 | Venture Deals - Brad Feld |
| exigir_critica_jefe_reticente | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| exito_franquiciado_determina_exito_franquiciador | 1 | Franchise Your Business - Mark Siebert |
| expand_phase_roadmap | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| expandir_cadena_valor | 1 | The Green to Gold Business Play - Daniel C. Esty |
| expected_commercial_value_ecv | 1 | Winning at New Products - Robert G. Cooper |
| experiencia_del_cliente_proactiva | 1 | Never Lose a Customer Again - Joey Coleman |
| experiencias_exclusivas_vip | 1 | Never Lose a Customer Again - Joey Coleman |
| experiment_library | 1 | Value Proposition Design |
| experimentacion_iterativa_mercado_fisico | 1 | The Lean Startup - Eric Ries |
| experimento_cuentas_rojas | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| experticia_operativa_vs_vision_sistemica | 1 | The Field Guide to Understandin - Dekker, Sidney |
| explicar_idea_facil_comprender_oyente | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| explotacion_tecnologias_disruptivas | 1 | Winning at New Products - Robert G. Cooper |
| export_administration_regulations | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| exportacion_de_servicios | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| extension_credito_compradores_extranjeros | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| extintores_portatiles_de_incendio | 1 | SMALL_BUSINESS |
| extraer_priorizar_hipotesis | 1 | Value Proposition Design |
| facilidad_supervision_franquicia | 1 | Franchise Your Business - Mark Siebert |
| facilitar_despido_tres_cosas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| facilitar_expresion_subordinado_pregunta_mas | 1 | High Output Management - Andrew S. Grove |
| facilitar_gente_diga_verdad | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| factores_explicativos_vs_factores_de_cambio | 1 | The Field Guide to Understandin - Dekker, Sidney |
| factores_valoracion_startup | 1 | Venture Deals - Brad Feld |
| fairness_opinion | 1 | Venture Deals - Brad Feld |
| falacia_cero_defectos | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| falacia_culpa_trabajadores | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| falacia_del_disenador_affordances | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| falacia_meta_numerica_sin_metodo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| falacia_problemas_diferentes | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| falacia_recompensa_loteria | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| falacia_redundancia_social | 1 | The Field Guide to Understandin - Dekker, Sidney |
| falla_sistemica_vs_error_individual | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| fallar_rapido_prototipado | 1 | Change by Design, Revised and U - Tim Brown |
| fallas_activas_condiciones_latentes | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| fallo_regulatorio_por_recursos_insuficientes | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| falsos_comienzos_mejora_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| falta_de_constancia_de_proposito | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| familia_normas_iso_9000 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| fase_acclimate | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_acclimate_experiencia_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_accomplish_experiencia_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_activate_primera_impresion | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_admit_celebracion | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_adopt | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_adopt_ciclo_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_affirm_buyers_remorse | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_assess | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_assess_ciclo_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| fase_de_eliminacion_de_no_comercializables | 1 | Cradle to Cradle - Michael Braungart |
| fase_diseno_prototipado_modelos | 1 | Business Model Generation - Osterwalder, Alexander |
| fase_entendimiento_investigacion_mercado | 1 | Business Model Generation - Osterwalder, Alexander |
| fase_gestion_continua_modelo | 1 | Business Model Generation - Osterwalder, Alexander |
| fase_implementacion_modelo | 1 | Business Model Generation - Osterwalder, Alexander |
| fase_mobilizar_modelo_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| fases_traccion_producto | 1 | Traction - Gabriel Weinberg |
| fatigue_performance_effects | 1 | The Field Guide to Understandin - Dekker, Sidney |
| feedback_efectivo_liderazgo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| feedback_supervisores_trabajadores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| feedforward_diseno | 1 | Cradle to Cradle - Michael Braungart |
| fees_publicidad_sistema | 1 | Franchise Your Business - Mark Siebert |
| fees_y_breakup_fee_adquisicion | 1 | Venture Deals - Brad Feld |
| fenomeno_del_click | 1 | The Art of Thought - Wallas, Graham |
| fenomenos_senuelo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| ferias_comerciales_franquicia | 1 | Franchise Your Business - Mark Siebert |
| ficcion_especulativa_como_metodo | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| fijacion_cognitiva | 1 | The Field Guide to Understandin - Dekker, Sidney |
| fijacion_de_metas | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| fijacion_precio_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| fijar_causa_ultimo_accidente_riesgo_siguiente | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| fijar_cuatro_notas_calcular_nota_global | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| fijar_duracion_lugar_reunion_individual | 1 | High Output Management - Andrew S. Grove |
| fijar_expectativas_claras_comienzo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| fijar_fecha_cierre_debate_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| fijar_frecuencia_reunion_individual_madurez_tarea | 1 | High Output Management - Andrew S. Grove |
| fijar_horizonte_ventana_replanificacion | 1 | High Output Management - Andrew S. Grove |
| fijar_meta_direccion_objetivos_mitad_probabilidad | 1 | High Output Management - Andrew S. Grove |
| fijar_periodo_direccion_objetivos_retroalimentacion | 1 | High Output Management - Andrew S. Grove |
| fijar_proceso_trabajo_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| fijar_resultado_excelente_reunion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| fijar_vision_concreta_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| filosofia_validacion_clientes | 1 | The Startup Owner's Manual - Blank, Steve |
| fin_precio_como_criterio_unico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| financial_performance_representations | 1 | Franchise Your Business - Mark Siebert |
| financiamiento_amigos_y_familia | 1 | The Founder's Dilemmas - Wasserman, Noam |
| financiamiento_angel_investors | 1 | The Founder's Dilemmas - Wasserman, Noam |
| financiamiento_bancos_multilaterales_desarrollo | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| financiamiento_sba_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| financiamiento_usda_agricola | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| financiamiento_venture_capital | 1 | The Founder's Dilemmas - Wasserman, Noam |
| fine_tuning_ia_para_caso_de_uso | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| fingir_prototipo_cinco_mil_replicas | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| fiscalidad_comercio_electronico_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| fit_problema_solucion | 1 | Value Proposition Design |
| fit_value_proposition | 1 | Value Proposition Design |
| fitness_for_purpose_vs_conformance | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| fitness_for_use_purpose | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| five_data_traps | 1 | Value Proposition Design |
| five_whys_inversion_proporcional | 1 | The Lean Startup - Eric Ries |
| flujo_de_caja_libre | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| flujo_decision_devoluciones | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| flujos_de_ingresos | 1 | Business Model Generation - Osterwalder, Alexander |
| fmea_analisis_de_modos_de_falla | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| foco_proximal_reacciones_falla | 1 | The Field Guide to Understandin - Dekker, Sidney |
| folleto_franquicia | 1 | Franchise Your Business - Mark Siebert |
| fomentar_guia_reciproca_companieros | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| fomento_educacion_autoeducacion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| footnotes_financieros | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| foreign_corrupt_practices_act | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| foreign_trade_zones | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| forma_de_contraprestacion_en_adquisicion | 1 | Venture Deals - Brad Feld |
| formacion_de_habitos_de_trabajo_creativo | 1 | The Art of Thought - Wallas, Graham |
| formacion_equipo_proyecto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| formacion_seleccion_y_retencion_de_personal | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| formal_acceptance | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| formalizar_alianza_estrategica | 1 | The Green to Gold Business Play - Daniel C. Esty |
| formalizar_junta_asesora | 1 | The Startup Owner's Manual - Blank, Steve |
| formalizar_un_proceso_ad_hoc | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| formar_consejo_asesor_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| formar_equipo_practicas_metodo | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| formula_exponencial_confiabilidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| formulacion_teorias_causa | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| founder_ceo_succession_process | 1 | The Founder's Dilemmas - Wasserman, Noam |
| founders_activities_clause | 1 | Venture Deals - Brad Feld |
| four_actions_framework_lado_cliente | 1 | Business Model Generation - Osterwalder, Alexander |
| fracaso_como_aprendizaje_startup | 1 | The Startup Owner's Manual - Blank, Steve |
| framework_caracteristicas_ventajas_beneficios | 1 | SPIN Selling - Neil Rackham |
| framework_efectividad_procesos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| framework_excelencia_operacional | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| framework_flujos_de_datos_ppp | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| framework_good_bad_product_manager | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| framework_ones_and_twos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| framework_ppph_flujos | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| framework_tres_rs_sucesion | 1 | The Founder's Dilemmas - Wasserman, Noam |
| franquicia_como_capital_alternativo | 1 | Franchise Your Business - Mark Siebert |
| franquicia_conversion | 1 | Franchise Your Business - Mark Siebert |
| franquicia_desarrollo_area | 1 | Franchise Your Business - Mark Siebert |
| franquicia_mas_crecimiento_corporativo_hibrido | 1 | Franchise Your Business - Mark Siebert |
| franquicia_representante_area | 1 | Franchise Your Business - Mark Siebert |
| franquicia_unidad_individual | 1 | Franchise Your Business - Mark Siebert |
| frecuencia_distribucion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| frenar_incoherencias_entrevista | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| fuentes_contratacion_ejecutivos | 1 | The Founder's Dilemmas - Wasserman, Noam |
| fuentes_datos_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| fuentes_financiamiento_startup | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| fuentes_investigacion_mercado | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| fuerza_bruta_industrial | 1 | Cradle to Cradle - Michael Braungart |
| funcion_detect_monitoreo_red | 1 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC) |
| funcion_identify_inventario_activos | 1 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC) |
| funcion_perdida_limites_especificacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| funcion_protect_politica_seguridad | 2 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC)<br>Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses |
| funcion_recover_restauracion | 1 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC) |
| funcion_respond_plan_incidentes | 2 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC)<br>NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide |
| funciones_del_departamento_de_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| fundadores_en_junta_directiva | 1 | The Founder's Dilemmas - Wasserman, Noam |
| fundadores_lideran_validacion | 1 | The Startup Owner's Manual - Blank, Steve |
| fundamentos_gestion_riesgo | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| fundamentos_inteligencia_financiera | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| funnel_get_customers_optimizacion | 1 | The Startup Owner's Manual - Blank, Steve |
| future_scenarios_planning | 2 | Business Model Generation - Osterwalder, Alexander<br>Winning at New Products - Robert G. Cooper |
| gamificacion_onboarding_visual | 1 | Never Lose a Customer Again - Joey Coleman |
| ganar_comprension_del_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| ganar_confianza_personas_cargo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| garantia_devolucion_dinero | 1 | Never Lose a Customer Again - Joey Coleman |
| garantias_implicitas_vs_expresas | 1 | Businessperson's Guide to Federal Warranty Law |
| garantias_producto_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| gate1_idea_screen | 1 | Winning at New Products - Robert G. Cooper |
| gate2_second_screen | 1 | Winning at New Products - Robert G. Cooper |
| gate3_go_to_development | 1 | Winning at New Products - Robert G. Cooper |
| gate4_go_to_testing | 1 | Winning at New Products - Robert G. Cooper |
| gate5_go_to_launch | 1 | Winning at New Products - Robert G. Cooper |
| gate_0_evaluacion_wishlist | 1 | Winning at New Products - Robert G. Cooper |
| gates_huecos_hollow_gates | 1 | Winning at New Products - Robert G. Cooper |
| gates_sin_dientes_problema | 1 | Winning at New Products - Robert G. Cooper |
| gates_tempranos_flexibles | 1 | Winning at New Products - Robert G. Cooper |
| genchi_gembutsu_salir_del_edificio | 1 | The Lean Startup - Eric Ries |
| generalistas_vs_especialistas | 1 | The Founder's Dilemmas - Wasserman, Noam |
| generar_insights_how_might_we | 1 | The field guide to human-centered design |
| generic_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gestion_alucinaciones_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| gestion_angel_investors | 1 | Venture Deals - Brad Feld |
| gestion_beneficios_alianza_sostenible | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_calidad_comunidad_a_escala | 1 | Traction - Gabriel Weinberg |
| gestion_capital_trabajo | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| gestion_centro_datos_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| gestion_configuracion_least_functionality | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| gestion_conflictos_franquicia | 1 | Franchise Your Business - Mark Siebert |
| gestion_confrontacion_ejecutiva | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| gestion_contrasenas_cui | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| gestion_contratos_desempeno | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_cuentas_por_cobrar | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| gestion_cuentas_por_pagar_dpo | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| gestion_datos_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gestion_de_aguas_pluviales_con_techos_verdes | 1 | Cradle to Cradle - Michael Braungart |
| gestion_de_conflictos_cofundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| gestion_de_errores | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| gestion_de_habitos_mentales_para_pensar | 1 | The Art of Thought - Wallas, Graham |
| gestion_de_las_cuatro_fases_del_negocio | 1 | The Lean Startup - Eric Ries |
| gestion_de_pensamientos_marginales | 1 | The Art of Thought - Wallas, Graham |
| gestion_de_portafolio_arriesgado | 1 | Winning at New Products - Robert G. Cooper |
| gestion_de_portafolio_gates_go_kill | 1 | Winning at New Products - Robert G. Cooper |
| gestion_de_problemas_sin_receta | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| gestion_decisiones_bajo_carga_emocional | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| gestion_del_cambio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gestion_desempeno_feedback | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| gestion_diferencias_culturales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| gestion_dinamica_de_fallas | 1 | The Field Guide to Understandin - Dekker, Sidney |
| gestion_dso | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| gestion_e_waste | 1 | The Green to Gold Business Play - Daniel C. Esty |
| gestion_efectiva_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gestion_empleados_brillantes_problematicos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| gestion_energia_equipos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| gestion_equilibrio_familia_startup | 1 | The Founder's Dilemmas - Wasserman, Noam |
| gestion_expectativas_equity_empleados | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| gestion_falsas_alarmas | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| gestion_fluctuaciones_cambiarias_clientes | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| gestion_forestal_regenerativa | 1 | Cradle to Cradle - Michael Braungart |
| gestion_incertidumbre_contratos | 1 | The Founder's Dilemmas - Wasserman, Noam |
| gestion_instalaciones | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_intraemprendedora_experimentacion | 1 | The Lean Startup - Eric Ries |
| gestion_inventario | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| gestion_junta_directiva_startup | 1 | The Founder's Dilemmas - Wasserman, Noam |
| gestion_libro_abierto_obm | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| gestion_logistica_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| gestion_materiales_peligrosos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| gestion_miedo_reportes | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| gestion_multiples_term_sheets | 1 | Venture Deals - Brad Feld |
| gestion_para_la_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gestion_participativa_qc_circle_supervisores | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| gestion_pedidos_order_management | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_portafolio_dos_niveles | 1 | Winning at New Products - Robert G. Cooper |
| gestion_portafolio_foco | 1 | Winning at New Products - Robert G. Cooper |
| gestion_portafolio_formal | 1 | Winning at New Products - Robert G. Cooper |
| gestion_procurement_consumo | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_rationing_shortage_gaming | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_relacion_bancaria | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| gestion_resistencia_cultural_cambio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gestion_responsabilidad_vicaria | 1 | Franchise Your Business - Mark Siebert |
| gestion_riesgo_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_riesgo_cambiario | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| gestion_riesgo_credito | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gestion_riesgo_seguridad_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| gestion_seguimiento_prospectos | 1 | Franchise Your Business - Mark Siebert |
| gestion_sindicato_inversores | 1 | Venture Deals - Brad Feld |
| gestion_terminacion_franquiciado | 1 | Franchise Your Business - Mark Siebert |
| gestion_testimonios | 1 | Never Lose a Customer Again - Joey Coleman |
| gestion_tiempo_lanzamiento_franquicia | 1 | Franchise Your Business - Mark Siebert |
| gestion_visual_del_pipeline_de_desarrollo | 1 | Winning at New Products - Robert G. Cooper |
| gestiona_contrato_tras_firma | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| gestionar_el_riesgo_es_de_adultos | 1 | DeMarco y Lister, Waltzing with Bears |
| gestionar_personas_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| gestionar_retencion_subordinado_valioso_renuncia | 1 | High Output Management - Andrew S. Grove |
| get_customers_funnel | 1 | The Startup Owner's Manual - Blank, Steve |
| get_customers_funnel_webmobile | 1 | The Startup Owner's Manual - Blank, Steve |
| get_out_building_test_sell | 1 | The Startup Owner's Manual - Blank, Steve |
| get_visual | 2 | The field guide to human-centered design<br>Change by Design, Revised and U - Tim Brown |
| getting_started_media_protection | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_personnel_security | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_physical_protection | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_planning | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_risk_assessment | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_security_assessment_monitoring | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_supply_chain_risk_management | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_system_communication_protection | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_system_information_integrity | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| getting_started_system_services_acquisition | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| global_vs_local_maximum | 1 | The Startup Owner's Manual - Blank, Steve |
| go_plan_de_accion | 1 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses |
| goal_statement_smart | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gobierno_corporativo_y_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| goodwill_en_adquisiciones | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| govern_cultura_privacidad | 1 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses |
| governance_integration_gates_portfolio_roadmap | 1 | Winning at New Products - Robert G. Cooper |
| grafico_box_jenkins | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| grafico_cusum | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| grafico_de_corrida_run_chart | 2 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev<br>Juran's Quality Handbook_ The C - Joseph A. Defeo |
| grafico_media_movil_ewma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| graficos_control_atributos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| graficos_control_individuales_operarios | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| graficos_control_multivariados | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| graficos_control_tiradas_cortas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| graficos_control_variables | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| graficos_de_control_uso | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| graficos_y_diagramas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| gratificacion_inmediata_producto | 1 | Never Lose a Customer Again - Joey Coleman |
| green_kaizen_events | 1 | The Green to Gold Business Play - Daniel C. Esty |
| green_six_sigma | 1 | The Green to Gold Business Play - Daniel C. Esty |
| green_team_oficina | 1 | The Green to Gold Business Play - Daniel C. Esty |
| guarda_lo_que_aprendiste_de_cada_golpe | 1 | Edwards et al., Managing Project Risks |
| guarda_un_colchon_de_tiempo_y_dinero | 1 | DeMarco y Lister, Waltzing with Bears |
| guia_entrevista_hcd | 1 | The field guide to human-centered design |
| guia_y_mentoria_vc | 1 | The Founder's Dilemmas - Wasserman, Noam |
| guiar_subordinado_etapas_resistencia_desempeno | 1 | High Output Management - Andrew S. Grove |
| guias_diseno_sistemas_estrategicos | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| gut_check | 1 | The field guide to human-centered design |
| habilidad_prompting_como_experticia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| habito_energetico_vs_mecanico | 1 | The Art of Thought - Wallas, Graham |
| hablar_con_clientes_desmontar_supuestos | 1 | The Lean Startup - Eric Ries |
| hacer_cajas_a_medida_del_pedido | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| hacer_critica_pares_transparente_ensenar_escribirla | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| hacer_opinion_accionable | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| hacer_remarcable_lo_requerido | 1 | Never Lose a Customer Again - Joey Coleman |
| hacer_repaso_posterior_proyecto | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| hacer_trabajo_futuro_imaginar_negocio | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| handoff_transicion_ventas_cuentas | 1 | Never Lose a Customer Again - Joey Coleman |
| hard_fixes_organizacionales | 1 | The Field Guide to Understandin - Dekker, Sidney |
| haz_tu_lista_de_lo_que_puede_fallar | 1 | DeMarco y Lister, Waltzing with Bears |
| heart_metodo_evaluacion_error_humano | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| heat_maps_eye_tracking | 1 | The Startup Owner's Manual - Blank, Steve |
| herramienta_fractal_triple_top_line | 1 | Cradle to Cradle - Michael Braungart |
| herramientas_accionadas_por_explosivos | 1 | SMALL_BUSINESS |
| herramientas_analisis_causa_raiz | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| herramientas_computacionales_business_model | 1 | Business Model Generation - Osterwalder, Alexander |
| herramientas_de_activacion_web | 1 | The Startup Owner's Manual - Blank, Steve |
| herramientas_de_diseno_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| herramientas_manuales_y_portatiles | 1 | SMALL_BUSINESS |
| herramientas_online_canal_fisico | 1 | The Startup Owner's Manual - Blank, Steve |
| hipotesis_de_canales | 1 | The Startup Owner's Manual - Blank, Steve |
| hipotesis_de_tamano_de_mercado | 1 | The Startup Owner's Manual - Blank, Steve |
| hipotesis_propuesta_de_valor_producto | 1 | The Startup Owner's Manual - Blank, Steve |
| hipotesis_relacion_clientes_web | 1 | The Startup Owner's Manual - Blank, Steve |
| hipotesis_valor_crecimiento | 1 | The Lean Startup - Eric Ries |
| hire_data_analytics_chief | 1 | The Startup Owner's Manual - Blank, Steve |
| hiring_blueprints | 1 | The Founder's Dilemmas - Wasserman, Noam |
| histograma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| histograma_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| historia_marca_diferenciacion | 1 | Franchise Your Business - Mark Siebert |
| hoist_auxiliary_equipment_safety | 1 | SMALL_BUSINESS |
| hoja_de_calculo_de_control | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| hoja_de_ruta_de_ventas | 1 | The Startup Owner's Manual - Blank, Steve |
| hoja_estimacion_costos | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| hojas_de_verificacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| homework_frontend_loading | 1 | Winning at New Products - Robert G. Cooper |
| homogeneidad_vs_diversidad_equipo | 1 | The Founder's Dilemmas - Wasserman, Noam |
| hoshin_kanri | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| hr_calidad_gestion | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| hr_como_control_de_calidad_gerencial | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| human_error_como_sintoma | 1 | The Field Guide to Understandin - Dekker, Sidney |
| human_in_the_loop_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| ia_como_nivelador_habilidades | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| ia_en_supply_chain | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| ia_generacion_ideas_negocio | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| ida_diagrama_influencia | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| ideacion_con_ia_en_la_sesion | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| identificacion_autenticacion_mfa | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| identificacion_bolsas_virales | 1 | Traction - Gabriel Weinberg |
| identificacion_brechas_funcionales | 1 | The Founder's Dilemmas - Wasserman, Noam |
| identificacion_de_riesgos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| identificacion_del_verdadero_cliente | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| identificacion_empleado_con_el_trabajo | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| identificacion_evaluacion_peligros | 2 | OSHA3885<br>OSHA3886 |
| identificacion_eventos_datos | 1 | The Field Guide to Understandin - Dekker, Sidney |
| identificacion_necesidad_sucesion_ceo | 1 | The Founder's Dilemmas - Wasserman, Noam |
| identificacion_oportunidades_sostenibilidad_marketing | 1 | The Green to Gold Business Play - Daniel C. Esty |
| identificacion_peligros_salud | 2 | OSHA3885<br>OSHA3886 |
| identificacion_practicas_lideres | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| identificacion_problema_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| identificacion_proveedores_criticos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| identificacion_recopilacion_informacion_peligros | 2 | OSHA3885<br>OSHA3886 |
| identificar_brechas_gaps | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| identificar_caracteristicas_metas_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| identificar_clientes_externos_e_internos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| identificar_competencias_tarjeta_puntuacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| identificar_consejo_asesores | 1 | The Startup Owner's Manual - Blank, Steve |
| identificar_disparadores_propios_reaccion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| identificar_earlyvangelists | 2 | The Startup Owner's Manual - Blank, Steve<br>Traction - Gabriel Weinberg |
| identificar_eco_riesgos_oportunidades | 1 | The Green to Gold Business Play - Daniel C. Esty |
| identificar_evaluar_socios_estrategicos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| identificar_high_value_jobs | 1 | Value Proposition Design |
| identificar_oportunidades_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| identificar_paso_limitante_jornada_desfases | 1 | High Output Management - Andrew S. Grove |
| identificar_pensadores_de_diseno_internos | 1 | Change by Design, Revised and U - Tim Brown |
| identificar_si_tu_producto_necesita_proteccion_especial | 1 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria |
| identificar_temas_formacion_tarjetas_decision | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| identify_mapeo_datos | 1 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses |
| imaginar_caso_simple_bragueta_abierta | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| impacto_calidad_ingresos_costos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| impacto_estado_resultados_en_balance | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| impedir_punialadas_espalda_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| implantar_politicas_respaldan_metodo | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| implementacion_controles | 2 | OSHA3885<br>OSHA3886 |
| implementacion_monitoreo_controles | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| implementar_controles | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| implementar_estrategias_reduccion_emisiones | 1 | The Green to Gold Business Play - Daniel C. Esty |
| import_regulations_foreign_governments | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| importancia_de_la_capacitacion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| impresion_inteligente | 1 | The Green to Gold Business Play - Daniel C. Esty |
| incentivos_internos_alineados_a_retencion | 1 | Never Lose a Customer Again - Joey Coleman |
| incentivos_no_monetarios_advocacy | 1 | Never Lose a Customer Again - Joey Coleman |
| incentivos_reconocimiento_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| incoterms_reglas_comerciales_internacionales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| indemnification_clause | 1 | Venture Deals - Brad Feld |
| indicadores_desempeno_recursos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| indice_cp | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| indice_cpk | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| indice_de_productividad | 1 | Winning at New Products - Robert G. Cooper |
| indice_de_reparabilidad | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| industrial_robots_automation | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| infection_control_plan | 1 | SMALL_BUSINESS |
| inferencia_estadistica_muestreo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| influence_map_organizacional | 1 | The Startup Owner's Manual - Blank, Steve |
| informar_cierre_jornada_conservar_propiedad_trabajo | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| information_driver_supply_chain | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| information_rights | 1 | Venture Deals - Brad Feld |
| informe_a_junta_directiva_despido_ejecutivo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| infundir_regularidad_reunion_proceso | 1 | High Output Management - Andrew S. Grove |
| ingenieria_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| ingenieria_calidad_proveedores | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| ingenieria_de_prompts_efectiva | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| ingenieria_inversa_metas | 1 | Franchise Your Business - Mark Siebert |
| ingresos_por_rebates | 1 | Franchise Your Business - Mark Siebert |
| inhibidores_del_breakthrough | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| innovacion_abierta | 1 | Winning at New Products - Robert G. Cooper |
| innovacion_abierta_externa | 1 | The Green to Gold Business Play - Daniel C. Esty |
| innovacion_como_apuesta_incremental | 1 | Winning at New Products - Robert G. Cooper |
| innovacion_tipo_ii | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| innovacion_tras_control_estadistico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| innovar_transformar_mercados | 1 | The Green to Gold Business Play - Daniel C. Esty |
| innovation_games_speedboat | 1 | Value Proposition Design |
| insight_de_wald | 1 | The Field Guide to Understandin - Dekker, Sidney |
| inspeccion_automatizada | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| inspeccion_caracteristicas_sensoriales | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| inspeccion_lugar_trabajo_peligros | 2 | OSHA3885<br>OSHA3886 |
| inspeccion_optima_proceso | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| inspeccionar_reparto_informacion_notas_jefe | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| inspecciones_superficiales_y_muestreo_incompleto | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| instalar_metodo_contratacion_empresa | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| institucionalizar_breakthrough | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| institucionalizar_capacitacion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| instituciones_financieras_bancos | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| insuficiencia_especificaciones | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| integracion_agresiva_ejecutivo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| integracion_deseabilidad_viabilidad_factibilidad_social | 1 | Change by Design, Revised and U - Tim Brown |
| integracion_sistemas_medicion_avanzada | 1 | The Green to Gold Business Play - Daniel C. Esty |
| integrar_peticion_critica_rutina_existente | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| integrar_trabajo_vida_mejor_version | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| inteligencia_de_anuncios_de_la_competencia | 1 | Traction - Gabriel Weinberg |
| intellectual_property_strategy | 2 | The Startup Owner's Manual - Blank, Steve<br>Venture Deals - Brad Feld |
| intercambio_de_roles_para_motivacion | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| internacionalizacion_sitio_web_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| internal_idea_capture | 1 | Winning at New Products - Robert G. Cooper |
| international_buyer_program | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| international_partner_search | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| interpretacion_graficos_variables | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| interrogar_negocio_cinco_preguntas | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| interrumpir_candidato_escucha_reflexiva | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| intimacion_emocional_como_senal_de_verdad | 1 | The Art of Thought - Wallas, Graham |
| introduccion_lean | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| inventar_tradiciones_celebrar_valores | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| inventario_conocimiento_estadistico_personal | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| inventory_analysis_lean | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| inversion_capacitacion_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| inversion_proporcional | 1 | The Lean Startup - Eric Ries |
| investiga_a_fondo_antes_de_renovar_un_contrato_existente | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| investigacion_analoga | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| investigacion_del_consumidor | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| investigacion_desarrollo_concepto | 1 | Franchise Your Business - Mark Siebert |
| investigacion_empresa_extranjera | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| investigacion_etnografica_ideacion | 2 | Winning at New Products - Robert G. Cooper<br>Change by Design, Revised and U - Tim Brown |
| investigacion_incidentes | 2 | OSHA3885<br>OSHA3886 |
| investigacion_mercado_primaria_secundaria_2 | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| investigacion_necesidades_consumidor | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| investigacion_new_view | 1 | The Field Guide to Understandin - Dekker, Sidney |
| investigar_antes_contratar_lideres | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| investigar_datos_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| invitar_desafio_reciproco_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| invitar_personas_necesarias_reunion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| involucramiento_empleados_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| involucramiento_fundador_busqueda_ceo | 1 | The Founder's Dilemmas - Wasserman, Noam |
| involucramiento_sindical_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| involucrar_empleados_ahorro_energetico | 1 | The Green to Gold Business Play - Daniel C. Esty |
| involucrar_varios_entrevistadores | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| iot_big_data_supply_chain | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| iota_analysis | 1 | Winning at New Products - Robert G. Cooper |
| ironias_de_la_automatizacion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| iso_31000_gestion_riesgo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| iso_ts_16949_automotriz | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| issue_log | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| issue_spotting_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| issue_spotting_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| jardines_terrenos_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| jerarquia_datos_scor | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| jerarquia_firma_vc | 1 | Venture Deals - Brad Feld |
| joint_ventures_internacionales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| juran_quality_by_design | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| juran_rcca_metodo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| just_do_its | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| just_in_time_manufacturing | 1 | The Green to Gold Business Play - Daniel C. Esty |
| justicia_restaurativa | 1 | The Field Guide to Understandin - Dekker, Sidney |
| juzgar_cultura_renuncias_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| kaizen_mejora_continua | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| kanban_validacion_aprendizaje | 1 | The Lean Startup - Eric Ries |
| keep_customers_strategy | 2 | The Startup Owner's Manual - Blank, Steve<br>Never Lose a Customer Again - Joey Coleman |
| key_partners_hypothesis | 1 | The Startup Owner's Manual - Blank, Steve |
| key_process_product_characteristics | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| key_resources_hypothesis | 2 | The Startup Owner's Manual - Blank, Steve<br>Business Model Generation - Osterwalder, Alexander |
| la_historia_de_la_empresa | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| la_lucha_resiliencia_ceo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| la_matriz_de_colores_te_engana | 1 | Hubbard, The Failure of Risk Management |
| landing_page_mvp | 1 | Value Proposition Design |
| lanzamiento_nuevos_productos_enfoque_problema | 1 | SPIN Selling - Neil Rackham |
| las_cuatro_ventas_franquicia | 1 | Franchise Your Business - Mark Siebert |
| las_formas_en_que_los_proyectos_mueren | 1 | DeMarco y Lister, Waltzing with Bears |
| launch_phase_roadmap | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| law_of_shitty_click_throughs | 1 | Traction - Gabriel Weinberg |
| lead_bullets_no_silver_bullets | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| lead_user_analysis | 1 | Winning at New Products - Robert G. Cooper |
| leaky_bucket_metaphor | 1 | Traction - Gabriel Weinberg |
| lean_launchpad_web_startup_process | 1 | The Startup Owner's Manual - Blank, Steve |
| lean_manufacturing | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| lean_manufacturing_tps | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| lean_six_sigma_roadmap | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| leap_of_faith_assumptions | 1 | The Lean Startup - Eric Ries |
| learning_card | 1 | Value Proposition Design |
| lectura_balance_general | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| lectura_estado_resultados | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| leer_seniales_fallo_jefe_reunion_solas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| legislacion_especifica_vs_accidente_organizacional | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| lenguajes_jerarquia_organizacional | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| lente_sostenibilidad_finanzas | 1 | The Green to Gold Business Play - Daniel C. Esty |
| lessons_learned | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| letra_de_cambio_bill_of_exchange | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| letter_of_intent_negociacion | 1 | Venture Deals - Brad Feld |
| letters_of_credit | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| leverage_en_negociacion_con_vcs | 1 | The Founder's Dilemmas - Wasserman, Noam |
| ley_de_capacidad_de_sistemas | 1 | The Field Guide to Understandin - Dekker, Sidney |
| licencia_exportacion_regulaciones | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| licencia_para_danar | 1 | Cradle to Cradle - Michael Braungart |
| licenciamiento_tecnologico | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| liderazgo_basado_en_valores_mas_alla_del_deber | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| liderazgo_calidad_mercado | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| liderazgo_ejecutivo_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| liderazgo_gerencial_seguridad | 2 | OSHA3885<br>OSHA3886 |
| lienzo_modelo_negocio | 3 | Business Model Generation - Osterwalder, Alexander<br>The field guide to human-centered design<br>Value Proposition Design |
| lienzo_proyecto_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| ligar_tareas_proposito_organizacion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| limitaciones_analisis_costo_beneficio | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| limitaciones_intervalos_confianza | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| limitaciones_ltif_indicador | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| limite_busqueda_causas_pendulo | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| limites_autorizacion_sistema | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| limites_control_estadistico_vs_tolerancias | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| limites_control_por_juicio_error | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| limites_de_especificacion_vs_limites_de_control | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| limites_de_la_voluntad_sobre_el_pensamiento | 1 | The Art of Thought - Wallas, Graham |
| limites_especificacion_dimensiones_interactuantes | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| limites_especificacion_funcionales | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| limites_tolerancia_estadistica | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| linea_base_costos | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| linking_environmental_performance_budgeting | 1 | The Green to Gold Business Play - Daniel C. Esty |
| listar_bueno_mejorable_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| listar_debilidades_disparadores_propios | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| listar_fuerzas_propias_cuatro_preguntas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| littles_law | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| llamar_lo_que_falta | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| lleva_scorecard_desempeno_proveedor | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| llevar_inventario_proyectos_discrecionales | 1 | High Output Management - Andrew S. Grove |
| local_rationality_principle | 1 | The Field Guide to Understandin - Dekker, Sidney |
| localizacion_internacionalizacion_web | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| lockout_tagout_procedures | 1 | SMALL_BUSINESS |
| logistica_inversa_rentable | 1 | The Green to Gold Business Play - Daniel C. Esty |
| logistica_inversa_retornos | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| long_tail_pattern | 1 | Business Model Generation - Osterwalder, Alexander |
| los_14_puntos_deming | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| los_controles_que_ya_tienes | 1 | Edwards et al., Managing Project Risks |
| los_tres_grandes_criterios | 1 | Franchise Your Business - Mark Siebert |
| mac_clause_gestion_riesgo | 1 | Venture Deals - Brad Feld |
| machine_guarding_abrasive_wheels | 1 | SMALL_BUSINESS |
| machinery_equipment_safety | 1 | SMALL_BUSINESS |
| make_certain_programa | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| mal_uso_histograma_vs_carta_control | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| manejar_enfado_persona_desafiada | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| manejo_crisis_auditoria_contable | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| manejo_de_hibridos_monstruosos | 1 | Cradle to Cradle - Michael Braungart |
| manejo_de_incertidumbre_proyectos_innovadores | 1 | Winning at New Products - Robert G. Cooper |
| manejo_de_quejas_entre_ejecutivos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| manejo_de_quimicos_peligrosos | 1 | SMALL_BUSINESS |
| manejo_empleados_en_adquisicion | 1 | Venture Deals - Brad Feld |
| manejo_objeciones_venta_franquicia | 1 | Franchise Your Business - Mark Siebert |
| manejo_problemas | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| manejo_psicologia_ceo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| manifiesto_agile | 1 | Winning at New Products - Robert G. Cooper |
| manten_viva_tu_lista_de_riesgos | 1 | DeMarco y Lister, Waltzing with Bears |
| mantener_manos_trabajo_real_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| mantener_proceso_evaluacion_ligero_vigilar_crecimiento | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| mantener_puntaje_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| mantenimiento_preventivo_orientado_al_cliente | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| mantenimiento_productivo_total | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| mantenimiento_productivo_total_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mantenimiento_sistema_cui | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| manual_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| manual_online_lms | 1 | Franchise Your Business - Mark Siebert |
| manufactura_aditiva_bajo_demanda | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| manufactura_celular | 1 | The Green to Gold Business Play - Daniel C. Esty |
| manufactura_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mapa_de_acceso_al_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| mapa_de_canal_de_ventas | 1 | The Startup Owner's Manual - Blank, Steve |
| mapa_de_influencia | 1 | The Startup Owner's Manual - Blank, Steve |
| mapa_de_proceso_planificacion_control | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| mapa_flujo_trabajo_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| mapa_organizacional_influencia | 1 | The Startup Owner's Manual - Blank, Steve |
| mapa_satisfaccion_importancia | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| mapear_servicio_antes_durante_despues | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| mapeo_capas_diseno | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| mapeo_de_patrones | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| mapeo_flujo_valor | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| mapeo_flujos_invisibles_datos | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| marcas_registradas | 1 | Venture Deals - Brad Feld |
| marco_analisis_mercado_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| marco_avances_continuaciones | 1 | SPIN Selling - Neil Rackham |
| marco_legal_comercio_electronico_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| marco_name_system_fee | 1 | Franchise Your Business - Mark Siebert |
| marco_nist_cybersecurity_framework | 1 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC) |
| marcos_historicos_comunidades_startup | 1 | Venture Deals - Brad Feld |
| marcos_pensamiento_dfe | 1 | The Green to Gold Business Play - Daniel C. Esty |
| margen_bruto | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| margen_neto | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| margen_operativo | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| market_type_revenue_growth | 1 | The Startup Owner's Manual - Blank, Steve |
| marketing_directo_y_llamadas_en_frio_franquicias | 1 | Franchise Your Business - Mark Siebert |
| marketing_verde_autentico | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mas_grande_mas_complejo_mas_riesgo | 1 | Edwards et al., Managing Project Risks |
| mash_ups | 1 | The field guide to human-centered design |
| mastery_sensibilidades_diseno | 1 | Change by Design, Revised and U - Tim Brown |
| materiales_ciclicos_infinitamente_reciclables | 1 | Cradle to Cradle - Michael Braungart |
| materiales_due_diligence | 1 | Venture Deals - Brad Feld |
| materials_handling_safety | 1 | SMALL_BUSINESS |
| matriz_asignacion_responsabilidades | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| matriz_de_planificacion_arbol | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| matriz_de_seleccion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| matriz_probabilidad_impacto | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| matriz_pugh | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| matriz_riesgo_conocido_desconocido | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| mecanica_conversion_deuda | 1 | Venture Deals - Brad Feld |
| mecanismo_resolucion_disputas | 1 | Businessperson's Guide to Federal Warranty Law |
| meda_analisis_error_mantenimiento | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| mediar_tiempo_palabra_reunion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| medical_services_first_aid | 1 | SMALL_BUSINESS |
| medicion_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| medicion_capacidad_servicio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| medicion_de_calidad_en_manufactura | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| medicion_desempeno_integrado | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| medicion_kpi | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| medicion_monitoreo_desempeno | 1 | Value Proposition Design |
| medicion_proactiva_procesos | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| medicion_resultados_marketing_franquicia | 1 | Franchise Your Business - Mark Siebert |
| medicion_servicios | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| medidas_proceso_vs_resultado | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| medidas_productividad_no_mejoran | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| medidas_reactivas_proactivas | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| medidas_tendencia_dispersion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| medir_comportamiento_cliente_mvp | 1 | The Startup Owner's Manual - Blank, Steve |
| medir_critica_respuesta_oyente_brujula | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| medir_guia_propia_pegatinas_marco | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| medir_huella_carbono_corporativa | 1 | The Green to Gold Business Play - Daniel C. Esty |
| medir_lo_que_importa_no_solo_lo_facil | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| medir_paquete_redondeando_hacia_arriba | 1 | Guia visual de empaque |
| medir_residuos_empresa | 1 | The Green to Gold Business Play - Daniel C. Esty |
| medir_satisfaccion_real_del_cliente | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| medir_sistema_venta_trece_indicadores_benchmark | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| meetups_bootstrapping_comunidad | 1 | Traction - Gabriel Weinberg |
| mejora_calidad_crosby | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| mejora_continua_del_proceso | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| mejora_continua_del_sistema | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| mejora_continua_operaciones | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| mejora_continua_relentless | 1 | Value Proposition Design |
| mejora_continua_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mejora_de_proceso_como_via_a_productividad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| mejora_del_sistema_responsabilidad_gerencial | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| mejora_envolvente_edificio | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mejora_valoracion_empresa | 1 | Franchise Your Business - Mark Siebert |
| mejorar_consciencia_propia_relacional_dos_practicas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| mejorar_deal_despues_del_hecho | 1 | Venture Deals - Brad Feld |
| menos_malo_vs_bueno | 1 | Cradle to Cradle - Michael Braungart |
| mensaje_desarrolladores_area | 1 | Franchise Your Business - Mark Siebert |
| mensaje_franquicias_conversion | 1 | Franchise Your Business - Mark Siebert |
| mensaje_marketing_franquicia | 1 | Franchise Your Business - Mark Siebert |
| mental_trial_and_error | 1 | The Art of Thought - Wallas, Graham |
| mentor_dos_tipos_de_amigos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| mercado_de_uno_fundraising | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| mercados_multilaterales | 1 | The Startup Owner's Manual - Blank, Steve |
| metabolismo_biologico_y_tecnico | 1 | Cradle to Cradle - Michael Braungart |
| metaforas_para_pensar | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| metas_de_seguridad_correctas | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| metas_desmaterializacion_energia | 1 | The Green to Gold Business Play - Daniel C. Esty |
| metas_negocio_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| metas_objetivos_smart_innovacion | 1 | Winning at New Products - Robert G. Cooper |
| metas_vs_proposito | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| metodo_conversion_notas_cap_table | 1 | Venture Deals - Brad Feld |
| metodo_payback | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| metodo_strategic_buckets | 1 | Winning at New Products - Robert G. Cooper |
| metodo_valor_presente_neto | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| metodologia_6s | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| metodologia_clara_reporte | 1 | The Green to Gold Business Play - Daniel C. Esty |
| metodologia_evaluacion_entrenamiento_ventas | 1 | SPIN Selling - Neil Rackham |
| metodologia_medicion_copq | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| metodologia_spin_selling | 1 | SPIN Selling - Neil Rackham |
| metodologias_analisis_territorio | 1 | Franchise Your Business - Mark Siebert |
| metodos_de_pago_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| metodos_de_pronostico | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| metodos_de_valuacion | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| metodos_exportacion_directa_indirecta_2 | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| metodos_pago_electronico_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| metricas_accionables | 1 | The Lean Startup - Eric Ries |
| metricas_calidad | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| metricas_como_validacion_cuantitativa | 1 | The Lean Startup - Eric Ries |
| metricas_de_adquisicion_activacion | 1 | The Startup Owner's Manual - Blank, Steve |
| metricas_de_startup | 1 | The Startup Owner's Manual - Blank, Steve |
| metricas_impacto_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| metricas_servicio_cliente_bts_bto | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| metrics_that_matter_framework | 1 | The Startup Owner's Manual - Blank, Steve |
| micro_experiencias_personalizadas | 1 | Never Lose a Customer Again - Joey Coleman |
| mide_lo_que_de_verdad_mueve_la_aguja | 1 | DeMarco y Lister, Waltzing with Bears |
| milestone_list | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| mini_folleto_franquicia | 1 | Franchise Your Business - Mark Siebert |
| minimizar_impuesto_colaboracion_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| minimizar_politica_organizacional | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| mission_and_operations_planning | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| mitigacion_efecto_latigo | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| mitigacion_riesgos_ambientales | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mitigar_falling_asleep_wheel | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| mito_departamento_control_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| mitos_stage_gate | 1 | Winning at New Products - Robert G. Cooper |
| mix_medios_marketing_franquicia | 1 | Franchise Your Business - Mark Siebert |
| mix_ubicaciones_corporativas_franquicia | 1 | Franchise Your Business - Mark Siebert |
| mobilizar_empleados_cultura_ecologica | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mock_sales | 1 | Value Proposition Design |
| modelado_simulacion_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| modelo_accidente_organizacional | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| modelo_barreras_defensas | 1 | The Field Guide to Understandin - Dekker, Sidney |
| modelo_cadena_de_eventos | 1 | The Field Guide to Understandin - Dekker, Sidney |
| modelo_contingencia_riesgo | 1 | Winning at New Products - Robert G. Cooper |
| modelo_costo_optimo_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| modelo_cradle_to_grave | 1 | Cradle to Cradle - Michael Braungart |
| modelo_curva_campana_ventas_franquicia | 1 | Franchise Your Business - Mark Siebert |
| modelo_customer_development | 1 | The Startup Owner's Manual - Blank, Steve |
| modelo_eco_criterios_ponderados | 1 | The Green to Gold Business Play - Daniel C. Esty |
| modelo_estrella_alineacion_organizacional | 1 | Business Model Generation - Osterwalder, Alexander |
| modelo_green_wave | 1 | The Green to Gold Business Play - Daniel C. Esty |
| modelo_hibrido_agile_stage_gate | 1 | Winning at New Products - Robert G. Cooper |
| modelo_lubin_esty_4_etapas | 1 | The Green to Gold Business Play - Daniel C. Esty |
| modelo_madurez_capacidades_cmmi | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| modelo_queso_suizo | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| modelo_servqual | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| modelo_shingo_evaluacion_excelencia | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| modelo_simulacion_cadena_suministro_circular | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| modelo_spin_preguntas | 2 | SPIN Selling - Neil Rackham<br>Traction - Gabriel Weinberg |
| modelo_tradicional_introduccion_producto | 1 | The Startup Owner's Manual - Blank, Steve |
| modelo_transformacion_juran | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| modelos_gestion_seguridad | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| modelos_negocio_mas_alla_del_lucro | 1 | Business Model Generation - Osterwalder, Alexander |
| modos_de_entrada_intermediarios | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| monetizacion_npv_caso_negocio | 1 | The Green to Gold Business Play - Daniel C. Esty |
| monitoreo_continuo | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| monitoreo_continuo_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| monocultura_como_paradigma | 1 | Cradle to Cradle - Michael Braungart |
| montar_equipo_gestion_desempenio_revisar_sistema | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| montar_evaluacion_360_grados_ligera_pares | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| montar_proceso_contratacion_reducir_sesgo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| montar_reunion_general_presentaciones_preguntas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| montar_reunion_gran_debate | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| montar_reunion_gran_decision | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| montar_reuniones_solas_mentalidad_frecuencia | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| montar_tablero_kanban_medir_actividades | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| monte_carlo_simulation_model | 1 | Winning at New Products - Robert G. Cooper |
| mostrar_candidato_cuanto_quieres | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| motivaciones_psicologicas_cofundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| motivaciones_reales_franquiciado | 1 | Franchise Your Business - Mark Siebert |
| motivated_management_franquiciado | 1 | Franchise Your Business - Mark Siebert |
| motor_crecimiento_pago | 1 | The Lean Startup - Eric Ries |
| motor_crecimiento_pegajoso | 1 | The Lean Startup - Eric Ries |
| motor_crecimiento_viral | 1 | The Lean Startup - Eric Ries |
| motor_de_crecimiento | 1 | The Lean Startup - Eric Ries |
| motor_idea_a_lanzamiento_agil | 1 | Winning at New Products - Robert G. Cooper |
| motores_de_seguridad_3cs | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| mover_rapido_persona_papel_equivocado | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| movilidad_verde_empleados | 1 | The Green to Gold Business Play - Daniel C. Esty |
| mrg_event | 1 | Winning at New Products - Robert G. Cooper |
| muestra_puntos_en_comun_antes_de_negociar | 1 | Chris Voss, Rompe la barrera del no |
| muestreo_aleatorio_operacional | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| muestreo_con_seguimiento_no_respondientes | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| muestreo_de_aceptacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| muestreo_dodge_romig | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| muestreo_estadistico_para_inspeccion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| multi_sided_market_channel | 1 | The Startup Owner's Manual - Blank, Steve |
| multi_sided_platforms | 1 | Business Model Generation - Osterwalder, Alexander |
| multiples_compradores_influyentes | 1 | Franchise Your Business - Mark Siebert |
| mvp_alta_fidelidad | 1 | The Startup Owner's Manual - Blank, Steve |
| mvp_catalogo_tecnicas | 1 | Value Proposition Design |
| mvp_tipo_video | 1 | The Lean Startup - Eric Ries |
| narrativa_como_herramienta_de_sentido | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| naturaleza_capital_de_riesgo_vc | 1 | The Founder's Dilemmas - Wasserman, Noam |
| navegacion_politica_organizacional | 1 | Change by Design, Revised and U - Tim Brown |
| necesidad_mantener_informado | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| necesidad_vs_deseo_en_ma | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| necesidades_implicitas_vs_explicitas | 1 | SPIN Selling - Neil Rackham |
| necesidades_psicologicas_cliente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| necesidades_reales_vs_declaradas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| necesidades_user_friendly | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| negocia_por_intereses_no_posiciones | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| negociacion_acuerdo_representante_extranjero | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| negociacion_carta_compromiso_banquero | 1 | Venture Deals - Brad Feld |
| negociacion_con_plazos_artificiales | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| negociacion_contratos_proveedores | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| netnografia_social_media | 1 | Winning at New Products - Robert G. Cooper |
| network_diagram | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| new_technology_error_pathways | 1 | The Field Guide to Understandin - Dekker, Sidney |
| new_view_human_error | 1 | The Field Guide to Understandin - Dekker, Sidney |
| new_view_investigation | 1 | The Field Guide to Understandin - Dekker, Sidney |
| new_view_vs_old_view | 1 | The Field Guide to Understandin - Dekker, Sidney |
| nist_privacy_framework_introduccion | 1 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses |
| niveles_calidad_muestreo_aql_lql_aoql | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| no_jugar_con_probabilidades | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| no_sacrificar_calidad_por_velocidad | 1 | The Lean Startup - Eric Ries |
| no_shop_agreement | 1 | Venture Deals - Brad Feld |
| no_shop_extension_negotiation | 1 | Venture Deals - Brad Feld |
| no_usar_triangulo_heinrich | 1 | The Field Guide to Understandin - Dekker, Sidney |
| nobody_cares_just_run_company | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| noise_exposure_control | 1 | SMALL_BUSINESS |
| nombra_tus_suposiciones_fragiles | 1 | DeMarco y Lister, Waltzing with Bears |
| nombrar_delegados_amigos_casa | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| nombrar_los_monstruos | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| normalizacion_datos_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| normalizacion_de_la_desviacion | 2 | Managing the Risks of Organizat - Reason, J. T_<br>The Field Guide to Understandin - Dekker, Sidney |
| normas_culturales_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| noticing_non_events | 1 | The Field Guide to Understandin - Dekker, Sidney |
| nueva_vision_organizacion_linea_seguridad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| nueve_pasos_iniciar_programa | 2 | OSHA3886<br>OSHA3885 |
| nueve_pecados_capitales_lanzamiento | 1 | The Startup Owner's Manual - Blank, Steve |
| nuevo_encargo_de_diseno | 1 | Cradle to Cradle - Michael Braungart |
| nutrientes_biologicos | 1 | Cradle to Cradle - Michael Braungart |
| nutrir_ideas_nuevas_reunion_solas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| observar_al_cliente_en_su_contexto | 1 | Never Lose a Customer Again - Joey Coleman |
| observar_reunion_rutinaria_senales_plantilla | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| obstaculos_innovacion_modelo_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| obtencion_compromiso | 1 | SPIN Selling - Neil Rackham |
| obtencion_compromiso_venta | 1 | SPIN Selling - Neil Rackham |
| obtencion_datos_factores_humanos | 1 | The Field Guide to Understandin - Dekker, Sidney |
| obtencion_de_compromiso | 1 | SPIN Selling - Neil Rackham |
| obtencion_marca_registrada | 1 | Franchise Your Business - Mark Siebert |
| ocho_desperdicios_lean | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| ocho_factores_exito_criticos | 1 | Winning at New Products - Robert G. Cooper |
| ocho_fases_experiencia_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| oficina_calidad_y_excelencia | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| oficina_digital_sin_papel_2 | 1 | The Green to Gold Business Play - Daniel C. Esty |
| ofrece_valor_no_economico | 1 | Chris Voss, Rompe la barrera del no |
| ofrecer_puntos_recogida | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| old_view_vs_new_view_human_error | 1 | The Field Guide to Understandin - Dekker, Sidney |
| onboarding_comunitario_y_lenguaje_propio | 1 | Never Lose a Customer Again - Joey Coleman |
| ooda_loop_decision | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| open_account | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| open_business_models | 1 | Business Model Generation - Osterwalder, Alexander |
| operacionalizacion_de_etiquetas_psicologicas | 1 | The Field Guide to Understandin - Dekker, Sidney |
| operar_modelo_gente_destreza_minima | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| oportunidades_ingresos_ti_sostenible | 1 | The Green to Gold Business Play - Daniel C. Esty |
| optimizacion_almacenes_distribucion | 1 | The Green to Gold Business Play - Daniel C. Esty |
| optimizacion_caracteristicas_diseno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| optimizacion_centro_datos_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| optimizacion_de_procesos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| optimizacion_embudo_get_customers | 1 | The Startup Owner's Manual - Blank, Steve |
| optimizacion_mercado_multilado | 1 | The Startup Owner's Manual - Blank, Steve |
| optimizacion_metricas_crecimiento | 1 | The Startup Owner's Manual - Blank, Steve |
| optimizacion_motores_busqueda | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| optimizacion_rutas_ecoruteo | 1 | The Green to Gold Business Play - Daniel C. Esty |
| optimizacion_tecnologia_cadena_suministro | 1 | The Green to Gold Business Play - Daniel C. Esty |
| option_pool_negociacion | 1 | Venture Deals - Brad Feld |
| orden_negociacion_puntos | 1 | Venture Deals - Brad Feld |
| organizacion_adaptativa | 1 | The Lean Startup - Eric Ries |
| organizacion_equipos_calidad_servicio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| organizacion_independiente_de_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| organizacion_interna_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| organizacion_liderazgo_estadistico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| organizaciones_alta_confiabilidad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| organizaciones_alta_confiabilidad_hro | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| organizaciones_ambidiestras | 1 | Business Model Generation - Osterwalder, Alexander |
| organizaciones_paralelas_cambio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| organizar_jornada_entrevistas_candidato | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| organizar_sistema_recoger_quejas_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| orgullo_por_el_trabajo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| original_issue_discount_oid | 1 | Venture Deals - Brad Feld |
| otras_fees_franquicia | 1 | Franchise Your Business - Mark Siebert |
| otros_terminos_contractuales | 1 | Franchise Your Business - Mark Siebert |
| outsourcing_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| outsourcing_funciones_franquicia | 1 | Franchise Your Business - Mark Siebert |
| outsourcing_ventas_fso | 1 | Franchise Your Business - Mark Siebert |
| overlapping_stages_concurrent_execution | 1 | Winning at New Products - Robert G. Cooper |
| owner_earnings | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| ownership_accountability_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| pagar_mas_por_velocidad | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| paradoja_bajos_incidentes_altas_fatalidades | 1 | The Field Guide to Understandin - Dekker, Sidney |
| paradoja_exito_emprendedor | 1 | The Founder's Dilemmas - Wasserman, Noam |
| paradoja_responsabilidad_creatividad | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| parar_debate_emocion_agotamiento | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| paris_convention_prioridad | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| participacion_ferias_comerciales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| participacion_preferente | 1 | Venture Deals - Brad Feld |
| participacion_trabajadores | 2 | OSHA3885<br>OSHA3886 |
| partir_meta_grande_hitos | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| partnerships_estrategicos_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| pasar_direccion_directa_indirecta | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| pasear_organizacion_hallar_problemas_pequenios | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| pasillos_superficies_transito | 1 | SMALL_BUSINESS |
| pasivos_vs_operadores | 1 | Franchise Your Business - Mark Siebert |
| paso1_libre_de_sustancias_x | 1 | Cradle to Cradle - Michael Braungart |
| paso2_preferencias_informadas | 1 | Cradle to Cradle - Michael Braungart |
| patent_cooperation_treaty | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| patent_mapping | 1 | Winning at New Products - Robert G. Cooper |
| patentes_startup | 1 | Venture Deals - Brad Feld |
| patrimonio_de_los_propietarios | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| patron_bait_hook | 1 | Business Model Generation - Osterwalder, Alexander |
| patron_free_business_model | 1 | Business Model Generation - Osterwalder, Alexander |
| patron_freemium | 1 | Business Model Generation - Osterwalder, Alexander |
| patron_inside_out | 1 | Business Model Generation - Osterwalder, Alexander |
| patron_outside_in | 1 | Business Model Generation - Osterwalder, Alexander |
| pay_to_play | 1 | Venture Deals - Brad Feld |
| pedir_ayuda_grupo_apoyo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| pedir_critica_anonima_curso_entrenamiento_dictado | 1 | High Output Management - Andrew S. Grove |
| pedir_critica_equipo_premiarla | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| pedir_critica_primero_crear_seguridad_psicologica | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| pedir_hechos_decision_evitar_recomendaciones | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| pedir_opinion_otros_mejorar | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| pedir_opinion_propia_reunion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| pedir_referencias_empleados | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| pedir_referencias_red_personal | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| pelear_proliferacion_reuniones_bloquear_ejecucion | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| peligro_capital_barato | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| peligros_emergencias_no_rutinarias | 2 | OSHA3885<br>OSHA3886 |
| penetracion_mercados_secundarios | 1 | Franchise Your Business - Mark Siebert |
| pensamiento_autoiniciado | 1 | The Art of Thought - Wallas, Graham |
| pensamiento_convergente_divergente | 2 | Change by Design, Revised and U - Tim Brown<br>Business Model Generation - Osterwalder, Alexander |
| pensamiento_de_conexiones_ripple_effect | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| pensamiento_espacial_mapeo | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| pensamiento_h2h | 1 | Never Lose a Customer Again - Joey Coleman |
| pensamiento_integrador | 1 | Change by Design, Revised and U - Tim Brown |
| pensamiento_no_guiado_vs_regulado | 1 | The Art of Thought - Wallas, Graham |
| pensamiento_serial_vs_espacial | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| pensamiento_visual_modelos_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| pensar_en_grande_empezar_pequeno | 1 | The Lean Startup - Eric Ries |
| pensar_en_verbos_no_sustantivos | 1 | Change by Design, Revised and U - Tim Brown |
| perdida_control_junta_directiva | 1 | The Founder's Dilemmas - Wasserman, Noam |
| perfeccionismo_vs_valor | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| permit_required_confined_spaces | 1 | SMALL_BUSINESS |
| perseguir_multiples_nortes | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| personal_protective_equipment | 1 | SMALL_BUSINESS |
| personalizacion_guiada_por_el_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| personalizacion_investigacion_prospecto | 1 | Never Lose a Customer Again - Joey Coleman |
| personalizar_interacciones_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| personas_productos_ganancias_orden | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| persuadir_emocion_oyente_no_propia | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| persuasion_directivos_prioridad_cliente | 1 | Never Lose a Customer Again - Joey Coleman |
| pide_una_revision_externa_antes_de_firmar_cualquier_contrato | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| piensa_en_rangos_no_en_numeros_unicos | 1 | Hubbard, The Failure of Risk Management |
| piggyback_marketing | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| pilares_control_calidad | 1 | Franchise Your Business - Mark Siebert |
| pilotos_estrategia_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| pipeline_alianzas_bd | 1 | Traction - Gabriel Weinberg |
| piramide_de_control | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| pisos_aberturas_paredes_seguridad | 1 | SMALL_BUSINESS |
| pivot_como_hipotesis_estrategica | 1 | The Lean Startup - Eric Ries |
| pivot_post_ventas | 1 | The Startup Owner's Manual - Blank, Steve |
| pivotar_o_perseverar | 1 | The Lean Startup - Eric Ries |
| pivote_estrategico | 2 | The Lean Startup - Eric Ries<br>The Startup Owner's Manual - Blank, Steve |
| pivote_o_proceder | 1 | The Startup Owner's Manual - Blank, Steve |
| plan_a_b_c_soft_landing | 1 | Venture Deals - Brad Feld |
| plan_accion_corto_mediano_largo_plazo | 1 | The Green to Gold Business Play - Daniel C. Esty |
| plan_accion_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| plan_b_antes_de_necesitarlo | 1 | Edwards et al., Managing Project Risks |
| plan_cambio_climatico | 1 | The Green to Gold Business Play - Daniel C. Esty |
| plan_continuation_bias | 1 | The Field Guide to Understandin - Dekker, Sidney |
| plan_control_peligros | 1 | OSHA3886 |
| plan_cumplimiento_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| plan_de_accion_de_emergencia | 1 | SMALL_BUSINESS |
| plan_de_accion_transformacion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| plan_de_activacion | 1 | The Startup Owner's Manual - Blank, Steve |
| plan_de_adquisicion_acquire | 1 | The Startup Owner's Manual - Blank, Steve |
| plan_de_contingencia_b | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| plan_de_control | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| plan_de_desastre_y_recuperacion | 1 | Edwards et al., Managing Project Risks |
| plan_de_implementacion_de_venta | 1 | The Startup Owner's Manual - Blank, Steve |
| plan_de_lanzamiento_al_mercado | 1 | Winning at New Products - Robert G. Cooper |
| plan_de_materiales_colaterales | 1 | The Startup Owner's Manual - Blank, Steve |
| plan_estrategico_franquicia | 1 | Franchise Your Business - Mark Siebert |
| plan_gestion_adquisiciones | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_gestion_calidad | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_gestion_cambios | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_gestion_comunicaciones | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_gestion_interesados | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_gestion_recursos_humanos | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_gestion_riesgos | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_mejora_procesos | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| plan_seguridad_sistema_poam | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| planes_de_muestreo_de_aceptacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planes_estatales_osha | 1 | SMALL_BUSINESS |
| planificacion_auditoria_individual | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_cadena_suministro | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_calidad_crosby | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| planificacion_cero_defectos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| planificacion_consecuencias_no_intencionadas | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| planificacion_de_la_inspeccion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_economica_conjunta | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_estrategica_despliegue | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_estrategica_despliegue_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_estudio_capacidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_gobierno_organizaciones_familiares | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_inicial_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_inspeccion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_itinerario_viaje_negocios | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| planificacion_preguntas_implicacion | 1 | SPIN Selling - Neil Rackham |
| planificacion_recoleccion_datos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| planificacion_recuperacion_post_accidente | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| planificacion_salida_estrategica | 1 | Franchise Your Business - Mark Siebert |
| planificacion_sucesion_ceo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| planificar_cinco_olas_venta | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| planificar_reduccion_trabajo_individual | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| planificar_tres_pasos_demanda_estado_brecha | 1 | High Output Management - Andrew S. Grove |
| plantea_oferta_como_rango_o_cifra_precisa | 1 | Chris Voss, Rompe la barrera del no |
| plantilla_fija_cotizaciones | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| plataforma_colaboracion_masiva | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| plataforma_colaboracion_tiempo_real | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| plataformas_comercio_electronico_marketplaces | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| playing_with_fire_gap | 1 | The Founder's Dilemmas - Wasserman, Noam |
| pocos_vitales_muchos_utiles | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| poder_a_traves_de_la_accion | 1 | The Art of Thought - Wallas, Graham |
| poka_yoke_a_prueba_de_errores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| politica_compras_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| politica_de_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| politica_formal_de_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| pool_opciones_empleados | 1 | Venture Deals - Brad Feld |
| por_que_balancea_el_balance | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| por_que_existen_los_term_sheets | 1 | Venture Deals - Brad Feld |
| portafolio_de_diseno | 1 | Change by Design, Revised and U - Tim Brown |
| portafolio_innovacion_diversificado | 1 | Change by Design, Revised and U - Tim Brown |
| portales_web_de_franquicias | 1 | Franchise Your Business - Mark Siebert |
| portfolio_management | 1 | Winning at New Products - Robert G. Cooper |
| portfolio_management_triangulation | 1 | Winning at New Products - Robert G. Cooper |
| posicionamiento_de_empresa | 1 | The Startup Owner's Manual - Blank, Steve |
| posicionamiento_est | 1 | Franchise Your Business - Mark Siebert |
| posicionamiento_por_tipo_de_mercado | 1 | The Startup Owner's Manual - Blank, Steve |
| posicionamiento_vs_competidores | 1 | Franchise Your Business - Mark Siebert |
| post_launch_review | 1 | Winning at New Products - Robert G. Cooper |
| power_of_nine_agile | 1 | Winning at New Products - Robert G. Cooper |
| powered_industrial_trucks_safety | 1 | SMALL_BUSINESS |
| ppc_para_venta_de_franquicias | 1 | Franchise Your Business - Mark Siebert |
| pr_no_convencional_stunts | 1 | Traction - Gabriel Weinberg |
| practica_de_observacion_atenta | 2 | Assembling Tomorrow: A Guide to Designing a Thriving Future<br>Change by Design, Revised and U - Tim Brown |
| practica_deliberada_asistida_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| practicar_franqueza_radical_jefe_propio | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| practicar_triangulo_critica_tres_papeles | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| practicas_gerenciales_no_delegables | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| practicas_manufactura_justo_a_tiempo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| pre_control_estadistico | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| precios_todos_los_dias_bajos | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| precision_exactitud_sensores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| prediccion_confiabilidad_diseno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| preferencia_de_liquidacion | 2 | Venture Deals - Brad Feld<br>The Founder's Dilemmas - Wasserman, Noam |
| preferencias_apiladas_vs_blended | 1 | Venture Deals - Brad Feld |
| preferir_inspeccion_proceso_prueba_destructiva | 1 | High Output Management - Andrew S. Grove |
| preframing_expectativas | 1 | Never Lose a Customer Again - Joey Coleman |
| pregunta_que_no_estamos_haciendo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| preguntar_conducir_reunion_individual | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| preguntar_contratar_unica_prioridad | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| preguntar_jefe_sonado_persona_cargo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| preguntar_por_que_no_que | 1 | Change by Design, Revised and U - Tim Brown |
| preguntar_que_no_quien | 1 | The Field Guide to Understandin - Dekker, Sidney |
| preguntar_seguimiento_hallar_huecos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| preguntas_abiertas_motivacion_proveedor | 1 | Chris Voss, Rompe la barrera del no |
| preguntas_clave_armadura_organizacional | 1 | The Field Guide to Understandin - Dekker, Sidney |
| preguntas_ipo_dolor_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| preguntas_need_payoff | 1 | SPIN Selling - Neil Rackham |
| preguntas_para_formacion_de_equipos | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| preguntas_problema_2 | 1 | SPIN Selling - Neil Rackham |
| preguntas_situacion | 1 | SPIN Selling - Neil Rackham |
| premiar_franqueza_hacer_escucha_tangible | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| premio_shingo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| prepara_posicion_agenda_antes_negociar | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| preparacion_conversacion_despido_ejecutivo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| preparacion_due_diligence | 1 | Venture Deals - Brad Feld |
| preparacion_materiales_fundraising | 1 | Venture Deals - Brad Feld |
| preparacion_para_salida_a_bolsa | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| preparacion_preguntas_problema_precall | 1 | SPIN Selling - Neil Rackham |
| preparar_candidato_validacion | 1 | Franchise Your Business - Mark Siebert |
| preparar_contacto_clientes | 1 | The Startup Owner's Manual - Blank, Steve |
| preparar_fdd | 1 | Franchise Your Business - Mark Siebert |
| preparar_guion_reunion_individual_subordinado | 1 | High Output Management - Andrew S. Grove |
| preparar_preguntas_entrevista_antemano | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| preparar_resena_mixta_hoja_trabajo | 1 | High Output Management - Andrew S. Grove |
| preparar_respuestas_estandar_interrupciones_repetidas | 1 | High Output Management - Andrew S. Grove |
| preparate_para_marcharte_del_trato | 1 | Chris Voss, Rompe la barrera del no |
| prepare_phase_roadmap | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| presales | 1 | Value Proposition Design |
| presentacion_inversionistas | 1 | Venture Deals - Brad Feld |
| presentacion_solucion_producto | 1 | The Startup Owner's Manual - Blank, Steve |
| presentaciones_alta_direccion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| presentate_con_tu_nombre_para_descuento | 1 | Chris Voss, Rompe la barrera del no |
| preservar_efectivo_buscar_modelo | 1 | The Startup Owner's Manual - Blank, Steve |
| presionar_curva_notas_evitar_forzarla | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| presupuesto_marketing_franquicia | 1 | Franchise Your Business - Mark Siebert |
| presupuesto_marketing_leads_franquicia | 1 | Franchise Your Business - Mark Siebert |
| presupuesto_publicidad_franquicia | 1 | Franchise Your Business - Mark Siebert |
| prevalencia_omisiones | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| prevencion_control_peligros | 2 | OSHA3885<br>OSHA3886 |
| prevencion_de_groupthink_en_evaluacion_de_riesgos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| prevencion_enfermedades_por_calor | 1 | SMALL_BUSINESS |
| prevencion_gestion_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| prevencion_objeciones_vs_manejo | 1 | SPIN Selling - Neil Rackham |
| prevencion_versus_control_de_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| prevencion_violencia_laboral | 1 | SMALL_BUSINESS |
| prevenir_franquicias_inadvertidas | 1 | Franchise Your Business - Mark Siebert |
| principio_apalancamiento_numero_magico | 1 | Franchise Your Business - Mark Siebert |
| principio_calidad_mvp | 2 | The Lean Startup - Eric Ries<br>The Hard Thing About Hard Things - Ben Horowitz |
| principio_correspondencia_contable | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| principio_enough_is_enough | 1 | Change by Design, Revised and U - Tim Brown |
| principio_green_tercer_boton | 1 | The Green to Gold Business Play - Daniel C. Esty |
| principio_humano_en_el_loop | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| principio_mejora_continua_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| principio_pareto | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| principio_reflexivo_contratacion | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| principios_alineacion_empresarial | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| principios_auditoria_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| principios_facilitadores_culturales | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| principios_gestion_calidad_iso9000 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| principios_gestion_error | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| principios_lean_startup | 1 | The Lean Startup - Eric Ries |
| principios_medicion_efectiva | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| principios_mejora_continua | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| priorizacion_hipercrecimiento | 1 | The Founder's Dilemmas - Wasserman, Noam |
| priorizacion_iniciativas_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| priorizacion_issues | 1 | The Green to Gold Business Play - Daniel C. Esty |
| priorizar_elementos_a_validar | 1 | The Startup Owner's Manual - Blank, Steve |
| priorizar_lista_entrenamiento_subordinados | 1 | High Output Management - Andrew S. Grove |
| priorizar_pocas_cosas_bien | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| pro_forma_vs_actuals | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| pro_rata_rights_deuda_convertible | 1 | Venture Deals - Brad Feld |
| probabilidad_falla_ensamblaje_multiple | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| probar_banquillo_vacaciones_largas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| probar_empaque_antes_de_escalar_envios | 1 | Guia de empaque para envios (FedEx) |
| probar_gestion_antes_decidir | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| probar_traje_azul_seis_semanas | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| problem_solution_fit | 1 | The Startup Owner's Manual - Blank, Steve |
| procedimientos_definidos_en_servicios | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| procesamiento_paralelo_con_espirales | 1 | Winning at New Products - Robert G. Cooper |
| proceso_benchmarking_juran_7pasos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| proceso_como_cadena_de_etapas | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| proceso_contratacion_ejecutivos_sin_experiencia | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| proceso_de_promocion_disciplinado | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| proceso_decision_vc | 1 | Venture Deals - Brad Feld |
| proceso_despidos_responsables | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| proceso_diseno_modelo_negocio_5_fases | 1 | Business Model Generation - Osterwalder, Alexander |
| proceso_ideacion_modelo_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| proceso_llamada_inicial_venta | 1 | Franchise Your Business - Mark Siebert |
| proceso_rmf_siete_pasos | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| proceso_sop_mop | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| proceso_venta_b2b | 1 | The Startup Owner's Manual - Blank, Steve |
| proceso_venta_franquicias | 1 | Franchise Your Business - Mark Siebert |
| procesos_contextuales_stage_gate | 1 | Winning at New Products - Robert G. Cooper |
| process_tracing_methods | 1 | The Field Guide to Understandin - Dekker, Sidney |
| procurement_audit | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| produccion_scheduling_balance_objetivos | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| produccion_y_proteccion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| product_backlog_agile | 1 | Winning at New Products - Robert G. Cooper |
| product_backlog_fisico | 1 | Winning at New Products - Robert G. Cooper |
| product_box_game | 1 | Value Proposition Design |
| product_design_spreadsheet | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| product_market_fit | 1 | The Startup Owner's Manual - Blank, Steve |
| product_roadmap_estrategico | 1 | Winning at New Products - Robert G. Cooper |
| producto_como_experimento | 1 | The Lean Startup - Eric Ries |
| producto_como_servicio_de_acceso | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| producto_mercado_fit_motores | 1 | The Lean Startup - Eric Ries |
| producto_minimo_viable | 2 | The Lean Startup - Eric Ries<br>The Startup Owner's Manual - Blank, Steve |
| producto_unico_superior | 1 | Winning at New Products - Robert G. Cooper |
| productos_crudos | 1 | Cradle to Cradle - Michael Braungart |
| productos_de_servicio | 1 | Cradle to Cradle - Michael Braungart |
| profundizar_respuestas_preguntas_curiosidad | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| programa_afiliados | 1 | Traction - Gabriel Weinberg |
| programa_auditoria_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| programa_cero_defectos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| programa_consulta_osha_onsite | 1 | SMALL_BUSINESS |
| programa_cumplimiento_legal | 1 | Franchise Your Business - Mark Siebert |
| programa_de_referidos_de_franquiciados | 1 | Franchise Your Business - Mark Siebert |
| programa_do_one_thing | 1 | The Green to Gold Business Play - Daniel C. Esty |
| programa_entrena_al_entrenador | 1 | Franchise Your Business - Mark Siebert |
| programa_entrenamiento_franquiciados | 1 | Franchise Your Business - Mark Siebert |
| programa_make_certain | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| programa_make_certain_2 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| programa_make_certain_3 | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| programa_mejora_calidad_14_pasos | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| programa_mentoria_proveedores | 1 | The Green to Gold Business Play - Daniel C. Esty |
| programa_proteccion_denunciantes | 1 | SMALL_BUSINESS |
| programa_proteccion_respiratoria | 1 | SMALL_BUSINESS |
| programa_reciclaje_integral | 1 | The Green to Gold Business Play - Daniel C. Esty |
| programa_referidos_exclusividad | 1 | Never Lose a Customer Again - Joey Coleman |
| programa_seguridad_salud_ocupacional | 2 | OSHA3885<br>SMALL_BUSINESS |
| programacion_cultura_empresarial | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| programacion_entregas_delivery_scheduling | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| programar_reunion_individual_cadena | 1 | High Output Management - Andrew S. Grove |
| programar_visita_area_observar_despachar | 1 | High Output Management - Andrew S. Grove |
| programas_5s_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| programas_compra_franquicia | 1 | Franchise Your Business - Mark Siebert |
| programas_cooperativos_osha | 1 | SMALL_BUSINESS |
| programas_estatales_locales_financiamiento_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| programas_ex_im_bank | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| prohibicion_tie_in_sales | 1 | Businessperson's Guide to Federal Warranty Law |
| project_charter | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| project_close_out | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| project_management_plan | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| project_performance_report | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| project_scope_statement | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| promocion_sitio_web | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| prompting_alta_variacion | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| prompting_cadena_de_pensamiento | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| prompting_por_persona_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| pronostico_de_demanda_variables | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| propagacion_de_ideas_meme | 1 | Change by Design, Revised and U - Tim Brown |
| proposito_como_motor_energia | 1 | The Art of Thought - Wallas, Graham |
| propuesta_valor_franquicia | 1 | Franchise Your Business - Mark Siebert |
| prospecto_emprendedor_flaming | 1 | Franchise Your Business - Mark Siebert |
| proteccion_del_tren_asociativo | 1 | The Art of Thought - Wallas, Graham |
| proteccion_marca_madrid_protocol | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| proteccion_organizacion_matriz_experimentos | 1 | The Lean Startup - Eric Ries |
| proteccion_patentes_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| proteccion_propiedad_intelectual_2 | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| proteccion_propiedad_intelectual_franq | 1 | Franchise Your Business - Mark Siebert |
| proteccion_propiedad_intelectual_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| protective_provisions | 1 | Venture Deals - Brad Feld |
| protective_provisions_alineacion | 1 | Venture Deals - Brad Feld |
| proteger_fragiles_caja_dentro_de_caja | 1 | DHL Express, Guia de empaque |
| proteger_tiempo_equipo_jefe | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| protocepto | 1 | Winning at New Products - Robert G. Cooper |
| protocolo_reuniones_gate | 1 | Winning at New Products - Robert G. Cooper |
| prototipado_de_experiencias | 1 | Change by Design, Revised and U - Tim Brown |
| prototipado_en_lo_salvaje | 1 | Change by Design, Revised and U - Tim Brown |
| prototipado_modelos_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| prototipado_organizacional_estrategico | 1 | Change by Design, Revised and U - Tim Brown |
| prototipado_rapido | 1 | Change by Design, Revised and U - Tim Brown |
| prototipado_virtual_mundos | 1 | Change by Design, Revised and U - Tim Brown |
| prototipar_con_medios_no_convencionales | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| prototyping_possibilities | 1 | Value Proposition Design |
| proyectos_vitales_pocos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| prueba_antes_de_comprometerse | 1 | The Founder's Dilemmas - Wasserman, Noam |
| prueba_hipotesis | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| prueba_mvp_alta_fidelidad | 1 | The Startup Owner's Manual - Blank, Steve |
| prueba_mvp_problema_baja_fidelidad | 1 | The Startup Owner's Manual - Blank, Steve |
| prueba_solucion_con_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| prueba_sustitucion_johnston | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| prueba_teorias_causa_raiz | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| pruebas_destructivas | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| pruebas_inadecuadas_prototipos | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| pruebas_no_parametricas_transformacion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| pruning_portafolio | 1 | Winning at New Products - Robert G. Cooper |
| publicidad_garantia_conforme | 1 | Businessperson's Guide to Federal Warranty Law |
| publicidad_impresa_franquicia | 1 | Franchise Your Business - Mark Siebert |
| publicidad_no_convencional_stunts | 1 | Traction - Gabriel Weinberg |
| publicidad_offline_pruebas_locales | 1 | Traction - Gabriel Weinberg |
| publicidad_remanente_remnant_ads | 1 | Traction - Gabriel Weinberg |
| publicidad_tradicional_pr | 1 | Traction - Gabriel Weinberg |
| pull_no_push | 1 | The Lean Startup - Eric Ries |
| punto_equilibrio_calidad_inspeccion | 2 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev<br>Juran's Quality Handbook_ The C - Joseph A. Defeo |
| punto_equilibrio_unidades | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| punto_unico_contacto_proveedores | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| puntos_brillantes_antes_del_pivote | 1 | Traction - Gabriel Weinberg |
| push_vs_pull_marketing | 1 | The Startup Owner's Manual - Blank, Steve |
| puzzle_prima_capital_privado | 1 | The Founder's Dilemmas - Wasserman, Noam |
| qfd_matriz | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| quality_audit | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| quality_awareness_crosby | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| quality_control_vs_quality_assurance | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| quality_score_optimizacion | 1 | Traction - Gabriel Weinberg |
| que_es_cui | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| que_hacer_con_un_riesgo_nuevo | 1 | Edwards et al., Managing Project Risks |
| quejas_llegan_tarde | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| quemar_las_naves_burning_the_boats | 1 | The Founder's Dilemmas - Wasserman, Noam |
| quimica_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| quimicos_toxicos_en_diseno | 1 | Cradle to Cradle - Michael Braungart |
| racional_mantenimiento_preventivo_correctivo | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| ranking_proyectos_por_npv | 1 | Winning at New Products - Robert G. Cooper |
| rapid_prototyping | 1 | The field guide to human-centered design |
| ratio_deuda_capital | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| ratios_eficiencia_inventario | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| ratios_liquidez | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| rcm_reliability_centered_maintenance | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| reacciones_al_fallo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| realizar_analisis_ciclo_de_vida_lca | 1 | The Green to Gold Business Play - Daniel C. Esty |
| realizar_analisis_ciclo_vida | 1 | The Green to Gold Business Play - Daniel C. Esty |
| realizar_pruebas_pasa_no_pasa | 1 | The Startup Owner's Manual - Blank, Steve |
| reasignacion_equity_fundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| rechazar_candidato_razones_relevantes | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| rechazar_conducta_toxica_entrevista | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| rechazar_contratacion_tibia | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| rechazo_gentil_prospecto | 1 | Franchise Your Business - Mark Siebert |
| rechazo_utilidades_corto_plazo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| reciclar_empleado_ascendido_mas_alla_capacidad | 1 | High Output Management - Andrew S. Grove |
| recoger_opinion_360_grados | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| recoleccion_validacion_datos_benchmarking | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| recomendaciones_smart | 1 | The Field Guide to Understandin - Dekker, Sidney |
| reconciliacion_utilidad_neta_flujo_caja | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| reconoce_las_tacticas_de_presion_y_urgencia_artificial_del_vendedor | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| reconocer_decision_dificil_valores | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| reconocer_el_sesgo_narrativo | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| reconocer_emociones_propias_avisar_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| reconocer_excelencia_trayectoria_gradual | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| reconocer_mercancia_peligrosa_disfrazada | 1 | Guia de empaque para envios (FedEx) |
| reconocer_recompensar_gente_estable | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| reconocer_recompensar_uso_metodo | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| reconocer_sesgo_de_apofenia | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| reconocimiento_al_desempeno | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| reconocimiento_de_ingresos | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| reconocimiento_publico_recompensas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| reconstruccion_contexto_situacional | 1 | The Field Guide to Understandin - Dekker, Sidney |
| reconstruccion_de_equipo_ejecutivo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| reconstruccion_significado_trabajo | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| recorrer_organizacion_escuchar_plantilla | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| recorrer_rueda_conscientemente_cultura_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| recorrer_rueda_hacer_cosas_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| recorrer_siete_pasos_programa_desarrollo_negocio | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| recorrer_trece_elementos_proceso_evaluacion_formal | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| recursos_apoyo_gubernamental_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| recursos_de_segundo_nivel | 1 | The Founder's Dilemmas - Wasserman, Noam |
| recursos_ecosistema_emprendedor | 1 | Venture Deals - Brad Feld |
| recursos_educativos_osha | 1 | SMALL_BUSINESS |
| recursos_externos_seguridad | 1 | SMALL_BUSINESS |
| recursos_humanos_cultura | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| recursos_niosh | 1 | SMALL_BUSINESS |
| red_flags_proyectos_en_problemas | 1 | Winning at New Products - Robert G. Cooper |
| redactar_mision_tarjeta_puntuacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| redemption_rights | 1 | Venture Deals - Brad Feld |
| redes_de_seguridad_regulatoria | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| rediseno_procesos_negocio_cx | 1 | Never Lose a Customer Again - Joey Coleman |
| rediseno_tras_fracaso_proyecto | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| reduccion_cargas_regulatorias | 1 | The Green to Gold Business Play - Daniel C. Esty |
| reduccion_de_tiempo_de_ciclo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| reduccion_inventario_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| reduccion_residuos_construccion | 1 | The Green to Gold Business Play - Daniel C. Esty |
| reduccion_riesgo_franquiciante | 1 | Franchise Your Business - Mark Siebert |
| reduccion_riesgo_percibido | 1 | Franchise Your Business - Mark Siebert |
| reduccion_tamano_de_lote_batch_size | 1 | The Lean Startup - Eric Ries |
| reduccion_tiempo_ciclo | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| reduccion_tiempo_de_mercado_velocidad | 1 | Winning at New Products - Robert G. Cooper |
| reducciones_cadena_suministro | 1 | The Green to Gold Business Play - Daniel C. Esty |
| reduce_el_riesgo_a_lo_razonable | 1 | Edwards et al., Managing Project Risks |
| reducir_devoluciones_mejorando_informacion_previa | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| reducir_playing_with_fire_gap | 1 | The Founder's Dilemmas - Wasserman, Noam |
| redundancia_en_diseno | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| reempaquetado_producto | 1 | The Startup Owner's Manual - Blank, Steve |
| reemplazarse_trabajo_propio | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| reevolucion_industrial | 1 | Cradle to Cradle - Michael Braungart |
| referidos_franquiciados_existentes | 1 | Franchise Your Business - Mark Siebert |
| refinar_sales_roadmap | 1 | The Startup Owner's Manual - Blank, Steve |
| reformular_problema_mas_alla_del_producto | 1 | Change by Design, Revised and U - Tim Brown |
| reforzar_principios_guia_lenguaje_prueba_conocimiento | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| regalos_estrategicos_personalizados | 1 | Never Lose a Customer Again - Joey Coleman |
| registration_rights_stock_consideration | 1 | Venture Deals - Brad Feld |
| registro_de_riesgos | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| registro_estatal_franquicia | 1 | Franchise Your Business - Mark Siebert |
| registro_lecciones_aprendidas_compra | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| registro_reporte_lesiones | 1 | SMALL_BUSINESS |
| regla_50_por_ciento | 1 | Traction - Gabriel Weinberg |
| regla_de_minimis | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| regla_disponibilidad_previa_venta | 1 | Businessperson's Guide to Federal Warranty Law |
| regla_divulgacion_garantia | 1 | Businessperson's Guide to Federal Warranty Law |
| regla_simplificada_tolerancia_errores | 1 | The Lean Startup - Eric Ries |
| regla_todo_o_nada_inspeccion_2 | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| reglas_aprendizaje_habilidades_venta | 1 | SPIN Selling - Neil Rackham |
| reglas_brainstorming | 2 | Business Model Generation - Osterwalder, Alexander<br>Change by Design, Revised and U - Tim Brown |
| reglas_de_origen_fta_2 | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| reglas_deming_consultoria_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| reglas_gestion_riesgo_gambling | 1 | Winning at New Products - Robert G. Cooper |
| reglas_origen_sectoriales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| regulatory_process_model | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| rehacer_flujo_paso_limitante_capacidad | 1 | High Output Management - Andrew S. Grove |
| reincorporacion_del_trabajo_previo | 1 | The Art of Thought - Wallas, Graham |
| reinicio_programa_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| reinvencion_constante | 1 | Value Proposition Design |
| reinvencion_diseno_nutrivehiculo | 1 | Cradle to Cradle - Michael Braungart |
| rejilla_madurez_gestion_calidad | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| relacion_confiabilidad_sistema_partes | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| relacion_continua_con_cliente | 1 | SPIN Selling - Neil Rackham |
| relacion_doble_reporte_dotted_line | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| relacion_franquiciador_franquiciado | 1 | Franchise Your Business - Mark Siebert |
| relacion_largo_plazo_proveedor_unico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| relacion_previa_y_estructura_roles | 1 | The Founder's Dilemmas - Wasserman, Noam |
| relaciones_con_clientes | 1 | Business Model Generation - Osterwalder, Alexander |
| relaciones_humanas_auditoria | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| relaciones_largo_plazo_con_proveedores | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| relaciones_publicas_leads_franquicia | 1 | Franchise Your Business - Mark Siebert |
| relocalizacion_clustering_logistico | 1 | The Green to Gold Business Play - Daniel C. Esty |
| remover_barreras_orgullo_trabajo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| rendicion_de_cuentas_del_equipo | 1 | Winning at New Products - Robert G. Cooper |
| rentabilidad_incrementada_franquicia | 1 | Franchise Your Business - Mark Siebert |
| reparar_mal_comportamiento_evitar_disculpa_falsa | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| repartir_decision_cercanos_hechos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| repartir_equipo_cartera_horizontes | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| repartir_material_antes_reunion | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| repartir_notas_publicar_reparto_esperado | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| repartir_papeles_directivo_reclutador | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| repartir_responsabilidad_contratar_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| repartir_semana_cuarenta_horas_jefe | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| repartir_supervision_puesto_funcional_mision | 1 | High Output Management - Andrew S. Grove |
| repartir_tiempo_atencion_mejores_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| reparto_inicial_equity | 1 | The Founder's Dilemmas - Wasserman, Noam |
| repetir_mensaje_invariable_diario_reunion_evento | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| replicar_resultados | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| reporta_el_riesgo_sin_maquillaje | 1 | Edwards et al., Managing Project Risks |
| reporte_auditoria | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| reporte_casi_accidentes | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| reporte_confidencial_seguridad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| reporte_estado_miembro_equipo | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| reporte_gerencial_diagnostico_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| reporte_sostenibilidad_digital | 1 | The Green to Gold Business Play - Daniel C. Esty |
| representar_actividad_caja_negra_ventanas | 1 | High Output Management - Andrew S. Grove |
| reps_warranties_indemnizacion | 1 | Venture Deals - Brad Feld |
| requirements_documentation | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| requirements_management_plan | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| requirements_traceability_matrix | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| requisitos_lider_de_rrhh | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| requisitos_numericos_calidad_lotes | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| requisitos_sistema_retroalimentacion | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| resegmentacion_mercado_nicho_bajo_costo | 1 | The Startup Owner's Manual - Blank, Steve |
| reservar_calendario_tiempo_ejecutar | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| reservar_media_hora_semanal_talento | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| reservar_tiempo_reflexion_metas | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| reservar_valor_unico_prioridades_arriba | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| reservas_de_capital_vc | 1 | Venture Deals - Brad Feld |
| reset_total_de_expectativas | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| resistencia_al_cambio | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| resistir_dar_solucion_clasificar_decision_urgencia | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| resolucion_problemas_de_pago | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| resolucion_problemas_niveles_supervision | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| resolver_desencaje_valores_persona_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| resolver_dudas_frecuentes_pedir_critica | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| resolver_dudas_frecuentes_reuniones_salto_nivel | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| resolver_problemas_climaticos_clientes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| resource_assessment | 1 | The field guide to human-centered design |
| resource_breakdown_structure | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| respetar_cautelas_legales_contratacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| respetar_cuidar_persona_cargo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| respeto_a_la_diversidad | 1 | Cradle to Cradle - Michael Braungart |
| responder_8_preguntas_construir_primary_aim | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| responder_critica_abrasiva_cuatro_reglas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| responder_primer_aviso_renuncia_subordinado | 1 | High Output Management - Andrew S. Grove |
| responder_tres_preguntas_vocacion_directiva | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| responsabilidad_de_seguridad_en_linea | 1 | The Field Guide to Understandin - Dekker, Sidney |
| responsabilidad_extendida_productor_2 | 1 | The Green to Gold Business Play - Daniel C. Esty |
| responsabilidad_gerencial_causas_comunes | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| responsabilidad_gerencial_en_la_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| responsabilidad_hacia_abajo_vs_rendicion_de_cuentas | 1 | The Field Guide to Understandin - Dekker, Sidney |
| responsabilidad_personal_en_gestion | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| responsabilidad_prospectiva | 1 | The Field Guide to Understandin - Dekker, Sidney |
| responsabilidad_sistemica | 1 | The Field Guide to Understandin - Dekker, Sidney |
| responsabilidades_desarrollo_talento_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| responsabilizacion_del_trabajador | 1 | The Field Guide to Understandin - Dekker, Sidney |
| respuesta_consultas_internacionales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| respuesta_estrategica_a_amenaza_competitiva | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| respuesta_incidentes_cui | 1 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer |
| restricciones_extremas_como_innovacion | 1 | Change by Design, Revised and U - Tim Brown |
| restricciones_reputacionales | 1 | Venture Deals - Brad Feld |
| resumen_de_datos_graficos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| retar_superestrellas_equipo_constantemente | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| retargeting_display | 1 | Traction - Gabriel Weinberg |
| retention_metrics | 1 | The Startup Owner's Manual - Blank, Steve |
| retirar_barreras_politicas_metodo | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| retirar_directivos_rechazan_metodo | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| retirar_etiquetas_permanentes_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| retorno_sobre_activos | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| retorno_sobre_capital | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| retroalimentacion_cliente_mejora_servicio | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| retroalimentacion_franquiciados | 1 | Franchise Your Business - Mark Siebert |
| retroalimentacion_inmediata_de_errores | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| retroalimentacion_shock_pensamiento_original | 1 | The Art of Thought - Wallas, Graham |
| reunion_conclusion_proyecto | 1 | Never Lose a Customer Again - Joey Coleman |
| reunion_pivotar_o_perseverar | 1 | The Lean Startup - Eric Ries |
| reuniones_diarias_eliminar_bloqueos | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| reuniones_uno_a_uno | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| reunir_informacion_gerencial_vias_variadas | 1 | High Output Management - Andrew S. Grove |
| revela_tu_propio_plazo_limite_al_negociar | 1 | Chris Voss, Rompe la barrera del no |
| revenue_pricing_hypothesis | 1 | The Startup Owner's Manual - Blank, Steve |
| review_mesh_evaluacion_por_calificacion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| revisa_tus_riesgos_con_un_ritmo | 1 | Edwards et al., Managing Project Risks |
| revisar_banderas_rojas_candidato | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| revisar_ciclo_responsabilidades_relaciones | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| revisar_cinco_causas_mal_desempenio | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| revisar_critica_mujer_agresiva_cuatro_tacticas | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| revisar_incentivos_trampas_equipo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| revisar_necesidades_de_empaque | 1 | DHL Express, Guia de empaque |
| revisar_proposito_personas_proceso | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| revisar_tres_preguntas_valor_carrera | 1 | High Output Management - Andrew S. Grove |
| revision_aplicabilidad_estandares_osha | 1 | SMALL_BUSINESS |
| revision_de_aprendizaje | 1 | The Field Guide to Understandin - Dekker, Sidney |
| revision_diseno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| revision_legal_marketing | 1 | Franchise Your Business - Mark Siebert |
| revision_portafolio_periodica | 1 | Winning at New Products - Robert G. Cooper |
| revision_progreso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| revisiones_regulares_desempeno_ceo | 1 | The Founder's Dilemmas - Wasserman, Noam |
| revolucion_relaciones_proveedores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rework_por_el_causante | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| riesgo_actividades_mantenimiento | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| riesgo_beneficio_retener_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| riesgo_concepto_vs_amenaza_competitiva | 1 | Franchise Your Business - Mark Siebert |
| riesgo_contra_valor_vale_la_pena | 1 | DeMarco y Lister, Waltzing with Bears |
| riesgo_contratar_amigos_familia | 1 | The Founder's Dilemmas - Wasserman, Noam |
| riesgo_control_algoritmico | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| riesgo_del_negocio_o_del_proyecto | 1 | Edwards et al., Managing Project Risks |
| riesgo_error_humano_en_mantenimiento | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| riesgo_fiduciario_insolvencia_deuda | 1 | Venture Deals - Brad Feld |
| riesgo_litigios_franquicia | 1 | Franchise Your Business - Mark Siebert |
| riesgo_no_es_mala_suerte | 1 | Edwards et al., Managing Project Risks |
| riesgo_no_pivotar_a_tiempo | 1 | The Lean Startup - Eric Ries |
| riesgo_recompensa_ideas_audaces | 1 | Business Model Generation - Osterwalder, Alexander |
| riesgo_sobredependencia_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| riesgo_split_51_49 | 1 | The Founder's Dilemmas - Wasserman, Noam |
| riesgo_titulos_inflados | 1 | The Founder's Dilemmas - Wasserman, Noam |
| riesgos_consenso_inspeccion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| riesgos_del_enfoque_en_error_humano | 1 | The Field Guide to Understandin - Dekker, Sidney |
| riesgos_lanzamiento_mvp | 1 | The Lean Startup - Eric Ries |
| right_of_first_refusal_pro_rata | 1 | Venture Deals - Brad Feld |
| risk_audit | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| rmf_paso_categorizar | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| rmf_paso_preparar | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| roadmap_despliegue_lean_six_sigma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| roadmap_proyectos_operacionales_12_meses | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| roi_proyectos_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_alta_direccion_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_black_belt_six_sigma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_de_la_fuerza_laboral_en_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_de_mandos_medios_y_supervisores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_del_equipo_de_trabajo_en_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_director_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_facilitador_equipos_mejora | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_gates_agile | 1 | Winning at New Products - Robert G. Cooper |
| rol_green_belt_six_sigma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_lider_equipo_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| rol_tactico_estrategico_oficina | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| role_playing | 1 | The field guide to human-centered design |
| roles_equipo_proyecto_six_sigma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| roles_product_owner_scrum_master | 1 | Winning at New Products - Robert G. Cooper |
| roles_responsabilidades | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| roles_six_sigma | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| romper_vision_en_experimentos | 1 | The Lean Startup - Eric Ries |
| rotacion_activos | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| rotacion_equipo_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| runway_como_numero_de_pivotes | 1 | The Lean Startup - Eric Ries |
| ruptura_de_habitos_para_estimulo | 1 | The Art of Thought - Wallas, Graham |
| rutas_salida_planificacion_emergencias | 1 | SMALL_BUSINESS |
| saber_hasta_donde_mejorar_servicio | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| safe_simple_agreement_future_equity | 1 | Venture Deals - Brad Feld |
| safety_case_evaluacion_formal | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| safety_culture_engineering | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| safety_i_safety_ii | 1 | The Field Guide to Understandin - Dekker, Sidney |
| sales_funnel_get_keep_grow | 1 | The Startup Owner's Manual - Blank, Steve |
| sales_operations_planning | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| sales_roadmap | 1 | The Startup Owner's Manual - Blank, Steve |
| sales_roadmap_vs_sales_force | 1 | The Startup Owner's Manual - Blank, Steve |
| salir_de_la_cabeza_movimiento_espacial | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| sandbox_de_innovacion | 1 | The Lean Startup - Eric Ries |
| satisfaccion_vs_insatisfaccion_kano | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sbrefa_cumplimiento | 1 | SMALL_BUSINESS |
| schedule_management_plan | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| scope_management_plan | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| scor_model_operaciones | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| scorecard_de_seleccion_de_proyectos | 1 | Winning at New Products - Robert G. Cooper |
| scorecard_descubrimiento_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| scorecard_desempeno_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| scorecards_criterios_gate | 1 | Winning at New Products - Robert G. Cooper |
| screening_mercados_potenciales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| search_for_business_model | 3 | The Startup Owner's Manual - Blank, Steve<br>Value Proposition Design<br>The Lean Startup - Eric Ries |
| second_wind_energia_mental | 1 | The Art of Thought - Wallas, Graham |
| seduccion_modelo_persona | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| seed_deals_riesgos_precedente | 1 | Venture Deals - Brad Feld |
| seeding_canal_viral | 1 | Traction - Gabriel Weinberg |
| seesaw_salario_equity | 1 | The Founder's Dilemmas - Wasserman, Noam |
| segmentacion_consumidor_verde | 1 | The Green to Gold Business Play - Daniel C. Esty |
| segmentacion_perfil_franquiciado | 1 | Franchise Your Business - Mark Siebert |
| segmentar_clientes_nivel_servicio | 1 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management |
| segmentos_de_clientes_problema_necesidad | 1 | The Startup Owner's Manual - Blank, Steve |
| segregacion_funciones_trading_settlement | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| seguimiento_accion_correctiva | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| seguimiento_cumplimiento_cadena_suministro | 1 | The Green to Gold Business Play - Daniel C. Esty |
| seguimiento_efectividad_controles | 2 | OSHA3885<br>OSHA3886 |
| seguimiento_tendencias_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| seguir_frustrado_preguntar_implantacion_ideas | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| seguridad_electrica | 1 | SMALL_BUSINESS |
| seguridad_producto | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| seguridad_soldadura_corte_bronceado | 1 | SMALL_BUSINESS |
| seguridad_trabajadores_jovenes | 1 | SMALL_BUSINESS |
| seguro_de_credito_a_la_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seguro_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seguro_inversion_opic | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seis_canales_comunicacion_assess | 1 | Never Lose a Customer Again - Joey Coleman |
| seis_formas_innovar_perfil_cliente | 1 | Value Proposition Design |
| seis_herramientas_comunicacion_celebracion | 1 | Never Lose a Customer Again - Joey Coleman |
| seis_herramientas_comunicacion_fase_activate | 1 | Never Lose a Customer Again - Joey Coleman |
| seleccion_abogado_venture | 1 | Venture Deals - Brad Feld |
| seleccion_agente_carga_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seleccion_arenas_estrategicas | 1 | Winning at New Products - Robert G. Cooper |
| seleccion_banquero_ma | 1 | Venture Deals - Brad Feld |
| seleccion_canal_distribucion | 1 | The Startup Owner's Manual - Blank, Steve |
| seleccion_canal_fisico | 1 | The Startup Owner's Manual - Blank, Steve |
| seleccion_canales_distribucion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seleccion_ceo_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| seleccion_consultor_franquicias | 1 | Franchise Your Business - Mark Siebert |
| seleccion_controles | 1 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide |
| seleccion_de_distribuidor_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seleccion_de_metodo_de_pago | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seleccion_de_proveedores_por_costo_total | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| seleccion_dominio_web | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seleccion_estrategia_pricing | 1 | The Startup Owner's Manual - Blank, Steve |
| seleccion_estructura_corporativa | 1 | Venture Deals - Brad Feld |
| seleccion_estructura_franquicia | 1 | Franchise Your Business - Mark Siebert |
| seleccion_fuente_unica_multiple | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| seleccion_hacer_o_comprar | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| seleccion_mensajeros_creibles | 1 | The Green to Gold Business Play - Daniel C. Esty |
| seleccion_metodo_transporte_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seleccion_modelo_ia_adecuado | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| seleccion_plan_muestreo_ansi_z14 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| seleccion_plataforma_social_ads | 1 | Traction - Gabriel Weinberg |
| seleccion_prestamista_relacion_vs_transaccion | 1 | Venture Deals - Brad Feld |
| seleccion_productos_servicios_verdes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| seleccion_proyectos_agile | 1 | Winning at New Products - Robert G. Cooper |
| seleccion_proyectos_six_sigma_basada_en_copq | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| seleccion_relaciones_cofundadores | 1 | The Founder's Dilemmas - Wasserman, Noam |
| seleccion_representante_extranjero | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| seleccionar_diseno_general_proceso | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| seleccionar_jugador_cuatro_entrevistas | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| seleccionar_tipo_de_lca_segun_recursos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| self_regulation_deregulation_tradeoffs | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| sellar_cajas_metodo_cinta_en_h | 1 | Guia de empaque para envios (FedEx) |
| sem_estrategia_ejecucion | 1 | Traction - Gabriel Weinberg |
| seminario_de_exito_para_gerencia | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |
| senales_alerta_no_atendidas | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| senales_de_compra_en_venta_grande | 1 | SPIN Selling - Neil Rackham |
| senalizacion_de_salidas | 1 | SMALL_BUSINESS |
| sensor_medicion_desempeno | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sentido_del_humor_como_herramienta_de_pensamiento | 1 | The Art of Thought - Wallas, Graham |
| seo_estrategia_fat_head | 1 | Traction - Gabriel Weinberg |
| seo_link_building | 1 | Traction - Gabriel Weinberg |
| seo_long_tail | 1 | Traction - Gabriel Weinberg |
| seo_para_captacion_de_franquiciados | 1 | Franchise Your Business - Mark Siebert |
| separa_la_visita_de_evaluacion_de_la_decision_de_compra | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| separar_hechos_de_percepcion | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| separar_opciones_dfe | 1 | The Green to Gold Business Play - Daniel C. Esty |
| ser_buen_jig | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| ser_honesto_transparente_desempenio | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| servicio_postventa_internacional | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| servicizacion_producto | 1 | The Green to Gold Business Play - Daniel C. Esty |
| sesgo_optimismo_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| sesgo_retrospectivo | 1 | The Field Guide to Understandin - Dekker, Sidney |
| sesgo_retrospectivo_hindsight_2 | 2 | The Field Guide to Understandin - Dekker, Sidney<br>Managing the Risks of Organizat - Reason, J. T_ |
| sesgos_naturales_del_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| shadow_ia_organizacional | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| shapeshifting_diversidad | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| shareholder_representative_role | 1 | Venture Deals - Brad Feld |
| sharp_end_blunt_end | 1 | The Field Guide to Understandin - Dekker, Sidney |
| shingo_enterprise_excellence_model | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| shingo_prize | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| shock_and_awe_kit_bienvenida | 1 | Never Lose a Customer Again - Joey Coleman |
| siete_razones_fracaso_productos | 1 | Winning at New Products - Robert G. Cooper |
| sigue_operando_pese_al_golpe | 1 | Edwards et al., Managing Project Risks |
| silla_vacia_del_cliente_en_decisiones | 1 | Never Lose a Customer Again - Joey Coleman |
| simplificar_trabajo_reducir_numero_pasos | 1 | High Output Management - Andrew S. Grove |
| simulacion_clientes_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| simulacion_de_operaciones_supply_chain | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| simular_riesgos_transito_antes_de_enviar | 1 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria |
| single_double_multiple_sampling | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sintesis_de_insights_en_principios_de_diseno | 1 | Change by Design, Revised and U - Tim Brown |
| sintesis_hipotesis_modelo_negocio | 1 | The Startup Owner's Manual - Blank, Steve |
| sipoc | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_captura_ideas | 1 | Winning at New Products - Robert G. Cooper |
| sistema_de_alarma_de_defectos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_estable_causas_comunes | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| sistema_estable_responsabilidad_gerencial | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| sistema_gates_go_kill | 1 | Winning at New Products - Robert G. Cooper |
| sistema_gestion_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| sistema_gestion_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_gestion_cumplimiento_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| sistema_informacion_calidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_inmune_producto | 1 | The Lean Startup - Eric Ries |
| sistema_lms_entrenamiento | 1 | Franchise Your Business - Mark Siebert |
| sistema_manejo_quejas | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_medicion_kpi | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_pull_push | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_puntuacion_baldrige | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sistema_recoleccion_datos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| sistema_responsabilidad_gerencial | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| sistema_responsabilidad_gerencial_2 | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| sistema_take_back | 1 | Cradle to Cradle - Michael Braungart |
| sistema_triage_x_gray_p_list | 1 | Cradle to Cradle - Michael Braungart |
| sistema_triple_a_stage_gate | 1 | Winning at New Products - Robert G. Cooper |
| sistema_visibilidad_cadena_suministro_low_cost | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| sistemas_alta_confiabilidad_hro | 1 | The Field Guide to Understandin - Dekker, Sidney |
| sistemas_de_extincion_de_incendios | 1 | SMALL_BUSINESS |
| sistemas_organizacionales_ia | 1 | Co-Intelligence_ Living and Wor - Ethan Mollick |
| sistemas_participativos_abiertos | 1 | Change by Design, Revised and U - Tim Brown |
| sistemas_sabios_vs_ignorantes | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| sistemas_sociotecnicos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sitio_web_franquicia | 1 | Franchise Your Business - Mark Siebert |
| situar_transicion_cuatro_caminos | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| six_sigma_dmaic | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| skunk_works_proyectos_paralelos | 1 | Winning at New Products - Robert G. Cooper |
| smed_setup_reduction | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| social_ads_indirect_response | 1 | Traction - Gabriel Weinberg |
| solicitud_cambio | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| solidificar_defensa_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| sop_colaborativo | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| sopesar_consejo_legal_despedir_humildad | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| soporte_continuo_franquicia | 1 | Franchise Your Business - Mark Siebert |
| soporte_publicidad_marketing | 1 | Franchise Your Business - Mark Siebert |
| soporte_segunda_victima | 1 | The Field Guide to Understandin - Dekker, Sidney |
| sorprender_cliente_estrategico | 1 | Never Lose a Customer Again - Joey Coleman |
| sostener_cambio_contexto_continuo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| sostener_contacto_oferta_aceptacion | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| sostener_las_ganancias | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sostenibilidad_agil | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| sostenibilidad_cafeteria_oficina | 1 | The Green to Gold Business Play - Daniel C. Esty |
| sostenibilidad_local_y_materiales | 1 | Cradle to Cradle - Michael Braungart |
| speaking_engagements_estrategia | 1 | Traction - Gabriel Weinberg |
| split_testing | 1 | Value Proposition Design |
| split_testing_experimentos_ab | 1 | The Lean Startup - Eric Ries |
| sprint_board_burn_down | 1 | Winning at New Products - Robert G. Cooper |
| stage5_launch | 1 | Winning at New Products - Robert G. Cooper |
| stage_gate_system | 1 | Winning at New Products - Robert G. Cooper |
| stage_gate_td_tecnologia | 1 | Winning at New Products - Robert G. Cooper |
| stage_gate_tipos_proyectos | 1 | Winning at New Products - Robert G. Cooper |
| staging_de_inversiones_como_control | 1 | The Founder's Dilemmas - Wasserman, Noam |
| stakeholder_analysis_matrix | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| stakeholder_mapping_wheel | 1 | The Green to Gold Business Play - Daniel C. Esty |
| stakeholder_register | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| starting_points_innovacion | 1 | Value Proposition Design |
| startup_como_experimento_cientifico | 1 | The Lean Startup - Eric Ries |
| storyboard | 1 | The field guide to human-centered design |
| storytelling_como_herramienta_de_diseno | 1 | Change by Design, Revised and U - Tim Brown |
| storytelling_como_herramienta_diseno | 1 | Change by Design, Revised and U - Tim Brown |
| storytelling_modelo_negocio | 1 | Business Model Generation - Osterwalder, Alexander |
| strat_map_arenas_estrategicas | 1 | Winning at New Products - Robert G. Cooper |
| subfranquicia_master | 1 | Franchise Your Business - Mark Siebert |
| subir_productividad_gerencial_tres_vias | 1 | High Output Management - Andrew S. Grove |
| subir_vara_calidad_equipo | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| sucesion_iniciada_por_fundador | 1 | The Founder's Dilemmas - Wasserman, Noam |
| suenos_completos_diseno_responsable | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| sujetos_de_control | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| superacion_accidia_creativa | 1 | The Art of Thought - Wallas, Graham |
| superioridad_calidad_market_share | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| supervisar_decision_delegada_preguntas_concretas | 1 | High Output Management - Andrew S. Grove |
| supervisar_tarea_delegada_etapa_menor_valor | 1 | High Output Management - Andrew S. Grove |
| supervision_a_liderazgo | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| supply_chain_management_systems | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| supuestos_de_procedimientos | 1 | The Field Guide to Understandin - Dekker, Sidney |
| sustitucion_quimica_sinergetica | 1 | Cradle to Cradle - Michael Braungart |
| swot_business_model_canvas | 1 | Business Model Generation - Osterwalder, Alexander |
| tablero_control_scorecard | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| tacticas_cold_calling | 1 | Traction - Gabriel Weinberg |
| tacticas_de_ferias_comerciales | 1 | Traction - Gabriel Weinberg |
| tacticas_negociacion_bd | 1 | Traction - Gabriel Weinberg |
| takt_time | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| tamano_junta_directiva_vc | 1 | The Founder's Dilemmas - Wasserman, Noam |
| targeting_blogs_traccion | 1 | Traction - Gabriel Weinberg |
| tasa_captura_leads | 1 | Franchise Your Business - Mark Siebert |
| tasa_crecimiento_sostenible | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| tasa_de_retorno_requerida | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| tasa_interna_retorno_irr | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| team_directory | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| team_member_performance_assessment | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| team_operating_agreement | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| team_performance_assessment | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| teatro_del_exito | 1 | The Lean Startup - Eric Ries |
| technology_platform_evaluation | 1 | Winning at New Products - Robert G. Cooper |
| tecnica_anclaje_negociacion | 1 | Venture Deals - Brad Feld |
| tecnica_cambio_de_perspectiva_escala | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| tecnica_freaky_friday | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| tecnica_perder_objeto | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| tecnicas_calma_ceo | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| tecnicas_para_sacar_riesgos_a_la_luz | 1 | Edwards et al., Managing Project Risks |
| tecnologia_como_medio_no_fin | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| tecnologias_disruptivas_oportunidad | 1 | Winning at New Products - Robert G. Cooper |
| tecnologias_emergentes_cadena_suministro | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| tecnologias_manufactura_avanzada | 1 | The Green to Gold Business Play - Daniel C. Esty |
| teletrabajo_sostenible | 1 | The Green to Gold Business Play - Daniel C. Esty |
| temas_legales_empleo | 1 | Venture Deals - Brad Feld |
| ten_reglas_claras_para_avisar_a_proveedores_no_elegidos | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| ten_un_checklist_de_clausulas_de_contrato | 1 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) |
| teoremas_probabilidad | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| teoria_accidentes_normales | 1 | The Field Guide to Understandin - Dekker, Sidney |
| teoria_de_juegos_en_negociacion | 1 | Venture Deals - Brad Feld |
| teoria_de_la_gestion | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| teoria_de_restricciones | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| teoria_desastres_organizacionales | 1 | The Field Guide to Understandin - Dekker, Sidney |
| teoria_equidad_split_equity | 1 | The Founder's Dilemmas - Wasserman, Noam |
| teoria_sistemas_seguridad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| teoria_triple_rol_sistemas_abiertos | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| term_sheet_disposiciones_vinculantes | 1 | Venture Deals - Brad Feld |
| term_sheet_negociacion | 1 | Venture Deals - Brad Feld |
| terminologia_clave_breakthrough | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| terminos_adicionales_deuda_convertible | 1 | Venture Deals - Brad Feld |
| tesis_boulder_compromiso_largo_plazo | 1 | Venture Deals - Brad Feld |
| tesis_boulder_inclusividad | 1 | Venture Deals - Brad Feld |
| tesis_boulder_liderazgo_emprendedor | 1 | Venture Deals - Brad Feld |
| tesis_boulder_stack_emprendedor | 1 | Venture Deals - Brad Feld |
| test_ab_precio | 1 | Value Proposition Design |
| test_card | 1 | Value Proposition Design |
| test_rico_vs_rey | 1 | The Founder's Dilemmas - Wasserman, Noam |
| test_socios_de_trafico | 1 | The Startup Owner's Manual - Blank, Steve |
| testear_circulo_cuadrado_rectangulo | 1 | Value Proposition Design |
| testing_process_completo | 1 | Value Proposition Design |
| thin_edge_of_the_wedge | 1 | The Field Guide to Understandin - Dekker, Sidney |
| three_rs_equilibrium | 1 | The Founder's Dilemmas - Wasserman, Noam |
| ti_para_desempeno_ecologico | 1 | The Green to Gold Business Play - Daniel C. Esty |
| tiempo_ciclo_viral | 1 | Traction - Gabriel Weinberg |
| timing_equity_split | 1 | The Founder's Dilemmas - Wasserman, Noam |
| timing_solicitud_referidos | 1 | Never Lose a Customer Again - Joey Coleman |
| tipos_adquisiciones_tecnologia | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| tipos_benchmarking_por_participante | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| tipos_criterios_gate | 1 | Winning at New Products - Robert G. Cooper |
| tipos_de_clientes | 1 | The Startup Owner's Manual - Blank, Steve |
| tipos_de_pasivos | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| tipos_de_riesgo_invencion_vs_mercado | 1 | The Startup Owner's Manual - Blank, Steve |
| tipos_de_utilidad | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| tipos_escalas_medicion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| tipos_planes_muestreo_atributos_variables | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| tipos_sitio_web_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| tirania_intergeneracional_remota | 1 | Cradle to Cradle - Michael Braungart |
| toma_decisiones_bajo_incertidumbre | 1 | The Hard Thing About Hard Things - Ben Horowitz |
| tomar_accion_deliberada_pausar_vocalizar_gesticular | 1 | Turn the Ship Around! A True Story of Turning Followers into Leaders - L. David Marquet |
| tomar_mando_reunion_pares_presidente_ausente | 1 | High Output Management - Andrew S. Grove |
| tomar_notas_copia_guion_reunion_individual | 1 | High Output Management - Andrew S. Grove |
| tpm_maintenance | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| trabajo_como_imaginado_vs_trabajo_como_hecho | 1 | The Field Guide to Understandin - Dekker, Sidney |
| trabajo_con_bancos_comerciales | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| trabajo_en_lotes_pequenos | 1 | The Lean Startup - Eric Ries |
| traccion_como_metrica_clave | 1 | Traction - Gabriel Weinberg |
| traction_channel_bias | 1 | Traction - Gabriel Weinberg |
| traction_goal | 1 | Traction - Gabriel Weinberg |
| trade_fair_certification_program | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| trade_missions | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| trade_off_responsividad_eficiencia | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| traduccion_necesidades_cliente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| traduce_stock_muerto_numeros | 1 | Max Muller, Essentials of Inventory Management |
| transferencia_de_actividades_a_departamentos_de_linea | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| transfiere_lo_que_no_debes_cargar | 1 | Edwards et al., Managing Project Risks |
| transformacion_calidad_compromiso_alta_direccion_japon | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| transformacion_gerencial_para_la_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| transformacion_organizacional_diseno | 1 | Change by Design, Revised and U - Tim Brown |
| transicion_energia_diversa_renovable | 1 | Cradle to Cradle - Michael Braungart |
| transicion_jerarquia_startup | 1 | The Founder's Dilemmas - Wasserman, Noam |
| transicion_organizacional_fluido_a_formal | 1 | The Founder's Dilemmas - Wasserman, Noam |
| transicion_post_sucesion | 1 | The Founder's Dilemmas - Wasserman, Noam |
| transicion_producto_a_experiencia | 1 | Change by Design, Revised and U - Tim Brown |
| transitar_aprendiz_primeros_meses | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| transitar_jefe_nuevo_equipo_establecido | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| transitar_pionero_equipo_nuevo | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| transitar_sucesor_equipo_entero | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| transitarios_freight_forwarders | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| transmitir_objetivos_prioridades_preferencias | 1 | High Output Management - Andrew S. Grove |
| transparencia_crisis_reputacional | 1 | The Green to Gold Business Play - Daniel C. Esty |
| transparencia_datos_ambientales | 1 | The Green to Gold Business Play - Daniel C. Esty |
| transparencia_facturacion | 1 | Never Lose a Customer Again - Joey Coleman |
| transporte_bajas_emisiones | 1 | The Green to Gold Business Play - Daniel C. Esty |
| tratar_jefe_entrenador | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| tratar_las_historias_como_herramientas | 1 | Assembling Tomorrow: A Guide to Designing a Thriving Future |
| tratar_packaging_costo_marca | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| trayectoria_del_accidente | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| trazabilidad_de_lotes | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| trazar_modelo_negocio_cliente_primero | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| trazar_plan_dieciocho_meses_aprendizaje | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| tres_as_de_metricas | 1 | The Lean Startup - Eric Ries |
| tres_espacios_innovacion_prototipado | 1 | Change by Design, Revised and U - Tim Brown |
| tres_palancas_rentabilidad | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| tres_preguntas_carrera | 1 | The Founder's Dilemmas - Wasserman, Noam |
| tres_tipos_desperdicio_tps | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| triangulo_de_interaccion_calidad | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| trilogia_de_juran | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| trilogia_juran_qa_qc | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| triple_bottom_line | 1 | The Green to Gold Business Play - Daniel C. Esty |
| triple_bottom_line_2 | 1 | The Green to Gold Business Play - Daniel C. Esty |
| triple_top_line | 1 | Cradle to Cradle - Michael Braungart |
| tripod_beta_analisis_incidentes | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| tripod_delta_general_failure_types | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| tu_gestion_de_riesgo_funciona | 1 | Hubbard, The Failure of Risk Management |
| tus_alertas_tempranas | 1 | DeMarco y Lister, Waltzing with Bears |
| ubicacion_estrategica_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| un_dueno_para_cada_riesgo | 1 | Edwards et al., Managing Project Risks |
| unbundling_business_models | 1 | Business Model Generation - Osterwalder, Alexander |
| understanding_customers_tecnicas | 1 | Value Proposition Design |
| unidades_medida_sensores | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| unificar_color_forma_vestuario_modelo | 1 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It - Michael E. Gerber |
| unique_link_tracking | 1 | Value Proposition Design |
| unique_selling_proposition_statement | 1 | The Startup Owner's Manual - Blank, Steve |
| unirse_organizacion_rsc_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| unstabilized_approach_go_around | 1 | The Field Guide to Understandin - Dekker, Sidney |
| upsell_post_logro | 1 | Never Lose a Customer Again - Joey Coleman |
| usa_el_no_del_proveedor_a_tu_favor | 1 | Chris Voss, Rompe la barrera del no |
| usa_preguntas_de_como_para_negociar_precio | 1 | Chris Voss, Rompe la barrera del no |
| usa_reglas_proveedor_palabra_justo | 1 | Chris Voss, Rompe la barrera del no |
| usa_silencio_no_partas_diferencia | 1 | Chris Voss, Rompe la barrera del no |
| usability_testing_producto | 1 | The Startup Owner's Manual - Blank, Steve |
| usar_banco_nueve_preguntas_entrevista | 1 | High Output Management - Andrew S. Grove |
| usar_calendario_herramienta_planificacion_produccion | 1 | High Output Management - Andrew S. Grove |
| usar_lenguaje_no_discriminatorio_entrevista | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| usar_tres_clases_reunion_proceso | 1 | High Output Management - Andrew S. Grove |
| uso_del_us_commercial_service | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| uso_inadecuado_computadoras | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| uso_intermediarios_exportacion | 1 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) |
| uso_regulaciones_como_espada | 1 | The Green to Gold Business Play - Daniel C. Esty |
| usuarios_extremos_edge_cases | 1 | Change by Design, Revised and U - Tim Brown |
| usuarios_extremos_globales | 1 | Change by Design, Revised and U - Tim Brown |
| vacios_conocimiento_cliente | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| validacion_certificaciones_terceros | 1 | The Green to Gold Business Play - Daniel C. Esty |
| validacion_con_franquiciados | 1 | Franchise Your Business - Mark Siebert |
| validacion_externa_reportes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| validacion_hipotesis_ingresos | 1 | The Startup Owner's Manual - Blank, Steve |
| validacion_sistema_medicion | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| validacion_sistema_medicion_2 | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| validar_canal_distribucion | 1 | The Startup Owner's Manual - Blank, Steve |
| validar_modelo_financiero | 1 | The Startup Owner's Manual - Blank, Steve |
| validar_modelo_negocio_hechos | 1 | The Startup Owner's Manual - Blank, Steve |
| validar_posicionamiento_con_analistas | 1 | The Startup Owner's Manual - Blank, Steve |
| valor_de_vida_del_cliente | 1 | The Startup Owner's Manual - Blank, Steve |
| valor_futuro | 1 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe |
| valor_intangible_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| valor_presente_franquicia_pvf | 1 | Franchise Your Business - Mark Siebert |
| valor_vs_desperdicio | 1 | The Lean Startup - Eric Ries |
| valoracion_costos_externos | 1 | The Green to Gold Business Play - Daniel C. Esty |
| valorar_logro_tres_comparaciones | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| valores_centrales_baldrige | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| valuacion_409a | 1 | Venture Deals - Brad Feld |
| valuacion_pre_post_money | 1 | Venture Deals - Brad Feld |
| valuation_cap_deuda_convertible | 1 | Venture Deals - Brad Feld |
| value_map | 1 | Value Proposition Design |
| value_non_value_added_analysis | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| value_proposition_canvas | 1 | Value Proposition Design |
| value_proposition_startup | 1 | The Startup Owner's Manual - Blank, Steve |
| value_stream_mapping_ambiental | 1 | The Green to Gold Business Play - Daniel C. Esty |
| variance_analysis | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| variar_frecuencia_inspeccion_nivel_calidad | 1 | High Output Management - Andrew S. Grove |
| vehiculos_autonomos_drones_supply_chain | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| vehiculos_combustibles_alternativos_2 | 1 | The Green to Gold Business Play - Daniel C. Esty |
| velocidad_crecimiento_franquicia | 1 | Franchise Your Business - Mark Siebert |
| velocidad_crecimiento_franquicia_2 | 1 | Franchise Your Business - Mark Siebert |
| vencer_sindrome_grupo_pares_autoconfianza | 1 | High Output Management - Andrew S. Grove |
| vender_abastecimiento_candidatos | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| vender_cambio_trabajo_familia | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| vender_concepto_franquicia | 1 | Franchise Your Business - Mark Siebert |
| vender_encaje_candidato_empresa | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| vender_final_entrevista | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| vender_fortuna_candidato | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| vender_libertad_candidato | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| vender_puesto_jugador | 1 | Who: The A Method for Hiring - Geoff Smart y Randy Street |
| vender_sin_stock_con_drop_shipping | 1 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) |
| venta_interna_cliente | 1 | SPIN Selling - Neil Rackham |
| venta_primer_franquiciado | 1 | Franchise Your Business - Mark Siebert |
| ventaja_competitiva_producto | 1 | Winning at New Products - Robert G. Cooper |
| ventajas_control_estadistico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| ventana_oportunidad_accidente | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| venture_debt_introduccion | 1 | Venture Deals - Brad Feld |
| venture_debt_terminos_economicos | 1 | Venture Deals - Brad Feld |
| verifica_que_el_si_es_real | 1 | Chris Voss, Rompe la barrera del no |
| verifica_quien_tiene_el_poder_de_decidir_o_vetar | 1 | Chris Voss, Rompe la barrera del no |
| verificacion_capitalizacion_credito | 1 | Franchise Your Business - Mark Siebert |
| verificacion_paralela_trabajo_critico | 1 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev |
| verificar_clientes_y_canales | 1 | The Startup Owner's Manual - Blank, Steve |
| verificar_modelo_ingresos | 1 | The Startup Owner's Manual - Blank, Steve |
| verificar_product_market_fit | 1 | The Startup Owner's Manual - Blank, Steve |
| vertical_vs_virtual_integracion | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| vesting_acciones_fundadores | 2 | Venture Deals - Brad Feld<br>The Founder's Dilemmas - Wasserman, Noam |
| vesting_dinamico | 1 | The Founder's Dilemmas - Wasserman, Noam |
| viaje_diagnostico_remedial | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| video_marketing_franquicia | 1 | Franchise Your Business - Mark Siebert |
| videoconferencia_reduccion_viajes | 1 | The Green to Gold Business Play - Daniel C. Esty |
| vieja_vision_vs_nueva_vision_seguridad | 1 | The Field Guide to Understandin - Dekker, Sidney |
| vinculacion_reporte_financiero | 1 | The Green to Gold Business Play - Daniel C. Esty |
| vincular_compensacion_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| violaciones_procedimentales_por_sobreespecificacion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| viral_loop_marketing | 3 | The Startup Owner's Manual - Blank, Steve<br>Never Lose a Customer Again - Joey Coleman<br>Traction - Gabriel Weinberg |
| virtualizacion_servidores | 1 | The Green to Gold Business Play - Daniel C. Esty |
| vision_alineacion_sostenibilidad | 1 | The Green to Gold Business Play - Daniel C. Esty |
| vision_estrategia_producto_pivote | 1 | The Lean Startup - Eric Ries |
| vision_periferica | 1 | Winning at New Products - Robert G. Cooper |
| visitas_soporte_campo | 1 | Franchise Your Business - Mark Siebert |
| visualizacion_datos_deteccion_outliers | 1 | Juran's Quality Handbook_ The C - Joseph A. Defeo |
| visualizar_recuperar_confianza | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| vivir_primero_valor_declarado | 1 | The Making of a Manager: What to Do When Everyone Looks to You - Julie Zhuo |
| vivir_valores_propios_evitar_listarlos | 1 | Radical Candor: Fully Revised and Updated Edition - Kim Scott |
| voc_temprano_en_agile_stage_gate | 1 | Winning at New Products - Robert G. Cooper |
| voces_externas_credibles | 1 | The Green to Gold Business Play - Daniel C. Esty |
| voice_of_customer_estrategico | 1 | Winning at New Products - Robert G. Cooper |
| voice_of_customer_homework | 1 | Winning at New Products - Robert G. Cooper |
| volverse_nativo_del_lugar | 1 | Cradle to Cradle - Michael Braungart |
| voz_del_cliente_voc | 1 | Winning at New Products - Robert G. Cooper |
| vpc_condiciones_productoras_violacion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| vuelve_a_medir_despues_del_susto | 1 | Edwards et al., Managing Project Risks |
| vulnerabilidad_instalacion | 1 | Managing the Risks of Organizat - Reason, J. T_ |
| wallas_etapa_incubacion | 1 | The Art of Thought - Wallas, Graham |
| wallas_etapa_preparacion | 1 | The Art of Thought - Wallas, Graham |
| wallas_etapa_verificacion | 1 | The Art of Thought - Wallas, Graham |
| wallas_intimacion_fringe_consciousness | 1 | The Art of Thought - Wallas, Graham |
| wallas_pensamiento_regulado | 1 | The Art of Thought - Wallas, Graham |
| war_room_pivot_proceed | 1 | The Startup Owner's Manual - Blank, Steve |
| warehouse_management_system | 1 | Essentials of Supply Chain Management - Michael H. Hugos |
| warrant_pricing_venture_debt | 1 | Venture Deals - Brad Feld |
| warrants_financiamiento | 1 | Venture Deals - Brad Feld |
| waterfall_vs_agile_development | 1 | The Startup Owner's Manual - Blank, Steve |
| ways_to_grow_framework | 1 | The field guide to human-centered design |
| ways_to_grow_matrix | 1 | Change by Design, Revised and U - Tim Brown |
| wbs_dictionary | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| welcome_call_cliente_veterano | 1 | Never Lose a Customer Again - Joey Coleman |
| what_if_questions | 1 | Business Model Generation - Osterwalder, Alexander |
| wizard_of_oz_testing | 1 | The Lean Startup - Eric Ries |
| work_breakdown_structure | 1 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder |
| worst_case_best_case_analysis | 1 | The Startup Owner's Manual - Blank, Steve |
| zanjar_seis_preguntas_decision_adelantado | 1 | High Output Management - Andrew S. Grove |
| zero_defects_concepto | 1 | Quality is free _ the art of making quality certain -- Philip B_ Crosby |

## Ids absorbidos sin fuente registrada

Referencias de la era de la extraccion y de las capas de alias (una arista a un id que nunca fue fichero de nodo, ni en dataset/ ni en el historial de git). No traen libro propio: su absorbedor ya lista el suyo.

M&A_negotiation, a_project_managers_book_of_forms:planificacion_formal, activity_cost_estimates, acuerdo_definitivo_de_adquisicion, acuerdo_equity_cofundadores, adaptacion_modelo_por_segmento, analisis_cash_flow_statement, analisis_de_riesgos_del_modelo, analisis_flujo_de_caja, analisis_industria, analisis_sensibilidad_financiera, asignacion_equity_cofundadores, balance_general_estructura, balance_sheet_basico, board_composition_investors, board_decision_exit, board_directores_formacion, brainstorm, brainstorming_estructurado, brainstorming_ideacion, brainstorming_ideacion_ideo, brainstorming_ideo, business_case_financiero, business_case_robusto, business_model_execution, business_model_generation:propuesta_valor, business_model_generation_lienzo, calculo_burn_rate, calculo_utilidad_neta, campana_crowdfunding, canvas_de_canales_bmg, captura_de_intimacion_e_ideas, ceo_guerra_vs_paz, channel_hypothesis, ciclo_retroalimentacion_autoajuste, cierre_de_ronda, cierre_de_ronda_financiamiento, cierre_ronda_financiamiento, cierre_transaccion_adquisicion, cinco_por_ques, clasificacion_garantia_full_limited_2, clasificacion_proyectos_por_riesgo, communications_management_plan, concept_testing, contratacion_abogado_especializado, contratar_por_fortaleza_no_ausencia_debilidad, contrato_firmado, control_de_calidad, control_de_costos, creacion_de_clientes, create_frameworks, cuatro_etapas_llamada_venta, cultura_disciplina_operativa, cultura_organizacional_inicial, culture_of_fixing, customer_acquisition_tactics, customer_relationship_hypotheses, customer_relationships_hypothesis, decision_reemplazo_fundador_ceo, definicion_de_brief, definicion_de_estrategia_de_innovacion, definicion_de_kpis_modelo_negocio, definicion_de_pov_ideo, definicion_del_problema_de_diseño, definicion_del_problema_ideo, definicion_estrategia_innovacion, definicion_hipotesis_negocio, definicion_hipotesis_valor, definicion_necesidad_capital, definicion_problema_change_by_design, definicion_problema_diseno, definicion_problema_diseno_centrado_humano, definicion_problema_inicial, definicion_problema_sistemico, definicion_problema_social, definicion_roles_equipo_fundador, definicion_vision_innovacion, definicion_vision_producto, definicion_vision_proyecto, definir_hipotesis_producto, definir_problema_de_diseño, desarrollo_experticia_era_ia, desarrollo_hipotesis_problema, descubrimiento_de_ideas, descubrimiento_de_necesidades_ideo, design_prototyping, design_thinking_como_mentalidad_organizacional, design_thinking_para_sistemas_complejos, design_thinking_tim_brown, deteccion_incidente_operativo, deteccion_necesidad_innovacion_disruptiva, dilema_cofundadores, dilema_relaciones_cofundadores, dilema_roles_cofundadores, diseno_etico_tecnologia, diseno_iterativo_sistemas, diseno_modelo_de_negocio_canvas, diseno_salvaguardas_failsafes, diseñar_prompts_efectivos_para_ia, diseño_centrado_en_sistemas, diseño_de_constraints_eticos, diseño_de_touchpoints, division_de_capital_fundadores, division_equidad_fundadores, ejecucion_de_ventas, ejecucion_escalamiento_circular, eleccion_cofundadores, empatia_con_el_usuario, empatia_con_usuario, empatia_en_diseño, empatia_field_guide_ideo, empatia_usuario, employee_pool_management, encaje_problema_solucion, encaje_producto_mercado, engaging_employees_transicion, entrevistas_de_descubrimiento_de_clientes, entrevistas_descubrimiento_cliente, equipo_fundador_inicial, equipo_fundador_roles, equity_financing_terminos, equity_split_fundadores, equity_splits_fundadores, escala_actitud_cierre_2, escalamiento_equipo, escalamiento_negocio, escalar_equipo_ventas, espacio_de_inspiracion, estados_financieros_basicos, estrategia_de_salida, estrategia_de_salida_exit, estrategia_financiamiento_temprano, estrategia_innovacion_empresa, estructura_de_capital_startup, estructura_de_equity_fundadores, estructura_ronda_financiamiento, estructura_societaria, etapa_investigacion_necesidades, evaluacion_balanceada_ejecutivos, evaluacion_modelos_negocio, evitar_terminos_engañosos_garantia, exit_strategy, expansion_del_sandbox, experiencia_postventa_diferenciadora, experimentos_de_validacion_de_problema, extreme_users_identification, fail_safes_diseno, fase_accomplish_2, fase_adopt_2, fase_advocate_customer_journey, fase_disenar_modelo_negocio, fase_implementar_modelo_negocio, field_guide_prototipos_con_usuarios, field_observations_ideo, field_research_empatia, field_test_modelo_negocio, field_trials, find_themes, formacion_equipo_dedicado, formacion_equipo_fundador, formulacion_hipotesis_negocio, formulacion_idea_negocio, formular_hipotesis_modelo_negocio, founder_role_after_succession, fuentes_alternativas_financiamiento_temprano, fuentes_de_financiamiento_deuda_vs_equity, fundamentos_estados_financieros, funding_strategy, gain_creators, gate_de_aprobacion_desarrollo, gate_governance_execution, gating_process_stage_gate, generacion_ideas_brainstorming, generacion_ideas_brainstormings, generacion_ideas_innovadoras, generacion_ideas_nuevo_producto, gestion_alucinaciones_ia_2, gestion_compromiso_stakeholders, gestion_de_board_de_directores, gestion_de_cartera_de_innovacion, gestion_de_relaciones_entre_cofundadores, gestion_del_cambio_organizacional, gestion_riesgos_proyecto, get_feedback, gobernanza_etica_proyecto, hipotesis_ingresos_precio, hitos_de_aprendizaje, hoja_datos_riesgo, hoja_de_ruta_de_implementacion, human_centered_design_ideo, ideacion_busqueda_oportunidades, ideacion_de_producto, ideacion_divergente_ideo, ideacion_necesidades_cliente, ideacion_problema_solucion, identificacion_cuello_de_botella_organizacional, identificacion_de_fallo_o_sintoma, iluminacion_creativa, implementacion_piloto_a_escala, inmersion_contextual, inmersion_inspiracion, innovation_show, insight_a_oportunidad, integracion_agresiva_ejecutivos, integrate_feedback_and_iterate, intervencion_proactiva_en_portafolio, interview, investigacion_contextual, investigacion_de_campo_observacional, investigacion_de_usuario_ideo, investigacion_de_usuarios_ideo, investigar_consecuencias_no_intencionadas, investor_dilemmas, ipo_preparacion, iteracion_diseno_producto, jagged_frontier_ia_2, jagged_frontier_ia_3, lectura_balance_sheet, lectura_cash_flow_statement, levantamiento_capital_serie_a, lista_actividades, los_9_bloques_de_construccion, mapa_de_mercado, mapa_ecosistema_business_model_generation, mapa_riesgos, mapeo_ecosistema_stakeholders, mapeo_recorrido_cliente, mapeo_tendencias, market_attractiveness_assessment, metodos_de_valoracion_empresarial, metricas_clave_modelo_negocio, metricas_de_negocio, metricas_pirata_aarrr, modelo_de_negocio_escalable, modelo_de_negocio_sistemico, modelo_ingresos_bmc, modelo_negocio_sostenible_social, modelo_spin_2, mvp, narrativa_disenio_ideo, necesidades_implicitas_vs_explicitas_2, negociacion_de_adquisicion, negociacion_term_sheets, negociacion_terminos_inversion, negociacion_terminos_valuacion, negociacion_termsheet, negociacion_termsheet_vc, net_present_value_npv, observacion_de_campo, observacion_etnografica_ideo, pain_relievers, patrones_modelo_negocio, pensamiento_sistemico, pitch_a_inversionistas, plan_contrataciones, plan_de_opciones_empleados, plan_gestion_cronograma, planificacion_de_salida, planificacion_preguntas_implicacion_2, plataforma_colaboracion_masiva_2, plataforma_experimentacion_organizacional, preframing_expectativas_2, preguntas_implicacion_2, preguntas_situacion_2, preparacion_del_problema, preparacion_para_ipo, preparacion_pitch_inversion, presupuesto_proyecto, priorizacion_objetivos_estrategicos, proceso_stage_gate_tradicional, procurement_management_plan, product_development_milestones, project_budget, prototipado_bajo_costo, prototipado_centrado_en_usuario, prototipado_emocional, prototipado_escenarios, prototipado_field_guide_ideo, prototipado_iterativo, prototipado_narrativo_ideo, prototipado_para_pensar, prototipo_etico, ratios_de_rentabilidad, rediseno_experiencia_usuario, reencuadre_problema, regla_disponibilidad_previa_venta_2, reglas_de_compromiso_gatekeepers, reintegracion_a_la_organizacion, relaciones_largo_plazo_con_inversionistas, reparto_equity_fundadores, resolucion_conflictos_equipo_fundador, retencion_de_talento, risk_management_plan, risk_register, ronda_de_financiamiento_serie_a, ronda_de_inversion, scaling_business_model, schedule_baseline, segmentacion_clientes, seleccion_banco_inversion_ma, serie_a_financiamiento, sprint_iterativo_de_desarrollo, stage3_development, stage_gate_flexible_criteria, stage_gate_ideacion, stage_gate_process, stage_gate_process_design, stage_gate_process_overview, stage_gate_scorecards, stage_gate_tradicional, strategic_roadmap, swot_por_bloque_de_construccion, t_shaped_people_equipos_interdisciplinarios, tarjeta_de_test, term_sheet_acciones_preferentes, terminos_hoja_de_terminos_deuda_convertible, testing_hypotheses, the_lean_startup:experimentacion_validada, the_lean_startup:vision_producto, tipos_de_startup, tipos_relaciones_previas_cofundadores, trade_off_responsividad_eficiencia_2, validacion_clientes_fase_get_ready_to_sell, validacion_producto_early_adopters, valoracion_pre_money, valuation_pre_money, value_proposition_design, value_proposition_hypothesis, value_proposition_statement, verificacion_de_ideas, vesting_de_equity, vision_producto_inicial, voice_of_customer_research
