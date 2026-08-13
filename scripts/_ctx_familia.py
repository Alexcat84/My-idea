#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_ctx_familia.py  SOLO LECTURA. Contexto de familia para dictaminar un tramo.
Para cada par [desde..hasta], lista TODOS los veredictos ya registrados (puesto<=corte
o cualquiera) que tocan a nodo_a o nodo_b, y ademas veredictos de nodos que comparten
raiz de id (para ver el cumulo). No imprime nada del tramo aun sin dictar."""
import json, io, sys, argparse, re
ap = argparse.ArgumentParser()
ap.add_argument("desde", type=int); ap.add_argument("hasta", type=int)
a = ap.parse_args(); sys.stdout.reconfigure(encoding="utf-8")
P=[json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl",encoding="utf-8") if l.strip()]
V=[json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl",encoding="utf-8") if l.strip()]
bynode={}
for v in V:
    bynode.setdefault(v["nodo_a"],[]).append(v); bynode.setdefault(v["nodo_b"],[]).append(v)
def toks(nid): return set(t for t in re.split(r"[_0-9]+",nid) if len(t)>=4)
seg=[p for p in P if a.desde<=p["puesto_intra"]<=a.hasta]
allnodes=[(v["nodo_a"],v["nodo_b"]) for v in V]
for p in seg:
    print("#"*70); print("PAR %d  %s  <>  %s  (sim_tit %.1f)"%(p["puesto_intra"],p["nodo_a"],p["nodo_b"],p.get("sim_titulo",0)))
    for k in (p["nodo_a"],p["nodo_b"]):
        vs=[x for x in bynode.get(k,[]) if x["puesto_intra"]<p["puesto_intra"]]
        print("  -- %s: %d veredictos previos"%(k,len(vs)))
        for x in vs:
            otro=x["nodo_b"] if x["nodo_a"]==k else x["nodo_a"]
            print("       [%d %s] vs %s"%(x["puesto_intra"],x["clase"],otro))
    # cumulo por token compartido de id
    kt=toks(p["nodo_a"])|toks(p["nodo_b"])
    rel=set()
    for v in V:
        if v["puesto_intra"]>=p["puesto_intra"]: continue
        for nn in (v["nodo_a"],v["nodo_b"]):
            if nn in (p["nodo_a"],p["nodo_b"]): continue
            if len(toks(nn)&kt)>=2:
                rel.add((v["puesto_intra"],v["clase"],v["nodo_a"],v["nodo_b"]))
    if rel:
        print("  -- cumulo (>=2 tokens de id compartidos):")
        for r in sorted(rel)[:12]:
            print("       [%d %s] %s <> %s"%r)
