# -*- coding: utf-8 -*-
"""AUDITOR v146: el recorte posicional de la ficha de OP-A-01, medido sobre el
grafo del CORTE (0e5e0c60, 9 ago 2026) y sobre el de HOY, con el mismo codigo."""
import json, subprocess, sys
def medir(ref):
    if ref == "WORK":
        blob = open("dataset/metadata/master_graph.json", encoding="utf-8").read()
    else:
        blob = subprocess.run(["git","cat-file","-p",ref+":dataset/metadata/master_graph.json"],
                              capture_output=True).stdout.decode("utf-8")
    nodos = json.loads(blob)["nodos"]
    vivos = {k:n for k,n in nodos.items() if not n.get("deprecado")}
    p = lambda v: [t.strip() for t in (v or "").split("|") if t.strip()]
    mas = [k for k,n in vivos.items() if len(p(n.get("fuente")))>1]
    seg = sum(max(0,len(p(n.get("fuente")))-1) for n in vivos.values())
    def gr(pool, autor):
        s=set()
        for n in pool.values():
            for t in p(n.get("fuente")):
                if autor.lower() in t.lower(): s.add(t)
        return s
    def usan(pool, autor, canon=None):
        c=0
        for n in pool.values():
            ts=p(n.get("fuente"))
            if canon: c += 1 if any(t==canon for t in ts) else 0
            else:     c += 1 if any(autor.lower() in t.lower() for t in ts) else 0
        return c
    print("REF %-10s vivos %d | nodos con mas de una fuente %d | declaraciones en 2.a o posterior %d"
          % (ref, len(vivos), len(mas), seg))
    for a, canon in [("Hugos","Essentials of Supply Chain Management - Michael H. Hugos"),
                     ("Horowitz","The Hard Thing About Hard Things - Ben Horowitz")]:
        print("   %-9s grafias vivos %d todos %d | nodos vivos que lo citan: TODA grafia %d, SOLO la canonica %d"
              % (a, len(gr(vivos,a)), len(gr(nodos,a)), usan(vivos,a), usan(vivos,a,canon)))
for r in sys.argv[1:]: medir(r)
