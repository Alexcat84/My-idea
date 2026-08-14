# Auditor vuelta 26: impresion cruda de pasos para la relectura ciega. Sin filtros.
import json, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ndir = os.path.join(BASE, 'dataset', 'nodos')
nodes = {}
for fn in os.listdir(ndir):
    if fn.endswith('.json'):
        with open(os.path.join(ndir, fn), encoding='utf-8') as f:
            nd = json.load(f)
        nodes[nd['node_id']] = nd

for nid in sys.argv[1:]:
    nd = nodes.get(nid)
    if nd is None:
        print(f"== {nid}: NO EXISTE ==")
        continue
    print("=" * 78)
    print(f"ID: {nid} | deprecado={bool(nd.get('deprecado'))}")
    print(f"TITULO: {nd.get('titulo_concepto')}")
    print(f"FUENTE: {nd.get('fuente')}")
    print(f"RESUMEN: {(nd.get('resumen_teorico') or '')[:400]}")
    pasos = nd.get('pasos_accionables') or []
    print(f"PASOS ({len(pasos)}):")
    for i, p in enumerate(pasos, 1):
        print(f"  {i}. {p}")
    print(f"ENTREGABLE: {nd.get('entregable_esperado')}")
    print()
