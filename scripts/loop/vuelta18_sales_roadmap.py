# -*- coding: utf-8 -*-
"""VUELTA 18, TAREA 2.A: instrumento de las cinco lecturas dirigidas del acto
`customer_validation_sales_roadmap`. SOLO LECTURA.

No decide ninguna clase: la clase la pone la lectura. Lo que mide es lo que la
lectura NO puede medir a ojo:

  1. los seis nodos con sus pasos y su cableado, impresos para leerlos
  2. los diez pares ya leidos con su clase, del archivo
  3. el grafo de A del acto, ANTES y DESPUES de las cinco clases que la lectura
     de esta vuelta pone, con sus componentes conexas (banco 9.24)
  4. que pasa con las componentes si se quita un nodo: prueba de NODO PUENTE
  5. que operaciones de las 71 nombran estos seis nodos
  6. los hijos con casa propia que los pasos de hoja_de_ruta_de_ventas nombran,
     para poder aplicar 9.6.1 (la mayoria manda) en vez de suponerla
"""
import json
import itertools
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"
VER = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
OPS = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"

SEIS = [
    "customer_validation_sales_roadmap",
    "estrategia_de_ventas",
    "sales_roadmap",
    "hoja_de_ruta_de_ventas",
    "refinar_sales_roadmap",
    "sales_roadmap_vs_sales_force",
]

# las cinco clases que la LECTURA de esta vuelta pone. El script no las calcula:
# las recibe escritas para poder medir su consecuencia estructural.
LEIDAS_HOY = {
    ("customer_validation_sales_roadmap", "estrategia_de_ventas"): ("D", "LD-66"),
    ("customer_validation_sales_roadmap", "sales_roadmap"): ("D", "LD-67"),
    ("estrategia_de_ventas", "hoja_de_ruta_de_ventas"): ("A", "LD-68"),
    ("estrategia_de_ventas", "refinar_sales_roadmap"): ("D", "LD-69"),
    ("estrategia_de_ventas", "sales_roadmap_vs_sales_force"): ("D", "LD-70"),
}


def jsonl(ruta):
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                yield json.loads(linea)


def clave(a, b):
    return tuple(sorted((a, b)))


def componentes(nodos, aristas):
    padre = {n: n for n in nodos}

    def raiz(x):
        while padre[x] != x:
            padre[x] = padre[padre[x]]
            x = padre[x]
        return x

    for a, b in aristas:
        if a in padre and b in padre:
            ra, rb = raiz(a), raiz(b)
            if ra != rb:
                padre[ra] = rb
    grupos = {}
    for n in nodos:
        grupos.setdefault(raiz(n), []).append(n)
    return sorted([sorted(v) for v in grupos.values()], key=lambda x: (-len(x), x[0]))


