# -*- coding: utf-8 -*-
"""Aplica a un pack las aristas internas de un mundo, leidas y decididas una a una (integracion del mundo 11, paso 5,
28 sep 2026). Cada arista A -> B afirma una continuidad de contenido (decision del fundador del 25 sep 2026) y viaja
con su `por_que` en el fichero de aristas; aqui solo se escriben, reciprocas: B entra en `A.nodos_siguientes` y A en
`B.nodos_previos`.

Se niega a escribir si una arista nombra un nodo que no esta en el pack, si une un nodo consigo mismo o si el grafo
del pack con las aristas cerraria un ciclo dirigido. Es idempotente: una arista ya presente no se duplica.

    python scripts/aplicar_aristas_internas.py docs/puente_forja/aristas_internas_mundo11.json --nodos packs/primer_equipo/nodos
    python scripts/aplicar_aristas_internas.py <aristas.json> --nodos <carpeta> --comprobar     (solo valida)
"""
import argparse
import json
import sys
from pathlib import Path


def cargar(carpeta):
    nodos = {}
    for p in sorted(Path(carpeta).glob("*.json")):
        n = json.loads(p.read_text(encoding="utf-8"))
        nodos[n["node_id"]] = (p, n)
    return nodos


def hay_ciclo(ady):
    blanco, gris, negro = 0, 1, 2
    color = {}

    def visitar(x):
        pila = [(x, iter(ady.get(x, ())))]
        color[x] = gris
        while pila:
            nodo, hijos = pila[-1]
            siguiente = next(hijos, None)
            if siguiente is None:
                color[nodo] = negro
                pila.pop()
            elif color.get(siguiente, blanco) == gris:
                return True
            elif color.get(siguiente, blanco) == blanco:
                color[siguiente] = gris
                pila.append((siguiente, iter(ady.get(siguiente, ()))))
        return False

    return any(color.get(x, blanco) == blanco and visitar(x) for x in list(ady))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("aristas")
    ap.add_argument("--nodos", required=True)
    ap.add_argument("--comprobar", action="store_true")
    args = ap.parse_args()
    aristas = json.loads(Path(args.aristas).read_text(encoding="utf-8"))["aristas"]
    nodos = cargar(args.nodos)
    fallos = []
    ady = {i: set(t for t in (n.get("nodos_siguientes") or []) if t in nodos) for i, (_, n) in nodos.items()}
    for x in aristas:
        a, b = x["de"], x["a"]
        if a not in nodos or b not in nodos:
            fallos.append("%s -> %s: nodo fuera del pack" % (a, b))
        elif a == b:
            fallos.append("%s: arista consigo mismo" % a)
        elif not str(x.get("por_que", "")).strip():
            fallos.append("%s -> %s: sin por que" % (a, b))
        else:
            ady[a].add(b)
    if not fallos and hay_ciclo(ady):
        fallos.append("el grafo del pack con estas aristas cierra un ciclo dirigido")
    if fallos:
        print("ARISTAS RECHAZADAS: %d" % len(fallos), *fallos[:20], sep="\n  ")
        return 1
    if args.comprobar:
        print("ARISTAS VALIDAS: %d (sin escribir)" % len(aristas))
        return 0
    tocados, nuevas = set(), 0
    for x in aristas:
        a, b = x["de"], x["a"]
        na, nb = nodos[a][1], nodos[b][1]
        if b not in (na.get("nodos_siguientes") or []):
            na.setdefault("nodos_siguientes", []).append(b)
            tocados.add(a)
            nuevas += 1
        if a not in (nb.get("nodos_previos") or []):
            nb.setdefault("nodos_previos", []).append(a)
            tocados.add(b)
    for i in sorted(tocados):
        p, n = nodos[i]
        p.write_text(json.dumps(n, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("ARISTAS APLICADAS: %d nuevas en %d nodos" % (nuevas, len(tocados)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
