#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""racimos_health_safety.py . mide los racimos de ids de health_safety para el plan.

SOLO LECTURA. Para cada racimo levanta miembros, pares posibles, pares leidos con su
clase, aristas entre miembros, y la COBERTURA (banco 9.26: toda forma lleva su cobertura
al lado). No adjudica nada: mide.
"""
import json, io, sys, itertools, collections

sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
AL = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}


def res(x):
    s = set()
    while x in AL and x not in s:
        s.add(x); x = AL[x]
    return x


def vecinos(k):
    out = set()
    for c in ("nodos_previos", "nodos_siguientes"):
        for y in (G.get(k, {}).get(c) or []):
            out.add(res(y))
    return out


LEIDO = {}
for r in V:
    LEIDO[frozenset((r["nodo_a"], r["nodo_b"]))] = (r["puesto_intra"], r["clase"])

RACIMOS = [
 ("LA VIEJA Y LA NUEVA VISION", ["new_view_human_error", "new_view_vs_old_view",
  "old_view_vs_new_view_human_error", "new_view_vs_old_view_de_error_humano",
  "vieja_vision_vs_nueva_vision_seguridad", "nueva_vision_organizacion_linea_seguridad"]),
 ("EL SESGO RETROSPECTIVO", ["evitar_sesgo_retrospectivo_hindsight", "sesgo_retrospectivo_hindsight_2",
  "sesgo_retrospectivo", "sesgo_retrospectivo_hindsight", "reconstruccion_contexto_situacional",
  "evitar_shopping_bag", "perspectiva_dentro_del_tunel"]),
 ("LAS DEFENSAS", ["defensas_en_profundidad", "defensas_en_profundidad_2", "defensas_en_profundidad_3",
  "modelo_barreras_defensas", "modelo_queso_suizo", "trayectoria_del_accidente",
  "ventana_oportunidad_accidente"]),
 ("LAS CONDICIONES LATENTES", ["condiciones_latentes_largo_plazo", "condiciones_latentes_organizacionales",
  "fallas_activas_condiciones_latentes", "caso_descarrilamiento_nakina", "condiciones_latentes_riesgo_universal"]),
 ("EL ERROR COMO SINTOMA", ["errores_como_consecuencia", "human_error_como_sintoma",
  "falla_sistemica_vs_error_individual", "riesgos_del_enfoque_en_error_humano",
  "error_humano_vs_falla_mecanica", "seduccion_modelo_persona", "enfoque_situacional_vs_personal",
  "atribucion_retrospectiva_del_error", "preguntar_que_no_quien"]),
 ("LA DERIVA", ["deriva_hacia_el_fallo", "drift_hacia_el_fallo", "drift_hacia_el_fallo_2",
  "normalizacion_de_la_desviacion"]),
 ("LA CULTURA JUSTA", ["cultura_justa", "cultura_justa_organizacional", "cultura_justa_3", "cultura_de_reporte"]),
 ("EL ERROR DE MANTENIMIENTO", ["omisiones_en_mantenimiento", "prevalencia_omisiones",
  "vulnerabilidad_instalacion", "caracteristicas_tareas_propensas_omision",
  "diseno_recordatorios_efectivos_2", "riesgo_actividades_mantenimiento",
  "riesgo_error_humano_en_mantenimiento"]),
 ("LA GESTION DEL ERROR", ["gestion_de_errores", "principios_gestion_error", "enfoque_situacional_vs_personal"]),
 ("LA MEDICION QUE CORROMPE", ["cuestionar_vision_zero", "responsabilidad_hacia_abajo_vs_rendicion_de_cuentas",
  "limitaciones_ltif_indicador", "medidas_proceso_vs_resultado", "metas_de_seguridad_correctas",
  "no_usar_triangulo_heinrich", "paradoja_bajos_incidentes_altas_fatalidades"]),
 ("LA CULTURA COORDINADORA", ["cultura_flexible", "cultura_flexible_organizacional",
  "cultura_como_mecanismo_descentralizacion"]),
 ("EL APRENDIZAJE ORGANIZACIONAL", ["cultura_de_aprendizaje", "ingenieria_cultura_aprendizaje",
  "aprendizaje_organizacional_desde_incidentes", "reporte_casi_accidentes", "revision_de_aprendizaje"]),
 ("LA REACCION AL FALLO", ["reacciones_al_fallo", "foco_proximal_reacciones_falla", "ciclo_de_culpa",
  "ciclo_de_culpa_2", "dysfunctional_organizational_culture_patterns", "abandonar_arreglos_rapidos",
  "hard_fixes_organizacionales"]),
]

tot_m = tot_pos = tot_leidos = tot_a = tot_ar = 0
print("| racimo | miembros | pares posibles | leidos | A | D | **cobertura** | aristas entre miembros |")
print("|---|---:|---:|---:|---:|---:|---:|---:|")
det = []
for nombre, ms in RACIMOS:
    faltan = [m for m in ms if m not in G]
    assert not faltan, "ids que no existen en el grafo: %s" % faltan
    pos = len(ms) * (len(ms) - 1) // 2
    leidos = a = d = 0
    puestos = []
    for x, y in itertools.combinations(ms, 2):
        k = frozenset((x, y))
        if k in LEIDO:
            leidos += 1
            p, c = LEIDO[k]
            puestos.append((p, c))
            if c == "A":
                a += 1
            elif c == "D":
                d += 1
    ar = sum(1 for x, y in itertools.combinations(ms, 2) if res(y) in vecinos(x) or res(x) in vecinos(y))
    print("| **%s** | %d | %d | %d | %d | %d | **%.0f%%** | %d |" %
          (nombre, len(ms), pos, leidos, a, d, 100.0 * leidos / pos, ar))
    det.append((nombre, ms, sorted(puestos)))
    tot_m += len(ms); tot_pos += pos; tot_leidos += leidos; tot_a += a; tot_ar += ar

print()
print("TOTALES: %d miembros nominales, %d pares posibles, %d leidos (%.0f%%), %d A, %d aristas"
      % (tot_m, tot_pos, tot_leidos, 100.0 * tot_leidos / tot_pos, tot_a, tot_ar))
print()
for nombre, ms, puestos in det:
    print("--- %s" % nombre)
    print("    miembros: %s" % ", ".join(ms))
    print("    puestos leidos: %s" % (", ".join("%d%s" % (p, c) for p, c in puestos) or "ninguno"))
