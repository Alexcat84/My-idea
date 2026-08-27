# -*- coding: utf-8 -*-
"""AUDITOR, vuelta 87. Vuelca ENTERAS las 8 fichas del tramo 12 (madre e hijo
de las cuatro unidades), leyendo los ids del fichero del filtro: ninguno se
teclea. Es el volcado desde el que hice la relectura ciega de la seccion 2 del
acta.

  python docs/loop/_auditor_v87_volcar.py > docs/loop/_auditor_v87_volcado.txt
"""
import json
import io
import sys
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

F87 = "docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V87.jsonl"
B = [json.loads(l) for l in open(F87, encoding="utf-8") if l.strip()]


def ficha(nid):
    r = os.path.join("dataset", "nodos", nid + ".json")
    return json.load(open(r, encoding="utf-8")) if os.path.exists(r) else None


def volcar(nid, rol):
    d = ficha(nid)
    print()
    print("-" * 78)
    print("%s: %s" % (rol, nid))
    print("-" * 78)
    if d is None:
        print("   (ficha no encontrada)")
        return
    for k in ("titulo_concepto", "dominio", "etiqueta_arbol", "fase_proyecto",
              "resumen_teorico", "condiciones_activacion", "entregable_esperado"):
        if d.get(k):
            print("  %s: %s" % (k.upper(), d[k]))
    ps = d.get("pasos_accionables") or []
    print("  PASOS_ACCIONABLES (%d):" % len(ps))
    for i, p in enumerate(ps, 1):
        print("    %d. %s" % (i, p))
    print("  nodos_siguientes: %s" % (d.get("nodos_siguientes") or []))
    print("  nodos_previos: %s" % (d.get("nodos_previos") or []))


for i in range(117, 121):
    f = B[i]
    print()
    print("=" * 78)
    print("UNIDAD %d | %s -> %s | paso %s | dominio %s"
          % (i, f["madre"], f["hijo"], f["paso"], f["dominio"]))
    print("=" * 78)
    volcar(f["madre"], "MADRE")
    volcar(f["hijo"], "HIJO")
