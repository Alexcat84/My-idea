# -*- coding: utf-8 -*-
"""Auditor v141: mide IDA Y VUELTA a la vez sobre las direcciones de las cinco
operaciones remitidas a la fase 06, con parser y resolutor propios y el regimen
de vuelta LEIDO DE LA VERIFICACION de la ficha (nunca del campo tipo).
Se corre ANTES de abrir SALIDA_V141_4_RELECTURA_AL_DOBLE.txt."""
import json, os, glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
N={}; ALIAS={}
for p in glob.glob("dataset/nodos/*.json"):
    d=json.load(open(p,encoding="utf-8")); nid=d.get("node_id") or os.path.splitext(os.path.basename(p))[0]
    N[nid]=d
    for a in d.get("ids_alias") or []: ALIAS[a]=nid
def R(x):
    v=x
    for _ in range(10):
        if v in N and not N[v].get("deprecado"): return v
        if v in ALIAS and ALIAS[v]!=v: v=ALIAS[v]; continue
        return v
    return v
SIG={n:[R(t) for t in (d.get("nodos_siguientes") or [])] for n,d in N.items()}
PREV={n:[R(t) for t in (d.get("nodos_previos") or [])] for n,d in N.items()}
def hay(a,b):
    a,b=R(a),R(b)
    return (b in SIG.get(a,[])) or (a in PREV.get(b,[]))
OPS={}
for l in open("docs/plan/OPERACIONES.jsonl",encoding="utf-8"):
    l=l.strip()
    if l: d=json.loads(l); OPS[d["id_op"]]=d
REM=["OP-M-03-ENLACES","OP-M-01-SEXTO","OP-E-05","OP-M-01-ESLABONES","OP-E-04"]
RX=re.compile(r"([a-z0-9_]+)\s*->\s*([a-z0-9_]+)")
tot=0; conv=0; prohibe_conv=0
for oid in REM:
    d=OPS.get(oid)
    if d is None: print("!! %s no esta en OPERACIONES.jsonl"%oid); continue
    verif=" ".join(str(x) for x in (d.get("verificacion") or []))
    tipo=(d.get("tipo") or "")
    vl=verif.lower()
    if "la vuelta si existe y es correcta" in vl or "enlace mutuo" in vl: reg="MUTUO"
    elif "la vuelta no debe existir" in vl or "la vuelta no existe" in vl: reg="PROHIBE"
    else: reg="SIN REGLA"
    dirs=[]
    for a in d.get("aristas_nuevas") or []:
        for m in RX.finditer(a):
            dirs.append((R(m.group(1)), R(m.group(2))))
    uniq=[]
    for x in dirs:
        if x not in uniq: uniq.append(x)
    print("="*74); print("%s | tipo=%s | REGIMEN LEIDO DE LA VERIFICACION: %s"%(oid,tipo[:40],reg))
    print("  filas de ficha: %d | direcciones distintas tras resolver: %d"%(len(dirs),len(uniq)))
    for (a,b) in uniq:
        tot+=1
        i=hay(a,b); v=hay(b,a)
        if v: conv+=1
        if v and reg=="PROHIBE": prohibe_conv+=1
        print("   %-42s -> %-38s IDA=%-5s VUELTA=%-5s%s"%(a,b,i,v," <-- VUELTA EN FICHA QUE LA PROHIBE" if (v and reg=="PROHIBE") else ""))
print("="*74)
print("TOTAL direcciones distintas medidas: %d"%tot)
print("con LA VUELTA PRESENTE: %d"%conv)
print("de esas, en ficha que PROHIBE la vuelta: %d"%prohibe_conv)
