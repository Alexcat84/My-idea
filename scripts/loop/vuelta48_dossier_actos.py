# -*- coding: utf-8 -*-
"""Vuelta 48, TAREA 2: EL DOSSIER DE LECTURA DE CADA ACTO DEL TRAMO, para
cumplir P.5 (el acto se lee ENTERO antes de fundirse) SIN adivinar nada.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo, ni una operacion, ni un
veredicto. No escribe ningun fichero: imprime.

QUE IMPRIME, por acto, en este orden:
  0. la cabecera con el numero de orden, el tamano y las clases internas.
  1. LOS VEREDICTOS DIRECTOS de todos los pares internos, con su puesto, su
     clase y su razon ENTERA. P.12 parte 2: mandan los veredictos directos.
  2. EL CONTENIDO de cada miembro, verbatim del fichero del nodo: titulo,
     fuente, etiqueta, entregable, condiciones y LOS PASOS UNO A UNO. Esto es
     lo que la regla de la pagina llama CONTENIDO, y es lo que decide quien
     sobrevive.
  3. EL CABLEADO de cada miembro (pasos, a cuantos nombra, cuantos lo nombran),
     que por P.8 SOLO habla a contenido empatado.
  4. LA FIGURA DEL ACTO: si todos los pares internos son A o si hay mixtos. Un
     acto con una D dentro NO se funde entero por transitividad: P.12 manda
     leer el nodo mixto CONTRA EL SUPERVIVIENTE y decidir ENTRA (comparte
     procedimiento) o CONTINUA (comparte la idea en lineas: enlace mas poda).

EL ORDEN ES EL ORDEN IMPRESO de la nomina re-medida al abrir el tramo, que es
la vara que el auditor adjudico (acta 47, seccion 5 punto 3).

Uso:
  python scripts/loop/vuelta48_dossier_actos.py --nomina docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl
                                                --desde 1 --hasta 50 [--compacto]
"""
import argparse
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")

