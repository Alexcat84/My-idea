# -*- coding: utf-8 -*-
"""Prueba en vivo (API real, costo minimo ~2-3 llamadas Haiku) de
extender_sigamos_dirigido: verifica que el clasificador REAL
(SYSTEM_PROFUNDIZAR) reconoce 'dame mi plan' dicho a mitad de la
extension dirigida y corta de inmediato, sin llegar a un 3er nodo."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import prototipo_motor as pm

pm.db.forzar_offline(True)

graph = pm.cargar_grafo()
families = pm.plan_readiness.cargar_families(graph)
preguntas_cache = pm.cargar_preguntas_cache()

respuestas_guion = [
    "cobro por pieza pero no se cuanto me cuesta en materiales o tiempo",
    "dame mi plan ya, con esto alcanza",
]
idx = {"i": 0}


def leer_entrada_falsa(prompt=""):
    print(prompt)
    r = respuestas_guion[idx["i"]]
    idx["i"] += 1
    print(">", r)
    return r


pm.leer_entrada = leer_entrada_falsa

ruta = ["leap_of_faith_assumptions"]
modos = ["conversado"]
visitados = set(ruta)

resultado = pm.extender_sigamos_dirigido(
    graph, families, visitados, ruta, modos,
    perfil_sesion="Hace macetas de calcita con resina, trabaja solo.",
    texto_original="quiero saber si mi idea de macetas tiene futuro",
    familias_faltantes=["viabilidad_economica"],
    preguntas_cache=preguntas_cache,
    ultimas_preguntas=[],
    session_id="test29real", project_id=None, db_session_id=None,
    es_seguimiento=False, estado_vivo_previo=None, fallback_events=[],
    prioridad_declarada=None,
)

pm.reportar_costo()
print("\nResultado:", resultado)
print("Ruta final:", ruta)
print("Preguntas hechas (respuestas consumidas):", idx["i"])

assert idx["i"] == 2, f"se esperaban exactamente 2 respuestas consumidas (real API), hubo {idx['i']}"
assert len(ruta) == 3, f"se esperaban 2 nodos nuevos (base + 2 = 3), ruta tiene {len(ruta)}: {ruta}"
print("\nTODO OK (API real): 'dame mi plan' a mitad de la extension corta de inmediato, sin llegar a un 3er nodo.")
