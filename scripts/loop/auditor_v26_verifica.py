# Auditor vuelta 26: recomputo independiente del marcador, el grafo, las operaciones
# de fuente, el muro del indice semantico y la aritmetica de OP-F-01 (14 ago 2026)
import json, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1) MARCADOR desde INTRA_DOMINIO_VEREDICTOS.jsonl
vpath = os.path.join(BASE, 'docs', 'INTRA_DOMINIO_VEREDICTOS.jsonl')
rows = []
with open(vpath, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))
puestos = [r['puesto_intra'] for r in rows]
clases = {}
for r in rows:
    clases[r['clase']] = clases.get(r['clase'], 0) + 1
n = len(rows)
huecos = sorted(set(range(1, max(puestos) + 1)) - set(puestos)) if puestos else []
dups = n - len(set(puestos))
fuera = [c for c in clases if c not in 'ABCD']
print(f"MARCADOR: n={n} max_puesto={max(puestos)} huecos={len(huecos)} dup={dups} fuera_ABCD={fuera}")
print(f"  A={clases.get('A',0)} ({clases.get('A',0)/n*100:.1f}%) B={clases.get('B',0)} ({clases.get('B',0)/n*100:.1f}%) "
      f"C={clases.get('C',0)} ({clases.get('C',0)/n*100:.1f}%) D={clases.get('D',0)} ({clases.get('D',0)/n*100:.1f}%)")
doms = {}
for r in rows:
    d = r.get('dominio', '?')
    doms.setdefault(d, {'n': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0})
    doms[d]['n'] += 1
    doms[d][r['clase']] += 1
for d in sorted(doms, key=lambda x: -doms[x]['n']):
    v = doms[d]
    print(f"  {d}: n={v['n']} A={v['A']} ({v['A']/v['n']*100:.1f}%) B={v['B']} C={v['C']} D={v['D']}")

# 2) GRAFO desde dataset/nodos
ndir = os.path.join(BASE, 'dataset', 'nodos')
nodes = {}
for fn in os.listdir(ndir):
    if fn.endswith('.json'):
        with open(os.path.join(ndir, fn), encoding='utf-8') as f:
            nd = json.load(f)
        nodes[nd['node_id']] = nd
vivos = {i: nd for i, nd in nodes.items() if not nd.get('deprecado')}
deps = {i: nd for i, nd in nodes.items() if nd.get('deprecado')}
enlaces = sum(len(nd.get('nodos_previos', []) or []) + len(nd.get('nodos_siguientes', []) or []) for nd in nodes.values())
claves = set()
for nd in nodes.values():
    claves.update(nd.keys())
print(f"\nGRAFO: nodos={len(nodes)} vivos={len(vivos)} deprecados={len(deps)} enlaces={enlaces} claves={len(claves)}")

# auto-aristas de vivos tras resolver
alias = {}
for i, nd in nodes.items():
    for a in nd.get('ids_alias', []) or []:
        alias[a] = i
auto_vivos = []
for i, nd in vivos.items():
    for campo in ('nodos_previos', 'nodos_siguientes'):
        for dest in nd.get(campo, []) or []:
            if alias.get(dest, dest) == i:
                auto_vivos.append(f"{i}.{campo}->{dest}")
print(f"AUTO-ARISTAS de vivos tras resolver: {len(auto_vivos)}")

