# -*- coding: utf-8 -*-
"""_auditor_v94_grafo.py . EL INSTRUMENTO DEL AUDITOR DE LA VUELTA 94: las ocho
cifras del grafo en dos refs, con sha256 en las dos, y el diff de la union
entera de aristas dirigidas.

ESTE FICHERO ES EL QUE PRODUCE docs/loop/_auditor_v94_grafo.txt. Se corre asi:

    python docs/loop/_auditor_v94_grafo.py > docs/loop/_auditor_v94_grafo.txt

y su salida tiene que ser identica a la commiteada. La razon de que la
docstring lo diga con estas palabras es que el instrumento equivalente de la
vuelta 93 (_auditor_v93_grafo.py) NO reproducia su propia salida (buscaba una
clave "nodes" que master_graph.json no tiene), y eso quedo declarado como caida
de procedimiento del auditor en el acta de la vuelta 94, seccion 7.1.
"""
import hashlib
import json
import subprocess

APERTURA = "267365c8"
CIERRE = "WORK"


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
    dep_en = sum(1 for _, n in items if n.get("deprecated"))
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
    return dict(ref=ref, sha=sha, total=total, deprecado=dep, deprecated_en=dep_en,
                vivos=total - dep, sig=sig, prev=prev, suma=sig + prev,
                union=len(union), auto=auto), union


a, ua = medir(APERTURA)
b, ub = medir(CIERRE)
for m in (a, b):
    print(json.dumps(m, ensure_ascii=False))
sa = ua - ub
sb = ub - ua
print("SOLO EN APERTURA (borradas):", len(sa))
for x in sorted(sa):
    print("   -", x)
print("SOLO EN CIERRE (nuevas):", len(sb))
for x in sorted(sb):
    print("   +", x)
print("DELTA sig/prev/suma/union:", b["sig"] - a["sig"], b["prev"] - a["prev"],
      b["suma"] - a["suma"], b["union"] - a["union"])
