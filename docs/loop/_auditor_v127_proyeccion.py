# -*- coding: utf-8 -*-
"""Auditor 127: separa las 32 huerfanas de HOY en HEREDADAS (el mismo hueco
ya existia al nacer el bucle, aunque sus extremos se hayan renombrado por
fusiones posteriores) y FABRICADAS POR LA CAMPANA. Proyecta el conjunto
huerfano del baseline por el resolutor de HOY, igual que verificar_aristas_vivas.py."""
import json, os, subprocess
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
exec(open(os.path.join(RAIZ,"docs","loop","_auditor_v127_historia.py")).read().split("refs=sys.argv")[0])
nodos_hoy = json.load(open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"),encoding="utf-8"))["nodos"]
alias={}
for nid,n in nodos_hoy.items():
    if n.get("deprecado"): continue
    for x in (n.get("ids_alias") or []): alias[x]=nid
def resolver(x):
    v=set()
    while x in alias and x not in v: v.add(x); x=alias[x]
    return x
base = en("50f03099"); hoy = en("WORK")
proyectadas = {(resolver(o), resolver(d)) for o,d in base}
heredadas = hoy & proyectadas
fabricadas = hoy - proyectadas
print("baseline (50f03099, encendido del bucle): %d" % len(base))
print("hoy: %d" % len(hoy))
print("HEREDADAS (el hueco ya existia antes del bucle, proyectado por el alias de hoy): %d" % len(heredadas))
print("FABRICADAS POR LA CAMPANA (hueco que no existia antes del bucle): %d" % len(fabricadas))
for p in sorted(fabricadas): print("   %s -> %s" % p)
print("del baseline, ya no huerfanas hoy (reparadas de rebote): %d" % len(proyectadas - hoy))
for p in sorted(proyectadas - hoy): print("   %s -> %s" % p)
