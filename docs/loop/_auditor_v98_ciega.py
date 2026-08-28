# -*- coding: utf-8 -*-
"""_auditor_v98_ciega.py . INSTRUMENTO PROPIO DEL AUDITOR DE LA VUELTA 98.

Imprime el MATERIAL de los pares que se le pidan de docs/plan/DIFERENCIA_CONTRA_COLA.jsonl
(titulos, entregables y pasos_accionables ENTEROS de madre e hijo, mas el paso que el
barrido caso), SIN la clase ni la razon del ejecutor. La lectura ciega de AUDITOR.md 1.2
exige adjudicar ANTES de destapar.

    python docs/loop/_auditor_v98_ciega.py 111 114 145 147 148
"""
import io, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
BOLSA = os.path.join(RAIZ, "docs", "plan", "DIFERENCIA_CONTRA_COLA.jsonl")

nodos = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
alias = {a: k for k, v in nodos.items() for a in (v.get("ids_alias") or [])}


def res(x):
    visto = set()
    while x in alias and x not in visto:
        visto.add(x); x = alias[x]
    return x


bolsa = [json.loads(l) for l in io.open(BOLSA, encoding="utf-8") if l.strip()]


def pinta(nid, rol):
    n = nodos[nid]
    print("  %s: %s   [id %s]" % (rol, n.get("titulo_concepto"), nid))
    ent = n.get("entregable_esperado")
    print("     entregable: %s" % (ent if ent else "(ninguno)"))
    for j, p in enumerate(n.get("pasos_accionables") or [], 1):
        print("     paso %d: %s" % (j, p))


for arg in sys.argv[1:]:
    i = int(arg)
    r = bolsa[i - 1]
    m, h = res(r["madre"]), res(r["hijo"])
    print("=" * 96)
    print("PAR %d . dominio %s . titulo_ratio %.1f . contencion %s"
          % (i, r.get("dominio"), r.get("titulo_ratio"), r.get("contencion")))
    print("PASO QUE EL BARRIDO CASO (de la madre): %s" % r.get("paso"))
    print("TEXTO DEL PASO CASADO: %s" % r.get("texto_paso"))
    print("-" * 96)
    pinta(m, "MADRE segun la bolsa")
    print()
    pinta(h, "HIJO  segun la bolsa")
    print()
