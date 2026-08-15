# -*- coding: utf-8 -*-
"""vuelta34_leer_opd03.py - LOS SEIS NODOS DE OP-D-03, IMPRESOS ENTEROS.

ESTRICTAMENTE DE SOLO LECTURA. Ninguna cola sustituye a leer el nodo: este
instrumento pone el texto delante, que es lo que el encargo manda hacer ANTES de
decidir nada (P.5 y el punto 2.2 del encargo de la vuelta 34).

Imprime, por nodo: id, dominio, titulo, fuente, deprecado, pasos numerados uno a
uno, condiciones, entregable, resumen, alias, y las dos listas de aristas. Y al
final, LAS ARISTAS INTERNAS DEL ACTO buscadas en LOS DOS SENTIDOS.

Uso: python scripts/loop/vuelta34_leer_opd03.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

ACTO = ["ab_testing_optimizacion", "funnel_get_customers_optimizacion",
        "optimizacion_embudo_get_customers", "split_testing",
        "split_testing_experimentos_ab", "test_ab_precio"]

COSTURAS = ["ab_testing_optimizacion", "optimizacion_embudo_get_customers",
            "split_testing_experimentos_ab"]


def leer(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(io.open(ruta, encoding="utf-8"))


def main():
    G = {nid: leer(nid) for nid in ACTO}
    for nid in ACTO:
        d = G[nid]
        if d is None:
            print("%s: AUSENTE DEL ARBOL" % nid)
            continue
        marca = "COSTURA declarada por el plan" if nid in COSTURAS else "SANO segun el plan"
        print("=" * 78)
        print("%s   [%s]" % (nid, marca))
        print("=" * 78)
        print("  dominio    : %s" % d.get("dominio"))
        print("  titulo     : %s" % d.get("titulo_concepto"))
        print("  fuente     : %s" % d.get("fuente"))
        print("  deprecado  : %s" % bool(d.get("deprecado")))
        print("  alias      : %s" % (d.get("ids_alias") or []))
        print("  etiqueta   : %s" % d.get("etiqueta_arbol"))
        pasos = d.get("pasos_accionables") or []
        print("  PASOS (%d):" % len(pasos))
        for i, p in enumerate(pasos, 1):
            print("    %2d. %s" % (i, p))
        cond = d.get("condiciones_activacion") or []
        print("  CONDICIONES (%d):" % len(cond))
        for i, c in enumerate(cond, 1):
            print("    %2d. %s" % (i, c))
        print("  ENTREGABLE : %s" % d.get("entregable_esperado"))
        res = d.get("resumen_ejecutivo") or d.get("resumen") or ""
        print("  RESUMEN    : %s" % res)
        print("  previos    : %s" % (d.get("nodos_previos") or []))
        print("  siguientes : %s" % (d.get("nodos_siguientes") or []))
        print()

    print("=" * 78)
    print("LAS ARISTAS INTERNAS DEL ACTO, buscadas en LOS DOS SENTIDOS")
    print("=" * 78)
    hay = False
    for a in ACTO:
        da = G.get(a) or {}
        for b in ACTO:
            if a == b:
                continue
            en_sig = b in (da.get("nodos_siguientes") or [])
            en_pre = b in (da.get("nodos_previos") or [])
            if en_sig or en_pre:
                hay = True
                print("  %s nombra a %s   (siguientes=%s, previos=%s)" % (a, b, en_sig, en_pre))
    if not hay:
        print("  NINGUNA: los seis nodos del acto no se nombran entre si en ningun sentido.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
