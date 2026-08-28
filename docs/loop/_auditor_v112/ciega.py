# -*- coding: utf-8 -*-
"""Volcado CIEGO propio del auditor v112: madre (paso casado) + hijo entero,
SIN direccion_leida, SIN razon, SIN vara, SIN veredicto."""
import io, json, os, sys
RAIZ = os.getcwd()
TRAMOS = [os.path.join(RAIZ,"docs","plan","OP_E_03_LECTURA_TRAMO%d_V%d.jsonl"%(i,v))
          for i,v in ((1,96),(2,97),(3,98),(4,99))]
PROHIBIDOS = ("direccion_leida","razon","vara","veredicto","correccion","clase","nota")
filas={}
for r in TRAMOS:
    for ln in io.open(r,encoding="utf-8"):
        if ln.strip():
            d=json.loads(ln); filas[d["puesto_tramo"]]=(d,r)
g=json.load(io.open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"),encoding="utf-8"))
nodos=g["nodos"]
for p in [int(x) for x in sys.argv[1:]]:
    f,r=filas[p]
    madre=nodos.get(f["madre_de_la_bolsa"],{}); hijo=nodos.get(f["hijo_de_la_bolsa"],{})
    pm=madre.get("pasos_accionables",[]); idx=f["paso_casado"]-1
    print("="*96)
    print("PUESTO %d   (fichero %s)"%(p, os.path.basename(r)))
    print("MADRE: %s  |  titulo: %s"%(f["madre_de_la_bolsa"], madre.get("titulo_concepto")))
    print("  PASO CASADO n.%d de %d: %s"%(f["paso_casado"], len(pm), pm[idx] if 0<=idx<len(pm) else "(FUERA DE RANGO)"))
    print("  TODOS LOS PASOS DE LA MADRE:")
    for i,s in enumerate(pm,1): print("    %d. %s"%(i,s))
    print("HIJO: %s  |  titulo: %s"%(f["hijo_de_la_bolsa"], hijo.get("titulo_concepto")))
    print("  descripcion: %s"%(hijo.get("descripcion") or hijo.get("descripcion_corta")))
    print("  PASOS DEL HIJO:")
    for i,s in enumerate(hijo.get("pasos_accionables",[]),1): print("    %d. %s"%(i,s))
    print("  entregable_esperado: %s"%hijo.get("entregable_esperado"))
    print("  CAMPOS DE LA FILA (censurados los prohibidos):")
    for k,v in f.items():
        if any(t in k.lower() for t in PROHIBIDOS): continue
        print("    %s = %s"%(k, json.dumps(v,ensure_ascii=False)[:300]))
