# -*- coding: utf-8 -*-
"""vuelta38_marcador.py - EL MARCADOR DEL ARCHIVO, RECOMPUTADO AL CIERRE.

ESTRICTAMENTE DE SOLO LECTURA.

POR QUE SE CORRE AL CIERRE Y NO AL PRINCIPIO: EJECUTOR.md regla 1, segundo
parrafo, EL ESTADO AL CIERRE SE MIDE AL CIERRE. La caida de la vuelta 28 fue
publicar en la tabla de cierre la medicion de apertura despues de que la propia
vuelta la moviera. Esta vuelta no deberia mover el marcador (sus tres lecturas
son dirigidas y estan fuera de cola), y precisamente por eso la cifra se vuelve a
medir: para poder decir que no se movio con la medicion del dia al lado, no con
el recuerdo.

Uso: python scripts/loop/vuelta38_marcador.py
"""
import collections
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PARES = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_PARES.jsonl")


def main():
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    P = sum(1 for l in io.open(PARES, encoding="utf-8") if l.strip())
    c = collections.Counter(v["clase"] for v in V)
    print("=" * 78)
    print("MARCADOR DEL ARCHIVO, recomputado al cierre de la vuelta 38")
    print("=" * 78)
    print("  docs/INTRA_DOMINIO_VEREDICTOS.jsonl : %d filas" % len(V))
    print("  docs/INTRA_DOMINIO_PARES.jsonl      : %d filas" % P)
    print("")
    print("  n = %d" % len(V))
    for k in sorted(c):
        print("  %s = %d" % (k, c[k]))
    print("")
    print("  suma de clases: %d   (tiene que ser igual a n)" % sum(c.values()))
    print("  cuadra: %s" % ("SI" if sum(c.values()) == len(V) else "NO"))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
