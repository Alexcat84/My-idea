# -*- coding: utf-8 -*-
"""AUDITOR v146: mido yo el prerrequisito de OP-A-01 contra el grafo."""
import json, io, re
g = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))
nodos = g["nodos"]
vivos = {k: n for k, n in nodos.items() if not n.get("deprecado")}
tipos = set(type(n.get("fuente")).__name__ for n in nodos.values())
print("tipos del campo fuente en TODO el grafo:", sorted(tipos))
def trozos(v, sep):
    return [t.strip() for t in (v or "").split(sep) if t.strip()]
for sep, nombre in [("|", "barra vertical"), (";", "punto y coma")]:
    mas_de_uno = [k for k, n in vivos.items() if len(trozos(n.get("fuente"), sep)) > 1]
    segundas = sum(max(0, len(trozos(n.get("fuente"), sep)) - 1) for n in vivos.values())
    print("sep %-14s -> nodos VIVOS con mas de una fuente: %d | declaraciones en 2.a posicion o posterior: %d"
          % (nombre, len(mas_de_uno), segundas))
for autor in ["Hugos", "Horowitz"]:
    def grafias(pool):
        s = set()
        for n in pool.values():
            for t in trozos(n.get("fuente"), "|"):
                if autor.lower() in t.lower():
                    s.add(t)
        return s
    gv, gt = grafias(vivos), grafias(nodos)
    print("%-9s grafias SOLO VIVOS: %d %s" % (autor, len(gv), sorted(gv)))
    print("%-9s grafias TODOS:      %d %s" % (autor, len(gt), sorted(gt)))
import os
for c in ["dataset/metadata/libros_canonicos.json", "dataset/metadata/fuentes_canonicas.json", "docs/plan/LIBROS_CANONICOS.md"]:
    print("candidato %-45s existe: %s" % (c, os.path.exists(c)))
