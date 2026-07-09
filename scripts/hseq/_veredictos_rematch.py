#!/usr/bin/env python3
"""Herramienta temporal (checkpoint 4): aplica los veredictos de la
revision por significado sobre la banda 0.55-0.70 del re-match semantico.
Cada aprobacion se verifico leyendo el contenido del candidato (titulo +
resumen + pasos); los 'override' son casos donde el nodo correcto existia
pero no quedo en el top-3 del embedding (mismo fenomeno visto en dedup:
la señal superficial no basta en este corpus). Valida que todo destino
exista en su dominio antes de escribir."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import CATEGORIAS, cargar_dominio, dir_metadata, escribir_json

# fantasma -> destino aprobado (None = rechazado, poda definitiva)
VEREDICTOS = {
    "environmental": {
        "auditoria_energetica_edificio": "benchmark_auditoria_energetica",
        "auditorias_formales_proveedores": "auditorias_proveedores",
        "ciclos_biologicos_tecnicos": "metabolismo_tecnico",
        "medicion_impacto_ambiental": "metricas_impacto_ambiental",       # override fuera de top-3
        "medicion_impactos_ambientales": "metricas_impacto_ambiental",    # override fuera de top-3
        "medir_desechos_empresariales": "medir_residuos_empresa",         # override fuera de top-3
    },
    "health_safety": {
        "analisis_fallas_latentes": "fallas_activas_condiciones_latentes",
        "calidad_control_vs_aseguramiento": "quality_control_vs_quality_assurance",
        "competencia_como_responsabilidad_sistema": None,
        "construccion_causas_recomendaciones": "construccion_de_causas",  # override
        "cultura_justa_en_investigacion_de_accidentes": "cultura_justa",  # override
        "cultura_organizacional_cerrada": "dysfunctional_organizational_culture_patterns",
        "diseno_a_prueba_de_errores": None,
        "establecimiento_indicadores_desempeno_sst": "evaluacion_periodica_programa_seguridad",
        "herramientas_diagnostico_proactivo": "identificacion_evaluacion_peligros",
        "identificacion_pasos_propensos_error": "caracteristicas_tareas_propensas_omision",
        "identificacion_riesgos_caida": None,
        "identificacion_riesgos_respiratorios": "identificacion_peligros_salud",  # candidato 2 (top-1 era auto-ref)
        "informe_causas_raiz": "investigacion_incidentes_2",
        "investigacion_nueva_vision": "new_view_vs_old_view_de_error_humano",
        "modelo_de_persona_vs_organizacional": "modelo_accidente_organizacional",  # override
        "modelo_queso_suizo_reason": "modelo_barreras_swiss_cheese",
        "no_confiar_en_sistema_gestion_seguridad": None,
        "recoleccion_datos_incidente": "investigacion_incidentes",        # override
        "reconstruccion_de_mentalidad_practicante": "perspectiva_dentro_del_tunel",  # override
        "rediseno_de_procesos_de_mantenimiento": None,
        "sistema_informacion_seguridad": None,
        "sistema_reporte_incidentes": "reporte_casi_accidentes",          # override
    },
    "quality": {
        "ajuste_proceso": None,
        "alineacion_estrategica_empresarial": "metas_negocio_calidad",
        "analisis_causa_efecto_xs_ys": "diseno_experimentos_doe_mejora",
        "analisis_causa_raiz": "analisis_diagnostico_causa",              # candidato 2
        "analisis_causa_raiz_rcca": "analisis_diagnostico_causa",
        "analisis_estadistico_de_datos": "estadistica_basica_calidad",
        "analisis_modal_fallos_efectos": "fmea_analisis_de_modos_de_falla",
        "catorce_puntos_para_la_gestion": "los_14_puntos_deming",         # override
        "compromiso_alta_direccion": "aprobacion_alta_direccion",
        "compromiso_gerencial": "compromiso_gerencial_calidad",           # override
        "conceptos_basicos_estadistica_descriptiva": "estadistica_basica_calidad",  # override
        "consejo_de_calidad_ejecutivo": "consejo_ejecutivo_calidad",      # override
        "control_calidad_especificaciones": None,
        "control_de_calidad_ciclo_de_retroalimentacion": "ciclo_de_retroalimentacion_control",
        "control_de_calidad_por_retroalimentacion": "ciclo_de_retroalimentacion_control",  # override
        "cultura_calidad": "normas_culturales_calidad",
        "cultura_calidad_positiva": "normas_culturales_calidad",          # candidato 2
        "cultura_de_mejora_continua": "breakthrough_cultural",
        "definicion_valor_nominal": "funcion_perdida_taguchi",
        "desarrollo_caracteristicas_detalladas_producto": "desarrollo_caracteristicas_producto",  # override
        "desarrollo_continuo_del_personal": "formacion_seleccion_y_retencion_de_personal",  # candidato 2
        "desarrollo_del_producto": "desarrollar_caracteristicas_producto",  # override
        "difusion_de_mejores_practicas": "clonacion_replicacion_breakthrough",  # override
        "dmadv_fase_medicion": "dmadv_design_for_six_sigma",
        "dmaic_fase_control": "dmaic_six_sigma",                          # override (no existe nodo de fase Control)
        "educacion_estadistica_continua_personal": "educacion_estadistica_para_la_calidad",  # candidato 2
        "especificaciones_de_producto": "establecer_diseno_final_producto",
        "estado_de_control_estadistico": "sistema_estable_variacion",     # override
        "fundamentos_iso_9001": "iso_9000_sistema_gestion_calidad",       # candidato 2
        "fundamentos_variacion_estadistica": "concepto_variacion_estadistica",
        "gestion_causas_comunes_especiales": "causas_comunes_vs_especiales",
        "graficos_control_shewhart": "carta_de_control_shewhart",
        "identificacion_oportunidades_mejora": "proceso_nominacion_seleccion",  # override
        "identificacion_procesos_clave_servicio": None,
        "institucionalizar_control_estadistico": "control_estadistico_de_procesos",  # override
        "medicion_costo_de_calidad": "metodologia_medicion_copq",         # override
        "medicion_del_programa_de_calidad": "medicion_calidad_2",         # override
        "mejora_continua_kaizen": "kaizen_mejora_continua",
        "mejora_continua_organizacional": "mejora_continua_del_proceso",  # override
        "mejora_sistematica_six_sigma": "dmaic_six_sigma",
        "operacion_de_aceptacion_calidad": "muestreo_de_aceptacion",      # override
        "paso_cuatro_evaluacion_coq": "costo_de_calidad_2",               # override
        "planeacion_de_calidad_juran": "juran_quality_by_design",         # override
        "planificacion_calidad_juran": "juran_quality_by_design",         # override
        "planificacion_para_organizaciones_familiares": "planificacion_gobierno_organizaciones_familiares",
        "posicionamiento_en_el_mercado": "estudio_mercado_calidad",
        "prevencion_de_defectos": "programa_cero_defectos",               # candidato 2
        "quality_function_deployment": "qfd_matriz_calidad",
        "recoleccion_datos_calidad": "diseno_de_metodos_de_recoleccion_de_datos",  # override
        "recoleccion_datos_desempeno_operativo": "diseno_de_metodos_de_recoleccion_de_datos",
        "reduccion_variabilidad": None,
        "reduccion_variacion_procesos": None,
        "reduccion_y_control_de_errores_de_medicion": "errores_de_medicion",  # override
        "reglas_de_escalamiento_calidad": None,
        "relacion_proveedor_unico": "relacion_largo_plazo_proveedor_unico",  # override
        "seleccion_de_proveedores": "planificacion_cadena_suministro",
        "seleccion_socios_benchmarking": "tipos_benchmarking_por_participante",
        "seven_basic_tools_of_quality": "herramientas_analisis_causa_raiz",  # override
        "sistema_medicion_calidad": "medicion_calidad_2",                 # candidato 2
        "trabajo_con_proveedores": "equipo_conjunto_de_mejora_con_proveedores",
        "trabajo_conjunto_con_proveedor": "equipo_conjunto_de_mejora_con_proveedores",
        "voz_del_cliente": "descubrir_necesidades_cliente",               # override
    },
}

for cat, veredictos in VEREDICTOS.items():
    nodos = cargar_dominio(cat)
    ruta = dir_metadata(cat) / "aristas_resemantizadas.json"
    entradas = json.load(open(ruta, encoding="utf-8"))
    pendientes = {e["fantasma"] for e in entradas if e["banda"] == "revision"}
    faltan = pendientes - set(veredictos)
    sobran = set(veredictos) - pendientes
    assert not faltan, f"{cat}: sin veredicto para {faltan}"
    assert not sobran, f"{cat}: veredictos para fantasmas inexistentes {sobran}"
    aprobados = rechazados = 0
    for e in entradas:
        if e["banda"] != "revision":
            continue
        destino = veredictos[e["fantasma"]]
        if destino is None:
            e["veredicto"] = "rechazado_revision"
            rechazados += 1
            continue
        assert destino in nodos, f"{cat}: destino '{destino}' no existe en el dominio"
        if destino != e["destino"]:
            e["destino_original_top1"] = e["destino"]
            e["destino"] = destino
        e["veredicto"] = "aprobado_revision"
        aprobados += 1
    escribir_json(ruta, entradas)
    print(f"{cat}: {aprobados} aprobados en revision, {rechazados} rechazados (poda definitiva)")
