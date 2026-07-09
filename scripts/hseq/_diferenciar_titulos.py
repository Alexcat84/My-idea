#!/usr/bin/env python3
"""Herramienta temporal (checkpoint 5): diferencia los 39 grupos de titulo
duplicado por LECTURA de contenido -- cada nodo gana el parentesis de su
angulo real (sector para los pares OSHA3885/3886 = industria general vs
construccion; enfasis de contenido para el resto). JAMAS fusiona: estos
son los rechazos correctos de la dedup (conceptos distintos con nombre
repetido) mas pares de solape de chunk que se marcan en el reporte final
como candidatos a fusion futura con datos de la caja de vidrio."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import CATEGORIAS, cargar_dominio, dir_metadata, escribir_json, guardar_nodo

NUEVOS_TITULOS = {
    "environmental": {
        "realizar_analisis_ciclo_de_vida_lca": "Análisis de Ciclo de Vida (LCA) — Metodología por Etapas",
        "realizar_analisis_ciclo_vida": "Análisis de Ciclo de Vida (LCA) — Pasos de Aplicación",
        "evitar_greenwashing": "Evitar el Greenwashing (Las Fallas Comunes de TerraChoice)",
        "evitar_greenwashing_2": "Evitar el Greenwashing (Riesgo de Credibilidad)",
    },
    "health_safety": {
        "comunicacion_coordinacion_multiempleador": "Comunicación y Coordinación Multiempleador (Industria General)",
        "comunicacion_coordinacion_multiempleador_2": "Comunicación y Coordinación Multiempleador (Construcción)",
        "coordinacion_multiempleador": "Coordinación Multiempleador (Agencias de Personal y Empleador Anfitrión)",
        "defensas_en_profundidad": "Defensas en Profundidad (Las Siete Funciones)",
        "defensas_en_profundidad_2": "Defensas en Profundidad (Capas de Barreras y Salvaguardas)",
        "ciclo_de_culpa": "El Ciclo de Culpa (Reacciones ante la Impotencia)",
        "ciclo_de_culpa_blame_cycle": "El Ciclo de Culpa (El Supuesto del Agente Libre)",
        "evaluacion_mejora_programa_2": "Evaluación y Mejora del Programa de Seguridad (Elemento del Programa)",
        "evaluacion_mejora_programa_3": "Evaluación y Mejora del Programa de Seguridad (Verificación Inicial y Anual)",
        "identificacion_peligros_salud": "Identificación de Peligros para la Salud (Industria General)",
        "identificacion_peligros_salud_2": "Identificación de Peligros para la Salud (Construcción)",
        "identificacion_evaluacion_peligros": "Identificación y Evaluación de Peligros (Industria General)",
        "identificacion_evaluacion_peligros_2": "Identificación y Evaluación de Peligros (Construcción)",
        "organizaciones_alta_confiabilidad_hro": "Organizaciones de Alta Confiabilidad (HRO) — Características Operativas",
        "sistemas_alta_confiabilidad_hro": "Organizaciones de Alta Confiabilidad (HRO) — Lectura Crítica de la Teoría",
        "lockout_tagout_procedures": "Procedimientos de Bloqueo y Etiquetado (Control de Energías Peligrosas)",
        "procedimientos_lockout_tagout": "Procedimientos de Bloqueo y Etiquetado (Procedimiento Escrito)",
        "elevated_surfaces_fall_protection": "Protección contra Caídas en Superficies Elevadas (Medidas y Sistemas)",
        "superficies_elevadas_proteccion_caidas": "Protección contra Caídas en Superficies Elevadas (Requisito desde 4 Pies)",
        "seguimiento_efectividad_controles": "Seguimiento de la Efectividad de los Controles (Industria General)",
        "seguimiento_efectividad_controles_2": "Seguimiento de la Efectividad de los Controles (Construcción)",
    },
    "quality": {
        "accion_correctiva_2": "Acción Correctiva (De la Detección a la Prevención)",
        "accion_correctiva_6": "Acción Correctiva (Destapar Causas — Rolling Over the Rocks)",
        "auditoria_de_producto": "Auditoría de Producto (Evaluación Independiente del Producto Terminado)",
        "auditoria_de_producto_2": "Auditoría de Producto (Reinspección para Verificar Decisiones)",
        "auditoria_producto": "Auditoría de Producto (Aptitud de Uso y Conformidad)",
        "auditoria_sistema_control_calidad": "Auditoría del Sistema de Control de Calidad (Por Qué se Deteriora)",
        "auditoria_sistema_control_calidad_2": "Auditoría del Sistema de Control de Calidad (Verificación Periódica)",
        "conformance_to_requirements": "Calidad como Conformidad con los Requisitos (Rechazo de Definiciones Subjetivas)",
        "definicion_calidad_conformidad": "Calidad como Conformidad con los Requisitos (La Primera Suposición Errónea)",
        "definicion_calidad_conformidad_requisitos": "Calidad como Conformidad con los Requisitos (El Ejemplo del Cadillac)",
        "clasificacion_de_seriedad_de_defectos_2": "Clasificación de Seriedad de Defectos (Guía para el Proveedor)",
        "clasificacion_seriedad_defectos": "Clasificación de Seriedad de Defectos (Características y Defectos por Gravedad)",
        "conciencia_de_calidad_2": "Conciencia de Calidad (Elevar la Preocupación Personal)",
        "quality_awareness_crosby": "Conciencia de Calidad (Comunicación por Participación)",
        "consejo_de_calidad": "Consejo de Calidad (Liderazgo y Selección de Proyectos — Juran)",
        "consejo_de_calidad_2": "Consejo de Calidad (Red Autogestionada de Profesionales — Crosby)",
        "control_estadistico_de_metodo_de_prueba": "Control Estadístico del Método de Prueba (Instrumento y Operador)",
        "control_estadistico_metodo_medicion": "Control Estadístico del Método de Medición (Condición de Validez)",
        "concepto_costo_de_calidad": "Costo de la Calidad (El Gasto de Hacer las Cosas Mal)",
        "costo_de_calidad": "Costo de la Calidad (Marco de Análisis Financiero)",
        "costo_de_mala_calidad_copq": "Costo de la Mala Calidad — COPQ (Costos que Desaparecerían sin Fallos)",
        "costo_de_mala_calidad_copq_2": "Costo de la Mala Calidad — COPQ (Cómo se Mide)",
        "costo_de_mala_calidad_copq_3": "Costo de la Mala Calidad — COPQ (Incumplimiento de Requisitos)",
        "costo_de_mala_calidad": "Costo de la Mala Calidad (Efecto Directo sobre los Costos)",
        "costo_de_mala_calidad_2": "Costo de la Mala Calidad (Si Productos y Procesos Fueran Perfectos)",
        "costo_de_mala_calidad_copq_4": "Costo de la Mala Calidad (En Promedio 15% de los Ingresos)",
        "circulos_calidad_qc": "Círculos de Calidad (La Gerencia Debe Actuar)",
        "circulos_de_calidad_qc_circles": "Círculos de Calidad (Origen con Ishikawa)",
        "definiciones_operacionales_2": "Definiciones Operacionales (Método, Prueba y Criterio)",
        "definiciones_operacionales_3": "Definiciones Operacionales (Traducir Conceptos Abstractos)",
        "definiciones_operacionales_4": "Definiciones Operacionales (Significado Comunicable)",
        "dia_cero_defectos": "Día de Cero Defectos (El Estándar se Fija en Un Solo Día)",
        "dia_cero_defectos_3": "Día de Cero Defectos (Evento Simbólico ZD)",
        "consumidor_como_eje_de_produccion": "El Consumidor en la Línea de Producción (Investigación del Consumidor)",
        "consumidor_parte_linea_produccion": "El Consumidor en la Línea de Producción (Extensión de la Línea)",
        "costo_de_calidad_5": "El Costo de la Calidad (Prevención, Evaluación y Fallas)",
        "costo_de_calidad_crosby": "El Costo de la Calidad (Por Qué la Calidad es Gratis)",
        "entrenamiento_supervisores": "Entrenamiento de Supervisores (Orientación Previa al Programa)",
        "entrenamiento_supervisores_calidad": "Entrenamiento de Supervisores (El Supervisor como Clave)",
        "falta_de_constancia_de_proposito": "Falta de Constancia de Propósito (La Enfermedad Más Incapacitante)",
        "falta_de_constancia_de_proposito_2": "Falta de Constancia de Propósito (Ausencia de Plan a Largo Plazo)",
        "enfermedades_mortales_gestion": "Las Enfermedades Mortales de la Gestión (Panorama de las Siete)",
        "las_siete_enfermedades_mortales": "Las Enfermedades Mortales de la Gestión (Bloqueo de los 14 Puntos)",
        "mapeo_flujo_valor": "Mapeo de Flujo de Valor (De la Concepción a la Comercialización)",
        "mapeo_flujo_valor_2": "Mapeo de Flujo de Valor (Valor Agregado y No Agregado)",
        "normalizacion_datos_benchmarking": "Normalización de Datos en Benchmarking (Comparación Justa)",
        "normalizacion_datos_benchmarking_2": "Normalización de Datos en Benchmarking (Conversión a Forma Comparable)",
        "perfeccionismo_vs_valor": "Perfeccionismo como Desperdicio de Valor (Cuándo la Perfección Sí Vale)",
        "perfeccionismo_vs_valor_2": "Perfeccionismo como Desperdicio de Valor (Contextos Críticos vs Desperdicio)",
        "principios_auditoria_calidad": "Principios del Programa de Auditoría de Calidad (Los Cinco Principios)",
        "principios_del_programa_de_auditoria_de_calidad": "Principios del Programa de Auditoría de Calidad (Hechos y Actitud de Servicio)",
        "quality_management_maturity_grid": "Quality Management Maturity Grid (Evaluación sin Ser Experto)",
        "quality_management_maturity_grid_2": "Quality Management Maturity Grid (Las Cinco Etapas de Madurez)",
        "rol_black_belt": "Rol del Black Belt en Six Sigma (Especialista en Breakthrough)",
        "rol_black_belt_six_sigma": "Rol del Black Belt en Six Sigma (Experto de Implementación en Sitio)",
        "validacion_sistema_medicion": "Validación del Sistema de Medición (Antes de Confiar en los Datos)",
        "validacion_sistema_medicion_2": "Validación del Sistema de Medición (Bajo Six Sigma)",
        "value_stream_mapping": "Value Stream Mapping (Métricas del Proceso)",
        "value_stream_mapping_2": "Value Stream Mapping (Distinguir Valor de Desperdicio)",
    },
}

for cat, mapa in NUEVOS_TITULOS.items():
    nodos = cargar_dominio(cat)
    log = {}
    for nid, nuevo in mapa.items():
        assert nid in nodos, f"{cat}: {nid} no existe"
        viejo = nodos[nid].get("titulo_concepto", "")
        nodos[nid]["titulo_concepto"] = nuevo
        guardar_nodo(cat, nid, nodos[nid])
        log[nid] = {"antes": viejo, "despues": nuevo}
    # validar unicidad total post-cambio
    titulos = {}
    for nid, d in nodos.items():
        t = (d.get("titulo_concepto") or "").strip().lower()
        titulos.setdefault(t, []).append(nid)
    dups = {t: v for t, v in titulos.items() if len(v) > 1 and t}
    assert not dups, f"{cat}: siguen duplicados {dups}"
    escribir_json(dir_metadata(cat) / "titulos_diferenciados.json", log)
    print(f"{cat}: {len(mapa)} titulos diferenciados | 0 duplicados restantes")
