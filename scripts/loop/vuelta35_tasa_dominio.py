# -*- coding: utf-8 -*-
"""vuelta35_tasa_dominio.py - LA TASA POR DOMINIO, recomputada del archivo.

SOLO LECTURA. SUCESOR DECLARADO del que produjo docs/loop/SALIDA_V34_TASA_DOMINIO.txt
(EJECUTOR.md regla 2), con la misma maquinaria y sin cambio de criterio: se cuenta
sobre docs/INTRA_DOMINIO_VEREDICTOS.jsonl, un registro por par, y la tasa es A
sobre n del dominio.

POR QUE SE VUELVE A CORRER AUNQUE ESTA VUELTA NO MUEVA EL ARCHIVO: porque la
regla 2 dice que una cifra publicada se lee de la salida del instrumento corrido
EN ESTA VUELTA, y un reporte anterior nunca es fuente. Si sale identica, esa
identidad tambien es una medicion.

Uso: python scripts/loop/vuelta35_tasa_dominio.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def main():
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    conteo = {}
    for v in V:
        conteo[v["clase"]] = conteo.get(v["clase"], 0) + 1
    print("n %d" % len(V))
    print("marcador %s" % conteo)
    print()
    por_dom = {}
    for v in V:
        d = v.get("dominio") or "(sin dominio)"
        c = por_dom.setdefault(d, {"n": 0, "A": 0, "B": 0, "C": 0, "D": 0})
        c["n"] += 1
        if v["clase"] in c:
            c[v["clase"]] += 1
    print("%-20s %6s %6s %8s %6s %6s %6s" % ("dominio", "n", "A", "tasa", "B", "C", "D"))
    for d in sorted(por_dom, key=lambda k: -por_dom[k]["n"]):
        c = por_dom[d]
        tasa = (100.0 * c["A"] / c["n"]) if c["n"] else 0.0
        print("%-20s %6d %6d %7.1f%% %6d %6d %6d"
              % (d, c["n"], c["A"], tasa, c["B"], c["C"], c["D"]))
    print("\ndominios: %d" % len(por_dom))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
