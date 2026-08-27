# -*- coding: utf-8 -*-
"""_auditor_v95_ciega_pasos.py . LA RELECTURA CIEGA DE LA VUELTA 95: vuelca
los pasos_accionables de los dos nodos de cada par SIN LA RAZON y SIN la
direccion escrita, para adjudicar antes de destapar (AUDITOR.md seccion 1.2).

    python docs/loop/_auditor_v95_ciega_pasos.py > docs/loop/_auditor_v95_ciega_pasos.txt
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUESTOS = [886, 890, 947, 1844, 896, 909, 910, 940, 983, 993, 1020, 1057, 1086, 1196, 1220, 1083]


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


g = json.load(io.open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]
ver = {int(v["puesto_intra"]): v for v in cargar(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"))}


def pinta(nid, etiqueta):
    n = g.get(nid) or {}
    print("  %s  [%s]" % (etiqueta, nid))
    print("     titulo: %s" % n.get("titulo_concepto", "(sin titulo)"))
    pasos = n.get("pasos_accionables") or []
    if not pasos:
        print("     (sin pasos_accionables)")
    for i, p in enumerate(pasos, 1):
        if isinstance(p, dict):
            p = p.get("texto") or p.get("paso") or json.dumps(p, ensure_ascii=False)
        print("     %d. %s" % (i, p))


for p in PUESTOS:
    v = ver[p]
    print("=" * 90)
    print("PUESTO %d  (dominio %s, clase %s)  -- PASOS SOLOS, SIN RAZON" % (p, v["dominio"], v["clase"]))
    print("=" * 90)
    pinta(v["nodo_a"], "NODO A")
    print()
    pinta(v["nodo_b"], "NODO B")
    print()
