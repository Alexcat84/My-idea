# -*- coding: utf-8 -*-
"""vuelta33_ld_opd02.py

LECTURA PURA para las TRES LECTURAS DIRIGIDAS que le faltan al acto de OP-D-02.
DE SOLO LECTURA: no decide, no clasifica y no escribe en ningun documento.

P.5 del BANCO_DEL_PLAN manda leer el acto ENTERO despues del destejido y antes de
la fusion, y la pregunta que contesta es si el acto es UNA familia o DOS. El
encargo de la vuelta 33 adjudica que los tres pares que la cola nunca trajo se
leen como LECTURAS DIRIGIDAS: misma vara del cribado, NO entran en la cola y NO
mueven n.

ESTE SCRIPT IMPRIME LOS CUATRO NODOS ENTEROS ANTES DE QUE NADIE DECIDA NADA, con
todos los campos que la vara mira: titulo, fuente, entregable, pasos y condiciones.
No imprime un resumen: imprime el texto. Esa es la mitad del punto de P.5, porque
un par leido sobre un resumen es un par leido sobre otra cosa.

Imprime ademas, para cada uno de los tres pares por leer:
  - la ARISTA, buscada en los DOS sentidos contra el grafo de hoy (una busqueda
    negativa no se puede citar sin haberla hecho, EJECUTOR.md regla 9)
  - si el par esta o no en la cola del cribado, contra INTRA_DOMINIO_PARES.jsonl,
    que es lo que sostiene que sea LECTURA DIRIGIDA y no un par saltado
Y los TRES pares A ya leidos del acto, con su razon entera, porque la pregunta de
P.5 se contesta sobre el acto completo y no sobre los tres nuevos sueltos.

Uso: python scripts/loop/vuelta33_ld_opd02.py
"""
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PARES = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_PARES.jsonl")


def nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def imprimir_nodo(nid):
    d = nodo(nid)
    print("-" * 78)
    if d is None:
        print("NODO %s: AUSENTE DEL GRAFO" % nid)
        return
    print("NODO: %s" % nid)
    print("  titulo    : %s" % d.get("titulo_concepto"))
    print("  fuente    : %s" % d.get("fuente"))
    print("  dominio   : %s   fase: %s   vivo: %s"
          % (d.get("dominio"), d.get("fase_proyecto"),
             not (d.get("deprecado") or d.get("deprecated"))))
    print("  entregable: %s" % d.get("entregable_esperado"))
    print("  resumen   : %s" % d.get("resumen_teorico"))
    print("  PASOS (%d):" % len(d.get("pasos_accionables") or []))
    for i, p in enumerate(d.get("pasos_accionables") or [], 1):
        print("    %2d. %s" % (i, p))
    print("  CONDICIONES (%d):" % len(d.get("condiciones_activacion") or []))
    for i, c in enumerate(d.get("condiciones_activacion") or [], 1):
        print("    %2d. %s" % (i, c))
    print("  previos   : %s" % (d.get("nodos_previos") or []))
    print("  siguientes: %s" % (d.get("nodos_siguientes") or []))


def arista(a, b):
    da, db = nodo(a), nodo(b)
    ab = b in ((da or {}).get("nodos_previos") or []) + ((da or {}).get("nodos_siguientes") or [])
    ba = a in ((db or {}).get("nodos_previos") or []) + ((db or {}).get("nodos_siguientes") or [])
    return ab, ba


def main():
    ops = {}
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                o = json.loads(linea)
                ops[o["id_op"]] = o
    nomina = ops["OP-D-02"]["nodos"]

    vs = [json.loads(l) for l in open(VER, encoding="utf-8") if l.strip()]
    por_par = {frozenset((v["nodo_a"], v["nodo_b"])): v for v in vs}
    en_cola = set()
    with open(PARES, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                p = json.loads(linea)
                en_cola.add(frozenset((p["nodo_a"], p["nodo_b"])))

    print("=" * 78)
    print("LECTURA DIRIGIDA DEL ACTO DE OP-D-02 (P.5). LOS CUATRO NODOS, ENTEROS")
    print("=" * 78)
    print("NOMINA, leida hoy de OPERACIONES.jsonl: %d nodos" % len(nomina))
    print()
    for nid in sorted(nomina):
        imprimir_nodo(nid)
    print()

    print("=" * 78)
    print("LOS TRES PARES A YA LEIDOS DEL ACTO, con su razon entera")
    print("=" * 78)
    for a, b in itertools.combinations(sorted(nomina), 2):
        v = por_par.get(frozenset((a, b)))
        if v is None or v["clase"] != "A":
            continue
        print()
        print("PUESTO %d, clase %s, clave %s: %s contra %s"
              % (v["puesto_intra"], v["clase"], v["clave"], v["nodo_a"], v["nodo_b"]))
        for i in range(0, len(v["razon"]), 96):
            print("    %s" % v["razon"][i:i + 96])
    print()

    print("=" * 78)
    print("LOS TRES PARES POR LEER, con su arista y su prueba de que no estan en la cola")
    print("=" * 78)
    for a, b in itertools.combinations(sorted(nomina), 2):
        if por_par.get(frozenset((a, b))) is not None:
            continue
        ab, ba = arista(a, b)
        print()
        print("PAR: %s contra %s" % (a, b))
        print("  veredicto en el archivo        : NINGUNO")
        print("  esta en la cola del cribado    : %s"
              % ("SI" if frozenset((a, b)) in en_cola else "NO, o sea LECTURA DIRIGIDA legitima"))
        print("  %s nombra a %s: %s" % (a, b, ab))
        print("  %s nombra a %s: %s" % (b, a, ba))
        print("  HAY ARISTA: %s" % (ab or ba))
    print()
    print("=" * 78)
    print("FIN DE LA LECTURA. Nada se clasifico y nada se escribio.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
