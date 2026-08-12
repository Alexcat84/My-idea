# -*- coding: utf-8 -*-
"""Verificacion del cableado de la mesa de la junta asesora ANTES de escribir la
   operacion. Solo lectura. Simula las dos fusiones sobre una COPIA en memoria."""
import json, io, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
IC, IJ = "identificar_consejo_asesores", "identificar_junta_asesores"
FZ, FB = "formalizar_junta_asesora", "formalize_advisory_board"
print("ALIAS QUE YA CARGAN HOY:")
for k in (IC, IJ, FZ, FB): print("   %-32s %s" % (k, G[k].get("ids_alias")))
print()
print("LA ARISTA ENTRE LOS DOS QUE SI SE TOCAN, campo por campo:")
for a, b in ((FZ, IJ), (IJ, FZ)):
    for campo in ("nodos_previos", "nodos_siguientes"):
        if b in (G[a].get(campo) or []): print("   %-30s.%-17s contiene %s" % (a, campo, b))
print()
# simulacion de las dos fusiones: IJ -> IC, FB -> FZ
AL = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}
AL[IJ] = IC; AL[FB] = FZ
def res(x):
    s = set()
    while x in AL and x not in s: s.add(x); x = AL[x]
    return x
print("TRAS LAS DOS FUSIONES, las aristas que quedan entre madre e hijo:")
for a in (IC, FZ):
    for campo in ("nodos_previos", "nodos_siguientes"):
        dest = sorted(set(res(y) for y in (G[a].get(campo) or [])))
        rel = [d for d in dest if d in (IC, FZ) and d != a]
        print("   %-30s.%-17s -> %s" % (a, campo, rel or "NADA hacia el otro"))
print()
print("   NOTA: los nodos que mueren (IJ y FB) pierden sus listas; solo cuentan las del superviviente.")
print()
print("QUIEN APUNTA A CADA UNO DE LOS CUATRO, y como queda tras resolver:")
for k, v in G.items():
    if v.get("deprecado"): continue
    for campo in ("nodos_previos", "nodos_siguientes"):
        L = v.get(campo) or []
        hits = [y for y in L if y in (IC, IJ, FZ, FB)]
        if not hits: continue
        resu = [res(y) for y in hits]
        marca = "  <== DUPLICADA TRAS FUSION" if len(resu) != len(set(resu)) else ""
        print("   %-40s %-17s %s -> %s%s" % (k, campo, hits, resu, marca))
