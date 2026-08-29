# -*- coding: utf-8 -*-
"""Codigo PROPIO del auditor de la vuelta 127: recuento independiente de las
'aristas huerfanas por fusion' con CUATRO definiciones distintas, para
adjudicar la discrepancia 32 (ejecutor, vuelta 126) contra 39 (auditor,
acta 125, cuyo codigo NO quedo en el repo y por tanto no es cotejable)."""
import json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

def main():
    nodos = json.load(open(RUTA, encoding="utf-8"))["nodos"]
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        for x in (n.get("ids_alias") or []):
            alias[x] = nid
    def res(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x); x = alias[x]
        return x
    def vivo(i):
        n = nodos.get(i); return n is not None and not n.get("deprecado")
    def presente(o, d):
        return d in (nodos[o].get("nodos_siguientes") or []) or o in (nodos[d].get("nodos_previos") or [])

    v1 = set()          # dedup por par resuelto, cualquier muerto con superviviente vivo
    v2 = []             # ocurrencias crudas (muerto, entrada, direccion)
    v3 = set()          # SOLO cuando el OTRO extremo historico tambien estaba deprecado
    v4 = set()          # presencia exigida en UNA sola vista (la del superviviente)
    for muere, n in nodos.items():
        if not n.get("deprecado"):
            continue
        sup = res(muere)
        if sup == muere or not vivo(sup):
            continue
        for campo, direccion in (("nodos_siguientes", "sig"), ("nodos_previos", "prev")):
            for x in (n.get(campo) or []):
                otro = res(x)
                if otro == sup or not vivo(otro):
                    continue
                o, d = (sup, otro) if direccion == "sig" else (otro, sup)
                if not presente(o, d):
                    v1.add((o, d))
                    v2.append((muere, campo, x, o, d))
                    nx = nodos.get(x)
                    if nx is not None and nx.get("deprecado"):
                        v3.add((o, d))
                if direccion == "sig":
                    ok = d in (nodos[o].get("nodos_siguientes") or [])
                else:
                    ok = o in (nodos[d].get("nodos_previos") or [])
                if not ok:
                    v4.add((o, d))
    print("V1 dedup por par resuelto (metodo del ejecutor): %d" % len(v1))
    print("V2 ocurrencias crudas sin dedup: %d" % len(v2))
    print("V3 solo si el otro extremo historico tambien estaba deprecado: %d" % len(v3))
    print("V4 presencia exigida en UNA sola vista, dedup: %d" % len(v4))
    print("--- V1 ---")
    for p in sorted(v1):
        print("  %s -> %s" % p)
    return 0

sys.exit(main())
