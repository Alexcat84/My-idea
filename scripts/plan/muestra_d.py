# -*- coding: utf-8 -*-
"""Sorteo pineado y estratificado de 24 veredictos D. Semilla y metodo declarados
   en docs/plan/PIN_MUESTRA_D.txt ANTES de mirar. Solo lectura."""
import json, io, sys, random, collections, argparse
sys.stdout.reconfigure(encoding="utf-8")
ap = argparse.ArgumentParser(); ap.add_argument("--destapar", action="store_true"); a = ap.parse_args()
SEMILLA = 20260812
CUOTA = {"core": 15, "entrega": 2, "compras": 2, "environmental": 2, "exportacion": 2, "franquicias": 1}
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
D = [r for r in V if r["clase"] == "D"]
por = collections.defaultdict(list)
for r in D:
    por[r["dominio"]].append(r)
sel = []
for i, dom in enumerate(sorted(por)):
    if dom not in CUOTA:
        continue
    lote = sorted(por[dom], key=lambda r: r["puesto_intra"])
    sel += random.Random(SEMILLA + i).sample(lote, CUOTA[dom])
sel.sort(key=lambda r: (r["dominio"], r["puesto_intra"]))
print("MUESTRA DE %d D, semilla %d, estratificada: %s" % (len(sel), SEMILLA, dict(CUOTA)))
for i, r in enumerate(sel, 1):
    print("=" * 78)
    print("D-%02d  puesto %d  [%s]" % (i, r["puesto_intra"], r["dominio"]))
    if a.destapar:
        print("  RAZON VIEJA: %s" % r["razon"])
        continue
    for k in (r["nodo_a"], r["nodo_b"]):
        n = G.get(k) or {}
        print("  --- %s" % k)
        print("      %s" % (n.get("titulo_concepto") or "SIN NODO"))
        print("      entregable: %s" % (n.get("entregable_esperado") or "")[:120])
        for j, s in enumerate(n.get("pasos_accionables") or [], 1):
            print("      %d. %s" % (j, s[:135]))
