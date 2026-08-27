"""Auditor v80: re-corrida propia de la relectura al doble del tramo 5 (TAREA 4).
Las 12 del tramo 5 = S(38ab7b37) - S(43b02413). Barrido 1 contra los veredictos
sin direccion; barrido 2 contra la bolsa filtrada de la vuelta 79 buscando la reciproca."""
import json, sys
sys.path.insert(0, "docs/loop")
from _auditor_v80_conteo import medir

A = medir("43b02413"); B = medir("38ab7b37")
doce = sorted(B["S"] - A["S"])
print(f"ARISTAS DEL TRAMO 5 (S(38ab7b37) - S(43b02413)): {len(doce)}")
for i,(m,h) in enumerate(doce,1): print(f"  {i:>2}. {m} -> {h}")

ver = [json.loads(l) for l in open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl",encoding="utf-8") if l.strip()]
idx = {}
for v in ver: idx.setdefault(frozenset((v["nodo_a"], v["nodo_b"])), []).append(v)

print("\n--- BARRIDO 1: las 12 contra el archivo, SIN DIRECCION ---")
leidas=0; claseA=0
for m,h in doce:
    hits = idx.get(frozenset((m,h)), [])
    for v in hits:
        leidas+=1
        if v["clase"]=="A": claseA+=1
        print(f"  LEIDA: {m} -> {h} | puesto {v['puesto_intra']} clase {v['clase']}")
print(f"  leidas por el cribado: {leidas} | clase A: {claseA} | A REVERTIR: {claseA}")

print("\n--- BARRIDO 2: las 12 contra la bolsa filtrada V79, buscando la RECIPROCA ---")
bolsa=[json.loads(l) for l in open("docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl",encoding="utf-8") if l.strip()]
print(f"  filas de la bolsa V79: {len(bolsa)}")
pares_bolsa = {(f["madre"], f["hijo"]) for f in bolsa}
n=0
for m,h in doce:
    if (h,m) in pares_bolsa:
        n+=1; print(f"  RECIPROCA EN LA BOLSA: {h} -> {m}")
print(f"  de las 12, con reciproca propuesta en la bolsa y no leida: {n}")
