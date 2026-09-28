# -*- coding: utf-8 -*-
"""La muestra estratificada de la auditoria final (docs/ACTA_SANEAMIENTO_FINAL.md, seccion 3), reproducible.

Semilla 20260929, escrita en el acta antes de sortear. 200 nodos vivos: 10 por espacio como minimo y el resto
proporcional por restos mayores. Dentro de cada espacio, ids en orden alfabetico y random.Random(semilla + indice del
espacio en la tabla del acta).

    python scripts/auditoria_final/muestra.py      # escribe docs/auditoria_final/muestra.json
"""
import glob
import json
import os
import random

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEMILLA = 20260929
# el orden y el reparto de la tabla del acta (seccion 3)
REPARTO = [
    ("core", 45), ("quality", 27), ("primer_equipo", 22), ("environmental", 17), ("health_safety", 16),
    ("franquicias", 14), ("exportacion", 13), ("entrega", 12), ("risk_management", 12), ("compras", 11),
    ("seguridad_digital", 11),
]


def vivos_por_espacio():
    por = {}
    for f in glob.glob(os.path.join(RAIZ, "dataset", "nodos", "*.json")):
        n = json.load(open(f, encoding="utf-8"))
        if not n.get("deprecado"):
            por.setdefault(n["dominio"], []).append(n["node_id"])
    return {d: sorted(v) for d, v in por.items()}


def sortear():
    por = vivos_por_espacio()
    assert sum(k for _, k in REPARTO) == 200
    muestra = {}
    for i, (espacio, k) in enumerate(REPARTO):
        muestra[espacio] = sorted(random.Random(SEMILLA + i).sample(por[espacio], k))
    return muestra


if __name__ == "__main__":
    m = sortear()
    os.makedirs(os.path.join(RAIZ, "docs", "auditoria_final"), exist_ok=True)
    json.dump({"semilla": SEMILLA, "muestra": m}, open(os.path.join(RAIZ, "docs", "auditoria_final", "muestra.json"), "w",
              encoding="utf-8"), ensure_ascii=False, indent=1)
    print({e: len(v) for e, v in m.items()}, sum(len(v) for v in m.values()))
