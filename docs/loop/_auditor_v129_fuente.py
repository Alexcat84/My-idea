# -*- coding: utf-8 -*-
"""Auditor v129: censo del campo `fuente` en primera posicion sobre los nodos
VIVOS de HOY. Codigo propio del auditor, para fijar el corte nuevo."""
import io, json, os, re
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = json.load(io.open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"), encoding="utf-8"))["nodos"]

vivos = {k:v for k,v in G.items() if not v.get("deprecado")}
print("NODOS VIVOS:", len(vivos))

con_fuente = [v for v in vivos.values() if (v.get("fuente") or "").strip()]
print("VIVOS CON CAMPO fuente NO VACIO:", len(con_fuente))

# separador: se mide, no se supone
seps = Counter()
for v in con_fuente:
    f = v["fuente"]
    for s in [";", " | ", " + ", " y ", ","]:
        if s in f: seps[s]+=1
print("PRESENCIA DE SEPARADORES CANDIDATOS (nodos que lo contienen):", dict(seps))

def primera(f):
    return re.split(r"\s*;\s*", f.strip())[0].strip()

cnt = Counter(primera(v["fuente"]) for v in con_fuente)
print("GRAFIAS DISTINTAS EN PRIMERA POSICION:", len(cnt))

# truncadas: prefijo estricto de otra
claves = sorted(cnt)
trunc = [(a,b) for a in claves for b in claves if a!=b and b.startswith(a)]
print("PARES PREFIJO-ESTRICTO (grafia truncada -> mas larga):", len(trunc))
for a,b in trunc: print("   '%s' (%d)  ->  '%s' (%d)" % (a, cnt[a], b, cnt[b]))

# los dos casos probados
for libro in ("Hugos", "Horowitz"):
    ms = sorted(g for g in claves if libro.lower() in g.lower())
    print("\nCASO %s: %d grafia(s) distintas, %d declaraciones en total" % (libro, len(ms), sum(cnt[g] for g in ms)))
    for g in ms: print("   %3d  '%s'" % (cnt[g], g))
