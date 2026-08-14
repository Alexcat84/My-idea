# Auditor vuelta 25: recomputo independiente del marcador y del grafo (14 ago 2026)
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
print(f"  A={clases.get('A',0)} B={clases.get('B',0)} C={clases.get('C',0)} D={clases.get('D',0)}")
print(f"  tasa A={clases.get('A',0)/n*100:.1f}%")

# por dominio
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
enlaces = sum(len(nd.get('nodos_previos', [])) + len(nd.get('nodos_siguientes', [])) for nd in nodes.values())
claves = set()
for nd in nodes.values():
    claves.update(nd.keys())
print(f"\nGRAFO: nodos={len(nodes)} vivos={len(vivos)} deprecados={len(deps)} enlaces={enlaces} claves={len(claves)}")
print(f"  claves: {sorted(claves)}")

# 3) resolutor (copia de mapaDeAlias/resolverId)
alias = {}
for i, nd in nodes.items():
    for a in nd.get('ids_alias', []) or []:
        alias[a] = i

def resolver(x):
    return alias.get(x, x)

auto_vivos = []
for i, nd in vivos.items():
    for campo in ('nodos_previos', 'nodos_siguientes'):
        for dest in nd.get(campo, []) or []:
            if resolver(dest) == i:
                auto_vivos.append(f"{i}.{campo}->{dest}")
print(f"\nAUTO-ARISTAS de vivos tras resolver: {len(auto_vivos)}")
for a in auto_vivos[:10]:
    print('  ', a)

# 4) alias-contra-alias inertes en deprecados (enlaces de deprecados que resuelven a deprecados o entre alias)
# la letra: 48 alias contra alias en 33 nodos deprecados intactas
dep_enl = 0
dep_nodos = set()
for i, nd in deps.items():
    for campo in ('nodos_previos', 'nodos_siguientes'):
        for dest in nd.get(campo, []) or []:
            dep_enl += 1
            dep_nodos.add(i)
print(f"\nENLACES restantes en nodos deprecados: {dep_enl} en {len(dep_nodos)} nodos")

# 4b) las 48 alias-contra-alias inertes: enlaces de nodos DEPRECADOS-alias cuyo destino
#     es a su vez un id alias (deprecado), sin tocar por OP-S-07
alias_dep = {a for a in alias}  # ids que son alias de algun vivo
inertes = []
lit_al_vivo = []
for i, nd in deps.items():
    if i not in alias_dep:
        continue
    twin = alias[i]
    for campo in ('nodos_previos', 'nodos_siguientes'):
        for dest in nd.get(campo, []) or []:
            if dest == twin:
                lit_al_vivo.append(f"{i}.{campo}->{dest}")
            elif dest in alias_dep:
                inertes.append((i, campo, dest))
print(f"\nINERTES alias-contra-alias hoy: {len(inertes)} en {len(set(x[0] for x in inertes))} nodos")
print(f"RECIPROCAS literales al gemelo vivo que QUEDAN (deberian ser 0): {len(lit_al_vivo)}")

# 5) symmetrize_added en phase1_run_log.json
logp = os.path.join(BASE, 'dataset', 'metadata', 'phase1_run_log.json')
with open(logp, encoding='utf-8') as f:
    plog = json.load(f)
sym = plog.get('symmetrize_added', None)
if sym is None:
    # buscar anidado
    def find(o, k):
        if isinstance(o, dict):
            if k in o:
                return o[k]
            for v in o.values():
                r = find(v, k)
                if r is not None:
                    return r
        if isinstance(o, list):
            for v in o:
                r = find(v, k)
                if r is not None:
                    return r
        return None
    sym = find(plog, 'symmetrize_added')
print(f"\nsymmetrize_added: {len(sym) if isinstance(sym, list) else sym}")

# 6) OPERACIONES.jsonl
opath = os.path.join(BASE, 'docs', 'plan', 'OPERACIONES.jsonl')
ops = []
with open(opath, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            ops.append(json.loads(line))
ids = [o['id_op'] for o in ops]
print(f"\nOPERACIONES: {len(ops)} ids_unicos={len(set(ids))}")
est = {}
fases = {}
for o in ops:
    est[o.get('estado')] = est.get(o.get('estado'), 0) + 1
    fases[o.get('fase')] = fases.get(o.get('fase'), 0) + 1
print(f"  estados: {est}")
print(f"  fases: {dict(sorted(fases.items()))}")
idset = set(ids)
rotas = [(o['id_op'], d) for o in ops for d in (o.get('depende_de') or []) if d not in idset]
print(f"  dependencias rotas: {len(rotas)} {rotas[:5]}")

# 7) el nodo del choque: en cuantas operaciones aparece
target = 'background_startup_vs_corporativo'
en_ops = [o['id_op'] for o in ops if target in json.dumps(o.get('nodos', []))]
print(f"\n{target} aparece en operaciones: {en_ops}")

# 8) los siete de OP-F-01: pasos hoy
siete = ['seleccion_representante_extranjero', 'internacionalizacion_sitio_web_exportacion',
         'elaboracion_pro_forma_invoice', 'elementos_plan_exportacion_ejemplo',
         'principios_medicion_efectiva', 'fmea_analisis_de_modos_de_falla',
         'background_startup_vs_corporativo']
print("\nPASOS de los siete de OP-F-01:")
for s in siete:
    nd = nodes.get(s)
    if nd is None:
        print(f"  {s}: NO EXISTE")
    else:
        pasos = nd.get('pasos_accionables') or []
        print(f"  {s}: {len(pasos)} pasos, status={nd.get('status','vivo')}")

# 9) los tres de OP-F-02
tres = ['future_scenarios_planning', 'gut_check', 'brainstorming_divergente']
print("\nLOS TRES de OP-F-02 (pasos y fuente):")
for s in tres:
    nd = nodes.get(s)
    if nd is None:
        print(f"  {s}: NO EXISTE")
    else:
        pasos = nd.get('pasos_accionables') or []
        fu = nd.get('fuente', '')
        print(f"  {s}: {len(pasos)} pasos, fuente={fu!r:.120}")
