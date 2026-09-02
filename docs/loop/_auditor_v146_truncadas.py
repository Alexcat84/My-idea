# -*- coding: utf-8 -*-
"""AUDITOR v146: la hipotesis de la TRUNCACION, medida sobre todo el catalogo."""
import json, io
g = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))
nodos = g["nodos"]
def partes(v): return [t.strip() for t in (v or "").split("|") if t.strip()]
uso = {}
for k, n in nodos.items():
    for t in partes(n.get("fuente")):
        uso.setdefault(t, {"vivos": 0, "depr": 0})
        uso[t]["depr" if n.get("deprecado") else "vivos"] += 1
print("grafias distintas del campo fuente en TODO el grafo:", len(uso))
def titulo(t): return t.split(" - ")[0]
pares = []
for a in uso:
    for b in uso:
        if a != b and titulo(b).startswith(titulo(a)) and len(titulo(a)) < len(titulo(b)):
            if a.split(" - ")[-1] == b.split(" - ")[-1]:
                pares.append((a, b))
print("PAREJAS titulo-prefijo con el MISMO autor (la corta y la larga):", len(pares))
largos = sorted(set(len(titulo(a)) for a, b in pares))
print("longitud del titulo CORTO en cada pareja:", largos)
for a, b in sorted(pares):
    print("  CORTA len %2d %-40s vivos %d depr %d" % (len(titulo(a)), a, uso[a]["vivos"], uso[a]["depr"]))
    print("  LARGA len %2d %-40s vivos %d depr %d" % (len(titulo(b)), b, uso[b]["vivos"], uso[b]["depr"]))
