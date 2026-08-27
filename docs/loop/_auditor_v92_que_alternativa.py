# -*- coding: utf-8 -*-
"""Vara PROPIA del auditor v92: para cada una de las 87 que PASAN, que
alternativa(s) de MARCA_MADRE_POSITIVA la sostienen. Las que descansan en UNA
SOLA alternativa debil son las candidatas a relectura ciega."""
import io, json, os, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import vuelta92_tarea2_guarda_direccion as G

V = {int(v["puesto_intra"]): v for v in (json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","INTRA_DOMINIO_VEREDICTOS.jsonl"),encoding="utf-8") if l.strip())}
filas = [json.loads(l) for l in io.open(os.path.join(RAIZ,"docs","plan","OP_E_07_DIRECCION_V92.jsonl"),encoding="utf-8") if l.strip()]
alts = [(p, re.compile(p, re.IGNORECASE)) for p in G._ALTERNATIVAS_MARCA_MADRE]

FUERTES = {r"paso\s+\d", r"pasos\s+\d", r"etapas?\s+\d"}
solo_una = []
for f in sorted(filas, key=lambda x: x["puesto"]):
    p = f["puesto"]
    r = V[p]["razon"]
    m = [pat for pat, c in alts if c.search(r)]
    if len(m) == 1:
        solo_una.append((p, m[0]))
print("de las 87, cuantas descansan en UNA SOLA alternativa: %d" % len(solo_una))
for p, pat in solo_una:
    print("  puesto %-5s  alternativa unica: %s" % (p, pat))
print()
# cuantas tienen al menos una FUERTE (paso/etapa numerada)
con_fuerte = 0
sin_fuerte = []
for f in filas:
    p = f["puesto"]; r = V[p]["razon"]
    m = set(pat for pat, c in alts if c.search(r))
    if m & FUERTES: con_fuerte += 1
    else: sin_fuerte.append((p, sorted(m)))
print("de las 87, con marca FUERTE (paso/etapa NUMERADA): %d" % con_fuerte)
print("SIN marca fuerte: %d" % len(sin_fuerte))
for p, m in sorted(sin_fuerte):
    print("  puesto %-5s  %s" % (p, m))
