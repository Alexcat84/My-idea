import json, subprocess, sys, hashlib

def cargar(ref):
    if ref == 'WORK':
        b = open('dataset/metadata/master_graph.json','rb').read()
    else:
        b = subprocess.run(['git','show',f'{ref}:dataset/metadata/master_graph.json'],
                           capture_output=True).stdout
    return b, json.loads(b.decode('utf-8'))

def medir(ref):
    b, g = cargar(ref)
    sha = hashlib.sha256(b).hexdigest()
    nodos = g['nodes'] if isinstance(g, dict) and 'nodes' in g else g
    if isinstance(nodos, dict):
        items = list(nodos.items())
    else:
        items = [(n.get('id'), n) for n in nodos]
    total = len(items)
    vivos = sum(1 for _, n in items if not n.get('deprecated'))
    dep = total - vivos
    sig = sum(len(n.get('nodos_siguientes') or []) for _, n in items)
    prev = sum(len(n.get('nodos_previos') or []) for _, n in items)
    union = set()
    for i, n in items:
        for d in (n.get('nodos_siguientes') or []):
            union.add((i, d))
        for o in (n.get('nodos_previos') or []):
            union.add((o, i))
    return dict(ref=ref, sha=sha, total=total, vivos=vivos, dep=dep,
                sig=sig, prev=prev, suma=sig+prev, union=len(union)), union

for r in sys.argv[1:]:
    m, u = medir(r)
    print(m)

a, ua = medir(sys.argv[1])
b, ub = medir(sys.argv[2])
solo_a = ua - ub
solo_b = ub - ua
print('SOLO EN APERTURA (borradas):', len(solo_a))
for x in sorted(solo_a): print('   -', x)
print('SOLO EN CIERRE (nuevas):', len(solo_b))
for x in sorted(solo_b): print('   +', x)
print('DELTA sig/prev/suma/union:', b['sig']-a['sig'], b['prev']-a['prev'], b['suma']-a['suma'], b['union']-a['union'])
