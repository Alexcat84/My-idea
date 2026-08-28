# -*- coding: utf-8 -*-
"""Auditor v110: recuento PROPIO del lote preposicional, codigo mio, sin
importar el script del ejecutor. Aplica las correcciones declaradas sobre
direccion_leida (mismo criterio que contar_cierre_efectivo) leyendo los
jsonl a mano."""
import io, json, os, re, glob
RAIZ = os.getcwd()
PLAN = os.path.join(RAIZ, "docs", "plan")
rutas = sorted(glob.glob(os.path.join(PLAN, "OP_E_03_LECTURA_TRAMO*_V*.jsonl")))
print("tramos:", [os.path.basename(r) for r in rutas])
filas=[]
for r in rutas:
    for l in io.open(r, encoding="utf-8"):
        l=l.strip()
        if l: filas.append(json.loads(l))
print("n =", len(filas))

def direccion_final(f):
    d = f.get("direccion_leida")
    for c in (f.get("correcciones") or []):
        if c.get("campo_corregido") == "direccion_leida":
            d = c.get("valor_nuevo")
    return d

resueltas = [f for f in filas if direccion_final(f) == "RESUELTA"]
print("RESUELTA (tras correcciones):", len(resueltas))

g = json.load(io.open(os.path.join(RAIZ,"dataset","metadata","master_graph.json"), encoding="utf-8"))
nodos = g["nodos"]
alias = {}
for nid, v in nodos.items():
    for a in (v.get("ids_alias") or []):
        if a != nid: alias[a] = nid
def resolver(x, vistos=None):
    vistos = vistos or set()
    while x not in nodos and x in alias and x not in vistos:
        vistos.add(x); x = alias[x]
    return x

PREP = re.compile(r"\b(con|por|a|de|en|hacia|contra)\b", re.IGNORECASE)
con_prep=[]; sin_prep=[]; malos=[]
for f in resueltas:
    m = resolver(f["madre_de_la_bolsa"])
    if m not in nodos: malos.append((f["puesto_tramo"], "madre no resuelve")); continue
    pasos = nodos[m].get("pasos_accionables") or []
    i = f.get("paso_casado")
    if not isinstance(i,int) or i<1 or i>len(pasos):
        malos.append((f["puesto_tramo"], "paso_casado fuera de rango")); continue
    txt = pasos[i-1]
    (con_prep if PREP.search(txt) else sin_prep).append((f["puesto_tramo"], m, i, txt))
print("MALOS:", malos)
print("CON preposicion:", len(con_prep))
print("SIN preposicion:", len(sin_prep), sorted(p for p,_,_,_ in sin_prep))
json.dump([{"puesto":p,"madre":m,"paso":i,"texto":t} for p,m,i,t in con_prep],
          io.open("docs/loop/_auditor_v110/lote63.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
