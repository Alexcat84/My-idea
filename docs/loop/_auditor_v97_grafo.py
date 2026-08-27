# -*- coding: utf-8 -*-
"""_auditor_v97_grafo.py . INSTRUMENTO PROPIO DEL AUDITOR DE LA VUELTA 96.

Las ocho cifras del grafo en CINCO refs (apertura sellada eb91fbd4, el commit
del acta 95 ea93d674, el cierre de las tareas c1873af3, y el arbol de trabajo),
con sha256 en las cuatro, y el diff de la union entera de aristas dirigidas
entre la apertura y el arbol de trabajo.

    python docs/loop/_auditor_v97_grafo.py > docs/loop/_auditor_v97_grafo.txt
"""
import hashlib
import json
import subprocess

RUTA = "dataset/metadata/master_graph.json"
REFS = ["eb91fbd4", "eee77af3", "9788a45d", "c46cd795", "bbdb5a13", "WORK"]


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

ap, tr = unis["eb91fbd4"], unis["WORK"]
print("BORRADAS (apertura eb91fbd4 menos trabajo):", len(ap - tr))
for e in sorted(ap - tr):
    print("  -", e)
print("NUEVAS (trabajo menos apertura eb91fbd4):", len(tr - ap))
for e in sorted(tr - ap):
    print("  +", e)
print("SHA IGUALES EN LAS SEIS REFS:",
      len({medir(r)[0]["sha"] for r in REFS}) == 1)
