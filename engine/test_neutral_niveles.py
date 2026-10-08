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
# "el equipo" tambien da por hecho un equipo (la guarda de la tercera vuelta encontro 15 en el nivel 1)
for con_papel in ["¿Qué te preocupa más: que el equipo siga debatiendo o decidir rápido?",
                  "¿Cómo se entera el resto del equipo de lo que pasó?",
                  "¿Qué cambia en cómo trabaja el equipo?",
                  "¿Qué impide que el equipo las cumpla día a día?",
                  "Una vez que los departamentos sientan el impacto, ¿qué harías?",
                  "¿Cómo es la relación entre los responsables de equipo y quienes hacen el trabajo?",
                  "¿Lograrías que todo el equipo entienda esas ideas?"]:
    assert "papel" in [p["clase"] for p in nn.problemas(con_papel)], con_papel
# ...pero no la maquinaria, ni un equipo hipotetico, ni el equipo en condicional
for sin_papel in ["¿Hay equipos en tu taller que levanten cargas?",
                  "¿Necesitarías invertir en equipos nuevos?",
                  "¿Quieres armar un equipo de directores que te ayude?",
                  "Si llegas a tener un equipo, ¿cómo lo organizarías?",
                  "¿Usas equipo de protección cuando trabajas?"]:
    assert "papel" not in [p["clase"] for p in nn.problemas(sin_papel)], sin_papel
# VOSEO por regla general (cuarta vuelta, 8 oct 2026): -ás, -és, -ís de presente, salvo las palabras de siempre y el
# futuro. Las formas que se colaron en la tercera muestra: sentis, contactas, imaginas, descubris, decidis, contas.
for vos in ["¿Qué sentís cuando contactás a un cliente?", "¿Cómo imaginás tu primer año?", "¿Qué descubrís al probar?",
            "¿Cómo decidís el precio?", "¿A quién le contás tu idea?", "¿Qué preferís hacer primero?",
            "¿Cuánto gastás en envíos?", "¿Qué entendés por calidad?", "Si mirás tus números, ¿qué ves?"]:
    assert "voseo" in [p["clase"] for p in nn.problemas(vos)], vos
for tu in ["¿Qué es lo más importante para ti?", "¿Cómo estás hoy con tu idea?", "¿Qué harás después?",
           "¿En qué país vendes?", "¿Qué tendrás listo a través de este paso?", "¿Qué lograrás si funciona?",
           "Cuando estés listo, ¿qué harás además?", "¿Qué interés tiene?", "¿Qué podrás medir?", "¿Qué sabrás entonces?"]:
    assert "voseo" not in [p["clase"] for p in nn.problemas(tu)], tu
# PAPELES IMPLICITOS y plurales de grupo (cuarta vuelta): nunca tal cual
for implicito in ["¿Qué hace la gente que trabaja en él cuando algo falla?", "¿Hacia dónde quieres ir como organización?",
                  "¿Cómo lo muestras para que todos sepan en qué etapa está cada uno?", "¿Ya tienen claro qué quieren resolver?",
                  "¿Cómo convences a quien toma las decisiones?", "¿Qué hacen los responsables de equipos?",
                  "¿Qué pasa cuando alguien que trabaja contigo atiende a un cliente?", "¿Ya tenemos claro qué queremos?"]:
    assert nn.problemas(implicito) and not nn.nivel_1(implicito), implicito
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
# el condicional insertado se cierra con su coma si lo que sigue no es puntuacion (piloto del 8 oct: "si lo tienes no vea")
B3 = "¿Qué pasa si tu equipo no ve por qué importa?"
ok, err = nn.aplicar_cambios(B3, [{"original": "tu equipo", "nuevo": "tu equipo, si lo tienes"}])
assert (ok, err) == ("¿Qué pasa si tu equipo, si lo tienes, no ve por qué importa?", None), ok
B4 = "¿Qué opina tu equipo?"
ok, err = nn.aplicar_cambios(B4, [{"original": "tu equipo", "nuevo": "tu equipo, si lo tienes"}])
assert ok == "¿Qué opina tu equipo, si lo tienes?", ok
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


# --- 5. correccion declarada de una BASE (voseo, ingles, forma rota), con la misma maquina de edicion minima ----------
BV = "¿Qué sentís cuando contactás a tu primer cliente?"
C_BV = [{"original": "sentís", "nuevo": "sientes"}, {"original": "contactás", "nuevo": "contactas"}]
r = nn.corregir_base(cliente([json.dumps({"cambios": C_BV})]), cliente([json.dumps({"mismo_sentido": True, "motivo": "igual"})]),
                     "n2", BV, GRAFO, extras=[])
