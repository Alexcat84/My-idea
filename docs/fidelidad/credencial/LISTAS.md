# Sesion con credencial: listas exactas de la campania de fidelidad

Sacadas del repositorio por script (campo `correcciones` de cada nodo vivo, cache de preguntas y registro de retiradas), no de memoria.

## 1. Nodos a re-embeber (Voyage): 44

El indice semantico embebe titulo, resumen_teorico y condiciones_activacion (`scripts/build_semantic_index_voyage.py`, `texto_nodo`). Los pasos y el entregable NO entran: una correccion de paso no cambia el vector. Van aqui los nodos con alguna correccion en esos campos. Fichero, uno por linea: `docs/fidelidad/credencial/nodos_a_reembeber.txt`.

El constructor no tiene modo parcial: vuelve a embeber todos los nodos vivos (unos 3.500, dentro de la cuota gratuita de Voyage). La lista sirve para comprobar despues que estos vectores si cambiaron.

- `acolchado_segun_forma` (fidelidad-t1-08)
- `analisis_trafico_competitivo` (fidelidad-t1-11)
- `bullseye_framework` (fidelidad-t8-018)
- `business_materiality_assessment` (fidelidad-t6-009)
- `calculo_de_aranceles_importacion` (fidelidad-t4-008)
- `cierre_segun_complejidad_venta` (fidelidad-t9-004)
- `co_sale_drag_along_agreements` (fidelidad-t4-028)
- `colocar_etiquetas_de_manejo_correctamente` (fidelidad-t3-26)
- `consejo_de_calidad_2` (fidelidad-t8-011)
- `coordinacion_organica_de_elementos_independientes` (fidelidad-t9-010)
- `creacion_option_pool` (fidelidad-t14-02)
- `critica_del_plan_con_ia` (fidelidad-t9-032)
- `cuan_probable_y_cuanto_doleria` (fidelidad-t5-038)
- `customer_retention_tactics` (fidelidad-t7-028)
- `decide_si_lo_compras_o_lo_haces_tu` (fidelidad-t5-053)
- `decisiones_reversibles_irreversibles` (fidelidad-t7-031)
- `desarrollo_en_espiral` (fidelidad-t7-010)
- `el_riesgo_eres_tu` (fidelidad-t9-075)
- `elegir_material_de_relleno_segun_producto` (fidelidad-t9-073)
- `elegir_sobre_o_caja_tamano` (fidelidad-t1-06)
- `empacar_liquidos_doble_barrera` (fidelidad-t9-063, fidelidad-t9-068)
- `entrega_por_partes_para_exponer_el_riesgo` (fidelidad-t11-06)
- `escenarios_de_evolucion_de_la_ia` (fidelidad-t9-007)
- `future_scenarios_planning` (fidelidad-t9-017, fidelidad-t9-019)
- `getting_started_system_communication_protection` (fidelidad-t5-045)
- `infection_control_plan` (fidelidad-t3-38)
- `inspeccion_lugar_trabajo_peligros` (fidelidad-t3-29, fidelidad-t3-31)
- `manejo_de_quimicos_peligrosos` (fidelidad-t3-40)
- `no_shop_agreement` (fidelidad-t4-013)
- `peligros_emergencias_no_rutinarias` (fidelidad-t3-33)
- `preguntas_situacion` (fidelidad-t9-028)
- `producto_como_servicio_de_acceso` (fidelidad-t8-031)
- `programas_cooperativos_osha` (fidelidad-t3-45)
- `punto_equilibrio_unidades` (fidelidad-t5-032, fidelidad-t5-035)
- `realizar_analisis_ciclo_de_vida_lca` (fidelidad-t7-002)
- `reglas_brainstorming` (fidelidad-t9-025)
- `sellar_cajas_metodo_cinta_en_h` (fidelidad-t1-04)
- `sistema_estable_causas_comunes` (fidelidad-t7-022)
- `sistemas_de_extincion_de_incendios` (fidelidad-t3-47)
- `tecnica_freaky_friday` (fidelidad-t8-006)
- `tecnicas_para_sacar_riesgos_a_la_luz` (fidelidad-t2-03, fidelidad-t2-04)
- `usa_silencio_no_partas_diferencia` (fidelidad-t5-011, fidelidad-t5-012)
- `vehiculos_autonomos_drones_supply_chain` (fidelidad-t8-033)
- `verifica_quien_tiene_el_poder_de_decidir_o_vetar` (fidelidad-t5-014)

## 2. Preguntas a regenerar: 23

Con `python engine/build_question_cache.py --patch-file docs/fidelidad/credencial/preguntas_a_regenerar.txt`.

### Obligatorias: las 23 retiradas de la cache

Retiradas el 24 sep por la decision del fundador 1 (commit de fidelidad-cache-1): su pregunta nacio de un resumen corregido por CONTRARIO o por cifra, plazo o norma. Detalle y motivo de cada una en `docs/fidelidad/PREGUNTAS_RETIRADAS.json`.

- `analisis_trafico_competitivo`
- `bullseye_framework`
- `calculo_de_aranceles_importacion`
- `cierre_segun_complejidad_venta`
- `colocar_etiquetas_de_manejo_correctamente`
- `consejo_de_calidad_2`
- `creacion_option_pool`
- `el_riesgo_eres_tu`
- `entrega_por_partes_para_exponer_el_riesgo`
- `future_scenarios_planning`
- `getting_started_system_communication_protection`
- `infection_control_plan`
- `inspeccion_lugar_trabajo_peligros`
- `manejo_de_quimicos_peligrosos`
- `no_shop_agreement`
- `peligros_emergencias_no_rutinarias`
- `preguntas_situacion`
- `programas_cooperativos_osha`
- `punto_equilibrio_unidades`
- `sistemas_de_extincion_de_incendios`
- `tecnica_freaky_friday`
- `tecnicas_para_sacar_riesgos_a_la_luz`
- `usa_silencio_no_partas_diferencia`

### Recomendadas: 0

Su resumen cambio dentro de los 400 caracteres que lee el generador, pero por una correccion de "Sugerencia de My Idea" (un anadido practico, no un dato): la pregunta no afirma nada falso y sigue en la cache. Regenerarla la alinea con el texto nuevo.

