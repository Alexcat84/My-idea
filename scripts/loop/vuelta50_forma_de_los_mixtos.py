# -*- coding: utf-8 -*-
"""vuelta50_forma_de_los_mixtos.py . CLASIFICA LA FORMA DEL SUBGRAFO `A` DE CADA
ACTO MIXTO, ANTES DE APLICARLE LA RECETA DE `P.12`.

POR QUE EXISTE, y el motivo se levanto LEYENDO y no teorizando: el encargo de la
vuelta 50 manda, por cada acto mixto, "elegir el superviviente de la PARTE A" y
"leer el MIXTO contra ese superviviente". Esa receta presupone una forma
concreta, que es la que tenia el unico acto ya resuelto (el del SPIN, vuelta 49):
una CLIQUE de pares `A` de dos o mas nodos, mas UN nodo colgando que entra a la
componente por UNA sola arista `A` y tiene `D` con el resto. Ahi la parte A y el
mixto son dos cosas distintas y la receta se aplica sola.

EL PRIMER ACTO QUE ABRI EN ESTA VUELTA NO TIENE ESA FORMA, y por eso existe este
instrumento antes que ninguna fusion. Sus pares `A` no forman clique: forman una
ESTRELLA cuyo centro es el nodo que REPITE contra los otros tres, y esos tres son
`D` entre si. Ahi no hay "la parte A" ni "el mixto": hay tres supervivientes
posibles y un nodo que repite contra los tres, que es una decision que el archivo
NO tomo (su propio veredicto la deja escrita como CONDICION VIVA).

QUE CLASIFICA, sobre el subgrafo que forman SOLO los pares `A` del acto:
  CLIQUE_MAS_COLGANTE : hay una clique `A` maximal de tamano >= 2 y EXACTAMENTE
                        un nodo fuera de ella. Es la forma del SPIN y la unica a
                        la que la receta del encargo se aplica tal cual.
  ESTRELLA            : un solo nodo (el CENTRO) toca todas las aristas `A` y los
                        demas no tienen ninguna `A` entre si. El centro es el que
                        repite contra varios; elegir cual lo absorbe es una
                        decision que la receta no toma.
  OTRA                : cualquier otra forma. Se imprime entera y no se fuerza.

Y para cada acto imprime ademas quien es el CENTRO o la CLIQUE, quien cuelga, y
los puestos de cada arista, para que la adjudicacion sea de lectura.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo ni un veredicto: imprime.

Uso:
  python scripts/loop/vuelta50_forma_de_los_mixtos.py \
      --hoy docs/loop/RECOMPUTO_V50_APERTURA.jsonl --hasta 35
"""
import argparse
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def cargar_jsonl(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hoy", required=True)
    ap.add_argument("--hasta", type=int, default=0, help="0 = todos los CERRADOS")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            todos[d["node_id"]] = d
    alias = {}
    for nid, d in todos.items():
        if not (d.get("deprecado") or d.get("deprecated")):
            for x in (d.get("ids_alias") or []):
                alias[x] = nid

    def res(x):
        s = set()
        while x in alias and x not in s:
            s.add(x)
            x = alias[x]
        return x

    porpar = {}
    for v in cargar_jsonl(VER):
        porpar.setdefault(frozenset((res(v["nodo_a"]), res(v["nodo_b"]))), []).append(v)

    cerrados = [c for c in cargar_jsonl(a.hoy) if c["estado"] == "CERRADO"]
    if a.hasta:
        cerrados = cerrados[:a.hasta]

    print("=" * 78)
    print("LA FORMA DEL SUBGRAFO A DE CADA ACTO MIXTO, medida hoy")
    print("nomina: %s (%d actos mirados)" % (a.hoy, len(cerrados)))
    print("=" * 78)
    print()

    cuenta = {}
    for n, c in enumerate(cerrados, 1):
        ms = sorted(set(res(m) for m in c["miembros"]))
        aristas_a, aristas_no = [], []
        for x, y in itertools.combinations(ms, 2):
            vs = porpar.get(frozenset((x, y))) or []
            cl = sorted(set(v["clase"] for v in vs))
            ps = [v["puesto_intra"] for v in vs]
            if "A" in cl:
                aristas_a.append((x, y, cl, ps))
            if [k for k in cl if k != "A"]:
                aristas_no.append((x, y, cl, ps))
        if not aristas_a or not aristas_no:
            continue  # no es mixto

        adyA = {m: set() for m in ms}
        for x, y, _, _ in aristas_a:
            adyA[x].add(y)
            adyA[y].add(x)

        # LA CLIQUE A MAXIMAL, por fuerza bruta (los actos son de 2 a 4 nodos).
        mejor = []
        for k in range(len(ms), 1, -1):
            for sub in itertools.combinations(ms, k):
                if all(y in adyA[x] for x, y in itertools.combinations(sub, 2)):
                    mejor = list(sub)
                    break
            if mejor:
                break
        fuera = [m for m in ms if m not in mejor]

        centros = [m for m in ms if len(adyA[m]) == len(ms) - 1]
        hojas_sin_a = all(not (adyA[x] & adyA[y] - {x, y}) or True for x, y in [])
        es_estrella = (len(centros) == 1 and len(mejor) == 2
                       and all(len(adyA[m]) == 1 for m in ms if m not in centros))

        if len(mejor) >= 2 and len(fuera) == 1 and not es_estrella:
            forma = "CLIQUE_MAS_COLGANTE"
        elif es_estrella:
            forma = "ESTRELLA"
        else:
            forma = "OTRA"
        cuenta[forma] = cuenta.get(forma, 0) + 1

        print("--- ACTO %d  tam %d  FORMA: %s" % (n, len(ms), forma))
        print("      miembros: %s" % ", ".join(ms))
        print("      aristas A  : %s"
              % "; ".join("%s + %s [%s]" % (x, y, ",".join(str(p) for p in ps))
                          for x, y, _, ps in aristas_a))
        print("      aristas NO A: %s"
              % "; ".join("%s + %s %s[%s]" % (x, y, ",".join(cl),
                                              ",".join(str(p) for p in ps))
                          for x, y, cl, ps in aristas_no))
        if forma == "CLIQUE_MAS_COLGANTE":
            print("      PARTE A (clique): %s" % ", ".join(mejor))
            print("      EL MIXTO que cuelga: %s" % fuera[0])
            print("      entra a la componente por: %s"
                  % "; ".join("%s + %s [%s]" % (x, y, ",".join(str(p) for p in ps))
                              for x, y, _, ps in aristas_a
                              if fuera[0] in (x, y)))
        elif forma == "ESTRELLA":
            print("      CENTRO (el que toca todas las A): %s" % centros[0])
            print("      LAS PUNTAS (sin ninguna A entre si): %s"
                  % ", ".join(m for m in ms if m != centros[0]))
            print("      AVISO: no hay 'la parte A' ni 'el mixto'. El centro repite")
            print("             contra cada punta y elegir cual lo absorbe es una")
            print("             decision que la receta del encargo NO toma.")
        print()

    print("=" * 78)
    print("RESUMEN DE FORMAS")
    for k in sorted(cuenta):
        print("  %-22s %d" % (k, cuenta[k]))
    print("  TOTAL de actos mixtos: %d" % sum(cuenta.values()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
