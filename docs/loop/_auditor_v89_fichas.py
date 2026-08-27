import json, sys
G = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))['nodos']
for nid in sys.argv[1:]:
    n = G[nid]
    print('='*78)
    print('ID:', nid, '| dominio:', n.get('dominio'), '| deprecado:', n.get('deprecado'))
    print('TITULO:', n.get('titulo_concepto'))
    print('FUENTE:', n.get('fuente'))
    print('RESUMEN:', (n.get('resumen_teorico') or '')[:900])
    print('PASOS:')
    for i, p in enumerate(n.get('pasos_accionables') or [], 1):
        print('  %d. %s' % (i, p))
    print('ENTREGABLE:', n.get('entregable_esperado'))
    print('SIGUIENTES:', n.get('nodos_siguientes'))
    print('PREVIOS:', n.get('nodos_previos'))
