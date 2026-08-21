# -*- coding: utf-8 -*-
"""vuelta65_puentes_del_tramo.py . LA MITAD DIAGNOSTICA DE P.5 SOBRE EL TRAMO
UNICO DE OP-U-02: LOS NODOS PUENTE, ACTO POR ACTO.

POR QUE NACE, y no es un capricho. Los actos de OP-U-01 eran todos de DOS
miembros: la componente ERA el par, y la pregunta de P.5 (una familia o dos) se
contestaba leyendo ese par. Los actos de OP-U-02 van de 3 a 15 miembros, y ahi
manda P.10 del banco del plan con todas sus letras:

  UN NODO PUENTE es el que tiene A con dos nodos que entre si son D. La
  componente que forma puede ser UNA familia o DOS pegadas por el, y el cierre
  transitivo no lo distingue: las junta igual.
  UN NODO PUENTE SOLO SE VE MIRANDO LA COMPONENTE ENTERA. Leyendo un par, jamas.
  Si aparece, la componente NO se funde hasta que ese triangulo se cierre.
  LO QUE NUNCA ES SALIDA: fundir la componente entera porque el cierre
  transitivo la junta. El cierre transitivo no lee: cuenta.

ESTE INSTRUMENTO NO ADJUDICA NADA: cuenta y publica. Por cada acto imprime sus
pares internos con veredicto, los que NO tienen veredicto escrito, y LOS
TRIANGULOS PUENTE (un nodo con A hacia dos que entre si son D). Las tres salidas
de P.10 las elige el ejecutor con la medicion delante, no este fichero.

TODO ID PASA POR EL RESOLUTOR ANTES DE CONTAR (P.1): los veredictos se indexan
por el par de ids RESUELTOS a su vivo, que es como el resto de la campana cuenta.

DE SOLO LECTURA. No escribe nada fuera de su salida.

Uso:
  python scripts/loop/vuelta65_puentes_del_tramo.py --tramo docs/loop/TRAMO_UNICO_OPU02_V64.jsonl
      [--actos 1,3,5] [--detalle]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
NL = chr(10)


def resolutor():
    """P.1: id a id VIVO siguiendo alias. LA MAQUINA ES LA MISMA QUE LA DE
    scripts/plan/aristas_duplicadas_tras_resolver.py, copiada de sus lineas 38 a
    46 y no re-inventada, para que dos instrumentos de la campana no resuelvan
    distinto en silencio."""
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    vivos = {k for k, v in G.items() if not v.get("deprecado")}
    return res, vivos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True)
    ap.add_argument("--actos", default=None)
    ap.add_argument("--detalle", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    quiero = set(int(x) for x in a.actos.split(",")) if a.actos else None
    filas = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, a.tramo.replace("/", os.sep)), encoding="utf-8")
             if l.strip()]
    claves = sorted({k for k in filas[0] if k.startswith("orden_")})
    if len(claves) != 1:
        print("ROJO: %d claves de ordinal (%s). PARADA." % (len(claves), claves))
        return 1
    ORD = claves[0]

    res, _ = resolutor()
    ver = {}
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        ver[frozenset((res(v["nodo_a"]), res(v["nodo_b"])))] = v

    print("=" * 78)
    print("LOS NODOS PUENTE DEL TRAMO, ACTO POR ACTO (P.10, la mitad diagnostica de P.5)")
    print("  tramo      : %s" % a.tramo)
    print("  clave      : %s" % ORD)
    print("  veredictos : %d pares indexados por par RESUELTO (P.1)" % len(ver))
    print("=" * 78)

    resumen = []
    for f in filas:
        n = f[ORD]
        if quiero and n not in quiero:
            continue
        ms = sorted(set(res(x) for x in f["miembros"]))
        pares_A, pares_D, sin = [], [], []
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                v = ver.get(frozenset((ms[i], ms[j])))
                if not v:
                    sin.append((ms[i], ms[j]))
                elif (v.get("clase") or "").upper() == "A":
                    pares_A.append((ms[i], ms[j], v))
                else:
                    pares_D.append((ms[i], ms[j], v))
        setA = {frozenset((x, y)) for x, y, _ in pares_A}
        setD = {frozenset((x, y)) for x, y, _ in pares_D}
        # UN PUENTE: un nodo con A hacia dos nodos que entre si son D.
        puentes = {}
        for p in ms:
            vecinos = sorted(q for q in ms if q != p and frozenset((p, q)) in setA)
            for i in range(len(vecinos)):
                for j in range(i + 1, len(vecinos)):
                    if frozenset((vecinos[i], vecinos[j])) in setD:
                        puentes.setdefault(p, []).append((vecinos[i], vecinos[j]))
        combinaciones = len(ms) * (len(ms) - 1) // 2
        resumen.append((n, len(ms), combinaciones, len(pares_A), len(pares_D),
                        len(sin), len(puentes), sum(len(v) for v in puentes.values())))
        print()
        print("-" * 78)
        print("ACTO %d | miembros %d | combinaciones %d | A %d | D %d | SIN VEREDICTO %d"
              % (n, len(ms), combinaciones, len(pares_A), len(pares_D), len(sin)))
        print("  NODOS PUENTE: %d | TRIANGULOS PUENTE (A mas A mas D): %d"
              % (len(puentes), sum(len(v) for v in puentes.values())))
        for p in sorted(puentes):
            print("     %s hace de puente en %d triangulo(s):" % (p, len(puentes[p])))
            for x, y in puentes[p]:
                v = ver[frozenset((x, y))]
                print("        A con %s y A con %s, y esos dos son D entre si (puesto %s)"
                      % (x, y, v.get("puesto_intra")))
        if a.detalle:
            print("  pares D internos, que son los que la fusion entera desmentiria:")
            for x, y, v in sorted(pares_D, key=lambda t: t[2].get("puesto_intra") or 0):
                print("     puesto %-6s %s  contra  %s" % (v.get("puesto_intra"), x, y))
            if sin:
                print("  pares SIN VEREDICTO ESCRITO: %d (la primera salida de P.10 es leerlos)"
                      % len(sin))

    print()
    print("=" * 78)
    print("RESUMEN DEL TRAMO")
    print("%-6s %-6s %-8s %-5s %-5s %-8s %-8s %s"
          % ("acto", "miem", "combin", "A", "D", "sin_ver", "puentes", "triangulos"))
    for r_ in resumen:
        print("%-6d %-6d %-8d %-5d %-5d %-8d %-8d %d" % r_)
    con = len([x for x in resumen if x[6]])
    print()
    print("  actos mirados                         : %d" % len(resumen))
    print("  actos CON al menos un nodo puente     : %d" % con)
    print("  actos SIN ningun nodo puente          : %d" % (len(resumen) - con))
    print("  actos con algun par SIN veredicto     : %d" % len([x for x in resumen if x[5]]))
    print()
    print("LO QUE ESTO NO HACE: no elige salida de P.10 ni funde ni declara nada.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
