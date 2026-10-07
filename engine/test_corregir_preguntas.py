"""Correccion declarada de preguntas (decision del fundador, 1 oct 2026; docs/REGLAS_DE_LA_CASA.md, R1).

Las preguntas (base de la cache, de entrada de cada puerta y neutral) no se reescriben para adaptarlas a la persona,
pero SI se reemplazan cuando son contrarias a su nodo o a su libro, inventan, o su logica no encaja. El reemplazo va por
correccion declarada, verificada a ciegas, y el texto anterior queda en el registro interno. Prueba en rojo primero.
"""
import json
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts" / "fidelidad"))

import corregir_preguntas as cp  # noqa: E402

ANTES = "¿Quieres que un equipo externo te consiga franquiciados?"
NUEVA = "¿Quieres que un equipo externo cierre las ventas de los franquiciados que tú atraes?"


def _corr(**kw):
    c = {"id": "t-1", "fecha": "2026-10-01", "node_id": "n1", "campo": "pregunta", "veredicto": "CONTRARIO",
         "texto_anterior": ANTES, "texto_nuevo": NUEVA,
         "cita": {"fichero": "libro.txt", "lineas": "10", "frase": "not responsible for lead generation"},
         "verificacion": {"paquete": "paq_vp", "veredicto": "sostiene"},
         "decision": "x", "auditoria": "acta"}
    c.update(kw)
    return c


def _entorno():
    d = Path(tempfile.mkdtemp())
    cache = d / "cache.json"
    cache.write_text(json.dumps({"n1": {"pregunta": ANTES, "candidatos": ["a", "b"]}}, ensure_ascii=False), encoding="utf-8")
    return cache, d / "registro.json"


def test_aplica_y_registra_el_texto_anterior():
    cache, reg = _entorno()
    assert cp.aplicar([_corr()], cache, reg) == 1
    assert json.loads(cache.read_text(encoding="utf-8"))["n1"] == {"pregunta": NUEVA, "candidatos": ["a", "b"]}
    r = json.loads(reg.read_text(encoding="utf-8"))["correcciones"]
    assert [(x["id"], x["texto_anterior"], x["texto_nuevo"]) for x in r] == [("t-1", ANTES, NUEVA)]


def test_es_idempotente():
    cache, reg = _entorno()
    cp.aplicar([_corr()], cache, reg)
    assert cp.aplicar([_corr()], cache, reg) == 0
    assert len(json.loads(reg.read_text(encoding="utf-8"))["correcciones"]) == 1


def _rechaza(c):
    cache, reg = _entorno()
    try:
        cp.aplicar([c], cache, reg)
    except cp.CorreccionInvalida:
        return json.loads(cache.read_text(encoding="utf-8"))["n1"]["pregunta"] == ANTES
    return False


def test_rechazos():
    assert _rechaza(_corr(texto_anterior="otra pregunta?"))          # el anterior no es el vigente
    assert _rechaza(_corr(verificacion={"paquete": "x", "veredicto": "no_sostiene"}))  # sin verificacion que sostenga
    assert _rechaza(_corr(verificacion=None))
    assert _rechaza(_corr(veredicto="VOZ"))                          # solo contrario, invencion o logica
    assert _rechaza(_corr(campo="otra_cosa"))
    assert _rechaza(_corr(texto_nuevo="Cuéntame de tus ventas."))    # tiene que ser pregunta
    assert _rechaza(_corr(texto_nuevo="¿Sugerencia de My Idea: quieres vender?"))
    assert _rechaza(_corr(texto_nuevo="¿Quieres vender " + chr(0x2014) + " o no?"))
    assert _rechaza(_corr(cita={"fichero": "libro.txt", "lineas": "10"}))  # cita de libro sin frase
    assert _rechaza(_corr(veredicto="LOGICA", cita={"fichero": "x", "lineas": "1", "frase": "y"}))  # logica: instrumento


def test_contraria_contra_el_nodo_se_cita_con_instrumento():
    # auditoria de preguntas (6 oct 2026): la pregunta se lee contra su propio nodo, no contra el libro
    cache, reg = _entorno()
    c = _corr(veredicto="INVENCION", cita={"instrumento": "auditoria de preguntas", "evidencia": "el nodo no da cifra"})
    assert cp.aplicar([c], cache, reg) == 1


def test_logica_se_cita_con_instrumento_contra_el_nodo():
    cache, reg = _entorno()
    c = _corr(veredicto="LOGICA", cita={"instrumento": "auditoria de preguntas", "evidencia": "pregunta por otro tema"})
    assert cp.aplicar([c], cache, reg) == 1


if __name__ == "__main__":
    fallos = 0
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_") and callable(f):
            try:
                f()
                print("OK  ", nombre)
            except Exception as e:  # noqa: BLE001
                fallos += 1
                print("FALLA", nombre, repr(e)[:300])
    sys.exit(1 if fallos else 0)
