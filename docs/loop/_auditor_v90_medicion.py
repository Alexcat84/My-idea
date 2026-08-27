import json, hashlib, sys
p = 'dataset/metadata/master_graph.json'
G = json.load(open(p, encoding='utf-8'))
N = G['nodos']
items = list(N.items())
tot = len(items)
dep = sum(1 for _, n in items if n.get('deprecado'))
sig = sum(len(n.get('nodos_siguientes') or []) for _, n in items)
pre = sum(len(n.get('nodos_previos') or []) for _, n in items)
union = set()
for i, n in items:
    for d in (n.get('nodos_siguientes') or []): union.add((i, d))
    for o in (n.get('nodos_previos') or []): union.add((o, i))
print('censo total/vivos/deprecados:', tot, tot-dep, dep)
print('aristas sig/pre/suma/union:', sig, pre, sig+pre, len(union))
print('sha256 master_graph:', hashlib.sha256(open(p,'rb').read()).hexdigest())
print('auto-aristas:', sum(1 for a,b in union if a==b))
d = 0
for i,n in items:
    for c in ('nodos_siguientes','nodos_previos'):
        L = n.get(c) or []
        if len(L) != len(set(L)): d += 1
print('listas con duplicadas internas:', d)
# volcado de la union entera para diffs entre refs
out = sys.argv[1] if len(sys.argv) > 1 else None
if out:
    with open(out, 'w', encoding='utf-8') as f:
        for a,b in sorted(union):
            f.write(a + ' -> ' + b + '\n')
    print('union volcada en', out)
