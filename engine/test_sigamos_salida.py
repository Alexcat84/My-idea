# -*- coding: utf-8 -*-
"""Verifica que extender_sigamos_dirigido (Fase 2.9) respeta la intencion
de salida del usuario DENTRO de la extension: al primer 'dame mi plan',
corta de inmediato en vez de forzar las preguntas restantes. Monkeypatch
de leer_entrada (2 respuestas: una real, luego 'dame mi plan') y de
llamar_claude (el detector de decision) para no gastar API real."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm

graph = pm.cargar_grafo()
families = pm.plan_readiness.cargar_families(graph)
preguntas_cache = pm.cargar_preguntas_cache()

respuestas_guion = [
    "cobro por pieza pero no se cuanto me cuesta en materiales o tiempo",
    "dame mi plan ya, con esto alcanza",
]
idx = {"i": 0}


def leer_entrada_falsa(prompt=""):
    r = respuestas_guion[idx["i"]]
    idx["i"] += 1
    return r


def llamar_claude_falso(system, user_text, model, max_tokens=1500, componente=None):
    # SYSTEM_PREGUNTA_DIRIGIDA -> devuelve la pregunta tal cual (no importa el texto)
    if system == pm.SYSTEM_PREGUNTA_DIRIGIDA:
        return "¿ya sacaste la cuenta de cuanto te cuesta cada pieza?"
    # SYSTEM_PROFUNDIZAR -> el detector de decision de plan
    if system == pm.SYSTEM_PROFUNDIZAR:
        respuesta = json.loads(user_text) if user_text.strip().startswith("{") else user_text
        texto = respuesta if isinstance(respuesta, str) else str(respuesta)
        if "dame mi plan" in texto.lower():
            return json.dumps({"decision": "generar_ya"})
        return json.dumps({"decision": "continuar"})
    raise AssertionError(f"llamada inesperada con system no reconocido: {system[:50]}")


pm.leer_entrada = leer_entrada_falsa
pm.llamar_claude = llamar_claude_falso

ruta = ["leap_of_faith_assumptions"]
modos = ["conversado"]
visitados = set(ruta)

resultado = pm.extender_sigamos_dirigido(
    graph, families, visitados, ruta, modos,
    perfil_sesion="Hace macetas, trabaja solo.",
    texto_original="quiero saber si mi idea tiene futuro",
    familias_faltantes=["viabilidad_economica"],
    preguntas_cache=preguntas_cache,
    ultimas_preguntas=[],
    session_id="test29mock", project_id=None, db_session_id=None,
    es_seguimiento=False, estado_vivo_previo=None, fallback_events=[],
    prioridad_declarada=None,
)

print("Resultado:", resultado)
print("Ruta final:", ruta)
print("Modos final:", modos)
print("Preguntas hechas (idx consumido):", idx["i"])

assert resultado["hubo_extension"] is True
assert idx["i"] == 2, f"se esperaban exactamente 2 preguntas (la real + la que trae 'dame mi plan'), se hicieron {idx['i']}"
# nodo 1: pregunta real, respuesta real (continua). nodo 2: pregunta real,
# la RESPUESTA a esa pregunta es 'dame mi plan' -> corta ahi mismo, sin
# llegar a preguntar un 3er nodo (elegidos tenia hasta MAX_TURNOS_EXTRA=3
# candidatos disponibles). Por eso la ruta gana exactamente 2 nodos
# nuevos, no 3 - la prueba real es que NUNCA se llega a un 3er intento.
assert len(ruta) == 3, f"se esperaban 2 nodos nuevos (1 base + 2 = 3 total), ruta tiene {len(ruta)} elementos: {ruta}"

print("\nTODO OK: la extension dirigida corta en cuanto detecta 'dame mi plan', sin llegar a un 3er intento.")
