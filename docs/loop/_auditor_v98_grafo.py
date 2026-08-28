# -*- coding: utf-8 -*-
"""_auditor_v98_grafo.py . INSTRUMENTO PROPIO DEL AUDITOR DE LA VUELTA 98.

Las ocho cifras del grafo en CINCO refs (apertura sellada 19a8f95e, el commit
del acta 95 ea93d674, el cierre de las tareas c1873af3, y el arbol de trabajo),
con sha256 en las cuatro, y el diff de la union entera de aristas dirigidas
entre la apertura y el arbol de trabajo.

    python docs/loop/_auditor_v97_grafo.py > docs/loop/_auditor_v97_grafo.txt
"""
import hashlib
import json
import subprocess

RUTA = "dataset/metadata/master_graph.json"
REFS = ["19a8f95e", "61448511", "13b8d3c5", "91675e18", "395a1524", "752f39a6", "43e014a0", "12fcedb6", "WORK"]


def cargar(ref):
    if ref == "WORK":
        b = open(RUTA, "rb").read()
    else:
        b = subprocess.run(["git", "show", ref + ":" + RUTA],
                           capture_output=True, check=True).stdout
    return b, json.loads(b.decode("utf-8"))


def medir(ref):
    b, g = cargar(ref)
    items = list(g["nodos"].items())
    total = len(items)
    dep = sum(1 for _, n in items if n.get("deprecado"))
    sig = sum(len(n.get("nodos_siguientes") or []) for _, n in items)
    prev = sum(len(n.get("nodos_previos") or []) for _, n in items)
    union, auto = set(), 0
    for i, n in items:
        for d in (n.get("nodos_siguientes") or []):
            union.add((i, d))
            auto += (d == i)
        for o in (n.get("nodos_previos") or []):
            union.add((o, i))
            auto += (o == i)
    return dict(ref=ref, sha=hashlib.sha256(b).hexdigest(), total=total,
                deprecado=dep, vivos=total - dep, sig=sig, prev=prev,
                suma=sig + prev, union=len(union), auto=auto), union


unis = {}
for r in REFS:
    m, u = medir(r)
    unis[r] = u
    print(json.dumps(m, ensure_ascii=False))

ap, tr = unis["19a8f95e"], unis["WORK"]
print("BORRADAS (apertura 19a8f95e menos trabajo):", len(ap - tr))
for e in sorted(ap - tr):
    print("  -", e)
print("NUEVAS (trabajo menos apertura 19a8f95e):", len(tr - ap))
for e in sorted(tr - ap):
    print("  +", e)
print("SHA IGUALES EN LAS NUEVE REFS:",
      len({medir(r)[0]["sha"] for r in REFS}) == 1)
