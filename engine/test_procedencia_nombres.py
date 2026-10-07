"""Ninguna persona con nombre como fuente en los textos de cara (medida 4 de procedencia, acta 15.3, 6 oct 2026).

La medida 4 encontro lo que las guardas no veian: "Popularizada por Janine Benyus", "El filosofo Don Ihde llama",
"Basado en el modelo de Stewart Brand", "(ver NIST SP 800-60)". La guarda de titulos (test_fuentes_de_cara.py) solo
conoce los libros de la lista canonica, y la de origen solo las marcas internas. Esta guarda busca las formas de
autoria con nombre propio en todos los textos de cara de los nodos vivos: etiqueta, resumen, pasos, condiciones,
entregable y pregunta base. Un nombre de metodo que se explica sin atribuirlo no es procedencia (regla D5): las
formas de abajo exigen un verbo o una frase de autoria delante del nombre.

Si un texto nuevo cae aqui, la salida es corregirlo por el metodo de la casa, no ampliar la lista de excepciones.
Prueba en rojo primero.
"""
import glob
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GUARDAS = BASE / "dataset" / "metadata" / "guardas_contenido.json"

# Una sola fuente (PROXIMOS_PASOS 6, punto 3; 7 oct 2026): las formas viven en web/lib/pautasProcedencia.ts, salen a
# dataset/metadata/guardas_contenido.json (pauta "nombrePropio", desde la version 1.1.0) y esta prueba las lee de ahi,
# las mismas que copia la forja. El verbo o la frase de autoria no distingue mayusculas; el NOMBRE si: tiene que
# empezar en mayuscula. Los patrones son ECMAScript, pero los de esta pauta solo usan lo que re tambien entiende.
_FLAGS = {"i": re.IGNORECASE, "m": re.MULTILINE, "s": re.DOTALL, "u": 0, "g": 0}


def _pauta(pid):
    g = json.loads(GUARDAS.read_text(encoding="utf-8"))
    pautas = {p["id"]: p for p in g.get("procedencia") or []}
    assert pid in pautas, ("guardas_contenido.json (version %s) no trae la pauta %r: cd web && npx tsx "
                           "scripts/exportar_guardas.ts" % (g.get("version"), pid))
    return pautas[pid]


def _compilar(p):
    fl = 0
    for c in p["flags"]:
        fl |= _FLAGS[c]
    return re.compile(p["patron"], fl)


def formas():
    """[(id, patron compilado, campos donde no aplica)] de la pauta nombrePropio."""
    return [(p["id"], _compilar(p), set(p.get("no_aplica_en") or [])) for p in _pauta("nombrePropio")["patrones"]]


def textos():
    cache = json.loads((BASE / "engine" / "preguntas_cache.json").read_text(encoding="utf-8"))
    for f in sorted(glob.glob(str(BASE / "dataset" / "nodos" / "*.json"))):
        n = json.loads(Path(f).read_text(encoding="utf-8"))
        if n.get("deprecado"):
            continue
        nid = n["node_id"]
        for campo in ("etiqueta_arbol", "resumen_teorico", "entregable_esperado"):
            if n.get(campo):
                yield nid, campo, n[campo]
        for campo in ("pasos_accionables", "condiciones_activacion"):
            for i, t in enumerate(n.get(campo) or []):
                yield nid, "%s[%d]" % (campo, i), t
        p = (cache.get(nid) or {}).get("pregunta")
        if p:
            yield nid, "pregunta", p


def faltas():
    out = []
    lista = formas()
    for nid, campo, t in textos():
        for nombre, rx, no_aplica in lista:
            # p. ej. las etiquetas van en mayuscula de titulo: "Calidad Según Quien Juzga" no nombra a nadie
            if campo.split("[")[0] in no_aplica:
                continue
            m = rx.search(t)
            if m:
                out.append("%s.%s [%s] %r" % (nid, campo, nombre, t[max(0, m.start() - 20):m.end() + 30]))
    return out


def test_ninguna_persona_con_nombre_como_fuente():
    f = faltas()
    assert not f, "procedencia con nombre propio (%d):\n  %s" % (len(f), "\n  ".join(f[:40]))


def test_las_formas_salen_de_guardas_contenido():
    """Las seis formas llegan por el fichero que copia la forja, con la excepcion de la etiqueta, y sus fixtures
    se cumplen tambien en Python."""
    p = _pauta("nombrePropio")
    assert [f["id"] for f in p["patrones"]] == ["autoria", "basado_en", "segun_nombre", "oficio_nombre",
                                                "dijo_nombre", "referencia"]
    assert dict((i, n) for i, _, n in formas())["segun_nombre"] == {"etiqueta_arbol"}
    rx = [r for _, r, _ in formas()]
    for t in p["caza"]:
        assert any(r.search(t) for r in rx), t
    for t in p["no_caza"]:
        assert not any(r.search(t) for r in rx), t


def test_las_formas_cazan_los_casos_de_la_medida_4():
    FORMAS = [(i, r) for i, r, _ in formas()]
    casos = ["Popularizada por Janine Benyus, la biomímesis propone",
             "Basado en el modelo de Stewart Brand, todo sistema",
             "El filósofo Don Ihde llama 'falacia del diseñador'",
             "documentar la categorización (ver NIST SP 800-60).",
             "como dijo George Box: 'todos los modelos'"]
    for c in casos:
        assert any(rx.search(c) for _, rx in FORMAS), c
    for limpio in ["Aplica el ciclo PDCA a tu proceso", "Usa el diagrama de Ishikawa para ordenar causas",
                   "Si vendes en Estados Unidos, revisa la norma"]:
        assert not any(rx.search(limpio) for _, rx in FORMAS), limpio


if __name__ == "__main__":
    fallos = 0
    for nombre, fn in list(globals().items()):
        if nombre.startswith("test_") and callable(fn):
            try:
                fn()
                print("OK  ", nombre)
            except AssertionError as e:
                fallos += 1
                print("FALLA", nombre, str(e)[:3000])
    sys.exit(1 if fallos else 0)
