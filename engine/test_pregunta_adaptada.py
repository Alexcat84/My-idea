# -*- coding: utf-8 -*-
"""Verifica que interpretar_multi_salto EXIGE pregunta_adaptada cuando
pregunta_necesaria=true: si el modelo devuelve un camino valido pero omite
pregunta_adaptada, debe tratarse como respuesta invalida (retry), y si el
segundo intento SI la trae, debe usarse tal cual (nunca la cruda del cache)."""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import prototipo_motor as pm

graph = pm.cargar_grafo()
preguntas_cache = pm.cargar_preguntas_cache()
actual_id = "design_thinking_fundamentos"
visitados = {actual_id}
primer_sucesor = graph[actual_id]["nodos_siguientes"][0]

llamadas = {"n": 0}


def llamar_claude_falso(system, user_text, model, max_tokens=1500, componente=None):
    llamadas["n"] += 1
    if llamadas["n"] == 1:
        # camino valido, pero SIN pregunta_adaptada -> debe rechazarse
        return json.dumps({
            "accion": "avanzar",
            "camino": [primer_sucesor],
            "pregunta_necesaria": True,
            "pregunta_adaptada": None,
            "repregunta": None,
            "perfil_update": None,
        })
    # segundo intento: ahora si trae pregunta_adaptada
    return json.dumps({
        "accion": "avanzar",
        "camino": [primer_sucesor],
        "pregunta_necesaria": True,
        "pregunta_adaptada": "¿Ya probaste tu idea con alguien fuera de tu círculo cercano?",
        "repregunta": None,
        "perfil_update": None,
    })


pm.llamar_claude = llamar_claude_falso

resultado = pm.interpretar_multi_salto(
    actual_id, graph, visitados,
    perfil_sesion="Hace macetas de resina y calcita, trabaja solo.",
    texto_original="quiero saber si mi idea de macetas tiene futuro",
    pregunta_hecha=None,
    respuesta_usuario=None,
    repreguntas_disponibles=True,
    preguntas_cache=preguntas_cache,
    ultimas_preguntas=[],
    registrar_evento=None,
)

print("Llamadas:", llamadas["n"])
print("Resultado:", resultado)

assert llamadas["n"] == 2, "debio reintentar tras faltar pregunta_adaptada en el primer intento"
assert resultado["pregunta_adaptada"] == "¿Ya probaste tu idea con alguien fuera de tu círculo cercano?"
print("\nTODO OK: pregunta_adaptada faltante se trata como invalida y dispara retry; el retry exitoso se usa tal cual.")
