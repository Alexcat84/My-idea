# -*- coding: utf-8 -*-
"""_auditor_v95_grafo.py . EL INSTRUMENTO DEL AUDITOR DE LA VUELTA 95: las ocho
cifras del grafo en tres refs (apertura 325f537c, cierre 220c07a1, arbol de
trabajo), con sha256 en las tres, y el diff de la union entera de aristas
dirigidas entre apertura y trabajo.

Se corre asi:

    python docs/loop/_auditor_v95_grafo.py > docs/loop/_auditor_v95_grafo.txt

y su salida tiene que ser identica a la commiteada.
"""
import hashlib
import json
import subprocess

REFS = ["325f537c", "220c07a1", "WORK"]


def cargar(ref):
    if ref == "WORK":
        b = open("dataset/metadata/master_graph.json", "rb").read()
    else:
        b = subprocess.run(["git", "show", ref + ":dataset/metadata/master_graph.json"],
                           capture_output=True).stdout
    return b, json.loads(b.decode("utf-8"))


def medir(ref):
    b, g = cargar(ref)
    sha = hashlib.sha256(b).hexdigest()
    items = list(g["nodos"].items())
    total = len(items)
    dep = sum(1 for _, n in items if n.get("deprecado"))
    sig = sum(len(n.get("nodos_siguientes") or []) for _, n in items)
    prev = sum(len(n.get("nodos_previos") or []) for _, n in items)
    union = set()
    auto = 0
    for i, n in items:
        for d in (n.get("nodos_siguientes") or []):
            union.add((i, d))
            auto += (d == i)
        for o in (n.get("nodos_previos") or []):
            union.add((o, i))
            auto += (o == i)
    return dict(ref=ref, sha=sha, total=total, deprecado=dep,
                vivos=total - dep, sig=sig, prev=prev, suma=sig + prev,
                union=len(union), auto=auto), union


unis = {}
for r in REFS:
    m, u = medir(r)
    unis[r] = u
    print(json.dumps(m, ensure_ascii=False))

ap, tr = unis["325f537c"], unis["WORK"]
print("BORRADAS (apertura menos trabajo):", len(ap - tr))
for e in sorted(ap - tr):
    print("  -", e)
print("NUEVAS (trabajo menos apertura):", len(tr - ap))
for e in sorted(tr - ap):
    print("  +", e)
