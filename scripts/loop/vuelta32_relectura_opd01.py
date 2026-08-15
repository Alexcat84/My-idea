"""Vuelta 32, OP-D-01 movimientos 3 y 4: LA RELECTURA DE LOS TRES CONGELADOS.

ESTRICTAMENTE DE SOLO LECTURA. Imprime, no decide y no escribe ningun nodo ni
ningun veredicto: la lectura la hace el ejecutor con esta salida delante y la
escribe en docs/plan/02_DESTEJIDOS.md y en la nota de la operacion.

QUE IMPRIME, por cada par congelado:
  * la clase y la razon que el ARCHIVO tiene HOY (leidas de
    docs/INTRA_DOMINIO_VEREDICTOS.jsonl en esta corrida, no de un acta), que es
    el contraste contra el que se lee;
  * los pasos de los DOS nodos tal como estan HOY, uno debajo del otro;
  * SI HAY ARISTA entre ellos, en los dos sentidos, resuelta contra el grafo. La
    arista importa porque los dos arreglos que la relectura puede proponer (el
    ENLACE MUTUO del banco 9.22 y LA ARISTA QUE FALTA del 9.6) son justamente
    aristas, y afirmar que falta una sin haberla buscado seria citar una busqueda
    negativa que nadie corrio.

Uso: python scripts/loop/vuelta32_relectura_opd01.py
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

PARES = [494, 592, 830]


def cargar(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def imprimir_nodo(d, nid):
    if d is None:
        print("    %s: AUSENTE DEL GRAFO" % nid)
        return
    print("    %s" % nid)
    print("      titulo    : %s" % d.get("titulo_concepto"))
    print("      fuente    : %s" % d.get("fuente"))
    print("      entregable: %s" % d.get("entregable_esperado"))
    for i, p in enumerate(d.get("pasos_accionables") or [], 1):
        print("      %2d. %s" % (i, p))


def main():
    ver = {}
    with open(VER, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                v = json.loads(linea)
                ver[v["puesto_intra"]] = v

    print("=" * 78)
    print("RELECTURA DE LOS CONGELADOS DE OP-D-01, con el texto de HOY delante")
    print("=" * 78)
    for p in PARES:
        v = ver.get(p)
        print()
        print("-" * 78)
        if v is None:
            print("PUESTO %d: NO ESTA EN EL ARCHIVO" % p)
            continue
        a, b = v["nodo_a"], v["nodo_b"]
        print("PUESTO %d: %s contra %s" % (p, a, b))
        print("  CLASE EN EL ARCHIVO HOY: %s   clave %.4f" % (v["clase"], v["clave"]))
        print("  RAZON EN EL ARCHIVO HOY (contraste, no fuente de la clase nueva):")
        print("    %s" % v["razon"])
        print()
        da, db = cargar(a), cargar(b)
        print("  LOS DOS NODOS, HOY:")
        imprimir_nodo(da, a)
        print()
        imprimir_nodo(db, b)
        print()
        if da is not None and db is not None:
            ida = set((da.get("nodos_previos") or []) + (da.get("nodos_siguientes") or []))
            idb = set((db.get("nodos_previos") or []) + (db.get("nodos_siguientes") or []))
            print("  ARISTA, buscada en los dos sentidos contra el grafo de hoy:")
            print("    %s nombra a %s: %s" % (a, b, b in ida))
            print("    %s nombra a %s: %s" % (b, a, a in idb))
            print("    HAY ARISTA: %s" % ((b in ida) or (a in idb)))
    print()
    print("=" * 78)
    print("FIN. La clase nueva se escribe fuera de este script, con su razon.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
