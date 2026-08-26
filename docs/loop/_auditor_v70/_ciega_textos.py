# -*- coding: utf-8 -*-
# CIEGA v70: imprime SOLO los nodos y sus textos pre fusion de los puestos
# pedidos. NO imprime la clase ni la razon del veredicto: eso se destapa
# despues, con _ciega_destapar.py.
import json, subprocess, sys

PUESTOS = [880, 2233, 2272, 2562, 2639, 279]

vs = {v['puesto_intra']: v for v in
      (json.loads(l) for l in open('docs/INTRA_DOMINIO_VEREDICTOS.jsonl', encoding='utf-8'))}
G = json.loads(subprocess.run(
    ['git', 'show', 'bf4f20f9:dataset/metadata/master_graph.json'],
    capture_output=True, text=True, encoding='utf-8').stdout)['nodos']

for p in PUESTOS:
    v = vs[p]
    print('=' * 78)
    print('PUESTO', p, '| dominio', v['dominio'])
    for lado in ('nodo_a', 'nodo_b'):
        nid = v[lado]
        n = G.get(nid)
        print('-' * 78)
        print(lado.upper(), ':', nid)
        if n is None:
            print('   (no esta en el grafo pre fusion)')
            continue
        print('   titulo :', n.get('titulo_concepto'))
        print('   fuente :', n.get('fuente'))
        print('   resumen:', (n.get('resumen_teorico') or '')[:500])
        for i, paso in enumerate(n.get('pasos_accionables') or [], 1):
            print('   paso %d: %s' % (i, paso))
        for i, c in enumerate(n.get('condiciones_activacion') or [], 1):
            print('   cond %d: %s' % (i, c))
    print()
