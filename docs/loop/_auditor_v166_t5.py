# -*- coding: utf-8 -*-
"""EL COLAPSO DEL FICHERO ENTERO, RE MEDIDO POR EL AUDITOR (vuelta 166, TAREA 5)."""
import collections, io, json, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = json.load(io.open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]
ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}
def res(x, visto=None):
    visto = visto or set()
    while x in ALIAS and x not in visto:
        visto.add(x); x = ALIAS[x]
    return x
V = [json.loads(l) for l in io.open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"), encoding="utf-8") if l.strip()]
auto = [r for r in V if res(r["nodo_a"]) == res(r["nodo_b"])]
porpar = collections.OrderedDict()
for r in V:
    ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
    if ra == rb: continue
    porpar.setdefault(frozenset((ra, rb)), []).append(r)
multi = {k: v for k, v in porpar.items() if len(v) > 1}
conflicto = {k: v for k, v in multi.items() if len(set(r["clase"] for r in v)) > 1}
print("filas totales: %d" % len(V))
print("filas que colapsan a auto-par: %d" % len(auto))
print("pares resueltos distintos: %d" % len(porpar))
print("pares con mas de una fila: %d" % len(multi))
print("de esos, con CLASES DISTINTAS: %d" % len(conflicto))
combos = collections.Counter("".join(sorted(set(r["clase"] for r in v))) for v in conflicto.values())
print("reparto de combinaciones: %s" % dict(combos))
print()
for i, (k, v) in enumerate(sorted(conflicto.items(), key=lambda kv: min(r["puesto_intra"] for r in kv[1])), 1):
    print("%2d. %s" % (i, sorted(k)))
    for r in sorted(v, key=lambda r: r["puesto_intra"]):
        print("      puesto %4d  clase %s  crudos: %s / %s" % (r["puesto_intra"], r["clase"], r["nodo_a"], r["nodo_b"]))
