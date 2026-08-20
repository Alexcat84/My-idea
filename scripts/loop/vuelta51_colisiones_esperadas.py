# -*- coding: utf-8 -*-
"""vuelta51_colisiones_esperadas.py . CUANTAS COLISIONES DE CLASE FABRICA CADA
FUSION, CONTADAS SOBRE EL ARCHIVO ENTERO Y ANTES DE TOCAR UN SOLO NODO.

POR QUE EXISTE, y no es comodidad: el encargo de la vuelta 51 pone una guarda de
cuenta, "una colision por cada CONTINUA sobre mixto CON forma y CERO por cada
ENTRA; una colision que no calce con esa cuenta te detiene". Esa cuenta es
EXACTA para la forma del acto que la vuelta 50 ejecuto y NO es exacta en general.
Medir eso DESPUES de fundir es descubrirlo con el dataset ya movido.

CORRECCION DECLARADA SOBRE ESTE MISMO INSTRUMENTO, EL DIA QUE NACIO (20 ago
2026, vuelta 51), y es la que le da su forma actual: LA PRIMERA VERSION SOLO
MIRABA DENTRO DEL ACTO. Contaba las colisiones entre los veredictos internos del
acto y nada mas, y con esa cuenta dio el visto bueno al acto del reparto de
equity. La fusion se ejecuto y el censo del archivo entero devolvio CINCO
colisiones donde el instrumento habia prometido TRES: las dos de mas eran
veredictos del absorbido split_igual_vs_desigual contra nodos de FUERA del acto
(reparto_inicial_equity, puesto 266, y timing_equity_split, puesto 246), que al
resolver caian sobre los pares que el superviviente ya tenia leidos con esos
mismos nodos (puestos 754 y 688). El acto se revirtio con git checkout y este
instrumento se reescribio para mirar EL ARCHIVO ENTERO. La leccion, escrita
donde no se pierde: UNA FUSION NO SOLO CHOCA CONSIGO MISMA. Absorber un nodo
arrastra TODOS sus veredictos, tambien los que apuntan fuera del acto, y cada
uno puede caer sobre un par que el superviviente ya tenia leido.

LA ARITMETICA, escrita entera para poder discutirla:
  - dado un superviviente S: PARTE A = {S} mas los miembros con arista `A`
    contra S; ABSORBIDOS = PARTE A menos S; MIXTOS = el resto.
  - se construye una COPIA EN MEMORIA del mapa de alias con cada absorbido
    apuntando a S, y se re-resuelven LOS 3.388 VEREDICTOS con ella.
  - un par resuelto con los dos lados iguales es AUTO-ARISTA: colapsa, y eso no
    es colision (lo cuenta el retrato como colapso).
  - un par resuelto con DOS O MAS CLASES distintas es una COLISION DE CLASE.
  - las colisiones se separan en DENTRO DEL ACTO (las que la cuenta del encargo
    predice) y FUERA DEL ACTO (las que no predice y son el hallazgo).

DE SOLO LECTURA. No toca ni un nodo ni un veredicto: imprime.

Uso:
  python scripts/loop/vuelta51_colisiones_esperadas.py \
      --hoy docs/loop/RECOMPUTO_V51_APERTURA.jsonl --hasta 30
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
    """Colisiones de clase sobre el archivo entero con el mapa alias mas extra."""
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
    ap.add_argument("--hoy", required=True)
    ap.add_argument("--desde", type=int, default=1)
    ap.add_argument("--hasta", type=int, default=30)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    alias = cargar_alias()
    crudos = [(v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"])
              for v in cargar_jsonl(VER)]

    def res(x):
        return alias.get(x, x)

    base = set(k for k, _ in colisiones_con(crudos, alias, {}))

    # clase del par directo, por par resuelto
    directas = {}
    for pu, cl, na, nb in crudos:
        directas[frozenset((res(na), res(nb)))] = cl

    comps = [c for c in cargar_jsonl(a.hoy) if c.get("estado") == "CERRADO"]

    print("=" * 78)
    print("COLISIONES DE CLASE ESPERADAS, MEDIDAS SOBRE EL ARCHIVO ENTERO")
    print("nomina: %s" % a.hoy)
    print("colisiones VIGENTES antes de tocar nada: %d" % len(base))
    print("=" * 78)

    resumen = []
    for i, c in enumerate(comps, 1):
        if i < a.desde or i > a.hasta:
            continue
        miem = sorted(c.get("miembros") or c.get("nodos") or [])
        cls = {}
        for u, v in itertools.combinations(miem, 2):
            k = frozenset((res(u), res(v)))
            if k in directas:
                cls[frozenset((u, v))] = directas[k]
        if not cls or all(x == "A" for x in cls.values()):
            continue  # fusion pura, no pide P.12

        print()
        print("--- ACTO %d  tam %d" % (i, len(miem)))
        print("      miembros: %s" % ", ".join(miem))

        for S in miem:
            parteA = [m for m in miem
                      if m == S or cls.get(frozenset((m, S))) == "A"]
            absorb = [m for m in parteA if m != S]
            mixtos = [m for m in miem if m not in parteA]
            if not mixtos:
                continue
            if not all(cls.get(frozenset((u, v))) == "A"
                       for u, v in itertools.combinations(parteA, 2)):
                continue  # parte A no es clique A: no viable
            nuevas = [(k, vs) for k, vs in colisiones_con(
                crudos, alias, dict((x, S) for x in absorb)) if k not in base]
            dentro = [(k, vs) for k, vs in nuevas
                      if set(k) <= set(res(m) for m in miem)]
            fuera = [(k, vs) for k, vs in nuevas
                     if not set(k) <= set(res(m) for m in miem)]
            calza = len(nuevas) == len(mixtos)
            resumen.append((i, S, len(mixtos), len(dentro), len(fuera), calza))
            print("      SUPERVIVIENTE %-46s mixtos %d | colisiones DENTRO %d, FUERA %d | %s"
                  % (S, len(mixtos), len(dentro), len(fuera),
                     "CALZA con la cuenta del encargo" if calza else "NO CALZA"))
            for k, vs in dentro + fuera:
                etiqueta = "dentro" if (k, vs) in dentro else "FUERA DEL ACTO"
                print("          [%s] %s contra %s" % (etiqueta, k[0], k[1]))
                for pu, cl, na, nb in vs:
                    print("              puesto %-6s %s | crudo: %s + %s" % (pu, cl, na, nb))

    print()
    print("=" * 78)
    print("RESUMEN: acto, superviviente, mixtos, colisiones dentro y fuera")
    print("=" * 78)
    ok, no = 0, 0
    for i, S, nm, d, f, calza in resumen:
        if calza:
            ok += 1
        else:
            no += 1
        print("  acto %-4d %-50s mixtos %d  dentro %d  fuera %d  %s"
              % (i, S, nm, d, f, "CALZA" if calza else "NO CALZA"))
    print()
    print("  combinaciones que CALZAN con la cuenta del encargo: %d" % ok)
    print("  combinaciones que NO CALZAN                        : %d" % no)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
