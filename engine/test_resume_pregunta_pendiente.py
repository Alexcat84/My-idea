# -*- coding: utf-8 -*-
"""Hotfix v2.1.2: verifica que la pregunta pendiente se persiste ANTES de
leer la respuesta del usuario, y que cargar_sesion la recupera intacta —
lo que permite a modo_nuevo_proyecto re-presentarla en --continuar en vez
de reanudar con respuesta_usuario=None (indistinguible del arranque de una
sesion nueva).

Bug real encontrado en una sesion en vivo sin guion (idea de tienda de
barrio con entregas a domicilio): al resumir con --continuar, el interprete
recibia respuesta_usuario=None y, sin ninguna senal de que el usuario
quisiera salir, decidia accion='salir' de todas formas — descartando en
silencio lo que el usuario estaba a punto de responder. La causa raiz:
guardar_sesion() nunca persistia la pregunta literal que estaba pendiente,
asi que --continuar no tenia forma de re-presentarla ni de leer una
respuesta real para ella.

Sin llamadas reales a la API (llamar_claude mockeado)."""
import json
import sys
import uuid

sys.path.insert(0, r"C:\Users\AlexDesk\Documents\I have an idea\engine")
import prototipo_motor as pm

graph = pm.cargar_grafo()
preguntas_cache = pm.cargar_preguntas_cache()
actual_id = "design_thinking_fundamentos"
nodo_siguiente = "mapeo_capas_diseno"
assert nodo_siguiente in graph, "el nodo de prueba debe existir en el grafo"

PREGUNTA_ESPERADA = "¿cual es tu mayor duda sobre esto?"


def _resultado_avanza():
    return json.dumps({
        "accion": "avanzar", "camino": [nodo_siguiente],
        "pregunta_necesaria": True, "pregunta_adaptada": PREGUNTA_ESPERADA,
        "repregunta": None, "perfil_update": None, "prioridad_declarada": None,
        "es_salto": False,
    })


# ejecutar_recorrido siempre inicializa su propio historial_mensajes=[] (no
# None), y el chequeo real es `historial_mensajes is not None` (linea 1559),
# no una verificacion de verdad — asi que SIEMPRE usa llamar_claude_conversacion,
# nunca llamar_claude, incluso en el primer turno. Hay que mockear la que
# realmente se llama o esto dispara una llamada real a la API.
pm.llamar_claude = lambda *a, **k: _resultado_avanza()
pm.llamar_claude_conversacion = lambda *a, **k: _resultado_avanza()

# --- Caso 1: EOF justo al pedir la respuesta a la pregunta recien impresa.
# guardar_sesion debe haber sido llamado con pregunta_hecha=esa pregunta
# ANTES de que leer_entrada falle (no despues, no nunca). ---
llamadas_guardado = []
guardar_sesion_original = pm.guardar_sesion


def guardar_sesion_espia(*args, **kwargs):
    llamadas_guardado.append(kwargs.get("pregunta_hecha"))
    return guardar_sesion_original(*args, **kwargs)


pm.guardar_sesion = guardar_sesion_espia
pm.leer_entrada = lambda prompt="": (_ for _ in ()).throw(pm.SesionInterrumpida())

session_id = uuid.uuid4().hex[:8]
try:
    pm.ejecutar_recorrido(
        graph, {}, preguntas_cache,
        actual_id, {actual_id}, [actual_id], ["conversado"],
        "Hace macetas, trabaja solo.", "quiero saber si mi idea tiene futuro",
        session_id, None, None,
    )
    raise AssertionError("ejecutar_recorrido deberia haber propagado SesionInterrumpida")
except pm.SesionInterrumpida:
    pass

assert PREGUNTA_ESPERADA in llamadas_guardado, (
    f"guardar_sesion debio recibir pregunta_hecha={PREGUNTA_ESPERADA!r} antes "
    f"del EOF; llamadas vistas: {llamadas_guardado!r}"
)
print("Caso 1 OK: la pregunta pendiente se persiste antes de leer la respuesta.")

# --- Caso 2: cargar_sesion recupera exactamente esa pregunta_hecha, lista
# para que modo_nuevo_proyecto la re-presente y lea una respuesta real en
# --continuar (en vez de arrancar el bucle con respuesta_usuario=None). ---
sesion_guardada = pm.cargar_sesion(session_id)
assert sesion_guardada.get("pregunta_hecha") == PREGUNTA_ESPERADA, (
    "cargar_sesion debe devolver la misma pregunta_hecha que se guardo"
)
print("Caso 2 OK: cargar_sesion recupera la pregunta_hecha guardada, lista para --continuar.")

print("\nTODO OK: hotfix v2.1.2 (resume ya no pierde la pregunta pendiente) verificado.")
