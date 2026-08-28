# -*- coding: utf-8 -*-
"""Relectura ciega del auditor, vuelta 106.

Vuelca los DOS nodos enteros de cada par discutible (titulo, resumen,
entregable y TODOS los pasos, con el paso_casado marcado) SIN
direccion_leida, SIN razon, SIN correccion_v106 y SIN el veredicto de la
TAREA 4.4. El destape va en el fichero _reveal.txt y se lee DESPUES.
"""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

G = json.load(open('dataset/metadata/master_graph.json', encoding='utf-8'))
idx = G['nodos']

FILAS = {}
for f in ('docs/plan/OP_E_03_LECTURA_TRAMO3_V98.jsonl',
          'docs/plan/OP_E_03_LECTURA_TRAMO4_V99.jsonl'):
    for l in open(f, encoding='utf-8'):
        if l.strip():
            r = json.loads(l)
            FILAS[r['puesto_tramo']] = r

OBJETIVO = [int(x) for x in sys.argv[2:]]
MODO = sys.argv[1]

def volcar(n, rol, casado=None):
    print('  [%s] id=%s' % (rol, n.get('node_id')))
    print('    titulo   : %s' % n.get('titulo_concepto', ''))
    print('    dominio/fase: %s / %s' % (n.get('dominio'), n.get('fase_proyecto')))
    print('    resumen  : %s' % (n.get('resumen_teorico') or ''))
    print('    entregable: %s' % (n.get('entregable_esperado') or ''))
    pasos = n.get('pasos_accionables') or []
    for i, p in enumerate(pasos, 1):
        marca = '  <<< PASO CASADO' if casado == i else ''
        t = p if isinstance(p, str) else (p.get('texto') or json.dumps(p, ensure_ascii=False))
        print('    paso %d: %s%s' % (i, t, marca))
    print()

for pu in OBJETIVO:
    r = FILAS[pu]
    print('=' * 78)
    print('PUESTO %d   dominio=%s   clase=%s   paso_casado=%s' % (pu, r['dominio'], r['clase'], r['paso_casado']))
    print('=' * 78)
    volcar(idx[r['madre_de_la_bolsa']], 'MADRE', r['paso_casado'])
    volcar(idx[r['hijo_de_la_bolsa']], 'HIJO')
    if MODO == 'reveal':
        print('  --- DESTAPE ---')
        print('  direccion_leida: %s' % r.get('direccion_leida'))
        print('  razon: %s' % r.get('razon'))
        for k in r:
            if k.startswith('correccion_'):
                print('  %s: %s' % (k, json.dumps(r[k], ensure_ascii=False)))
        print()
