# -*- coding: utf-8 -*-
"""scripts/importar_forja.py: los nodos APARCADOS se quedan en la forja y no entran al pack (decision del fundador del
28 sep 2026: los 5 aislados del mundo 11 salen del pack sin borrarse, con su ficha en docs/PENDIENTES.md).

Caso a mano, forja de cuatro nodos A, B, C y D:
  aparcados = [B (motivo "sin arista real"), Z (motivo "no existe")]
    dentro      = [A, C, D]        (B sale; el orden de la forja se conserva)
    aparcados   = [B]
    desconocidos = [Z]             (un aparcado que no esta en la forja se dice, no se calla)
  aparcados = [] -> dentro = [A, B, C, D], aparcados = [], desconocidos = []
  un aparcado sin motivo -> ValueError (no se aparca nada sin su por que)

    python engine/test_importar_forja_aparcados.py
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

import importar_forja as imp  # noqa: E402


def main():
    fallos = []
    forja = [{"id": x} for x in "ABCD"]
    dentro, aparcados, desconocidos = imp.aparcar(forja, [{"id": "B", "motivo": "sin arista real"},
                                                          {"id": "Z", "motivo": "no existe"}])
    if [n["id"] for n in dentro] != ["A", "C", "D"]:
        fallos.append("dentro: %r" % [n["id"] for n in dentro])
    if [n["id"] for n in aparcados] != ["B"]:
        fallos.append("aparcados: %r" % [n["id"] for n in aparcados])
    if desconocidos != ["Z"]:
        fallos.append("desconocidos: %r" % desconocidos)
    dentro, aparcados, desconocidos = imp.aparcar(forja, [])
    if [n["id"] for n in dentro] != ["A", "B", "C", "D"] or aparcados or desconocidos:
        fallos.append("sin aparcados cambia algo: %r %r %r" % (dentro, aparcados, desconocidos))
    try:
        imp.aparcar(forja, [{"id": "B", "motivo": " "}])
        fallos.append("un aparcado sin motivo no se rechazo")
    except ValueError:
        pass
    if fallos:
        print("ROJO: %d fallos" % len(fallos), *fallos, sep="\n  ")
        sys.exit(1)
    print("VERDE: los aparcados salen del pack, con motivo, y los desconocidos se dicen")


if __name__ == "__main__":
    main()
