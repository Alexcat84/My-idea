# -*- coding: utf-8 -*-
"""CIEGA del auditor 96: vuelca SOLO los pasos_accionables de los dos nodos de
cada par pedido, SIN la razon, SIN la clase y SIN la direccion escrita.
AUDITOR.md 1.2: primero los pasos, se adjudica, y solo despues se destapa."""
import json, io, sys

G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
T = [json.loads(l) for l in io.open("docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl", encoding="utf-8") if l.strip()]
por = {r["puesto_tramo"]: r for r in T}

def vuelca(nid, rol):
    n = G.get(nid, {})
    print("  %s: %s" % (rol, nid))
    print("     titulo: %s" % n.get("titulo"))
    ps = n.get("pasos_accionables") or []
    print("     pasos_accionables (%d):" % len(ps))
    for i, p in enumerate(ps, 1):
        if isinstance(p, dict):
            p = p.get("texto") or p.get("paso") or json.dumps(p, ensure_ascii=False)
        print("       %d. %s" % (i, p))

for k in [int(x) for x in sys.argv[1:]]:
    r = por[k]
    print("=" * 78)
    print("PAR %d  (dominio %s)" % (k, r.get("dominio")))
    print("  [la etiqueta de la bolsa dice madre/hijo, pero NO la leo como veredicto]")
    vuelca(r["madre_de_la_bolsa"], "nodo X (etiquetado madre en la bolsa)")
    vuelca(r["hijo_de_la_bolsa"], "nodo Y (etiquetado hijo en la bolsa)")
    print()
