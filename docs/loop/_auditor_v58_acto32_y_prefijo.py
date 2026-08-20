# -*- coding: utf-8 -*-
# 1) Varas del acto 32 (hoy == blob pre fusion, verificado campo a campo antes).
# 2) Prefijo: cuantos actos de los tramos 1-4 tienen HOY sus dos miembros vivos.
import json, io, glob

G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
ALIAS = {}
for k, v in G.items():
    for x in (v.get("ids_alias") or []):
        ALIAS[x] = k

def res(x):
    vistos = set()
    while x in ALIAS and x not in vistos:
        vistos.add(x)
        x = ALIAS[x]
    return x

def varas(nid):
    o = json.load(io.open("dataset/nodos/%s.json" % nid, encoding="utf-8"))
    cab = {res(y) for c in ("nodos_previos", "nodos_siguientes") for y in (o.get(c) or [])} - {res(nid)}
    return len(o.get("pasos_accionables") or []), len(o.get("condiciones_activacion") or []), len(cab)

a = "programa_de_referidos_de_franquiciados"
b = "referidos_franquiciados_existentes"
print("acto 32:", a, varas(a), "|", b, varas(b))

def vivo(nid):
    n = G.get(nid)
    return n is not None and not n.get("deprecado")

total = 0
for t in ["docs/loop/TRAMO1_V49.jsonl", "docs/loop/TRAMO2_V54.jsonl", "docs/loop/TRAMO3_V56.jsonl", "docs/loop/TRAMO4_V57.jsonl"]:
    hits = glob.glob(t) or glob.glob(t.replace("_V49", "_*").replace("_V54", "_*").replace("_V56", "_*").replace("_V57", "_*"))
    if not hits:
        print("SIN FICHERO para", t)
        continue
    vivos_t = 0
    for l in io.open(hits[0], encoding="utf-8"):
        f = json.loads(l)
        if all(vivo(m) for m in f["miembros"]):
            vivos_t += 1
    print(hits[0], "-> actos con los dos miembros vivos:", vivos_t)
    total += vivos_t
print("PREFIJO TOTAL:", total)
