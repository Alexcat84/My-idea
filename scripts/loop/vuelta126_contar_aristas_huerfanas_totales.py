# -*- coding: utf-8 -*-
"""vuelta126_contar_aristas_huerfanas_totales.py . CUENTA, SOBRE EL CATALOGO
DE HOY ENTERO, LAS "ARISTAS HUERFANAS POR FUSION" (TAREA 2.c de la vuelta
126, ficha nueva docs/PENDIENTES.md).

QUE CUENTA. Generaliza a TODO el grafo la comprobacion (4) nueva de
scripts/loop/verificar_fusion_ops09.py (ver su docstring): para cada nodo
DEPRECADO del catalogo, se leen sus dos listas TAL COMO QUEDARON (registro
historico), se resuelve cada entrada con el resolutor de HOY y, si resuelve a
un nodo VIVO distinto de a quien el propio muerto resuelve (su superviviente),
se comprueba si esa arista existe HOY entre los dos supervivientes, mirando
las dos vistas. Si no existe, es una arista huerfana por fusion: el gemelo
exacto de la que la vuelta 125 corto en OP-S-09 (docs/loop/ACTA_AUDITOR.md,
acta de la vuelta 125, seccion 4.1), mismo mecanismo, distinta operacion.

Los pares se acumulan en un SET (origen, destino) para no contar dos veces la
misma arista cuando los DOS extremos historicos eran nodos deprecados de la
misma fusion (cada uno la ve desde su lado, pero el par resuelto es el mismo).

Uso:
  python scripts/loop/vuelta126_contar_aristas_huerfanas_totales.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


def cargar():
    with open(RUTA_GRAFO, encoding="utf-8") as f:
        return json.load(f)["nodos"]


def resolver_de(nodos):
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        for x in (n.get("ids_alias") or []):
            alias[x] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return resolver


def main():
    nodos = cargar()
    resolver = resolver_de(nodos)
    faltantes = set()

    for muere, n in nodos.items():
        if not n.get("deprecado"):
            continue
        sup = resolver(muere)
        if sup == muere:
            continue
        n_sup = nodos.get(sup)
        if n_sup is None or n_sup.get("deprecado"):
            continue

        for x in (n.get("nodos_siguientes") or []):
            destino = resolver(x)
            if destino == sup:
                continue
            n_destino = nodos.get(destino)
            if n_destino is None or n_destino.get("deprecado"):
                continue
            presente = destino in (n_sup.get("nodos_siguientes") or []) or \
                       sup in (n_destino.get("nodos_previos") or [])
            if not presente:
                faltantes.add((sup, destino))

        for x in (n.get("nodos_previos") or []):
            origen = resolver(x)
            if origen == sup:
                continue
            n_origen = nodos.get(origen)
            if n_origen is None or n_origen.get("deprecado"):
                continue
            presente = origen in (n_sup.get("nodos_previos") or []) or \
                       sup in (n_origen.get("nodos_siguientes") or [])
            if not presente:
                faltantes.add((origen, sup))

    print("ARISTAS HUERFANAS POR FUSION en el catalogo de HOY: %d" % len(faltantes))
    for o, d in sorted(faltantes):
        print("  %s -> %s" % (o, d))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
