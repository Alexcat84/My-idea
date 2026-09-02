import json,subprocess,sys
ref=sys.argv[1]
out=subprocess.run(["git","ls-tree","-r","--format=%(objectname) %(path)",ref,"dataset/nodos/"],capture_output=True,text=True,encoding="utf-8").stdout
items=[l.split(" ",1) for l in out.splitlines() if l.strip()]
p=subprocess.run(["git","cat-file","--batch"],input="\n".join(o for o,_ in items).encode(),capture_output=True)
raw=p.stdout; pos=0
nodos_con_dup=0; entradas_sobran=0; por_campo={}
for o,path in items:
    nl=raw.index(b"\n",pos); size=int(raw[pos:nl].split()[2])
    n=json.loads(raw[nl+1:nl+1+size].decode("utf-8")); pos=nl+1+size+1
    tiene=False
    for campo in ("nodos_siguientes","nodos_previos"):
        lst=n.get(campo) or []
        sobra=len(lst)-len(set(lst))
        if sobra:
            tiene=True; entradas_sobran+=sobra
            por_campo[campo]=por_campo.get(campo,0)+sobra
    if tiene: nodos_con_dup+=1
print(f"{ref}: nodos con al menos una duplicada = {nodos_con_dup} | entradas que sobran = {entradas_sobran} | por campo = {por_campo}")
