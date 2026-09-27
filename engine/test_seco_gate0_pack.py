# -*- coding: utf-8 -*-
"""scripts/seco_gate0_pack.py: el seco de una integracion corre el Gate 0 de grafo completo (componentes, cobertura y
alcanzabilidad dirigida) sobre el catalogo con el pack y sus puentes tejidos EN MEMORIA, y ademas el 100 por cien del
mundo (leccion del mundo 11, 28 sep 2026: el seco del importador no miraba el grafo y la primera corrida real se paro en
Gate 0 con 259 componentes).

Caso a mano. Catalogo: A -> B (core), semilla del motor A. Pack del mundo m: X -> Y, y Z sin aristas.
  1. puente B -> X, sin semillas del pack:
       nodos 5; componentes {A,B,X,Y} y {Z} = 2; cobertura 4/5 = 80.0
       alcance dirigido desde {A}: A, B, X, Y = 4/5 = 80.0; mundo 2/3 = 66.67; aislados del mundo [Z]
  2. sin puente, semillas del pack [X, Z]:
       componentes {A,B}, {X,Y}, {Z} = 3; cobertura 2/5 = 40.0
       alcance desde {A, X, Z}: 5/5 = 100.0; mundo 3/3 = 100.0; aislados del mundo [Z]
  3. el puente B -> X queda tejido reciproco: X.nodos_previos contiene B y B.nodos_siguientes contiene X, sin tocar
     los diccionarios de entrada (todo en memoria).

    python engine/test_seco_gate0_pack.py
"""
import copy
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

import seco_gate0_pack as seco  # noqa: E402


def nodo(i, dominio, sig=(), prev=()):
    return {"node_id": i, "dominio": dominio, "nodos_siguientes": list(sig), "nodos_previos": list(prev)}


def main():
    fallos = []
    catalogo = {"A": nodo("A", "core", sig=["B"]), "B": nodo("B", "core", prev=["A"])}
    pack = {"X": nodo("X", "m", sig=["Y"]), "Y": nodo("Y", "m", prev=["X"]), "Z": nodo("Z", "m")}
    antes = copy.deepcopy((catalogo, pack))

    tejido = seco.tejer(catalogo, pack, [{"core": "B", "dominio": "X"}])
    r = seco.medir(tejido, ["A"], "m")
    esperado = {"nodos": 5, "componentes": 2, "cobertura_pct": 80.0, "alcance_pct": 80.0,
                "mundo_alcance_pct": 66.67, "mundo_aislados": ["Z"]}
    for k, v in esperado.items():
        if r[k] != v:
            fallos.append("caso 1 %s: %r, esperado %r" % (k, r[k], v))
    if "B" not in tejido["X"]["nodos_previos"] or "X" not in tejido["B"]["nodos_siguientes"]:
        fallos.append("caso 3: el puente no quedo tejido reciproco")
    if (catalogo, pack) != antes:
        fallos.append("caso 3: tejer toco los diccionarios de entrada")

    r = seco.medir(seco.tejer(catalogo, pack, []), ["A", "X", "Z"], "m")
    esperado = {"nodos": 5, "componentes": 3, "cobertura_pct": 40.0, "alcance_pct": 100.0,
                "mundo_alcance_pct": 100.0, "mundo_aislados": ["Z"]}
    for k, v in esperado.items():
        if r[k] != v:
            fallos.append("caso 2 %s: %r, esperado %r" % (k, r[k], v))

    if fallos:
        print("ROJO: %d fallos" % len(fallos), *fallos, sep="\n  ")
        sys.exit(1)
    print("VERDE: el seco teje el pack en memoria y mide componentes, cobertura y alcance como Gate 0")


if __name__ == "__main__":
    main()
