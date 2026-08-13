#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""recomputar_marcador.py . recomputa el marcador y las tasas del cribado.

SOLO LECTURA. No toca ni un nodo ni un veredicto.

Uso:  python scripts/recomputar_marcador.py 3000
      python scripts/recomputar_marcador.py 3000 --dominio quality --desde 2901
"""
import json, io, sys, argparse, collections

ap = argparse.ArgumentParser()
ap.add_argument("corte", type=int)
ap.add_argument("--dominio", default=None)
ap.add_argument("--desde", type=int, default=None, help="inicio del tramo para la vara por 25")
ap.add_argument("--hasta", type=int, default=None, help="fin del tramo para la vara por 25")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")

V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
V = [p for p in V if p["puesto_intra"] <= a.corte]
n = len(V)
puestos = set(p["puesto_intra"] for p in V)
huecos = set(range(1, a.corte + 1)) - puestos
dups = n - len(puestos)
print("n =", n, "corte =", a.corte, "huecos:", sorted(huecos)[:10], "dups(puesto):", dups)

claves = collections.Counter((p["nodo_a"], p["nodo_b"], p["dominio"]) for p in V)
dupclaves = [k for k, c in claves.items() if c > 1]
print("pares duplicados (nodo_a,nodo_b,dominio):", len(dupclaves))

cnt = collections.Counter(p["clase"] for p in V)
print("\nMARCADOR GLOBAL")
for k in ("A", "B", "C", "D"):
    print(" ", k, cnt[k], round(cnt[k] / n * 100, 1))

print("\nTASA POR DOMINIO")
byd = collections.defaultdict(lambda: collections.Counter())
for p in V:
    byd[p["dominio"]][p["clase"]] += 1
for dom in sorted(byd):
    c = byd[dom]
    nd = sum(c.values())
    print(" ", dom, nd, c.get("A", 0), round(c.get("A", 0) / nd * 100, 1))

if a.dominio and a.desde and a.hasta:
    q = [p for p in V if p["dominio"] == a.dominio and a.desde <= p["puesto_intra"] <= a.hasta]
    print("\nVARA POR TRAMO DE 25, dominio=%s, %d-%d, n=%d" % (a.dominio, a.desde, a.hasta, len(q)))
    for start in range(a.desde, a.hasta + 1, 25):
        end = min(start + 24, a.hasta)
        seg = [p for p in q if start <= p["puesto_intra"] <= end]
        if not seg:
            continue
        ac = sum(1 for p in seg if p["clase"] == "A")
        print("  %d-%d n=%d A=%d tasa=%.1f%%" % (start, end, len(seg), ac, ac / len(seg) * 100))
