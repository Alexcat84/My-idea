# -*- coding: utf-8 -*-
"""Las barandas del extractor de mundos (scripts/extraer_mundo.py).

Todo lo que se prueba aqui es PURO: no toca la API ni gasta un token. Son
justo las revisiones que evitan pagar una corrida entera para descubrir al
final que los nodos venian mal.

Dos de estas pruebas cubren trampas ya cazadas en corridas anteriores:
  - el bloque de pensamiento, que rompe a quien lee content[0];
  - el corte por techo de tokens, que no se arregla reintentando contra el
    mismo techo.
"""
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from extraer_mundo import (  # noqa: E402
    PALABRAS_RESUMEN,
    TECHOS,
    _texto_de,
    llamar,
    revisar_nodo,
    tirada_literal,
)

FRAGMENTO = (
    "Inventory management is the art of having the right amount of stock at the "
    "right time in the right place, and it always begins with knowing exactly "
    "what you already own before you sign another purchase order with a supplier."
)


def nodo_base(**cambios):
    n = {
        "node_id": "cuenta_lo_que_ya_tienes",
        "fase_proyecto": "planificacion",
        "titulo_concepto": "Cuenta lo que ya tienes",
        "fuente": "Max Muller, Essentials of Inventory Management",
        # 96 palabras, en palabras propias
        "resumen_teorico": " ".join(["palabra"] * 96),
        "pasos_accionables": ["Cuenta tu bodega hoy.", "Anota lo que sobra."],
        "entregable_esperado": "Una lista de lo que tienes en la mano.",
        "nodos_previos": ["Elige a quien le compras"],
        "nodos_siguientes": ["Pide solo lo que falta"],
        "condiciones_activacion": ["Compras de nuevo sin saber que te queda."],
        "etiqueta_arbol": "Cuenta lo que Tienes",
    }
    n.update(cambios)
    return n


def test_nodo_limpio_pasa():
    assert revisar_nodo(nodo_base(), FRAGMENTO, set()) == []
    print("  ok: un nodo conforme no levanta ninguna falla")


def test_copia_literal():
    # 12 palabras seguidas de la fuente, incrustadas en un resumen propio.
    copiado = ("Antes de comprar mas conviene saber lo tuyo. " +
               "having the right amount of stock at the right time in the right " +
               "place es la idea. " + " ".join(["relleno"] * 70))
    fallas = revisar_nodo(nodo_base(resumen_teorico=copiado), FRAGMENTO, set())
    assert any("copia literal" in f for f in fallas), fallas
    # y el destilado en palabras propias NO se marca
    assert tirada_literal(" ".join(["palabra"] * 96), FRAGMENTO) is None
    print("  ok: la copia literal se caza y el destilado no da falso positivo")


def test_campo_renegado_y_obligatorio():
    # 'familia' es EL campo que el validador rechaza y que los documentos
    # viejos de arranque pedian. No puede volver a colarse.
    fallas = revisar_nodo(nodo_base(familia="compras"), FRAGMENTO, set())
    assert any("lista blanca" in f and "familia" in f for f in fallas), fallas

    sin_entregable = nodo_base()
    del sin_entregable["entregable_esperado"]
    fallas = revisar_nodo(sin_entregable, FRAGMENTO, set())
    assert any("entregable_esperado" in f for f in fallas), fallas
    print("  ok: 'familia' se rechaza y el entregable ausente se caza")


def test_fase_inventada():
    fallas = revisar_nodo(nodo_base(fase_proyecto="operacion"), FRAGMENTO, set())
    assert any("fase_proyecto invalida" in f for f in fallas), fallas
    print("  ok: solo entran las 4 fases del motor")


def test_largo_del_resumen():
    corto = revisar_nodo(nodo_base(resumen_teorico="tres palabras solas"), FRAGMENTO, set())
    assert any("resumen_teorico de 3 palabras" in f for f in corto), corto
    largo = revisar_nodo(nodo_base(resumen_teorico=" ".join(["x"] * 200)), FRAGMENTO, set())
    assert any(f"{PALABRAS_RESUMEN[1]}" in f for f in largo), largo
    print(f"  ok: el resumen vive entre {PALABRAS_RESUMEN[0]} y {PALABRAS_RESUMEN[1]} palabras")


