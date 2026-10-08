# -*- coding: utf-8 -*-
"""PRINCIPIO 2 (decision del fundador, 28 sep 2026): nada se elimina ni se cambia. El generador de la cache solo
AÑADE: la version neutral de cada base (campo aparte, pregunta_neutral) y la pregunta de los nodos con siguientes que
no la tienen. La base no se toca jamas. Todo con un cliente falso: ninguna llamada a la API real hasta la corrida
final (regla del fundador, 28 sep 2026). Las funciones que se prueban reciben el cliente; ninguna mira ANTHROPIC_API_KEY
(la guardia vive solo en main), asi que el veredicto no depende de los secretos del ambiente."""
import json
import os
import re
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_question_cache as bqc

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# --- 1. La regla unica es la misma letra que la del producto ---------------------------------------------------------
ts = open(os.path.join(RAIZ, "web", "lib", "reglaContextoUsuario.ts"), encoding="utf-8").read()
cuerpo = ts[ts.index("REGLA_CONTEXTO_USUARIO =") : ts.index(";", ts.index("REGLA_CONTEXTO_USUARIO ="))]
regla_ts = "".join(re.findall(r'"((?:[^"\\]|\\.)*)"', cuerpo))
assert regla_ts == bqc.REGLA_CONTEXTO_USUARIO, "la regla del generador difiere de web/lib/reglaContextoUsuario.ts"
assert bqc.REGLA_CONTEXTO_USUARIO in bqc.SYSTEM_NEUTRAL
assert bqc.SYSTEM_PREGUNTA_CON_REGLA.endswith(bqc.REGLA_CONTEXTO_USUARIO)
assert bqc.SYSTEM_PREGUNTA_CON_REGLA.startswith(bqc.SYSTEM_PREGUNTA)
print("OK regla unica: misma letra que el producto, en los dos generadores")


# --- 2. comprobar_neutral ---------------------------------------------------------------------------------------------
BASE = "¿Qué le dirías a tu propio jefe si te pide un informe de avance?"
assert len(BASE) == 64
assert bqc.comprobar_neutral(BASE, "¿Qué le contarías a quien sigue tu avance?") is None
# tuteo que se parece al voseo salvo la tilde: NO es voseo
assert bqc.comprobar_neutral(BASE, "Mira tus números: ¿qué sabes hoy de lo que buscas y necesitas?") is None
assert bqc.comprobar_neutral(BASE, "¿Qué haces cuando tienes dudas?") is None
# voseo: no pasa
for vos in ["¿Qué tenés pensado?", "¿Qué sabés de tu cliente?", "Mirá, ¿qué harías?", "¿Vos qué buscás?", "¿Qué podes hacer?"]:
    assert bqc.comprobar_neutral(BASE, vos) == "voseo", vos
assert bqc.comprobar_neutral(BASE, "Cuéntame tu avance.") == "no_es_pregunta"
assert bqc.comprobar_neutral(BASE, "¿A quién le cuentas — si hay alguien — cómo vas?") == "guion_largo"
assert bqc.comprobar_neutral(BASE, "  ") == "vacia"
# Tope a mano: max(2 x 64, 64 + 200) = max(128, 264) = 264 caracteres.
assert bqc.comprobar_neutral(BASE, "¿" + "a" * 262 + "?") is None  # 1 + 262 + 1 = 264
assert bqc.comprobar_neutral(BASE, "¿" + "a" * 263 + "?") == "demasiado_larga"  # 265
print("OK comprobar_neutral: tuteo pasa, voseo/guion/largo/vacia/no-pregunta no")


# --- 2b. los cuatro patrones de la muestra que NO PASO (decision del fundador, 8 oct 2026) ---------------------------
# La muestra ciega (semilla 20261008) sostuvo 49 de 200: la neutral añadia una segunda peticion, perdia el contexto
# propio de la base, marcaba el genero ("tu misma, si trabajas sola") y metia personas sin condicional. La regla de la
# casa: al lector se le habla en masculino generico. La causa del genero estaba en las propias instrucciones, escritas
# en femenino ("si es dueña", "si trabaja sola", "ella misma").
for femenino in ["dueña", "trabaja sola", "ella misma", "puede estar sola"]:
    assert femenino not in bqc.REGLA_CONTEXTO_USUARIO, f"la regla unica habla en femenino: {femenino}"
    assert femenino not in bqc.SYSTEM_NEUTRAL, f"las instrucciones de la neutral hablan en femenino: {femenino}"
assert "masculino genérico" in bqc.REGLA_CONTEXTO_USUARIO
for regla in ["segunda petición", "contexto propio", "masculino genérico", "en condicional", "dentro de la misma pregunta",
              "NUNCA termines con"]:
    assert regla in bqc.SYSTEM_NEUTRAL, f"falta la regla: {regla}"
