"""Auditor v80: aristas acumuladas de la fase 04 contra 62d4f28e, cuantas toca la
vara de los A, y el censo de 2-ciclos en apertura y cierre. ESTE es el script que
produjo _auditor_v80_fase04.txt en la vuelta 80."""
import json, sys
sys.path.insert(0,"docs/loop")
from _auditor_v80_conteo import medir
A=medir("62d4f28e"); H=medir("WORK"); AP=medir("3cdf90d1")
nuevas=sorted(H["S"]-A["S"])
print(f"ARISTAS ACUMULADAS DE LA FASE 04 (S(HEAD) - S(62d4f28e)): {len(nuevas)}")
print(f"borradas desde 62d4f28e: {len(A['S']-H['S'])}")
G=json.load(open("dataset/metadata/master_graph.json",encoding="utf-8"))["nodos"]
vivo=lambda n: n in G and not G[n].get("deprecado")
paresA=set()
for l in open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl",encoding="utf-8"):
    l=l.strip()
    if not l: continue
    o=json.loads(l)
    if o["clase"]=="A" and vivo(o["nodo_a"]) and vivo(o["nodo_b"]):
        paresA.add(o["nodo_a"]); paresA.add(o["nodo_b"])
toc=[(m,h) for m,h in nuevas if m in paresA or h in paresA]
print(f"nodos vivos en un veredicto A vivo: {len(paresA)}")
print(f"DE LAS {len(nuevas)}, TOCADAS POR LA VARA DE LOS A: {len(toc)}")
for m,h in toc: print(f"   {m} -> {h}")
print("\n--- 2-CICLOS (pares escritos en los DOS sentidos en nodos_siguientes) ---")
for nom,r in (("apertura 3cdf90d1",AP),("cierre HEAD",H)):
    c={frozenset(e) for e in r["S"] if (e[1],e[0]) in r["S"]}
    print(f"  {nom}: {len(c)}")
cA={frozenset(e) for e in AP["S"] if (e[1],e[0]) in AP["S"]}
cH={frozenset(e) for e in H["S"] if (e[1],e[0]) in H["S"]}
print(f"  NUEVOS esta vuelta: {len(cH-cA)} | desaparecidos: {len(cA-cH)}")
print(f"\n  solo en nodos_siguientes: apertura {AP['solo_S']} / cierre {H['solo_S']}")
print(f"  solo en nodos_previos   : apertura {AP['solo_P']} / cierre {H['solo_P']}")
