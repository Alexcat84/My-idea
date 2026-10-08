# -*- coding: utf-8 -*-
"""SEGURIDAD MAXIMA DE SENTIDO (decision del fundador, corrida final, 8 oct 2026): la neutral deja de reescribirse
libremente. Tres niveles, en orden:
  1. BASE TAL CUAL si la base no supone ningun papel y pasa todas las guardas.
  2. EDICION MINIMA: solo cambian las palabras exactas del problema; comprobaciones obligatorias (diferencia palabra por
     palabra, terminos clave, polaridad y un juez independiente de otro modelo).
  3. PLANTILLA SEGURA si la edicion no supera TODO (la neutral queda vacia con nivel 3 y la app pone la plantilla).
Todo con clientes falsos: ninguna llamada a la API real."""
import json
import os
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import neutral_niveles as nn  # noqa: E402


# --- 1. NIVEL 1: base tal cual ----------------------------------------------------------------------------------------
LIMPIA = "¿Qué es lo que más te preocupa hoy de tu idea: el precio o la calidad de lo que ofreces?"
assert nn.problemas(LIMPIA) == []
assert nn.nivel_1(LIMPIA) is True
for con_problema, clase in [
    ("¿Cómo lo hablas con tu jefe antes de decidir?", "papel"),
    ("¿Qué opina tu equipo de esta idea?", "papel"),
    ("¿Cómo lo deciden ustedes en el proyecto?", "grupo"),
    ("¿Cómo sabríais ambos que funciona?", "grupo"),
    ("¿Qué tenés pensado para empezar?", "voseo"),
    ("¿Lo haces tú misma o con ayuda?", "genero"),
    ("¿Qué dice el libro sobre tu caso?", "voz_de_libro"),
]:
    assert clase in [p["clase"] for p in nn.problemas(con_problema)], (con_problema, nn.problemas(con_problema))
    assert nn.nivel_1(con_problema) is False, con_problema
print("OK nivel 1: la base sin papeles ni defectos pasa tal cual; con cualquier problema, no")


# --- 2. aplicar la edicion minima -------------------------------------------------------------------------------------
B = "Cuando lo hablas con tu equipo, ¿qué es lo que más te preocupa de vender franquicias en otro país?"
ok, err = nn.aplicar_cambios(B, [{"original": "con tu equipo", "nuevo": "con quienes trabajan contigo, si los tienes"}])
assert err is None and ok == "Cuando lo hablas con quienes trabajan contigo, si los tienes, ¿qué es lo que más te preocupa de vender franquicias en otro país?"
# el fragmento tiene que estar en la base, una sola vez
assert nn.aplicar_cambios(B, [{"original": "con tus socios", "nuevo": "x"}])[1] == "fragmento_inexistente"
# el fragmento tiene que contener el problema: no se puede tocar otra cosa
assert nn.aplicar_cambios(B, [{"original": "vender franquicias", "nuevo": "vender tu negocio"}])[1] == "fragmento_sin_problema"
# el fragmento es corto (las palabras del problema, no la frase entera)
assert nn.aplicar_cambios(B, [{"original": "Cuando lo hablas con tu equipo, ¿qué es lo que más te preocupa", "nuevo": "y"}])[1] == "fragmento_largo"
print("OK aplicar_cambios: solo fragmentos que existen, cortos y que contienen el problema")


# --- 3. las comprobaciones obligatorias de la edicion -----------------------------------------------------------------
NODO = {"etiqueta_arbol": "Vende Franquicias Fuera", "titulo_concepto": "Franquicia internacional"}
CAMBIO = [{"original": "con tu equipo", "nuevo": "con quienes trabajan contigo, si los tienes"}]
BUENA = "Cuando lo hablas con quienes trabajan contigo, si los tienes, ¿qué es lo que más te preocupa de vender franquicias en otro país?"
assert nn.comprobar_edicion(B, BUENA, CAMBIO, NODO) is None
# diferencia palabra por palabra: fuera del fragmento permitido no cambia nada
assert nn.comprobar_edicion(B, BUENA.replace("otro país", "el extranjero"), CAMBIO, NODO) == "cambio_fuera_del_fragmento"
# el caso del fundador: "vender franquicias" convertido en "vender tu negocio" se rechaza (termino clave perdido)
CAMBIO_MALO = [{"original": "con tu equipo, ¿qué es lo que más te preocupa de vender franquicias",
                "nuevo": "si trabajas con otras personas, ¿qué es lo que más te preocupa de vender tu negocio"}]
