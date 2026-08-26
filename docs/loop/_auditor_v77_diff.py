import json, subprocess, sys
def pares(ref):
    b = subprocess.run(["git","show",f"{ref}:dataset/metadata/master_graph.json"],capture_output=True)
    N = json.loads(b.stdout.decode("utf-8"))["nodos"]
    ps, pp = set(), set()
    for nid, n in N.items():
        for d in (n.get("nodos_siguientes") or []): ps.add((nid,d))
        for d in (n.get("nodos_previos") or []): pp.add((d,nid))
    return ps, pp
a_s, a_p = pares(sys.argv[1])
b_s, b_p = pares(sys.argv[2])
nuevas = sorted(b_s - a_s); borradas = sorted(a_s - b_s)
print(f"NUEVAS en nodos_siguientes: {len(nuevas)}")
for m,h in nuevas:
    rec = "reciproca OK" if (m,h) in b_p else "!! SIN RECIPROCA en nodos_previos"
    print(f"  {m} -> {h}   [{rec}]")
print(f"BORRADAS de nodos_siguientes: {len(borradas)}")
for m,h in borradas: print(f"  {m} -> {h}")
print(f"NUEVAS en nodos_previos: {len(b_p - a_p)}   BORRADAS en nodos_previos: {len(a_p - b_p)}")
huerfanas = (b_p - a_p) - (b_s - a_s)
print(f"previos nuevos SIN siguiente nuevo correspondiente: {len(huerfanas)}", sorted(huerfanas)[:10])
# auto-aristas y duplicadas
auto = [(m,h) for (m,h) in b_s if m==h]
print("auto-aristas:", len(auto))
