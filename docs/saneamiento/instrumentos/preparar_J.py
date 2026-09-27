# -*- coding: utf-8 -*-
"""Pasada J (VIGENCIA Y JURISDICCION) del diagnostico de saneamiento: prepara lotes y bases de trampa.
Universo: los candidatos de la criba lexica (criba.json) mas una MUESTRA CIEGA de 1 de cada 10 no marcados
(semilla 20260926), para medir lo que la criba se deja. Catalogo vivo de My-idea + mundo 11 (forja + bandeja).
Uso: python preparar_J.py <repo> <forja> <W>"""
import glob
import hashlib
import io
import json
import os
import random
import sys

REPO, FORJA, W = sys.argv[1], sys.argv[2], sys.argv[3]
SEMILLA = 20260926
TAM = 45
for d in ('J/reales', 'J/lotes', 'J/claves'):
    os.makedirs(os.path.join(W, d), exist_ok=True)

nodos = {}
for p in glob.glob(os.path.join(REPO, 'dataset/nodos/*.json')):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nodos[n['node_id']] = {'id': n['node_id'], 'mundo': n['dominio'], 'titulo': n['titulo_concepto'],
                               'resumen': n['resumen_teorico'], 'pasos': n.get('pasos_accionables') or [],
                               'entregable': n.get('entregable_esperado') or '',
                               'condiciones': n.get('condiciones_activacion') or []}
for l in io.open(os.path.join(FORJA, 'dataset/nodos.jsonl'), encoding='utf-8'):
    if l.strip():
        n = json.loads(l)
        ca = n.get('condiciones_activacion') or []
        nodos[n['id']] = {'id': n['id'], 'mundo': 'mundo11', 'titulo': n['titulo'], 'resumen': n['resumen_teorico'],
                          'pasos': n.get('pasos_accionables') or [], 'entregable': n.get('entregable_esperado') or '',
                          'condiciones': ca if isinstance(ca, list) else [ca]}
for p in glob.glob(os.path.join(FORJA, 'cuarentena/marquet_turn_the_ship/*.json')):
    n = json.load(io.open(p, encoding='utf-8'))
    ca = n.get('condiciones_activacion') or []
    k = n.get('id') or os.path.basename(p)[:-5]
    nodos[k] = {'id': k, 'mundo': 'mundo11_bandeja', 'titulo': n.get('titulo', ''), 'resumen': n.get('resumen_teorico', ''),
                'pasos': n.get('pasos_accionables') or [], 'entregable': n.get('entregable_esperado') or '',
                'condiciones': ca if isinstance(ca, list) else [ca]}

criba = json.load(io.open(os.path.join(W, 'criba.json'), encoding='utf-8'))
marcados = sorted(f['id'] for f in criba if f['vigencia'] or f['paises'])
no_marcados = sorted(f['id'] for f in criba if not (f['vigencia'] or f['paises']))
azar = random.Random(SEMILLA)
muestra = sorted(azar.sample(no_marcados, len(no_marcados) // 10))
universo = [k for k in marcados + muestra if k in nodos]
azar.shuffle(universo)
n_lotes = -(-len(universo) // TAM)
lotes = {'J%02d' % (i + 1): universo[i::n_lotes] for i in range(n_lotes)}
for lote, ids in lotes.items():
    json.dump([nodos[k] for k in ids], io.open(os.path.join(W, 'J/reales', lote + '.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
json.dump({'marcados': marcados, 'muestra_no_marcados': muestra}, io.open(os.path.join(W, 'J/universo.json'), 'w', encoding='utf-8'))

# bases de trampa: 3 por lote, sobre nodos SIN PAIS NI VIGENCIA de la criba que no estan en ningun lote
libres = [k for k in no_marcados if k not in set(muestra) and k in nodos]
tipos = ['PAIS_SIN_CLASE', 'NORMA_O_PLAZO_DATADO', 'ENLACE_O_INSTITUCION']
bases = []
nombres = sorted(lotes)
for i, lote in enumerate(nombres):
    az = random.Random(int(hashlib.sha256(('J' + lote).encode()).hexdigest()[:8], 16))
    for t in tipos:
        k = az.choice(libres)
        libres.remove(k)
        bases.append(dict(nodos[k], clave='%s-%s' % (lote, t), lote=lote, tipo=t))
json.dump(bases, io.open(os.path.join(W, 'J/bases_trampa.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('universo', len(universo), '(marcados', len(marcados), '+ muestra ciega de no marcados', len(muestra), ')')
print('lotes', len(lotes), 'de', TAM, 'aprox | bases de trampa', len(bases))
