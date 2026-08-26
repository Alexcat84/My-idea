# Sonda del auditor de la vuelta 72: marcador propio sobre el archivo de
# veredictos (n, huecos, duplicados, A/B/C/D y tasa por dominio) y conteo de
# enlaces, vivos y deprecados sobre master_graph. Solo lee.
import json, collections

vs = [json.loads(l) for l in open('docs/INTRA_DOMINIO_VEREDICTOS.jsonl', encoding='utf-8')]
puestos = [v['puesto_intra'] for v in vs]
n = len(vs)
dup = n - len(set(puestos))
huecos = sorted(set(range(1, max(puestos) + 1)) - set(puestos))
clases = collections.Counter(v['clase'] for v in vs)
print('n', n, 'max', max(puestos), 'duplicados', dup, 'huecos', len(huecos), huecos[:5])
print('marcador A/B/C/D:', clases.get('A', 0), clases.get('B', 0), clases.get('C', 0), clases.get('D', 0))
print('otras clases:', {k: c for k, c in clases.items() if k not in 'ABCD'})

dom = collections.defaultdict(lambda: [0, 0])
for v in vs:
    d = v.get('dominio') or '?'
    dom[d][0] += 1
    if v['clase'] == 'A':
        dom[d][1] += 1
print('\ntasa por dominio:')
for d in sorted(dom):
    p, a = dom[d]
    print('  %-18s pares %5d  A %4d  tasa %.1f' % (d, p, a, 100.0 * a / p))

g = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']
vivos = [i for i, nn in g.items() if not nn.get('deprecado')]
dep = [i for i, nn in g.items() if nn.get('deprecado')]
prev = sum(len(nn.get('nodos_previos') or []) for nn in g.values())
sig = sum(len(nn.get('nodos_siguientes') or []) for nn in g.values())
print('\ngrafo: ficheros', len(g), 'vivos', len(vivos), 'deprecados', len(dep))
print('enlaces: previos', prev, 'siguientes', sig, 'total', prev + sig)
