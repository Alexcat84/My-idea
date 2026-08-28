# -*- coding: utf-8 -*-
"""Censo de alcance, codigo del AUDITOR, sin importar censar_alcance_de_la_vara."""
import io, os, re, sys
RAIZ = os.getcwd(); LOOP = os.path.join(RAIZ, "docs", "loop")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import contar_cierre_efectivo as cce
FICH = [("SALIDA_V105_TAREA4_3_RE_BARRIDO.txt","b"),("SALIDA_V106_TAREA4_3_TRES_VIAS.txt","b"),
        ("SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md","t"),("SALIDA_V107_TAREA5_3_TRAMO1_TRES_VIAS.md","t"),
        ("SALIDA_V108_TAREA3_3_TRES_VIAS_46.md","t"),("SALIDA_V108_TAREA5_2_TRAMO2_TRES_VIAS.md","t")]
CAB = re.compile(r"^--- PUESTO (\d+) ---")
VER = re.compile(r"VEREDICTO:\s*(OBJETO|SATELITE|NO_OBJETO)\b")
FIL = re.compile(r"^(\d+)\s*\|.*\|\s*(OBJETO|SATELITE|NO_OBJETO)\b")
ult = {}; prim = {}
for nom, f in FICH:
    txt = io.open(os.path.join(LOOP,nom),encoding="utf-8").read()
    hall = {}
    if f=="b":
        cur=None
        for l in txt.splitlines():
            m=CAB.match(l)
            if m: cur=int(m.group(1)); continue
            if not l.strip(): cur=None; continue
            if cur is not None:
                v=VER.search(l)
                if v: hall[cur]=v.group(1); cur=None
    else:
        for l in txt.splitlines():
            m=FIL.match(l)
            if m: hall[int(m.group(1))]=m.group(2)
    for p,v in hall.items():
        ult[p]=(v,nom)
        prim.setdefault(p,(v,nom))
d,fallos = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
assert not fallos, fallos
nores=set(d["sin_dir"]); todos=set(range(1,d["n"]+1)); res=todos-nores
print("n TOTAL", d["n"], "| RESUELTA", len(res), "| NO RESUELTA", len(nores))
for et,gr in (("RESUELTA",sorted(res)),("NO RESUELTA",sorted(nores))):
    c={"OBJETO":[],"SATELITE":[],"NO_OBJETO":[],"SIN":[]}
    for p in gr:
        v=ult.get(p)
        c["SIN"].append(p) if v is None else c[v[0]].append(p)
    print(et, {k:(len(v), v if len(v)<=10 else "") for k,v in c.items()})
print("VUELCOS (primera != ultima):", sorted(p for p in ult if prim[p][0]!=ult[p][0]))
for p in sorted(p for p in ult if prim[p][0]!=ult[p][0]):
    print("  ",p,prim[p],"->",ult[p])
