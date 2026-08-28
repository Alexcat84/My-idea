# -*- coding: utf-8 -*-
"""_auditor_v107_ciega.py . INSTRUMENTO DEL AUDITOR, VUELTA 107.
Vuelca los DOS nodos de un puesto de OP-E-03 ENTEROS (titulo, resumen,
entregable y todos los pasos), con el paso_casado marcado, y SIN la
direccion_leida, SIN la razon y SIN ninguna correccion_vNN: el auditor
adjudica primero y destapa despues.
  --modo blind    (por defecto) solo los nodos
  --modo reveal   destapa direccion_leida, razon y correcciones
USO: python docs/loop/_auditor_v107_ciega.py --puestos 145 109 --modo blind
"""
import argparse, io, json, os, re
RA = "docs/plan"
TR = ["OP_E_03_LECTURA_TRAMO1_V96.jsonl", "OP_E_03_LECTURA_TRAMO2_V97.jsonl",
      "OP_E_03_LECTURA_TRAMO3_V98.jsonl", "OP_E_03_LECTURA_TRAMO4_V99.jsonl"]
CR = re.compile(r"^correccion_v(\d+)$")

def filas():
    d = {}
    for t in TR:
        for l in io.open(os.path.join(RA, t), encoding="utf-8"):
            if l.strip():
                r = json.loads(l); r["_f"] = t; d[r["puesto_tramo"]] = r
    return d

def nodo(nid):
    p = os.path.join("dataset", "nodos", nid + ".json")
    return json.load(io.open(p, encoding="utf-8"))

def volcar(nid, paso_casado, papel):
    n = nodo(nid)
    print("  --- %s: %s (%s)" % (papel, nid, n.get("titulo_concepto")))
    print("      dominio: %s | deprecado: %s" % (n.get("dominio"), n.get("deprecado")))
    print("      RESUMEN: %s" % (n.get("resumen_teorico") or "").strip())
    print("      ENTREGABLE: %s" % (n.get("entregable_esperado") or "").strip())
    for i, p in enumerate(n.get("pasos_accionables") or [], 1):
        marca = "  <== PASO CASADO" if (papel == "MADRE" and i == paso_casado) else ""
        print("      paso %d: %s%s" % (i, p, marca))

ap = argparse.ArgumentParser()
ap.add_argument("--puestos", nargs="+", type=int, required=True)
ap.add_argument("--modo", default="blind")
a = ap.parse_args()
F = filas()
for p in a.puestos:
    r = F[p]
    print("=" * 78)
    print("PUESTO %d (%s) | dominio %s | paso_casado declarado: %s | clase: %s" % (
        p, r["_f"], r.get("dominio"), r.get("paso_casado"), r.get("clase")))
    volcar(r["madre_de_la_bolsa"], r.get("paso_casado"), "MADRE")
    volcar(r["hijo_de_la_bolsa"], None, "HIJO")
    if a.modo == "reveal":
        print("  *** direccion_leida CRUDA: %s" % r.get("direccion_leida"))
        print("  *** razon: %s" % r.get("razon"))
        for _, k in sorted(((int(CR.match(k).group(1)), k) for k in r if CR.match(k))):
            print("  *** %s: %s" % (k, json.dumps(r[k], ensure_ascii=False)))
