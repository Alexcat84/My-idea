#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""simular_fusion.py . SIMULA UNA FUSION SOBRE UNA COPIA EN MEMORIA.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo. Es el instrumento del estandar
P.7 del banco del plan: TODA OPERACION DE MESA SE SIMULA ANTES DE ESCRIBIRSE LISTA.

POR QUE EXISTE. La simulacion de la mesa de la junta asesora le hizo DOS
correcciones a la premisa de la adjudicacion, y las dos cambiaban la ejecucion:
la arista que se creia bidireccional era una sola y apuntaba al reves, y la entrada
que se creia que habria que redirigir ya estaba duplicada. Ninguna de las dos se ve
leyendo: se ven simulando.

QUE MIDE, por cada fusion (superviviente, muere):
  1. DESEMPATE POR CABLEADO: grado de cada uno, para decidir quien sobrevive.
  2. ALIAS RESULTANTES del superviviente.
  3. ENTRADAS QUE SE REDIRIGEN: quien nombra al que muere y a donde va a parar.
  4. DUPLICADAS GENERADAS: entradas que tras la fusion resuelven al mismo destino
     dentro del mismo campo. Es la clase de OP-S-12, y toda fusion fabrica alguna.
  5. ARISTAS QUE SOBREVIVEN ENTRE LOS NODOS DEL ACTO, con su direccion resuelta.
  6. AUTO-ARISTAS que la fusion crearia: la clase de OP-S-07.

USO
  python scripts/plan/simular_fusion.py --fusion superviviente:muere [--fusion ...]
                                        [--acto id1,id2,...]
"""
import argparse, collections, json, io, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CAMPOS = ("nodos_previos", "nodos_siguientes")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grafo", default=str(RAIZ / "dataset" / "metadata" / "master_graph.json"))
    ap.add_argument("--fusion", action="append", required=True,
                    help="superviviente:muere . repetible")
    ap.add_argument("--acto", default=None,
                    help="ids del acto separados por coma, para ver las aristas internas que sobreviven")
    args = ap.parse_args()

    G = json.load(io.open(args.grafo, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}
    pares = [tuple(f.split(":", 1)) for f in args.fusion]
    for viv, mue in pares:
        for x in (viv, mue):
            if x not in G:
                sys.exit("no existe en el grafo: %s" % x)
        ALIAS[mue] = viv

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    def grado(k):
        sal = len(set(res(y) for c in CAMPOS for y in (G[k].get(c) or [])))
        ent = sum(1 for kk, vv in G.items() if not vv.get("deprecado")
                  for c in CAMPOS if k in (vv.get(c) or []))
        return sal, ent

    print("=" * 78)
    print("SIMULACION DE FUSION, sobre copia en memoria. NADA SE ESCRIBE.")
    print("=" * 78)
    for viv, mue in pares:
        sv, ev = grado(viv)
        sm, em = grado(mue)
        print()
        print("### %s  <==  %s" % (viv, mue))
        print("  1. DESEMPATE POR CABLEADO")
        print("     %-44s pasos %2d | nombra %2d | LO NOMBRAN %2d"
              % (viv, len(G[viv].get("pasos_accionables") or []), sv, ev))
        print("     %-44s pasos %2d | nombra %2d | LO NOMBRAN %2d"
              % (mue, len(G[mue].get("pasos_accionables") or []), sm, em))
        if ev == em:
            print("     >>> EMPATE DE CABLEADO: %d contra %d. SE TRAE AL AUDITOR." % (ev, em))
        else:
            print("     >>> gana %s por %d contra %d" % (viv if ev > em else mue, max(ev, em), min(ev, em)))
        print("  2. ALIAS DEL SUPERVIVIENTE TRAS LA FUSION")
        print("     %s" % sorted(set((G[viv].get("ids_alias") or []) + [mue])))
        print("  3. ENTRADAS QUE SE REDIRIGEN")
        n = 0
        for kk, vv in sorted(G.items()):
            if vv.get("deprecado") or kk == mue:
                continue
            for c in CAMPOS:
                if mue in (vv.get(c) or []):
                    print("     %-44s %-17s -> %s" % (kk, c, viv)); n += 1
        if not n:
            print("     ninguna")

    print()
    print("### 4. DUPLICADAS QUE LA FUSION FABRICA (clase OP-S-12)")
    print("    Solo las NUEVAS: se cuentan las duplicadas antes y despues, y se resta.")
    ALIAS0 = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}
    def res0(x):
        s = set()
        while x in ALIAS0 and x not in s:
            s.add(x)
            x = ALIAS0[x]
        return x
    def dups(f):
        out = set()
        for kk, vv in G.items():
            if vv.get("deprecado"):
                continue
            for c in CAMPOS:
                d = [f(y) for y in (vv.get(c) or []) if f(y) != kk]
                for x, n in collections.Counter(d).items():
                    if n > 1:
                        out.add((kk, c, x))
        return out
    nuevas = sorted(dups(res) - dups(res0))
    for kk, c, x in nuevas:
        print("     %-44s %-17s -> %s" % (kk, c, x))
    print("     TOTAL NUEVAS: %d" % len(nuevas))

    print()
    print("### 5. AUTO-ARISTAS QUE LA FUSION CREARIA (clase OP-S-07)")
    auto = 0
    for viv, _ in pares:
        for c in CAMPOS:
            for y in (G[viv].get(c) or []):
                if res(y) == viv:
                    print("     %s %s -> %s resuelve a si mismo" % (viv, c, y)); auto += 1
    if not auto:
        print("     ninguna")

    if args.acto:
        acto = [x.strip() for x in args.acto.split(",") if x.strip()]
        print()
        print("### 6. ARISTAS INTERNAS DEL ACTO QUE SOBREVIVEN, con su direccion resuelta")
        vivos = sorted(set(res(x) for x in acto))
        hay = 0
        for a in vivos:
            for c in CAMPOS:
                dest = sorted(set(res(y) for y in (G[a].get(c) or [])) & set(vivos) - {a})
                for d in dest:
                    flecha = "%s -> %s" % (a, d) if c == "nodos_siguientes" else "%s -> %s" % (d, a)
                    print("     %-30s.%-17s  %s" % (a, c, flecha)); hay += 1
        if not hay:
            print("     NINGUNA: el acto queda sin aristas internas tras la fusion")


if __name__ == "__main__":
    main()
