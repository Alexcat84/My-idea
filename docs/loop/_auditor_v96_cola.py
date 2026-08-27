# -*- coding: utf-8 -*-
"""Vara PROPIA del auditor 96: reproduce, sin mirar el codigo del ejecutor mas
que para saber que la cola sale de PARES+VEREDICTOS resueltos, los 2.796 pares
distintos de la cola y el cruce contra las 40 filas del tramo 1."""
import json, io

G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
alias = {}
for k, v in G.items():
    for a in (v.get("ids_alias") or []):
        alias[a] = k

def res(x):
    visto = set()
    while x in alias and x not in visto:
        visto.add(x); x = alias[x]
    return x

def jl(r): return [json.loads(l) for l in io.open(r, encoding="utf-8") if l.strip()]

pares = jl("docs/INTRA_DOMINIO_PARES.jsonl")
vere  = jl("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
tramo = jl("docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl")

print("PARES:", len(pares), " VEREDICTOS:", len(vere))
crudos = {frozenset((r["nodo_a"], r["nodo_b"])) for r in pares + vere}
print("pares distintos SIN resolver:", len(crudos))
cola = {frozenset((res(r["nodo_a"]), res(r["nodo_b"])))
        for r in pares + vere if res(r["nodo_a"]) != res(r["nodo_b"])}
print("pares distintos EN LA COLA TRAS RESOLVER:", len(cola))

vistos, choques, movidos, inexistentes = set(), [], [], []
for r in tramo:
    m, h = res(r["madre_de_la_bolsa"]), res(r["hijo_de_la_bolsa"])
    if m != r["madre_de_la_bolsa"] or h != r["hijo_de_la_bolsa"]:
        movidos.append((r["puesto_tramo"], r["madre_de_la_bolsa"], m, r["hijo_de_la_bolsa"], h))
    for x in (m, h):
        if x not in G: inexistentes.append((r["puesto_tramo"], x))
    p = frozenset((m, h))
    if p in cola: choques.append((r["puesto_tramo"], m, h))
    if p in vistos: choques.append(("REPETIDA", r["puesto_tramo"], m, h))
    vistos.add(p)

print("filas del tramo:", len(tramo), " pares distintos dentro del tramo:", len(vistos))
print("filas del tramo YA EN LA COLA:", len(choques), choques)
print("ids que el resolutor MOVIO:", len(movidos), movidos)
print("nodos que no existen en el grafo:", len(inexistentes), inexistentes)
