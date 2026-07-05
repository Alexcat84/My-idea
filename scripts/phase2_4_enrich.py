# -*- coding: utf-8 -*-
"""
phase2_4_enrich.py - Enriquecimiento de estrangulamientos topologicos (Fase 2.4)

Identifica nodos a <=3 saltos de las 20 puertas de entrada (entry_seeds.json)
con 0 sucesores (callejones sin salida) o con exactamente 1 sucesor de mal
ajuste tematico, y les agrega 2-3 nodos_siguientes nuevos, coherentes,
elegidos semanticamente (misma fase o posterior, tematica afin) a partir de
titulo + resumen_teorico + condiciones_activacion.

Este script SOLO toca topologia (nodos_siguientes / nodos_previos). Esta
PROHIBIDO modificar resumen_teorico, pasos_accionables, entregable_esperado
u otro contenido teorico de cualquier nodo.

La lista ENRIQUECIMIENTOS de abajo es el resultado de ese analisis semantico
(ver phase1_run_log.json tras correr este script para el registro completo
de aristas agregadas). Los callejones sin salida (34) se identificaron via
BFS estricto; los nodos de 1 sucesor se revisaron a mano y solo se
enriquecieron los de peor ajuste tematico confirmado (no todos los 289 que
tecnicamente tienen un solo sucesor - la mayoria de esos ya apunta a un
sucesor razonable).

Uso: python scripts/phase2_4_enrich.py
Luego: python scripts/run_phase1.py   (debe quedar en verde)
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAPH_DIR = BASE / "dataset" / "nodos"
MASTER_GRAPH_PATH = BASE / "dataset" / "metadata" / "master_graph.json"
LOG_PATH = BASE / "dataset" / "metadata" / "phase2_4_enrich_log.json"

# node_id -> nuevos nodos_siguientes a agregar (ademas de los que ya tenga).
# Elegidos a mano por afinidad tematica + fase igual o posterior, a partir
# de titulo_concepto + resumen_teorico + condiciones_activacion.
ENRIQUECIMIENTOS = {
    # --- 34 callejones sin salida (0 sucesores) confirmados por BFS ---
    "analisis_trafico_competitivo": ["capturar_conocimiento_de_mercado", "herramientas_de_activacion_web", "metricas_de_adquisicion_activacion"],
    "audacia_del_cero": ["nueve_pecados_capitales_lanzamiento", "producto_como_experimento", "data_integrity_forecasting"],
    "automatizacion_software_gestion_innovacion": ["asignacion_recursos_en_gates", "gestion_visual_del_pipeline_de_desarrollo", "gates_go_kill_decision_points"],
    "company_building": ["plan_de_lanzamiento_al_mercado", "equipo_multifuncional", "preservar_caja_hasta_validar"],
    "consecuencias_no_intencionadas_sistemicas": ["planificacion_consecuencias_no_intencionadas", "disenar_para_sanacion", "aceptar_la_imperfeccion_del_diseno"],
    "contabilidad_innovacion_largo_plazo": ["mantener_puntaje_innovacion", "reconocimiento_de_ingresos", "depreciacion_y_amortizacion"],
    "customer_discovery_phase2_problem_test": ["problem_solution_fit", "actualizar_business_model_canvas_discovery", "product_market_fit"],
    "customer_validation_sales_roadmap": ["sintesis_hipotesis_modelo_negocio", "vision_estrategia_producto_pivote", "tipos_de_pivote"],
    "definicion_sprint_terminado_fisico": ["definicion_sprint_terminado", "spiral_development", "espiral_mortal_lotes_grandes"],
    "diseno_ciclo_completo_equipo": ["diseno_para_el_ciclo_completo", "equipo_dedicado_continuo", "equipo_multifuncional"],
    "diseno_como_plataforma_expansiva": ["diseno_activismo_social", "how_might_we_briefs", "sistema_gates_go_kill"],
    "diseno_de_desafios_de_innovacion": ["desafios_de_diseno_competitivos", "how_might_we_framing", "transformacion_organizacional_diseno"],
    "diseno_etico_de_privacidad": ["diseno_intencional_etica", "disenar_para_sanacion", "aceptar_la_imperfeccion_del_diseno"],
    "diseno_intencional_etica": ["integracion_deseabilidad_viabilidad_factibilidad_social", "transformacion_organizacional_diseno", "diseno_etico_de_privacidad"],
    "ejecucion_de_touchpoints": ["pull_no_push", "overlapping_stages_concurrent_execution", "spiral_development"],
    "emprendedor_como_puesto_de_trabajo": ["paradoja_exito_emprendedor", "background_startup_vs_corporativo", "navegacion_politica_organizacional"],
    "esfuerzo_y_energia_intelectual": ["encontrar_el_golpe_mental", "proposito_como_motor_energia", "habito_energetico_vs_mecanico"],
    "formacion_de_habitos_de_trabajo_creativo": ["second_wind_energia_mental", "gestion_de_habitos_mentales_para_pensar", "ruptura_de_habitos_para_estimulo"],
    "gestion_de_habitos_mentales_para_pensar": ["equilibrio_habito_estimulo", "formacion_de_habitos_de_pensamiento", "gestion_de_pensamientos_marginales"],
    "gestion_intraemprendedora_experimentacion": ["sandbox_de_innovacion", "reduccion_tamano_de_lote_batch_size", "cultura_de_optimismo"],
    "introduccion_validacion_clientes": ["filosofia_validacion_clientes", "customer_validation_sell_phase", "realizar_pruebas_pasa_no_pasa"],
    "mapeo_de_patrones": ["pensamiento_espacial_mapeo", "pensamiento_serial_vs_espacial", "pensamiento_visual"],
    "mastery_sensibilidades_diseno": ["diseno_de_sistemas_a_escala", "identificacion_talento_design_thinking", "transformacion_organizacional_diseno"],
    "motor_crecimiento_pegajoso": ["motor_crecimiento_pago", "hipotesis_valor_crecimiento", "afinar_motor_crecimiento"],
    "multi_sided_platforms": ["multi_sided_platform_pattern", "customer_scenarios_business_model", "priorizar_elementos_a_validar"],
    "plan_mejora_procesos": ["schedule_management_plan", "estrategia_innovacion_producto", "analisis_flujo_de_valor"],
    "portafolio_formal_management": ["gestion_portafolio_formal", "sistema_gates_go_kill", "governance_integration_gates_portfolio_roadmap"],
    "revision_portafolio_periodica": ["gates_go_kill_decision_points", "red_flags_proyectos_en_problemas", "post_launch_review"],
    "sprint_board_burn_down": ["gestion_visual_del_pipeline_de_desarrollo", "kanban_validacion_aprendizaje", "reduccion_tamano_de_lote_batch_size"],
    "storytelling_para_el_cambio": ["storytelling_como_herramienta_de_diseno", "navegacion_politica_organizacional", "propagacion_de_ideas_meme"],
    "superacion_accidia_creativa": ["wallas_etapa_iluminacion", "encontrar_el_golpe_mental", "cuatro_etapas_del_pensamiento_creativo"],
    "tres_as_de_metricas": ["metricas_accionables", "evitar_pseudociencia_producto", "vanity_metrics_vs_accionables"],
    "value_stream_analysis_lean": ["analisis_flujo_de_valor", "pull_no_push", "valor_vs_desperdicio"],
    "wallas_etapa_verificacion": ["intimacion_emocional_como_senal_de_verdad", "principio_enough_is_enough", "realizar_pruebas_pasa_no_pasa"],

    # --- chokepoints de 1 sucesor con peor ajuste (revision manual, no exhaustiva) ---
    # Empiricamente encontrado: unico sucesor real (ways_to_grow_matrix, gestion
    # de portafolio) no atendia ninguna senal de validacion con clientes; el
    # interprete alucino un id al no tener opciones reales (Fase 2.3, prueba del sonar).
    "desirability_feasibility_viability": ["construir_mvp_baja_fidelidad", "voz_del_cliente_voc"],
    # unico sucesor (patron_free_business_model) no tiene relacion tematica con
    # "medir lo que importa": agregamos las metricas accionables reales.
    "medir_lo_que_importa_no_solo_lo_facil": ["metricas_accionables", "vanity_metrics_vs_accionables"],
    # unico sucesor (term_sheet_overview) retrocede a una vision general del
    # term sheet ya cerrado; agregamos los pasos reales posteriores al cierre.
    "cierre_term_sheet": ["preparacion_due_diligence", "company_building"],
    # unico sucesor (contabilidad_innovacion) no continua el hilo de "obstaculos
    # al construir el MVP"; agregamos las pruebas que resuelven esos obstaculos.
    "riesgos_lanzamiento_mvp": ["prueba_mvp_alta_fidelidad", "wizard_of_oz_testing"],

    # --- ronda 2: callejones preexistentes que la ronda 1 dejo a <=3 saltos ---
    # (0 sucesores desde antes, pero fuera de la zona caliente original; los
    # nuevos enlaces de arriba los acercaron a las puertas de entrada)
    "second_wind_energia_mental": ["habito_energetico_vs_mecanico", "encontrar_el_golpe_mental", "formacion_de_habitos_de_pensamiento"],
    "transformacion_organizacional_diseno": ["identificacion_talento_design_thinking", "diseno_de_sistemas_a_escala", "navegacion_politica_organizacional"],
    "escalamiento_prematuro": ["eleccion_ritmo_crecimiento", "riesgo_no_pivotar_a_tiempo", "red_flags_proyectos_en_problemas"],
}


def cargar_nodo(nid):
    path = GRAPH_DIR / f"{nid}.json"
    return json.load(open(path, encoding="utf-8")), path


def main():
    master = json.load(open(MASTER_GRAPH_PATH, encoding="utf-8"))["nodos"]
    log = []
    saltados = []

    for origen, nuevos in ENRIQUECIMIENTOS.items():
        if origen not in master:
            saltados.append((origen, "origen no existe"))
            continue
        origen_data, origen_path = cargar_nodo(origen)
        siguientes = origen_data.setdefault("nodos_siguientes", [])
        for destino in nuevos:
            if destino not in master:
                saltados.append((f"{origen}->{destino}", "destino no existe"))
                continue
            if destino == origen or destino in siguientes:
                continue
            siguientes.append(destino)
            log.append({"origen": origen, "destino": destino})

            destino_data, destino_path = cargar_nodo(destino)
            previos = destino_data.setdefault("nodos_previos", [])
            if origen not in previos:
                previos.append(origen)
            destino_path.write_text(json.dumps(destino_data, ensure_ascii=False, indent=2), encoding="utf-8")

        origen_path.write_text(json.dumps(origen_data, ensure_ascii=False, indent=2), encoding="utf-8")

    LOG_PATH.write_text(json.dumps({"aristas_agregadas": log, "saltados": saltados}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Aristas agregadas: {len(log)}")
    if saltados:
        print(f"Saltados: {len(saltados)}")
        for s in saltados:
            print(" ", s)
    print(f"Log: {LOG_PATH}")
    print("\nAhora corre: python scripts/run_phase1.py")


if __name__ == "__main__":
    main()
