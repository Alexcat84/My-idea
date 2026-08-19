# -*- coding: utf-8 -*-
"""vuelta40_reciprocidad_post.py - LO QUE LA FUSION DEJARIA ROTO, MEDIDO ANTES.

ESTRICTAMENTE DE SOLO LECTURA. No escribe en el archivo, ni en un nodo, ni en el plan.

POR QUE EXISTE, y es una pregunta que ningun instrumento de la casa contestaba.
scripts/loop/vuelta33_fundir.py, que es el ejecutor de fusiones, redirige lo que
NOMBRA al absorbido y depreca al absorbido. Con eso el vecino queda apuntando al
superviviente. Pero el superviviente NO gana en SU PROPIO fichero las aristas que
el absorbido declaraba: su lista no se toca. Resultado: una arista que hoy esta
declarada en los DOS extremos puede quedar declarada en UNO SOLO despues de la
fusion.

Esa rotura no la ve simular_fusion.py (que mide duplicadas y auto aristas, no
reciprocidad) ni la ve la tabla de perdidas (que es de contenido, no de grafo).
Aqui se mide, y se mide TRES veces:

  1. LA VARA DE LA CASA: que porcentaje de las aristas del grafo ENTERO es
     reciproco hoy. Sin esa cifra no se sabe si romper la reciprocidad es un
     defecto o es lo corriente.
  2. LAS ROTURAS QUE CADA FUSION FABRICA, una por una, con nombre y direccion.
  3. LAS ARISTAS QUE HAY QUE REPONER en el superviviente para que la fusion no
     deje el grafo peor de como lo encontro (P.16, quien fabrica limpia).

SUCESOR DECLARADO de scripts/loop/vuelta38_reciprocidad_post.py (EJECUTOR.md
regla 2), y lo que cambia es una sola cosa dicha entera: aquel traia LAS DOS
FUSIONES DE OP-D-04 ESCRITAS DENTRO DEL CODIGO y no servia para ninguna otra.
Este LEE LA FUSION DE LA LINEA DE ORDENES. La aritmetica de los cuatro bloques
es LA MISMA y a proposito: cambiar la vara y el sujeto en la misma corrida haria
incomparables las dos medidas.

Uso:
  python scripts/loop/vuelta40_reciprocidad_post.py       --nombre "OP-D-05" --superviviente seleccion_ceo_fundador       --absorbido asignacion_de_titulos_ejecutivos       --absorbido errores_comunes_asignacion_roles
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

def _fusiones_de_la_linea():
    """La nomina entra por la linea de ordenes, no por el codigo."""
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--nombre", required=True)
    ap.add_argument("--superviviente", required=True)
    ap.add_argument("--absorbido", action="append", required=True)
    a = ap.parse_args()
    return [(a.nombre, a.superviviente, list(a.absorbido))]


FUSIONES = None   # se rellena en el arranque, desde la linea de ordenes


def bloque(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    with io.open(GRAFO, encoding="utf-8") as fh:
        G = json.load(fh)["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    bloque("1. LA VARA DE LA CASA: cuanta reciprocidad tiene el grafo HOY")
    tot = rec = 0
    for nid, d in G.items():
        if d.get("deprecado"):
            continue
        for c in CAMPOS:
            for y in (d.get(c) or []):
                dest = res(y)
                if dest not in G or dest == nid:
                    continue
                tot += 1
                if nid in (G[dest].get(OPUESTO[c]) or []):
                    rec += 1
    print("  aristas declaradas por nodos vivos, resueltas (P.1): %d" % tot)
    print("  de ellas RECIPROCAS (el otro extremo la devuelve): %d" % rec)
    print("  tasa de reciprocidad del grafo: %.2f por ciento" % (100.0 * rec / tot))
    print("")
    print("  LECTURA DE LA CIFRA: si la tasa es alta, la reciprocidad es la practica")
    print("  de la casa y romperla es un defecto que el plan tiene que reponer.")

    for nombre, sup, mueren in FUSIONES:
        bloque("2. %s: lo que la fusion hacia %s dejaria declarado en UN SOLO extremo"
               % (nombre, sup))
        alias2 = dict(ALIAS)
        for m in mueren:
            alias2[m] = sup

        def res2(x):
            s = set()
            while x in alias2 and x not in s:
                s.add(x)
                x = alias2[x]
            return x

        # El ejecutor redirige lo que NOMBRA al absorbido, y NO toca la lista propia
        # del superviviente. Asi que tras la fusion el vecino declara al superviviente
        # y el superviviente solo devuelve lo que ya tenia en su fichero.
        propias_sup = dict((c, [res(y) for y in (G[sup].get(c) or [])]) for c in CAMPOS)
        roturas = []
        for nid, d in G.items():
            if d.get("deprecado") or nid in mueren or nid == sup:
                continue
            for c in CAMPOS:
                for y in (d.get(c) or []):
                    if y not in mueren:
                        continue
                    # el vecino pasara a declarar al superviviente en el campo c
                    devuelve = nid in propias_sup[OPUESTO[c]]
                    if not devuelve:
                        roturas.append((nid, c, sup))
        print("  vecinos que quedarian apuntando al superviviente sin que el devuelva:")
        if not roturas:
            print("     ninguno")
        for nid, c, s in sorted(set(roturas)):
            print("     %-45s %-17s -> %s" % (nid, c, s))
        print("  TOTAL ROTURAS: %d" % len(set(roturas)))

        print("")
        print("  3. ARISTAS A REPONER EN %s para no dejar el grafo peor (P.16):" % sup)
        reponer = sorted(set((OPUESTO[c], nid) for nid, c, _s in roturas))
        if not reponer:
            print("     ninguna")
        for campo, nid in reponer:
            print("     %s.%-17s += %s" % (sup, campo, nid))
        print("     TOTAL A REPONER: %d" % len(reponer))

        print("")
        print("  4. LAS PROPIAS DEL ABSORBIDO QUE SE QUEDAN EN UN NODO DEPRECADO:")
        n = 0
        for m in mueren:
            for c in CAMPOS:
                for y in (G[m].get(c) or []):
                    dest = res2(y)
                    if dest == sup:
                        continue
                    ya = dest in propias_sup[c]
                    if not ya:
                        print("     %-45s %-17s -> %s   %s"
                              % (m, c, dest,
                                 "el vecino la devuelve, se redirige sola"
                                 if m in (G[dest].get(OPUESTO[c]) or []) else
                                 "NADIE la devuelve: SE PIERDE"))
                        n += 1
        if not n:
            print("     ninguna")

    bloque("VEREDICTO DE LA MEDICION")
    print("la tasa de reciprocidad del grafo esta medida; las roturas que cada fusion")
    print("fabricaria estan contadas y nombradas; la lista de aristas a reponer esta")
    print("impresa. NADA SE ESCRIBIO.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    FUSIONES = _fusiones_de_la_linea()
    raise SystemExit(main())
