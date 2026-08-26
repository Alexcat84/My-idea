"""VUELTA 76, OP-E-01, TRAMO 2: escribe en dataset/nodos/<madre>.json las
aristas nuevas confirmadas por lectura par a par (vara 9.6.1 Y 9.6.2, las dos
obligatorias en esta operacion desde esta vuelta), leidas contra la cabeza de
la bolsa recalibrada FRESCA en esta vuelta y ya filtrada por P.9.1
(docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V76.jsonl).

Los primeros 30 candidatos de esa bolsa filtrada se leyeron enteros (textos
completos de madre e hijo). CUATRO se descartan, dos porque repiten
descartes ya adjudicados en el tramo 1 (medicion_servicios, el par D1;
consejo_de_calidad_y_rol_del_director, el D3 con su razon ya corregida en
1.3.d) y dos nuevos de esta vuelta, los dos por sufijo numerico vivo en un
racimo de MESA_RACIMOS grupo 1 sin operacion que lo nombre (misma figura que
D3): capacidad_de_proceso_2 y eliminacion_causas_error_4. El D2
(mejora_calidad_crosby -> concepto_programa_catorce_pasos) se escribe: fue
adjudicado A FAVOR del auditor en la relectura conjunta de la TAREA 2.4,
verificado por cuenta propia que ninguna operacion nombra a los tres
miembros de su racimo y que el hijo no lleva sufijo numerico.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

# (madre, hijo, razon breve de la lectura, incluye 9.6.1 y 9.6.2)
PARES_SANOS = [
    ("customer_validation", "prueba_mvp_alta_fidelidad",
     "paso 1 es la linea (despliega version alta fidelidad para probar con clientes); el hijo trae el procedimiento de 5 pasos de la prueba. 9.6.1: madre liga 5 de 5 pasos (mayoria confirma)"),
    ("rol_alta_direccion_calidad", "alineacion_estrategica_despliegue",
     "paso 2 es la linea (definir estrategias y metas alineadas); el hijo trae el procedimiento de 5 pasos de alineacion. 9.6.1: madre liga 2 de 6 pasos (mitad o menos, manda 9.6.2)"),
    ("cap_table_basico", "valuacion_pre_post_money",
     "paso 2 es la linea (define pre-money y post-money); el hijo trae el procedimiento de 3 pasos para clarificar y calcular. 9.6.1: madre liga 6 de 7 pasos (mayoria confirma)"),
    ("criterios_de_exito_gate", "post_launch_review",
     "paso 4 es la linea (compara resultados en la revision post lanzamiento); el hijo ES esa revision con procedimiento de 5 pasos. 9.6.1: madre liga CERO de 4 (caso extremo del mitad-o-menos, manda contenido)"),
    ("causas_especiales_y_comunes_variacion", "six_sigma_dmaic",
     "paso 3 nombra DMAIC como ejemplo; el hijo ES el modelo DMAIC entero con 12 pasos. 9.6.1: madre liga 1 de 4 (mitad o menos, manda contenido, y el contenido es clarisimo)"),
    ("analisis_capacidad_proceso", "capacidad_de_proceso_2",
     "paso 2 es la linea (verificar control estadistico via cartas de control); el hijo trae monitoreo de ~3 meses y la intervencion sobre el sistema (no el individuo), contenido que NO esta en capacidad_del_proceso (ya enlazado en tramo 1, que es calculo con formulas y comunicacion a diseno). 9.6.3: el solape no decide, lo que queda fuera es distinto en cada uno. 9.6.1: madre liga 3 de 5 pasos (mayoria confirma, contando ya el enlace de tramo 1). DISCUTIBLE por similitud de titulo con capacidad_del_proceso (Gate 0 la marca 97,6% de similitud), marcado para relectura ciega"),
    ("customer_insights_design", "value_proposition_startup",
     "paso 4 es la linea (cuestionar si la propuesta de valor resuelve un problema real); el hijo trae el procedimiento de 3 pasos para construir la propuesta. 9.6.1: madre liga 4 de 4 (mayoria trivial, pero el contenido decide de verdad por 9.6.2)"),
    ("testing_process_completo", "value_proposition_canvas",
     "paso 1 nombra el Value Proposition Canvas explicitamente; el hijo ES ese canvas con procedimiento de 6 pasos. 9.6.1: madre liga 6 de 5 pasos (mayoria confirma, hay mas ligados que pasos por fan out)"),
    ("lean_manufacturing_tps", "poka_yoke_a_prueba_de_errores",
     "paso 4 nombra poka-yoke explicitamente; el hijo ES ese procedimiento de 4 pasos. Racimo MESA_RACIMOS grupo 2 (Poka yoke, DECISION 2 aprobada) sin ninguna operacion que lo nombre, verificado, y sin sufijo numerico: no hay fusion pendiente que este enlace tenga que esperar. 9.6.1: madre liga 2 de 6 (mitad o menos, manda contenido)"),
    ("lente_sostenibilidad_finanzas", "eco_eficiencia",
     "paso 2 es la linea (evaluar ahorro en eficiencia energetica); el hijo trae el procedimiento de 6 pasos. 9.6.1: madre liga 2 de 4 (mitad, manda contenido)"),
    ("planificacion_de_la_inspeccion", "clasificacion_caracteristicas_calidad",
     "pasos 4 y 5 son la linea (clasificacion de caracteristicas y de defectos); el hijo trae el procedimiento de 4 pasos que cubre ambas listas. Racimo MESA_RACIMOS grupo 2 (Clasificacion de defectos, DECISION 2 aprobada) sin operacion que lo nombre y sin sufijo numerico. 9.6.1: madre liga 3 de 5 (mayoria confirma)"),
    ("retention_metrics", "valor_de_vida_del_cliente",
     "paso 5 nombra el lifetime value explicitamente; el hijo ES el LTV con procedimiento de 4 pasos. 9.6.1: madre liga 4 de 6 (mayoria confirma)"),
    ("control_estadistico_de_inventario_en_transito", "causas_comunes_vs_especiales",
     "paso 3 es la linea (separar causas especiales de variacion normal); el hijo ES la doctrina Deming completa de 15 pasos. Racimo MESA_RACIMOS grupo 2 (Causas comunes, DECISION 2 aprobada) y ya es hub establecido con 15 previos: un padre mas es el patron ya validado, no una anomalia. 9.6.1: madre liga 1 de 5 (mitad o menos, manda contenido)"),
    ("customer_validation", "mvp_alta_fidelidad",
     "paso 1 tambien cubre construir la version de alta fidelidad (complementario de prueba_mvp_alta_fidelidad, ya escrito arriba: build y test del mismo paso). 9.6.1: madre liga 5 de 5 pasos (mayoria confirma)"),
    ("earlyvangelists_ventas_tempranas", "value_proposition_startup",
     "paso 4 es la linea (reconsiderar la propuesta de valor); el hijo trae el procedimiento de 3 pasos. 9.6.1: madre liga 1 de 4 (mitad o menos, manda contenido)"),
    ("scope_management_plan", "wbs_dictionary",
     "paso 3 nombra el WBS Dictionary explicitamente; el hijo ES ese documento con procedimiento de 5 pasos. 9.6.1: madre liga 4 de 5 (mayoria confirma)"),
    ("simulacion_clientes_ia", "value_proposition_startup",
     "paso 2 es la linea (entrevista simulada sobre la propuesta de valor); el hijo trae el procedimiento de 3 pasos. 9.6.1: madre liga 2 de 4 (mitad, manda contenido)"),
    ("distribucion_binomial", "planes_de_muestreo_de_aceptacion",
     "paso 4 es la linea (usar resultados para disenar planes de muestreo); el hijo trae el procedimiento de 5 pasos. 9.6.1: madre liga 1 de 4 (mitad o menos, manda contenido)"),
    ("mantenimiento_productivo_total", "capacidad_de_proceso",
     "paso 2 menciona la capacidad del proceso como efecto; el hijo ES el concepto de capacidad de proceso (Juran) con procedimiento de 4 pasos. Ya es hub con 5 previos: un padre mas es el patron ya validado. 9.6.1: madre liga 1 de 4 (mitad o menos, manda contenido)"),
    ("planificacion_inicial_calidad", "capacidad_de_proceso",
     "paso 5 es la linea (validar la capacidad y sistemas de medicion); el hijo ES ese procedimiento (segunda madre legitima del mismo hijo, mismo patron que capacidad_del_proceso en tramo 1). 9.6.1: madre liga 5 de 5 (mayoria confirma)"),
    ("rol_alta_direccion_calidad", "consejo_ejecutivo_calidad",
     "paso 1 casi repite el titulo del hijo verbatim (crear y participar en espacio de revision de calidad); el hijo trae el procedimiento de 5 pasos. 9.6.1: madre liga 2 de 6 (mitad o menos, manda contenido, y aqui el contenido es clarisimo por el calco de titulo)"),
    ("estrategia_ti_verde", "virtualizacion_servidores",
     "paso 1 es la linea (evaluar virtualizacion de servidores); el hijo trae el procedimiento de 4 pasos. 9.6.1: madre liga CERO de 5 (caso extremo, manda contenido)"),
    ("guias_diseno_sistemas_estrategicos", "complejidad_acorde_capacidad_organizacional",
     "paso 6 casi repite el titulo del hijo verbatim (contrastar complejidad contra capacidad de la organizacion); el hijo trae el procedimiento de 8 pasos. 9.6.1: madre liga 1 de 11 (mitad o menos, manda contenido, clarisimo por el calco de titulo)"),
    ("lean_launchpad_web_startup_process", "mvp_alta_fidelidad",
     "paso 9 es la linea (construir version de alta fidelidad para probar la solucion); el hijo ES ese MVP de alta fidelidad. 9.6.1: madre liga 4 de 10 (mitad o menos, manda contenido)"),
    ("principio_correspondencia_contable", "contabilidad_caja_vs_devengo",
     "paso 1 es la linea (identificar si la empresa usa caja o devengo); el hijo trae el procedimiento de 4 pasos para evaluar y migrar. 9.6.1: madre liga 2 de 4 (mitad, manda contenido)"),
    ("mejora_calidad_crosby", "concepto_programa_catorce_pasos",
     "D2 ADJUDICADO A FAVOR DEL AUDITOR (correccion declarada, acta vuelta 75 seccion 2 D2, relectura conjunta TAREA 2.4). paso 2 es la linea (implementar el programa de catorce pasos); el hijo ES ese programa con el procedimiento de adopcion (adaptar, piloto, documentar, sostener anos). Verificado por cuenta propia HOY: ninguna operacion de OPERACIONES.jsonl nombra a mejora_calidad_crosby ni a los tres miembros del racimo Programa de catorce pasos de Crosby (concepto_programa_catorce_pasos, programa_mejora_calidad_14_pasos, crosby_programa_14_pasos_introduccion), y el hijo no lleva sufijo numerico. La fusion que P.9 pediria esperar NO ESTA EN EL PLAN: esperar seria aplazar a un momento que el plan no programa. 9.6.1: madre liga 1 de 4 (mitad o menos, manda contenido, y el contenido es 9.6.2 limpio)"),
]

# Pares leidos y NO enlazados (para el reporte, no escriben nada en el grafo).
PARES_DESCARTADOS = [
    ("medicion_servicios", "programa_make_certain_3",
     "REPITE EL DESCARTE DEL TRAMO 1 (D1 del acta vuelta 75, A FAVOR): gemelo de make_certain_programa, mismo programa Make Certain de Crosby escrito dos veces. Espera a OP-S-09 (fase 05), familia de 4 ids citada en su nota"),
    ("medicion_servicios", "make_certain_programa",
     "REPITE EL DESCARTE DEL TRAMO 1 (D1): mismo caso que programa_make_certain_3, ver arriba. Espera a OP-S-09"),
    ("consejo_de_calidad_y_rol_del_director", "planificacion_estrategica_despliegue_2",
     "REPITE EL DESCARTE DEL TRAMO 1 (D3, razon corregida en 1.3.d): el destino lleva sufijo numerico y la verificacion de OP-S-09 exige que ningun id vivo lo lleve. Espera a OP-S-09"),
    ("planificacion_cero_defectos", "eliminacion_causas_error_4",
     "NUEVO EN ESTA VUELTA, MISMA FIGURA QUE D3: el hijo lleva sufijo numerico vivo y pertenece al racimo MESA_RACIMOS grupo 1 'Eliminacion de causas de error' (eliminacion_causas_error, eliminacion_causas_error_2, eliminacion_causas_error_4), racimo con fusion adjudicada pendiente solo del disparo del fundador (DECISION 1, nota de la ficha OP-E-02/mesa). A diferencia del D2, aqui SI hay sufijo numerico: no se escribe, espera a OP-S-09 o al disparo de la fusion del trio ECR"),
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
    print(f"DESCARTADOS: {len(PARES_DESCARTADOS)}")
    for m, h, r in PARES_DESCARTADOS:
        print(f"  {m} -> {h} | {r}")


if __name__ == "__main__":
    main()
