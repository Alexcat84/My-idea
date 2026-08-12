# -*- coding: utf-8 -*-
"""RE-MEDIDA del puro COMPETENCIA ENTRE INVERSORES, con los dos instrumentos."""
import json, io, sys, re, collections, itertools
sys.stdout.reconfigure(encoding="utf-8")
G = json.load(io.open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
VIV = {k: v for k, v in G.items() if not v.get("deprecado")}
V = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", encoding="utf-8") if l.strip()]
P = [json.loads(l) for l in io.open("docs/INTRA_DOMINIO_PARES.jsonl", encoding="utf-8") if l.strip()]
CORTE = max(r["puesto_intra"] for r in V)
leido = {frozenset((r["nodo_a"], r["nodo_b"])): r for r in V}
encola = {frozenset((p["nodo_a"], p["nodo_b"])) for p in P}
ady = collections.defaultdict(set)
for r in V:
    if r["clase"] == "A": ady[r["nodo_a"]].add(r["nodo_b"]); ady[r["nodo_b"]].add(r["nodo_a"])
def comp(n):
    pila=[n]; c=set()
    while pila:
        x=pila.pop()
        if x in c: continue
        c.add(x); pila.extend(ady[x]-c)
    return c
RX = re.compile(r"leverage|term.?sheet|competencia.*(vc|inversor)|anclaje|negociacion.*vc", re.I)
cont = sorted(k for k,v in VIV.items() if RX.search(k) or RX.search(v.get("titulo_concepto") or ""))
print("1. CONTADOR: %d candidatos" % len(cont))
for k in cont: print("   -", k, "|", VIV[k].get("titulo_concepto"))
nuc = comp("gestion_multiples_term_sheets")
print()
print("2. BARRIDO DE LAS A: componente de %d nodos" % len(nuc))
for k in sorted(nuc):
    print("   -", k, "|", VIV[k].get("titulo_concepto"), "" if k in cont else "  <== SOLO POR EL BARRIDO")
print()
nom = sorted(nuc)
pos = len(nom)*(len(nom)-1)//2
ley = [p for p in itertools.combinations(nom,2) if frozenset(p) in leido]
col = [p for p in itertools.combinations(nom,2) if frozenset(p) in encola and frozenset(p) not in leido]
fue = [p for p in itertools.combinations(nom,2) if frozenset(p) not in encola and frozenset(p) not in leido]
cl = collections.Counter(leido[frozenset(p)]["clase"] for p in ley)
print("3. COBERTURA al puesto %d: miembros %d | posibles %d | leidos %d %s | en cola %d | FUERA DE COLA %d"
      % (CORTE, len(nom), pos, len(ley), dict(cl), len(col), len(fue)))
forma = "PURO" if cl.get("A",0)==len(ley)==pos else ("SUB-PURO" if cl.get("A",0)==len(ley) else "MEZCLADO")
print("   FORMA:", forma)
print()
for a,b in ley: print("   [%s] %s | %s (puesto %d)"%(leido[frozenset((a,b))]["clase"],a,b,leido[frozenset((a,b))]["puesto_intra"]))
print()
print("   FALTANTES, nombrados:")
for a,b in fue: print("      FUERA DE COLA:",a,"|",b)
for a,b in col: print("      EN COLA:",a,"|",b)
