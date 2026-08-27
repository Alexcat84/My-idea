import json, io, sys
G = json.load(io.open('dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']
B = {}
for l in io.open('docs/plan/OP_E_06_REBASE_V90.jsonl', encoding='utf-8'):
    if l.strip():
        f = json.loads(l); B[f['puesto']] = f
def ficha(i):
    n = G.get(i)
    if not n: return '   (no existe)'
    out = ['   titulo: ' + str(n.get('titulo_concepto')), '   dominio: ' + str(n.get('dominio')), '   deprecado: ' + str(n.get('deprecado'))]
    ps = n.get('pasos') or n.get('pasos_accionables') or []
    for k, p in enumerate(ps, 1):
        t = p if isinstance(p, str) else (p.get('texto') or p.get('descripcion') or json.dumps(p, ensure_ascii=False))
        out.append('   paso %d: %s' % (k, t))
    return '\n'.join(out)
for arg in sys.argv[1:]:
    p = int(arg); f = B[p]
    print('=' * 90)
    print('PUESTO %d  (%s)' % (p, f['dominio']))
    print('NODO A: %s' % f['nodo_a']); print(ficha(f['nodo_a']))
    print('-' * 90)
    print('NODO B: %s' % f['nodo_b']); print(ficha(f['nodo_b']))