# 03_FUSIONES.md declara desde el 11 ago 2026 que estos cuatro no se resuelven
# nunca en OP-U-01. La guarda se re-comprueba en cada corrida.
AJENOS = ["gates_go_kill_decision_points", "customer_discovery",
          "ab_testing_optimizacion", "brainstorming_divergente"]


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", required=True)
    ap.add_argument("--desde", type=int, default=1)
    ap.add_argument("--hasta", type=int, default=50)
    ap.add_argument("--compacto", action="store_true",
                    help="razones recortadas a 400 caracteres")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    V = cargar(VER)
    idx = {}
    for r in V:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra != rb:
            idx[frozenset((ra, rb))] = r

    entra = {}
    for k, v in G.items():
        if v.get("deprecado"):
            continue
        for c in CAMPOS:
            for y in (v.get(c) or []):
                entra.setdefault(res(y), set()).add(k)

    R = cargar(a.nomina)
    C = [r for r in R if r["estado"] == "CERRADO"]

    print("=" * 78)
    print("DOSSIER DE LECTURA, actos %d a %d del lote CERRADO de OP-U-01"
          % (a.desde, a.hasta))
    print("nomina: %s (%d actos CERRADOS)" % (a.nomina, len(C)))
    print("=" * 78)
    print()
    print("GUARDA DE LOS CUATRO AJENOS (03_FUSIONES.md, 11 ago 2026):")
    sucio = []
    for x in AJENOS:
        dentro = [i + 1 for i, r in enumerate(C) if x in r["miembros"]]
        if dentro:
            sucio.append(x)
        print("   %-38s en el lote CERRADO: %s"
              % (x, "SI, actos %s" % dentro if dentro else "NO"))
    print("   GUARDA: %s" % ("ROJO" if sucio else "VERDE, ninguno de los cuatro entra"))

    for n in range(a.desde, min(a.hasta, len(C)) + 1):
        act = C[n - 1]
        mi = sorted(act["miembros"])
        print()
        print("#" * 78)
        print("# ACTO %d de %d . tamano %d . clases internas %s"
              % (n, len(C), act["tamano"], act["clases_internas"]))
        print("# %s" % ", ".join(mi))
        print("#" * 78)

        print()
        print("--- 1. VEREDICTOS DIRECTOS DE LOS PARES INTERNOS (P.12: mandan estos) ---")
        clases = {}
        for p in itertools.combinations(mi, 2):
            v = idx.get(frozenset(p))
            if not v:
                print("  [SIN VEREDICTO] %s + %s" % (p[0], p[1]))
                continue
            clases[p] = v["clase"]
            raz = v["razon"]
            if a.compacto and len(raz) > 400:
                raz = raz[:400] + " [...]"
            print("  [%s] puesto %-5d %s + %s" % (v["clase"], v["puesto_intra"], p[0], p[1]))
            print("      %s" % raz)

        print()
        print("--- 2. EL CONTENIDO DE CADA MIEMBRO, verbatim del fichero ---")
        for x in mi:
            d = json.load(io.open(os.path.join(NODOS, x + ".json"), encoding="utf-8"))
            print()
            print("  ## %s" % x)
            print("     titulo    : %s" % d.get("titulo_concepto"))
            print("     fuente    : %s" % d.get("fuente"))
            print("     dominio   : %s | fase: %s" % (d.get("dominio"), d.get("fase_proyecto")))
            print("     etiqueta  : %s" % d.get("etiqueta_arbol"))
            print("     entregable: %s" % d.get("entregable_esperado"))
            print("     alias     : %s" % (d.get("ids_alias") or []))
            print("     resumen   : %d caracteres" % len(d.get("resumen_teorico") or ""))
            ps = d.get("pasos_accionables") or []
            print("     PASOS (%d):" % len(ps))
            for j, s in enumerate(ps, 1):
                print("       %d. %s" % (j, s))
            cs = d.get("condiciones_activacion") or []
            print("     CONDICIONES (%d):" % len(cs))
            for j, s in enumerate(cs, 1):
                print("       %d. %s" % (j, s))

        print()
        print("--- 3. EL CABLEADO (P.8: solo habla a contenido empatado) ---")
        print("  %-46s %6s %8s %8s" % ("nodo", "pasos", "nombra", "LO NOMBRAN"))
        for x in mi:
            d = G[x]
            sal = len(set(res(y) for c in CAMPOS for y in (d.get(c) or [])))
            ent = len(entra.get(x, set()) - {x})
            print("  %-46s %6d %8d %8d"
                  % (x, len(d.get("pasos_accionables") or []), sal, ent))
        internas = []
        for p in itertools.combinations(mi, 2):
            for c in CAMPOS:
                if p[1] in (G[p[0]].get(c) or []):
                    internas.append("%s.%s -> %s" % (p[0], c, p[1]))
                if p[0] in (G[p[1]].get(c) or []):
                    internas.append("%s.%s -> %s" % (p[1], c, p[0]))
        print("  aristas INTERNAS del acto: %s" % (internas or "ninguna"))

        print()
        print("--- 4. LA FIGURA DEL ACTO ---")
        noA = dict((p, c) for p, c in clases.items() if c != "A")
        if not noA:
            print("  TODOS los pares internos en A. La lectura decide el superviviente")
            print("  por CONTENIDO; el cableado solo desempata (P.8).")
        else:
            print("  ACTO MIXTO: %d par(es) interno(s) NO en A." % len(noA))
            for p, c in noA.items():
                print("     [%s] %s + %s" % (c, p[0], p[1]))
            print("  P.12 MANDA: el cierre transitivo CONVOCA, la lectura DECIDE. El nodo")
            print("  mixto se lee CONTRA EL SUPERVIVIENTE: si comparte PROCEDIMIENTO,")
            print("  ENTRA; si comparte LA IDEA EN LINEAS, CONTINUA (enlace mas poda del")
            print("  solape). NI transitividad automatica NI mayoria.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
