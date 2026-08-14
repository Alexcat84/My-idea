# -*- coding: utf-8 -*-
"""VUELTA 18, TAREA 2.B: instrumento de los ejemplares de las figuras. SOLO LECTURA.

QUE HACE, y en este orden:

  1. VERIFICA los ejemplares que la lectura localizo, uno por uno, contra
     docs/INTRA_DOMINIO_VEREDICTOS.jsonl: que el puesto existe, con que clase y
     entre que dos nodos. Un ejemplar que no verifique NO se nombra.
  2. MIDE la forma mecanica de tres figuras que se pueden contar sin leer
     (TRIANGULO ABIERTO, ESTRELLA, EL PASO DE OFICIO), para poder DECLARAR la
     diferencia entre "ejemplar declarado" y "par que calza con la forma".
  3. ACOTA EL PASO DE OFICIO: cuantos nodos de `exportacion` abren con la linea
     generica y cuales son.

EL CRITERIO DE EJEMPLAR, escrito para que se pueda discutir: un ejemplar de una
figura de lectura es una instancia DECLARADA POR ESCRITO (en el informe, en el
banco, en un expediente o en una lectura dirigida), no cualquier par que calce
con la forma. La medicion del punto 2 esta para probar que la diferencia entre
las dos definiciones es enorme, no anecdotica.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
VER = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"

# ---------------------------------------------------------------- los candidatos
# cada uno: (figura, puesto, la pareja de nodos esperada o None, clase esperada)
CANDIDATOS = [
    ("EL ESQUELETO COMPARTIDO", 2001, ("customs_bonded_warehouses", "foreign_trade_zones"), "D"),
    ("EL ESQUELETO COMPARTIDO", 2011, ("financiamiento_sba_exportacion", "programas_ex_im_bank"), "D"),
    ("LAS DOS ADUANAS", 2008, None, None),
    ("LAS DOS ADUANAS", 2013, None, None),
    ("LAS DOS ADUANAS", 2037, None, None),
    ("LAS DOS ADUANAS", 2054, None, None),
    ("LAS DOS ADUANAS", 2070, None, None),
    ("LA BIFURCACION", 2030, None, None),
    ("LA BIFURCACION", 2050, None, None),
    ("LOS DOS PARES QUE NO SE CRUZAN", 1942, None, "A"),
    ("LOS DOS PARES QUE NO SE CRUZAN", 1969, None, "A"),
    ("LOS DOS PARES QUE NO SE CRUZAN", 2034, None, "D"),
    ("LOS DOS PARES QUE NO SE CRUZAN", 2059, None, "D"),
    ("LA VARA EN LOS DOS SENTIDOS, polo 1", 1077, None, "C"),
    ("LA VARA EN LOS DOS SENTIDOS, polo 1", 1240, None, "C"),
    ("LA VARA EN LOS DOS SENTIDOS, polo 2", 2080, None, "A"),
    ("LA VARA EN LOS DOS SENTIDOS, polo 2", 2105, None, "A"),
    ("LA VARA, el contraste que fija el limite", 2091, None, "D"),
    ("TRIANGULO ABIERTO 1", 1558, None, "D"),
    ("TRIANGULO ABIERTO 2", 377, None, "D"),
    ("TRIANGULO ABIERTO 2", 854, None, "D"),
    ("TRIANGULO ABIERTO 2", 855, None, "D"),
]

# las estrellas declaradas, cada una con su centro y sus pares
ESTRELLAS = [
    ("pass/fail", "diseno_experimentos_pass_fail", [467, 511, 639], [636, 1346]),
    ("scorecard", "scoring_model_scorecard", [184, 820], [1201]),
    ("los regalos", "regalos_estrategicos_sorpresa", [251, 799], [1348]),
    ("la fase de diseno", "fase_diseno_prototipado_modelos", [507, 641], [572]),
    ("el peso dimensional", "calcular_peso_dimensional_antes_cotizar", [1601, 1602], [1609]),
    ("investigacion de mercados", "enfoque_paso_a_paso_investigacion_mercado", [1966, 1967], [1972]),
    ("el abogado, INVERTIDA", "contratar_abogado_especializado_franquicias", [2076, 2090], [2086]),
    ("los costos de franquicia", "cinco_categorias_costos_franquicia", [2074, 2075], [2092]),
]

TRIO_MERCADOS = ["mercados_multilaterales", "multi_sided_market_channel",
                 "optimizacion_mercado_multilado"]
TRIO_ALTURAS = ["customer_validation", "customer_development_process",
                "customer_development_modelo"]

# la linea generica de EL PASO DE OFICIO, en las formas en que aparece
PISTAS_OFICIO = [
    "oficina de comercio exterior", "comercio exterior", "us commercial service",
    "servicio comercial", "district export council", "distrito de exportacion",
    "consulta con la oficina", "oficina que lo administra",
]


def cargar():
    filas = []
    with open(VER, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def main():
    V = cargar()
    por_puesto = {v["puesto_intra"]: v for v in V}
    par = {}
    A = collections.defaultdict(set)
    ady = collections.defaultdict(set)
    for v in V:
        k = tuple(sorted((v["nodo_a"], v["nodo_b"])))
        par[k] = (v["clase"], v["puesto_intra"])
        ady[v["nodo_a"]].add(v["nodo_b"])
        ady[v["nodo_b"]].add(v["nodo_a"])
        if v["clase"] == "A":
            A[v["nodo_a"]].add(v["nodo_b"])
            A[v["nodo_b"]].add(v["nodo_a"])

    print("=" * 96)
    print("1. VERIFICACION DE LOS EJEMPLARES LOCALIZADOS POR LECTURA")
    print("=" * 96)
    fallos = 0
    for fig, p, nodos, clase in CANDIDATOS:
        v = por_puesto.get(p)
        if v is None:
            print("  FALLA  %-40s puesto %-5d NO EXISTE" % (fig, p))
            fallos += 1
            continue
        ok = True
        if clase and v["clase"] != clase:
            ok = False
        if nodos and set(nodos) != {v["nodo_a"], v["nodo_b"]}:
            ok = False
        print("  %-6s %-40s puesto %-5d %s  %s vs %s" % (
            "OK" if ok else "FALLA", fig, p, v["clase"], v["nodo_a"], v["nodo_b"]))
        if not ok:
            fallos += 1
    print("  ejemplares verificados: %d, fallos: %d" % (len(CANDIDATOS), fallos))

    print()
    print("=" * 96)
    print("2. LAS ESTRELLAS DECLARADAS, con sus dos cuentas del banco 9.23")
    print("=" * 96)
    for nombre, centro, radios, perif in ESTRELLAS:
        lineas = []
        bien = True
        for p in radios:
            v = por_puesto.get(p)
            if v is None or v["clase"] != "A" or centro not in (v["nodo_a"], v["nodo_b"]):
                bien = False
                lineas.append("radio %d MAL" % p)
            else:
                otro = v["nodo_b"] if v["nodo_a"] == centro else v["nodo_a"]
                lineas.append("%d A %s" % (p, otro))
        for p in perif:
            v = por_puesto.get(p)
            if v is None or v["clase"] == "A" or centro in (v["nodo_a"], v["nodo_b"]):
                bien = False
                lineas.append("periferico %d MAL" % p)
            else:
                lineas.append("%d %s periferico" % (p, v["clase"]))
        print("  %-6s %-28s centro %-46s %s" % (
            "OK" if bien else "FALLA", nombre, centro, " | ".join(lineas)))

    print()
    print("  LA MISMA FORMA, CONTADA A MAQUINA sobre las 3.388 lineas:")
    mec = []
    for c, per in A.items():
        if len(per) < 2:
            continue
        per = sorted(per)
        leidos = [(a, b) for a, b in itertools.combinations(per, 2)
                  if tuple(sorted((a, b))) in par]
        if leidos and all(par[tuple(sorted(p))][0] != "A" for p in leidos):
            mec.append(c)
    print("    centros que calzan con las DOS cuentas de 9.23 al corte 3.388: %d" % len(mec))
    print("    ejemplares DECLARADOS por escrito: %d" % len(ESTRELLAS))

    print()
    print("=" * 96)
    print("3. LOS DOS TRIANGULOS ABIERTOS, y la forma contada a maquina")
    print("=" * 96)
    for nombre, trio in (("mercados de varios lados", TRIO_MERCADOS),
                         ("el proceso a tres alturas", TRIO_ALTURAS)):
        print("  %s:" % nombre)
        todos = True
        for a, b in itertools.combinations(sorted(trio), 2):
            k = tuple(sorted((a, b)))
            if k not in par:
                print("     SIN LEER  %s vs %s" % (a, b))
                todos = False
                continue
            cl, p = par[k]
            if cl != "D":
                todos = False
            print("     puesto %-5d %s  %s vs %s" % (p, cl, a, b))
        print("     los tres pares leidos y los tres en D: %s" % todos)

    n_tri = 0
    for n in sorted(ady):
        vec = sorted(x for x in ady[n] if x > n)
        for a, b in itertools.combinations(vec, 2):
            if tuple(sorted((a, b))) in par:
                t = (n, a, b)
                if all(par[tuple(sorted(x))][0] == "D"
                       for x in itertools.combinations(t, 2)):
                    n_tri += 1
    print("  LA MISMA FORMA A MAQUINA: trios con sus tres pares leidos y los tres en D,")
    print("    al corte 3.388: %d. Ejemplares DECLARADOS por escrito: 2" % n_tri)

    print()
    print("=" * 96)
    print("4. EL PASO DE OFICIO, ACOTADO: cuantos son y donde estan")
    print("=" * 96)
    grafo = json.load(open(GRAFO, encoding="utf-8"))
    nodos = grafo["nodos"]
    exp = {k: n for k, n in nodos.items() if n.get("dominio") == "exportacion"}
    print("  nodos vivos del dominio exportacion: %d" % len(exp))
    con = {}
    for nid, n in exp.items():
        pasos = n.get("pasos_accionables") or []
        marcas = []
        for i, p in enumerate(pasos, 1):
            bajo = p.lower()
            for pista in PISTAS_OFICIO:
                if pista in bajo:
                    marcas.append((i, pista))
                    break
        if marcas:
            con[nid] = marcas
    print("  nodos con la linea generica de oficina en algun paso: %d" % len(con))
    for nid in sorted(con):
        print("     %-52s pasos %s" % (nid, [m[0] for m in con[nid]]))
    primero = {k: v for k, v in con.items() if any(m[0] == 1 for m in v)}
    print("  de esos, los que la traen en su PASO 1: %d  %s" % (
        len(primero), sorted(primero)))
    print("  el dominio tiene %d pares leidos en el archivo" % sum(
        1 for v in V if v["dominio"] == "exportacion"))
    tocados = [v for v in V if v["dominio"] == "exportacion"
               and (v["nodo_a"] in con or v["nodo_b"] in con)]
    print("  pares de exportacion donde al menos un lado trae la linea: %d" % len(tocados))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
