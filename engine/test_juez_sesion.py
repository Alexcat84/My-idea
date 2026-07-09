# -*- coding: utf-8 -*-
"""Fase 3.1 (caja de vidrio): evaluar_calidad_sesion. Verifica muestreo
(0.0 = nunca llama, 1.0 = siempre llama), que resuelve node_ids a titulos
reales antes de mandarlos al juez, y que una sesion sin decision_turno (o
sin API_KEY) devuelve None sin llamar a nada."""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm

graph = pm.cargar_grafo()
nodo_id = next(iter(graph))
titulo_real = graph[nodo_id]["titulo_concepto"]

decisiones = [
    {"tipo": "fallback_auto", "nodo_actual": nodo_id, "candidato_elegido": nodo_id, "motivo": "x"},
    {
        "tipo": "decision_turno",
        "nodo_actual": nodo_id,
        "respuesta_usuario": "no he calculado costos todavia",
        "candidatos_locales": [nodo_id],
        "saltos_posibles": [{"id": nodo_id, "titulo": titulo_real, "afinidad": 0.5}],
        "decision": {"accion": "avanzar", "camino": [nodo_id], "es_salto": False},
        "razonamiento": "el usuario menciono costos",
    },
]

# --- Caso 1: muestreo=0.0 nunca llama (ni siquiera con API_KEY real) ---
pm.API_KEY = "test-fake-key"
llamadas = {"n": 0}
pm.llamar_claude = lambda *a, **k: (llamadas.__setitem__("n", llamadas["n"] + 1), "{}")[1]
resultado_sin_muestreo = pm.evaluar_calidad_sesion(decisiones, graph, muestreo=0.0)
assert resultado_sin_muestreo is None
assert llamadas["n"] == 0, "muestreo=0.0 no deberia llamar nunca al juez"
print("Caso 1 OK: muestreo=0.0 nunca invoca al juez.")

# --- Caso 2: sin API_KEY, no llama aunque muestreo=1.0 ---
pm.API_KEY = ""
resultado_sin_key = pm.evaluar_calidad_sesion(decisiones, graph, muestreo=1.0)
assert resultado_sin_key is None
assert llamadas["n"] == 0
print("Caso 2 OK: sin API_KEY no invoca al juez aunque muestreo=1.0.")

# --- Caso 3: sin eventos decision_turno, no llama (nada que evaluar) ---
pm.API_KEY = "test-fake-key"
solo_fallback = [d for d in decisiones if d["tipo"] != "decision_turno"]
resultado_sin_turnos = pm.evaluar_calidad_sesion(solo_fallback, graph, muestreo=1.0)
assert resultado_sin_turnos is None
assert llamadas["n"] == 0
print("Caso 3 OK: sin eventos decision_turno, no invoca al juez.")

# --- Caso 4: muestreo=1.0 con API_KEY y eventos reales SI llama, y resuelve titulos ---
capturado = {}


def llamar_claude_falso(system, user_text, model, max_tokens=1500, componente=None):
    llamadas["n"] += 1
    capturado["ctx"] = json.loads(user_text)
    return json.dumps({
        "pertinencia_transiciones": 5,
        "repeticion_detectada": False,
        "señales_fuera_de_material": [],
        "comentario": "todo coherente",
    })


pm.llamar_claude = llamar_claude_falso
veredicto = pm.evaluar_calidad_sesion(decisiones, graph, muestreo=1.0)
assert llamadas["n"] == 1, "muestreo=1.0 con eventos reales debe llamar exactamente una vez"
assert veredicto == {
    "pertinencia_transiciones": 5, "repeticion_detectada": False,
    "señales_fuera_de_material": [], "comentario": "todo coherente",
}
turnos_enviados = capturado["ctx"]["turnos"]
assert len(turnos_enviados) == 1, "solo debe enviar los eventos decision_turno, no fallback_auto"
assert turnos_enviados[0]["nodo"] == titulo_real, "debe resolver node_id a titulo real, no mandar el id crudo"
assert turnos_enviados[0]["destino"] == [titulo_real]
assert turnos_enviados[0]["respuesta_usuario"] == "no he calculado costos todavia"
print("Caso 4 OK: llama al juez, filtra solo decision_turno, y resuelve ids a titulos reales.")

print("\nTODO OK: juez de sesion muestreado (Fase 3.1) funciona.")
