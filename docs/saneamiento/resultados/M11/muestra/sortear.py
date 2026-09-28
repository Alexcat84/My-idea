# -*- coding: utf-8 -*-
"""Muestra ciega de la limpieza M11: 25 nodos del pack limpio, semilla escrita antes de sortear
(../m11-claves/muestra_semilla.json), con 3 trampas SIN MARCA (el id es el del nodo real)."""
import json, glob, os, random, re
sem = json.load(open('../m11-claves/muestra_semilla.json'))['semilla']
rnd = random.Random(sem)
ev = {c['node_id']: c['cita']['evidencia'] for c in json.load(open('tanda_m11_limpieza.json', encoding='utf-8')) if c['veredicto'] == 'RESUMEN'}
ids = sorted(os.path.basename(p)[:-5] for p in glob.glob('copia/primer_equipo/nodos/*.json'))
sel = rnd.sample(ids, 25)


def lineas(f, l):
    todas = open('../forja-lectura/' + f, encoding='utf-8').read().splitlines()
    nums = [int(x) for x in re.findall(r'\d+', l)]
    a, b = max(1, min(nums) - 1), min(len(todas), max(nums) + 1)
    b = min(b, a + 80)
    return "\n".join("%d: %s" % (i, todas[i - 1]) for i in range(a, b + 1))


nodos = []
for nid in sel:
    n = json.load(open('copia/primer_equipo/nodos/%s.json' % nid, encoding='utf-8'))
    e = ev[nid]
    nodos.append({'node_id': nid, 'titulo_concepto': n['titulo_concepto'], 'resumen_teorico': n['resumen_teorico'],
                  'pasos_accionables': list(n['pasos_accionables']), 'entregable_esperado': n['entregable_esperado'],
                  'condiciones_activacion': n['condiciones_activacion'], 'evidencia': e, 'lineas_del_libro': lineas(e['fichero'], e['lineas'])})
t1, t2, t3 = rnd.sample(range(25), 3)
clave = {}
r = nodos[t1]['resumen_teorico']
for p, s in [(r'\bpuede ', 'va a '), (r'\ba menudo ', ''), (r'\bsuele ', ''), (r'\balgunos ', 'todos los '), (r'\bpueden ', 'van a ')]:
    if re.search(p, r):
        nodos[t1]['resumen_teorico'] = re.sub(p, s, r, count=1)
        clave[nodos[t1]['node_id']] = {'campo': 'resumen_teorico', 'tipo': 'matiz quitado', 'patron': p}
        break
else:
    nodos[t1]['resumen_teorico'] = r.rstrip('.') + ', y siempre da resultado.'
    clave[nodos[t1]['node_id']] = {'campo': 'resumen_teorico', 'tipo': 'certeza anadida'}
k = rnd.randrange(len(nodos[t2]['pasos_accionables']))
nodos[t2]['pasos_accionables'][k] = nodos[t2]['pasos_accionables'][k].rstrip('.') + ', porque así la gente se compromete el doble con el resultado.'
clave[nodos[t2]['node_id']] = {'campo': 'pasos_accionables[%d]' % k, 'tipo': 'causa y cifra inventadas'}
k3 = rnd.randrange(len(nodos[t3]['pasos_accionables']))
nodos[t3]['pasos_accionables'][k3] = nodos[t3]['pasos_accionables'][k3].rstrip('.') + ' y pide feedback al terminar.'
clave[nodos[t3]['node_id']] = {'campo': 'pasos_accionables[%d]' % k3, 'tipo': 'ingles (feedback)'}
json.dump({'nodos': nodos}, open('muestra/entrada.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'semilla': sem, 'muestra': sel, 'trampas': clave}, open('../m11-claves/muestra.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('muestra de %d nodos, %d trampas sin marca' % (len(nodos), len(clave)))
