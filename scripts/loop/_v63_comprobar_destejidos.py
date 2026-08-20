# -*- coding: utf-8 -*-
"""_v63_comprobar_destejidos.py . COMPRUEBA CONTRA EL GRAFO DE HOY QUE LOS DOS
GRANDES DE DESTEJIDO DE LA EXCLUSION DE OP-U-02 YA NO SON ACTOS ABIERTOS, Y DICE
POR QUE CADA UNO. NO LO SUPONE.

POR QUE EXISTE. El encargo de la vuelta 63 pide que las exclusiones que el plan
escribe (docs/plan/03_FUSIONES.md lineas 226 a 228) vayan COMPROBADAS contra el
grafo de hoy, y nombra en particular los dos grandes de destejido, que OP-D-03 y
OP-D-04 ya consumieron. Una busqueda negativa no se puede citar (regla 9 del
EJECUTOR), asi que aqui se mide POR QUE desaparecieron, no solo QUE
desaparecieron.

DE SOLO LECTURA ENTERO.

Uso: python scripts/loop/_v63_comprobar_destejidos.py --componentes <jsonl>
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NL = chr(10)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--componentes", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    alias, dep = {}, {}
    for f in sorted(os.listdir(NODOS)):
        if not f.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
        dep[d["node_id"]] = bool(d.get("deprecado") or d.get("deprecated"))
        for x in (d.get("ids_alias") or []):
            alias[x] = d["node_id"]

    def res(x):
        v = set()
        while x in alias and x not in v:
            v.add(x)
            x = alias[x]
        return x

    comps = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, a.componentes.replace("/", os.sep)), encoding="utf-8")
             if l.strip()]
    fichas = {}
    for l in io.open(OPERACIONES, encoding="utf-8"):
        if l.strip():
            d = json.loads(l)
            fichas[d.get("id_op")] = d
    veredictos = [json.loads(l) for l in io.open(VEREDICTOS, encoding="utf-8") if l.strip()]

    print("=" * 78)
    print("LOS DOS GRANDES DE DESTEJIDO, COMPROBADOS CONTRA EL GRAFO DE HOY")
    print("  componentes: %s" % a.componentes)
    print("  veredictos : docs/INTRA_DOMINIO_VEREDICTOS.jsonl (%d)" % len(veredictos))
    print("=" * 78)

    for id_op in ("OP-D-03", "OP-D-04"):
        op = fichas[id_op]
        nom = list(op.get("nodos") or [])
        print()
        print("-" * 78)
        print("%s . la ficha nombra %d nodos" % (id_op, len(nom)))
        print("-" * 78)
        print("  %-46s %-46s %s" % ("id de la ficha", "resuelve HOY a", "deprecado"))
        destinos = set()
        for x in nom:
            r = res(x)
            destinos.add(r)
            print("  %-46s %-46s %s" % (x, r, dep.get(r, "NO EXISTE")))
        print("  supervivientes distintos tras resolver: %d" % len(destinos))
        en_comp = [c for c in comps if set(c["miembros"]) & destinos]
        print("  componentes del recomputo de HOY que tocan esa nomina: %d" % len(en_comp))
        for c in en_comp:
            print("     estado=%s tamano=%d" % (c["estado"], c["tamano"]))
        pares = [v for v in veredictos
                 if v.get("nodo_a") in destinos and v.get("nodo_b") in destinos]
        clases = {}
        for v in pares:
            clases[v.get("clase")] = clases.get(v.get("clase"), 0) + 1
        print("  pares INTERNOS entre esos supervivientes en el archivo: %d, por clase %s"
              % (len(pares), clases))
        for v in pares:
            print("     %-44s %-44s clase=%s"
                  % (v.get("nodo_a"), v.get("nodo_b"), v.get("clase")))
        print()
        if len(destinos) < len(nom):
            print("  LA CAUSA, MEDIDA: la nomina de %d resuelve hoy a %d nodo(s). LA "
                  "COMPONENTE SE CONSUMIO POR FUSION." % (len(nom), len(destinos)))
        elif not pares or "A" not in clases:
            print("  LA CAUSA, MEDIDA: los %d nodos siguen VIVOS y ninguno resuelve a otro, "
                  "asi que lo que desaparecio NO son los nodos: son LAS ARISTAS A. Los %d "
                  "pares internos que el archivo tiene entre ellos son %s, y una componente "
                  "de este recomputo se forma SOLO con aristas A."
                  % (len(destinos), len(pares),
                     " y ".join("%d de clase %s" % (v, k) for k, v in sorted(clases.items()))))
        else:
            print("  LA CAUSA NO QUEDA MEDIDA POR ESTE INSTRUMENTO y por eso NO SE AFIRMA.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
