# -*- coding: utf-8 -*-
"""VUELTA 19: instrumento de medicion. SOLO LECTURA, no escribe nada.

Mide, en esta vuelta y desde las fuentes, TODA cifra que el reporte publique:

  1. El marcador del archivo de veredictos (clases, huecos, duplicados) y la
     tasa por dominio.
  2. LA BIFURCACION: en cuantas razones aparece la palabra, en minusculas y en
     mayusculas, con sus puestos (caida 1 del acta de la vuelta 18).
  3. EL PASO DE OFICIO: nodos del dominio exportacion en el grafo, cuantos
     estan deprecado y cuantos quedan VIVOS (caida 2 del acta de la vuelta 18),
     mas la cota de la linea generica recontada SOLO sobre los vivos.
  4. El inventario entero: entradas por tipo, actos vigentes CERRADOS y
     ABIERTOS, y la deuda total de P.5 en pares (los pares que las notas de
     acto declaran en cola mas fuera de cola).
  5. La novena estrella: los dos radios del centro tecnologias_disruptivas_
     oportunidad y el estado del par entre sus perifericos.

Cada bloque imprime su cifra con la ruta de la que sale.
"""
import collections
import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
VER = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"
INV = RAIZ / "docs" / "plan" / "INVENTARIO.jsonl"


def cargar_jsonl(ruta):
    filas = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def titulo(t):
    print()
    print("=" * 96)
    print(t)
    print("=" * 96)


