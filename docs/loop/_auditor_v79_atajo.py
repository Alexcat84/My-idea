"""Auditor v79: LA VARA DE LA FORMA (banco 9.6.1, caveat de la familia ENCADENADA).
Para cada arista nueva madre->hijo, mide si en el grafo de la APERTURA el hijo YA ERA
ALCANZABLE desde la madre por nodos_siguientes, y con que camino mas corto.
Una arista sobre un hijo ya alcanzable NO es 'contenido huerfano de camino' (banco 9.6)."""
import sys, json
from collections import deque
sys.path.insert(0, "docs/loop")
from _auditor_v79_conteo import medir, cargar

A = medir("aea7cc81"); B = medir("WORK")
nuevas = sorted(B["S"] - A["S"])
G = cargar("aea7cc81")["nodos"]
ady = {n: [d for d in (G[n].get("nodos_siguientes") or []) if d in G] for n in G}

def camino(o, d, tope=6):
    if o == d: return [o]
    vis = {o}; q = deque([(o, [o])])
    while q:
        c, p = q.popleft()
        if len(p) > tope: continue
        for x in ady.get(c, []):
            if x == d: return p + [x]
            if x not in vis:
                vis.add(x); q.append((x, p + [x]))
    return None

atajos = 0
for m, h in nuevas:
    p = camino(m, h)
    if p:
        atajos += 1
        print(f"YA ALCANZABLE (salto {len(p)-1}) | {m} -> {h}")
        print(f"     camino previo: {' -> '.join(p)}")
    else:
        print(f"huerfano de camino    | {m} -> {h}   (no habia camino <=6 saltos)")
print(f"\nDE LAS {len(nuevas)} NUEVAS, EL HIJO YA ERA ALCANZABLE DESDE LA MADRE EN: {atajos}")
