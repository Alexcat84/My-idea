# -*- coding: utf-8 -*-
"""Auditor 127: cuantas aristas huerfanas por fusion (metodo del ejecutor,
par resuelto dedup) habia en varios puntos de la historia, para adjudicar si
las 32 de hoy son ANTERIORES a la campana o las fabrico la campana."""
import json, os, subprocess, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def contar(nodos):
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"): continue
        for x in (n.get("ids_alias") or []): alias[x] = nid
    def res(x):
        v=set()
        while x in alias and x not in v: v.add(x); x=alias[x]
        return x
    def vivo(i):
        n=nodos.get(i); return n is not None and not n.get("deprecado")
    def pres(o,d):
        return d in (nodos[o].get("nodos_siguientes") or []) or o in (nodos[d].get("nodos_previos") or [])
    s=set()
    for muere,n in nodos.items():
        if not n.get("deprecado"): continue
        sup=res(muere)
        if sup==muere or not vivo(sup): continue
        for campo,dr in (("nodos_siguientes","sig"),("nodos_previos","prev")):
            for x in (n.get(campo) or []):
                otro=res(x)
                if otro==sup or not vivo(otro): continue
                o,d=(sup,otro) if dr=="sig" else (otro,sup)
                if not pres(o,d): s.add((o,d))
    return s
def en(ref):
    if ref=="WORK":
        return contar(json.load(open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"),encoding="utf-8"))["nodos"])
    r=subprocess.run(["git","show","%s:dataset/metadata/master_graph.json"%ref],cwd=RAIZ,capture_output=True)
    if r.returncode!=0: return None
    return contar(json.loads(r.stdout.decode("utf-8"))["nodos"])
refs=sys.argv[1:]
prev=None; prevref=None
for ref in refs:
    s=en(ref)
    if s is None:
        print("%-12s NO LEGIBLE" % ref); continue
    print("%-12s huerfanas: %d" % (ref, len(s)))
    if prev is not None:
        print("      nuevas desde %s: %r" % (prevref, sorted(s-prev)))
    prev=s; prevref=ref
