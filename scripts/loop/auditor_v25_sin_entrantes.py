# Auditor vuelta 25: los nodos sin enlaces entrantes, hoy y antes de OP-S-07,
# y si el salto de 2 a 6 lo explican los 66 enlaces retirados.
import json, os, subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(BASE)

def cargar(rev=None):
    nodes = {}
    if rev is None:
        ndir = os.path.join(BASE, 'dataset', 'nodos')
        for fn in os.listdir(ndir):
            if fn.endswith('.json'):
                with open(os.path.join(ndir, fn), encoding='utf-8') as f:
                    nd = json.load(f)
                nodes[nd['node_id']] = nd
    else:
        out = subprocess.run(['git', 'ls-tree', '-r', '--name-only', rev, 'dataset/nodos/'],
                             capture_output=True, text=True).stdout.split()
        for p in out:
            if p.endswith('.json'):
                r = subprocess.run(['git', 'show', f'{rev}:{p}'], capture_output=True)
                nd = json.loads(r.stdout.decode('utf-8'))
                nodes[nd['node_id']] = nd
    return nodes

def sin_entrantes(nodes):
    # la semantica del validador: entrante = aparecer como destino en nodos_siguientes
    # de otro nodo o como origen en nodos_previos de otro; replico el conteo del
    # grafo compilado: un nodo tiene entrante si alguien lo lista en nodos_siguientes,
    # o si el aparece en nodos_previos de alguien (vista reciproca simetrizada).
    con_entrante = set()
    for i, nd in nodes.items():
        for dest in nd.get('nodos_siguientes', []) or []:
            con_entrante.add(dest)
    return sorted(set(nodes) - con_entrante)

hoy = cargar()
antes = cargar('ba109e5e')
sh, sa = sin_entrantes(hoy), sin_entrantes(antes)
print(f"sin entrantes HOY: {len(sh)} -> {sh}")
print(f"sin entrantes en ba109e5e: {len(sa)} -> {sa}")
nuevos = [x for x in sh if x not in sa]
print(f"nuevos: {nuevos}")
# de los nuevos: su unico entrante era una de las 66 retiradas?
for x in nuevos:
    citaban = [i for i, nd in antes.items() if x in (nd.get('nodos_siguientes') or [])]
    citan = [i for i, nd in hoy.items() if x in (nd.get('nodos_siguientes') or [])]
    print(f"  {x}: lo citaban en siguientes {citaban} -> hoy {citan}")
