# -*- coding: utf-8 -*-
"""Reparte los 471 nodos del pack limpio (copia/ con las tres tandas) en 19 lotes de auditoria, con semilla escrita
antes de sortear (../m11-claves/umbral_y_semilla_auditoria.json) y 1 o 2 trampas SIN MARCA por lote, en ids reales."""
import json, glob, os, random, re
sem = json.load(open('../m11-claves/umbral_y_semilla_auditoria.json', encoding='utf-8'))['semilla_reparto_auditoria']
rnd = random.Random(sem)
ev = {c['node_id']: c['cita']['evidencia'] for c in json.load(open('tanda_m11_limpieza.json', encoding='utf-8')) if c['veredicto'] == 'RESUMEN'}
ids = sorted(os.path.basename(p)[:-5] for p in glob.glob('copia/primer_equipo/nodos/*.json'))
rnd.shuffle(ids)
lotes = [ids[i::19] for i in range(19)]
TIPOS = ['matiz', 'invencion', 'calco', 'coherencia']
CAUSAS = [', porque así el equipo rinde el doble.', ', y eso elimina los conflictos para siempre.', ', porque es lo que hacen todas las empresas que crecen.']
CALCOS = [('Revisa', 'Chequea'), ('Pregunta', 'Haz un check de'), ('equipo', 'staff')]
clave = {}
for k, lote in enumerate(lotes, 1):
    nn = '%02d' % k
    nodos = []
    for nid in lote:
        n = json.load(open('copia/primer_equipo/nodos/%s.json' % nid, encoding='utf-8'))
        nodos.append({'node_id': nid, 'titulo_concepto': n['titulo_concepto'], 'resumen_teorico': n['resumen_teorico'],
                      'pasos_accionables': list(n['pasos_accionables']), 'entregable_esperado': n['entregable_esperado'],
                      'condiciones_activacion': list(n['condiciones_activacion']), 'evidencia': ev[nid]})
    for _ in range(rnd.choice([1, 2])):
        tipo = rnd.choice(TIPOS)
        for intento in range(50):
            nd = rnd.choice(nodos)
            if nd['node_id'] in clave:
                continue
            i = rnd.randrange(len(nd['pasos_accionables']))
            p = nd['pasos_accionables'][i]
            if tipo == 'matiz':
                m = re.search(r'\b(puede|pueden|suele|suelen|a menudo|a veces|probablemente)\b', p)
                if not m:
                    continue
                rep = {'puede': 'va a', 'pueden': 'van a', 'suele': '', 'suelen': '', 'a menudo': 'siempre', 'a veces': 'siempre', 'probablemente': 'seguro que'}[m.group(1)]
                nuevo = (p[:m.start()] + rep + p[m.end():]).replace('  ', ' ')
            elif tipo == 'invencion':
                nuevo = p.rstrip('.') + rnd.choice(CAUSAS)
            elif tipo == 'calco':
                a, b = rnd.choice(CALCOS)
                if a not in p:
                    continue
                nuevo = p.replace(a, b, 1)
            else:
                nuevo = p.rstrip('.') + ', como en el tercer punto de la lista anterior.'
            nd['pasos_accionables'][i] = nuevo
            clave[nd['node_id']] = {'lote': nn, 'campo': 'pasos_accionables[%d]' % i, 'tipo': tipo, 'original': p, 'plantado': nuevo}
            break
    json.dump({'lote': nn, 'nodos': nodos}, open('auditoria/entrada_%s.json' % nn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'semilla': sem, 'trampas': clave}, open('../m11-claves/auditoria.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('%d lotes, %d nodos, %d trampas sin marca' % (len(lotes), sum(map(len, lotes)), len(clave)))
