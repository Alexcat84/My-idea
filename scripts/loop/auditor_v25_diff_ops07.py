# Auditor vuelta 25: verificacion del diff de OP-S-07 (commit 82ee608a contra ba109e5e)
# y particion de las 48 inertes con el criterio de la letra (alias hacia OTRO alias
# del MISMO superviviente).
import json, os, subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(BASE)

ANTES, DESPUES = 'ba109e5e', '82ee608a'

def show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], capture_output=True)
    if r.returncode != 0:
        return None
    return json.loads(r.stdout.decode('utf-8'))

files = subprocess.run(['git', 'diff', '--name-only', ANTES, DESPUES, '--', 'dataset/nodos/'],
                       capture_output=True, text=True).stdout.split()
print(f"ficheros de dataset/nodos tocados por {DESPUES}: {len(files)}")

quitados = []
otros_campos = []
anadidos = []
for p in files:
    a = show(ANTES, p)
    b = show(DESPUES, p)
    for k in set(a) | set(b):
        va, vb = a.get(k), b.get(k)
        if va == vb:
            continue
        if k in ('nodos_previos', 'nodos_siguientes'):
            sa, sb = list(va or []), list(vb or [])
            for x in sa:
                if sa.count(x) > sb.count(x):
                    for _ in range(sa.count(x) - sb.count(x)):
                        quitados.append((a['node_id'], k, x))
            for x in sb:
                if sb.count(x) > sa.count(x):
                    anadidos.append((a['node_id'], k, x))
        else:
            otros_campos.append((p, k))

print(f"entradas RETIRADAS de previos/siguientes: {len(quitados)}")
print(f"entradas ANADIDAS: {len(anadidos)}")
print(f"OTROS campos tocados: {len(otros_campos)} {otros_campos[:5]}")

# clasificacion de las 66: vivas (nodo vivo, dest resuelve al propio) vs reciprocas del gemelo
nodes = {}
ndir = os.path.join(BASE, 'dataset', 'nodos')
for fn in os.listdir(ndir):
    if fn.endswith('.json'):
        with open(os.path.join(ndir, fn), encoding='utf-8') as f:
            nd = json.load(f)
        nodes[nd['node_id']] = nd
alias = {}
for i, nd in nodes.items():
    for a2 in nd.get('ids_alias', []) or []:
        alias[a2] = i

vivas = [q for q in quitados if not nodes[q[0]].get('deprecado') and alias.get(q[2], q[2]) == q[0]]
recip = [q for q in quitados if nodes[q[0]].get('deprecado')]
otras = [q for q in quitados if q not in vivas and q not in recip]
print(f"  de nodo VIVO que resolvia a si mismo: {len(vivas)} en {len(set(q[0] for q in vivas))} nodos")
print(f"  reciprocas en gemelo DEPRECADO: {len(recip)} en {len(set(q[0] for q in recip))} nodos")
print(f"  otras (no clasifican): {len(otras)} {otras[:5]}")
# las reciprocas: el deprecado citaba a su superviviente literal
recip_ok = [q for q in recip if alias.get(q[0]) == q[2]]
print(f"  reciprocas que citaban LITERAL a su superviviente: {len(recip_ok)} de {len(recip)}")

# 48 inertes con el criterio de la letra: en deprecados, dest es OTRO alias del MISMO superviviente
inertes = []
for i, nd in nodes.items():
    if not nd.get('deprecado') or i not in alias:
        continue
    surv = alias[i]
    for campo in ('nodos_previos', 'nodos_siguientes'):
        for dest in nd.get(campo, []) or []:
            if dest != surv and alias.get(dest) == surv:
                inertes.append((i, campo, dest))
print(f"\nINERTES (criterio letra: alias hacia OTRO alias del MISMO superviviente): "
      f"{len(inertes)} en {len(set(x[0] for x in inertes))} nodos")

# el peor: costo_de_mala_calidad_copq, retiradas 2 previos + 5 siguientes
peor = [q for q in quitados if q[0] == 'costo_de_mala_calidad_copq']
prev = sum(1 for q in peor if q[1] == 'nodos_previos')
sig = sum(1 for q in peor if q[1] == 'nodos_siguientes')
print(f"\nel peor, costo_de_mala_calidad_copq: retiradas {len(peor)} ({prev} previos, {sig} siguientes)")

# ejemplar
ej = [q for q in quitados if q[0] == 'analisis_flujo_de_valor' and q[2] == 'value_stream_analysis_lean']
print(f"ejemplar analisis_flujo_de_valor -> value_stream_analysis_lean retirado: {len(ej) == 1}")

# conteo de aristas antes y despues del commit
def total_links(rev):
    out = subprocess.run(['git', 'ls-tree', '-r', '--name-only', rev, 'dataset/nodos/'],
                        capture_output=True, text=True).stdout.split()
    t = 0
    for p in out:
        if p.endswith('.json'):
            nd = show(rev, p)
            t += len(nd.get('nodos_previos', []) or []) + len(nd.get('nodos_siguientes', []) or [])
    return t
ta, tb = total_links(ANTES), total_links(DESPUES)
print(f"\nconteo de aristas: {ANTES}={ta} -> {DESPUES}={tb} (baja {ta-tb})")
