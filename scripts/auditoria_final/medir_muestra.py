# -*- coding: utf-8 -*-
"""La cuenta de la muestra de la auditoria final contra los umbrales del acta (docs/ACTA_SANEAMIENTO_FINAL.md,
secciones 1 y 3). Solo cuenta lo que el arbitro CONFIRMO o RECLASIFICO (tipo_final).

  - U3 a U7 (tasa de nodos): nodos de la muestra con al menos un defecto confirmado de ese tipo / 200, con su intervalo
    de Wilson al 95 %.
  - U8 a U10 (tasa por nodo): defectos confirmados de ese tipo / 200, con su intervalo de Poisson exacto al 95 %.
  - U1 y U2: el numero de contrarios e invenciones confirmados (umbral 0).
PASA si la tasa observada no supera el umbral; el intervalo se informa y no cambia el veredicto.

    python scripts/auditoria_final/medir_muestra.py <carpeta de fallos del arbitro> [--json salida.json]
"""
import collections
import glob
import json
import math
import os
import sys

from scipy.stats import chi2

N = 200
UMBRALES = [
    ("U1", "contrario", "cuenta", 0), ("U2", "invencion", "cuenta", 0),
    ("U3", "fase", "nodos", 0.03), ("U4", "dominio", "nodos", 0.02), ("U5", "condicion", "nodos", 0.02),
    ("U6", "etiqueta", "nodos", 0.02), ("U7", "ortografia", "nodos", 0.01),
    ("U8", "matiz", "por_nodo", 0.2), ("U9", "calco", "por_nodo", 0.2), ("U10", "regionalismo", "por_nodo", 0.2),
]


def wilson(k, n, z=1.959964):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def poisson(k, n, a=0.05):
    lo = 0.0 if k == 0 else chi2.ppf(a / 2, 2 * k) / 2
    hi = chi2.ppf(1 - a / 2, 2 * k + 2) / 2
    return lo / n, hi / n


def medir(carpeta):
    defectos = collections.Counter()
    nodos = collections.defaultdict(set)
    for f in glob.glob(os.path.join(carpeta, "fallo_*.json")):
        for x in json.load(open(f, encoding="utf-8"))["fallos"]:
            if x.get("veredicto") in ("confirmado", "reclasificado") and x.get("tipo_final"):
                defectos[x["tipo_final"]] += 1
                nodos[x["tipo_final"]].add(x["node_id"])
    filas = []
    for u, tipo, modo, umbral in UMBRALES:
        if modo == "cuenta":
            k = defectos[tipo]
            filas.append({"umbral": u, "criterio": tipo, "valor": k, "tope": umbral, "pasa": k <= umbral})
        elif modo == "nodos":
            k = len(nodos[tipo])
            lo, hi = wilson(k, N)
            filas.append({"umbral": u, "criterio": tipo, "nodos": k, "tasa": k / N, "ic95": [lo, hi], "tope": umbral,
                          "pasa": k / N <= umbral})
        else:
            k = defectos[tipo]
            lo, hi = poisson(k, N)
            filas.append({"umbral": u, "criterio": tipo, "defectos": k, "tasa": k / N, "ic95": [lo, hi], "tope": umbral,
                          "pasa": k / N <= umbral})
    return filas


if __name__ == "__main__":
    filas = medir(sys.argv[1])
    for f in filas:
        print(json.dumps(f, ensure_ascii=False))
    if "--json" in sys.argv:
        json.dump(filas, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
