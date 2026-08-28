# -*- coding: utf-8 -*-
"""Instrumento PROPIO del auditor, vuelta 103. Vuelca a ciegas
entregable_esperado + pasos_accionables de madre e hijo, SIN clase, SIN
direccion_leida, SIN razon y SIN paso_casado. --modo reveal destapa."""
import argparse, io, json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
def nodos():
    return json.load(io.open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"),encoding="utf-8"))["nodos"]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--modo",required=True); ap.add_argument("--puestos",required=True)
    a=ap.parse_args(); sys.stdout.reconfigure(encoding="utf-8")
    ps=[int(x) for x in a.puestos.split(",")]
    filas={json.loads(l)["puesto_tramo"]: json.loads(l) for l in io.open(T1,encoding="utf-8") if l.strip()}
    G=nodos()
    for p in ps:
        r=filas[p]
        print("="*88); print("PUESTO %d"%p)
        if a.modo=="blind":
            for rol,k in (("MADRE","madre_de_la_bolsa"),("HIJO","hijo_de_la_bolsa")):
                n=G[r[k]]
                print("-- %s: %s | titulo: %s"%(rol,r[k],n.get("titulo_concepto")))
                print("   entregable: %s"%n.get("entregable_esperado"))
                for i,s in enumerate(n.get("pasos_accionables") or [],1):
                    print("   paso %d: %s"%(i,s))
        else:
            print("  paso_casado: %s"%r.get("paso_casado"))
            print("  direccion_leida: %s"%r.get("direccion_leida"))
            print("  clase: %s"%r.get("clase"))
            print("  razon: %s"%r.get("razon"))
        print()
if __name__=="__main__": raise SystemExit(main())
