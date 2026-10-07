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
MAY = "A-ZÁÉÍÓÚÑ"

NOMBRE = r"[%s][a-záéíóúñ]+" % MAY
# El verbo o la frase de autoria no distingue mayusculas; el NOMBRE si: tiene que empezar en mayuscula.
FORMAS = [
    ("autoria", re.compile(r"(?i:\b(popularizad|desarrollad|propuest|cread|acuñad|ideado|ideada|formulad|introducid|"
                           r"difundid|planteado|planteada)[oa]s?\s+por)\s+" + NOMBRE)),
    ("basado_en", re.compile(r"(?i:\bbasad[oa]s?\s+en\s+(el|la|los|las)\s+(modelo|trabajo|concepto|teor[ií]a|idea|"
                             r"enfoque|propuesta|an[eé]cdota)s?\s+de)\s+" + NOMBRE)),
    ("segun_nombre", re.compile(r"(?i:\bseg[uú]n)\s+" + NOMBRE + r"\s+" + NOMBRE)),
    ("oficio_nombre", re.compile(r"(?i:\b(el|la)\s+(fil[oó]sof[oa]|psic[oó]log[oa]|soci[oó]log[oa]|economista|autora?|"
                                 r"investigador[a]?|profesor[a]?|dise[nñ]ador[a]?|consultor[a]?))\s+" + NOMBRE)),
    ("dijo_nombre", re.compile(r"(?i:\bcomo\s+(dijo|dec[ií]a|escribi[oó]|afirm[oó]|explic[oó]|aconsejaba))\s+" + NOMBRE)),
    ("referencia", re.compile(r"\(\s*(?i:ver|v[eé]ase|cf\.?)\s+[A-Z]")),
]


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
    for nid, campo, t in textos():
        for nombre, rx in FORMAS:
            # las etiquetas van en mayuscula de titulo: "Calidad Según Quien Juzga" no nombra a nadie
            if campo == "etiqueta_arbol" and nombre == "segun_nombre":
                continue
            m = rx.search(t)
            if m:
                out.append("%s.%s [%s] %r" % (nid, campo, nombre, t[max(0, m.start() - 20):m.end() + 30]))
    return out


def test_ninguna_persona_con_nombre_como_fuente():
    f = faltas()
    assert not f, "procedencia con nombre propio (%d):\n  %s" % (len(f), "\n  ".join(f[:40]))


def test_las_formas_cazan_los_casos_de_la_medida_4():
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
