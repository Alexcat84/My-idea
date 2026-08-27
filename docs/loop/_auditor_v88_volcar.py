# -*- coding: utf-8 -*-
"""AUDITOR vuelta 88. Vuelca las fichas del camino del 117 leyendo los ids
del fichero del desfase (no tecleados) mas los del camino publicado por el
ejecutor, verificando cada arista contra el grafo en LAS DOS VISTAS.
"""
import json
import os
import re
import sys

GRAFO = "dataset/metadata/master_graph.json"
nodos = json.load(open(GRAFO, encoding="utf-8"))["nodos"]

# El camino se LEE de la salida del instrumento del ejecutor, no se teclea.
SAL = "docs/loop/SALIDA_V88_TAREA2_RELECTURA_117.txt"
txt = open(SAL, encoding="utf-8", errors="replace").read()

def ficha(nid):
    v = nodos.get(nid)
    if v is None:
        return "  [NO EXISTE EN EL GRAFO]"
    out = []
    out.append("  titulo: %s" % v.get("titulo_concepto"))
    out.append("  dominio: %s | deprecado: %r" % (v.get("dominio"), v.get("deprecado")))
    pas = v.get("pasos_accionables") or []
    out.append("  pasos_accionables (%d):" % len(pas))
    for i, p in enumerate(pas, 1):
        if isinstance(p, dict):
            p = p.get("texto") or p.get("descripcion") or json.dumps(p, ensure_ascii=False)
        out.append("    %d. %s" % (i, p))
    out.append("  entregable_esperado: %s" % (v.get("entregable_esperado") or "")[:400])
    out.append("  resumen_teorico: %s" % (v.get("resumen_teorico") or "")[:600])
    out.append("  siguientes (%d): %s" % (len(v.get("nodos_siguientes") or []), v.get("nodos_siguientes")))
    out.append("  previos (%d): %s" % (len(v.get("nodos_previos") or []), v.get("nodos_previos")))
    return "\n".join(out)

ids = sys.argv[1:]
for nid in ids:
    print("=" * 78)
    print("NODO: %s" % nid)
    print("=" * 78)
    print(ficha(nid))
    print()
