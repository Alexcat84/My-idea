# Sesion con credencial: listas exactas de la campania de fidelidad

Sacadas del repositorio por script (campo `correcciones` de cada nodo vivo, cache de preguntas y registro de retiradas), no de memoria.

**Primera sesion con credencial: HECHA el 24 sep 2026** (commit 58362389): 44 nodos re-embebidos con sus vectores comprobados y 23 preguntas regeneradas y de vuelta en la cache, tras las tandas fidelidad-t1 a fidelidad-t14. **Lo que sigue es lo PENDIENTE** para una segunda sesion, desde fidelidad-t15 (la pasada sobre los campos que llegan a la IA).

## 1. Nodos a re-embeber (Voyage): 52

El indice semantico embebe titulo, resumen_teorico y condiciones_activacion (`scripts/build_semantic_index_voyage.py`, `texto_nodo`). Los pasos y el entregable NO entran: una correccion de paso no cambia el vector. Van aqui los nodos con alguna correccion en esos campos. Fichero, uno por linea: `docs/fidelidad/credencial/nodos_a_reembeber.txt`.

El constructor no tiene modo parcial: vuelve a embeber todos los nodos vivos (unos 3.500, dentro de la cuota gratuita de Voyage). La lista sirve para comprobar despues que estos vectores si cambiaron.

- `actualizacion_hvac` (fidelidad-t15-56)
- `actualizacion_iluminacion` (fidelidad-t15-01, fidelidad-t15-57)
- `atributos_liderazgo_ceo` (fidelidad-t15-02)
- `breakup_fee_evaluation` (fidelidad-t15-03)
- `causas_comunes_vs_especiales` (fidelidad-t15-04)
- `clasificacion_tipos_activos` (fidelidad-t15-05)
- `comunicacion_interna_post_despido_ejecutivo` (fidelidad-t15-07)
- `condiciones_latentes_organizacionales` (fidelidad-t15-08)
- `consejo_de_calidad_3` (fidelidad-t15-09)
- `costo_de_mala_calidad_copq` (fidelidad-t15-10)
- `cronograma_proyecto` (fidelidad-t15-11)
- `customer_development_team` (fidelidad-t15-12)
- `customer_retention_tactics` (fidelidad-t15-60)
- `decidir_empacar_tu_mismo_o_subcontratar` (fidelidad-t15-61)
- `detectar_prioridad_cliente_entrega` (fidelidad-t15-14)
- `diseno_organizacional` (fidelidad-t15-16)
- `distorsion_muestreo_mecanico` (fidelidad-t15-17)
- `educacion_estadistica_para_la_calidad` (fidelidad-t15-18)
- `encontrar_lead_vc` (fidelidad-t15-20)
- `exenciones_legales_franquicia` (fidelidad-t15-21)
- `gestion_de_portafolio_arriesgado` (fidelidad-t15-65)
- `gestion_desempeno_feedback` (fidelidad-t15-66)
- `habito_energetico_vs_mecanico` (fidelidad-t15-23)
- `hr_como_control_de_calidad_gerencial` (fidelidad-t15-67)
- `incentivos_reconocimiento_sostenibilidad` (fidelidad-t15-24)
- `incoterms_reglas_comerciales_internacionales` (fidelidad-t15-25)
- `manejo_problemas` (fidelidad-t15-26)
- `matriz_riesgo_conocido_desconocido` (fidelidad-t15-27)
- `medicion_servicios` (fidelidad-t15-28)
- `modelo_tradicional_introduccion_producto` (fidelidad-t15-29)
- `motivated_management_franquiciado` (fidelidad-t15-30)
- `motor_crecimiento_viral` (fidelidad-t15-31)
- `nueve_pasos_iniciar_programa` (fidelidad-t15-32)
- `ofrecer_puntos_recogida` (fidelidad-t15-68)
- `personalizar_interacciones_cliente` (fidelidad-t15-34)
- `portfolio_management_triangulation` (fidelidad-t15-35)
- `programa_do_one_thing` (fidelidad-t15-70)
- `proteger_fragiles_caja_dentro_de_caja` (fidelidad-t15-38)
- `prototipado_virtual_mundos` (fidelidad-t15-39, fidelidad-t15-40)
- `recursos_apoyo_gubernamental_exportacion` (fidelidad-t15-41)
- `recursos_educativos_osha` (fidelidad-t15-42, fidelidad-t15-43)
- `relaciones_publicas_leads_franquicia` (fidelidad-t15-44)
- `restricciones_extremas_como_innovacion` (fidelidad-t15-45)
- `riesgo_del_negocio_o_del_proyecto` (fidelidad-t15-46)
- `scorecards_criterios_gate` (fidelidad-t15-47)
- `silla_vacia_del_cliente_en_decisiones` (fidelidad-t15-48)
- `sustitucion_quimica_sinergetica` (fidelidad-t15-49)
- `timing_equity_split` (fidelidad-t15-50)
- `transicion_energia_diversa_renovable` (fidelidad-t15-51)
- `video_marketing_franquicia` (fidelidad-t15-52)
- `videoconferencia_reduccion_viajes` (fidelidad-t15-53)
- `ways_to_grow_framework` (fidelidad-t15-54)

