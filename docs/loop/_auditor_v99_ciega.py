# -*- coding: utf-8 -*-
"""CIEGA v99: vuelca los dos nodos de un puesto de OP-E-03 SIN clase ni razon.
Uso: python docs/loop/_auditor_v99_ciega.py 152 156 157 ...
     python docs/loop/_auditor_v99_ciega.py --muestra   (elige la muestra adversarial)
"""
import json, sys, glob, statistics

G = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
FIL = {}
for f in glob.glob("docs/plan/OP_E_03_LECTURA_TRAMO*.jsonl"):
    for l in open(f, encoding="utf-8"):
        if l.strip():
            r = json.loads(l); FIL[r["puesto_tramo"]] = r
BOLSA = {}
for i, l in enumerate(open("docs/plan/DIFERENCIA_CONTRA_COLA.jsonl", encoding="utf-8"), 1):
    if l.strip(): BOLSA[i] = json.loads(l)

def volcar(n, etq):
    d = G.get(n, {})
    print(f"  [{etq}] id={n}")
    print(f"    titulo: {d.get('titulo_concepto')}")
    print(f"    entregable: {d.get('entregable_esperado')}")
    for i, p in enumerate(d.get("pasos_accionables") or [], 1):
        print(f"    paso {i}: {p}")

if sys.argv[1] == "--muestra":
    t4 = [FIL[p] for p in range(151, 184)]
    con = [(BOLSA[r["puesto_tramo"]]["titulo_ratio"], r["puesto_tramo"]) for r in t4 if r.get("direccion_leida")]
    sin = [(BOLSA[r["puesto_tramo"]]["titulo_ratio"], r["puesto_tramo"]) for r in t4 if not r.get("direccion_leida")]
    print("NO RESUELTAS de mayor titulo_ratio (contra el ejecutor):", sorted(sin, reverse=True)[:5])
    print("RESUELTAS de menor titulo_ratio (contra el ejecutor):", sorted(con)[:5])
    sys.exit(0)

for p in sys.argv[1:]:
    p = int(p); r = FIL[p]
    print("=" * 100)
    print(f"PUESTO {p}   dominio={r['dominio']}   paso casado por el barrido={r['paso_casado']}   titulo_ratio={BOLSA[p]['titulo_ratio']}")
    volcar(r["madre_de_la_bolsa"], "MADRE segun la bolsa")
    volcar(r["hijo_de_la_bolsa"], "HIJO segun la bolsa")
    print()
