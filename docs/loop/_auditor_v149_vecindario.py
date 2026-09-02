import json,subprocess,sys
def leer(ref):
    out=subprocess.run(["git","ls-tree","-r","--format=%(objectname) %(path)",ref,"dataset/nodos/"],capture_output=True,text=True,encoding="utf-8").stdout
    items=[l.split(" ",1) for l in out.splitlines() if l.strip()]
    p=subprocess.run(["git","cat-file","--batch"],input="\n".join(o for o,_ in items).encode(),capture_output=True)
    raw=p.stdout; pos=0; nodos={}
    for o,path in items:
        nl=raw.index(b"\n",pos); size=int(raw[pos:nl].split()[2])
        n=json.loads(raw[nl+1:nl+1+size].decode("utf-8")); pos=nl+1+size+1
        nodos[n["node_id"]]=n
    return nodos
def vecin(nodos):
    alias={a:k for k,v in nodos.items() for a in (v.get("ids_alias") or [])}
    def res(x):
        s=set()
        while x in alias and x not in s: s.add(x); x=alias[x]
        return x
    d={}
    for nid,n in nodos.items():
        for campo in ("nodos_previos","nodos_siguientes"):
            d[(nid,campo)]=frozenset(res(y) for y in (n.get(campo) or []))
    return d
A=vecin(leer(sys.argv[1])); B=vecin(leer(sys.argv[2]))
print("comparaciones nodo+campo antes:",len(A)," despues:",len(B))
claves=set(A)|set(B)
dif=[k for k in claves if A.get(k)!=B.get(k)]
print("vecindarios RESUELTOS distintos:",len(dif))
for k in dif[:5]: print("  ",k,"antes",len(A.get(k,())),"despues",len(B.get(k,())))
