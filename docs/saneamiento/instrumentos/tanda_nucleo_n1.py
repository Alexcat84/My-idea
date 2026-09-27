# -*- coding: utf-8 -*-
"""Nivel 1, criterio 6: cada raiz de los nodos del nucleo sin camino por el nucleo recibe el predecesor del nucleo que
eligio la pasada N (dos lectores ciegos, arbitro en los desacuerdos). Una eleccion que formaria un par de ida y vuelta
con una arista existente se rechaza aqui y se lista (Gate 0 exige cita a cada par bidireccional).
Uso: python tanda_nucleo_n1.py <repo> <resultado N> <claves N>"""
import io
import json
import os
import sys

REPO, RES, CLAVES = sys.argv[1], sys.argv[2], sys.argv[3]
os.chdir(REPO)
res = json.load(io.open(RES, encoding='utf-8'))
claves = json.load(io.open(CLAVES, encoding='utf-8'))
ops, pares = [], []
for x in sorted(res, key=lambda x: x['id']):
    t, e = claves[x['id']]['punta'], x['eleccion']
    if e == 'NINGUNO':
        raise SystemExit('%s sin predecesor' % x['id'])
    assert e in claves[x['id']]['candidatos'], (x['id'], e)
    nt = json.load(io.open('dataset/nodos/%s.json' % t, encoding='utf-8'))
    if e in (nt.get('nodos_siguientes') or []):
        pares.append((x['id'], e, t))
        continue
    ops.append({'id': 'n1-nucleo-%02d' % (len(ops) + 1), 'operacion': 'TEJER', 'desde': e, 'hacia': t,
                'motivo': x['nota'].replace(chr(0x2014), ',').replace(chr(0x2013), '-'),
                'evidencia': 'Pasada N del saneamiento (%s, %s): raiz de %d nodos del nucleo sin camino por el nucleo.' % (
                    x['id'], x['decidido_por'], 1 + len(claves[x['id']]['cuelgan'])),
                'decision': 'Saneamiento del dataset, nivel 1 (decision del fundador del 27 sep 2026), criterio 6: los nodos del nucleo inalcanzables dentro del nucleo reciben un predecesor del nucleo por lectura.',
                'fecha': '2026-09-27'})
json.dump(ops, io.open('docs/saneamiento/tandas/saneamiento-n1-nucleo.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('entradas', len(ops), '| pares de ida y vuelta rechazados', pares)
