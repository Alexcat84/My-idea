"""Auditor v79: escalera. Para cada arista nueva madre->hijo, mira si en el grafo
de la APERTURA el hijo ya apuntaba a la madre (hijo->madre en cualquiera de las dos vistas)."""
import sys
sys.path.insert(0, "docs/loop")
from _auditor_v79_conteo import medir
A = medir("aea7cc81"); B = medir("WORK")
nuevas = sorted(B["S"] - A["S"])
viejas = A["S"] | A["P"]
rotas = 0
for m, h in nuevas:
    inv = (h, m) in viejas
    if inv: rotas += 1
    print(f"{'ESCALERA ROTA' if inv else 'ok'} | {m} -> {h}")
print(f"\nESCALERA ROTA: {rotas} de {len(nuevas)}")
