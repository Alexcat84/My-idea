"""Estado de la campana recomputado HOY, para el reporte de la vuelta 26.

Nada sale de un acta ni de un reporte anterior: todo se mide aqui.

Uso: python scripts/loop/vuelta26_estado.py
"""
import json
import os
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def leer_jsonl(ruta):
    fuera = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                fuera.append(json.loads(linea))
    return fuera


def main():
    print("=" * 78)
    print("EL MARCADOR")
    print("=" * 78)
    v = leer_jsonl(VER)
    puestos = [x["puesto_intra"] for x in v]
    clases = Counter(x["clase"] for x in v)
    n = len(v)
    print("n = %d" % n)
    for c in ("A", "B", "C", "D"):
        print("  %s %5d  %5.1f por ciento" % (c, clases[c], 100.0 * clases[c] / n))
    fuera = sorted(set(clases) - {"A", "B", "C", "D"})
    print("clases fuera de ABCD: %s" % (fuera if fuera else 0))
    print("rango de puestos: %d a %d" % (min(puestos), max(puestos)))
    huecos = sorted(set(range(min(puestos), max(puestos) + 1)) - set(puestos))
    print("huecos: %d" % len(huecos))
    dup = [p for p, c in Counter(puestos).items() if c > 1]
    print("duplicados: %d" % len(dup))

    print()
    print("TASA DE A POR DOMINIO")
    por = {}
    for x in v:
        por.setdefault(x["dominio"], Counter())[x["clase"]] += 1
    print("%-20s %6s %6s %8s %5s %5s %6s" % ("dominio", "n", "A", "tasa", "B", "C", "D"))
    for dom, c in sorted(por.items(), key=lambda kv: -sum(kv[1].values())):
        t = sum(c.values())
        print("%-20s %6d %6d %7.1f%% %5d %5d %6d" % (
            dom, t, c["A"], 100.0 * c["A"] / t, c["B"], c["C"], c["D"]))

    print()
    print("=" * 78)
    print("EL GRAFO")
    print("=" * 78)
    nodos = {}
    for f in os.listdir(NODOS):
        if f.endswith(".json"):
            with open(os.path.join(NODOS, f), encoding="utf-8") as fh:
                d = json.load(fh)
            nodos[d["node_id"]] = d
    dep = [k for k, d in nodos.items() if d.get("deprecado")]
    enl = sum(len(d.get("nodos_previos") or []) + len(d.get("nodos_siguientes") or [])
              for d in nodos.values())
    claves = set()
    for d in nodos.values():
        claves |= set(d.keys())
    print("nodos en disco : %d" % len(nodos))
    print("vivos          : %d" % (len(nodos) - len(dep)))
    print("deprecados     : %d" % len(dep))
    print("enlaces        : %d (previos mas siguientes)" % enl)
    print("claves distintas: %d" % len(claves))

    print()
    print("=" * 78)
    print("LAS OPERACIONES")
    print("=" * 78)
    ops = leer_jsonl(OPS)
    ids = [o["id_op"] for o in ops]
    print("operaciones: %d, ids unicos: %d" % (len(ops), len(set(ids))))
    print("estados: %s" % dict(Counter(o["estado"] for o in ops)))
    print("por fase: %s" % dict(Counter(o["fase"] for o in ops)))
    rotas = []
    for o in ops:
        for d in (o.get("depende_de") or []) + (o.get("bloquea_a") or []):
            if d not in set(ids):
                rotas.append((o["id_op"], d))
    print("dependencias rotas: %d" % len(rotas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
