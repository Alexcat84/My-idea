# -*- coding: utf-8 -*-
"""vuelta51_censo_colisiones.py . CENSO DE COLISIONES DE CLASE VIGENTES SOBRE EL
ARCHIVO ENTERO, con el resolutor de la casa.

POR QUE EXISTE COMO INSTRUMENTO Y NO COMO SONDA SUELTA: la vuelta 50 midio su
censo con codigo escrito dentro de la vuelta y solo dejo la SALIDA
(docs/loop/SALIDA_V50_CENSO_COLISIONES_ACTO1.txt). Una cifra que se publica en
cada vuelta y cuyo instrumento no queda en el arbol no se puede re-correr contra
otro corte, y eso es lo que la regla 2 del EJECUTOR pide poder hacer.

QUE MIDE: agrupa los 3.388 veredictos por su PAR RESUELTO (`P.1`, mapa de alias
construido SOLO con nodos vivos) y cuenta los grupos con DOS O MAS CLASES
publicadas a la vez. Un par resuelto con una `A` y una `D` publicadas es una
contradiccion contra una cifra publicada con su corte.

SEPARA LOS AUTO-PARES y no los cuenta como colision: cuando los dos lados de un
veredicto resuelven al MISMO nodo vivo (lo que pasa con el par interno de un
acto que se acaba de fundir), el par colapsa a auto-arista. Eso lo cuenta el
retrato como colapso y no es una colision de clase.

DE SOLO LECTURA. No toca ni un nodo ni un veredicto: imprime.

Uso:
  python scripts/loop/vuelta51_censo_colisiones.py [--esperadas 3] [--titulo "..."]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--esperadas", type=int, default=None)
    ap.add_argument("--titulo", default="CENSO DE COLISIONES DE CLASE VIGENTES")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    alias = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        if d.get("deprecado") or d.get("deprecated"):
            continue
        for x in (d.get("ids_alias") or []):
            alias[x] = d["node_id"]

    def res(x):
        return alias.get(x, x)

    grupos, total = {}, 0
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        total += 1
        na, nb = res(v["nodo_a"]), res(v["nodo_b"])
        grupos.setdefault(frozenset((na, nb)), []).append(
            (v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))

    auto = [k for k in grupos if len(k) == 1]
    colisiones = []
    for k, vs in grupos.items():
        if len(k) == 1:
            continue
        if len(set(c for _, c, _, _ in vs)) > 1:
            colisiones.append((k, sorted(vs)))

    print("=" * 78)
    print(a.titulo)
    print("=" * 78)
    print("  veredictos leidos                       : %d" % total)
    print("  pares resueltos distintos               : %d" % len(grupos))
    print("  AUTO-PARES (los dos lados al mismo vivo): %d" % len(auto))
    print("  COLISIONES DE CLASE VIGENTES            : %d" % len(colisiones))
    print()
    for k, vs in sorted(colisiones, key=lambda x: sorted(x[0])):
        izq, der = sorted(k)
        print("  par resuelto: %s contra %s" % (izq, der))
        for pu, cl, na, nb in vs:
            print("     puesto %-6s %s | crudo: %s + %s" % (pu, cl, na, nb))
    if not colisiones:
        print("  ninguna.")
    print()
    if a.esperadas is not None:
        print("  CUENTA ESPERADA: %d | MEDIDA: %d | CALZA: %s"
              % (a.esperadas, len(colisiones),
                 "SI" if a.esperadas == len(colisiones) else "NO"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
