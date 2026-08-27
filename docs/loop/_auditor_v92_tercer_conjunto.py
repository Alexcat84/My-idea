# -*- coding: utf-8 -*-
"""ADJUDICACION DEL DISCUTIBLE 1 (auditor v92): el guarda corrido sobre un
TERCER CONJUNTO que no es ninguna de sus dos varas.

El tercer conjunto: los pares de docs/plan/COSECHA_RAZONES_D.jsonl cuyas
senales incluyen 'formula de la vara' o 'procedimiento de esa linea' (o sea,
pares donde la DIRECCION SI esta establecida en el texto cosechado), MENOS los
que ya viven en las dos bolsas con las que el guarda se calibro
(OP_E_07_REBASE_V91.jsonl y OP_E_06_DIRECCION_V90.jsonl).

Lo que mide: cuantos pares SANOS (con direccion establecida) el guarda tumbaria
si se corriera sobre razones que no vio. Eso es exactamente lo que el discutible
1 del reporte de la vuelta 92 dice que NO se probo."""
import io, json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
from vuelta92_tarea2_guarda_direccion import guarda_direccion

def jl(p):
    return [json.loads(l) for l in io.open(os.path.join(RAIZ, p), encoding="utf-8") if l.strip()]

V = {int(v["puesto_intra"]): v for v in jl("docs/INTRA_DOMINIO_VEREDICTOS.jsonl")}
vistos = set(f["puesto"] for f in jl("docs/plan/OP_E_07_REBASE_V91.jsonl"))
vistos |= set(f["puesto"] for f in jl("docs/plan/OP_E_06_DIRECCION_V90.jsonl"))

cosecha = jl("docs/plan/COSECHA_RAZONES_D.jsonl")
tercer = [c for c in cosecha
          if set(c.get("senales") or []) & {"formula de la vara", "procedimiento de esa linea"}
          and c["puesto"] not in vistos and c["puesto"] in V]
print("cosecha total: %d" % len(cosecha))
print("puestos ya vistos por el guarda (sus dos varas): %d" % len(vistos))
print("TERCER CONJUNTO (direccion establecida en el texto, NO visto por el guarda): %d" % len(tercer))
salen = []
for c in tercer:
    if guarda_direccion(V[c["puesto"]]["razon"]) == "SALE":
        salen.append(c["puesto"])
print()
print("PASAN: %d | SALEN (falsos positivos del guarda sobre pares sanos): %d" % (len(tercer)-len(salen), len(salen)))
print("tasa de falso SALE: %.1f por ciento" % (100.0*len(salen)/max(1,len(tercer))))
print("los que SALEN: %s" % sorted(salen))
