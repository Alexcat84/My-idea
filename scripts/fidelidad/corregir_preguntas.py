"""Correccion declarada de preguntas (decision del fundador, 1 oct 2026; docs/REGLAS_DE_LA_CASA.md, R1).

Las preguntas (la base de la cache, la de entrada de cada puerta y la neutral) NO se reescriben para adaptarlas a la
persona: eso lo hace el adaptador. Pero SI se reemplazan cuando son contrarias a su nodo o a su libro, inventan, o su
logica no encaja con su nodo (pregunta por otra cosa, presupone algo falso o no tiene sentido en ese punto): cero
contrarios y cero invenciones esta por encima de todo.

El reemplazo va por correccion declarada y verificada a ciegas (`verificacion.veredicto == "sostiene"`). El texto
anterior queda en el registro interno dataset/metadata/correcciones_preguntas.json, que no viaja a la web.

Uso: python scripts/fidelidad/corregir_preguntas.py docs/saneamiento/tandas/<tanda>.json
Prueba: engine/test_corregir_preguntas.py
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
CACHE = BASE / "engine" / "preguntas_cache.json"
REGISTRO = BASE / "dataset" / "metadata" / "correcciones_preguntas.json"

CAMPOS = {"pregunta", "pregunta_entrada", "pregunta_neutral"}
# CONTRARIO e INVENCION se citan con el libro (fichero, lineas, frase); LOGICA, contra el propio nodo, con el
# instrumento que la encontro y su evidencia.
POR_LIBRO = {"CONTRARIO", "INVENCION"}
POR_NODO = {"LOGICA"}
PROHIBIDOS = (chr(0x2014), chr(0x2013))


class CorreccionInvalida(Exception):
    pass


def validar(c, cache):
    f = []
    v = c.get("veredicto")
    if v not in POR_LIBRO | POR_NODO:
        f.append("veredicto %r: solo CONTRARIO, INVENCION o LOGICA" % v)
    if c.get("campo") not in CAMPOS:
        f.append("campo %r" % c.get("campo"))
    e = cache.get(c.get("node_id"))
    if e is None:
        f.append("nodo sin pregunta en la cache")
    elif c.get("campo") in CAMPOS and e.get(c["campo"]) != c.get("texto_anterior"):
        f.append("texto_anterior no es el vigente")
    n = c.get("texto_nuevo") or ""
    if not ("¿" in n and n.rstrip().endswith("?")):
        f.append("el texto nuevo no es una pregunta")
    if n == c.get("texto_anterior"):
        f.append("texto nuevo igual al vigente")
    if "sugerencia de my idea" in n.lower():
        f.append("prefijo de procedencia")
    if any(p in n for p in PROHIBIDOS):
        f.append("guion largo o medio")
    cita = c.get("cita") or {}
    contra_nodo = all(cita.get(k) for k in ("instrumento", "evidencia"))
    # CONTRARIO e INVENCION se citan con el libro, o contra el propio nodo cuando los encontro la auditoria de
    # preguntas (6 oct 2026), que lee cada pregunta contra su nodo saneado.
    if v in POR_LIBRO and not contra_nodo and not all(cita.get(k) for k in ("fichero", "lineas", "frase")):
        f.append("cita de libro incompleta (fichero, lineas, frase)")
    if v in POR_NODO and not all(cita.get(k) for k in ("instrumento", "evidencia")):
        f.append("cita contra el nodo incompleta (instrumento, evidencia)")
    if len((cita.get("frase") or "").split()) > 15:
        f.append("frase del libro de mas de 15 palabras")
    if (c.get("verificacion") or {}).get("veredicto") != "sostiene":
        f.append("sin verificacion ciega que la sostenga")
    return f


def aplicar(tanda, cache_path=CACHE, registro_path=REGISTRO):
    cache = json.loads(Path(cache_path).read_text(encoding="utf-8"))
    reg = json.loads(Path(registro_path).read_text(encoding="utf-8")) if Path(registro_path).exists() else {
        "_nota": "Registro interno de las correcciones declaradas de preguntas (scripts/fidelidad/corregir_preguntas.py). "
                 "Guarda el texto anterior. No se copia a la web.",
        "correcciones": []}
    hechas = {x["id"] for x in reg["correcciones"]}
    nuevas = [c for c in tanda if c.get("id") not in hechas]
    fallas = {c.get("id"): validar(c, cache) for c in nuevas}
    fallas = {k: v for k, v in fallas.items() if v}
    if fallas:
        raise CorreccionInvalida(json.dumps(fallas, ensure_ascii=False))
    for c in nuevas:
        cache[c["node_id"]] = {**cache[c["node_id"]], c["campo"]: c["texto_nuevo"]}
        reg["correcciones"].append(c)
    if nuevas:
        # mismo formato que engine/build_question_cache.py (sin salto final): el diff es solo la pregunta
        Path(cache_path).write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
        Path(registro_path).write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    return len(nuevas)


if __name__ == "__main__":
    t = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print("PREGUNTAS CORREGIDAS: %d" % aplicar(t))