def test_guion_largo_y_etiqueta():
    fallas = revisar_nodo(nodo_base(entregable_esperado="Una lista — la tuya."), FRAGMENTO, set())
    assert any("guion largo" in f for f in fallas), fallas
    larga = revisar_nodo(
        nodo_base(etiqueta_arbol="Una Etiqueta Demasiado Larga Que No Cabe En El Riel"),
        FRAGMENTO, set())
    assert any("etiqueta_arbol" in f for f in larga), larga
    print("  ok: sin guiones largos y con la etiqueta corta")


def test_id_colisionado():
    fallas = revisar_nodo(nodo_base(), FRAGMENTO, {"cuenta_lo_que_ya_tienes"})
    assert any("ya existe en el universo" in f for f in fallas), fallas
    malo = revisar_nodo(nodo_base(node_id="Cuenta-Lo-Que-Tienes"), FRAGMENTO, set())
    assert any("fuera de ^[a-z0-9_]+$" in f for f in malo), malo
    print("  ok: ni ids repetidos del universo ni ids fuera de forma")


# --- Las dos trampas de la API -------------------------------------------
class _Bloque:
    def __init__(self, tipo, texto=""):
        self.type = tipo
        self.text = texto


class _Respuesta:
    def __init__(self, bloques, stop="end_turn"):
        self.content = bloques
        self.stop_reason = stop
        self.usage = type("U", (), {"input_tokens": 10, "output_tokens": 5})()


def test_bloque_de_pensamiento_no_rompe():
    r = _Respuesta([_Bloque("thinking"), _Bloque("text", '[{"a":1}]')])
    assert _texto_de(r) == '[{"a":1}]'
    print("  ok: el texto se busca por tipo, no en content[0]")


class _Flujo:
    """El contexto que devuelve messages.stream()."""

    def __init__(self, respuesta):
        self._r = respuesta

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def get_final_message(self):
        return self._r


def _cliente_falso(guion, vistos):
    """Un cliente que SOLO sabe transmitir. Si el codigo llamara a
    messages.create, aqui reventaria: es la forma de que el test note si
    alguien vuelve al camino sin streaming, que el SDK rechaza en techos
    altos."""
    class _Mensajes:
        def stream(self, **kw):
            vistos.append(kw["max_tokens"])
            return _Flujo(guion(len(vistos)))

    return type("C", (), {"messages": _Mensajes()})()


def test_el_techo_escala_en_vez_de_repetirse():
    """La averia de origen: ante un corte, reintentar con el MISMO techo se
    corta identico las tres veces y el trozo se pierde. El techo tiene que
    subir."""
    vistos = []

    def guion(n):
        if n == 1:
            return _Respuesta([_Bloque("text", '[{"cort')], stop="max_tokens")
        return _Respuesta([_Bloque("text", '[{"ok": true}]')])

    datos, err = llamar(_cliente_falso(guion, vistos), "sys", "prompt", {"in": 0, "out": 0})
    assert err is None, err
    assert datos == [{"ok": True}]
    assert vistos == [TECHOS[0], TECHOS[1]], f"no escalo el techo: {vistos}"
    print(f"  ok: el techo subio de {TECHOS[0]} a {TECHOS[1]} en vez de repetirse")


def test_siempre_transmite():
    """El SDK rechaza la llamada sin streaming cuando el techo es alto
    ('Streaming is required for operations that may take longer than 10
    minutes'), justo cuando la escalera mas la necesita. Cazado en vivo el
    2026-08-07. El cliente falso no tiene messages.create: si alguien vuelve
    a ese camino, esto revienta."""
    vistos = []
    datos, err = llamar(_cliente_falso(lambda n: _Respuesta([_Bloque("text", "[]")]), vistos),
                        "sys", "prompt", {"in": 0, "out": 0})
    assert err is None and datos == [] and vistos == [TECHOS[0]], (err, datos, vistos)
    print("  ok: siempre se transmite, en todos los techos")


def main():
    for f in (test_nodo_limpio_pasa, test_copia_literal, test_campo_renegado_y_obligatorio,
              test_fase_inventada, test_largo_del_resumen, test_guion_largo_y_etiqueta,
              test_id_colisionado, test_bloque_de_pensamiento_no_rompe,
              test_el_techo_escala_en_vez_de_repetirse, test_siempre_transmite):
        f()
    print("OK: las barandas del extractor de mundos sostienen.")


if __name__ == "__main__":
    main()
