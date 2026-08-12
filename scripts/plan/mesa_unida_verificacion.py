# -*- coding: utf-8 -*-
"""La nomina de la MESA UNIDA, recomputada del archivo. Solo lectura."""
import json, io, sys, collections, itertools
sys.stdout.reconfigure(encoding="utf-8")
G=json.load(io.open("dataset/metadata/master_graph.json",encoding="utf-8"))["nodos"]
V=[json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl",encoding="utf-8") if l.strip()]
P={frozenset((p["nodo_a"],p["nodo_b"])) for p in (json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl",encoding="utf-8") if l.strip())}
L={frozenset((r["nodo_a"],r["nodo_b"])):r for r in V}
ady=collections.defaultdict(set)
for r in V:
    if r["clase"]=="A": ady[r["nodo_a"]].add(r["nodo_b"]); ady[r["nodo_b"]].add(r["nodo_a"])
def comp(n):
    pila=[n]; c=set()
    while pila:
        x=pila.pop()
        if x in c: continue
        c.add(x); pila.extend(ady[x]-c)
    return c
# LA NOMINA DE TEMA, 17. Por P.6 no es un acto: son TRES actos.
NOM=sorted(set(comp("sistema_stage_gate")) | set(comp("asignacion_recursos_en_gates")) | set(comp("estructura_gates")))
ACTOS=[sorted(comp("estructura_gates")), sorted(comp("sistema_stage_gate")), sorted(comp("asignacion_recursos_en_gates"))]
print("NOMINA DE TEMA: %d miembros, repartidos en %d ACTOS de %s" % (len(NOM),len(ACTOS),[len(a) for a in ACTOS]))
for k in NOM: print("   %-42s %s" % (k,(G[k].get("titulo_concepto") or "")[:58]))
pos=list(itertools.combinations(NOM,2))
ley=[p for p in pos if frozenset(p) in L]
col=[p for p in pos if frozenset(p) in P and frozenset(p) not in L]
fue=[p for p in pos if frozenset(p) not in P and frozenset(p) not in L]
cl=collections.Counter(L[frozenset(p)]["clase"] for p in ley)
print()
print("posibles %d | leidos %d %s | EN COLA %d | FUERA DE COLA %d" % (len(pos),len(ley),dict(cl),len(col),len(fue)))
print()
print("LOS QUE ESTAN EN COLA Y NO LEIDOS (%d):" % len(col))
for a,b in col: print("   %-42s %s" % (a,b))
print()
print("ARISTAS INTERNAS DEL ACTO:")
AL={a:k for k,v in G.items() for a in (v.get("ids_alias") or [])}
def res(x):
    s=set()
    while x in AL and x not in s: s.add(x); x=AL[x]
    return x
S=set(NOM); n=0
for a in NOM:
    for c in ("nodos_previos","nodos_siguientes"):
        for y in (G[a].get(c) or []):
            d=res(y)
            if d in S and d!=a:
                print("   %-42s %-17s %s" % (a,c,d)); n+=1
print("   total %d" % n)
print()
print("GRADO DE CADA MIEMBRO (lo nombran):")
for k in NOM:
    ent=sum(1 for kk,vv in G.items() if not vv.get("deprecado") for c in ("nodos_previos","nodos_siguientes") if k in (vv.get(c) or []))
    print("   %-42s pasos %2d  lo nombran %2d" % (k,len(G[k].get("pasos_accionables") or []),ent))