# 3) OPERACIONES
opath = os.path.join(BASE, 'docs', 'plan', 'OPERACIONES.jsonl')
ops = []
with open(opath, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            ops.append(json.loads(line))
ids = [o['id_op'] for o in ops]
est = {}
for o in ops:
    est[o.get('estado')] = est.get(o.get('estado'), 0) + 1
idset = set(ids)
rotas = [(o['id_op'], d) for o in ops for d in (o.get('depende_de') or []) if d not in idset]
print(f"\nOPERACIONES: {len(ops)} ids_unicos={len(set(ids))} estados={est} dependencias_rotas={len(rotas)}")

byid = {o['id_op']: o for o in ops}

# 4) OP-F-01: nomina de SEIS, sin background_startup_vs_corporativo, y sus pasos hoy
f01 = byid['OP-F-01']
print(f"\nOP-F-01 nodos ({len(f01.get('nodos', []))}): {f01.get('nodos')}")
target = 'background_startup_vs_corporativo'
en_ops = [o['id_op'] for o in ops if target in (o.get('nodos') or [])]
print(f"{target} en campo nodos de: {en_ops}")
print("PASOS de los seis de OP-F-01 hoy:")
for s in f01.get('nodos', []):
    nd = nodes.get(s)
    if nd is None:
        print(f"  {s}: NO EXISTE")
    else:
        print(f"  {s}: {len(nd.get('pasos_accionables') or [])} pasos, deprecado={bool(nd.get('deprecado'))}")

# 5) aritmetica de las operaciones de fuente
fuente_ops = ['OP-F-01', 'OP-F-02', 'OP-F-03', 'OP-F-04-HOR', 'OP-F-04-COL', 'OP-F-04-WEI', 'OP-F-04-RAC']
grupo_a = set()
for oid in ['OP-F-01', 'OP-F-02', 'OP-F-03']:
    grupo_a.update(byid[oid].get('nodos') or [])
grupo_b = set()
for oid in ['OP-F-04-HOR', 'OP-F-04-COL', 'OP-F-04-WEI', 'OP-F-04-RAC']:
    grupo_b.update(byid[oid].get('nodos') or [])
todas = set()
suma_bruta = 0
for oid in fuente_ops:
    nn = byid[oid].get('nodos') or []
    suma_bruta += len(nn)
    todas.update(nn)
print(f"\nARITMETICA fuente: |F01|={len(byid['OP-F-01'].get('nodos') or [])} "
      f"|F02|={len(byid['OP-F-02'].get('nodos') or [])} |F03|={len(byid['OP-F-03'].get('nodos') or [])} "
      f"grupo F01+F02+F03 distintos={len(grupo_a)}")
print(f"  las siete: suma_bruta={suma_bruta} distintos={len(todas)} | tanda OP-F-04 distintos={len(grupo_b)} "
      f"| solape entre grupos={len(grupo_a & grupo_b)}")

# 6) operaciones que piden crear nodo (texto de la operacion)
crean = []
for o in ops:
    blob = json.dumps(o, ensure_ascii=False).lower()
    if 'nodo propio' in blob or 'nodo nuevo' in blob or 'crear nodo' in blob or 'crea nodo' in blob:
        crean.append(o['id_op'])
print(f"\nOPERACIONES cuyo texto nombra crear nodo / nodo propio ({len(crean)}): {crean}")

# 7) OP-F-04-HOR: sus 13 vivos, y la familia Horowitz por fuente
hor = byid['OP-F-04-HOR']
nn = hor.get('nodos') or []
muertos = [s for s in nn if s not in nodes or nodes[s].get('deprecado')]
print(f"\nOP-F-04-HOR: {len(nn)} nodos, muertos_o_ausentes={muertos}")
fuentes_hor = {}
for i, nd in vivos.items():
    fu = (nd.get('fuente') or '')
    if 'Hard Thing' in fu or 'Horowitz' in fu:
        fuentes_hor[i] = fu
solo = [i for i, fu in fuentes_hor.items() if ' + ' not in fu]
combi = [i for i, fu in fuentes_hor.items() if ' + ' in fu]
print(f"familia Horowitz entre vivos: {len(fuentes_hor)} total, fuente_unica={len(solo)}, con_otro_libro={len(combi)}")
print(f"  ejemplos de fuente combinada: {sorted(combi)[:5]}")
print(f"  valores distintos de fuente unica: {sorted(set(fuentes_hor[i] for i in solo))}")

# 8) el muro: indice semantico y credencial
idx_path = os.path.join(BASE, 'web', 'lib', 'assets', 'semantic_index.json')
with open(idx_path, encoding='utf-8') as f:
    idx = json.load(f)
ids_idx = set(idx.get('ids') or [])
activos = set(vivos)
print(f"\nINDICE SEMANTICO: modelo={idx.get('model') or idx.get('modelo')} dim={idx.get('dim') or idx.get('dimension')} "
      f"ids={len(ids_idx)}")
print(f"  activos sin vector={len(activos - ids_idx)} vectores sobrantes={len(ids_idx - activos)}")
print(f"VOYAGE_API_KEY en entorno: {'SI' if os.environ.get('VOYAGE_API_KEY') else 'NO'}")
print(f".env en la raiz: {'SI' if os.path.exists(os.path.join(BASE, '.env')) else 'NO'}")

# 9) los dos nodos tocados: su fuente hoy
for s in ['gestion_libro_abierto_obm', 'seleccion_estrategia_pricing']:
    nd = nodes.get(s)
    print(f"\n{s}: fuente={nd.get('fuente')!r} pasos={len(nd.get('pasos_accionables') or [])} "
          f"deprecado={bool(nd.get('deprecado'))}")

# 10) los tres de OP-F-02: pasos y fuente hoy (deben estar intactos)
print("\nLOS TRES de OP-F-02 hoy:")
for s in ['future_scenarios_planning', 'gut_check', 'brainstorming_divergente']:
    nd = nodes.get(s)
    print(f"  {s}: {len(nd.get('pasos_accionables') or [])} pasos, fuente={nd.get('fuente')!r}")
