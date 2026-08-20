# -*- coding: utf-8 -*-
"""vuelta58_relectura_acto32.py . LA RELECTURA CONJUNTA DEL ACTO 32 DEL TRAMO 4,
MEDIDA CONTRA EL GRAFO PRE FUSION Y NO CONTRA NINGUNA NOTA.

POR QUE NACE: el acta 57 del auditor (secciones 2 y 4, discutible D4) sostiene
que el acto 32 (programa_de_referidos_de_franquiciados y
referidos_franquiciados_existentes) es EMPATE SIN VARA por la letra vigente y
que la vuelta 57 lo fundio rompiendo el empate con la CANTIDAD de lineas
propias declaradas, que es un conteo sobre la letra que ninguna acta adjudica.
El encargo de la vuelta 58 (TAREA 1.1) manda VERIFICAR CONTRA EL GRAFO y
DECIDIR CON LA VARA antes de tocar nada.

DE SOLO LECTURA. Imprime; no toca ni un nodo.

LA ARITMETICA DE LAS VARAS SE COPIA ENTERA de scripts/loop/vuelta56_varas_tramo3.py
(pasos, condiciones y cableado como vecinos resueltos distintos), que es el
instrumento con el que el tramo 4 se talló y el que el auditor re-derivo por su
cuenta. Lo unico que no es copia: aqui se mide sobre el arbol que se le pase en
--raiz, para poder medir el estado PRE FUSION, y se imprime tambien el ACTO 11
como contraste, que es el precedente que la propia vuelta 57 declaro.

Uso:
  python scripts/loop/vuelta58_relectura_acto32.py --raiz ../_v58_prefusion
  python scripts/loop/vuelta58_relectura_acto32.py --raiz .   (estado de hoy)
"""

import argparse
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAMPOS = ("nodos_previos", "nodos_siguientes")

# Los dos actos: el que se relee y el precedente con el que se contrasta.
ACTOS = [
    (32, ["programa_de_referidos_de_franquiciados",
          "referidos_franquiciados_existentes"]),
    (11, ["disruptores_endocrinos_y_salud_industrial",
          "quimicos_toxicos_en_diseno"]),
]


def protegidos(raiz):
    sem = set(json.load(io.open(os.path.join(raiz, "dataset", "metadata",
                                             "entry_seeds.json"),
                                encoding="utf-8")).get("seeds", []))
    packs = os.path.join(raiz, "packs")
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "entry_seeds.json")
        if os.path.exists(q):
            sem.update(json.load(io.open(q, encoding="utf-8")))
    pue = set()
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
        if not os.path.exists(q):
            continue
        for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
            for extremo in ("core", "dominio"):
                if x.get(extremo):
                    pue.add(x[extremo])
    return sem | pue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", required=True,
                    help="raiz del arbol a medir (worktree pre fusion, o . para hoy)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    raiz = os.path.abspath(a.raiz)
    nodos = os.path.join(raiz, "dataset", "nodos")
    grafo = os.path.join(raiz, "dataset", "metadata", "master_graph.json")

    G = json.load(io.open(grafo, encoding="utf-8"))["nodos"]
    ALIAS = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    prot = protegidos(raiz)

    print("=" * 78)
    print("RELECTURA CONJUNTA DEL ACTO 32, MEDIDA CONTRA EL GRAFO")
    print("=" * 78)
    print("  raiz medida : %s" % raiz)
    print("  nodos en el grafo: %d (deprecados %d)"
          % (len(G), sum(1 for v in G.values() if v.get("deprecado"))))
    print()

    for orden, miembros in ACTOS:
        mi = sorted(miembros)
        print("-" * 78)
        print("ACTO %d: %s | %s" % (orden, mi[0], mi[1]))
        print("-" * 78)
        d = []
        vivo_todos = True
        for x in mi:
            ruta = os.path.join(nodos, x + ".json")
            if not os.path.exists(ruta):
                print("  ROJO: no existe el fichero de nodo %s" % x)
                return 1
            o = json.load(io.open(ruta, encoding="utf-8"))
            g = G.get(x) or {}
            dep = bool(g.get("deprecado"))
            if dep:
                vivo_todos = False
            d.append({
                "id": x,
                "pasos": len(o.get("pasos_accionables") or []),
                "cond": len(o.get("condiciones_activacion") or []),
                "cab": len({res(y) for c in CAMPOS for y in (o.get(c) or [])} - {res(x)}),
                "deprecado": dep,
                "resuelve_a": res(x),
                "alias": list(g.get("ids_alias") or []),
            })

        def flecha(k):
            if d[0][k] > d[1][k]:
                return 1
            if d[1][k] > d[0][k]:
                return 2
            return 0

        fp, fc, fk = flecha("pasos"), flecha("cond"), flecha("cab")
        conte = [x for x in (fp, fc) if x]
        if not conte:
            forma = "CONTENIDO EMPATA" if fk else "EMPATE SIN VARA"
        elif len(set(conte)) == 2:
            forma = "CHOCAN"
        elif len(conte) == 1:
            forma = "UNA SOLA VARA"
        else:
            forma = "TODAS DE ACUERDO"

        for x in d:
            print("  %-46s pasos %2d | cond %2d | cab %2d | %s%s%s"
                  % (x["id"], x["pasos"], x["cond"], x["cab"],
                     "DEPRECADO" if x["deprecado"] else "vivo",
                     (" resuelve a " + x["resuelve_a"]) if x["resuelve_a"] != x["id"] else "",
                     (" | PUERTA" if x["id"] in prot else "")))
        print()
        print("  varas: pasos %d contra %d (flecha %s) | condiciones %d contra %d (flecha %s)"
              % (d[0]["pasos"], d[1]["pasos"], fp or "ninguna",
                 d[0]["cond"], d[1]["cond"], fc or "ninguna"))
        print("         cableado %d contra %d (flecha %s)"
              % (d[0]["cab"], d[1]["cab"], fk or "ninguna"))
        print("  FORMA POR LA RECETA: %s" % forma)
        print("  los dos vivos en este arbol: %s" % ("SI" if vivo_todos else "NO"))
        print()

    print("=" * 78)
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
