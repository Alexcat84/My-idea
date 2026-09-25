# -*- coding: utf-8 -*-
"""Convierte decisiones de la regla B (LEGAL_CIFRA / PRACTICO) en una tanda del aplicador; las EXCEPCION van aparte.

Uso: python decisiones_a_tanda.py <items.json> <decisiones.json|workflow.output> <repo> <tanda_id> <fecha> <salida_tanda.json> <salida_excepciones.json>
"""
import io
import json
import os
import re
import sys

items_p, dec_p, repo, tanda_id, fecha, sal_t, sal_e = sys.argv[1:8]
items = {x['id']: x for x in json.load(io.open(items_p, encoding='utf-8'))}
d = json.load(io.open(dec_p, encoding='utf-8'))
decis = d['result'] if isinstance(d, dict) and 'result' in d else d


def cita(it):
    m = re.match(r'\s*(L\d+(?:\s*-\s*L?\d+)?)\s*:?\s*"?(.*?)"?\s*$', it['cita'], re.S)
    f = it['libro_fichero'].replace('\\', '/')
    f = f.split('Documents/', 1)[1] if 'Documents/' in f else f
    return {'libro': os.path.basename(f).rsplit('.', 1)[0], 'fichero': f,
            'lineas': m.group(1).replace(' ', '') if m else '', 'frase': (m.group(2) if m else it['cita']).strip()}


tanda, excep, vigente, n = [], [], {}, 0
for dc in decis:
    it = items[dc['id']]
    if dc['tipo_anadido'] == 'EXCEPCION' or not dc.get('texto_final'):
        excep.append({'id': dc['id'], 'ficha': it['ficha'], 'node_id': it['node_id'], 'campo': it['campo'], 'indice': it['indice'],
                      'texto_actual': it['texto_actual'], 'motivo': dc['motivo'], 'cita': it['cita']})
        continue
    nodo = json.load(io.open('%s/dataset/nodos/%s.json' % (repo, it['node_id']), encoding='utf-8'))
    regla = ('regla B, ANADIDO de cifra, plazo, norma o materia legal: se quita o se reemplaza por lo que dice el libro'
             if dc['tipo_anadido'] == 'LEGAL_CIFRA' else
             'regla B, ANADIDO practico: se reescribe como sugerencia de My Idea, sin atribuirlo al autor')
    n += 1
    c = {'id': '%s-%02d' % (tanda_id, n), 'fecha': fecha, 'node_id': it['node_id'], 'campo': it['campo'],
         'veredicto': 'ANADIDO', 'texto_anterior': it['texto_actual'], 'texto_nuevo': dc['texto_final'], 'cita': cita(it),
         'decision': 'Mandato del fundador, %s (%s). %s' % (regla, dc['tipo_anadido'], dc['motivo']),
         'auditoria': it['ficha']}
    if it['campo'] == 'pasos_accionables':
        c['indice'] = it['indice']
    tanda.append(c)
    for s in dc.get('segmentos') or []:
        campo = s['campo']
        actual = vigente.setdefault((it['node_id'], campo), nodo.get(campo))
        if not isinstance(actual, str) or s['viejo'] not in actual:
            excep.append({'id': dc['id'] + '/' + campo, 'ficha': it['ficha'], 'node_id': it['node_id'], 'campo': campo,
                          'texto_actual': actual, 'motivo': 'segmento propuesto que no esta literal en el campo vigente: %r' % s['viejo'][:120],
                          'cita': it['cita']})
            continue
        n += 1
        nuevo = actual.replace(s['viejo'], s['nuevo'], 1)
        tanda.append({'id': '%s-%02d' % (tanda_id, n), 'fecha': fecha, 'node_id': it['node_id'], 'campo': campo,
                      'veredicto': 'ANADIDO', 'texto_anterior': actual, 'texto_nuevo': nuevo, 'cita': cita(it),
                      'decision': 'Mandato del fundador, %s: dato repetido en el campo %s del nodo; se cambia solo el segmento.' % (regla, campo),
                      'auditoria': it['ficha']})
        vigente[(it['node_id'], campo)] = nuevo
io.open(sal_t, 'w', encoding='utf-8', newline='\n').write(json.dumps(tanda, ensure_ascii=False, indent=2) + '\n')
io.open(sal_e, 'w', encoding='utf-8', newline='\n').write(json.dumps(excep, ensure_ascii=False, indent=2) + '\n')
tipos = {}
for dc in decis:
    tipos[dc['tipo_anadido']] = tipos.get(dc['tipo_anadido'], 0) + 1
print('decisiones', len(decis), tipos, '| correcciones', len(tanda), '| excepciones', len(excep))
