# -*- coding: utf-8 -*-
"""Tanda de ENTRADAS del saneamiento (TANDA 2, punto 7): cada nodo cuya unica entrada era una arista rancia recibe el
predecesor que eligio la pasada E (dos lectores ciegos y arbitro). E-12 se decidio sobre una lista ampliada de 20
candidatos, por un lector, porque en la de 8 ninguno servia. Uso: python tanda_entradas_t2.py <repo> <resultado E> <claves E>"""
import io
import json
import os
import sys

REPO, RES, CLAVES = sys.argv[1], sys.argv[2], sys.argv[3]
os.chdir(REPO)
res = json.load(io.open(RES, encoding='utf-8'))
claves = json.load(io.open(CLAVES, encoding='utf-8'))
AMPLIADO = {'E-12': ('recursos_ecosistema_emprendedor', 'Despues de mapear los recursos del ecosistema emprendedor, lo natural es preguntarse por que esos ecosistemas se concentran en ciertas geografias y como se forma una comunidad asi.', 'un lector sobre la lista ampliada de 20 candidatos')}
ops = []
for x in sorted(res, key=lambda x: x['id']):
    eleccion, nota, quien = x['eleccion'], x['nota'], x['decidido_por']
    if x['id'] in AMPLIADO:
        eleccion, nota, quien = AMPLIADO[x['id']]
    if eleccion == 'NINGUNO':
        raise SystemExit('%s sin predecesor' % x['id'])
    punta = claves[x['id']]['punta']
    ops.append({'id': 't2-entrada-%02d' % (len(ops) + 1), 'operacion': 'TEJER', 'desde': eleccion, 'hacia': punta,
                'motivo': nota.replace(chr(0x2014), ',').replace(chr(0x2013), '-'),
                'evidencia': 'Pasada E del saneamiento (%s, %s): su unica entrada era una arista rancia que sale en saneamiento-t2-aristas.' % (x['id'], quien),
                'decision': 'Saneamiento del dataset, TANDA 2, punto 7 (decision del fundador del 26 sep 2026): ningun nodo se queda sin camino al quitar una arista rancia.',
                'fecha': '2026-09-26'})
json.dump(ops, io.open('docs/saneamiento/tandas/saneamiento-t2-entradas.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('entradas', len(ops))
