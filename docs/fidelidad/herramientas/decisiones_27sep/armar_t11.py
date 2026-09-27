# -*- coding: utf-8 -*-
"""Tanda fidelidad-t11: los 5 CONTRARIOS de la segunda pasada ciega (lotes P) y el dato repetido en un resumen.
Uso (desde my-idea-correcciones): python armar_t11.py <contrarios_p2.json>"""
import io
import json
import sys

C = json.load(io.open(sys.argv[1], encoding='utf-8'))


def rel(f):
    return f.replace(chr(92), '/').split('Documents/', 1)[1]


def n(s):
    for a, b in ((chr(0x2019), "'"), (chr(0x2018), "'"), (chr(0x201c), '"'), (chr(0x201d), '"')):
        s = s.replace(a, b)
    return ' '.join(s.split())


AJ = {
    'prospecto_emprendedor_flaming': 'Buscar señales de alerta: cambios frecuentes de empleo, muchos negocios iniciados (con o sin éxito), a menudo desde joven, historial de manejo problemático',
    'decision_fpr': 'Sopesar los factores de incluir un FPR: reduce la exposición legal y le da al candidato información para decidir, frente a un historial poco representativo de lo que logrará un franquiciado o la confidencialidad de tus cifras',
}
T = []
i = 0
for c in sorted(C, key=lambda c: c['node_id']):
    i += 1
    trozo = n(c['frase_clave'].split('...')[0])[:60]
    fi = next(f for f in c['ficheros'] if trozo in n(io.open(f, encoding='utf-8', errors='replace').read()))
    nuevo = AJ.get(c['node_id'], c['texto_fiel'])
    dec = ('Mandato del fundador, regla B, CONTRARIO: version fiel escrita por el verificador o el arbitro, con su cita. '
           'Decision del fundador del 27 sep, punto 5: segunda pasada ciega dirigida sobre los FIEL no releidos de seguridad y salud, '
           'legal y dinero (lote %s, %s). ' % (c['id'].split('-')[0], c['decidido_por'])) + c['razon']
    if c['node_id'] == 'prospecto_emprendedor_flaming':
        dec += ' La sesion solo restituye las tildes y la enie que el texto del verificador traia sin ellas.'
    if c['node_id'] == 'decision_fpr':
        dec += (' La sesion ajusta el texto del arbitro, que traia "facilita la venta": el libro lo desmiente (L2052, "no significant '
                'correlation between the use of an FPR and speed of growth"; L4695). Queda con los dos beneficios que el libro si da '
                '(L4715, informacion para el candidato; L4717, menos exposicion legal) y dos de las razones para no usarlo (L4719). '
                'Anotado en EXCEPCIONES para que el fundador lo ratifique.')
    T.append({'node_id': c['node_id'], 'campo': 'pasos_accionables', 'indice': c['paso'] - 1, 'veredicto': 'CONTRARIO',
              'texto_anterior': c['texto_vigente'], 'texto_nuevo': nuevo,
              'cita': {'libro': c['libro'], 'fichero': rel(fi), 'lineas': c['lineas'], 'frase': c['frase_clave']},
              'decision': dec,
              'auditoria': 'rama fidelidad-total, docs/fidelidad/campania/p2/VEREDICTOS_SEGUNDA_PASADA.jsonl, id ' + c['id'],
              'id': 'fidelidad-t11-%02d' % i, 'fecha': '2026-09-24'})
d = json.load(io.open('dataset/nodos/entrega_por_partes_para_exponer_el_riesgo.json', encoding='utf-8'))
r = d['resumen_teorico']
viejo = 'una cada semana o par de semanas'
assert r.count(viejo) == 1
base = [t for t in T if t['node_id'] == 'entrega_por_partes_para_exponer_el_riesgo'][0]
i += 1
T.append({'node_id': base['node_id'], 'campo': 'resumen_teorico', 'indice': None, 'veredicto': 'CONTRARIO', 'texto_anterior': r,
          'texto_nuevo': r.replace(viejo, 'una cada semana, más o menos'), 'cita': base['cita'],
          'decision': ('Mandato del fundador, dato repetido en el resumen del mismo nodo: el resumen repetia el plazo "cada semana o par '
                       'de semanas", que el libro fija en "at least enough to schedule a new version every week or so" (L1576). Se '
                       'corrige con la misma cita que ' + base['id'] + '.'),
          'auditoria': base['auditoria'], 'id': 'fidelidad-t11-%02d' % i, 'fecha': '2026-09-24'})
print('posicion del cambio en el resumen:', r.find(viejo))
for t in T:
    for k in ('texto_nuevo', 'decision'):
        assert chr(0x2014) not in t[k] and chr(0x2013) not in t[k]
    print(t['id'], t['node_id'], t['campo'], '|', t['texto_nuevo'][:200], '|', t['cita']['fichero'])
json.dump(T, io.open('docs/fidelidad/tandas/fidelidad-t11.json', 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