## 2. Preguntas a regenerar: 52

Con `python engine/build_question_cache.py --patch-file docs/fidelidad/credencial/preguntas_a_regenerar.txt`.

### Obligatorias: las 50 retiradas de la cache

Retiradas de la cache porque nacieron de texto corregido por CONTRARIO o por cifra, plazo o norma: el resumen del propio nodo (el generador lee sus 400 primeros caracteres) o las condiciones de un candidato (lee las 3 primeras de cada uno). Mientras tanto la app usa la pregunta generica adaptada en vivo. Detalle y motivo de cada una en `docs/fidelidad/PREGUNTAS_RETIRADAS.json`, que guarda tambien, como historia, las 23 ya regeneradas.

- `actualizacion_iluminacion`
- `benchmark_auditoria_energetica`
- `breakup_fee_evaluation`
- `causas_comunes_vs_especiales`
- `channels_hypothesis_physical`
- `clasificacion_tipos_activos`
- `comunicacion_interna_post_despido_ejecutivo`
- `condiciones_latentes_organizacionales`
- `consejo_de_calidad_3`
- `customer_development_team`
- `customer_retention_strategy`
- `customer_segments_hypothesis`
- `definicion_startup_busqueda_modelo_negocio`
- `deuda_de_gestion`
- `diamante_de_innovacion`
- `diseno_organizacional`
- `distorsion_muestreo_mecanico`
- `educacion_estadistica_para_la_calidad`
- `encontrar_lead_vc`
- `estrategia_de_innovacion_arenas`
- `estrategia_de_innovacion_producto`
- `exenciones_legales_franquicia`
- `incentivos_reconocimiento_sostenibilidad`
- `incoterms_reglas_comerciales_internacionales`
- `integracion_agresiva_ejecutivo`
- `manejo_problemas`
- `matriz_riesgo_conocido_desconocido`
- `medicion_servicios`
- `mejora_envolvente_edificio`
- `mix_medios_marketing_franquicia`
- `motivated_management_franquiciado`
- `motor_de_crecimiento`
- `personalizar_interacciones_cliente`
- `portfolio_management_triangulation`
- `producto_minimo_viable`
- `programa_do_one_thing`
- `proteger_fragiles_caja_dentro_de_caja`
- `prototipado_en_lo_salvaje`
- `prototipado_virtual_mundos`
- `recursos_apoyo_gubernamental_exportacion`
- `recursos_educativos_osha`
- `restricciones_extremas_como_innovacion`
- `revision_aplicabilidad_estandares_osha`
- `riesgo_del_negocio_o_del_proyecto`
- `scorecards_criterios_gate`
- `seeding_canal_viral`
- `timing_equity_split`
- `vesting_acciones_fundadores`
- `video_marketing_franquicia`
- `ways_to_grow_framework`

### Recomendadas: 2

Siguen en la cache y no afirman nada falso, pero nacieron de texto que luego cambio: o su resumen cambio por una Sugerencia de My Idea, o son puertas de un mundo que se retiraron y se restauraron porque la guarda AUD-09 H13 exige que toda puerta tenga su pregunta escrita. Regenerarlas las alinea con el texto nuevo.

- `detectar_prioridad_cliente_entrega` (restaurada, puerta de mundo (guarda H13), fidelidad-t15-14 desde el caracter 88)
- `disenar_empaque_logistica` (restaurada, puerta de mundo (guarda H13))
