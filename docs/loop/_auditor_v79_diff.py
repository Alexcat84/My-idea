"""Auditor v79: diff de aristas POR CONJUNTOS entre dos refs, no por conteo."""
import sys
sys.path.insert(0, "docs/loop")
from _auditor_v79_conteo import medir

a, b = sys.argv[1], sys.argv[2]
A, B = medir(a), medir(b)
nuevas_S = B["S"] - A["S"]; borradas_S = A["S"] - B["S"]
nuevas_P = B["P"] - A["P"]; borradas_P = A["P"] - B["P"]
print(f"APERTURA {a} -> CIERRE {b}")
print(f"nuevas en nodos_siguientes : {len(nuevas_S)}")
print(f"nuevas en nodos_previos    : {len(nuevas_P)}")
print(f"nuevas con RECIPROCA completa (en las dos vistas): {len(nuevas_S & nuevas_P)} de {len(nuevas_S)}")
print(f"borradas de nodos_siguientes: {len(borradas_S)}")
print(f"borradas de nodos_previos   : {len(borradas_P)}")
print(f"borradas con reciproca tambien borrada: {len(borradas_S & borradas_P)} de {len(borradas_S)}")
print(f"auto-aristas al cierre: {B['auto']}")
print("\n--- LAS NUEVAS (nodos_siguientes), orden alfabetico ---")
for i, (m, h) in enumerate(sorted(nuevas_S), 1):
    tiene_p = "SI" if (m, h) in nuevas_P else "NO"
    print(f"{i:>3}. {m} -> {h}   [reciproca nueva en previos: {tiene_p}]")
print("\n--- LAS BORRADAS (nodos_siguientes) ---")
for i, (m, h) in enumerate(sorted(borradas_S), 1):
    tiene_p = "SI" if (m, h) in borradas_P else "NO"
    print(f"{i:>3}. {m} -> {h}   [borrada tambien de previos: {tiene_p}]")
