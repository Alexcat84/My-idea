#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""barrido_quinta_cara_cuerpo.py . hermano de solo lectura de barrido_quinta_cara.py.

Extiende el barrido de la quinta cara (senal del idioma, 9.28.1) al CUERPO del nodo
(resumen_teorico y pasos_accionables), no solo title+id, y RESTRINGE el universo a los
dominios de nombre largo en castellano: FUERA `core`, cuyos ids son ingleses por diseno
(get_customers, the_mom_test, SPIN, MVP) y donde el nombre ingles ES el nombre, no una
denominacion que se pierda frente a un nombre largo en castellano (9.28.1, primero).

SOLO LECTURA. No toca ni un nodo ni un veredicto.

Universo del barrido: los pares 1..CORTE del archivo de veredictos cuyo dominio NO es
`core`, y que llevan AL MENOS un candidato foraneo (sigla o token ingles/japones) en el
TITULO, el ID o el CUERPO de alguno de sus dos nodos. La separacion denominacion real /
falso positivo se hace A MANO sobre esta salida (el COC deletreado del 2.593 muestra que
ni el regex ni la lista curada bastan solos; 9.28: el barrido es buscador de candidatos,
no censo).

Uso:  python scripts/barrido_quinta_cara_cuerpo.py 2800
      python scripts/barrido_quinta_cara_cuerpo.py 2800 --dominio quality
"""
import json, io, sys, re, argparse, collections

ap = argparse.ArgumentParser()
ap.add_argument("corte", type=int)
ap.add_argument("--dominio", default=None, help="restringe a un solo dominio")
a = ap.parse_args()
sys.stdout.reconfigure(encoding="utf-8")

G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
V = [v for v in V if v["puesto_intra"] <= a.corte and v["dominio"] != "core"]
if a.dominio:
    V = [v for v in V if v["dominio"] == a.dominio]

# marcadores en ingles/japones (palabra completa). curada, incompleta por construccion (9.28).
# la misma lista base del hermano title+id, para que las cifras se comparen.
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
concerns options consequences
""".split()))
ING_RE = re.compile(r"(?<![a-z])(" + "|".join(re.escape(w) for w in INGLES) + r")(?![a-z])", re.I)
SIGLA_RE = re.compile(r"[A-Z]{2,}")

# GENERICOS: tokens ingleses que en `quality` son VOCABULARIO TRADUCIDO ordinario del
# dominio (viven en la prosa de casi todo nodo: grafico de CONTROL, calidad=QUALITY,
# PROCESO, DISENO), no una DENOMINACION que quien viene del libro ingles usa como NOMBRE
# y que puede MORIR en el par (9.28.1). Se excluyen del universo de denominacion foranea,
# igual que la curacion a mano del title+id saco ISO/romanos/normas. La sigla en MAYUSCULAS
# nunca es generica: si aparece deletreada como sigla, cuenta.
GENERICOS = set("""control quality process design function deployment customer performance
performing feedback affinity""".split())


def cuerpo(k):
    n = G.get(k) or {}
    res = n.get("resumen_teorico") or ""
    pasos = " ".join(n.get("pasos_accionables") or [])
    return res + " " + pasos


def marca(k):
    n = G.get(k) or {}
    tit = n.get("titulo_concepto") or ""
    nid = k or ""
    cpo = cuerpo(k)
    # siglas: en titulo o cuerpo (el id no lleva mayusculas). ISO fuera por neutro.
    sig = sorted(set(s for s in SIGLA_RE.findall(tit + " " + cpo) if s != "ISO"))
    # ingles/japones: title+id (como el hermano) SEPARADO del cuerpo, para poder decir
    # cuales caen SOLO en el cuerpo (la senal que title+id no ve). Los genericos se sacan
    # del universo de denominacion foranea pero se dejan visibles con marca [gen].
    ing_ti = sorted(set(m.group(0).lower() for m in ING_RE.finditer(tit + " " + nid.replace("_", " "))))
    ing_cu = sorted(set(m.group(0).lower() for m in ING_RE.finditer(cpo)))
    return tit, sig, ing_ti, ing_cu


def fuerte(sig, ti, cu):
    """hay al menos una DENOMINACION foranea real (no generica): una sigla, o un token
    ingles/japones que no esta en la lista de genericos."""
    if sig:
        return True
    return any(t not in GENERICOS for t in (ti + cu))


universo_bruto = 0       # cualquier candidato, generico incluido (la superficie saturada)
universo_fuerte = 0      # denominacion foranea real (sigla o token no generico)
por_dom = collections.Counter()
solo_cuerpo = 0          # su senal fuerte no estaba en title+id de ningun nodo
for v in V:
    at, a_sig, a_ti, a_cu = marca(v["nodo_a"])
    bt, b_sig, b_ti, b_cu = marca(v["nodo_b"])
    hit = a_sig or a_ti or a_cu or b_sig or b_ti or b_cu
    if not hit:
        continue
    universo_bruto += 1
    es_fuerte = fuerte(a_sig, a_ti, a_cu) or fuerte(b_sig, b_ti, b_cu)
    if not es_fuerte:
        continue
    universo_fuerte += 1
    por_dom[v["dominio"]] += 1
    fuerte_ti = fuerte(a_sig, a_ti, []) or fuerte(b_sig, b_ti, [])
    if not fuerte_ti:
        solo_cuerpo += 1
    print("PUESTO %d [%s] %s%s" % (v["puesto_intra"], v["dominio"], v["clase"],
                                   "  <== SOLO EN CUERPO" if not fuerte_ti else ""))
    for tag, k, tit, sg, ti, cu in (("A", v["nodo_a"], at, a_sig, a_ti, a_cu),
                                    ("B", v["nodo_b"], bt, b_sig, b_ti, b_cu)):
        if sg or ti or cu:
            marc = lambda ws: [("%s[gen]" % w if w in GENERICOS else w) for w in ws]
            print("   %s %s | %s" % (tag, k, tit[:56]))
            print("      SIG=%s ING_ti=%s ING_cuerpo=%s" % (sg, marc(ti), marc(cu)))
print("=" * 60)
print("corte %d, dominios NO-core%s" % (a.corte, (" (%s)" % a.dominio) if a.dominio else ""))
print("universo BRUTO (cualquier token, genericos incluidos): %d de %d leidos" % (universo_bruto, len(V)))
print("universo de DENOMINACION FORANEA (sigla o token no generico, title+id+cuerpo): %d" % universo_fuerte)
print("de esos, pares cuya senal fuerte esta SOLO en el cuerpo: %d" % solo_cuerpo)
print("por dominio (universo fuerte):", dict(por_dom))
