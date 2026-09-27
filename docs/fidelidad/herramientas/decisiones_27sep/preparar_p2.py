# -*- coding: utf-8 -*-
"""Segunda pasada ciega dirigida (decision del fundador del 27 sep, punto 5): los FIEL no releidos de
seguridad y salud (tramo 1) y de legal y dinero (tramo 2), en lotes nuevos P001.. con el mismo formato
que la campania, para wf_trampas.js, mezclar2.py y wf_lectura.js sin tocarlos.

Poblacion:
- VEREDICTOS_TRAMO1.jsonl: todos los FIEL (decidido_por 'lector'). El registro no separa los 109 FIEL que
  el verificador releyo en su muestra (89 siguieron FIEL): se releen todos, y se declara.
- c2/VEREDICTOS_CAMPANIA.jsonl: los FIEL 'lector (FIEL no muestreado)' de los lotes de tramo 1 y 2.
Solo pasos vivos de main cuyo texto no haya cambiado desde la lectura (se comprueba contra dataset/nodos).

Uso: python preparar_p2.py <W2> <repo_fidelidad> <repo_correcciones> [tramos, por defecto 1,2] [prefijo, por defecto P]
La ampliacion al resto de los FIEL (tramo 3) usa tramos=3 y prefijo Q.
"""
import io
import json
import os
import sys

W2, RF, RC = sys.argv[1:4]
TRAMOS = tuple(int(t) for t in (sys.argv[4] if len(sys.argv) > 4 else '1,2').split(','))
PREF = sys.argv[5] if len(sys.argv) > 5 else 'P'
OBJ = 110
C = RF + '/docs/fidelidad/campania'
INV = {x['libro']: x for x in json.load(io.open(RF + '/docs/fidelidad/INVENTARIO_LIBROS.json', encoding='utf-8'))}
PLAN = json.load(io.open(C + '/c2/rastro/plan_lotes.json', encoding='utf-8'))


def ficheros_de(libro, lote=None):
    # nombre del libro tal como lo trae el inventario; si el registro lo escribe distinto, los ficheros del lote original
    if all(l.strip() in INV for l in libro.split(' | ')):
        return [f for l in libro.split(' | ') for f in INV[l.strip()]['texto']]
    return list(PLAN[lote]['ficheros'])


TRAMO_LIBRO = {}


def tramo_de(libro):
    if libro in TRAMO_LIBRO:
        return TRAMO_LIBRO[libro]
    return min(INV[l.strip()]['tramo'] for l in libro.split(' | '))


pob = []
for l in io.open(C + '/VEREDICTOS_TRAMO1.jsonl', encoding='utf-8'):
    x = json.loads(l)
    if 1 in TRAMOS and x['veredicto'] == 'FIEL':
        pob.append((x, 'tramo1_calibrado'))
for l in io.open(C + '/c2/VEREDICTOS_CAMPANIA.jsonl', encoding='utf-8'):
    x = json.loads(l)
    if x['veredicto'] == 'FIEL' and x['decidido_por'].startswith('lector (FIEL') and PLAN[x['id'].split('-')[0]]['tramo'] in TRAMOS:
        pob.append((x, 'campania_tramo%d' % PLAN[x['id'].split('-')[0]]['tramo']))

items, fuera = [], []
for x, origen in pob:
    d = json.load(io.open('%s/dataset/nodos/%s.json' % (RC, x['node_id']), encoding='utf-8'))
    if d.get('deprecado') is True or x['paso'] > len(d['pasos_accionables']):
        fuera.append((x['node_id'], x['paso'], 'no vivo'))
        continue
    idx = x['paso'] - 1
    if any(c.get('campo') == 'pasos_accionables' and c.get('indice') == idx for c in d.get('correcciones', [])):
        fuera.append((x['node_id'], x['paso'], 'ya corregido'))
        continue
    libro = x['libro']
    lote0 = x['id'].split('-')[0]
    if lote0 in PLAN:
        TRAMO_LIBRO.setdefault(libro, PLAN[lote0]['tramo'])
    items.append({'node_id': x['node_id'], 'paso': x['paso'], 'titulo': d.get('titulo_concepto', ''),
                  'resumen': d.get('resumen_teorico', ''), 'texto': d['pasos_accionables'][idx], 'libro': libro,
                  'ficheros': ficheros_de(libro, lote0 if lote0 in PLAN else None), 'origen': origen, 'id_primera_lectura': x['id']})

items.sort(key=lambda it: (tramo_de(it['libro']), it['libro'], it['node_id'], it['paso']))
lotes, cur = [], []
for it in items:
    nuevo_nodo = not cur or cur[-1]['node_id'] != it['node_id']
    cambia_tramo = cur and tramo_de(cur[-1]['libro']) != tramo_de(it['libro'])
    if cur and nuevo_nodo and (len(cur) >= OBJ or cambia_tramo):
        lotes.append(cur)
        cur = []
    cur.append(it)
if cur:
    lotes.append(cur)

os.makedirs(W2 + '/c2/claves', exist_ok=True)
plan, args_tr = {}, {}
for i, lote in enumerate(lotes, 1):
    nombre = PREF + '%03d' % i
    json.dump(lote, io.open('%s/c2/claves/reales_%s.json' % (W2, nombre), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    fs = sorted({f for it in lote for f in it['ficheros']})
    plan[nombre] = {'n': len(lote), 'libros': sorted({it['libro'] for it in lote}), 'ficheros': fs,
                    'tramo': min(tramo_de(it['libro']) for it in lote)}
    args_tr[nombre] = {'ficheros': fs}
json.dump(plan, io.open(W2 + '/c2/plan_lotes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'W': W2.replace('/', '\\'), 'lotes': args_tr, 'conc': 4}, io.open(W2 + '/args_trampas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('poblacion', len(pob), '| a releer', len(items), '| fuera', len(fuera), fuera[:10])
print(len(lotes), 'lotes;', {t: sum(p['n'] for p in plan.values() if p['tramo'] == t) for t in TRAMOS})
import collections
print(collections.Counter(it['origen'] for it in items))
