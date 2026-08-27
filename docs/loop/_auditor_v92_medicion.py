import json, subprocess, sys, hashlib, os

def leer_ref(ref):
    """Devuelve dict id -> nodo leyendo dataset/nodos/*.json de un ref de git (o WORK)."""
    nodos = {}
    if ref == "WORK":
        d = "dataset/nodos"
        for f in sorted(os.listdir(d)):
            if not f.endswith(".json"): continue
            with open(os.path.join(d, f), encoding="utf-8") as fh:
                nodos[f[:-5]] = json.load(fh)
    else:
        out = subprocess.run(["git","ls-tree","--name-only",ref+":dataset/nodos"],
                             capture_output=True, text=True, check=True).stdout
        for f in out.split("\n"):
            f = f.strip()
            if not f.endswith(".json"): continue
            blob = subprocess.run(["git","show",ref+":dataset/nodos/"+f],
                                  capture_output=True, check=True).stdout.decode("utf-8")
            nodos[f[:-5]] = json.loads(blob)
    return nodos

def medir(ref):
    nodos = leer_ref(ref)
    total = len(nodos)
    deprecados = sum(1 for n in nodos.values() if n.get("deprecado") or n.get("estado")=="deprecado")
    sig = prev = 0
    union = set()
    auto = 0
    dup = 0
    for nid, n in nodos.items():
        s = n.get("nodos_siguientes") or []
        p = n.get("nodos_previos") or []
        sig += len(s); prev += len(p)
        if len(s) != len(set(s)): dup += 1
        if len(p) != len(set(p)): dup += 1
        for x in s:
            if x == nid: auto += 1
            union.add((nid, x))
        for x in p:
            if x == nid: auto += 1
            union.add((x, nid))
    return dict(ref=ref, nodos=total, vivos=total-deprecados, deprecados=deprecados,
                siguientes=sig, previos=prev, suma=sig+prev, union=len(union),
                auto=auto, listas_dup=dup), union

def sha_master(ref):
    if ref == "WORK":
        data = open("dataset/metadata/master_graph.json","rb").read()
    else:
        data = subprocess.run(["git","show",ref+":dataset/metadata/master_graph.json"],
                              capture_output=True, check=True).stdout
    return hashlib.sha256(data).hexdigest()

refs = sys.argv[1:]
uniones = {}
for r in refs:
    m, u = medir(r)
    uniones[r] = u
    m["sha256_master_graph"] = sha_master(r)
    print(json.dumps(m, ensure_ascii=False))
    with open("docs/loop/_auditor_v92_union_%s.txt" % r.replace("/","_"), "w", encoding="utf-8") as fh:
        for a,b in sorted(u):
            fh.write("%s -> %s\n" % (a,b))

if len(refs) == 2:
    a, b = refs
    borradas = sorted(uniones[a] - uniones[b])
    nuevas = sorted(uniones[b] - uniones[a])
    print("\n--- DIFF DE LA UNION %s -> %s ---" % (a,b))
    print("solo en %s (borradas): %d" % (a, len(borradas)))
    for x in borradas: print("   BORRADA: %s -> %s" % x)
    print("solo en %s (nuevas): %d" % (b, len(nuevas)))
    for x in nuevas: print("   NUEVA: %s -> %s" % x)
