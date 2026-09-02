# -*- coding: utf-8 -*-
"""AUDITOR v146: el '23 y 16 donde el canonico da 21 y 14' de la ficha de
OP-A-01, medido sobre el grafo del corte y sobre el de hoy."""
import json, subprocess, sys
CANON = {"Hugos":"Essentials of Supply Chain Management - Michael H. Hugos",
         "Horowitz":"The Hard Thing About Hard Things - Ben Horowitz"}
def medir(ref):
    blob = (open("dataset/metadata/master_graph.json",encoding="utf-8").read() if ref=="WORK"
            else subprocess.run(["git","cat-file","-p",ref+":dataset/metadata/master_graph.json"],
                                capture_output=True).stdout.decode("utf-8"))
    nodos = json.loads(blob)["nodos"]
    vivos = {k:n for k,n in nodos.items() if not n.get("deprecado")}
    p = lambda v: [t.strip() for t in (v or "").split("|") if t.strip()]
    print("REF", ref)
    for a in ("Hugos","Horowitz"):
        tot = sum(1 for n in vivos.values() if any(a.lower() in t.lower() for t in p(n.get("fuente"))))
        can = sum(1 for n in vivos.values() if CANON[a] in p(n.get("fuente")))
        seg_tot = sum(1 for n in vivos.values() if any(a.lower() in t.lower() for t in p(n.get("fuente"))[1:]))
        seg_can = sum(1 for n in vivos.values() if CANON[a] in p(n.get("fuente"))[1:])
        pri_tot = sum(1 for n in vivos.values() if p(n.get("fuente"))[:1] and a.lower() in p(n.get("fuente"))[0].lower())
        pri_can = sum(1 for n in vivos.values() if p(n.get("fuente"))[:1] and p(n.get("fuente"))[0]==CANON[a])
        print("  %-9s | citan (toda grafia) %4d, (solo canonica) %4d | en 2.a o posterior: toda %3d, canonica %3d | en 1.a: toda %4d, canonica %4d"
              % (a, tot, can, seg_tot, seg_can, pri_tot, pri_can))
for r in sys.argv[1:]: medir(r)
