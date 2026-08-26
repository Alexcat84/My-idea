import json,sys
G=json.load(open('dataset/metadata/master_graph.json',encoding='utf-8'))['nodos']
for nid in sys.argv[1:]:
    n=G.get(nid)
    if not n: print("NO EXISTE:",nid); continue
    print("="*78)
    print("ID:",nid,"| deprecado:",bool(n.get('deprecado')),"| dominio:",n.get('dominio'),"| fase:",n.get('fase_proyecto'))
    print("TITULO:",n.get('titulo_concepto'))
    print("FUENTE:",n.get('fuente'))
    print("RESUMEN:",(n.get('resumen_teorico') or '')[:900])
    print("PASOS:")
    for i,p in enumerate(n.get('pasos_accionables') or [],1): print(f"  {i}. {p}")
    print("SIGUIENTES(",len(n.get('nodos_siguientes') or []),"):",n.get('nodos_siguientes'))
    print("PREVIOS(",len(n.get('nodos_previos') or []),"):",n.get('nodos_previos'))
