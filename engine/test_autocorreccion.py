# -*- coding: utf-8 -*-
"""Verifica la auto-correccion invisible forzando ambos intentos a fallar
(mock de llamar_claude devolviendo un id inventado dos veces seguidas)."""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import prototipo_motor as pm

graph = pm.cargar_grafo()
preguntas_cache = pm.cargar_preguntas_cache()
actual_id = "design_thinking_fundamentos"
visitados = {actual_id}

llamadas = {"n": 0}
ids_recibidos_en_retry = {}


def llamar_claude_falso(system, user_text, model, max_tokens=1500, componente=None):
    llamadas["n"] += 1
    ctx = json.loads(user_text)
    if llamadas["n"] == 2:
        # Verificamos que el retry SI incluyo el error y los ids validos literales
        assert "error_previo" in ctx, "el retry no incluyo error_previo"
        assert "ids_validos" in ctx and len(ctx["ids_validos"]) > 0, "el retry no incluyo ids_validos"
        ids_recibidos_en_retry["ids"] = ctx["ids_validos"]
    # En AMBOS intentos, el modelo "alucina" un id que no existe
    return json.dumps({
        "accion": "avanzar",
        "camino": ["id_totalmente_inventado_no_existe"],
        "pregunta_necesaria": True,
        "repregunta": None,
        "perfil_update": None,
    })


pm.llamar_claude = llamar_claude_falso

eventos = []
resultado = pm.interpretar_multi_salto(
    actual_id, graph, visitados,
    perfil_sesion="Quiero validar con clientes reales antes de construir nada.",
    texto_original="tengo miedo de construir algo que nadie use",
    pregunta_hecha="¿Qué te preocupa más?",
    respuesta_usuario="me preocupa hablar con clientes reales antes de construir",
    repreguntas_disponibles=True,
    preguntas_cache=preguntas_cache,
    ultimas_preguntas=[],
    registrar_evento=lambda e: eventos.append(e),
)

print("Llamadas a llamar_claude:", llamadas["n"])
print("ids_validos vistos en el retry (primeros 5):", ids_recibidos_en_retry["ids"][:5])
print("Resultado final:", resultado)
print("Eventos registrados:", eventos)

assert llamadas["n"] == 2, f"se esperaban exactamente 2 llamadas (intento + retry), hubo {llamadas['n']}"
assert resultado is not None, "no deberia devolver None (eso dispara el menu numerado visible)"
assert resultado["accion"] == "avanzar"
assert len(resultado["camino"]) == 1
candidato_elegido = resultado["camino"][0]
assert candidato_elegido in graph[actual_id]["nodos_siguientes"], "el candidato auto-elegido debe ser un sucesor real"
assert len(eventos) == 1 and eventos[0]["tipo"] == "fallback_auto"
assert eventos[0]["candidato_elegido"] == candidato_elegido
assert resultado.get("pregunta_adaptada"), "el fallback tier-2 debe traer una pregunta (aunque sea la cruda del cache)"

print("\nTODO OK: retry con error+ids_validos confirmado, auto-seleccion silenciosa funciona, evento registrado.")
print("Candidato auto-elegido por afinidad:", candidato_elegido, "->", graph[candidato_elegido]["titulo_concepto"])
