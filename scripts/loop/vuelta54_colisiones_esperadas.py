# -*- coding: utf-8 -*-
"""vuelta54_colisiones_esperadas.py . SUCESOR DECLARADO DE
scripts/loop/vuelta51_colisiones_esperadas.py, AL QUE NO REEMPLAZA NI CORRIGE.

POR QUE NACE, y se dice con la medicion que lo levanto: la guarda 2.2 del
encargo de la vuelta 54 manda correr el instrumento de la vuelta 51 sobre la
nomina re-medida del dia antes de cada lote. Corrido asi
(docs/loop/SALIDA_V54_COLISIONES_ESPERADAS.txt), el instrumento NO IMPRIME NI
UNO SOLO de los 50 actos del tramo 2. El motivo esta escrito en su propio
codigo, linea 130:

    if not cls or all(x == "A" for x in cls.values()):
        continue  # fusion pura, no pide P.12

Y ES CORRECTO PARA LO QUE AQUEL INSTRUMENTO MIDE: nacio para la guarda de
cuenta del encargo de la vuelta 51, que cuenta UNA colision por cada mixto en
CONTINUA, o sea para los actos que piden lectura P.12. LOS 50 ACTOS DEL TRAMO 2
SON TODOS DE FUSION PURA (50 de 50, medido en
docs/loop/SALIDA_V54_TRAMO2_NOMINA.txt), y por eso el filtro los salta enteros.

LA GUARDA NO SE APAGA POR ESO, Y TAMPOCO SE FALSEA EL INSTRUMENTO VIEJO: se
escribe este sucesor, que hace LA MISMA ARITMETICA sobre EL ARCHIVO ENTERO
(copia de sus funciones, no reimplementacion) y anade la rama que faltaba.

LO UNICO QUE CAMBIA, declarado:
  - LA FUSION PURA SE MIDE. Para un acto sin mixtos, cada eleccion posible de
    superviviente se simula igual y se cuentan las colisiones que fabricaria.
  - LA CUENTA ESPERADA NO ES "una por mixto", porque aqui no hay mixtos. El
    censo esperado es EL QUE ESTA SIMULACION IMPRIME, que es lo que el encargo
    2.2 pide con todas sus letras: "el censo esperado es el que la simulacion
    imprime, por PAR RESUELTO".

LO QUE NO CAMBIA: la aritmetica (copia en memoria del mapa de alias, los 3.388
veredictos re-resueltos, auto-arista no es colision, dos o mas clases sobre el
mismo par resuelto si lo es) y la separacion DENTRO / FUERA del acto.

DE SOLO LECTURA. No toca ni un nodo ni un veredicto: imprime.

Uso:
  python scripts/loop/vuelta54_colisiones_esperadas.py \
      --hoy docs/loop/RECOMPUTO_V54_APERTURA.jsonl --tramo docs/loop/TRAMO2_V54.jsonl
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


def cargar_alias():
    alias = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        if d.get("deprecado") or d.get("deprecated"):
            continue
        for x in (d.get("ids_alias") or []):
            alias[x] = d["node_id"]
    return alias


def colisiones_con(veredictos, alias, extra):
    """Colisiones de clase sobre el archivo entero con el mapa alias mas extra.

    COPIA LITERAL de la funcion del instrumento de la vuelta 51: la aritmetica
    no se toca, para que las dos corridas sean comparables al digito.
    """
    mapa = dict(alias)
    mapa.update(extra)
    grupos = {}
    for pu, cl, na, nb in veredictos:
        ra, rb = mapa.get(na, na), mapa.get(nb, nb)
        if ra == rb:
            continue  # auto-arista, colapsa
        grupos.setdefault(frozenset((ra, rb)), []).append((pu, cl, na, nb))
    fuera = []
    for k, vs in grupos.items():
        if len(set(c for _, c, _, _ in vs)) > 1:
            fuera.append((tuple(sorted(k)), sorted(vs)))
    return sorted(fuera)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hoy", required=True, help="nomina re-medida del dia")
    ap.add_argument("--tramo", required=True, help="el jsonl del tramo, con orden_tramo2")
    ap.add_argument("--actos", default=None,
                    help="ordinales del tramo separados por coma; por defecto, todos")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    alias = cargar_alias()
    crudos = [(v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"])
              for v in cargar_jsonl(VER)]

    def res(x):
        return alias.get(x, x)

    base = set(k for k, _ in colisiones_con(crudos, alias, {}))

    directas = {}
    for pu, cl, na, nb in crudos:
        directas[frozenset((res(na), res(nb)))] = cl

    tramo = cargar_jsonl(a.tramo)
    if a.actos:
        quiere = set(int(x) for x in a.actos.split(",") if x.strip())
        tramo = [t for t in tramo if t["orden_tramo2"] in quiere]

    print("=" * 78)
    print("COLISIONES DE CLASE ESPERADAS DEL TRAMO 2, SOBRE EL ARCHIVO ENTERO")
    print("nomina: %s | tramo: %s | actos: %d" % (a.hoy, a.tramo, len(tramo)))
    print("colisiones VIGENTES antes de tocar nada: %d" % len(base))
    print("=" * 78)

    resumen = []
    for act in tramo:
        miem = sorted(act["miembros"])
        cls = {}
        for u, v in itertools.combinations(miem, 2):
            k = frozenset((res(u), res(v)))
            if k in directas:
                cls[frozenset((u, v))] = directas[k]
        pura = bool(cls) and all(x == "A" for x in cls.values())

        print()
        print("--- ACTO %d del tramo 2  tam %d  %s"
              % (act["orden_tramo2"], len(miem),
                 "FUSION PURA" if pura else "MIXTO"))
        print("      miembros: %s" % ", ".join(miem))

        for S in miem:
            parteA = [m for m in miem
                      if m == S or cls.get(frozenset((m, S))) == "A"]
            absorb = [m for m in parteA if m != S]
            mixtos = [m for m in miem if m not in parteA]
            if not all(cls.get(frozenset((u, v))) == "A"
                       for u, v in itertools.combinations(parteA, 2)):
                continue  # parte A no es clique A: no viable
            nuevas = [(k, vs) for k, vs in colisiones_con(
                crudos, alias, dict((x, S) for x in absorb)) if k not in base]
            dentro = [(k, vs) for k, vs in nuevas
                      if set(k) <= set(res(m) for m in miem)]
            fuera = [(k, vs) for k, vs in nuevas
                     if not set(k) <= set(res(m) for m in miem)]
            resumen.append((act["orden_tramo2"], S, len(mixtos), len(dentro), len(fuera)))
            print("      SUPERVIVIENTE %-46s mixtos %d | colisiones DENTRO %d, FUERA %d"
                  % (S, len(mixtos), len(dentro), len(fuera)))
            for k, vs in dentro + fuera:
                etiqueta = "dentro" if (k, vs) in dentro else "FUERA DEL ACTO"
                print("          [%s] %s contra %s" % (etiqueta, k[0], k[1]))
                for pu, cl, na, nb in vs:
                    print("              puesto %-6s %s | crudo: %s + %s" % (pu, cl, na, nb))

    print()
    print("=" * 78)
    print("RESUMEN: acto del tramo 2, superviviente, mixtos, colisiones dentro y fuera")
    print("=" * 78)
    total = 0
    for i, S, nm, d, f in resumen:
        if d + f:
            total += 1
        print("  acto %-4d %-52s mixtos %d  dentro %d  fuera %d" % (i, S, nm, d, f))
    print()
    print("  combinaciones simuladas          : %d" % len(resumen))
    print("  combinaciones que FABRICAN alguna: %d" % total)
    print()
    print("  EL CENSO ESPERADO DE CADA LOTE ES LA SUMA DE LAS COLISIONES DE LAS")
    print("  ELECCIONES QUE EL PLAN SELLE, y una colision real fuera de esa")
    print("  prediccion DETIENE.")
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
