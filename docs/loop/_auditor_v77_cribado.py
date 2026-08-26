"""Cruza un conjunto de pares (madre,hijo) contra INTRA_DOMINIO_VEREDICTOS.jsonl,
sin direccion (el cribado lee pares, no aristas)."""
import json, subprocess, sys
V={}
for l in open("docs/INTRA_DOMINIO_VEREDICTOS.jsonl",encoding="utf-8"):
    if not l.strip(): continue
    r=json.loads(l)
    V[frozenset((r["nodo_a"],r["nodo_b"]))]=r
print("veredictos cargados:",len(V))
from collections import Counter
print("marcador del archivo:",Counter(r["clase"] for r in V.values()))
def pares(ref):
    b=subprocess.run(["git","show",f"{ref}:dataset/metadata/master_graph.json"],capture_output=True)
    N=json.loads(b.stdout.decode("utf-8"))["nodos"]
    return {(nid,d) for nid,n in N.items() for d in (n.get("nodos_siguientes") or [])}
def cruzar(nombre, conj):
    print(f"\n=== {nombre}: {len(conj)} pares ===")
    leidos=[]; n_A=0
    for m,h in sorted(conj):
        r=V.get(frozenset((m,h)))
        if r:
            leidos.append((m,h,r))
            if r["clase"]=="A": n_A+=1
    print(f"LEIDOS por el cribado: {len(leidos)} | NUNCA LEIDOS: {len(conj)-len(leidos)}")
    for m,h,r in leidos:
        print(f"  [{r['clase']}] puesto {r['puesto_intra']}  {m} -> {h}")
        print(f"       razon: {r['razon'][:160]}")
    print(f"CLASE A ENTRE LOS LEIDOS: {n_A}")
    return n_A
if __name__=="__main__":
    a=pares("4f2e587a"); b=pares("122bcc77")
    t3 = b-a
    cruzar("TRAMO 3, las 28 aristas nuevas de esta vuelta", t3)
    # tramo 2: 26 nuevas entre 3b319801 (apertura v76) y 7fa9f979 (cierre v76)
    t2 = pares("7fa9f979") - pares("3b319801")
    cruzar("TRAMO 2, las 26 aristas de la vuelta 76", t2)
    # fase 04 entera
    base = pares("62d4f28e")
    cruzar("FASE 04 ENTERA (contra 62d4f28e)", b-base)
