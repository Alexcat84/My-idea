# -*- coding: utf-8 -*-
"""AUDITOR vuelta 88. BFS propio: camino mas corto madre -> hijo (sin usar la
arista directa madre->hijo), y los pasos de la madre al lado, para adjudicar
si el camino es LA CADENA PROPIA (adjudicacion 6.1 del acta 83).
"""
import collections
import json
import sys

nodos = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]


def bfs(madre, hijo, tope=8):
    if madre not in nodos or hijo not in nodos:
        return None
    q = collections.deque([(madre, [madre])])
    visto = {madre}
    while q:
        cur, cam = q.popleft()
        if len(cam) > tope:
            continue
        for d in (nodos[cur].get("nodos_siguientes") or []):
            if cur == madre and d == hijo:
                continue        # se ignora la arista directa
            if d == hijo:
                return cam + [d]
            if d not in visto:
                visto.add(d)
                q.append((d, cam + [d]))
    return None


PARES = [(a, b) for a, b in (x.split("->") for x in sys.argv[1:])]
for madre, hijo in PARES:
    madre, hijo = madre.strip(), hijo.strip()
    print("=" * 78)
    print("PAR: %s -> %s" % (madre, hijo))
    m = nodos.get(madre) or {}
    print("PASOS DE LA MADRE (%s):" % (m.get("titulo_concepto") or "?"))
    for i, p in enumerate(m.get("pasos_accionables") or [], 1):
        print("   %d. %s" % (i, p))
    cam = bfs(madre, hijo)
    if cam is None:
        print("SIN CAMINO (horizonte 8, ignorando la arista directa)")
        continue
    print("CAMINO MAS CORTO (%d saltos, ignorando la arista directa):" % (len(cam) - 1))
    for n in cam:
        v = nodos.get(n) or {}
        print("   %-46s  %s" % (n, v.get("titulo_concepto")))
    print("INTERMEDIOS (ni madre ni hijo): %d" % max(0, len(cam) - 2))
    print()
