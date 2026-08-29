# -*- coding: utf-8 -*-
"""Variantes adicionales del recuento de aristas huerfanas por fusion,
buscando si alguna definicion razonable da el 39 del acta 125."""
import json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def cargar(ruta):
    return json.load(open(ruta, encoding="utf-8"))["nodos"]
def analizar(nodos, etiqueta):
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"): continue
        for x in (n.get("ids_alias") or []): alias[x] = nid
    def res(x):
        v = set()
        while x in alias and x not in v:
            v.add(x); x = alias[x]
        return x
    def vivo(i):
        n = nodos.get(i); return n is not None and not n.get("deprecado")
    def presente(o, d):
        return d in (nodos[o].get("nodos_siguientes") or []) or o in (nodos[d].get("nodos_previos") or [])
    v1, crudas_par, ambos_muertos_crudas = set(), set(), set()
    for muere, n in nodos.items():
        if not n.get("deprecado"): continue
        sup = res(muere)
        if sup == muere or not vivo(sup): continue
        for campo, dr in (("nodos_siguientes","sig"), ("nodos_previos","prev")):
            for x in (n.get(campo) or []):
                otro = res(x)
                if otro == sup or not vivo(otro): continue
                o, d = (sup, otro) if dr == "sig" else (otro, sup)
                if presente(o, d): continue
                v1.add((o, d))
                crudas_par.add((muere, x) if dr == "sig" else (x, muere))
                nx = nodos.get(x)
                if nx is not None and nx.get("deprecado"):
                    ambos_muertos_crudas.add((muere, x) if dr == "sig" else (x, muere))
    print("[%s] V1 par resuelto dedup: %d | V5 par CRUDO historico dedup: %d | V6 par crudo con AMBOS extremos deprecados: %d"
          % (etiqueta, len(v1), len(crudas_par), len(ambos_muertos_crudas)))
    return v1
work = cargar(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"))
analizar(work, "WORK hoy")
import subprocess
for ref in ("7150339f", "c9ac2fb8"):
    r = subprocess.run(["git","show","%s:dataset/metadata/master_graph.json" % ref], cwd=RAIZ, capture_output=True)
    analizar(json.loads(r.stdout.decode("utf-8"))["nodos"], ref)
