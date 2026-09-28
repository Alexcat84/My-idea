# -*- coding: utf-8 -*-
"""Muestra ciega FINAL de la limpieza M11 (umbral del fundador, 28 sep 2026). Semilla y diseno escritos antes de sortear
en ../m11-claves/umbral_y_semilla_auditoria.json: 50 nodos del pack con las cinco tandas, 2 auditores de 25, 2 trampas
sin marca por auditor en ids reales."""
import json, glob, os, random, re
cfg = json.load(open('../m11-claves/umbral_y_semilla_auditoria.json', encoding='utf-8'))['muestra_final']
rnd = random.Random(cfg['semilla'])
ev = {c['node_id']: c['cita']['evidencia'] for c in json.load(open('tanda_m11_limpieza.json', encoding='utf-8')) if c['veredicto'] == 'RESUMEN'}
ids = sorted(os.path.basename(p)[:-5] for p in glob.glob('copia/primer_equipo/nodos/*.json'))
sel = rnd.sample(ids, cfg['nodos'])
clave = {}
for k in range(cfg['auditores']):
    nn = 'F%d' % (k + 1)
    nodos = []
    for nid in sel[k::cfg['auditores']]:
        n = json.load(open('copia/primer_equipo/nodos/%s.json' % nid, encoding='utf-8'))
        nodos.append({'node_id': nid, 'titulo_concepto': n['titulo_concepto'], 'resumen_teorico': n['resumen_teorico'],
                      'pasos_accionables': list(n['pasos_accionables']), 'entregable_esperado': n['entregable_esperado'],
                      'condiciones_activacion': list(n['condiciones_activacion']), 'evidencia': ev[nid]})
    tipos = ['invencion', 'matiz']
    for tipo in tipos:
        for _ in range(60):
            nd = rnd.choice(nodos)
            if nd['node_id'] in clave:
                continue
            i = rnd.randrange(len(nd['pasos_accionables']))
            p = nd['pasos_accionables'][i]
            if tipo == 'invencion':
                nuevo = p.rstrip('.') + ', porque así se reduce a la mitad el tiempo perdido.'
            else:
                m = re.search(r'\b(puede|pueden|suele|suelen|a menudo|a veces)\b', p)
                if not m:
                    continue
                nuevo = p[:m.start()] + {'puede': 'va a', 'pueden': 'van a', 'suele': 'siempre', 'suelen': 'siempre', 'a menudo': 'siempre', 'a veces': 'siempre'}[m.group(1)] + p[m.end():]
            nd['pasos_accionables'][i] = nuevo
            clave[nd['node_id']] = {'lote': nn, 'campo': 'pasos_accionables[%d]' % i, 'tipo': tipo, 'original': p, 'plantado': nuevo}
            break
    json.dump({'lote': nn, 'nodos': nodos}, open('muestra_final/entrada_%s.json' % nn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'semilla': cfg['semilla'], 'muestra': sel, 'trampas': clave}, open('../m11-claves/muestra_final.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('muestra final: %d nodos, %d trampas sin marca' % (len(sel), len(clave)))
