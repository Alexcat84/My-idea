# -*- coding: utf-8 -*-
"""Vuelta 124, auditor: volcado CIEGO de las familias de OP-S-09.
NO lee docs/loop/SALIDA_V123_OPS09_LECTURA.jsonl."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')
G = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))
N = G['nodos']

def volcar(nid):
    n = N.get(nid)
    if n is None:
        print('  !! NO ENCONTRADO', nid); return
    print('  --- %s ---' % nid)
    print('    titulo: %s' % n.get('titulo_concepto'))
    print('    dominio: %s | fase: %s | deprecado: %s' % (n.get('dominio'), n.get('fase_proyecto'), n.get('deprecado')))
    print('    fuente: %s' % n.get('fuente'))
    print('    resumen: %s' % (n.get('resumen_teorico') or '')[:600])
    for i, p in enumerate(n.get('pasos_accionables') or [], 1):
        print('    paso %d: %s' % (i, p))
    print('    entregable: %s' % n.get('entregable_esperado'))
    print('    activacion: %s' % n.get('condiciones_activacion'))
    print('    etiqueta: %s' % n.get('etiqueta_arbol'))
    print('    n_prev %d n_sig %d' % (len(n.get('nodos_previos') or []), len(n.get('nodos_siguientes') or [])))

for f in json.loads(sys.argv[1]):
    print('===== FAMILIA: %s =====' % f[0])
    for nid in f[1]:
        volcar(nid)
    print()
