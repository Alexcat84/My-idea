# -*- coding: utf-8 -*-
r"""vuelta115_tarea3_2_ope01_vs_grafo.py . TAREA 3.2 de la vuelta 115: cuenta
las filas de docs/plan/OP_E_01_DECIDIDAS.jsonl por su campo `decision` y
comprueba, contra dataset/metadata/master_graph.json DE HOY, cuantas de las
ESCRITA estan presentes como arista y cuantas ausentes.

CRITERIO DE PRESENCIA (el que pide el encargo, literal, SIN resolver por
alias): una arista (madre, hijo) cuenta como PRESENTE si el hijo esta en
`nodos_siguientes` de la madre O la madre esta en `nodos_previos` del hijo.
Las dos vistas se comprueban por separado y tambien se informan solas, para
que un desacuerdo entre las dos vistas (arista en una sola direccion) no
quede escondido dentro del OR.

USO:
  python scripts/loop/vuelta115_tarea3_2_ope01_vs_grafo.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_DECIDIDAS = os.path.join(RAIZ, "docs", "plan", "OP_E_01_DECIDIDAS.jsonl")
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


def cargar_decididas():
    filas = []
    with open(RUTA_DECIDIDAS, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def cargar_grafo():
    with open(RUTA_GRAFO, encoding="utf-8") as f:
        return json.load(f)["nodos"]


def main():
    filas = cargar_decididas()
    nodos = cargar_grafo()

    from collections import Counter
    c = Counter(f["decision"] for f in filas)
    print("OP_E_01_DECIDIDAS.jsonl: %d filas totales." % len(filas))
    for clave, n in sorted(c.items()):
        print("   %s: %d" % (clave, n))
    print()

    escritas = [f for f in filas if f["decision"] == "ESCRITA"]
    presentes, ausentes = [], []
    solo_sig, solo_prev, en_las_dos = [], [], []
    for f in escritas:
        madre, hijo = f["madre"], f["hijo"]
        en_sig = hijo in (nodos.get(madre, {}).get("nodos_siguientes") or [])
        en_prev = madre in (nodos.get(hijo, {}).get("nodos_previos") or [])
        if en_sig or en_prev:
            presentes.append((madre, hijo))
        else:
            ausentes.append((madre, hijo))
        if en_sig and en_prev:
            en_las_dos.append((madre, hijo))
        elif en_sig:
            solo_sig.append((madre, hijo))
        elif en_prev:
            solo_prev.append((madre, hijo))

    print("CRITERIO: hijo en nodos_siguientes(madre) O madre en nodos_previos(hijo).")
    print("ESCRITA: %d filas." % len(escritas))
    print("PRESENTES (por el OR): %d" % len(presentes))
    print("AUSENTES (ninguna de las dos vistas): %d" % len(ausentes))
    for m, h in ausentes:
        print("   AUSENTE: %s -> %s" % (m, h))
    print()
    print("Desglose de las presentes: en las DOS vistas %d, SOLO nodos_siguientes %d, SOLO nodos_previos %d."
          % (len(en_las_dos), len(solo_sig), len(solo_prev)))
    if solo_sig or solo_prev:
        print("(las que no calzan en las dos vistas, nombradas:)")
        for m, h in solo_sig:
            print("   SOLO nodos_siguientes: %s -> %s" % (m, h))
        for m, h in solo_prev:
            print("   SOLO nodos_previos: %s -> %s" % (m, h))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
