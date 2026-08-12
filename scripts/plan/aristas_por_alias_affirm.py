# -*- coding: utf-8 -*-
"""LAS ARISTAS QUE ATRAVIESAN EL ALIAS DE LA FASE 3 DE COLEMAN.
   Solo lectura. Verifica que la fusion ya hecha SOSTIENE el grafo:
   quien apunta a un id que hoy solo existe como alias, y a donde llega."""
import json, io, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
DEST = "fase_affirm_buyers_remorse"
ALIAS = G[DEST].get("ids_alias") or []
print("DESTINO:", DEST, "| deprecado:", G[DEST].get("deprecado"))
print("ALIAS QUE CARGA:", ALIAS)
for a in ALIAS:
    print("   %-40s existe como nodo: %-5s deprecado: %s" % (a, a in G, G[a].get("deprecado") if a in G else "no aplica"))
print()
S = set(ALIAS)
filas = []
for k, v in G.items():
    if v.get("deprecado"): continue
    for campo in ("nodos_previos", "nodos_siguientes"):
        for y in (v.get(campo) or []):
            if y in S:
                filas.append((k, campo, y))
print("ARISTAS VIVAS QUE APUNTAN A UN ALIAS Y SOLO LLEGAN POR EL RESOLUTOR: %d" % len(filas))
for k, campo, y in sorted(filas):
    print("   %-46s %-17s -> %-42s  [%s]" % (k, campo, y, (G[k].get("dominio") or "?")))
print()
print("Y LAS ARISTAS PROPIAS DEL DESTINO, las que si son literales:")
for campo in ("nodos_previos", "nodos_siguientes"):
    for y in (G[DEST].get(campo) or []):
        viv = y in G and not G[y].get("deprecado")
        print("   %-17s -> %-44s vivo: %s" % (campo, y, viv))
print()
print("QUIEN APUNTA AL DESTINO POR SU NOMBRE PROPIO:")
n = 0
for k, v in G.items():
    if v.get("deprecado"): continue
    for campo in ("nodos_previos", "nodos_siguientes"):
        if DEST in (v.get(campo) or []):
            print("   %-46s %s" % (k, campo)); n += 1
print("   total %d" % n)
