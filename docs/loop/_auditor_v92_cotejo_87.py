# -*- coding: utf-8 -*-
"""Cotejo propio del auditor v92: las 87 filas de OP_E_07_DIRECCION_V92.jsonl
resueltas por alias contra el grafo del arbol de trabajo."""
import io, json, os
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = json.load(io.open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"), encoding="utf-8"))["nodos"]
ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}
def res(x):
    visto=set()
    while x in ALIAS and x not in visto:
        visto.add(x); x=ALIAS[x]
    return x

nodos = {}
d = os.path.join(RAIZ,"dataset","nodos")
for f in sorted(os.listdir(d)):
    if f.endswith(".json"):
        nodos[f[:-5]] = json.load(io.open(os.path.join(d,f), encoding="utf-8"))

def existe(m,h):
    return h in (nodos.get(m,{}).get("nodos_siguientes") or [])
def existe_prev(m,h):
    return m in (nodos.get(h,{}).get("nodos_previos") or [])

filas=[json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","plan","OP_E_07_DIRECCION_V92.jsonl"),encoding="utf-8") if l.strip()]
print("filas V92:", len(filas))
resueltas=[]
faltan=[]
media=[]
for p in filas:
    m,h=res(p["madre"]),res(p["hijo"])
    resueltas.append((m,h))
    if not existe(m,h): faltan.append((p["puesto"],p["madre"],p["hijo"],m,h,"falta en nodos_siguientes"))
    elif not existe_prev(m,h): media.append((p["puesto"],m,h,"falta la vista nodos_previos"))
distintas=set(resueltas)
print("pares resueltos distintos:", len(distintas))
print("filas que colapsan a un par ya visto (YA_ESTABA esperados):",
      sorted(p["puesto"] for i,p in enumerate(filas) if resueltas[i] in [resueltas[j] for j in range(i)]))
print("FALTAN EN EL GRAFO:", len(faltan))
for x in faltan: print("   ", x)
print("MEDIA ARISTA (solo una vista):", len(media))
for x in media: print("   ", x)
# el 1098
m,h=res("customer_validation_sell_phase"),res("prueba_solucion_con_cliente")
print("\n1098 resuelto:", m, "->", h)
print("1098 en nodos_siguientes:", existe(m,h), "| en nodos_previos:", existe_prev(m,h))
