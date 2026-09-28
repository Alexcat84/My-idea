# -*- coding: utf-8 -*-
"""Tildes mecanicas del remedio (acta de la auditoria final, seccion 9.3; decision del fundador del 28 sep 2026).

Corrige solo las palabras de docs/saneamiento/ortografia/tildes_mecanicas.json: las que sin tilde no existen en espanol
y cuya forma con tilde es unica. Las ambiguas quedan para los lectores. Respeta los nombres en ingles ("Decision Log",
"Cash Conversion Cycle") y conserva las mayusculas de la palabra.

Uso:
  python scripts/saneamiento/tildes_mecanicas.py <tanda.json>   escribe la tanda ORTOGRAFIA (no toca el dataset);
                                                                se aplica con scripts/fidelidad/aplicar_correcciones.py
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
CAMPOS = ["resumen_teorico", "pasos_accionables", "condiciones_activacion", "entregable_esperado", "etiqueta_arbol",
          "titulo_concepto"]
PALABRA = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")
# Vecinos que delatan un nombre en ingles: la palabra de al lado no se traduce y la de la lista tampoco.
INGLES = {"automatic", "cash", "cycle", "rights", "log", "mechanics", "error", "aid", "day", "key", "person",
          "discovery", "maintenance", "availability"}


def _con_caso(original, nueva):
    if original.isupper() and len(original) > 1:
        return nueva.upper()
    if original[0].isupper():
        return nueva[0].upper() + nueva[1:]
    return nueva


def corregir(texto, pares):
    tokens = list(PALABRA.finditer(texto))
    salida, ultimo = [], 0
    for i, m in enumerate(tokens):
        w = m.group(0)
        nueva = pares.get(w.lower())
        if not nueva:
            continue
        vecinos = {tokens[j].group(0).lower() for j in (i - 1, i + 1) if 0 <= j < len(tokens)}
        if w[0].isupper() and vecinos & INGLES:
            continue
        salida.append(texto[ultimo:m.start()])
        salida.append(_con_caso(w, nueva))
        ultimo = m.end()
    salida.append(texto[ultimo:])
    return "".join(salida)


def _vivos(carpeta):
    for p in sorted(Path(carpeta).glob("*.json")):
        n = json.loads(p.read_text(encoding="utf-8"))
        if not n.get("deprecado"):
            yield n


def _textos(n):
    for campo in CAMPOS:
        v = n.get(campo)
        if isinstance(v, list):
            for i, t in enumerate(v):
                yield campo, i, t
        elif isinstance(v, str):
            yield campo, None, v


def pendientes(carpeta, pares):
    """Campos vivos donde la lista todavia corrige algo."""
    return ["%s.%s%s" % (n["node_id"], campo, "" if i is None else "[%d]" % i)
            for n in _vivos(carpeta) for campo, i, t in _textos(n) if corregir(t, pares) != t]


def tanda(carpeta, pares, fecha="2026-09-28"):
    salida = []
    for n in _vivos(carpeta):
        for campo, i, t in _textos(n):
            nuevo = corregir(t, pares)
            if nuevo == t:
                continue
            cambios = sorted({a.group(0) for a, b in zip(PALABRA.finditer(t), PALABRA.finditer(nuevo))
                              if a.group(0) != b.group(0)})
            c = {"id": "final-tildes-%s-%s%s" % (n["node_id"], campo, "" if i is None else "-%d" % i),
                 "fecha": fecha, "node_id": n["node_id"], "campo": campo, "veredicto": "ORTOGRAFIA",
                 "texto_anterior": t, "texto_nuevo": nuevo,
                 "cita": {"instrumento": "scripts/saneamiento/tildes_mecanicas.py con la lista curada "
                                         "docs/saneamiento/ortografia/tildes_mecanicas.json",
                          "evidencia": "palabras sin tilde que no existen en español: " + ", ".join(cambios)},
                 "decision": "auditoria final, remedio 9.3: tildes mecanicas (decision del fundador, 28 sep 2026)",
                 "auditoria": "docs/ACTA_SANEAMIENTO_FINAL.md seccion 9.3"}
            if i is not None:
                c["indice"] = i
            salida.append(c)
    return salida


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    pares = json.loads((BASE / "docs" / "saneamiento" / "ortografia" / "tildes_mecanicas.json")
                       .read_text(encoding="utf-8"))["pares"]
    t = tanda(BASE / "dataset" / "nodos", pares)
    Path(argv[1]).write_text(json.dumps(t, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("tanda escrita: %d correcciones en %d nodos" % (len(t), len({c["node_id"] for c in t})))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
