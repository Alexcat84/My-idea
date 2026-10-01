# -*- coding: utf-8 -*-
"""scripts/auditoria_final/muestra.py: el sorteo de la muestra es reproducible por semilla. La medida 1 usa 20260929 y
la medida 2 usa 20261010 (docs/ACTA_SANEAMIENTO_FINAL.md, secciones 3 y 10): mismo reparto, sorteos independientes."""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "auditoria_final"))
import muestra as mu  # noqa: E402

m1 = mu.sortear(20260929)
m2 = mu.sortear(20261010)

# el reparto de la tabla del acta, en las dos medidas
for m in (m1, m2):
    assert {e: len(v) for e, v in m.items()} == dict(mu.REPARTO), m
    assert sum(len(v) for v in m.values()) == 200

# reproducible: la misma semilla da la misma muestra
assert mu.sortear(20261010) == m2

# independientes: la medida 2 no repite la muestra de la medida 1
assert m1 != m2
comunes = set(sum(m1.values(), [])) & set(sum(m2.values(), []))
assert len(comunes) < 50, len(comunes)

# la medida 1 sigue siendo la del acta (la semilla por defecto no cambia)
assert mu.sortear() == m1

print("OK test_muestra_auditoria")
