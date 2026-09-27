# -*- coding: utf-8 -*-
"""Pasada F del saneamiento (TANDA 2, punto 8, decision del fundador del 26 sep 2026): la FASE de los nodos vivos
marcados validacion o ideacion, con el metodo calibrado de la pasada M (misma vara), lector con trampas, verificador
ciego y arbitro. Solo lectura del repo. Prepara los lotes ciegos y sus claves.

Trampas, dos por lote, sobre nodos FUERA del universo (planificacion o ejecucion):
  FASE_MAL: el nodo se muestra con una fase de las del universo que no le toca (tiene que salir marcado);
  FASE_BIEN: el nodo se muestra con su fase verdadera (no tiene que salir marcado: mide el exceso de celo).

Uso: python preparar_F.py <repo> <W>"""
import glob
import hashlib
import io
import json
import os
import random
import sys

REPO, W = sys.argv[1], sys.argv[2]
SEMILLA = 20260928
TAM = 30
nodos = {}
for p in glob.glob(os.path.join(REPO, 'dataset/nodos/*.json')):
    n = json.load(io.open(p, encoding='utf-8'))
    if not n.get('deprecado'):
        nodos[n['node_id']] = n
universo = sorted(k for k, n in nodos.items() if n['fase_proyecto'] in ('validacion', 'ideacion'))
fuera = sorted(k for k, n in nodos.items() if n['fase_proyecto'] in ('planificacion', 'ejecucion'))
orden = universo[:]
random.Random(SEMILLA).shuffle(orden)
N = (len(orden) + TAM - 1) // TAM
lotes = {'F%02d' % (i + 1): orden[i::N] for i in range(N)}


def bloque(cid, n, fase):
    pasos = '\n'.join('  %d. %s' % (i + 1, p) for i, p in enumerate(n.get('pasos_accionables') or []))
    cond = '\n'.join('  - %s' % c for c in n.get('condiciones_activacion') or [])
    return ('### %s\n- fase: %s\n- dominio: %s\n- titulo: %s\n- resumen: %s\n- pasos:\n%s\n- entregable: %s\n'
            '- condiciones:\n%s\n' % (cid, fase, n['dominio'], n['titulo_concepto'], n['resumen_teorico'], pasos,
                                      n.get('entregable_esperado') or '', cond))


os.makedirs(os.path.join(W, 'F', 'lotes'), exist_ok=True)
os.makedirs(os.path.join(W, 'F', 'claves'), exist_ok=True)
args = {}
usados = set()
for l, ids in sorted(lotes.items()):
    az = random.Random(int(hashlib.sha256(('F' + l).encode()).hexdigest()[:8], 16))
    items = [(k, nodos[k]['fase_proyecto'], None) for k in ids]
    for tipo in ('FASE_MAL', 'FASE_BIEN'):
        k = az.choice([x for x in fuera if x not in usados])
        usados.add(k)
        verdad = nodos[k]['fase_proyecto']
        fase = az.choice(['validacion', 'ideacion']) if tipo == 'FASE_MAL' else verdad
        items.append((k, fase, tipo))
    az.shuffle(items)
    mapa, texto, trampas = {}, ['# Lote %s: %d nodos\n' % (l, len(items))], {}
    for i, (k, fase, tipo) in enumerate(items, 1):
        cid = '%s-%03d' % (l, i)
        mapa[cid] = {'nodo': k, 'fase_mostrada': fase, 'trampa': tipo, 'fase_verdadera': nodos[k]['fase_proyecto']}
        texto.append(bloque(cid, nodos[k], fase))
        if tipo:
            trampas[cid] = tipo
    io.open(os.path.join(W, 'F', 'lotes', 'lote_%s.md' % l), 'w', encoding='utf-8').write('\n'.join(texto))
    json.dump(mapa, io.open(os.path.join(W, 'F', 'claves', 'mapa_%s.json' % l), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    args[l] = {'n': len(items), 'trampas': trampas}
json.dump({'semilla': SEMILLA, 'universo': len(universo), 'lotes': args},
          io.open(os.path.join(W, 'F', 'args.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('universo', len(universo), '| validacion', sum(1 for k in universo if nodos[k]['fase_proyecto'] == 'validacion'),
      '| ideacion', sum(1 for k in universo if nodos[k]['fase_proyecto'] == 'ideacion'), '| lotes', N)
