import json, sys

g = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))
N = g['nodos']

dead_to_alive = {}
for nid, n in N.items():
    if n.get('deprecado'):
        continue
    for alias in n.get('ids_alias', []) or []:
        dead_to_alive[alias] = nid

def resolver(nid):
    seen = set()
    while nid in dead_to_alive and nid not in seen:
        seen.add(nid)
        nid = dead_to_alive[nid]
    return nid

def vecinos_reales(nid):
    n = N.get(nid)
    if not n:
        return None
    sal = set()
    for d in n.get('nodos_siguientes') or []:
        r = resolver(d)
        if r in N and not N[r].get('deprecado') and r != nid:
            sal.add(r)
    ent = set()
    for otro_id, otro in N.items():
        if otro.get('deprecado'):
            continue
        for s in otro.get('nodos_siguientes') or []:
            if resolver(s) == nid and otro_id != nid:
                ent.add(otro_id)
    return sal, ent

for nid in sys.argv[1:]:
    r = vecinos_reales(nid)
    if r is None:
        print(nid, 'NO EXISTE')
        continue
    sal, ent = r
    print('%s | deprecado=%s | salientes=%d entrantes=%d total=%d' % (
        nid, N[nid].get('deprecado', False), len(sal), len(ent), len(sal) + len(ent)))
    print('   salientes:', sorted(sal))
    print('   entrantes:', sorted(ent))
