#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""registrar_veredictos.py . anade veredictos al archivo, en orden y sin huecos.

Entrada: un fichero JSONL con objetos {"puesto": N, "clase": "A|B|C|D", "razon": "..."}
Los campos dominio, nodo_a, nodo_b, clave y banda se toman de la COLA, no se escriben
a mano: asi no se puede registrar un veredicto contra un par que no existe.

Comprueba antes de escribir:
  - que el puesto exista en la cola
  - que no este ya registrado
  - que la secuencia quede SIN HUECOS desde 1
"""
import json, io, sys, argparse

ap = argparse.ArgumentParser()
ap.add_argument("lote")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
P = {p["puesto_intra"]: p for p in
     (json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip())}
V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
ya = {r["puesto_intra"] for r in V}
lote = [json.loads(l) for l in io.open(a.lote, encoding="utf-8") if l.strip()]

nuevos = []
for x in lote:
    n = x["puesto"]
    assert n in P, "puesto %d no esta en la cola" % n
    assert n not in ya, "puesto %d YA registrado" % n
    assert x["clase"] in ("A", "B", "C", "D"), "clase invalida en %d" % n
    p = P[n]
    nuevos.append({"puesto_intra": n, "dominio": p["dominio"], "nodo_a": p["nodo_a"], "nodo_b": p["nodo_b"],
                   "clave": None, "banda_078_080": p.get("banda_078_080", False),
                   "clase": x["clase"], "razon": x["razon"]})
    ya.add(n)

V += nuevos
V.sort(key=lambda r: r["puesto_intra"])
faltan = [i for i in range(1, max(ya) + 1) if i not in ya]
assert not faltan, "HUECOS: %s" % faltan[:20]
io.open(VER, "w", encoding="utf-8", newline="\n").write(
    "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in V))
import collections
c = collections.Counter(r["clase"] for r in V)
print("registrados %d | archivo %d veredictos, hasta el puesto %d, sin huecos" % (len(nuevos), len(V), max(ya)))
print("marcador: %s | tasa de A %.1f%%" % (dict(c), 100.0 * c["A"] / len(V)))