MALA = "Cuando lo hablas si trabajas con otras personas, ¿qué es lo que más te preocupa de vender tu negocio en otro país?"
assert nn.comprobar_edicion(B, MALA, CAMBIO_MALO, NODO) in ("termino_clave_perdido", "fragmento_largo")
assert nn.terminos_clave(B, NODO) and "franquic" in nn.terminos_clave(B, NODO)
assert nn.termino_perdido(B, "¿Qué te preocupa de vender tu negocio en otro país?", NODO) == "franquic"
# polaridad: ni negaciones ni limites nuevos o quitados, ni cifras ni plazos
B2 = "Si tu jefe solo aprueba dos proyectos al año, ¿cuál eliges primero?"
C2 = [{"original": "tu jefe", "nuevo": "quien decide por encima de ti, si lo hay,"}]
assert nn.comprobar_edicion(B2, "Si quien decide por encima de ti, si lo hay, solo aprueba dos proyectos al año, ¿cuál eliges primero?", C2, {}) is None
assert nn.polaridad_cambiada(B2, "Si quien decide por encima de ti no aprueba dos proyectos al año, ¿cuál eliges primero?")
assert nn.polaridad_cambiada(B2, "Si quien decide aprueba dos proyectos al año, ¿cuál eliges primero?")  # quito "solo"
assert nn.polaridad_cambiada(B2, "Si quien decide solo aprueba tres proyectos al año, ¿cuál eliges primero?")  # cifra
assert nn.polaridad_cambiada(B2, "Si quien decide solo aprueba dos proyectos al mes, ¿cuál eliges primero?")  # plazo
assert not nn.polaridad_cambiada(B2, "Si quien decide, si lo hay, solo aprueba dos proyectos al año, ¿cuál eliges primero?")
# la neutral no puede seguir suponiendo el papel fuera de un condicional
assert nn.comprobar_edicion(B, "Cuando lo hablas con quienes trabajan contigo, ¿qué es lo que más te preocupa de vender franquicias en otro país?",
                            [{"original": "con tu equipo", "nuevo": "con quienes trabajan contigo"}], NODO) == "problema_sin_resolver"
print("OK comprobaciones: diferencia palabra por palabra, terminos clave (franquicias), polaridad y problema resuelto")


# --- 4. el sistema completo, con clientes falsos -------------------------------------------------------------------------
def cliente(respuestas):
    cola = list(respuestas)

    def create(**kw):
        texto = cola.pop(0)
        return SimpleNamespace(content=[SimpleNamespace(type="text", text=texto)], stop_reason="end_turn",
                               usage=SimpleNamespace(input_tokens=100, output_tokens=10, cache_read_input_tokens=0,
                                                     cache_creation_input_tokens=0))
    return SimpleNamespace(messages=SimpleNamespace(create=create), cola=cola)


GRAFO = {"n1": NODO, "n2": {"etiqueta_arbol": "Precio y Calidad"}, "n3": NODO}
# n1: base con papel -> edicion valida + juez de acuerdo -> nivel 2
r = nn.neutral_por_niveles(cliente([json.dumps({"cambios": CAMBIO})]), cliente([json.dumps({"mismo_sentido": True, "motivo": "igual"})]), "n1", B, GRAFO)
assert (r["nivel"], r["texto"]) == (2, BUENA), r
# n2: base limpia -> nivel 1 sin llamar a nadie
vacio = cliente([])
r = nn.neutral_por_niveles(vacio, vacio, "n2", LIMPIA, GRAFO)
assert (r["nivel"], r["texto"], r["tokens_in"]) == (1, LIMPIA, 0), r
# n3: el juez independiente duda -> se reintenta una vez y, si vuelve a dudar, plantilla (nivel 3, sin texto)
juez_no = json.dumps({"mismo_sentido": False, "motivo": "cambia el foco"})
r = nn.neutral_por_niveles(cliente([json.dumps({"cambios": CAMBIO})] * 2), cliente([juez_no] * 2), "n3", B, GRAFO)
assert (r["nivel"], r["texto"]) == (3, None) and r["motivo"] == "juez_independiente", r
# una edicion que pierde el termino clave nunca llega al juez y termina en plantilla
r = nn.neutral_por_niveles(cliente([json.dumps({"cambios": CAMBIO_MALO})] * 2), cliente([]), "n3", B, GRAFO)
assert r["nivel"] == 3, r
# el juez es un modelo distinto del editor
assert nn.MODELO_EDITOR != nn.MODELO_JUEZ
print("OK niveles: 1 sin llamadas, 2 con edicion verificada y juez de acuerdo, 3 ante cualquier duda")
print("\nTODO OK")
