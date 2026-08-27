# -*- coding: utf-8 -*-
"""DESTAPE del auditor 96: se corre DESPUES de haber adjudicado a ciegas."""
import json, io, sys
T = [json.loads(l) for l in io.open("docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl", encoding="utf-8") if l.strip()]
por = {r["puesto_tramo"]: r for r in T}
for k in [int(x) for x in sys.argv[1:]]:
    r = por[k]
    print("=" * 78)
    print("PAR %d | clase ESCRITA: %s | paso_casado: %s" % (k, r["clase"], r.get("paso_casado")))
    print("direccion_leida: %s" % r.get("direccion_leida"))
    print("bolsa decia: %s (madre) / %s (hijo)" % (r["madre_de_la_bolsa"], r["hijo_de_la_bolsa"]))
    print("razon: %s" % r.get("razon"))
    print("vara: %s" % r.get("vara"))
    print()
