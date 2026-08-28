# -*- coding: utf-8 -*-
"""Vara propia del auditor v99: censo, aristas y sha del grafo en cada ref."""
import json, hashlib, subprocess

def medir(txt):
    g = json.loads(txt)
    nodos = g["nodos"]
    items = list(nodos.values())
    total = len(items)
    dep = sum(1 for n in items if n.get("deprecado"))
    sig = sum(len(n.get("nodos_siguientes") or []) for n in items)
    prev = sum(len(n.get("nodos_previos") or []) for n in items)
    union = set(); auto = 0
    for k, n in nodos.items():
        i = n.get("node_id") or k
        for d in (n.get("nodos_siguientes") or []):
            union.add((i, d))
            if d == i: auto += 1
        for o in (n.get("nodos_previos") or []):
            union.add((o, i))
            if o == i: auto += 1
    return total, total - dep, dep, sig, prev, sig + prev, len(union), auto, union

RUTA = "dataset/metadata/master_graph.json"
refs = ["de4cc0e2", "bcc389ee", "f5ff3d03", "acb897c7", "47d456e2", "9fdb8228"]
prev_union = None
for r in refs:
    b = subprocess.run(["git", "show", f"{r}:{RUTA}"], capture_output=True).stdout
    sha = hashlib.sha256(b).hexdigest()
    t, v, d, s, p, su, u, a, un = medir(b.decode("utf-8"))
    print(f"{r}  sha256={sha[:20]}  censo {t}/{v}/{d}  aristas {s}/{p}/{su}/{u}  auto {a}")
    if prev_union is not None:
        print(f"     vs anterior: borradas {len(prev_union - un)}  nuevas {len(un - prev_union)}")
    prev_union = un
b = open(RUTA, "rb").read().replace(b"\r\n", b"\n")
sha = hashlib.sha256(b).hexdigest()
t, v, d, s, p, su, u, a, un = medir(b.decode("utf-8"))
print(f"ARBOL_TRABAJO(LF)  sha256={sha[:20]}  censo {t}/{v}/{d}  aristas {s}/{p}/{su}/{u}  auto {a}")
print(f"     vs 9fdb8228: borradas {len(prev_union - un)}  nuevas {len(un - prev_union)}")