# el genero marcado al hablarle a la persona no pasa
B2 = "¿Cómo te organizas hoy para atender a tus clientes?"
for g in ["¿Lo haces tú misma o con ayuda?", "¿Trabajas sola o con alguien?", "¿Lo decides por ti misma?",
          "¿Te sientes preparada para atenderlos?", "¿Estás segura de cómo atenderlos?", "¿Lo haces tú mismo/a?"]:
    assert bqc.comprobar_neutral(B2, g) == "genero", g
# el masculino generico y los usos que no se refieren a la persona SI pasan
for ok in ["¿Lo haces tú mismo o con ayuda?", "¿Trabajas solo o con alguien?", "¿Cómo se ve tu lista de clientes?",
           "¿Lo haces una sola vez o cada semana?", "¿Qué tan segura es la forma en que guardas sus datos?",
           # los tres falsos positivos del primer conteo (preguntas base reales): posesivo y tercera persona
           "¿Compartirías lo que aprendiste con otros que están en tu misma situación?",
           "¿Te preocupa que otros en tu misma industria sigan igual?",
           "¿Por qué pensaste que esa persona podría estar interesada en comprar?"]:
    assert bqc.comprobar_neutral(B2, ok) is None, ok
# una segunda peticion que la base no tiene no pasa (mas preguntas que la base)
assert bqc.comprobar_neutral(B2, "¿Cómo te organizas hoy? ¿Y cómo lo harías con alguien por encima?") == "segunda_peticion"
# ...ni una frase añadida despues de la pregunta (el piloto del 8 oct: "Si trabajas solo, dime cual...")
assert bqc.comprobar_neutral(B2, "¿Cómo te organizas hoy? Si trabajas solo, dime cuál te preocupa más.") == "segunda_peticion"
assert bqc.comprobar_neutral(B2, "¿Cómo te organizas hoy? (Si trabajas solo, piensa en ti mismo.)") == "segunda_peticion"
B_COLA = "¿Cómo te organizas hoy para atender a tus clientes? Cuéntame un ejemplo."
assert bqc.comprobar_neutral(B_COLA, "¿Cómo te organizas para atender a tus clientes? Cuéntame un caso.") is None
B_DOS = "¿Cómo atiendes hoy a tus clientes? ¿Qué te gustaría cambiar?"
assert bqc.comprobar_neutral(B_DOS, "¿Cómo los atiendes hoy? ¿Qué cambiarías?") is None
# personas sin condicional y contexto propio perdido (el segundo piloto del 8 oct): tambien se rechazan al generar
B_EQ = "Antes de trabajar con tu equipo en esta estrategia, ¿sabes cómo piensan tus colaboradores?"
assert bqc.comprobar_neutral(B_EQ, "Antes de trabajar en esta estrategia con las personas que te acompañan, ¿sabes cómo piensan?") == "personas_sin_condicional"
assert bqc.comprobar_neutral(B_EQ, "Antes de trabajar en esta estrategia, si trabajas con otras personas, ¿sabes cómo piensan?") is None
B_FR = "¿Qué pasos sigues hoy con cada persona interesada en tu franquicia?"
assert bqc.comprobar_neutral(B_FR, "¿Qué pasos sigues hoy con cada persona interesada en lo que ofreces?") == "contexto_perdido"
assert bqc.comprobar_neutral(B_FR, "¿Qué pasos sigues hoy con quien se interesa en tu franquicia?") is None
# el generador y la guarda usan la MISMA definicion
import importlib.util as _u
_sp = _u.spec_from_file_location("vc", os.path.join(RAIZ, "scripts", "corrida_final", "verificar_cache.py"))
_vc = _u.module_from_spec(_sp); _sp.loader.exec_module(_vc)
assert _vc.patrones is bqc.patrones_neutral
print("OK los cuatro patrones: instrucciones en masculino generico con sus reglas; genero y segunda peticion no pasan")


# --- cliente falso ----------------------------------------------------------------------------------------------------
class ClienteFalso:
    def __init__(self, salidas):
        self.salidas = list(salidas)  # (texto, stop_reason)
        self.llamadas = []
        self.messages = self

    def create(self, **kw):
        self.llamadas.append(kw)
        texto, stop = self.salidas.pop(0)
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=texto)],
            usage=SimpleNamespace(input_tokens=300, output_tokens=40),
            stop_reason=stop,
        )


def nodo(titulo, siguientes=(), deprecado=False):
    n = {"titulo_concepto": titulo, "etiqueta_arbol": titulo.lower(), "resumen_teorico": "resumen de " + titulo,
         "nodos_siguientes": list(siguientes), "condiciones_activacion": ["cuando aplica"]}
    if deprecado:
        n["deprecado"] = True
    return n


