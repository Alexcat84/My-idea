# -*- coding: utf-8 -*-
r"""_auditor_v105_ciega.py . AUDITOR DE LA VUELTA 105, RELECTURA CIEGA.

Vuelca, para cada uno de los SIETE discutibles marcados del reporte 105
(20, 93, 21, 38, 66, 87, 91), los CUATRO nodos enteros del par (madre e
hijo: titulo, resumen, entregable y todos los pasos) mas el paso_casado
LEIDO HOY del nodo. NO imprime la direccion_leida, ni la razon, ni la
correccion_v105, ni el veredicto del re-barrido, ni el motivo: eso va al
REVEAL, que se abre DESPUES de adjudicar por escrito.

USO:
  python docs/loop/_auditor_v105_ciega.py blind  > docs/loop/_auditor_v105_ciega_blind.txt
  python docs/loop/_auditor_v105_ciega.py reveal > docs/loop/_auditor_v105_ciega_reveal.txt
"""
import io, json, os, sys, re, glob

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
DISCUTIBLES = [20, 21, 38, 66, 87, 91, 93]

def leer(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]

def nodo(nid):
    return json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))

filas = []
for p in sorted(glob.glob(os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO*_V*.jsonl"))):
    tramo = re.findall(r"TRAMO(\d)", p)[0]
    for d in leer(p):
        if d["puesto_tramo"] in DISCUTIBLES:
            filas.append(("TRAMO" + tramo, d))

modo = sys.argv[1] if len(sys.argv) > 1 else "blind"
out = io.StringIO()
out.write("MODO %s . %d pares\n" % (modo.upper(), len(filas)))
for tramo, d in filas:
    p = d["puesto_tramo"]; m = d["madre_de_la_bolsa"]; h = d["hijo_de_la_bolsa"]
    nm = nodo(m); nh = nodo(h)
    pasos = nm.get("pasos_accionables") or []
    pc = d.get("paso_casado")
    texto = pasos[pc-1] if isinstance(pc, int) and 1 <= pc <= len(pasos) else "(sin paso_casado utilizable: %r)" % pc
    out.write("\n" + "="*96 + "\nPUESTO %d (%s)  paso_casado=%s  clase_registrada=%s\n" % (p, tramo, pc, d.get("clase")))
    out.write("--- MADRE: %s\n" % m)
    out.write("    titulo: %s\n" % nm.get("titulo_concepto"))
    out.write("    entregable: %s\n" % nm.get("entregable_esperado"))
    out.write("    resumen: %s\n" % (nm.get("resumen_teorico") or "")[:900])
    out.write("    PASOS:\n")
    for i, s in enumerate(pasos, 1):
        out.write("      %s%d) %s\n" % (">>" if i == pc else "  ", i, s))
    out.write("--- HIJO: %s\n" % h)
    out.write("    titulo: %s\n" % nh.get("titulo_concepto"))
    out.write("    entregable: %s\n" % nh.get("entregable_esperado"))
    out.write("    resumen: %s\n" % (nh.get("resumen_teorico") or "")[:900])
    out.write("    PASOS:\n")
    for i, s in enumerate(nh.get("pasos_accionables") or [], 1):
        out.write("      %d) %s\n" % (i, s))
    if modo == "reveal":
        out.write("--- [REVEAL] direccion_leida original: %s\n" % d.get("direccion_leida"))
        out.write("--- [REVEAL] vara: %s\n" % d.get("vara"))
        out.write("--- [REVEAL] razon: %s\n" % d.get("razon"))
        for k in sorted([k for k in d if k.startswith("correccion_v")]):
            out.write("--- [REVEAL] %s: %s\n" % (k, json.dumps(d[k], ensure_ascii=False)))
sys.stdout.write(out.getvalue())
