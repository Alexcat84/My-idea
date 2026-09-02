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
alias={a:k for k,v in nodos.items() for a in (v.get("ids_alias") or [])}
def res(x):
    s=set()
    while x in alias and x not in s: s.add(x); x=alias[x]
    return x
ndup=0;sobran=0;porcampo={};pordom={};motivo={}
for nid,n in nodos.items():
    if n.get("deprecado"): continue
    tocado=False
    for campo in ("nodos_previos","nodos_siguientes"):
        L=n.get(campo) or []; grupos={}
        for y in L:
            d=res(y)
            if d==nid: continue
            grupos.setdefault(d,[]).append(y)
        for d,orig in grupos.items():
            if len(orig)<2: continue
            s=len(orig)-1; sobran+=s; tocado=True
            porcampo[campo]=porcampo.get(campo,0)+s
            pordom[n.get("dominio") or "?"]=pordom.get(n.get("dominio") or "?",0)+s
            k="el id nuevo mas su alias" if d in orig else "dos alias del mismo destino"
            motivo[k]=motivo.get(k,0)+s
    if tocado: ndup+=1
print(f"{ref}  VIVOS: nodos con dup={ndup}  entradas que sobran={sobran}")
print("   por campo:",porcampo)
print("   por motivo:",motivo)
print("   por dominio:",dict(sorted(pordom.items(),key=lambda k:-k[1])))
