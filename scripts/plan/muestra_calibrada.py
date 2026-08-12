# -*- coding: utf-8 -*-
"""Sorteo pineado de 24 sobre la bolsa reducida. Semilla declarada en
   docs/plan/PIN_SORTEO_CALIBRADO.txt ANTES de mirar los candidatos."""
import json, io, sys, random
sys.stdout.reconfigure(encoding="utf-8")
SEMILLA = 20260811
bolsa = [json.loads(l) for l in io.open("docs/plan/PASO_NODO_CALIBRADO.jsonl", encoding="utf-8") if l.strip()]
bolsa = [f for f in bolsa if not f["arista"]]
bolsa.sort(key=lambda f: (f["dominio"], f["madre"], f["paso"], f["hijo"]))
print("bolsa reducida sin arista:", len(bolsa), "| semilla:", SEMILLA)
m = random.Random(SEMILLA).sample(bolsa, 24)
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
for i, f in enumerate(sorted(m, key=lambda x: (x["dominio"], x["madre"])), 1):
    print("="*76)
    print("M-%02d  [%s]  t%.0f c%.2f  fam %s -> %s" % (i, f["dominio"], f["titulo_ratio"], f["contencion"], f["familia_paso"], f["familia_hijo"]))
    print("  MADRE %s, paso %d:" % (f["madre"], f["paso"]))
    print("     %s" % f["texto_paso"][:190])
    print("  HIJO  %s: %s" % (f["hijo"], f["titulo_hijo"]))
    for j, s in enumerate(G[f["hijo"]].get("pasos_accionables") or [], 1):
        print("     %d. %s" % (j, s[:130]))
