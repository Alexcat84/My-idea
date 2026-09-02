import json,subprocess,sys
ref=sys.argv[1]
out=subprocess.run(["git","ls-tree","-r","--format=%(objectname) %(path)",ref,"dataset/nodos/"],capture_output=True,text=True,encoding="utf-8").stdout
items=[l.split(" ",1) for l in out.splitlines() if l.strip()]
p=subprocess.run(["git","cat-file","--batch"],input="\n".join(o for o,_ in items).encode(),capture_output=True)
raw=p.stdout; pos=0; nodos={}
for o,path in items:
    nl=raw.index(b"\n",pos); size=int(raw[pos:nl].split()[2])
    n=json.loads(raw[nl+1:nl+1+size].decode("utf-8")); pos=nl+1+size+1
    nodos[n["node_id"]]=n
# mapa alias -> canonico
alias={}
for nid,n in nodos.items():
    for a in (n.get("ids_alias") or []):
        alias[a]=nid
def res(x): 
    seen=set()
    while x in alias and x not in seen:
        seen.add(x); x=alias[x]
    return x
ndup=0; sobran=0; porcampo={}; pordom={}; tam={}
for nid,n in nodos.items():
    tiene=False
    for campo in ("nodos_siguientes","nodos_previos"):
        lst=n.get(campo) or []
        rs=[res(x) for x in lst]
        # excluye auto-arista (OP-S-07)
        grupos={}
        for i,r in enumerate(rs):
            if r==nid: continue
            grupos.setdefault(r,[]).append(lst[i])
        for r,g in grupos.items():
            if len(g)>1:
                tiene=True; s=len(g)-1; sobran+=s
                porcampo[campo]=porcampo.get(campo,0)+s
                pordom[n.get("dominio","?")]=pordom.get(n.get("dominio","?"),0)+s
                tam[len(g)-1]=tam.get(len(g)-1,0)+1
    if tiene: ndup+=1
print(f"{ref}: nodos con dup (tras resolver) = {ndup} | entradas que sobran = {sobran}")
print("  por campo:",porcampo)
print("  por dominio:",dict(sorted(pordom.items(),key=lambda k:-k[1])))
print("  por tamano (de mas):",dict(sorted(tam.items())))
