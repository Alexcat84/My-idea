#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""volcar_pares.py . vuelca los pares de un tramo de la cola para leerlos.

SOLO LECTURA. No toca ni un nodo ni un veredicto.

Uso:  python scripts/volcar_pares.py 2118 2142
      python scripts/volcar_pares.py 2118 2142 --breve
"""
import json, io, sys, argparse

ap = argparse.ArgumentParser()
ap.add_argument("desde", type=int)
ap.add_argument("hasta", type=int)
ap.add_argument("--breve", action="store_true", help="solo titulos y entregables")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")

G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
P = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip()]
AL = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}


def res(x):
    s = set()
    while x in AL and x not in s:
        s.add(x)
        x = AL[x]
    return x


def vecinos(k):
    out = set()
    for c in ("nodos_previos", "nodos_siguientes"):
        for y in (G.get(k, {}).get(c) or []):
            out.add(res(y))
    return out


for p in sorted((x for x in P if a.desde <= x["puesto_intra"] <= a.hasta), key=lambda x: x["puesto_intra"]):
    A, B = p["nodo_a"], p["nodo_b"]
    arista = (res(B) in vecinos(A)) or (res(A) in vecinos(B))
    print("=" * 78)
    print("PUESTO %d  [%s]  sim_tit %.1f  sim_sem %.3f  %s" %
          (p["puesto_intra"], p["dominio"], p.get("sim_titulo", 0), p.get("sim_semantica", 0),
           "CON ARISTA" if arista else "sin arista"))
    for k in (A, B):
        n = G.get(k) or {}
        fu = n.get("fuente")
        print("  --- %s   [%s]" % (k, (fu if isinstance(fu, str) else " | ".join(fu or []))[:52]))
        print("      %s" % (n.get("titulo_concepto") or "SIN NODO"))
        if not a.breve:
            for j, s in enumerate(n.get("pasos_accionables") or [], 1):
                print("      %d. %s" % (j, s[:150]))
        else:
            print("      entregable: %s" % (n.get("entregable_esperado") or "")[:110])
