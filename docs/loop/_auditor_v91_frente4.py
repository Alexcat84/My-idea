# -*- coding: utf-8 -*-
"""VARA PROPIA DEL AUDITOR, VUELTA 91, discutible 4: el frente 4 del dedupe de
OP-E-07 (13 quitados), recomputado por mi sobre el grafo de APERTURA, con mi
propia lectura de la cosecha y sin usar el script del ejecutor."""
import io, json, sys
COSECHA = 'docs/plan/COSECHA_RAZONES_D.jsonl'
G = json.load(io.open(sys.argv[1], encoding='utf-8'))['nodos']
ALIAS = {a: k for k, v in G.items() for a in (v.get('ids_alias') or []) if a != k}
def res(x):
    visto = set()
    while x in ALIAS and x not in visto:
        visto.add(x); x = ALIAS[x]
    return x
# union de aristas del grafo, resuelta por alias, NO dirigida
U = set()
for i, n in G.items():
    for d in (n.get('nodos_siguientes') or []): U.add(tuple(sorted((res(i), res(d)))))
    for o in (n.get('nodos_previos') or []): U.add(tuple(sorted((res(o), res(i)))))
bolsa = []
for l in io.open(COSECHA, encoding='utf-8'):
    l = l.strip()
    if not l: continue
    d = json.loads(l)
    if d.get('nuevo') is True and d.get('senales') == ['continua por la vara']:
        bolsa.append(d)
print('bolsa de la ficha (nuevo + solo "continua por la vara"):', len(bolsa))
rep = {}
for d in bolsa: rep[d['dominio']] = rep.get(d['dominio'], 0) + 1
print('reparto por dominio:', dict(sorted(rep.items())))
quitados, quedan = [], []
for d in bolsa:
    a, b = res(d['nodo_a']), res(d['nodo_b'])
    if tuple(sorted((a, b))) in U: quitados.append((d['puesto'], d['nodo_a'], d['nodo_b'], a, b))
    else: quedan.append(d['puesto'])
print()
print('FRENTE 4 (arista ya en el grafo resolviendo por alias) QUITA:', len(quitados))
for p, na, nb, a, b in sorted(quitados): print('   puesto %-6s %s / %s   (resuelto %s / %s)' % (p, na, nb, a, b))
print()
print('QUEDAN:', len(quedan))
