import json, subprocess, sys
def medir(blob):
    g = json.loads(blob)
    nodos = g["nodos"]
    if not isinstance(nodos, dict):
        raise SystemExit("forma inesperada")
    total = len(nodos)
    vivos, depr = 0, 0
    sig = prev = 0
    S = set(); P = set()
    desaj = 0
    for k, n in nodos.items():
        if n.get("node_id") != k: desaj += 1
        if n.get("deprecado") is True: depr += 1
        else: vivos += 1
        for d in n.get("nodos_siguientes", []) or []:
            sig += 1; S.add((k, d))
        for o in n.get("nodos_previos", []) or []:
            prev += 1; P.add((o, k))
    return total, vivos, depr, sig, prev, sig+prev, len(S | P), desaj

refs = sys.argv[1:]
for r in refs:
    if r == "WORK":
        blob = open("dataset/metadata/master_graph.json", encoding="utf-8").read()
    else:
        blob = subprocess.run(["git","cat-file","-p",r+":dataset/metadata/master_graph.json"],
                              capture_output=True).stdout.decode("utf-8")
    t,v,d,s,p,su,u,dj = medir(blob)
    print(f"{r:>10}  nodos {t} / vivos {v} / depr {d} | sig {s} prev {p} suma {su} union {u} | desaj {dj}")
