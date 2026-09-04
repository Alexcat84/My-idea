# -*- coding: utf-8 -*-
"""POR QUE FALLA LA COMPROBACION ii, MEDIDO Y NO SUPUESTO (auditor, vuelta 166).

Mismo cargador, mismo resolutor y mismo criterio que scripts/plan/recomputo_3388.py.
"""
import collections
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = json.load(io.open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]
ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}


def res(x, visto=None):
    visto = visto or set()
    while x in ALIAS and x not in visto:
        visto.add(x)
        x = ALIAS[x]
    return x


V = [json.loads(l) for l in io.open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"), encoding="utf-8") if l.strip()]

retrato = collections.OrderedDict()
for r in V:
    if r["clase"] != "A":
        continue
    ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
    if ra != rb:
        retrato.setdefault(frozenset((ra, rb)), []).append(r)

# el `leido` del instrumento: ULTIMO GANA, sin mirar la clase
leido = {}
for r in V:
    ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
    if ra == rb:
        continue
    leido[frozenset((ra, rb))] = r

print("A) RETRATO (pares resueltos distintos con al menos una fila A): %d" % len(retrato))

perdidos = [k for k in retrato if leido[k]["clase"] != "A"]
print("B) PARES DEL RETRATO QUE EL `leido` DEL INSTRUMENTO NO CUENTA COMO A: %d" % len(perdidos))
for k in perdidos:
    filas = [(r["puesto_intra"], r["clase"]) for r in V
             if frozenset((res(r["nodo_a"]), res(r["nodo_b"]))) == k]
    print("   %s" % sorted(k))
    print("      todas sus filas crudas (puesto, clase): %s" % filas)
    print("      la que el instrumento guarda (ULTIMA del fichero): puesto %d clase %s"
          % (leido[k]["puesto_intra"], leido[k]["clase"]))

print()
print("C) LA RESTA: %d menos %d es %d, y %d es exactamente la 'suma de aristas A internas'"
      " que el instrumento imprime en su comprobacion ii."
      % (len(retrato), len(perdidos), len(retrato) - len(perdidos), len(retrato) - len(perdidos)))
