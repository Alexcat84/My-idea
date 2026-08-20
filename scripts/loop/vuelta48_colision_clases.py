# -*- coding: utf-8 -*-
"""Vuelta 48, TAREA 2: LA GUARDA QUE DECIDE QUE ACTOS SE DEJAN FUNDIR.

ESTRICTAMENTE DE SOLO LECTURA.

LA PREGUNTA, y sale de leer los actos y no de una teoria: cuando un acto tiene
DENTRO un par que no es A, que le pasa al archivo si se funde?

LA MEDICION: se simula la fusion sobre una COPIA EN MEMORIA del mapa de alias
(nada se escribe), se RESUELVEN todos los veredictos del archivo con ese mapa, y
se cuenta cuantos PARES RESUELTOS quedan con DOS CLASES DISTINTAS a la vez. Un
par resuelto con una A y una D publicadas es una contradiccion contra una cifra
publicada con su corte, que es condicion de parada por la regla 5 de EJECUTOR.md
si se consuma. Medirlo ANTES es la unica forma de no consumarla.

LAS DOS FORMAS QUE SE SIMULAN POR ACTO:
  a) FUSION ENTERA: todos los miembros al superviviente.
  b) FUSION DEL NUCLEO: solo el subgrafo de miembros unidos por A entre si,
     dejando fuera al nodo mixto (que por P.12 iria a enlace).

Uso:
  python scripts/loop/vuelta48_colision_clases.py --nomina docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl
                                                  [--hasta 50]
"""
import argparse
import collections
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", required=True)
    ap.add_argument("--hasta", type=int, default=0, help="0 = todos los CERRADOS")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    BASE = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}
    V = cargar(VER)

    def hacer_res(extra):
        m = dict(BASE)
        m.update(extra)

        def res(x):
            s = set()
            while x in m and x not in s:
                s.add(x)
                x = m[x]
            return x
        return res

    res0 = hacer_res({})
    # veredictos con su par ya resuelto en el estado de HOY
    hoy = []
    for r in V:
        hoy.append((res0(r["nodo_a"]), res0(r["nodo_b"]), r["clase"], r["puesto_intra"]))

    def colisiones(extra):
        res = hacer_res(extra)
        por_par = collections.defaultdict(set)
        detalle = collections.defaultdict(list)
        for na, nb, cl, pu in hoy:
            ra, rb = res(na), res(nb)
            if ra == rb:
                continue
            k = frozenset((ra, rb))
            por_par[k].add(cl)
            detalle[k].append((cl, pu))
        malos = {k: detalle[k] for k, v in por_par.items() if len(v) > 1}
        return malos

    base_malos = colisiones({})
    print("=" * 78)
    print("COLISIONES DE CLASE, medidas sobre copia en memoria. NADA SE ESCRIBE.")
    print("=" * 78)
    print("EN EL ESTADO DE HOY, sin fundir nada: pares resueltos con dos clases = %d"
          % len(base_malos))
    for k, d in sorted(base_malos.items(), key=lambda x: sorted(x[0])):
        print("   %s -> %s" % (sorted(k), sorted(d)))

    R = cargar(a.nomina)
    C = [r for r in R if r["estado"] == "CERRADO"]
    if a.hasta:
        C = C[:a.hasta]

    # clase de cada par interno, en el estado de hoy
    idx = {}
    for na, nb, cl, pu in hoy:
        if na != nb:
            idx[frozenset((na, nb))] = (cl, pu)

    print()
    print("POR ACTO: colisiones NUEVAS que fabricaria cada forma de fundir")
    print("%4s %5s %-10s %10s %10s" % ("acto", "tam", "figura", "ENTERA", "NUCLEO-A"))
    resumen = collections.Counter()
    limpios, sucios = [], []
    for n, act in enumerate(C, 1):
        mi = sorted(act["miembros"])
        clases = dict((p, idx.get(frozenset(p), ("?", 0))[0])
                      for p in itertools.combinations(mi, 2))
        puro = set(clases.values()) == {"A"}

        # a) fusion ENTERA: el primero por orden alfabetico hace de superviviente,
        #    da igual cual sea: la colision no depende de quien sobreviva.
        sup = mi[0]
        nuevas_ent = len(colisiones(dict((x, sup) for x in mi[1:]))) - len(base_malos)

        # b) fusion del NUCLEO-A: subgrafo de miembros unidos por A entre si.
        ady = collections.defaultdict(set)
        for p, c in clases.items():
            if c == "A":
                ady[p[0]].add(p[1])
                ady[p[1]].add(p[0])
        nucleos = []
        visto = set()
        for x in mi:
            if x in visto or x not in ady:
                continue
            pila, comp = [x], set()
            while pila:
                y = pila.pop()
                if y in comp:
                    continue
                comp.add(y)
                pila.extend(ady[y] - comp)
            visto |= comp
            # nucleo = clique de A (todos con todos en A)
            clique = [z for z in sorted(comp)
                      if all(clases.get(tuple(sorted((z, w)))) == "A"
                             for w in comp if w != z)]
            if len(clique) > 1:
                nucleos.append(clique)
        extra = {}
        for cl in nucleos:
            for x in cl[1:]:
                extra[x] = cl[0]
        nuevas_nuc = (len(colisiones(extra)) - len(base_malos)) if extra else 0

        fig = "TODO-A" if puro else "MIXTO"
        resumen[(fig, nuevas_ent == 0)] += 1
        (limpios if nuevas_ent == 0 else sucios).append(n)
        print("%4d %5d %-10s %10d %10d" % (n, act["tamano"], fig, nuevas_ent, nuevas_nuc))

    print()
    print("RESUMEN sobre %d actos:" % len(C))
    print("  actos que NO fabrican ninguna colision al fundirse ENTEROS: %d" % len(limpios))
    print("  actos que SI fabrican colision al fundirse enteros        : %d" % len(sucios))
    print("  los que la fabrican: %s" % sucios)
    print()
    print("  cruce figura contra colision (fusion ENTERA):")
    for (fig, ok), c in sorted(resumen.items()):
        print("    %-8s sin colision=%-5s : %d" % (fig, ok, c))
    return 0


if __name__ == "__main__":
    sys.exit(main())
