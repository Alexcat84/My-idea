"""VUELTA 75, OP-E-01, TRAMO 1: escribe en dataset/nodos/<madre>.json las
aristas nuevas confirmadas por lectura par a par (vara 9.6.1/9.6.2/9.6.3 del
banco), leidas contra la bolsa recalibrada EN ESTA VUELTA
(docs/plan/PASO_NODO_CALIBRADO.jsonl, corrida fresca, no la del 11 ago 2026).

Solo anade el id del hijo a nodos_siguientes de la madre. La reciprocidad
(nodos_previos del hijo) la completa el paso 5 de scripts/run_phase1.py
(aristas_a_simetrizar), que se corre despues como parte del ciclo de Gate 0.

CADA PAR TIENE SU RAZON DE UNA LINEA, citada al lado, para que la lectura se
pueda auditar sin volver a abrir los nodos.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

# (madre, hijo, razon breve de la lectura)
PARES_SANOS = [
    ("verificar_clientes_y_canales", "dia_en_la_vida_del_cliente",
     "paso 2 nombra el ejercicio entero; el hijo trae las 5 acciones que lo hacen"),
    ("planificacion_estrategica_despliegue", "definir_mision_organizacional",
     "paso 1 es la linea; el hijo trae reunir, redactar, validar, comunicar"),
    ("six_sigma_dmaic", "replicar_resultados",
     "paso 12 es la linea final del DMAIC; el hijo trae evaluar, adaptar, documentar, nominar, reiniciar"),
    ("project_close_out", "project_charter",
     "paso 1 nombra el Acta de Constitucion; el hijo ES esa Acta con sus 6 pasos de construccion"),
    ("adaptar_empaque_segun_tipo_de_articulo", "proteger_fragiles_caja_dentro_de_caja",
     "paso 4 nombra el metodo caja dentro de caja; el hijo trae el procedimiento de 5 pasos"),
    ("contractor_status_report", "project_performance_report",
     "paso 5 nombra el Informe de Desempeno; el hijo ES ese informe con su procedimiento de 4 pasos"),
    ("segmentos_de_clientes_problema_necesidad", "get_out_of_the_building",
     "paso 1 es la consigna; el hijo trae el procedimiento de 4 pasos, incluida la prohibicion de delegar"),
    ("customer_creation", "determinar_tipo_de_mercado",
     "paso 1 es la linea; el hijo trae los 12 pasos del analisis de tipo de mercado y posicion competitiva"),
    ("cultura_justa_2", "justicia_restaurativa",
     "paso 4 nombra la dicotomia; el hijo trae los 4 pasos de la justicia restaurativa"),
    ("evitar_pseudociencia_producto", "metricas_accionables",
     "paso 1 es la linea; el hijo trae los 9 pasos de metricas accionables contra vanidad"),
    ("mobilizar_empleados_cultura_ecologica", "evaluacion_actitudes_empleados",
     "paso 3 es la linea; el hijo trae los 4 pasos de la evaluacion de actitudes"),
    ("pivot_post_ventas", "value_proposition_startup",
     "paso 4 pide evaluar el encaje de la propuesta de valor; el hijo ES el procedimiento de esa propuesta"),
    ("resumen_de_datos_graficos", "medidas_tendencia_dispersion",
     "paso 4 es la linea; el hijo trae los 5 pasos de calculo de tendencia y dispersion"),
    ("plan_cambio_climatico", "establecer_metas_reduccion_emisiones",
     "paso 2 es la linea; el hijo trae los 5 pasos para fijar la meta"),
    ("franquicia_unidad_individual", "proceso_venta_franquicias",
     "paso 1 es la linea; el hijo trae los 5 pasos del proceso de venta"),
    ("planificacion_inicial_calidad", "analisis_flujo_proceso",
     "paso 4 es la linea; el hijo trae los 4 pasos del analisis del diagrama de flujo"),
    ("marco_analisis_mercado_cadena_suministro", "ciclo_de_conversion_de_efectivo",
     "paso 17 es la linea; el hijo trae los 7 pasos del calculo del ciclo"),
    ("dmadv_fase_verificacion", "analisis_de_sistemas_de_medicion_msa",
     "paso 2 pide revisar los sistemas de medicion; el hijo ES el MSA con sus 6 pasos"),
    ("identificar_caracteristicas_metas_proceso", "diseno_de_procesos_por_caracteristicas",
     "paso 3 es la linea; el hijo trae los 5 pasos de la hoja de diseno de proceso"),
    ("desarrollo_de_controles_de_proceso", "decision_conformidad_producto",
     "paso 4 es la linea; el hijo trae los 4 pasos de la decision de conformidad"),
    ("recursos_apoyo_gubernamental_exportacion", "programas_ex_im_bank",
     "paso 3 nombra el Ex-Im Bank; el hijo trae los 6 pasos de sus programas de financiamiento"),
    ("definiciones_operacionales_de_calidad", "ctq_caracteristicas_criticas",
     "paso 1 es la linea; el hijo ES el procedimiento CTQ de 5 pasos"),
    ("funnel_get_customers_optimizacion", "disenar_tests_pass_fail",
     "paso 3 es la linea; el hijo trae los 5 pasos del diseno del test"),
    ("analisis_capacidad_proceso", "capacidad_del_proceso",
     "paso 3 es la linea; el hijo trae los 4 pasos del calculo de capacidad"),
    ("brecha_de_calidad_cuatro_gaps", "capacidad_del_proceso",
     "paso 3 es la linea (segunda madre del mismo hijo, dos padres legitimos); mismo hijo, misma razon"),
    ("adn_de_innovacion_organizacional", "espacios_fisicos_de_innovacion",
     "paso 3 es la linea; el hijo trae los 4 pasos del diseno de espacios"),
]

# Pares leidos y NO enlazados, con la razon del descarte (para el reporte,
# no escriben nada en el grafo).
PARES_DESCARTADOS = [
    ("medicion_servicios", "make_certain_programa",
     "MADRE QUE REPITE: coincide con programa_make_certain_3 sobre el mismo paso 3, mismo tema con dos escrituras. Gemelo posible, no arista aqui"),
    ("medicion_servicios", "programa_make_certain_3",
     "MADRE QUE REPITE: mismo caso que make_certain_programa, ver arriba"),
    ("mejora_calidad_crosby", "concepto_programa_catorce_pasos",
     "MADRE QUE REPITE: coincide con el racimo de MESA_RACIMOS grupo 1, 'Programa de catorce pasos de Crosby' (3 nodos declarados). No se enlaza sin resolver antes el racimo"),
    ("consejo_de_calidad_y_rol_del_director", "planificacion_estrategica_despliegue_2",
     "MADRE QUE REPITE: el sufijo _2 es la figura de MESA_RACIMOS grupo 4 (familia de ids); es gemelo de planificacion_estrategica_despliegue, no hijo nuevo"),
]


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def main():
    tocados = []
    ya_estaban = []
    for madre_id, hijo_id, razon in PARES_SANOS:
        data, path = cargar(madre_id)
        sig = data.get("nodos_siguientes") or []
        if hijo_id in sig:
            ya_estaban.append((madre_id, hijo_id))
            continue
        sig.append(hijo_id)
        data["nodos_siguientes"] = sig
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        tocados.append((madre_id, hijo_id))

    print(f"ARISTAS ESCRITAS: {len(tocados)}")
    for m, h in tocados:
        print(f"  {m} -> {h}")
    if ya_estaban:
        print(f"YA EXISTIAN (no tocadas, declarado): {len(ya_estaban)}")
        for m, h in ya_estaban:
            print(f"  {m} -> {h}")
    print(f"DESCARTADOS (madre que repite, sin arista): {len(PARES_DESCARTADOS)}")
    for m, h, r in PARES_DESCARTADOS:
        print(f"  {m} -> {h} | {r}")


if __name__ == "__main__":
    main()
