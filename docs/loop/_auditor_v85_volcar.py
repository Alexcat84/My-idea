# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 85. Vuelca los campos crudos de las 30 madres y 30 hijos del
tramo 10 (indices 72..101 de PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl) desde
dataset/nodos/*.json. Los pares se LEEN del fichero del filtro; ninguno se
teclea. Para la relectura ciega: primero los textos, la razon escrita despues.

  python docs/loop/_auditor_v85_volcar.py 72 86 > docs/loop/_auditor_v85_volcado_a.txt
  python docs/loop/_auditor_v85_volcar.py 87 101 > docs/loop/_auditor_v85_volcado_b.txt
"""
import glob
import json
import os
import sys

F85 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl"
GRAFO = "dataset/metadata/master_graph.json"

_CACHE = {}


def cargar_fichas():
    if _CACHE:
        return _CACHE
    for ruta in glob.glob("dataset/nodos/*.json"):
        try:
            d = json.load(open(ruta, encoding="utf-8"))
        except Exception:
            continue
        for n in (d if isinstance(d, list) else [d]):
            if isinstance(n, dict) and n.get("node_id"):
                _CACHE[n["node_id"]] = n
    return _CACHE


def campo(n, *nombres):
    for k in nombres:
        if n.get(k):
            return n[k]
    return None


def ficha(idn, nodos, rol):
    n = cargar_fichas().get(idn)
    g = nodos.get(idn, {})
    print("  --- %s: %s" % (rol, idn))
    if n is None:
        print("      (SIN FICHA en dataset/nodos)")
    else:
        print("      titulo   : %s" % campo(n, "titulo_concepto", "titulo"))
        res = campo(n, "resumen_teorico", "resumen")
        if res:
            print("      resumen  : %s" % " ".join(str(res).split()))
        pasos = campo(n, "pasos_accionables", "pasos")
        if pasos:
            for i, p in enumerate(pasos, 1):
                if isinstance(p, dict):
                    p = p.get("texto") or p.get("descripcion") or json.dumps(p, ensure_ascii=False)
                print("      paso %-2d  : %s" % (i, " ".join(str(p).split())))
        ent = campo(n, "entregable_esperado", "entregable", "resultado_esperado")
        if ent:
            print("      entrega  : %s" % " ".join(str(ent).split()))
    print("      sig(%d)   : %s" % (len(g.get("nodos_siguientes") or []),
                                    ", ".join(g.get("nodos_siguientes") or []) or "(vacio)"))
    print("      prev(%d)  : %s" % (len(g.get("nodos_previos") or []),
                                    ", ".join(g.get("nodos_previos") or []) or "(vacio)"))


def main():
    desde = int(sys.argv[1])
    hasta = int(sys.argv[2])
    nodos = json.load(open(GRAFO, encoding="utf-8"))["nodos"]
    filas = [json.loads(l) for l in open(F85, encoding="utf-8") if l.strip()]
    for i in range(desde, hasta + 1):
        r = filas[i]
        print()
        print("=" * 78)
        print("UNIDAD %d | %s -> %s | paso %s | dominio %s | titulo_ratio %s | contencion %s"
              % (i, r["madre"], r["hijo"], r["paso"], r["dominio"],
                 r.get("titulo_ratio"), r.get("contencion")))
        print("TEXTO DEL PASO: %s" % " ".join(str(r.get("texto_paso")).split()))
        print("=" * 78)
        ficha(r["madre"], nodos, "MADRE")
        ficha(r["hijo"], nodos, "HIJO")


main()
