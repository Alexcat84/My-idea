# -*- coding: utf-8 -*-
"""Vuelca los PASOS de un nodo, para la relectura ciega del auditor."""
import json, io, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for nid in sys.argv[1:]:
    p = os.path.join(RAIZ, 'dataset', 'nodos', nid + '.json')
    d = json.load(io.open(p, encoding='utf-8'))
    print('=' * 88)
    print('NODO', nid)
    print('titulo:', d.get('titulo_concepto'))
    print('fuente:', d.get('fuente'))
    print('resumen:', d.get('resumen_teorico'))
    print('PASOS ACCIONABLES:')
    for i, s in enumerate(d.get('pasos_accionables') or [], 1):
        print('  %d. %s' % (i, s))
    print('entregable:', d.get('entregable_esperado'))
    print()
