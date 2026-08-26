import json,sys
def load(p):
    G=json.load(open(p,encoding='utf-8'))['nodos']
    s=set(); pv=set()
    for nid,n in G.items():
        for d in (n.get('nodos_siguientes') or []): s.add((nid,d))
        for d in (n.get('nodos_previos') or []): pv.add((nid,d))
    return s,pv
a_s,a_p=load(sys.argv[1]); b_s,b_p=load(sys.argv[2])
print("== nodos_siguientes ==")
print("nuevas:",len(b_s-a_s)," borradas:",len(a_s-b_s))
for e in sorted(a_s-b_s): print("  BORRADA:",e[0],"->",e[1])
print("== nodos_previos ==")
print("nuevas:",len(b_p-a_p)," borradas:",len(a_p-b_p))
for e in sorted(a_p-b_p): print("  BORRADA(prev):",e[0],"<-",e[1])
# reciprocidad de las nuevas
nn=b_s-a_s
falt=[e for e in nn if (e[1],e[0]) not in b_p]
print("nuevas de siguientes sin su reciproca en previos:",len(falt))
for e in sorted(nn): print("  NUEVA:",e[0],"->",e[1])
