"""VUELTA 77, TAREA 3: OP-E-01, TRAMO 3. Escribe en dataset/nodos/<madre>.json
las aristas nuevas confirmadas por lectura par a par (9.6.2 contenido, con
9.6.1 y escalera chequeados igual que en los tramos 1 y 2), leidas contra la
cabeza de la bolsa recalibrada FRESCA de esta vuelta y ya filtrada por el
P.9.1 ENSANCHADO (docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V77.jsonl,
docs/loop/SALIDA_V77_TRAMO3_FILTRO_P91.txt).

CRITERIO ADJUDICADO PARA ESTE TRAMO (encargo, TAREA 3): veredicto del
cribado (docs/INTRA_DOMINIO_VEREDICTOS.jsonl) PRIMERO; el sufijo numerico
solo opina cuando NO hay veredicto (y en ese caso ya lo cubre el filtro
P.9.1 via OP-S-09). De los 30 primeros candidatos limpios, 4 tenian
veredicto propio (todos D, ninguno A: nada que revertir por esa via) y 26
no tenian veredicto (el contenido decide, 9.6.2).

DOS pares de los 30 se leen y NO se escriben, los dos por la MISMA figura
nueva de esta vuelta (no cubierta por P.9.1 porque ninguna operacion
nombra los ids exactos, pero SI verificada contra docs/RACIMOS_MIEMBROS.jsonl
por corrida propia): madre e hijo son miembros DEL MISMO racimo declarado.
- `human_error_como_sintoma` -> `preguntar_que_no_quien`: los dos son
  miembros del racimo "No culpar a la persona, arreglar el sistema"
  (health_safety, 20 miembros, DECISION 2, sin operacion ejecutada que lo
  toque). Enlazarlos como jerarquia madre-hijo adjudicaria por la puerta de
  enlaces una pregunta que pertenece a la mesa de DECISION 2 (continua o
  repite, par a par, dentro del racimo). PENDIENTE DE DOCTRINA: ninguna
  regla escrita cubre "candidato con madre e hijo en el mismo racimo
  declarado"; se registra el criterio aplicado (no se enlaza dentro de un
  racimo sin adjudicar) y se sigue, por EJECUTOR.md regla 5.
- `mejora_calidad_crosby` -> `programa_mejora_calidad_14_pasos`: mismo
  racimo "Programa de catorce pasos de Crosby" (quality, 3 miembros, sin
  operacion) que el D2 YA ESCRITO en el tramo 2
  (`mejora_calidad_crosby` -> `concepto_programa_catorce_pasos`). El D2 fue
  una excepcion adjudicada UNA VEZ por el auditor (acta vuelta 75 seccion 2
  D2) para ESE par; extenderla sin nueva adjudicacion a un SEGUNDO hijo del
  mismo racimo seria adjudicar por acumulacion. PENDIENTE DE DOCTRINA, mismo
  criterio que arriba.

Los otros dos casos leidos con cuidado especial (declarados en el reporte,
no aqui, para no repetir el texto): `lean_launchpad_web_startup_process` ->
`construir_mvp_baja_fidelidad` (el paso que la calibra, el 9, habla de ALTA
fidelidad; el paso real que calza es el 5, que SI habla de baja fidelidad;
se escribe igual, la arista no lleva indice de paso) y `cero_defectos` ->
`zero_defects_concepto` (veredicto D del cribado, pero titulo y contenido
muy cercanos: se escribe porque el veredicto manda, marcado discutible).
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
NODOS = RAIZ / "dataset" / "nodos"

PARES_SANOS = [
    ("muestreo_de_aceptacion", "tipos_planes_muestreo_atributos_variables",
     "paso 4 es la linea (seleccionar/disenar plan de muestreo, por atributos o variables); el hijo trae el procedimiento propio de 4 pasos para elegir entre los dos tipos. sin veredicto de cribado"),
    ("distribuciones_probabilidad", "distribucion_normal_probabilidad",
     "paso 4 es la linea (usar la distribucion para estimar probabilidades); el hijo especializa en la distribucion normal con el procedimiento Z de 4 pasos. sin veredicto de cribado"),
    ("definiciones_operacionales_de_calidad", "key_process_product_characteristics",
     "paso 1 es la linea (identificar caracteristicas criticas de calidad); el hijo trae el procedimiento propio de 5 pasos (QFD, AMFE, clasificacion por importancia). sin veredicto de cribado"),
    ("estadistica_basica_calidad", "medidas_tendencia_dispersion",
     "pasos 2 y 3 son la linea (medidas de tendencia central y dispersion); el hijo trae contenido propio que la madre no tiene (coeficiente de variacion, no eliminar atipicos sin evidencia). VEREDICTO DEL CRIBADO: puesto 2826, clase D (confirma que no son el mismo par de nodos)"),
    ("identificar_oportunidades_sostenibilidad", "benchmarking_desempeno_ambiental",
     "paso 3 es la linea (comparar desempeno ambiental con competidores); el hijo trae el procedimiento propio de 5 pasos (autoevaluacion, KPIs, matriz comparativa). sin veredicto de cribado"),
    ("post_launch_review", "lessons_learned",
     "paso 4 es la linea (documentar lecciones aprendidas); el hijo trae el procedimiento propio de 5 pasos de captura. sin veredicto de cribado"),
    ("dmaic_fase_measure", "formulacion_teorias_causa",
     "paso 7 es la linea (generar teorias de causa raiz con diagramas causa-efecto); el hijo ES ese proceso con procedimiento propio de 4 pasos (brainstorm, afinidad, ishikawa, FMEA). sin veredicto de cribado"),
    ("lean_launchpad_web_startup_process", "construir_mvp_baja_fidelidad",
     "CORRECCION DE PASO: el calibrador senalo el paso 9 (que habla de ALTA fidelidad, no calza). El paso real que calza es el 5 ('Construir un sitio web de baja fidelidad, splash page, formularios de pre-orden'), que SI es la linea del hijo; el hijo trae el procedimiento propio de 5 pasos. DISCUTIBLE: se escribe por el contenido verificado contra el paso 5, no contra el paso que trajo el calibrador. sin veredicto de cribado"),
    ("ecuacion_de_valor_cliente", "preguntas_need_payoff",
     "paso 3 nombra Necesidad-Beneficio explicitamente; el hijo ES esas preguntas Need-Payoff con procedimiento propio de 6 pasos. sin veredicto de cribado"),
    ("capacitacion_roles_gerencia", "investigacion_incidentes",
     "paso 4 es la linea (capacitar en investigacion de incidentes); el hijo trae el procedimiento propio de 6 pasos, mas amplio (enfoque sistemico). El gemelo de titulo investigacion_incidentes_2 (96.7% Gate 0) ya esta deprecado: sin conflicto de duplicado vivo. sin veredicto de cribado"),
    ("seleccion_estrategia_pricing", "determinar_tipo_de_mercado",
     "paso 1 es la linea (determinar tipo de mercado); el hijo ES ese analisis con procedimiento propio de 12 pasos. sin veredicto de cribado"),
    ("cero_defectos", "zero_defects_concepto",
     "paso 1 es la linea (establecer el estandar CD como compromiso personal); el hijo trae contenido propio (poner el compromiso por escrito con quien te ayuda, enfoque de negocio pequeno) mas alla de lo que la madre cubre. VEREDICTO DEL CRIBADO: puesto 2464, clase D. DISCUTIBLE por cercania de titulo y tema con la madre (mismo concepto Crosby Cero Defectos): se escribe porque el veredicto de cribado manda sobre la sospecha de gemelo, marcado para relectura ciega"),
    ("post_launch_review", "team_performance_assessment",
     "paso 2 es la linea (evaluar responsabilidad y desempeno del equipo); el hijo ES esa evaluacion con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("definicion_objetivos_proyecto_sistema", "diseno_conceptual_sistema",
     "paso 1 nombra 'el diseno conceptual' como el objeto que se descompone; el hijo ES el proceso de construir ese diseno conceptual, con procedimiento propio de 7 pasos. sin veredicto de cribado"),
    ("concepto_proyecto_breakthrough", "pocos_vitales_muchos_utiles",
     "paso 2 nombra 'vitales pocos' y 'utiles muchos' explicitamente; el hijo ES esa clasificacion de Pareto con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("estrategia_de_innovacion_arenas", "product_roadmap_estrategico",
     "paso 4 es la linea (desarrollar roadmap de producto para las arenas seleccionadas); el hijo ES ese roadmap con procedimiento propio de 7 pasos. sin veredicto de cribado"),
    ("capacidad_proceso_concepto", "control_estadistico_de_procesos",
     "paso 1 es la linea (confirmar control estadistico, sin causas asignables); el hijo ES el SPC con procedimiento propio de 10 pasos. DISCUTIBLE: Gate 0 marca control_estadistico_de_procesos y control_estadistico_del_proceso con 97,3% de similitud de titulo (control_estadistico_del_proceso esta en la nomina de OP-S-09 de esta vuelta, este hijo NO); se escribe porque el contenido de este hijo (metodologia SPC general de 10 pasos) es distinto del contenido ya visto de control_estadistico_del_proceso, pero se marca para relectura ciega igual que el discutible equivalente de la vuelta 76 (capacidad_de_proceso_2). sin veredicto de cribado"),
    ("prueba_teorias_causa_raiz", "diagrama_causa_efecto",
     "paso 1 nombra el diagrama de causa-efecto explicitamente; el hijo ES ese diagrama Ishikawa con procedimiento propio de 7 pasos. sin veredicto de cribado"),
    ("waterfall_vs_agile_development", "desarrollo_de_clientes_customer_development",
     "paso 3 es la linea (alinear desarrollo de producto con Customer Development); el hijo ES ese modelo con procedimiento propio de 4 pasos. DISCUTIBLE: el titulo del hijo ('El Modelo de Desarrollo de Clientes') se parece al de dos ids ya marcados en la nomina de OP-S-09 de esta vuelta (customer_development_modelo, modelo_customer_development), pero el recomputo lexico de OP-S-09 NO agrupo a este tercer id (usa 'desarrollo_de_clientes' en vez de 'customer_development_modelo/modelo_customer_development', fuera del alcance del metodo por sufijo/particula/orden de palabras declarado); posible sinonimo puro no detectado, se marca para relectura ciega. sin veredicto de cribado"),
    ("fees_y_breakup_fee_adquisicion", "breakup_fee_evaluation",
     "paso 2 es la linea (evaluar si conviene pedir breakup fee); el hijo ES esa evaluacion con procedimiento propio de 5 pasos. VEREDICTO DEL CRIBADO: puesto 223, clase D"),
    ("screening_mercados_potenciales", "uso_del_us_commercial_service",
     "paso 5 nombra el U.S. Commercial Service explicitamente; el hijo ES el aprovechamiento de ese servicio con procedimiento propio de 6 pasos. sin veredicto de cribado"),
    ("plan_cambio_climatico", "compra_offsets_carbono",
     "paso 4 es la linea (considerar compra de offsets de carbono); el hijo ES esa compra con procedimiento propio de 6 pasos. sin veredicto de cribado"),
    ("analisis_de_ratios_financieros", "retorno_sobre_capital",
     "paso 1 nombra el ROE explicitamente; el hijo ES el ROE con procedimiento propio de 3 pasos. VEREDICTO DEL CRIBADO: puesto 1369, clase D"),
    ("franquicia_unidad_individual", "programa_de_referidos_de_franquiciados",
     "paso 1 es la linea (definir proceso de venta para franquicias unitarias); el hijo trae el procedimiento propio de referidos de franquiciados, canal especifico de venta. sin veredicto de cribado"),
    ("determinar_tipo_de_mercado", "actualizar_business_model_canvas_tuneup",
     "paso 12 nombra actualizar el Business Model Canvas con la hipotesis; el hijo ES ese tune-up con procedimiento propio de 4 pasos. sin veredicto de cribado"),
    ("analisis_de_capacidad_de_recursos", "metodo_strategic_buckets",
     "paso 6 nombra Strategic Buckets explicitamente; el hijo ES ese metodo con procedimiento propio de 6 pasos. sin veredicto de cribado"),
    ("identificar_si_tu_producto_necesita_proteccion_especial", "probar_empaque_antes_de_escalar_envios",
     "paso 5 es la linea (reforzar empaque antes de escalar envios); el hijo trae el procedimiento propio de prueba de empaque con courier, 5 pasos. VEREDICTO DEL CRIBADO: puesto 1746, clase D"),
    ("control_exportaciones_bis", "licencia_exportacion_regulaciones",
     "paso 1 es la linea (determinar si se requiere licencia de exportacion); el hijo ES esa determinacion con procedimiento propio de 6 pasos (ECCN, ITAR, OFAC). VEREDICTO DEL CRIBADO: puesto 1951, clase D"),
]

# Pares leidos y NO enlazados (para el reporte, no escriben nada en el grafo).
PARES_DESCARTADOS = [
    ("human_error_como_sintoma", "preguntar_que_no_quien",
     "PENDIENTE DE DOCTRINA: madre e hijo son miembros del MISMO racimo declarado "
     "'No culpar a la persona, arreglar el sistema' (health_safety, 20 miembros, "
     "DECISION 2, verificado contra docs/RACIMOS_MIEMBROS.jsonl). P.9.1 no lo "
     "aparta (ninguna operacion ejecutada nombra estos ids), pero enlazarlos como "
     "jerarquia adjudicaria por la puerta de enlaces una pregunta de esa mesa "
     "(continua o repite, par a par, dentro del racimo). No se enlaza."),
    ("mejora_calidad_crosby", "programa_mejora_calidad_14_pasos",
     "PENDIENTE DE DOCTRINA: mismo racimo 'Programa de catorce pasos de Crosby' "
     "(quality, 3 miembros, sin operacion) que el D2 ya escrito en el tramo 2 "
     "(mejora_calidad_crosby -> concepto_programa_catorce_pasos). El D2 fue una "
     "excepcion adjudicada UNA VEZ por el auditor para ESE par; extenderla sin "
     "nueva adjudicacion a un segundo hijo del mismo racimo seria adjudicar por "
     "acumulacion. No se enlaza."),
]


def cargar(node_id):
    p = NODOS / f"{node_id}.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def main():
    tocados = []
    ya_estaban = []
    escalera_rota = []
    for madre_id, hijo_id, razon in PARES_SANOS:
        data, path = cargar(madre_id)
        hijo_data, _ = cargar(hijo_id)

        if madre_id in (hijo_data.get("nodos_siguientes") or []):
            escalera_rota.append((madre_id, hijo_id))

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
    print(f"ESCALERA ROTA (ciclo de dos, hijo ya apuntaba a la madre): {len(escalera_rota)}")
    for m, h in escalera_rota:
        print(f"  {m} -> {h}")
    print(f"DESCARTADOS: {len(PARES_DESCARTADOS)}")
    for m, h, r in PARES_DESCARTADOS:
        print(f"  {m} -> {h} | {r}")


if __name__ == "__main__":
    main()