def main():
    V = cargar_jsonl(VER)
    inv = cargar_jsonl(INV)
    grafo = json.load(open(GRAFO, encoding="utf-8"))
    nodos = grafo["nodos"]

    # ------------------------------------------------------------------ 1
    titulo("1. EL MARCADOR, desde docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
    clases = collections.Counter(v["clase"] for v in V)
    n = len(V)
    for c in ("A", "B", "C", "D"):
        print("  %s  %5d   %4.1f%%" % (c, clases[c], 100.0 * clases[c] / n))
    print("  n  %5d" % n)
    puestos = [v["puesto_intra"] for v in V]
    print("  puestos unicos: %d, min %d, max %d, duplicados %d, huecos %d" % (
        len(set(puestos)), min(puestos), max(puestos),
        len(puestos) - len(set(puestos)),
        len(set(range(min(puestos), max(puestos) + 1)) - set(puestos))))
    print()
    print("  tasa por dominio:")
    por_dom = collections.defaultdict(lambda: [0, 0])
    for v in V:
        por_dom[v["dominio"]][0] += 1
        if v["clase"] == "A":
            por_dom[v["dominio"]][1] += 1
    for d in sorted(por_dom):
        t, a = por_dom[d]
        print("    %-20s %5d pares  %4d A  %5.1f%%" % (d, t, a, 100.0 * a / t))

    # ------------------------------------------------------------------ 2
    titulo("2. LA BIFURCACION: la palabra en las razones del archivo")
    baja, alta = [], []
    for v in V:
        r = v.get("razon") or ""
        if "bifurcacion" in r.lower():
            baja.append(v["puesto_intra"])
        if "BIFURCACION" in r:
            alta.append(v["puesto_intra"])
    print("  razones que contienen la palabra (sin distinguir mayusculas): %d" % len(baja))
    print("    puestos: %s" % sorted(baja))
    print("  razones que la traen en MAYUSCULAS: %d  puestos %s" % (len(alta), sorted(alta)))
    for p in sorted(baja):
        v = next(x for x in V if x["puesto_intra"] == p)
        print("    %-5d %s  %s vs %s" % (p, v["clase"], v["nodo_a"], v["nodo_b"]))
        print("          %s" % v["razon"][:150])

    # ------------------------------------------------------------------ 3
    titulo("3. EL DOMINIO exportacion EN EL GRAFO: totales, deprecado y VIVOS")
    exp_todos = {k: x for k, x in nodos.items() if x.get("dominio") == "exportacion"}
    exp_dep = {k: x for k, x in exp_todos.items() if x.get("deprecado")}
    exp_vivos = {k: x for k, x in exp_todos.items() if not x.get("deprecado")}
    print("  nodos del dominio en el grafo: %d" % len(exp_todos))
    print("  de esos, deprecado: %d" % len(exp_dep))
    print("  VIVOS: %d" % len(exp_vivos))
    print("  los deprecado son: %s" % sorted(exp_dep))
    ent_dom = [e for e in inv if e.get("tipo") == "dominio"
               and e.get("nombre") == "exportacion"]
    for e in ent_dom:
        print("  lo que publica la entrada de tipo dominio del inventario:")
        print("     %s" % (e.get("nota") or "")[:220])

    PISTAS = [
        "oficina de comercio exterior", "comercio exterior", "us commercial service",
        "servicio comercial", "district export council", "distrito de exportacion",
        "consulta con la oficina", "oficina que lo administra",
    ]
    con = {}
    for nid, x in exp_vivos.items():
        marcas = []
        for i, p in enumerate(x.get("pasos_accionables") or [], 1):
            bajo = p.lower()
            if any(pi in bajo for pi in PISTAS):
                marcas.append(i)
        if marcas:
            con[nid] = marcas
    print("  cota de la linea generica RECONTADA SOLO SOBRE LOS VIVOS: %d nodos" % len(con))
    for nid in sorted(con):
        print("     %-52s pasos %s   deprecado: %s" % (
            nid, con[nid], bool(nodos[nid].get("deprecado"))))
    pares_exp = [v for v in V if v["dominio"] == "exportacion"]
    tocados = [v for v in pares_exp if v["nodo_a"] in con or v["nodo_b"] in con]
    print("  pares leidos del dominio: %d" % len(pares_exp))
    print("  pares donde al menos un lado trae la linea: %d" % len(tocados))
    for v in sorted(tocados, key=lambda x: x["puesto_intra"]):
        print("     %-5d %s  %s vs %s" % (
            v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))

    # ------------------------------------------------------------------ 4
    titulo("4. EL INVENTARIO: tipos, actos vigentes y la deuda de P.5")
    tipos = collections.Counter(e.get("tipo") for e in inv)
    print("  entradas: %d" % len(inv))
    for t, c in sorted(tipos.items()):
        print("    %-16s %d" % (t, c))
    actos = [e for e in inv if e.get("tipo") == "acto"]
    superadas = [e for e in actos if "superada" in (e.get("estado") or "").lower()]
    vigentes = [e for e in actos if e not in superadas]
    print("  actos: %d (superadas %d, vigentes %d)" % (
        len(actos), len(superadas), len(vigentes)))
    est = collections.Counter()
    for e in vigentes:
        s = (e.get("estado") or "").upper()
        if "CERRADO" in s:
            est["CERRADO"] += 1
        elif "ABIERTO" in s:
            est["ABIERTO"] += 1
        else:
            est["otro: " + s] += 1
    for k in sorted(est):
        print("    vigentes %-12s %d" % (k, est[k]))

    # la deuda de P.5: los pares que las notas de acto vigentes declaran
    # pendientes, en cola y fuera de cola, leidos del texto de la nota
    rx_cola = re.compile(r"(\d+)\s+en\s+cola", re.I)
    rx_fuera = re.compile(r"(\d+)\s+fuera\s+de\s+cola", re.I)
    deuda_cola = deuda_fuera = 0
    con_deuda = []
    for e in vigentes:
        nota = e.get("nota") or ""
        mc = rx_cola.search(nota)
        mf = rx_fuera.search(nota)
        c = int(mc.group(1)) if mc else 0
        f = int(mf.group(1)) if mf else 0
        if c or f:
            con_deuda.append((e.get("nombre"), c, f))
        deuda_cola += c
        deuda_fuera += f
    print("  DEUDA DE P.5 leida de las notas de acto vigentes:")
    print("    pares en cola:        %d" % deuda_cola)
    print("    pares fuera de cola:  %d" % deuda_fuera)
    print("    TOTAL:                %d" % (deuda_cola + deuda_fuera))
    print("    actos con deuda: %d" % len(con_deuda))

    # ------------------------------------------------------------------ 5
    titulo("5. LA NOVENA ESTRELLA: tecnologias_disruptivas_oportunidad")
    centro = "tecnologias_disruptivas_oportunidad"
    tocan = [v for v in V if centro in (v["nodo_a"], v["nodo_b"])]
    print("  pares leidos que tocan al centro: %d" % len(tocan))
    for v in sorted(tocan, key=lambda x: x["puesto_intra"]):
        otro = v["nodo_b"] if v["nodo_a"] == centro else v["nodo_a"]
        print("     %-5d %s  contra %s" % (v["puesto_intra"], v["clase"], otro))
    perif = ["evaluacion_tecnologias_disruptivas", "explotacion_tecnologias_disruptivas"]
    k = tuple(sorted(perif))
    hallado = [v for v in V
               if tuple(sorted((v["nodo_a"], v["nodo_b"]))) == k]
    print("  el par entre los dos perifericos %s: %s" % (
        k, "LEIDO puesto %d clase %s" % (hallado[0]["puesto_intra"], hallado[0]["clase"])
        if hallado else "NO ESTA EN EL ARCHIVO (nunca entro a la cola)"))
    for nid in [centro] + perif:
        x = nodos.get(nid)
        print("  nodo %-46s existe: %s  deprecado: %s  dominio: %s" % (
            nid, x is not None, bool(x.get("deprecado")) if x else "-",
            x.get("dominio") if x else "-"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
