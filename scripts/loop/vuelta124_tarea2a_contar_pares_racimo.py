# -*- coding: utf-8 -*-
"""vuelta124_tarea2a_contar_pares_racimo.py . TAREA 2.a de la vuelta 124.

Cuenta, con codigo propio y sin copiar la cifra del auditor, los pares TOTALES
del racimo (suma de C(n,2) sobre los miembros de cada familia de
docs/loop/SALIDA_V123_OPS09_LECTURA.jsonl) contra los pares YA LEIDOS (los que
ya aparecen en el campo "pares" de cada fila, que son los 39 consecutivos de
la vuelta 123), y nombra los que faltan.

USO:
  python scripts/loop/vuelta124_tarea2a_contar_pares_racimo.py
"""
import itertools
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V123_OPS09_LECTURA.jsonl")


def main():
    familias = []
    with open(RUTA, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                familias.append(json.loads(linea))

    total_racimo = 0
    total_leidos = 0
    faltantes = []
    for fam in familias:
        miembros = sorted(fam["miembros"])
        n = len(miembros)
        c_n_2 = n * (n - 1) // 2
        total_racimo += c_n_2
        leidos = set()
        for p in fam["pares"]:
            leidos.add(tuple(sorted((p["a"], p["b"]))))
        total_leidos += len(leidos)
        for a, b in itertools.combinations(miembros, 2):
            par = tuple(sorted((a, b)))
            if par not in leidos:
                faltantes.append({"familia": fam["familia"], "a": par[0], "b": par[1]})

    print("familias: %d" % len(familias))
    print("pares TOTALES del racimo (suma C(n,2)): %d" % total_racimo)
    print("pares YA LEIDOS (campo pares de cada fila): %d" % total_leidos)
    print("pares FALTANTES (%d):" % len(faltantes))
    for f in faltantes:
        print("  %s: %s <-> %s" % (f["familia"], f["a"], f["b"]))


if __name__ == "__main__":
    main()
