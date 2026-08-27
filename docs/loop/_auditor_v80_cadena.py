"""Auditor v80: vara de la cadena, corrida POR MI sobre las 30 unidades de
cabeza de PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl, con el grafo de c25403a0
(el de la TAREA 3, ANTES de las dos escrituras del tramo 6) en disco."""
import json
from collections import deque

G = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
ady = {n: [d for d in (G[n].get("nodos_siguientes") or []) if d in G] for n in G}

def camino(o, d, tope=6):
    if o == d: return [o]
    vis={o}; q=deque([(o,[o])])
    while q:
        c,p=q.popleft()
        if len(p)>tope: continue
        for x in ady.get(c,[]):
            if x==d: return p+[x]
            if x not in vis: vis.add(x); q.append((x,p+[x]))
    return None

filas=[json.loads(l) for l in open("docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl",encoding="utf-8") if l.strip()]
print(f"filas del fichero filtrado: {len(filas)}")
n=0
for i,f in enumerate(filas[:30]):
    p=camino(f["madre"],f["hijo"])
    if p: n+=1
    marca = f"ALCANZABLE ({len(p)-1} saltos): {' -> '.join(p)}" if p else "sin camino previo"
    print(f"  {i}: {f['madre']} -> {f['hijo']} (paso {f['paso']}) | {marca}")
print(f"\nDE LAS 30 DE CABEZA, CON CAMINO PREVIO: {n}")
