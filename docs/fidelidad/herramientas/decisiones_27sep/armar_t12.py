# -*- coding: utf-8 -*-
"""Tanda fidelidad-t12: los hallazgos de la ampliacion de la segunda pasada ciega (lotes Q, tramo 3).
Uso (desde my-idea-correcciones): python armar_t12.py <VEREDICTOS_AMPLIACION.jsonl> <p3> <ajustes.json>
ajustes.json: {node_id: texto} para los textos que la sesion retoca (solo tildes u ortografia), declarado en la decision."""
import io
import json
import sys

VER, P3, AJ = sys.argv[1], sys.argv[2], json.load(io.open(sys.argv[3], encoding='utf-8'))


def rel(f):
    return f.replace(chr(92), '/').split('Documents/', 1)[1]


def n(s):
    for a, b in ((chr(0x2019), "'"), (chr(0x2018), "'"), (chr(0x201c), '"'), (chr(0x201d), '"')):
        s = s.replace(a, b)
    return ' '.join(s.split())


hall = [json.loads(l) for l in io.open(VER, encoding='utf-8')]
hall = [x for x in hall if x['veredicto'] in ('CONTRARIO', 'ANADIDO')]
T = []
for i, x in enumerate(sorted(hall, key=lambda x: (x['veredicto'] != 'CONTRARIO', x['node_id'])), 1):
    lote = x['id'].split('-')[0]
    reales = json.load(io.open('%s/c2/claves/reales_%s.json' % (P3, lote), encoding='utf-8'))
    re_ = next(r for r in reales if r['node_id'] == x['node_id'] and r['paso'] == x['paso'])
    trozo = n(x['frase_clave'].split('...')[0])[:60]
    fi = next(f for f in re_['ficheros'] if trozo in n(io.open(f, encoding='utf-8', errors='replace').read()))
    d = json.load(io.open('dataset/nodos/%s.json' % x['node_id'], encoding='utf-8'))
    vigente = d['pasos_accionables'][x['paso'] - 1]
    assert vigente == re_['texto'], x['id']
    if x['veredicto'] == 'CONTRARIO':
        nuevo = AJ.get(x['node_id'], x['texto_fiel'])
        dec = 'Mandato del fundador, regla B, CONTRARIO: version fiel escrita por el verificador o el arbitro, con su cita. '
    elif x.get('tipo_anadido') == 'LEGAL_CIFRA':
        nuevo = AJ.get(x['node_id'], x['texto_fiel'])
        dec = 'Mandato del fundador, regla B, ANADIDO de cifra, plazo, norma o materia legal: quitado o sustituido por lo que dice el libro. '
    else:
        nuevo = AJ.get(x['node_id'], x['texto_sugerencia'])
        dec = 'Mandato del fundador, regla B, ANADIDO practico: reescrito como sugerencia de My Idea sin atribuirlo al autor. '
    dec += ('Decision del fundador del 27 sep, punto 5: la segunda pasada dio contrarios y se amplio al resto de los FIEL no releidos '
            '(lote %s, %s). ' % (lote, x['decidido_por'])) + x['razon']
    if x['node_id'] in AJ:
        dec += ' La sesion solo restituye las tildes que el texto propuesto traia sin ellas.'
    T.append({'node_id': x['node_id'], 'campo': 'pasos_accionables', 'indice': x['paso'] - 1, 'veredicto': x['veredicto'],
              'texto_anterior': vigente, 'texto_nuevo': nuevo,
              'cita': {'libro': x['libro'], 'fichero': rel(fi), 'lineas': x['lineas'], 'frase': x['frase_clave']},
              'decision': dec,
              'auditoria': 'rama fidelidad-total, docs/fidelidad/campania/p3/VEREDICTOS_AMPLIACION.jsonl, id ' + x['id'],
              'id': 'fidelidad-t12-%02d' % i, 'fecha': '2026-09-24'})
for t in T:
    for k in ('texto_nuevo', 'decision'):
        assert chr(0x2014) not in t[k] and chr(0x2013) not in t[k]
    print(t['id'], t['veredicto'], t['node_id'], '|', t['texto_nuevo'][:220])
json.dump(T, io.open('docs/fidelidad/tandas/fidelidad-t12.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
