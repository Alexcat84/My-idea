"""Auditor v78: diff de aristas por CONJUNTOS entre dos refs."""
import sys
sys.path.insert(0, "docs/loop")
from _auditor_v78_conteo import medir

a = medir(sys.argv[1]); b = medir(sys.argv[2])
nuevas_s = b["ps"] - a["ps"]; borradas_s = a["ps"] - b["ps"]
nuevas_p = b["pp"] - a["pp"]; borradas_p = a["pp"] - b["pp"]
print(f"APERTURA {sys.argv[1]}  ->  CIERRE {sys.argv[2]}")
print(f"nuevas en nodos_siguientes : {len(nuevas_s)}")
print(f"borradas de nodos_siguientes: {len(borradas_s)}")
print(f"nuevas en nodos_previos    : {len(nuevas_p)}")
print(f"borradas de nodos_previos  : {len(borradas_p)}")
print(f"nuevas con reciproca completa en previos: {len(nuevas_s & nuevas_p)} de {len(nuevas_s)}")
print(f"borradas con reciproca completa en previos: {len(borradas_s & borradas_p)} de {len(borradas_s)}")
print(f"auto-aristas al cierre: {b['auto']}")
print("\n--- NUEVAS (madre -> hijo) ---")
for m, h in sorted(nuevas_s):
    print(f"  + {m} -> {h}   {'RECIPROCA_OK' if (m,h) in nuevas_p else 'FALTA_PREVIOS'}")
print("\n--- BORRADAS (madre -> hijo) ---")
for m, h in sorted(borradas_s):
    print(f"  - {m} -> {h}   {'RECIPROCA_OK' if (m,h) in borradas_p else 'SIGUE_EN_PREVIOS'}")
