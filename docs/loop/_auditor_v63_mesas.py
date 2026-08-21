# -*- coding: utf-8 -*-
# Censo del auditor, vuelta 63: TODAS las operaciones OP-M-* con nomina de
# nodos, medidas contra el grafo de HOY (vivos, deprecados, y si el par ya
# resuelve a un solo vivo por la cadena de alias, P.1). Solo lectura.
# Ademas: la medicion del puesto 2 (desbloqueos por depende_de, la vara
# general de la vuelta 47).
import json, os, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

nodos = {}
for raiz, _d, fs in os.walk("dataset/nodos"):
    for f in fs:
        if f.endswith(".json"):
            d = json.load(open(os.path.join(raiz, f), encoding="utf-8"))
            nodos[d.get("node_id") or f[:-5]] = d

alias = {}
for nid, d in nodos.items():
    for a in (d.get("ids_alias") or []):
        alias[a] = nid

def vivo(d):
    return not (d.get("deprecado") or d.get("deprecated") or d.get("estado") == "deprecado")

def resolver(n):
    vistos = set()
    while n in alias and n not in vistos:
        vistos.add(n)
        n = alias[n]
    return n

ops = [json.loads(l) for l in open("docs/plan/OPERACIONES.jsonl", encoding="utf-8") if l.strip()]

print("=== CENSO DE FICHAS OP-M-* CONTRA EL GRAFO DE HOY ===")
for o in ops:
    if not o["id_op"].startswith("OP-M"):
        continue
    ns = o.get("nodos") or []
    if not ns:
        print("%-22s fase %-12s SIN nomina de nodos" % (o["id_op"], o.get("fase")))
        continue
    estados = []
    for n in ns:
        if n not in nodos:
            estados.append(n + ":NO EXISTE")
        elif vivo(nodos[n]):
            estados.append(n + ":VIVO")
        else:
            estados.append(n + ":DEPRECADO->" + resolver(n))
    res = set(resolver(n) for n in ns if n in nodos)
    sup = o.get("superviviente")
    sup_estado = "SIN SUPERVIVIENTE EN FICHA" if not sup else (
        "VIVO" if (sup in nodos and vivo(nodos[sup])) else "DEPRECADO O AUSENTE")
    consumido = "CONSUMIDO (resuelven a %d vivo)" % len(res) if len(res) == 1 and len(ns) > 1 else (
        "PENDIENTE (%d resueltos distintos)" % len(res))
    print("%-22s fase %-12s %s | superviviente ficha: %s (%s)" %
          (o["id_op"], o.get("fase"), consumido, sup, sup_estado))
    for e in estados:
        print("      " + e)

print()
print("=== PUESTO 2 DE LA FASE 03, LA VARA GENERAL DE LA VUELTA 47 ===")
print("empatadas por campo orden == 2 en fase 03_FUSIONES:")
cand = [o["id_op"] for o in ops if o.get("fase") == "03_FUSIONES" and o.get("orden") == 2]
print("  ", cand)
for c in cand:
    dep = [o["id_op"] for o in ops if c in (o.get("depende_de") or [])]
    print("  %-18s desbloquea %d: %s" % (c, len(dep), dep))
