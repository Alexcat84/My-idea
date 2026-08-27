# Auditor v82: vuelca los campos de lectura de un nodo, sin razones ajenas.
import json, sys
from pathlib import Path
R = Path("dataset/nodos")
def volcar(nid):
    d = json.loads((R / (nid + ".json")).read_text(encoding="utf-8"))
    print("=" * 78)
    print("NODO:", nid)
    print("titulo:", d.get("titulo_concepto"))
    print("dominio:", d.get("dominio"), "| fase:", d.get("fase_proyecto"), "| fuente:", d.get("fuente"))
    print("resumen_teorico:", (d.get("resumen_teorico") or ""))
    pasos = d.get("pasos_accionables") or []
    print("PASOS (%d):" % len(pasos))
    for i, s in enumerate(pasos, 1):
        print("  %d. %s" % (i, s))
    print("ENTREGABLE:", d.get("entregable_esperado"))
    print("nodos_siguientes:", d.get("nodos_siguientes"))
    print("nodos_previos:", d.get("nodos_previos"))
for nid in sys.argv[1:]:
    volcar(nid)
