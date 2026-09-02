# -*- coding: utf-8 -*-
"""Auditor v141: censo y las cuatro cifras de aristas con parser PROPIO,
leidas de dataset/nodos/*.json y NUNCA de master_graph.json.
USO: python docs/loop/_auditor_v141_censo.py <raiz de nodos>"""
import json, os, sys, glob
raiz = sys.argv[1]
nodos = {}
for p in glob.glob(os.path.join(raiz, "*.json")):
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    nid = d.get("id") or os.path.splitext(os.path.basename(p))[0]
    nodos[nid] = d
total = len(nodos)
depre = sum(1 for d in nodos.values() if d.get("deprecado"))
claves = set()
for d in nodos.values():
    for k in d.keys():
        claves.add(k)
sig = prev = 0
S = set(); P = set()
auto = 0; dup = 0
for nid, d in nodos.items():
    ns = d.get("nodos_siguientes") or []
    np = d.get("nodos_previos") or []
    if len(set(ns)) != len(ns): dup += 1
    if len(set(np)) != len(np): dup += 1
    sig += len(ns); prev += len(np)
    for t in ns:
        S.add((nid, t))
        if t == nid: auto += 1
    for t in np:
        P.add((t, nid))
union = S | P
print("CLAVES:", sorted(claves))
print("nodos:", total, "deprecados:", depre, "vivos:", total - depre)
print("sig:", sig, "prev:", prev, "suma:", sig + prev, "union:", len(union))
print("solo_sig:", len(S - P), "solo_prev:", len(P - S),
      "auto(literal):", auto, "nodos con duplicada en lista:", dup)