graph = {
    "a": nodo("Informe al jefe", ["s"]),
    "t": nodo("Tema cortado", ["s"]),
    "b": nodo("Deprecado", ["s"], deprecado=True),
    "c": nodo("Ya neutral", ["s"]),
    "x": nodo("Sin pregunta", ["s"]),
    "s": nodo("Siguiente"),
}


def cache_inicial():
    return {
        "a": {"pregunta": BASE, "candidatos": ["s"]},
        "t": {"pregunta": "¿Qué tema quieres cortar?", "candidatos": ["s"]},
        "b": {"pregunta": "¿Deprecada?", "candidatos": ["s"]},
        "c": {"pregunta": "¿Ya neutral?", "pregunta_neutral": "¿Ya neutral, de verdad?", "candidatos": ["s"]},
        "d": {"pregunta": "¿De un nodo que ya no existe?", "candidatos": []},
    }


# --- 3. correr_neutrales ----------------------------------------------------------------------------------------------
cache = cache_inicial()
assert bqc.objetivos_neutrales(cache, graph) == ["a", "t"]  # ni deprecado, ni ya hecho, ni nodo inexistente
cliente = ClienteFalso([
    (json.dumps({"pregunta_neutral": "¿Qué le contarías a quien sigue tu avance si te lo pide? Contame."}), "end_turn"),  # a: voseo
    (json.dumps({"pregunta_neutral": "¿Qué le contarías a quien sigue tu avance si te pide un informe?"}), "end_turn"),  # a: bien
    ('{"pregunta_neutral": "¿Qué tema', "max_tokens"),  # t: cortada
    ('{"pregunta_neutral": "¿Qué tema', "max_tokens"),  # t: cortada otra vez
])
guardados = []
r = bqc.correr_neutrales(cliente, cache, graph, guardar=lambda c: guardados.append(json.loads(json.dumps(c))))
# A mano: 4 llamadas pagadas (2 de 'a', 2 de 't'), cada una 300 de entrada y 40 de salida.
#   tokens_in  = 4 x 300 = 1200
#   tokens_out = 4 x 40  = 160
# 'a' queda hecha al segundo intento; 't' falla las dos veces (reintentos=1 -> 2 intentos) y se reporta.
assert r["hechas"] == 1
assert r["fallidas"] == [("t", "respuesta cortada por tope de tokens")]
assert r["tokens_in"] == 1200 and r["tokens_out"] == 160, r
assert len(cliente.llamadas) == 4
assert cache["a"] == {"pregunta": BASE, "candidatos": ["s"],
                      "pregunta_neutral": "¿Qué le contarías a quien sigue tu avance si te pide un informe?"}
assert cache["t"] == cache_inicial()["t"]  # sin neutral: nada inventado
for nid in ["b", "c", "d"]:
    assert cache[nid] == cache_inicial()[nid], nid  # intactas
for nid, e in cache.items():
    assert e["pregunta"] == cache_inicial()[nid]["pregunta"], nid  # NINGUNA base cambia
assert guardados and guardados[-1] == cache  # se guarda al final
# lo que viaja: la base, el concepto por su etiqueta y los siguientes por su etiqueta; system = SYSTEM_NEUTRAL
enviado = json.loads(cliente.llamadas[0]["messages"][0]["content"])
assert enviado == {"pregunta_base": BASE, "concepto": {"etiqueta": "informe al jefe", "resumen": "resumen de Informe al jefe"},
                   "temas_siguientes": ["siguiente"]}
assert cliente.llamadas[0]["system"][0]["text"] == bqc.SYSTEM_NEUTRAL
# reanudable: una segunda pasada solo trabaja lo que falta ('t')
assert bqc.objetivos_neutrales(cache, graph) == ["t"]
print("OK correr_neutrales: añade sin tocar la base, reintenta, reporta el fallo y cuenta todo lo pagado")


# --- 4. correr_faltantes ----------------------------------------------------------------------------------------------
cache = cache_inicial()
assert bqc.faltantes(cache, graph) == ["x"]  # 'b' deprecado no; los que tienen base no
cliente = ClienteFalso([(json.dumps({"pregunta": "¿Qué te gustaría ordenar primero?"}), "end_turn")])
r = bqc.correr_faltantes(cliente, cache, graph)
# A mano: 1 llamada -> 300 de entrada, 40 de salida.
# El cliente falso no trae tokens de cache: 0 leidos, 0 escritos.
assert r == {"hechas": 1, "fallidas": [], "tokens_in": 300, "tokens_out": 40, "cache_read": 0, "cache_write": 0}, r
assert cache["x"] == {"pregunta": "¿Qué te gustaría ordenar primero?", "candidatos": ["s"]}
assert cliente.llamadas[0]["system"][0]["text"] == bqc.SYSTEM_PREGUNTA_CON_REGLA  # nace con la regla unica
for nid, e in cache_inicial().items():
    assert cache[nid] == e, nid  # nada de lo que habia cambia
