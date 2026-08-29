# -*- coding: utf-8 -*-
"""vuelta130_hugos_horowitz.py . TAREA 3.b(v) de la vuelta 130: remide los
dos casos probados de OP-S-11 (Hugos y Horowitz) en DOS UNIDADES DISTINTAS,
cada una con su nombre, para no repetir la trampa que la nota de la
operacion ya trae (comparar "23 contra 21" y "16 contra 14" del RECORTE
POSICIONAL, 67 nodos, contra una medicion sobre el catalogo entero, 3.184
nodos vivos: son unidades y universos distintos, no comparables).

UNIDAD 1, "por NODO, fuente entero" (la cadena `fuente` completa, SIN
partir por `|`): cuenta cuantos NODOS vivos traen la palabra en su `fuente`,
y cuantas GRAFIAS DISTINTAS DE `fuente` COMPLETO la traen.

UNIDAD 2, "por DECLARACION resuelta" (partiendo `fuente` por `|`, la
propuesta de separador de esta vuelta, TAREA 3.b(i)): cuenta cuantas
DECLARACIONES (tras partir) traen la palabra, y cuantas grafias distintas
DE LA DECLARACION la traen. Difieren de la unidad 1 solo cuando un nodo
combina varios libros con `|` y mas de uno de ellos nombra al autor (hay
UN nodo asi para Horowitz: combina `The Founder's Dilemmas` con las dos
formas de `The Hard Thing About Hard Things`).

Salida: docs/loop/SALIDA_V130_3B_HUGOS_HOROWITZ.txt

Uso:
  python scripts/loop/vuelta130_hugos_horowitz.py
"""
import glob
import json
import os
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def medir(palabra):
    por_nodo = Counter()
    por_declaracion = Counter()
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        fu = d.get("fuente")
        if not fu:
            continue
        if palabra in fu:
            por_nodo[fu] += 1
        for decl in fu.split("|"):
            decl = decl.strip()
            if palabra in decl:
                por_declaracion[decl] += 1
    return por_nodo, por_declaracion


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    salida = os.path.join(RAIZ, "docs", "loop", "SALIDA_V130_3B_HUGOS_HOROWITZ.txt")
    with open(salida, "w", encoding="utf-8") as fh:
        for palabra in ("Hugos", "Horowitz"):
            por_nodo, por_decl = medir(palabra)
            fh.write("=== %s ===\n" % palabra)
            fh.write("UNIDAD 1, por NODO (fuente entero, corte catalogo 2026-08-29, %d nodos vivos con fuente):\n" % 3184)
            for g, n in por_nodo.most_common():
                fh.write("  %d\t%s\n" % (n, g))
            fh.write("  TOTAL nodos: %d, grafias (fuente-entero) distintas: %d\n" % (sum(por_nodo.values()), len(por_nodo)))
            fh.write("UNIDAD 2, por DECLARACION resuelta (separador '|', propuesta 3.b(i)):\n")
            for g, n in por_decl.most_common():
                fh.write("  %d\t%s\n" % (n, g))
            fh.write("  TOTAL declaraciones: %d, grafias (declaracion) distintas: %d\n" % (sum(por_decl.values()), len(por_decl)))
            fh.write("\n")
    print("escrito: %s" % salida)


if __name__ == "__main__":
    raise SystemExit(main())
