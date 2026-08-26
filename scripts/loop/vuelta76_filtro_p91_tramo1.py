"""VUELTA 76, TAREA 2.1.b: filtro de elegibilidad P.9.1 sobre las 25 aristas
del tramo 1 que sobreviven a la reversion de 1.3.a. Corrida propia, no copia
del acta: cruza madre e hijo de cada par contra el campo `eliminar` de las
71 operaciones de OPERACIONES.jsonl (las 71 estan en estado LISTA, ninguna
ejecutada: ese es el universo completo de "operaciones NO EJECUTADAS" hoy).
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
OPERACIONES = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

PARES = [
    ("adaptar_empaque_segun_tipo_de_articulo", "proteger_fragiles_caja_dentro_de_caja"),
    ("adn_de_innovacion_organizacional", "espacios_fisicos_de_innovacion"),
    ("analisis_capacidad_proceso", "capacidad_del_proceso"),
    ("brecha_de_calidad_cuatro_gaps", "capacidad_del_proceso"),
    ("contractor_status_report", "project_performance_report"),
    ("cultura_justa_2", "justicia_restaurativa"),
    ("customer_creation", "determinar_tipo_de_mercado"),
    ("definiciones_operacionales_de_calidad", "ctq_caracteristicas_criticas"),
    ("desarrollo_de_controles_de_proceso", "decision_conformidad_producto"),
    ("dmadv_fase_verificacion", "analisis_de_sistemas_de_medicion_msa"),
    ("evitar_pseudociencia_producto", "metricas_accionables"),
    ("franquicia_unidad_individual", "proceso_venta_franquicias"),
    ("funnel_get_customers_optimizacion", "disenar_tests_pass_fail"),
    ("identificar_caracteristicas_metas_proceso", "diseno_de_procesos_por_caracteristicas"),
    ("marco_analisis_mercado_cadena_suministro", "ciclo_de_conversion_de_efectivo"),
    ("mobilizar_empleados_cultura_ecologica", "evaluacion_actitudes_empleados"),
    ("pivot_post_ventas", "value_proposition_startup"),
    ("plan_cambio_climatico", "establecer_metas_reduccion_emisiones"),
    ("planificacion_estrategica_despliegue", "definir_mision_organizacional"),
    ("planificacion_inicial_calidad", "analisis_flujo_proceso"),
    ("project_close_out", "project_charter"),
    ("recursos_apoyo_gubernamental_exportacion", "programas_ex_im_bank"),
    ("resumen_de_datos_graficos", "medidas_tendencia_dispersion"),
    ("six_sigma_dmaic", "replicar_resultados"),
    ("verificar_clientes_y_canales", "dia_en_la_vida_del_cliente"),
]


def main():
    ops = [json.loads(l) for l in OPERACIONES.read_text(encoding="utf-8").splitlines() if l.strip()]
    no_ejecutadas = [op for op in ops if op["estado"] != "HECHA"]
    print(f"Operaciones NO EJECUTADAS (estado != HECHA): {len(no_ejecutadas)} de {len(ops)}")

    condenado_por = {}
    for op in no_ejecutadas:
        for nid in op.get("eliminar") or []:
            condenado_por.setdefault(nid, []).append(op["id_op"])

    rojas = []
    for madre_id, hijo_id in PARES:
        motivos = []
        if madre_id in condenado_por:
            motivos.append(f"madre {madre_id} condenada por {condenado_por[madre_id]}")
        if hijo_id in condenado_por:
            motivos.append(f"hijo {hijo_id} condenado por {condenado_por[hijo_id]}")
        estado = "ROJA" if motivos else "limpio"
        if motivos:
            rojas.append((madre_id, hijo_id, motivos))
        print(f"{madre_id} -> {hijo_id}: {estado} {'; '.join(motivos)}")

    print()
    print(f"TOTAL ROJAS: {len(rojas)} de {len(PARES)}")


if __name__ == "__main__":
    main()
