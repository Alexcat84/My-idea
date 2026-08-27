"""Auditor v80: escalera de las 2 aristas nuevas (el hijo ya apuntaba a la madre
ANTES de escribir, grafo de c25403a0) + la direccion inversa del par 28."""
import json, sys, subprocess
G = json.loads(subprocess.run(["git","show","c25403a0:dataset/metadata/master_graph.json"],
                              capture_output=True).stdout.decode("utf-8"))["nodos"]
W = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
nuevas = [("curva_caracteristica_operativa","distribucion_binomial"),
          ("desarrollo_de_controles_de_proceso","bucle_retroalimentacion_control")]
print("--- ESCALERA, sobre el grafo de c25403a0 (ANTES de escribir) ---")
inv=0
for m,h in nuevas:
    e = h in (G[m].get("nodos_siguientes") or [])
    i = m in (G[h].get("nodos_siguientes") or [])
    if i: inv+=1
    print(f"  {m} -> {h} | ya estaba: {e} | INVERSA (hijo->madre) ya estaba: {i}")
print(f"  INVERSAS: {inv} de {len(nuevas)}")
print("\n--- LAS 2, EN EL GRAFO DE HOY, EN LAS DOS VISTAS ---")
for m,h in nuevas:
    print(f"  {m} -> {h} | en siguientes de madre: {h in (W[m].get('nodos_siguientes') or [])}"
          f" | en previos de hijo: {m in (W[h].get('nodos_previos') or [])}"
          f" | inversa presente: {m in (W[h].get('nodos_siguientes') or [])}")
print("\n--- PAR 28: la direccion inversa, medida ---")
a,b = "qfd_matriz","identificar_clientes_externos_e_internos"
print(f"  arista {b} -> {a} directa: {a in (W[b].get('nodos_siguientes') or [])}")
from collections import deque
ady = {n:[d for d in (W[n].get('nodos_siguientes') or []) if d in W] for n in W}
def camino(o,d,tope=6):
    if o==d: return [o]
    vis={o}; q=deque([(o,[o])])
    while q:
        c,p=q.popleft()
        if len(p)>tope: continue
        for x in ady.get(c,[]):
            if x==d: return p+[x]
            if x not in vis: vis.add(x); q.append((x,p+[x]))
    return None
p1=camino(b,a); p2=camino(a,b)
print(f"  camino {b} -> {a}: {' -> '.join(p1) if p1 else 'NINGUNO <=6 saltos'}")
print(f"  camino {a} -> {b}: {' -> '.join(p2) if p2 else 'NINGUNO <=6 saltos'}")
