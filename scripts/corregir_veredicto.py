#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""corregir_veredicto.py . cambia la clase y la razon de veredictos YA registrados.

Entrada: un fichero JSONL con objetos {"puesto": N, "clase": "A|B|C|D", "razon": "..."}

A diferencia de registrar_veredictos.py, este NO anade: SUSTITUYE. Se usa solo
cuando una relectura tumba un veredicto, y siempre con correccion declarada
escrita dentro de la propia razon.

Comprueba antes de escribir:
  - que el puesto YA este registrado (si no lo esta, es un alta y va por el otro script)
  - que la clase sea valida
  - que el total de veredictos no cambie
Imprime el antes y el despues de cada puesto y el marcador recomputado.
"""
import json, io, sys, argparse, collections

ap = argparse.ArgumentParser()
ap.add_argument("lote")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")

VER = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
idx = {r["puesto_intra"]: i for i, r in enumerate(V)}
lote = [json.loads(l) for l in io.open(a.lote, encoding="utf-8") if l.strip()]
antes = len(V)

for x in lote:
    n = x["puesto"]
    assert n in idx, "puesto %d NO esta registrado: eso es un alta, va por registrar_veredictos.py" % n
    assert x["clase"] in ("A", "B", "C", "D"), "clase invalida en %d" % n
    r = V[idx[n]]
    print("puesto %d | %s -> %s | %s contra %s" % (n, r["clase"], x["clase"], r["nodo_a"], r["nodo_b"]))
    r["clase"] = x["clase"]
    r["razon"] = x["razon"]

assert len(V) == antes, "el total cambio: %d -> %d" % (antes, len(V))
io.open(VER, "w", encoding="utf-8", newline="\n").write(
    "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in V))
c = collections.Counter(r["clase"] for r in V)
print("corregidos %d | archivo %d veredictos, sin altas ni bajas" % (len(lote), len(V)))
print("marcador: %s | tasa de A %.1f%%" % (dict(c), 100.0 * c["A"] / len(V)))