assert r["corregida"] == "¿Qué sientes cuando contactas a tu primer cliente?" and r["clases"] == ["voseo"], r
# una forma rota que trae el lector (no la detectan las reglas): el fragmento lo marca el lector y solo ese se toca
BR = "¿Cómo vas a figura out el precio de tu servicio?"
r = nn.corregir_base(cliente([json.dumps({"cambios": [{"original": "figura out", "nuevo": "averiguar"}]})]),
                     cliente([json.dumps({"mismo_sentido": True, "motivo": "igual"})]), "n2", BR, GRAFO,
                     extras=[{"clase": "forma_rota", "fragmento": "figura out"}])
assert r["corregida"] == "¿Cómo vas a averiguar el precio de tu servicio?" and r["clases"] == ["forma_rota"], r
# solo las palabras del problema: un fragmento que va mas alla del problema se rechaza y la base NO se toca
r = nn.corregir_base(cliente([json.dumps({"cambios": [{"original": "figura out el precio", "nuevo": "bajar el precio"}]})] * 2),
                     cliente([]), "n2", BR, GRAFO, extras=[{"clase": "forma_rota", "fragmento": "figura out"}])
assert r["corregida"] is None and r["motivo"] == "fragmento_mas_que_el_problema", r
# si el juez independiente duda, la base no se toca
r = nn.corregir_base(cliente([json.dumps({"cambios": C_BV})] * 2), cliente([json.dumps({"mismo_sentido": False, "motivo": "x"})] * 2),
                     "n2", BV, GRAFO, extras=[])
assert r["corregida"] is None and r["motivo"] == "juez_independiente", r
# una base sin nada que corregir no llama a nadie
r = nn.corregir_base(cliente([]), cliente([]), "n2", LIMPIA, GRAFO, extras=[])
assert r["corregida"] is None and r["motivo"] == "sin_problemas_de_base", r
# una forma rota larga (hasta 12 palabras) cabe en la segunda pasada, con las mismas comprobaciones y el juez
BL = "¿O todos los que importan en la decisión eres tú y el que usa el producto?"
FR = "los que importan en la decisión eres tú y el que usa"  # 12 palabras
C_BL = [{"original": FR, "nuevo": "los que importan en la decisión son tú y quien usa"}]
assert nn.corregir_base(cliente([json.dumps({"cambios": C_BL})] * 2), cliente([]), "n2", BL, GRAFO,
                        extras=[{"clase": "forma_rota", "fragmento": FR}])["motivo"] == "fragmento_largo"
r = nn.corregir_base(cliente([json.dumps({"cambios": C_BL})]), cliente([json.dumps({"mismo_sentido": True, "motivo": "igual"})]),
                     "n2", BL, GRAFO, extras=[{"clase": "forma_rota", "fragmento": FR}], max_frag=12)
assert r["corregida"] == "¿O todos los que importan en la decisión son tú y quien usa el producto?", r
# la misma palabra de voseo repetida se cambia en todas sus apariciones (antes se rechazaba por "fragmento_repetido")
BR2 = "¿Ya tenés claro qué querés y tenés el dinero para empezar?"
C_R2 = [{"original": "tenés", "nuevo": "tienes"}, {"original": "querés", "nuevo": "quieres"}]
r = nn.corregir_base(cliente([json.dumps({"cambios": C_R2})]), cliente([json.dumps({"mismo_sentido": True, "motivo": "igual"})]),
                     "n2", BR2, GRAFO, extras=[])
assert r["corregida"] == "¿Ya tienes claro qué quieres y tienes el dinero para empezar?", r
# el pronombre "vos" va con la palabra de antes: tras preposicion pasa a "ti" ("de vos" -> "de ti"), si no a "tu"
BP = "¿Deben obtenerlos de vos o de proveedores que vos designes?"
frags = [p["fragmento"] for p in nn.problemas(BP) if p["clase"] == "voseo"]
assert "de vos" in frags and "que vos" in frags, frags
C_BP = [{"original": "de vos", "nuevo": "de ti"}, {"original": "que vos", "nuevo": "que tú"}]
r = nn.corregir_base(cliente([json.dumps({"cambios": C_BP})]), cliente([json.dumps({"mismo_sentido": True, "motivo": "igual"})]),
                     "n2", BP, GRAFO, extras=[])
assert r["corregida"] == "¿Deben obtenerlos de ti o de proveedores que tú designes?", r
# "vos" nunca se cambia en bloque: un unico reemplazo "vos" -> "tu" para todas las apariciones se rechaza
assert nn.aplicar_cambios(BP, [{"original": "vos", "nuevo": "tú"}], probs=nn.problemas(BP), editables=nn.CLASES_DE_BASE)[1] in (
    "fragmento_repetido", "fragmento_sin_problema")
assert "Juzga SOLO los cambios" in nn.SYSTEM_JUEZ_CORRECCION
print("OK correccion declarada de bases: voseo y formas rotas por edicion minima verificada; si duda, no se toca")
print("\nTODO OK")
