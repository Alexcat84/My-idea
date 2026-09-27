# -*- coding: utf-8 -*-
"""Arma una tanda del aplicador con las correcciones decididas de un bloque y sus datos repetidos.

Uso: python armar_tanda.py <decision.json> <repetidos.output|-> <repo_correcciones> <tanda_id> <fecha> <salida.json> <excepciones_extra.json>
Orden: CONTRARIOS primero. Un segmento repetido cuyo texto viejo no este literal en el campo vigente va a excepciones.
"""
import io
import json
import sys

dec_p, rep_p, repo, tanda_id, fecha, salida, exc_p = sys.argv[1:8]
dec = json.load(io.open(dec_p, encoding='utf-8'))['correcciones']
segs = []
if rep_p != '-':
    o = json.load(io.open(rep_p, encoding='utf-8'))
    segs = o['result'] if isinstance(o, dict) else o
por_ficha = {}
for s in segs:
    por_ficha.setdefault(s['ficha_id'], []).append(s)
orden = {'CONTRARIO': 0, 'ANADIDO': 1}
dec.sort(key=lambda d: (orden[d['veredicto']], d['ficha_id']))
tanda, excep, vigente, n = [], [], {}, 0


def valor(nodo, campo, indice):
    return nodo['pasos_accionables'][indice] if campo == 'pasos_accionables' else nodo.get(campo)


for d in dec:
    nodo = json.load(io.open('%s/dataset/nodos/%s.json' % (repo, d['node_id']), encoding='utf-8'))
    clave = (d['node_id'], 'pasos_accionables', d['indice'])
    actual = vigente.get(clave, d['texto_anterior'])
    if actual != d['texto_anterior']:
        excep.append({'ficha_id': d['ficha_id'], 'motivo': 'el paso ya lo cambio otra correccion de esta tanda'})
        continue
    n += 1
    c = {k: d[k] for k in ('node_id', 'campo', 'indice', 'veredicto', 'texto_anterior', 'texto_nuevo', 'cita', 'decision', 'auditoria')}
    c.update({'id': '%s-%03d' % (tanda_id, n), 'fecha': fecha})
    tanda.append(c)
    vigente[clave] = d['texto_nuevo']
    for s in por_ficha.get(d['ficha_id'], []):
        idx = int(s['indice']) if s['campo'] == 'pasos_accionables' and s.get('indice') is not None else None
        clave_s = (d['node_id'], s['campo'], idx)
        act = vigente.get(clave_s, valor(nodo, s['campo'], idx) if (s['campo'] != 'pasos_accionables' or idx is not None) else None)
        if not isinstance(act, str) or s['viejo'] not in act or s['viejo'] == s['nuevo']:
            excep.append({'ficha_id': d['ficha_id'], 'campo': s['campo'], 'motivo': 'segmento repetido no literal en el campo vigente: %r' % s['viejo'][:120]})
            continue
        n += 1
        nuevo = act.replace(s['viejo'], s['nuevo'], 1)
        e = {'id': '%s-%03d' % (tanda_id, n), 'fecha': fecha, 'node_id': d['node_id'], 'campo': s['campo'],
             'veredicto': d['veredicto'], 'texto_anterior': act, 'texto_nuevo': nuevo, 'cita': d['cita'],
             'decision': 'Mandato del fundador, dato repetido en el nodo (%s): %s' % (s['campo'], s['motivo']),
             'auditoria': d['auditoria']}
        if idx is not None:
            e['indice'] = idx
        tanda.append(e)
        vigente[clave_s] = nuevo
io.open(salida, 'w', encoding='utf-8', newline='\n').write(json.dumps(tanda, ensure_ascii=False, indent=2) + '\n')
io.open(exc_p, 'w', encoding='utf-8', newline='\n').write(json.dumps(excep, ensure_ascii=False, indent=2) + '\n')
print('%s: %d correcciones (CONTRARIO %d) | %d a excepciones' % (tanda_id, len(tanda), sum(1 for c in tanda if c['veredicto'] == 'CONTRARIO'), len(excep)))