# una salida cortada no se guarda nunca
cache = cache_inicial()
r = bqc.correr_faltantes(ClienteFalso([('{"pregunta": "¿Qué te', "max_tokens")]), cache, graph)
assert r["hechas"] == 0 and r["fallidas"] == [("x", "respuesta cortada por tope de tokens")]
assert "x" not in cache
print("OK correr_faltantes: solo los que no tienen pregunta, con la regla unica, nunca una salida cortada")

# --- 5. neutrales de las preguntas de ENTRADA (corrida final, 8 oct 2026) -------------------------------------------
# Decision del fundador: se generan las neutrales de TODAS las preguntas, base y de entrada. La de entrada va a su campo
# aparte (pregunta_entrada_neutral); la entrada y la base no se tocan.
ENT = "¿Tu equipo ya sabe a quién acudir cuando algo se atasca?"
graph_e = {**graph, "e": nodo("Puerta", ["s"]), "f": nodo("Puerta hecha", ["s"]), "g": nodo("Puerta deprecada", ["s"], deprecado=True)}
cache = {
    "e": {"pregunta": BASE, "pregunta_entrada": ENT, "candidatos": ["s"]},
    "f": {"pregunta": "¿F?", "pregunta_entrada": "¿Entrada F?", "pregunta_entrada_neutral": "¿Entrada F, neutral?", "candidatos": ["s"]},
    "g": {"pregunta": "¿G?", "pregunta_entrada": "¿Entrada G?", "candidatos": ["s"]},
}
ENTRADA = dict(origen="pregunta_entrada", destino="pregunta_entrada_neutral")
assert bqc.objetivos_neutrales(cache, graph_e, **ENTRADA) == ["e"]  # ni la hecha ni la deprecada
cliente = ClienteFalso([(json.dumps({"pregunta_neutral": "¿Quién sabe hoy a quién acudir cuando algo se atasca?"}), "end_turn")])
r = bqc.correr_neutrales(cliente, cache, graph_e, **ENTRADA)
# A mano: 1 llamada -> 300 de entrada, 40 de salida.
assert r == {"hechas": 1, "fallidas": [], "tokens_in": 300, "tokens_out": 40, "cache_read": 0, "cache_write": 0}, r
assert cache["e"] == {"pregunta": BASE, "pregunta_entrada": ENT, "candidatos": ["s"],
                      "pregunta_entrada_neutral": "¿Quién sabe hoy a quién acudir cuando algo se atasca?"}
assert "pregunta_neutral" not in cache["e"]  # la neutral de la base es otra cosa y no se toca aqui
assert json.loads(cliente.llamadas[0]["messages"][0]["content"])["pregunta_base"] == ENT  # se neutraliza la ENTRADA
# por defecto, el modo de siempre (las bases)
assert bqc.objetivos_neutrales(cache, graph_e) == ["e", "f"]
print("OK neutrales de entrada: campo aparte, ni la entrada ni la base cambian, el modo de las bases sigue igual")

# --- 6. el modelo y su coste (cambio de modelos, 8 oct 2026) ------------------------------------------------------
assert bqc.MODEL == "claude-haiku-5-5"
assert bqc.PARAMETROS_MODELO == {"thinking": {"type": "disabled"}}
cliente = ClienteFalso([(json.dumps({"pregunta_neutral": "¿Qué le contarías a quien sigue tu avance?"}), "end_turn")])
bqc.correr_neutrales(cliente, {"a": {"pregunta": BASE, "candidatos": ["s"]}}, graph)
assert cliente.llamadas[0]["thinking"] == {"type": "disabled"} and cliente.llamadas[0]["model"] == "claude-haiku-5-5"
# A mano: 1.000.000 de entrada x 0,10 + 100.000 de salida x 0,50 + 2.000.000 leidos x 0,01 + 400.000 escritos x 0,125
#   = 0,10 + 0,05 + 0,02 + 0,05 = 0,22 USD
r = {"tokens_in": 1_000_000, "tokens_out": 100_000, "cache_read": 2_000_000, "cache_write": 400_000}
assert abs(bqc.costo_usd(r) - 0.22) < 1e-9, bqc.costo_usd(r)
print("OK modelo: Haiku 5.5 sin razonamiento por defecto; el coste cuenta la cache")

print("\nTODO OK")