def main():
    grafo = json.load(open(GRAFO, encoding="utf-8"))
    nodos = grafo["nodos"]

    print("=" * 90)
    print("1. LOS SEIS NODOS DEL ACTO, con sus pasos y su cableado")
    print("=" * 90)
    for nid in SEIS:
        d = nodos.get(nid)
        if d is None:
            print("NO ESTA EN EL GRAFO:", nid)
            continue
        print("-" * 90)
        print(nid, "| dominio:", d.get("dominio"))
        print("  fuente     :", d.get("fuente"))
        print("  previos    :", d.get("nodos_previos"))
        print("  siguientes :", d.get("nodos_siguientes"))
        for i, p in enumerate(d.get("pasos_accionables") or [], 1):
            print("   %d. %s" % (i, p))

    print()
    print("=" * 90)
    print("2. LOS PARES DEL ACTO EN EL ARCHIVO DE VEREDICTOS")
    print("=" * 90)
    S = set(SEIS)
    ya = {}
    for v in jsonl(VER):
        if v["nodo_a"] in S and v["nodo_b"] in S:
            ya[clave(v["nodo_a"], v["nodo_b"])] = (v["clase"], v["puesto_intra"])
    posibles = [clave(a, b) for a, b in itertools.combinations(sorted(SEIS), 2)]
    print("pares posibles entre seis nodos:", len(posibles))
    print("pares CON veredicto en el archivo:", len(ya))
    print("pares SIN veredicto en el archivo:", len(posibles) - len(ya))
    for p in posibles:
        if p in ya:
            print("   %-6s puesto %-5s %s  vs  %s" % (ya[p][0], ya[p][1], p[0], p[1]))
    print("  LOS QUE FALTAN EN EL ARCHIVO (son los cinco de las dirigidas):")
    faltan = [p for p in posibles if p not in ya]
    for p in faltan:
        marca = LEIDAS_HOY.get(p) or LEIDAS_HOY.get((p[1], p[0]))
        print("   %-6s %-6s %s  vs  %s" % (
            marca[0] if marca else "?", marca[1] if marca else "", p[0], p[1]))

    print()
    print("=" * 90)
    print("3. EL GRAFO DE A DEL ACTO, antes y despues de las cinco dirigidas")
    print("=" * 90)
    a_antes = [p for p, (c, _) in ya.items() if c == "A"]
    hoy = {}
    for (a, b), (c, ld) in LEIDAS_HOY.items():
        hoy[clave(a, b)] = (c, ld)
    a_hoy = [p for p, (c, _) in hoy.items() if c == "A"]
    print("A del archivo        :", len(a_antes))
    for p in sorted(a_antes):
        print("     ", p[0], "--", p[1])
    print("A de las dirigidas   :", len(a_hoy))
    for p in sorted(a_hoy):
        print("     ", p[0], "--", p[1], hoy[p][1])
    todas = a_antes + a_hoy
    print()
    print("COMPONENTES SOLO CON LAS A DEL ARCHIVO:")
    for c in componentes(SEIS, a_antes):
        print("   %d miembros: %s" % (len(c), ", ".join(c)))
    print("COMPONENTES CON LAS A DEL ARCHIVO MAS LAS DE HOY:")
    for c in componentes(SEIS, todas):
        print("   %d miembros: %s" % (len(c), ", ".join(c)))

    print()
    print("=" * 90)
    print("4. PRUEBA DE NODO PUENTE: se quita un nodo y se cuentan las componentes")
    print("=" * 90)
    for fuera in SEIS:
        resto = [n for n in SEIS if n != fuera]
        ar = [p for p in todas if fuera not in p]
        comps = componentes(resto, ar)
        sueltos = [c[0] for c in comps if len(c) == 1]
        print("  sin %-38s -> %d componentes %s%s" % (
            fuera, len(comps), [len(c) for c in comps],
            "  SUELTOS: " + ", ".join(sueltos) if sueltos else ""))
    print()
    print("  PRUEBA DE CORTE POR ARISTA: se quita una A y se cuentan las componentes")
    for p in sorted(todas):
        ar = [q for q in todas if q != p]
        comps = componentes(SEIS, ar)
        print("    sin la A %-34s -- %-34s -> %d componentes %s" % (
            p[0], p[1], len(comps), [len(c) for c in comps]))
    print()
    print("  grado de A de cada nodo (con las cinco de hoy dentro):")
    for n in SEIS:
        g = [p for p in todas if n in p]
        print("    %-40s %d   %s" % (
            n, len(g), ", ".join(x for p in g for x in p if x != n)))

    print()
    print("=" * 90)
    print("5. QUE OPERACIONES DE LAS 71 NOMBRAN A ESTOS SEIS NODOS")
    print("=" * 90)
    encontradas = 0
    for o in jsonl(OPS):
        texto = json.dumps(o, ensure_ascii=False)
        toca = [n for n in SEIS if n in texto]
        if toca:
            encontradas += 1
            print("  %-22s %-20s %s" % (o["id_op"], o["fase"], ", ".join(toca)))
    print("  operaciones que los nombran:", encontradas, "de 71")

    print()
    print("=" * 90)
    print("6. LOS HIJOS CON CASA PROPIA QUE NOMBRAN LOS PASOS (para 9.6.1)")
    print("=" * 90)
    candidatos = {
        "hoja_de_ruta_de_ventas": [
            "mapa_de_influencia", "estrategia_de_ventas",
            "mapa_de_acceso_al_cliente", "plan_de_implementacion_de_venta",
        ],
        "refinar_sales_roadmap": [
            "mapa_de_acceso_al_cliente", "estrategia_de_ventas",
        ],
    }
    for madre, hijos in candidatos.items():
        d = nodos.get(madre) or {}
        enlazados = set((d.get("nodos_previos") or []) + (d.get("nodos_siguientes") or []))
        print("  madre:", madre)
        for h in hijos:
            print("    hijo %-36s existe en el grafo: %-5s | enlazado por la madre: %s" % (
                h, h in nodos, h in enlazados))
        n_en = sum(1 for h in hijos if h in enlazados)
        print("    ENLAZA A %d DE %d hijos con casa propia -> %s" % (
            n_en, len(hijos),
            "ESTRICTA MAYORIA, la jerarquia esta establecida"
            if n_en * 2 > len(hijos) else
            "MITAD O MENOS: la silueta ni exculpa ni acusa, manda el contenido"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
