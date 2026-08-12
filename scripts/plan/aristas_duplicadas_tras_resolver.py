#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""aristas_duplicadas_tras_resolver.py . LAS ARISTAS QUE SE REPITEN AL RESOLVER.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo. Escribe solo en docs/plan/.

LA CLASE QUE MIDE, y de donde salio. La fase 3 de Coleman se fundio en cuatro ids
y quedaron DIEZ aristas apuntando a un alias, LAS DIEZ con su gemela literal al
destino EN EL MISMO CAMPO. O sea: la fusion reescribio la referencia y ademas dejo
la vieja. Eso no es un fallo del resolutor, es BASURA ACUMULADA: dos entradas de la
misma lista que, tras resolver, van al mismo sitio.

QUE CUENTA: por cada nodo vivo y por cada uno de sus dos campos de arista, resuelve
todos los ids con la semantica de resolverId (camina la cadena de alias) y cuenta
cuantas entradas SOBRAN, o sea len(lista) menos len(destinos distintos).

QUE NO CUENTA, a proposito:
  - un mismo destino en nodos_previos Y en nodos_siguientes NO es duplicado: es una
    arista de ida y otra de vuelta, y decidir eso es otra operacion.
  - la auto-arista (destino igual al propio nodo) NO se cuenta aqui: es OP-S-07, y
    contarla dos veces inflaria las dos cifras.

REGLA P.1 DEL BANCO DEL PLAN: todo conteo que toque ids pasa por el resolutor antes
de contar.
"""
import argparse, collections, json, io, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CAMPOS = ("nodos_previos", "nodos_siguientes")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grafo", default=str(RAIZ / "dataset" / "metadata" / "master_graph.json"))
    ap.add_argument("--salida", default=str(RAIZ / "docs" / "plan" / "ARISTAS_DUPLICADAS.jsonl"))
    args = ap.parse_args()

    G = json.load(io.open(args.grafo, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    filas = []
    por_dom = collections.Counter()
    nodos_dom = collections.Counter()
    por_campo = collections.Counter()
    motivo = collections.Counter()
    for k, v in G.items():
        if v.get("deprecado"):
            continue
        tocado = False
        for campo in CAMPOS:
            L = v.get(campo) or []
            grupos = collections.defaultdict(list)
            for y in L:
                d = res(y)
                if d == k:          # auto arista: es OP-S-07, no se cuenta aqui
                    continue
                grupos[d].append(y)
            for destino, origenes in grupos.items():
                if len(origenes) < 2:
                    continue
                literal = destino in origenes
                filas.append({
                    "nodo": k, "dominio": v.get("dominio") or "?", "campo": campo,
                    "destino": destino, "entradas": origenes, "sobran": len(origenes) - 1,
                    "tiene_la_literal": literal,
                    "clase": ("el id nuevo mas su alias" if literal else "dos alias del mismo destino")})
                por_dom[v.get("dominio") or "?"] += len(origenes) - 1
                por_campo[campo] += len(origenes) - 1
                motivo["el id nuevo mas su alias" if literal else "dos alias del mismo destino"] += len(origenes) - 1
                tocado = True
        if tocado:
            nodos_dom[v.get("dominio") or "?"] += 1

    with io.open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
        for x in sorted(filas, key=lambda r: (-r["sobran"], r["nodo"])):
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")

    vivos = sum(1 for k, v in G.items() if not v.get("deprecado"))
    total = sum(f["sobran"] for f in filas)
    nodos = len(set(f["nodo"] for f in filas))
    print("ARISTAS DUPLICADAS TRAS RESOLUCION")
    print()
    print("| | |")
    print("|---|---:|")
    print("| nodos vivos revisados | %d |" % vivos)
    print("| **nodos con al menos una duplicada** | **%d** |" % nodos)
    print("| **entradas que SOBRAN** | **%d** |" % total)
    print("| grupos afectados (nodo mas campo mas destino) | %d |" % len(filas))
    print()
    print("POR MOTIVO")
    for m, n in motivo.most_common():
        print("   %-34s %d" % (m, n))
    print()
    print("POR CAMPO")
    for c, n in por_campo.most_common():
        print("   %-18s %d" % (c, n))
    print()
    print("| dominio | nodos | duplicadas |")
    print("|---|---:|---:|")
    for d in sorted(por_dom, key=lambda x: -por_dom[x]):
        print("| %s | %d | %d |" % (d, nodos_dom[d], por_dom[d]))
    print()
    print("LOS PEORES")
    for f in sorted(filas, key=lambda r: -r["sobran"])[:10]:
        print("   %-46s %-17s -> %-40s sobran %d" % (f["nodo"], f["campo"], f["destino"], f["sobran"]))
    print()
    print("escrito: %s" % args.salida)


if __name__ == "__main__":
    main()
