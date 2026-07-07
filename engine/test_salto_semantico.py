# -*- coding: utf-8 -*-
"""Verifica la validacion de salto_semantico (Fase 2.8) sin llamadas
reales a la API ni a la brujula: monkeypatch de pm.buscar_afines para
controlar exactamente que saltos_posibles se ofrecen, y de
pm.llamar_claude para simular al modelo eligiendo un salto valido, y
luego uno invalido (fuera de lo ofrecido, debe rechazarse y reintentar)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prototipo_motor as pm

graph = pm.cargar_grafo()
preguntas_cache = pm.cargar_preguntas_cache()
actual_id = "design_thinking_fundamentos"
visitados = {actual_id}

# Un candidato de salto real y valido (no visitado, existe en el grafo)
candidato_salto = "decision_fundador_solo_vs_equipo"
assert candidato_salto in graph, "el nodo de prueba debe existir en el grafo"

pm.buscar_afines = lambda texto, excluidos, k=5, min_score=0.0, con_score=False, graph=None, dominios_desbloqueados=None: (
    [(candidato_salto, 0.9)] if con_score else [candidato_salto]
)

# --- Caso 1: el modelo elige un salto valido (esta en saltos_posibles) ---
llamadas = {"n": 0}


def llamar_claude_falso_valido(system, user_text, model, max_tokens=1500, componente=None):
    llamadas["n"] += 1
    return json.dumps({
        "accion": "avanzar",
        "camino": [],
        "salto_semantico": candidato_salto,
        "pregunta_necesaria": True,
        "pregunta_adaptada": "ya que haces todo tu solo, ¿has pensado en tu limite de produccion mensual?",
        "repregunta": None,
        "perfil_update": None,
        "prioridad_declarada": None,
    })


pm.llamar_claude = llamar_claude_falso_valido
resultado = pm.interpretar_multi_salto(
    actual_id, graph, visitados,
    perfil_sesion="Hace macetas, trabaja solo.",
    texto_original="quiero saber si mi idea tiene futuro",
    pregunta_hecha=None, respuesta_usuario="hago todo yo solo, sin equipo ni empleados",
    repreguntas_disponibles=True, preguntas_cache=preguntas_cache,
)
print("Caso 1 - llamadas:", llamadas["n"], "resultado:", resultado)
assert llamadas["n"] == 1, "un salto valido no deberia disparar retry"
assert resultado["es_salto"] is True
assert resultado["camino"] == [candidato_salto]
print("Caso 1 OK: salto semantico valido aceptado en el primer intento.\n")

# --- Caso 2: el modelo "alucina" un salto que NO esta en saltos_posibles ---
llamadas2 = {"n": 0}


def llamar_claude_falso_invalido(system, user_text, model, max_tokens=1500, componente=None):
    llamadas2["n"] += 1
    ctx = json.loads(user_text)
    if llamadas2["n"] == 2:
        assert "ids_validos" in ctx, "el retry debe incluir ids_validos"
    return json.dumps({
        "accion": "avanzar",
        "camino": [],
        "salto_semantico": "id_que_no_fue_ofrecido",
        "pregunta_necesaria": True,
        "pregunta_adaptada": "algo",
        "repregunta": None,
        "perfil_update": None,
        "prioridad_declarada": None,
    })


pm.llamar_claude = llamar_claude_falso_invalido
resultado2 = pm.interpretar_multi_salto(
    actual_id, graph, visitados,
    perfil_sesion="Hace macetas, trabaja solo.",
    texto_original="quiero saber si mi idea tiene futuro",
    pregunta_hecha=None, respuesta_usuario="hago todo yo solo, sin equipo ni empleados",
    repreguntas_disponibles=True, preguntas_cache=preguntas_cache,
)
print("Caso 2 - llamadas:", llamadas2["n"], "resultado:", resultado2)
assert llamadas2["n"] == 2, "un salto invalido debe disparar exactamente 1 retry"
# tras 2 fallos (retry tambien invalido), cae al tier-2 (auto-afinidad local, es_salto=False)
assert resultado2 is not None, "no deberia devolver None (fallo de validacion, no de red)"
assert resultado2.get("es_salto") is False, "el respaldo tier-2 nunca es un salto (usa afinidad local)"
print("Caso 2 OK: salto_semantico inventado se rechaza, dispara retry, y cae al respaldo local tras fallar de nuevo.")

print("\nTODO OK: validacion de salto_semantico verificada.")
