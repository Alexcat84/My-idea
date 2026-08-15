# -*- coding: utf-8 -*-
"""vuelta35_razones.py - LAS RAZONES VIEJAS DE LOS PARES DEL ACTO, enteras.

SOLO LECTURA. Una relectura que no lea la razon vieja no es una relectura: es una
lectura nueva que finge corregir. Este instrumento pone delante lo que el archivo
dice hoy de cada par, sin recortar.

Uso: python scripts/loop/vuelta35_razones.py [puesto ...]
     sin argumentos, imprime los cinco RANCIOS medidos por vuelta35_rancios.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

RANCIOS = [277, 374, 452, 1571, 1575]


def main(argv):
    puestos = [int(a) for a in argv[1:]] or RANCIOS
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = {v["puesto_intra"]: v for v in V}
    for p in puestos:
        v = por_puesto.get(p)
        if v is None:
            print("puesto %d: NO REGISTRADO" % p)
            continue
        print("=" * 78)
        print("PUESTO %d   clase %s   clave %s   dominio %s"
              % (p, v["clase"], v.get("clave"), v.get("dominio")))
        print("  %s  contra  %s" % (v["nodo_a"], v["nodo_b"]))
        print("=" * 78)
        print(v["razon"])
        print()
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main(sys.argv))
