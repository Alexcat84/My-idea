#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""barrido_quinta_cara.py . busca candidatos a la quinta cara (senal del idioma)
en los pares YA LEIDOS del cribado intra-dominio.

SOLO LECTURA. No toca ni un nodo ni un veredicto.

Universo del barrido: los pares 1..CORTE del archivo de veredictos. Para cada par
mira el node_id y el titulo_concepto de sus DOS nodos y marca:
  - SIGLA: dos o mas mayusculas seguidas en el titulo (regex [A-Z]{2,})
  - INGLES: token del node_id o del titulo que casa la lista de marcadores en
    ingles de abajo (palabra completa, como manda 9.28: subcadena inventa nombres)

La lista de ingles es CURADA y por tanto incompleta por construccion (9.28): esto
es un BUSCADOR DE CANDIDATOS, no un censo. La separacion denominacion real / falso
positivo se hace A MANO sobre esta salida.

Uso:  python scripts/barrido_quinta_cara.py 2600
"""
import json, io, sys, re, argparse, collections

ap = argparse.ArgumentParser()
ap.add_argument("corte", type=int)
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")

G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
V = [v for v in V if v["puesto_intra"] <= a.corte]

# marcadores en ingles (palabra completa). curada, incompleta por construccion.
INGLES = sorted(set("""
box plot run chart zero defects lean voice customer benchmarking brainstorming
poka yoke kaizen gemba muda mura muri kanban jidoka andon takt heijunka
control chart flow chart flowchart scatter pareto stakeholder feedback
checklist check sheet dashboard mapping roadmap workflow scorecard mindmap
storming forming norming performing swot pdca dmaic dmaic sipoc ppap fmea
apqp msa spc voc voe coc mbo cpk ppk dpmo dfss qfd tqm jit oee wip ohsas
five whys design thinking value stream lead time cycle time first pass
right first time cost of quality quality function deployment house quality
gauge kappa gage capability sigma green belt black belt yellow champion
runchart boxplot scorecarding coaching mentoring outsourcing offshoring
just in time total quality management statistical process affinity
""".split()))
ING_RE = re.compile(r"(?<![a-z])(" + "|".join(re.escape(w) for w in INGLES) + r")(?![a-z])", re.I)
SIGLA_RE = re.compile(r"[A-Z]{2,}")


def texto(k):
    n = G.get(k) or {}
    return (n.get("titulo_concepto") or ""), (k or "")


def marca(k):
    tit, nid = texto(k)
    sig = sorted(set(SIGLA_RE.findall(tit)))
    ing = sorted(set(m.group(0).lower() for m in ING_RE.finditer(tit + " " + nid.replace("_", " "))))
    return sig, ing


universo = 0
por_dom = collections.Counter()
for v in V:
    a_sig, a_ing = marca(v["nodo_a"])
    b_sig, b_ing = marca(v["nodo_b"])
    hit = a_sig or a_ing or b_sig or b_ing
    if not hit:
        continue
    universo += 1
    por_dom[v["dominio"]] += 1
    print("PUESTO %d [%s] %s" % (v["puesto_intra"], v["dominio"], v["clase"]))
    for tag, k, sg, ig in (("A", v["nodo_a"], a_sig, a_ing), ("B", v["nodo_b"], b_sig, b_ing)):
        if sg or ig:
            tit, nid = texto(k)
            print("   %s %s | %s | SIG=%s ING=%s" % (tag, nid, tit[:60], sg, ig))
print("=" * 60)
print("universo de PARES con candidato al corte %d: %d de %d leidos" % (a.corte, universo, len(V)))
print("por dominio:", dict(por_dom))
