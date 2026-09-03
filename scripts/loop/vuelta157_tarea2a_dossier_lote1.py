# -*- coding: utf-8 -*-
"""vuelta157_tarea2a_dossier_lote1.py . TAREA 2.a DE LA VUELTA 157, EL DOSSIER.

IMPRIME LOS DOS NODOS DE CADA UNA DE LAS 66 LECTURAS DEL LOTE 1, para que la
pregunta estrecha y binaria de la adjudicacion 6.4 se pueda contestar CONTRA LOS
NODOS y no contra la razon escrita:

    SE PUEDEN NOMBRAR DOS LINEAS DISTINTAS, UNA EN CADA NODO, Y DECIR QUE
    PROCEDIMIENTO DEL OTRO NODO EXPANDE CADA UNA?

QUE IMPRIME DE CADA NODO, y nada mas: titulo, fuente, entregable esperado y
pasos accionables. Es lo mismo que necesita la vara del 9.22 y lo mismo que el
auditor imprimio en su ciega.

QUE IMPRIME DEL PAR: su id, su clase de hoy y LA RAZON ORIGINAL, o sea el texto
anterior al primer corchete de adjudicacion. La razon se imprime porque la 6.4
manda mirarla ("si la razon describe que CADA NODO EXPANDE LO SUYO, eso es el
puesto 2091 y la clase es D"), pero NO decide sola: la vara son los nodos.

LA NOMINA NO SE TECLEA: se lee de `docs/loop/NOMINA_V157_LOTE1.json`, que sella
`scripts/loop/vuelta157_tarea2a_nomina_lote1.py`. Si el fichero no esta, esto no
corre.

USO:  python scripts/loop/vuelta157_tarea2a_dossier_lote1.py
      python scripts/loop/vuelta157_tarea2a_dossier_lote1.py --desde 0 --hasta 22
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V157_LOTE1.json")


def razon_original(razon):
    i = razon.find("  [")
    return razon if i < 0 else razon[:i]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", type=int, default=0)
    ap.add_argument("--hasta", type=int, default=999)
    a = ap.parse_args()

    if not os.path.exists(NOMINA):
        print("ROJO PREVIO: falta docs/loop/NOMINA_V157_LOTE1.json. Corre la 2.a primero.")
        return 1
    ids = json.load(io.open(NOMINA, encoding="utf-8"))["lote"]
    N = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    E = {}
    for x in io.open(REGISTRO, encoding="utf-8").read().splitlines():
        if x.strip():
            d = json.loads(x)
            E[d["cita"].split(",")[0].strip()] = d

    print("DOSSIER DEL LOTE 1: %d lecturas. ESTE TRAMO CUBRE [%d, %d)."
          % (len(ids), a.desde, a.hasta))
    print("")

    for i, ld in enumerate(ids):
        if not (a.desde <= i < a.hasta):
            continue
        e = E[ld]
        print("=" * 78)
        print("%s  [%d de %d]  clase de hoy: %s" % (ld, i + 1, len(ids), e["clase"]))
        print("PAR: %s <-> %s" % (e["par"][0], e["par"][1]))
        print("RAZON ORIGINAL: %s" % razon_original(e["razon"]).strip())
        print("=" * 78)
        for nid in e["par"]:
            n = N.get(nid) or {}
            print("")
            print("  --- %s ---" % nid)
            print("  TITULO   : %s" % (n.get("titulo_concepto") or "(sin titulo)"))
            print("  FUENTE   : %s" % (n.get("fuente") or "(sin fuente)"))
            print("  DOMINIO  : %s" % (n.get("dominio") or "(sin dominio)"))
            ent = n.get("entregable_esperado") or n.get("entregable") or ""
            print("  ENTREGABLE: %s" % (ent or "(sin entregable)"))
            pasos = n.get("pasos_accionables") or []
            print("  PASOS (%d):" % len(pasos))
            for j, p in enumerate(pasos, 1):
                if isinstance(p, dict):
                    p = p.get("texto") or p.get("paso") or json.dumps(p, ensure_ascii=False)
                print("    %d. %s" % (j, p))
        print("")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
