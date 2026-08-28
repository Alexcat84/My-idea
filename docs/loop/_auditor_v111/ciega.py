# -*- coding: utf-8 -*-
import json, io, sys
TR=[("docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl",0),("docs/plan/OP_E_03_LECTURA_TRAMO2_V97.jsonl",0),
    ("docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl",0),("docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl",0)]
filas={}
for ruta,off in TR:
    for l in io.open(ruta,encoding="utf-8"):
        if l.strip():
            r=json.loads(l); filas[off+r["puesto_tramo"]]=r
g=json.load(io.open("dataset/metadata/master_graph.json",encoding="utf-8"))["nodos"]
for p in [int(x) for x in sys.argv[1:]]:
    r=filas[p]
    m=r["madre_de_la_bolsa"]; h=r["hijo_de_la_bolsa"]; pc=r["paso_casado"]
    print("="*100); print("PUESTO",p,"| dominio",r["dominio"],"| paso_casado",pc)
    for et,k in (("MADRE",m),("HIJO",h)):
        n=g[k]
        print("-"*90); print(et,":",k,"|",n.get("titulo_concepto"))
        ps=n.get("pasos_accionables") or []
        for i,s in enumerate(ps,1):
            marca=" <<< PASO CASADO" if (et=="MADRE" and i==pc) else ""
            print("   %d. %s%s"%(i,s,marca))
        ent=n.get("entregable_esperado")
        if ent: print("   ENTREGABLE:",ent)
