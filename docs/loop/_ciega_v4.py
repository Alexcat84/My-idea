#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Volcador CIEGO del auditor (vuelta 4): imprime titulo, resumen y pasos de los dos
nodos de cada puesto pedido. NUNCA imprime clase ni razon. Solo lectura."""
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
idx = {v["puesto_intra"]: v for v in V}
for p in [int(x) for x in sys.argv[1:]]:
    v = idx[p]
    print("=" * 70)
    print("PUESTO %d [%s]" % (p, v["dominio"]))
    for tag in ("nodo_a", "nodo_b"):
        k = v[tag]
        n = G.get(k) or {}
        print("-" * 70)
        print("%s: %s | %s" % (tag, k, n.get("titulo_concepto", "?")))
        print("RESUMEN:", (n.get("resumen_teorico") or "").strip())
        for i, paso in enumerate(n.get("pasos_accionables") or [], 1):
            print("  paso %d: %s" % (i, paso))
