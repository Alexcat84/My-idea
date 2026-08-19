# -*- coding: utf-8 -*-
"""vuelta38_triangulos.py - LOS DOS TRIANGULOS DE OP-D-04, MEDIDOS ANTES DE ELEGIR SUPERVIVIENTE.

ESTRICTAMENTE DE SOLO LECTURA. No escribe en el archivo, ni en un nodo, ni en el plan.

SUCESOR DECLARADO de scripts/plan/simular_fusion.py, al que NO reemplaza: aquel
simula UNA fusion ya decidida (P.7) y este mide lo que hace falta ANTES para
decidirla (P.8). LO QUE ANADE, y va dicho porque es la razon de que exista
(regla 2 del EJECUTOR):

  1. LOS GRADOS LIMPIOS, sin alias de fusion inyectado. simular_fusion.py
     computa los grados DESPUES de haber metido en ALIAS todas las fusiones que
     se le pasan en la misma corrida, asi que sus cifras sirven para la fusion
     que simula y NO para comparar candidatos entre si. Aqui se miden los ocho
     nodos del acto contra el grafo tal como esta hoy.
  2. LA RECIPROCIDAD ARISTA POR ARISTA. El ejecutor de fusiones de la casa
     (scripts/loop/vuelta33_fundir.py) DEPRECA al absorbido y redirige solo lo
     que lo NOMBRA desde fuera: las aristas que el absorbido declara en su
     propio fichero y que el otro extremo NO devuelve se quedan dentro de un
     nodo deprecado, o sea SE PIERDEN. Esa perdida no se ve en la tabla de
     perdidas de contenido y solo aparece midiendo la reciprocidad.
  3. EL CONTRAFACTUAL DE P.8: por cada triangulo, los TRES candidatos a
     superviviente con su grado y con las aristas que su eleccion perderia.

Uso: python scripts/loop/vuelta38_triangulos.py
"""
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
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

TALLER = ["brainstorming_divergente", "brainstorming_efectivo", "reglas_brainstorming"]
ALTERNANCIA = ["generar_multiples_opciones", "pensamiento_convergente_divergente",
               "design_attitude_vs_decision_attitude"]
COLGADO = "construir_sobre_ideas_ajenas"
CUARTO = "brainstorming"
ACTO = TALLER + ALTERNANCIA + [COLGADO]


def bloque(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    with io.open(GRAFO, encoding="utf-8") as fh:
        G = json.load(fh)["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    bloque("1. GRADOS LIMPIOS DE LOS OCHO, contra el grafo de hoy y resueltos (P.1)")
    print("  nodos en el grafo: %d   alias indexados: %d" % (len(G), len(ALIAS)))
    print("")
    print("  %-38s %6s %8s %10s" % ("nodo", "pasos", "nombra", "LO NOMBRAN"))
    grados = {}
    for nid in ACTO + [CUARTO]:
        sal = len(set(res(y) for c in CAMPOS for y in (G[nid].get(c) or [])))
        ent = sum(1 for kk, vv in G.items() if not vv.get("deprecado")
                  for c in CAMPOS if nid in (vv.get(c) or []))
        grados[nid] = (sal, ent)
        print("  %-38s %6d %8d %10d"
              % (nid, len(G[nid].get("pasos_accionables") or []), sal, ent))

    bloque("2. RECIPROCIDAD ARISTA POR ARISTA de los seis que se funden")
    print("  Una arista es RECIPROCA si el otro extremo la declara en el campo opuesto.")
    print("  Las NO reciprocas de un nodo que muere se pierden: viven solo en su fichero,")
    print("  y el ejecutor de fusiones lo depreca en vez de vaciarlo.")
    no_reciprocas = {}
    for nid in TALLER + ALTERNANCIA:
        print("")
        print("  --- %s" % nid)
        perdidas = []
        for c in CAMPOS:
            for y in (G[nid].get(c) or []):
                dest = res(y)
                if dest not in G:
                    print("     %-17s %-42s DESTINO NO EXISTE" % (c, y))
                    continue
                vuelta = nid in (G[dest].get(OPUESTO[c]) or [])
                marca = "reciproca" if vuelta else "NO RECIPROCA, se perderia"
                if not vuelta:
                    perdidas.append((c, dest))
                print("     %-17s %-42s %s" % (c, dest, marca))
        no_reciprocas[nid] = perdidas
        print("     no reciprocas: %d" % len(perdidas))

    bloque("3. LOS PARES INTERNOS DE CADA TRIANGULO, con su clase de hoy")
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v
    for nombre, tri in (("EL TALLER", TALLER), ("LA ALTERNANCIA", ALTERNANCIA)):
        print("")
        print("  --- %s" % nombre)
        for a, b in itertools.combinations(tri, 2):
            v = por_par.get((a, b))
            if v is None:
                print("     %-38s %-38s SIN VEREDICTO EN EL ARCHIVO" % (a, b))
            else:
                print("     %-38s %-38s %s  puesto %s"
                      % (a, b, v["clase"], v["puesto_intra"]))

    bloque("4. EL CONTRAFACTUAL DE P.8: los tres candidatos de cada triangulo")
    print("  El cableado NO decide (P.8): decide el contenido. Esta tabla existe para")
    print("  que el desempate quede MEDIDO y para saber que cuesta ir contra el.")
    for nombre, tri in (("EL TALLER", TALLER), ("LA ALTERNANCIA", ALTERNANCIA)):
        print("")
        print("  --- %s" % nombre)
        print("     %-38s %6s %10s %12s" % ("candidato", "pasos", "LO NOMBRAN", "aristas que"))
        print("     %-38s %6s %10s %12s" % ("", "", "", "se perderian"))
        for cand in tri:
            mueren = [x for x in tri if x != cand]
            perd = sum(len(no_reciprocas[m]) for m in mueren)
            print("     %-38s %6d %10d %12d"
                  % (cand, len(G[cand].get("pasos_accionables") or []),
                     grados[cand][1], perd))
        for cand in tri:
            mueren = [x for x in tri if x != cand]
            detalle = [(m, c, d) for m in mueren for c, d in no_reciprocas[m]]
            if detalle:
                print("       si sobrevive %s se pierden:" % cand)
                for m, c, d in detalle:
                    print("          %s.%s -> %s" % (m, c, d))

    bloque("5. EL CUARTO MIEMBRO Y EL COLGADO, que NO se funden")
    for nid in (CUARTO, COLGADO):
        print("  %-38s pasos %d   nombra %d   LO NOMBRAN %d"
              % (nid, len(G[nid].get("pasos_accionables") or []),
                 grados[nid][0], grados[nid][1]))
        for c in CAMPOS:
            print("     %-17s %s" % (c, json.dumps(G[nid].get(c) or [], ensure_ascii=False)))

    bloque("VEREDICTO DE LA MEDICION")
    print("los ocho grados medidos limpios; la reciprocidad contada arista por arista;")
    print("el contrafactual de P.8 impreso para los seis candidatos. NADA SE ESCRIBIO.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
