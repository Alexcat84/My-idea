# -*- coding: utf-8 -*-
"""vuelta56_colisiones_esperadas.py . SUCESOR DECLARADO DE
scripts/loop/vuelta54_colisiones_esperadas.py, AL QUE NO REEMPLAZA NI CORRIGE.

POR QUE NACE, y se dice con la medicion que lo levanto: el encargo 2.2 de la
vuelta 56 manda medir las colisiones esperadas del TRAMO 3 ENTERO con el
instrumento de la especie del de la vuelta 54. Aquel instrumento lee el
ordinal del acto en la clave "orden_tramo2", que es la que escribe el
abridor del tramo 2. El fichero del tramo 3 escribe "orden_tramo3", y aquel
instrumento cae con KeyError sobre el. Corregirlo alli habria movido un
instrumento cuyas cifras ya cita el registro del tramo 2 en
docs/plan/03_FUSIONES.md, y esa es exactamente la figura que la vara del acta
54, pregunta 3, manda resolver con SUCESOR DECLARADO Y ARITMETICA COPIADA.

LO UNICO QUE CAMBIA, y va declarado porque es lo unico que no es copia: LA
CLAVE DEL ORDINAL SE DESCUBRE DEL FICHERO en vez de estar escrita a mano. Se
busca la unica clave que empieza por "orden_tramo" en la primera fila; si hay
ninguna o mas de una, es ROJO y PARA, porque un ordinal ambiguo no es un
ordinal. Nada mas cambia: la aritmetica de las colisiones, la simulacion por
eleccion de superviviente, el reparto DENTRO y FUERA del acto y el resumen
son COPIA LITERAL del instrumento de la vuelta 54.

DE SOLO LECTURA. No toca ni un nodo ni un veredicto: imprime.

Uso:
  python scripts/loop/vuelta56_colisiones_esperadas.py       --hoy docs/loop/RECOMPUTO_V56_APERTURA.jsonl --tramo docs/loop/TRAMO3_V56.jsonl
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

    # LO UNICO QUE NO ES COPIA: la clave del ordinal se descubre del fichero.
    claves = sorted({k for k in tramo[0] if k.startswith("orden_tramo")}) if tramo else []
    if len(claves) != 1:
        print("ROJO: el fichero del tramo tiene %d claves de ordinal (%s). PARADA."
              % (len(claves), claves))
        return 1
    ORD = claves[0]
    NTRAMO = ORD.replace("orden_tramo", "")

    if a.actos:
        quiere = set(int(x) for x in a.actos.split(",") if x.strip())
        tramo = [t for t in tramo if t[ORD] in quiere]

    print("=" * 78)
    print("COLISIONES DE CLASE ESPERADAS DEL TRAMO %s, SOBRE EL ARCHIVO ENTERO" % NTRAMO)
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
        print("--- ACTO %d del tramo %s  tam %d  %s"
              % (act[ORD], NTRAMO, len(miem),
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
            resumen.append((act[ORD], S, len(mixtos), len(dentro), len(fuera)))
            print("      SUPERVIVIENTE %-46s mixtos %d | colisiones DENTRO %d, FUERA %d"
                  % (S, len(mixtos), len(dentro), len(fuera)))
            for k, vs in dentro + fuera:
                etiqueta = "dentro" if (k, vs) in dentro else "FUERA DEL ACTO"
                print("          [%s] %s contra %s" % (etiqueta, k[0], k[1]))
                for pu, cl, na, nb in vs:
                    print("              puesto %-6s %s | crudo: %s + %s" % (pu, cl, na, nb))

    print()
    print("=" * 78)
    print("RESUMEN: acto del tramo %s, superviviente, mixtos, colisiones dentro y fuera" % NTRAMO)
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
